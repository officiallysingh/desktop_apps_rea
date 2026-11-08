---
name: tally-xml-export
description: Read TallyPrime masters, vouchers and reports through Tally's XML-over-HTTP interface (localhost:9000) using Export requests only. Use when analysing TallyPrime data or structure.
---
# Reading TallyPrime via its XML interface (read-only)

TallyPrime keeps data in a proprietary store; its documented XML/HTTP interface is the safe way
to read it. **Export requests only**: never Import, Alter, Delete or Cancel (the guard blocks them).

## Preconditions
- TallyPrime is running with the company open, and its server port is already enabled
  (Help > Settings > Connectivity: "TallyPrime acts as Server", port 9000).
- If it is NOT enabled, do not change the setting yourself: that is a change to the app's
  configuration. Ask the user; it is their decision.

## How to send a request
```bash
curl -s -X POST http://localhost:9000 -H "Content-Type: text/xml" \
  --data-binary @.claude/skills/tally-xml-export/requests/list-of-accounts.xml \
  > _raw/tallyprime/dumps/list-of-accounts.xml
```
- Always write responses to `_raw/tallyprime/dumps/` (real client data). Never print full
  responses into the conversation: summarise structure (tags, counts, distinct values).
- For a date-bounded request, copy the template into `_raw/tallyprime/requests/` and edit
  `SVFROMDATE` / `SVTODATE` (format `YYYYMMDD`) and add `SVCURRENTCOMPANY` if several companies
  are open.
- Keep date ranges small (a month) to avoid long exports on the user's live Tally.

## Templates (`requests/`)
| File | Returns |
| --- | --- |
| `list-of-accounts.xml` | All masters (groups, ledgers, stock items, units, voucher types ...) |
| `day-book.xml` | Vouchers in a date range, with ledger and inventory entries |
| `trial-balance.xml` | Trial balance for the period |
| `stock-summary.xml` | Stock summary report |
| `company-info.xml` | Companies loaded |

The request layout follows Tally's integration documentation. If a request returns an error or
an empty envelope, check the current TallyPrime XML integration docs and adjust (report names
and variables can differ between releases). Inline TDL in a request may define a read-only
collection for specific fields; it must never contain actions that write.

## What to extract
- Master structure -> `tallyprime/02-data-model/` (our names; Tally's field names only in
  `_raw/tallyprime/name-mapping.md`).
- Voucher types and their entry structure -> `tallyprime/04-workflows/`, `05-business-rules/`.
