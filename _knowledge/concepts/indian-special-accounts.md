---
topic: Indian practice — interest on party accounts, sectional ledgers, branches, departments, partnerships, incomplete records
capabilities: [CRD-UDHAAR, RPT-LEDGER, LED-MASTER, STK-INVENTORY, CO-COMPANY, RPT-FINANCIAL, IO-IMPORT]
sources: [ICAI-AA2]
---
# Indian special accounting practices

From ICAI Board of Studies study material, *Advanced Accounting* Volume 2 (PCC, older edition):
classic Indian topics that Tally/BUSY/Marg implement and our product must too. Our words.

## Interest on party accounts [ICAI-AA2 ch.7]
- **Average due date**: to settle many dues with one payment (or one loan with many repayments)
  without interest difference. Method: pick a zero day (earliest due date), days from zero day ×
  amount for each item, sum of products ÷ sum of amounts = days from zero day to the average due
  date. Also used for interest on proprietor/partner drawings. Days of grace and holiday rules
  apply to bills of exchange.
- **Account current**: running statement between two parties including interest on each item,
  "A in account current with B"; prepared with interest tables, the **products method**
  (amount × days, interest on net products) or the **balances method** (interest on each
  running balance for the days it stood).
- Product: interest on overdue receivables/payables per party, bill-wise or on running balance,
  with rates by party/group; interest invoices (taxable under GST — see india/gst-core-rules.md);
  average due date helper for settlements.

## Self-balancing / sectional ledgers [ICAI-AA2 ch.7]
- Debtors' and creditors' ledgers kept separately, each with a **control (adjustment) account**
  in the general ledger so each ledger can be balanced independently and errors localised.
- Product: party groups are sub-ledgers with group totals = control balance; built-in
  "ledger vs control" reconciliation (always zero in software, but needed when importing data).

## Branch accounts [ICAI-AA2 ch.10 unit 4]
- Dependent branches: debtors system, **stock and debtors system** (goods sent at invoice price,
  branch adjustment account for loading/margin), final accounts system; independent branches keep
  full books, reconciled through branch / head-office accounts; goods/cash in transit at year end;
  inter-branch transfers.
- Product: multi-branch company with branch as a dimension or separate books; stock transfer
  vouchers at cost or invoice price with unrealised margin elimination; inter-branch
  reconciliation report; GST: transfers to branches in other states are taxable supplies
  between distinct persons.

## Departmental accounts [ICAI-AA2 ch.10 unit 3]
- Trading/P&L by department; allocation of common expenses on suitable bases (floor area,
  sales, headcount); inter-department transfers at cost or with profit, eliminating unrealised
  profit on closing stock.
- Product: cost centre / department dimension with allocation rules and department-wise P&L.

## Hire purchase and instalment sales [ICAI-AA2 ch.10 unit 1]
- Asset recorded at cash price; interest portion of each instalment expensed; repossession
  (full/partial) entries. Product: instalment schedule generator for EMI-based sales.

## Partnership [ICAI-AA2 ch.11]
- Fixed or fluctuating capital accounts, current accounts, interest on capital and drawings,
  salaries/commission to partners, profit appropriation; admission, retirement, death (goodwill,
  revaluation), dissolution, conversion to company.
- Product: partner capital/current ledgers, interest-on-capital/drawings computation (average due
  date), profit appropriation account at year end.

## Not-for-profit organisations [ICAI-AA2 ch.8]
- Receipts & payments account, income & expenditure account, capital fund; educational
  institutions. Product: NPO/trust edition with these statements (possible niche).

## Incomplete records (single entry) [ICAI-AA2 ch.9]
- Profit found by comparing **statements of affairs** (opening vs closing capital, adjusted for
  drawings/capital introduced), or by converting to double entry using cash book + debtor/creditor
  lists.
- Product: highly relevant to **udhaar/khata** users moving up — an onboarding wizard that builds
  opening balances and a statement of affairs from a simple cash book and party balances.

## Computerised accounting [ICAI-AA2 ch.12]
- Covers spreadsheets and accounting software concepts (codification, grouping, reports) — no new
  rules beyond `concepts/double-entry-and-ledger.md`.
