# Database Project | Academic Report Portfolio

**Database design · Research documentation · Academic project (2020)**

[![Document and archive checks](https://github.com/MD-IKRAM169/Database-Project/actions/workflows/archive-validation.yml/badge.svg)](https://github.com/MD-IKRAM169/Database-Project/actions/workflows/archive-validation.yml)

This repository preserves a historical academic database project as an original ZIP archive. The archive contains **one document, `Database Project.pdf`**; it does **not** contain separate SQL scripts or source-code files. The original archive remains unchanged.

This portfolio update adds a navigable README, provenance documentation and repeatable document-integrity checks. It does not modify the original submission or invent an implementation.

## Read the original project

**[Download Database Project.zip](Database%20Project.zip)** — then open the contained `Database Project.pdf`.

The ZIP's structure has been verified in GitHub Actions. The PDF is **18 pages** and has extractable text on all 18 pages. Its stored uncompressed size is **1,928,284 bytes**. No archived SQL source files are available separately for browsing on GitHub.

## Verified contents

| Item | Verified information |
| --- | --- |
| Original GitHub artifact | [`Database Project.zip`](Database%20Project.zip) |
| Files in archive | **1** |
| Internal file | `Database Project.pdf` |
| Internal PDF size | **1,928,284 bytes** |
| ZIP CRC verification | Passed in automated tests |
| PDF page count | **18** |
| Pages with extractable text | **18 of 18** |
| Standalone source code | Not present in the ZIP |
| Repository origin | June 2020 |
| Original database engine and project domain | Not yet established by a full reading of the report |

The archive and its member list have been checked directly using the GitHub Actions run; see the [validation workflow](.github/workflows/archive-validation.yml). **ZIP integrity is not a review of the report's academic or technical correctness.**

## Explore the project locally

Python 3.10+ is recommended.

```bash
# List ZIP members without extracting or executing anything
python tools/archive_audit.py --archive "Database Project.zip"

# Validate paths, entry limits, encryption status and CRC checksums
python tools/archive_audit.py --archive "Database Project.zip" --verify

# Export a local JSON manifest of the archive's contents
python tools/archive_audit.py --archive "Database Project.zip" --out outputs/archive_manifest.json

# Run offline unit tests
python -m unittest discover -s tests -v
```

To open the report, extract `Database Project.pdf` locally after reviewing its contents and scanning the downloaded archive. The ZIP auditing tool intentionally **does not extract files or run code**.

The optional PDF reader check needs the [pypdf](https://pypi.org/project/pypdf/) package:

```bash
python -m pip install -r requirements-report.txt
python tools/report_audit.py --archive "Database Project.zip"
```

This reads the PDF in memory and reports page and text-accessibility counts without writing or displaying its contents.

## What has been modernized?

| New file / folder | Purpose |
| --- | --- |
| [`README.md`](README.md) | A direct, accurate overview of the historical project |
| [`docs/ARCHIVE_CONTENTS.md`](docs/ARCHIVE_CONTENTS.md) | Verified PDF-only inventory and provenance |
| [`docs/PROJECT_REVIEW.md`](docs/PROJECT_REVIEW.md) | Guidance for a source-grounded technical review |
| [`docs/PORTFOLIO_CHECKLIST.md`](docs/PORTFOLIO_CHECKLIST.md) | Practical future steps |
| [`tools/archive_audit.py`](tools/archive_audit.py) | Read-only ZIP inventory and integrity check |
| [`tools/report_audit.py`](tools/report_audit.py) | In-memory PDF readability and page-count check |
| [`tests/`](tests/) | Eight offline tests using fictional archives and PDF fixtures |
| [GitHub Actions](.github/workflows/archive-validation.yml) | Automated tests and original-archive validation |

## Next steps for a technical portfolio

A document-based project can demonstrate database concepts and research communication, but it should not be presented as a runnable database application without source evidence. A useful next step is to **read the original PDF**, identify the system's actual domain and database design, and produce a faithful technical synopsis. If source SQL and an executable implementation are available elsewhere, they can be reviewed and published separately with permission.

See the [project review guide](docs/PROJECT_REVIEW.md) for what to verify.

## Historical integrity and rights

The 2020 archive is preserved unchanged. The new documentation and automated checks are **subsequent portfolio maintenance**, not part of the historical coursework. Do not assume redistribution rights for embedded diagrams, third-party images, personal records or sample data. No open-source license has been assigned to the original materials.

**Maintainer:** [MD-IKRAM169](https://github.com/MD-IKRAM169)
