"""Offline tests use generated, fictional PDF data only."""
from io import BytesIO
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from zipfile import ZipFile

from pypdf import PdfWriter

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.report_audit import ReportAuditError, inspect_report


class ReportAuditTests(unittest.TestCase):
    @staticmethod
    def _sample_pdf() -> bytes:
        writer = PdfWriter()
        writer.add_blank_page(width=612, height=792)
        stream = BytesIO()
        writer.write(stream)
        return stream.getvalue()

    def test_reads_pdf_without_extracting(self):
        with TemporaryDirectory() as d:
            zip_path = Path(d) / "test.zip"
            with ZipFile(zip_path, "w") as archive:
                archive.writestr("Database Project.pdf", self._sample_pdf())
            result = inspect_report(zip_path)
            self.assertEqual(result["pages"], 1)
            self.assertEqual(result["text_extractable_pages"], 0)

    def test_rejects_missing_pdf(self):
        with TemporaryDirectory() as d:
            zip_path = Path(d) / "wrong.zip"
            with ZipFile(zip_path, "w") as archive:
                archive.writestr("README.txt", "not a report")
            with self.assertRaisesRegex(ReportAuditError, "exactly one PDF"):
                inspect_report(zip_path)

    def test_rejects_false_pdf(self):
        with TemporaryDirectory() as d:
            zip_path = Path(d) / "bad.zip"
            with ZipFile(zip_path, "w") as archive:
                archive.writestr("Database Project.pdf", "not really a pdf")
            with self.assertRaisesRegex(ReportAuditError, "PDF header"):
                inspect_report(zip_path)


if __name__ == "__main__":
    unittest.main()
