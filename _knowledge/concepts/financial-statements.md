---
topic: Financial statements (balance sheet, P&L, retained earnings, cash flow)
capabilities: [RPT-FINANCIAL, CO-FY]
sources: [AMS, ANA, FADM]
---
# Financial statements

## In one paragraph
The **balance sheet** is a snapshot at a date (assets = liabilities + equity). The **income
statement (P&L)** covers a period. The **statement of retained earnings** bridges them (opening
RE + net income − dividends/drawings = closing RE). The **cash flow statement** shows actual cash
movement, split into operating, investing and financing activities.

## Concepts and rules
- Current assets: expected to turn into cash within 12 months; current liabilities: due within
  12 months; everything else is non-current by default. [AMS ch.2]
- Two-period (comparative) balance sheets show change between dates. [AMS ch.2]
- P&L structure: Revenue − COGS = **Gross profit**; − operating expenses = **Operating income**;
  − non-operating items = **Net income**. [AMS ch.3]
- Revenue is recognised when the business performs its obligation, i.e. when control of the
  goods/services passes to the customer — either at a point in time or over time. [FADM ch.3]
  [IFRS 15 / Ind AS 115]
- Expense classification is partly judgement, but companies must follow prescribed formats. [FADM ch.3]
- Dividends (or proprietor drawings) are NOT expenses; they are distributions of profit. [AMS ch.4]
- Retained earnings ≠ cash. [AMS ch.4]
- Operating cash flow by the **direct method** (analyse cash records) or **indirect method**
  (profit before tax + depreciation ± changes in inventories, receivables, payables). [FADM ch.6]
- Check: opening cash and cash equivalents + net change = closing; IAS 7 also wants a
  reconciliation of financing liabilities (loans) from opening to closing. [FADM ch.6]
- Cash flow vs income statement: different timing (accrual) and cash flow includes items that
  never hit P&L (loan taken, asset bought). [AMS ch.5]
  - Operating: cash from normal operations.
  - Investing: securities, property, plant and equipment.
  - Financing: transactions with owners and lenders. [AMS ch.5]
- [IN] Companies follow Schedule III (Companies Act 2013) formats; small proprietors/partnerships
  commonly use Trading A/c + P&L A/c + Balance Sheet (horizontal format). Verify against official text.

## Equity by type of business
- Proprietorship: capital account + drawings; profit added to capital. Partnership: one capital
  (and often current) account per partner, profit shared by agreement. Company: share capital,
  reserves/retained earnings, dividends; treasury stock and stock splits exist mainly for
  larger companies. [ANA ch.1, ch.7]

## Formulas
- Gross profit = Sales − COGS
- Operating income = Gross profit − Operating expenses
- Net income = Operating income − Non-operating expenses (+ non-operating income)
- Closing retained earnings = Opening + Net income − Dividends/Drawings

## What this means for our product
- Statements are pure functions over the ledger + account classification + period; no
  separately stored totals.
- Account groups need statement mapping: BS (current/non-current asset/liability, equity) vs P&L
  (direct = trading/gross profit, indirect = operating, non-operating).
- Support comparative periods and both vertical (Schedule III) and horizontal (Trading/P&L) layouts.
- Generate the cash flow statement both ways: indirect (from P&L + balance sheet changes, the
  usual published form) and direct (from bank/cash vouchers, easier for owners to read).
- Cash flow statement needs each bank/cash movement classified operating/investing/financing —
  derivable from the counter-account's group, with manual override.
- Entity type at company setup (proprietor / partnership / LLP / company) drives the equity
  section, profit appropriation and statement format.
- Year-end: close P&L into retained earnings / capital (or carry forward) — see CO-FY.
