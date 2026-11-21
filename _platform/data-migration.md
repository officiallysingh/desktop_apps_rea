# Data migration from existing apps (IO-MIGRATE)

Goal: a customer on Tally, BUSY, Marg, Bahi-Khata or CompuTax can move to our product in under
an hour, with figures that provably match the old app, and can keep using the old app until
they are confident.

## What to migrate
| Data | Needed for | Notes |
| --- | --- | --- |
| Company profile, GSTIN(s), FY, branches | Setup | One company per source company |
| Chart of accounts (groups, ledgers) with opening balances | Books | Map source groups to our groups (user-reviewed) |
| Parties: name, GSTIN, PAN, state, address, contact, credit limit/days, bank details | Billing, GST, TDS | Dedupe on GSTIN/PAN/phone |
| Items: name, code, unit + alternate units, HSN, GST rate, MRP/rates, price lists, barcode, reorder levels | Billing, inventory | Rates as effective-dated |
| Godowns, batches (mfg/expiry), serials | Inventory, pharma | Marg-type users |
| Closing stock by item × godown × batch, with value | Opening stock | Must match source stock summary |
| **Outstanding bills** (bill-wise receivables/payables with due dates) | Ageing, reminders, interest | Not just party balances |
| Pending orders, delivery challans not invoiced, post-dated cheques | Operations | Optional |
| Vouchers (current FY to date, optionally prior years) | GST returns not yet filed, annual return, comparatives, audit | Mid-year switch needs YTD vouchers |
| TDS data (deductee master, YTD deductions, challans) | Quarterly TDS returns | Mid-year switch |
| CompuTax: client master, assessment history, filed returns metadata | CA practice | Separate edition |

## Cut-over options (user chooses)
1. **Start of financial year** — masters + opening balances + outstanding bills + opening stock.
   Simplest and the default recommendation.
2. **Mid-year** — option 1 as at the FY start + all vouchers of the current FY (so GST returns,
   annual return and TDS returns can be done from our product).
3. **Full history** — all years, for comparatives and audit (read-only archive of prior years).

## Pipeline
```
Extract (connector per source app, on the Windows PC)
  → Stage (neutral JSON in our migration format, versioned)
  → Map (wizard: source groups → our groups, units, tax categories, godowns; saved per company)
  → Validate (balanced vouchers, GSTIN/PAN formats, HSN, missing masters, duplicates)
  → Load (idempotent: re-running replaces the previous load of the same source)
  → Reconcile (our trial balance, stock summary, party outstanding, GST summary vs source reports)
  → Sign-off report (PDF) → go live; optional parallel run
```
- **Reconciliation is the trust feature**: show source vs ours side by side, line by line, with zero
  differences required before go-live (or each difference explained).
- Dry runs are free and repeatable; nothing is final until sign-off.
- Migration never writes to the source app or its data (same rule as our analysis guard).

## Extraction per source (fill in during reverse engineering → `<app>/interop/`)
| Source | Preferred extraction | Fallback |
| --- | --- | --- |
| TallyPrime | Tally's documented XML/HTTP export (masters, vouchers, reports) while Tally runs | Tally's own export to XML/Excel by the user |
| BUSY | App's own export features (to verify) | Read-only read of its database (format documented in `busy/interop/`) |
| Marg ERP | App's own export features (to verify) | Read-only read of its data files |
| Bahi-Khata | App's own export (to verify) | Read-only read of its database |
| CompuTax | App's own export (to verify) | Read-only read of its data |
| Any other app | Our Excel/CSV import templates (masters, opening balances, bills, stock) | — |

## Clean-room and interoperability
- Reading a customer's **own data** from their files, with their consent, to move it to our
  product is interoperability. Knowing the file/database layout is required for that.
- Therefore vendor identifiers (table/column/field names, file formats) are **allowed only in
  `<app>/interop/`** (factual descriptions of data formats needed to read the data). They stay out
  of every other spec and out of the core product code.
- In the product repo, connectors live in a separate `migration-connectors` module that depends on
  the core, never the other way round. Get legal review of connector approach before launch.
- For the customer's own encrypted data, prefer the app's own export path over cracking the
  vendor's protection — it is simpler and keeps the clean-room position clean.

## Product requirements (for the BRD)
- Migration wizard (desktop): detect installed source apps and their companies on this PC
  (read-only), pick company, pick cut-over option, map, validate, load, reconcile.
- Assisted migration mode for partners/CAs: run on the customer's PC, produce the staged file,
  load into the customer's account (cloud) — useful for multi-PC firms.
- Excel/CSV templates + validation for manual migration from any app.
- Migration report retained in the company (audit trail).
