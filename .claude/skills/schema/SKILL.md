---
name: schema
description: Extract and document an app database schema read-only (DDL in our names, ER diagram, entity dictionary). Use after inventory.
argument-hint: <app-slug>
---
Document the data model of `$ARGUMENTS`. Follow "Rule zero" and "Real client data" in CLAUDE.md.

1. Read the schema from the DB copy in `_raw/<app>/db-copies/`, or from the live DB read-only
   (`sqlite3 -readonly`, SELECT on `INFORMATION_SCHEMA` / `sys.*` for SQL Server).
   Save the raw schema to `_raw/<app>/dumps/schema-raw.sql`.
2. Profile the data shape: row counts, `SELECT DISTINCT` on code/status/type columns, min/max
   lengths, null ratios → `_raw/<app>/dumps/profile.md`.
3. Build `_raw/<app>/name-mapping.md`: vendor table/column → our domain name.
4. Write `<app>/02-data-model/schema.sql` with OUR names, `er.mmd` (Mermaid erDiagram) and
   `entity-dictionary.md` (purpose, key fields, relationships, capability IDs, enum meanings).
5. Note: financial years, multi-company, soft deletes, audit columns, numbering, tax storage.
6. Update `<app>/PROGRESS.md`.
