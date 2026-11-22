# Database Project — Archived Coursework & Database Design

**Database systems · Academic project · Portfolio archive**

[![Archive validation](https://github.com/MD-IKRAM169/Database-Project/actions/workflows/archive-validation.yml/badge.svg)](https://github.com/MD-IKRAM169/Database-Project/actions/workflows/archive-validation.yml)

This repository preserves the original **[Database Project.zip](Database%20Project.zip)** from June 2020. The original GitHub history contains one ZIP archive rather than browsable SQL scripts or application source files. This update makes the archive discoverable, documents how to inspect it safely and adds integrity checks **without rewriting the historical project**.

> **Scope:** The ZIP's internal contents have not yet been independently reviewed for this portfolio update. This README deliberately does not guess its DBMS, schema, programming language, entity-relationship model, or application features. See the original archive before making claims about them in a résumé.

## Access the original project

**[Download the original Database Project archive](Database%20Project.zip)**

For a member listing without extraction or execution:

```bash
python tools/archive_audit.py --archive "Database Project.zip"
```

To validate ZIP checksums, path safety, entry limits and encryption status:

```bash
python tools/archive_audit.py --archive "Database Project.zip" --verify
```

To create a machine-readable archive manifest:

```bash
python tools/archive_audit.py --archive "Database Project.zip" --out outputs/archive_manifest.json
```

The audit uses only Python's standard library. It never extracts files, executes archived code or connects to databases; generated reports are ignored by Git.

## Repository overview

| File or directory | Purpose |
| --- | --- |
| [`Database Project.zip`](Database%20Project.zip) | Original historical project archive, unchanged |
| [`tools/archive_audit.py`](tools/archive_audit.py) | Read-only member inventory, structural checks and JSON manifest |
| [`tests/`](tests/) | Offline safety and functionality tests for archive handling |
| [`docs/PROJECT_REVIEW.md`](docs/PROJECT_REVIEW.md) | Evidence-first instructions for describing the project |
| [`docs/PORTFOLIO_CHECKLIST.md`](docs/PORTFOLIO_CHECKLIST.md) | Next steps for a browsable database portfolio |
| [GitHub Actions workflow](.github/workflows/archive-validation.yml) | Automated archive and tool checks |

## Run the checks

```bash
python -m unittest discover -s tests -v
python tools/archive_audit.py --archive "Database Project.zip" --verify
```

These checks assess ZIP structure and accessibility. They **do not validate database quality, SQL correctness, or application reproducibility**. GitHub may not identify the repository's main programming language until actual source files are published separately.

## Future engineering portfolio work

After inspecting the ZIP, the next priority is to publish the original SQL/DDL, schema diagram, queries, and any application source code in browsable folders, subject to privacy and redistribution rights. Add a verified database setup guide and test suite based on the actual technologies. See the [project review guide](docs/PROJECT_REVIEW.md).

## Provenance and attribution

The original archive dates to **2020**. This README and validation tooling are a **later portfolio-maintenance update** and not an altered academic submission or independently reproduced database implementation. Review the ZIP for private credentials, personal data and third-party assets before extracting or republishing any member files. No license for the historical materials has been assumed.

**Maintainer:** [MD-IKRAM169](https://github.com/MD-IKRAM169)
