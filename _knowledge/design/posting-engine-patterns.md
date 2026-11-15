---
topic: Posting engine and domain patterns (Fowler, Analysis Patterns)
capabilities: [LED-MASTER, VCH-JOURNAL, VCH-SALE, VCH-PURCHASE, STK-INVENTORY, GST-CALC, TAX-TDS, ITM-MASTER, PTY-MASTER, SYS-AUDIT]
sources: [FOWLER-AP]
---
# Posting engine patterns

Martin Fowler's *Analysis Patterns* ch.6 "Inventory and Accounting" gives a small set of
patterns that map directly onto our posting engine; ch.2, 3 and 5 add party, quantity/unit and
identity patterns. Our notes, our wording.

## Core accounting patterns [FOWLER-AP ch.6]
| Pattern | Idea | Our use |
| --- | --- | --- |
| **Account** (6.1) | A quantity plus an entry for every change; balance = net of all entries | Ledger, party, stock holding, tax liability — all are accounts |
| **Transaction** (6.2) | Links entries so a withdrawal from one account is a deposit in another; entries sum to zero | Voucher = transaction; ΣDr = ΣCr enforced |
| **Summary account** (6.3) | Hierarchy of detail and summary accounts; summary balance = sum of children | Ledger groups (Sundry Debtors, Duties & Taxes …) |
| **Booking to multiple accounts** (6.15) | When an entry belongs to several classifications, allow an account to have **several summary parents** (a DAG, no cycles) or use separate classification dimensions | Cost centres, projects, branches as dimensions instead of duplicate postings |
| **Memo account** (6.4) | Entries that track an amount without moving real value (e.g. tax set aside) | Statistical/memo ledgers, TDS deductible tracking, budget figures |
| **Posting rule** (6.5) | A rule watching a trigger account creates further entries (e.g. x% of each income entry to tax) | GST on sales, TDS on expenses, round-off, discount, commission, inventory COGS |
| **Individual instance method** (6.6) | Each rule instance can carry its own calculation strategy | Tax rates/thresholds as data with pluggable calculators |
| **Posting rule execution** (6.7) | Separate *when* rules fire from *what* they do: eager (at posting), account-based (process pending entries in a cycle), on demand | Real-time posting for vouchers; batch for depreciation, interest, period closing |
| **Posting rules for many accounts** (6.8) | One rule template applied across a family of accounts | One GST rule applied to every sales ledger |
| **Choosing entries** (6.9) | Select subsets of an account's entries by date range or type via filters | Reports, period balances, bill-wise selection |
| **Accounting practice** (6.10) | Group a network of accounts + rules into a named practice per customer type | Editions/business types (trader, composition dealer, pharma) as rule packs |
| **Sources of an entry** (6.11) | Every derived transaction remembers which rule created it and which entries were inputs | Explain any GST/TDS/COGS line; audit trail; re-posting |
| **Balance sheet vs income statement accounts** (6.12) | Account nature decides statement and closing behaviour | Account nature in the master |
| **Corresponding account** (6.13) | The other party's view of the same account (my bank account vs the bank's ledger) | Bank reconciliation, party confirmation/reconciliation statements |
| **Specialized account model** (6.14) | Subtype accounts per domain; inventory = account per (item × location) called a holding | Stock holdings per item × godown × batch |

## Supporting patterns
- **Quantity with units and conversion ratios** (3.1–3.3): store amount + unit; convert through
  explicit ratios; compound units. → item units (box = 12 pcs), GST UQC mapping. [FOWLER-AP ch.3]
- **Dual time record** (3.8): record both when something applies and when it was recorded. →
  voucher date vs entry timestamp; back-dated entries; audit. [FOWLER-AP ch.3]
- **Party / organisation hierarchy / accountability** (ch.2): one Party type for people and
  organisations, with roles and relationships. → customers, suppliers, employees, branches. [FOWLER-AP ch.2]
- **Identification scheme, object merge, equivalence** (ch.5): multiple identifiers per object
  (GSTIN, PAN, phone, code), merging duplicates while keeping history. [FOWLER-AP ch.5]

## What this means for our product
- Posting engine = documents → posting rules (versioned data, per accounting practice) → balanced
  transactions; every derived line keeps its source document and rule id ("why is this line here").
- Cost centres/branches as dimensions on entries, not separate ledgers.
- Stock is an account per item × godown × batch with quantity *and* value entries.
- Rule-firing strategies: synchronous for vouchers; scheduled jobs for recurring/closing rules;
  re-run rules for back-dated changes (recompute affected periods deterministically).
- Party dedupe/merge tool keyed on GSTIN/PAN/phone, keeping both histories.
