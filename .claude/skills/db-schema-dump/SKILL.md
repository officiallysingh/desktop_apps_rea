---
name: db-schema-dump
description: Read-only queries and commands to dump the schema and data profile of app databases (SQL Server, SQLite, MS Access, Firebird, FoxPro/DBF). Use during /schema or whenever inspecting an app database.
---
# Read-only schema and profile dumps

Rules: read-only connections only; prefer COPIES in `_raw/<app>/db-copies/`; write output to
`_raw/<app>/dumps/`; never `SELECT *` on client tables, profile with counts and distinct codes.
Don't use database MCP servers on this machine: the app guard only sees shell commands.

## SQL Server (live, SELECT only)
```bash
sqlcmd -S .\SQLEXPRESS -E -Q "SELECT name FROM sys.databases"
sqlcmd -S .\SQLEXPRESS -E -d <DB> -W -s"|" -Q "SET NOCOUNT ON; SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION, NUMERIC_SCALE, IS_NULLABLE, COLUMN_DEFAULT FROM INFORMATION_SCHEMA.COLUMNS ORDER BY TABLE_NAME, ORDINAL_POSITION" > _raw/<app>/dumps/columns.txt
sqlcmd -S .\SQLEXPRESS -E -d <DB> -W -s"|" -Q "SET NOCOUNT ON; SELECT fk.name, OBJECT_NAME(fk.parent_object_id) child, COL_NAME(fc.parent_object_id, fc.parent_column_id) child_col, OBJECT_NAME(fk.referenced_object_id) parent, COL_NAME(fc.referenced_object_id, fc.referenced_column_id) parent_col FROM sys.foreign_keys fk JOIN sys.foreign_key_columns fc ON fk.object_id = fc.constraint_object_id" > _raw/<app>/dumps/foreign-keys.txt
sqlcmd -S .\SQLEXPRESS -E -d <DB> -W -s"|" -Q "SET NOCOUNT ON; SELECT t.name, SUM(p.rows) FROM sys.tables t JOIN sys.partitions p ON t.object_id = p.object_id AND p.index_id IN (0,1) GROUP BY t.name ORDER BY 2 DESC" > _raw/<app>/dumps/row-counts.txt
sqlcmd -S .\SQLEXPRESS -E -d <DB> -W -Q "SET NOCOUNT ON; SELECT OBJECT_SCHEMA_NAME(object_id) s, OBJECT_NAME(object_id) n, definition FROM sys.sql_modules" > _raw/<app>/dumps/procs-views-triggers.sql
```
Stored procedures, views and triggers often hold business rules: read them.

## SQLite (copy, or `-readonly`)
```bash
sqlite3 -readonly _raw/<app>/db-copies/<file>.db ".schema" > _raw/<app>/dumps/schema-raw.sql
sqlite3 -readonly _raw/<app>/db-copies/<file>.db "SELECT name FROM sqlite_master WHERE type='table'"
```

## MS Access (.mdb/.accdb), on a COPY
```powershell
$cn = New-Object System.Data.OleDb.OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=_raw\<app>\db-copies\<file>.mdb;Mode=Read")
$cn.Open(); $cn.GetSchema("Columns") | Select TABLE_NAME,COLUMN_NAME,DATA_TYPE,CHARACTER_MAXIMUM_LENGTH,IS_NULLABLE | Export-Csv _raw\<app>\dumps\columns.csv -NoTypeInformation; $cn.Close()
```
Needs the Access Database Engine (use 32-bit PowerShell for 32-bit ACE). Opening even a copy
creates a `.ldb/.laccdb` lock file next to it: fine in `_raw/`, never on the original.

## Firebird (.fdb/.gdb), on a COPY
```bash
isql -user SYSDBA -password <pwd> -x "_raw/<app>/db-copies/<file>.fdb" > _raw/<app>/dumps/schema-raw.sql
```
If the password is unknown, ask the user; never try to bypass it.

## FoxPro / dBase (.dbf), on a COPY
```bash
python -I -c "import sys,dbfread; t=dbfread.DBF(sys.argv[1], load=False); print([(f.name,f.type,f.length,f.decimal_count) for f in t.fields])" _raw/<app>/db-copies/<file>.dbf
```
(`pip install dbfread`; `.cdx/.idx` index and `.fpt` memo files sit next to the `.dbf`.)

## Profiling without reading client rows
- Row counts per table; `SELECT <code_col>, COUNT(*) ... GROUP BY <code_col>` for type/status
  columns; `MIN/MAX(LEN(col))`; null ratios; `MIN/MAX(date_col)`.
- Save to `_raw/<app>/dumps/profile.md`; only the meaning of codes goes into committed specs.
