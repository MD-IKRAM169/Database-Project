# Research and technical review of the historical project

## Proven repository and archive facts

The repository was created in **June 2020** and originally contained `Database Project.zip` on its `master` branch, with no separate README or license. An automated ZIP audit subsequently verified that the archive contains **one PDF report** named `Database Project.pdf`, not a folder of SQL scripts. Its integrity check succeeded.

A PDF report may document SQL, schemas or diagrams, but these do **not** become reproducible source files simply because they are pictured or described in the report.

## Safe review procedure

1. Keep `Database Project.zip` intact as a historical source.
2. Run `python tools/archive_audit.py --archive "Database Project.zip" --verify`.
3. In an isolated local folder, extract the verified `Database Project.pdf` and review it with an updated PDF reader.
4. Record the report's actual title, author/contributor roles, project goal, DBMS, tables, relationships, queries and conclusions **only where documented**.
5. Check the report for passwords, personal data, third-party material and academic sharing restrictions before republishing excerpts or images.
6. If original SQL or program source exists elsewhere, verify its provenance and shareability before adding it.
7. Add technical documentation and reproducible experiments only when supported by the original project or when clearly marked as a later independent implementation.

## What makes a persuasive database portfolio

A reviewer should be able to understand the real use case, data model, primary/foreign keys, important constraints, queries, and a tested database setup if any was built. Present missing artifacts as limits or future work, never as completed capabilities.

## Provenance

The README, archive audit and CI are **modern additions**. They do not prove the original coursework included these tools or tests. No license for the original project materials has been selected.
