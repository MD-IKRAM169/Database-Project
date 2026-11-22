#!/usr/bin/env python3
"""Inventory and validate a ZIP without extracting or executing files.

A structural check is not a malware scan and does not assess rights to redistribute.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import stat
import sys
from zipfile import BadZipFile, ZipFile

MAX_ENTRIES = 10000
MAX_TOTAL_UNCOMPRESSED = 2 * 1024**3
MAX_COMPRESSION_RATIO = 1000


class ArchiveAuditError(ValueError):
    """Unsafe or structurally invalid archive."""


def _validate_name(name: str) -> None:
    if not name or "\\" in name or "\x00" in name:
        raise ArchiveAuditError(f"Invalid archive member name: {name!r}")
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or name.startswith("/"):
        raise ArchiveAuditError(f"Archive member escapes extraction root: {name!r}")
    if len(name) >= 2 and name[1] == ":":
        raise ArchiveAuditError(f"Windows drive path is not allowed: {name!r}")


def audit_archive(path: Path, verify: bool = False) -> dict:
    path = Path(path)
    if not path.is_file():
        raise ArchiveAuditError(f"Archive not found: {path}")
    try:
        with ZipFile(path) as archive:
            infos = archive.infolist()
            if not infos:
                raise ArchiveAuditError("ZIP archive contains no members")
            if len(infos) > MAX_ENTRIES:
                raise ArchiveAuditError(f"Too many ZIP members: {len(infos)}")
            names = set()
            total_size = 0
            entries = []
            for info in infos:
                name = info.filename
                _validate_name(name)
                if name in names:
                    raise ArchiveAuditError(f"Duplicate member path: {name!r}")
                names.add(name)
                if info.file_size < 0 or info.compress_size < 0:
                    raise ArchiveAuditError(f"Negative ZIP size: {name!r}")
                total_size += info.file_size
                if total_size > MAX_TOTAL_UNCOMPRESSED:
                    raise ArchiveAuditError("Uncompressed size exceeds safety limit")
                if info.file_size and info.file_size / max(info.compress_size, 1) > MAX_COMPRESSION_RATIO:
                    raise ArchiveAuditError(f"Suspicious compression ratio: {name!r}")
                mode = (info.external_attr >> 16) & 0xFFFF
                if stat.S_IFMT(mode) == stat.S_IFLNK:
                    raise ArchiveAuditError(f"Symbolic link entry: {name!r}")
                if info.flag_bits & 0x01:
                    raise ArchiveAuditError(f"Encrypted ZIP entry: {name!r}")
                entries.append({
                    "path": name,
                    "directory": info.is_dir(),
                    "uncompressed_bytes": info.file_size,
                    "compressed_bytes": info.compress_size,
                })
            if verify:
                for info in infos:
                    if info.is_dir():
                        continue
                    with archive.open(info) as stream:
                        while stream.read(1024 * 1024):
                            pass  # checks CRC; does not extract to disk
    except (BadZipFile, OSError, RuntimeError, EOFError, NotImplementedError) as exc:
        raise ArchiveAuditError(f"Cannot validate ZIP archive: {exc}") from exc
    return {
        "archive": path.name,
        "archive_bytes": path.stat().st_size,
        "member_count": len(entries),
        "uncompressed_bytes": total_size,
        "crc_verified": verify,
        "note": "Structural ZIP audit only; contents and rights require review.",
        "entries": entries,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=Path("Database Project.zip"))
    parser.add_argument("--verify", action="store_true", help="Stream ZIP members to check CRC")
    parser.add_argument("--out", type=Path, help="Optional JSON manifest destination")
    args = parser.parse_args(argv)
    try:
        report = audit_archive(args.archive, verify=args.verify)
    except ArchiveAuditError as exc:
        print(f"Archive validation FAILED: {exc}", file=sys.stderr)
        return 1
    print(f"OK: {report['archive']} | {report['member_count']} entries | "
          f"{report['uncompressed_bytes']:,} uncompressed bytes")
    print("CRC verified" if args.verify else "CRC not checked; pass --verify to verify")
    for entry in report["entries"]:
        print(f"  {entry['path']} ({entry['uncompressed_bytes']:,} bytes)")
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Saved report: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
