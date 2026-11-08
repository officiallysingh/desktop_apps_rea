---
topic: Accounting equation, double entry, ledger, trial balance
capabilities: [LED-MASTER, VCH-SALE, VCH-PURCHASE, VCH-RECEIPT, VCH-PAYMENT, VCH-JOURNAL, RPT-LEDGER, RPT-FINANCIAL]
sources: [AMS, ANA, AIS]
---
# Accounting equation, double entry, ledger, trial balance

## In one paragraph
Every business record rests on **Assets = Liabilities + Owners' Equity** (equivalently
Assets − Liabilities = Equity). Every transaction is a journal entry with at least one debit and
one credit of equal total, so the equation always stays balanced. Journal entries post to ledger
accounts; a trial balance lists every account balance and proves total debits = total credits.

## Concepts and rules
- Equation always holds; equity is the residual ("plug") after liabilities. [AMS ch.1]
- One party's asset is the other party's liability (our receivable = customer's payable). [AMS ch.1]
- Debit increases assets and expenses; decreases liabilities, equity and revenue.
  Credit is the reverse. Mnemonic: debit = left side of the equation, credit = right. [AMS ch.8]
- Revenue increases equity → credited; expenses decrease equity → debited. [AMS ch.8]
- General ledger = all journal entries grouped by account; a T-account shows one account's
  debits (left) and credits (right) for a period, with opening and closing balance. [AMS ch.8]
- Trial balance = balance of every account at a point in time; total Dr must equal total Cr.
  It does NOT catch an entry posted to the wrong account of the same side, or an omitted entry. [AMS ch.8]
- Chart of accounts = numbered list of every ledger account; posting = copying each journal
  line to its ledger account with a back-reference to the journal page/voucher. [ANA ch.6]
- Accounting cycle: record journal → post to ledger → trial balance → adjusting entries →
  adjusted trial balance → statements → closing entries → post-closing trial balance. [ANA ch.6]
- Closing entries move every income and expense balance into retained earnings (or the
  proprietor's capital) so P&L accounts start the next period at zero; only balance-sheet
  accounts carry forward. [ANA ch.6]
- Negative numbers in statements are conventionally shown in parentheses. [AMS end-notes]

## Normal balances
| Account type | Increases with | Normal balance |
| --- | --- | --- |
| Asset | Debit | Debit |
| Expense | Debit | Debit |
| Liability | Credit | Credit |
| Equity / Capital | Credit | Credit |
| Revenue / Income | Credit | Credit |
| Contra-asset (e.g. accumulated depreciation) | Credit | Credit |

## Journal entries (Dr / Cr)
| Event | Debit | Credit |
| --- | --- | --- |
| Buy equipment for cash | Equipment | Cash/Bank |
| Buy goods on credit | Purchases / Inventory | Supplier (Accounts Payable) |
| Pay supplier | Supplier (A/P) | Cash/Bank |
| Take a loan | Cash/Bank | Loan (Notes Payable) |
| Credit sale | Customer (A/R) | Sales |
| Receive from customer | Cash/Bank | Customer (A/R) |

## Worked example (made-up numbers)
Opening: Assets 3,00,000 = Liabilities 2,30,000 + Equity 70,000. Pay 15,000 of a loan from cash:
Dr Loan 15,000 / Cr Cash 15,000 → Assets 2,85,000 = Liabilities 2,15,000 + Equity 70,000.

## What this means for our product
- The posting engine must reject any voucher where ΣDr ≠ ΣCr (to the paisa) — enforced in the
  shared core, not the UI.
- Account master needs a **nature** (asset/liability/equity/income/expense) that drives normal
  balance, sign display (Dr/Cr, parentheses) and statement placement.
- User-facing vouchers (sale, purchase, receipt, payment) are templates that generate balanced
  journal lines; "journal" voucher exposes raw Dr/Cr for accountants.
- Trial balance report: per account opening, Dr total, Cr total, closing; a built-in integrity
  check that should never fail (if it does, it's a bug, not a user error).
- Period close is a first-class operation: adjusted TB → statements → closing → post-closing TB.
  Software can close "virtually" (compute retained earnings on the fly) instead of posting
  closing entries, but must show the same results. [ANA ch.6]
- Account and item codes: allow optional structured codes (block/group) and mnemonic aliases
  for fast keyboard entry; validate codes with check digits where users type them. [AIS ch.8]
- Every ledger line keeps a link to its source voucher (audit trail, drill-down).
- Ledger/party statement = T-account with running balance; drill-down to voucher.
