# Original project archive: review and provenance

## Verified repository facts

The original repository was created in June 2020 and contained one file, `Database Project.zip`, on its `master` branch. It had no top-level README, browsable SQL scripts or declared license when this documentation update was prepared.

The archived project itself must be inspected before describing specific database technology, domain, SQL dialect, table counts, constraints, application code, or accomplishments.

## Safe inspection process

1. Preserve the original archive and work on a separate copy.
2. Run `python tools/archive_audit.py --archive "Database Project.zip" --verify` to check member names and CRCs without extraction.
3. Review the ZIP member list before opening files. Scan files with appropriate security tools in an isolated environment. Structural validation alone does not certify malware safety.
4. Find the actual SQL/DDL scripts, schema diagram, code, reports, data files, dependencies and screenshots.
5. Check for passwords, private credentials, personal data, student identifiers and third-party materials that must not be redistributed.
6. Reconstruct the database with documented versions *only after* confirming the correct database engine and dependencies.
7. Add source-supported technical documentation, test fixtures and project examples as a separate, reviewable improvement.

## For a future portfolio summary

Explain the database's purpose, entities, relationships, normalization rationale, constraints, indexes, sample queries, DBMS version and reproducible setup procedure, **only when backed by the original files**. Separate the features of the original coursework from any modern documentation or refactoring.

## Historical credit

The README and tooling added later are portfolio maintenance, not evidence that archive auditing or GitHub Actions was part of the original 2020 project. No general redistribution license was added to the academic archive.
