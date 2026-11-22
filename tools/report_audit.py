#!/usr/bin/env python3
"""Read an archived PDF *in memory* and report basic document statistics.

This checks PDF readability, not schema correctness, research validity or safety.
No archive members are extracted and no PDF content is printed.
"""
from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path
import sys
from zipfile import BadZipFile, ZipFile

from pypdf import PdfReader

REPORT_NAME = "Database Project.pdf"
MAX_PDF_BYTES = 25 * 1024 * 1024


class ReportAuditError(ValueError):
    """Report missing, too large, encrypted or unreadable."""


def inspect_report(archive_path: Path) -> dict[str, object]:
    archive_path = Path(archive_path)
    if not archive_path.is_file():
        raise ReportAuditError(f"Archive not found: {archive_path}")
    try:
        with ZipFile(archive_path) as archive:
            files = [item for item in archive.infolist() if not item.is_dir()]
            if len(files) != 1 or files[0].filename != REPORT_NAME:
                raise ReportAuditError("Expected exactly one PDF named Database Project.pdf")
            info = files[0]
            if info.file_size == 0 or info.file_size > MAX_PDF_BYTES:
                raise ReportAuditError("Report size outside configured bounds")
            if info.flag_bits & 1:
                raise ReportAuditError("Report is stored in an encrypted ZIP member")
            content = archive.read(info)
    except (OSError, BadZipFile, RuntimeError, NotImplementedError) as exc:
        raise ReportAuditError(f"Cannot read archive: {exc}") from exc
    if not content.startswith(b"%PDF-"):
        raise ReportAuditError("Archived file does not have a PDF header")
    try:
        reader = PdfReader(BytesIO(content), strict=False)
        if reader.is_encrypted:
            raise ReportAuditError("PDF is encrypted")
        page_count = len(reader.pages)
        if page_count < 1:
            raise ReportAuditError("PDF contains no pages")
        readable_text_pages = 0
        for page in reader.pages:
            try:
                if (page.extract_text() or "").strip():
                    readable_text_pages += 1
            except (ValueError, KeyError, TypeError, IndexError):
                # Text extraction can fail for damaged/missing font maps even when
                # the PDF remains viewable in a standard PDF reader.
                pass
    except ReportAuditError:
        raise
    except Exception as exc:
        raise ReportAuditError(f"PDF parser could not read document: {exc}") from exc
    return {
        "pdf_name": REPORT_NAME,
        "pdf_bytes": len(content),
        "pages": page_count,
        "text_extractable_pages": readable_text_pages,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=Path("Database Project.zip"))
    args = parser.parse_args(argv)
    try:
        report = inspect_report(args.archive)
    except ReportAuditError as exc:
        print(f"PDF check FAILED: {exc}", file=sys.stderr)
        return 1
    print(f"PDF check OK: {report['pdf_name']} | {report['pages']} pages | "
          f"{report['pdf_bytes']:,} bytes | "
          f"{report['text_extractable_pages']} page(s) with extractable text")
    print("Document structure only; database design and research contents unreviewed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
