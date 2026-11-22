"""Hermetic ZIP tests with fictional contents; never modify the original project."""
from __future__ import annotations
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
import warnings
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.archive_audit import ArchiveAuditError, audit_archive


class ArchiveAuditTests(unittest.TestCase):
    def test_valid_zip_with_crc(self):
        with TemporaryDirectory() as d:
            archive = Path(d) / "sample.zip"
            with ZipFile(archive, "w") as z:
                z.writestr("schema.sql", "CREATE TABLE example (id INTEGER);\n")
                z.writestr("README.txt", "fictional sample")
            result = audit_archive(archive, verify=True)
            self.assertEqual(result["member_count"], 2)
            self.assertTrue(result["crc_verified"])
            self.assertEqual(result["entries"][0]["path"], "schema.sql")

    def test_rejects_parent_traversal(self):
        with TemporaryDirectory() as d:
            archive = Path(d) / "bad.zip"
            with ZipFile(archive, "w") as z:
                z.writestr("../secrets.txt", "dummy")
            with self.assertRaisesRegex(ArchiveAuditError, "escapes"):
                audit_archive(archive)

    def test_rejects_windows_drive(self):
        with TemporaryDirectory() as d:
            archive = Path(d) / "bad.zip"
            with ZipFile(archive, "w") as z:
                z.writestr("C:/private.txt", "dummy")
            with self.assertRaisesRegex(ArchiveAuditError, "drive"):
                audit_archive(archive)

    def test_missing_zip(self):
        with TemporaryDirectory() as d:
            with self.assertRaisesRegex(ArchiveAuditError, "not found"):
                audit_archive(Path(d) / "notfound.zip")

    def test_duplicate_members(self):
        with TemporaryDirectory() as d:
            archive = Path(d) / "duplicate.zip"
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                with ZipFile(archive, "w") as z:
                    z.writestr("a.sql", "one")
                    z.writestr("a.sql", "two")
            with self.assertRaisesRegex(ArchiveAuditError, "Duplicate"):
                audit_archive(archive)


if __name__ == "__main__":
    unittest.main()
