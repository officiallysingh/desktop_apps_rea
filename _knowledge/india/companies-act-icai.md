---
topic: Companies Act schedules, audit trail rule, ICAI accounting standards
capabilities: [FA-ASSETS, RPT-FINANCIAL, RPT-ANALYSIS, SYS-AUDIT, SYS-BACKUP, STK-INVENTORY, CRD-UDHAAR]
sources: [CA-2013-SCH-II, CA-2013-SCH-III, CO-ACCTS-RULES, ICAI-AS, ICAI-JOURNAL]
as_of: 2026-11-08
---
# Companies Act, audit trail and Indian Accounting Standards [IN]

## Schedule II — useful lives (Part C, single shift) [bare act via bnblegal.com]
| Asset class | Years |
| --- | --- |
| Buildings RCC frame (non-factory) | 60 |
| Buildings non-RCC (non-factory); factory buildings | 30 |
| Temporary structures | 3 |
| Fences, wells, tube wells | 5 |
| Plant & machinery — general | 15 |
| Plant & machinery — continuous process (general) | 8 |
| Furniture and fittings — general | 10 |
| Furniture in hotels, restaurants, schools etc. | 8 |
| Motorcycles, scooters, mopeds | 10 |
| Motor cars, buses, lorries — used for hire / not for hire | 6 / 8 |
| Electric vehicles; tractors, heavy vehicles | 8 |
| Office equipment | 5 |
| Computers — end-user devices / servers and networks | 3 / 6 |
| Electrical installations and equipment | 10 |
- Part A: residual value normally ≤ 5% of cost; pro-rata depreciation from date of addition / to
  date of disposal; significant components with different lives depreciated separately;
  double shift +50%, triple shift +100% (not for items marked NESD); intangibles follow AS.
  Companies following accounting standards may use different lives/residuals with disclosed
  justification; others may not use longer lives or higher residuals. [Sch. II Part A]

## Audit trail — proviso to Rule 3(1), Companies (Accounts) Rules 2014 [ICAI Journal]
- For financial years from **1 Apr 2023**, every company keeping books in accounting software
  must use software that records an **audit trail of each transaction**, an **edit log of each
  change with the date**, and where the audit trail **cannot be disabled**.
- ICAI guidance: capture what changed (create/modify/delete), when (timestamp), who (user ID),
  which record. Kept as books of account: **8 years**. Fine ₹50,000–₹5 lakh (s.128(6)).
- Auditors report under Rule 11(g) whether the feature existed, operated all year, was not
  tampered with, and was preserved.
- Rule 3(5): electronic books' backups must be kept on servers physically in India, daily. [verify]

## Schedule III — financial statement formats (companies)
- Division I (AS companies), Division II (Ind AS), Division III (NBFCs).
- 2021 amendments add disclosures software should be able to produce: **trade receivables and
  payables ageing** (by buckets from due date: < 6 months, 6–12 months, 1–2, 2–3, > 3 years;
  disputed/undisputed; MSME/others for payables), CWIP ageing, promoter shareholding, and
  **11 ratios** (current, debt-equity, debt service coverage, ROE, inventory turnover, trade
  receivables turnover, trade payables turnover, net capital turnover, net profit, ROCE, return
  on investment) with explanation for > 25% change. [verify against MCA text]
- MSME dues: disclosure of amounts due to micro/small enterprises; under income tax, payments to
  micro/small suppliers beyond the MSMED Act s.15 limit (agreed ≤ 45 days, else 15 days) are
  deductible only when paid (1961 s.43B(h) → 2025 Act s.37(2)(g), confirmed in the Act text).

## ICAI Accounting Standards (non-Ind AS entities) most relevant to SMB software
| AS | Topic | Software impact |
| --- | --- | --- |
| AS 1 | Disclosure of accounting policies | Policy notes |
| AS 2 | Inventories: lower of cost and NRV; FIFO or weighted average (no LIFO) | Valuation settings |
| AS 3 | Cash flow statements | Cash flow report |
| AS 9 | Revenue recognition | Sales timing |
| AS 10 | Property, plant and equipment | Fixed asset register |
| AS 11 | Foreign exchange | Out of scope (India-only) |
| AS 15 | Employee benefits | Payroll provisions (gratuity, leave) |
| AS 19 | Leases | Rarely needed for SMBs |
| AS 22 | Taxes on income (deferred tax) | Company editions |
| AS 26 | Intangible assets | Asset register |
| AS 29 | Provisions and contingencies | Provision ledgers, notes |
- ICAI's Board of Studies publishes free, yearly-updated study material (Foundation/Intermediate:
  Accounting, Taxation (income tax + GST), Cost & Management Accounting) — the best free
  Indian textbook substitute. Download from ICAI's BoS knowledge portal. [not yet ingested]

## What this means for our product
- Audit log is a **legal requirement** for company users: immutable, always on, 8-year
  retention, exportable report for auditors. Backups for company users must stay on Indian servers
  (cloud region choice: India).
- Fixed-asset register seeded with Schedule II classes and lives; shift-wise depreciation option;
  separate income-tax block/WDV book.
- Schedule III report pack with ageing schedules and the 11 ratios incl. variance explanations.
- MSME flag on supplier master; payables ageing vs 45-day limit; tax-disallowance warning.
