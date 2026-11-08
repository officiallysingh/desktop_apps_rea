---
topic: QuickBooks Desktop 2024 feature and UX benchmark
capabilities: [CO-COMPANY, LED-MASTER, ITM-MASTER, PTY-MASTER, VCH-SALE, ORD-SALES, ORD-PURCHASE, VCH-PURCHASE, VCH-PAYMENT, VCH-RECEIPT, VCH-RETURN, STK-INVENTORY, BNK-RECON, PAY-PAYROLL, VCH-JOURNAL, RPT-FINANCIAL, BUD-BUDGET, USR-ROLES, SYS-AUDIT, SYS-BACKUP, SYS-FOREX, CRD-REMIND]
sources: [QB]
---
# QuickBooks Desktop 2024 — benchmark

QuickBooks is the global reference for SMB desktop accounting. It is US-centric (sales tax, 1099,
cheques) but its feature set and workflows are a useful checklist against the Indian apps.
Accounting concepts in its Book 1 duplicate notes already in `concepts/` and are not repeated.

## Feature checklist (book structure) [QB]
| Area | QuickBooks feature | Indian-app equivalent to compare | Book/chapter |
| --- | --- | --- | --- |
| Setup | Setup wizard; suggested chart of accounts by industry; start date + opening trial balance | Company creation, default groups | Book 2 ch.1 |
| Masters | Item types: service, inventory part, non-inventory, other charge, subtotal, group (kit), discount, payment, sales-tax item and group; custom fields | Item master, units, HSN, BOM/kit | Book 2 ch.2; Book 3 ch.3 |
| Masters | Price levels and billing rate levels; bulk "change item prices"; advanced pricing rules | Price lists, rate slabs, schemes | Book 3 ch.3 |
| Masters | Classes (department/segment tracking) on any line; jobs under customers | Cost centres / categories | Book 2 ch.2; Book 4 ch.4–5 |
| Masters | Profile lists (terms, ship-via, customer types, sales reps) | Credit days, transport, salesman | Book 2 ch.2 |
| Preferences | Account numbers on/off; date warnings; **closing date** (password to change prior periods) | Period lock / F11 features | Book 2 ch.3 |
| Preferences | Finance charges on overdue balances (rules, auto calculation) | Interest on overdue | Book 2 ch.3; Book 3 ch.1 |
| Preferences | Multiple currencies; reminders; integrated payments | Forex, reminders, UPI | Book 2 ch.3 |
| Sales | Estimates → invoices; time billing (timesheets onto invoices); sales receipts (cash sale); credit memos; receive payments; email/print invoices; template **layout designer** | Quotation, invoice, POS, credit note, receipt, print designer | Book 3 ch.1 |
| Purchases | Purchase order → item receipt → bill (or receipt+bill together) → pay bills | PO → GRN → purchase invoice → payment | Book 3 ch.2 |
| Inventory | Physical count and value adjustments; assemblies (simple manufacturing); multiple inventory locations; inventory reports | Stock journal, godowns, BOM | Book 3 ch.3 |
| Banking | Write/print cheques; deposits; transfers; account register; **reconcile**; credit-card charges; **bank feeds**; loan manager | Bank reco, cheque printing, statement import | Book 3 ch.4 |
| Payroll | Payroll items; employees; YTD amounts; scheduled runs; void paychecks; pay liabilities | Payroll (PF/ESI/PT/TDS) | Book 3 ch.5 |
| Accountant | Journal entries incl. **reversing** JE; **memorized (recurring) transactions**; **accountant's copy** (accountant works on a copy while client keeps working, then merges changes); client data review | CA collaboration, remote access | Book 4 ch.1 |
| Reports | Customise display/filters/header-footer; memorised reports; process multiple reports in a batch | Report designer, favourites | Book 4 ch.2 |
| Planning | Budgets (top-line, zero-based, benchmarking); activity-based costing via classes; project/job costing | Budgets, cost centres, job work | Book 4 ch.3–5 |
| Analysis | Ratio analysis, EVA, capital budgeting, profit-volume-cost, business plan forecast | MIS reports | Book 5–6 |
| Admin | Users and permissions; audit trail (always on in recent versions); data protection/backup; troubleshooting | Security control, backup, data repair | Book 7 |

## UX patterns worth keeping
- One "centre" per party type (Customer Center, Vendor Center) with all transactions, balances
  and actions for the selected party.
- Account register (cheque-book style) for fast bank entry and review.
- Forms that look like the paper document (invoice, cheque) — familiar to non-accountants.
- Reminders/to-do list driven by due dates (bills to pay, invoices overdue, reorder).

## Gaps / pain points to beat
- Accountant's-copy workflow is a workaround for the lack of real multi-device sync — our
  sync model makes CA collaboration live and conflict-free.
- Many features are US-specific (1099, cheques, sales tax); India needs GST, TDS, e-invoice,
  e-way bill, UPI and WhatsApp.

## What this means for our product
- Add to taxonomy/backlog: item types (service, kit/group, discount, other charge), price
  levels, classes/cost centres on every line, finance charges, reversing and recurring
  journals, accountant collaboration (CA role with live access), batch reports, bank feeds
  (statement import + auto-match), data verify/repair tool.
