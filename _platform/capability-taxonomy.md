# Capability taxonomy

Our own IDs. Every feature found in any app maps to one of these. Add new IDs here first.
Format: `AREA-NAME`. Keep descriptions neutral (no vendor wording).

| ID | Capability | Description |
| --- | --- | --- |
| CO-COMPANY | Company setup | Business profile, GSTIN, address, logo, multiple companies |
| CO-FY | Financial years | Year open/close, carry-forward balances |
| USR-ROLES | Users and roles | Login, permissions, audit |
| PTY-MASTER | Party master | Customers, suppliers, groups, contact, GST details |
| LED-MASTER | Ledger / account master | Chart of accounts, groups, opening balances |
| ITM-MASTER | Item master | Items, units, HSN/SAC, rates, tax categories |
| VCH-SALE | Sales voucher / invoice | Sales entry, invoice, credit/cash |
| VCH-PURCHASE | Purchase voucher | Purchase entry |
| VCH-RECEIPT | Receipt | Money received |
| VCH-PAYMENT | Payment | Money paid |
| VCH-JOURNAL | Journal / contra | Adjustments, bank-cash transfers |
| VCH-RETURN | Returns / notes | Sales/purchase returns, credit/debit notes |
| VCH-NUMBERING | Voucher numbering | Series, prefixes, resets per year |
| CRD-UDHAAR | Credit (udhaar) tracking | Running party balances, due tracking |
| CRD-REMIND | Payment reminders | SMS/WhatsApp reminders, schedules |
| STK-INVENTORY | Stock | Stock in/out, godowns, valuation |
| STK-BATCH | Batches / expiry / serials | Batch and expiry tracking |
| GST-CALC | GST calculation | CGST/SGST/IGST, place of supply, rounding |
| GST-RETURNS | GST returns | GSTR-1, GSTR-3B data and exports |
| GST-EINV | E-invoice / e-way bill | IRN, e-way bill generation |
| BNK-RECON | Bank reconciliation | Statement matching |
| RPT-LEDGER | Ledger / statement reports | Party and account statements |
| RPT-DAYBOOK | Day book / cash book | Daily transaction reports |
| RPT-FINANCIAL | Financial statements | Trial balance, P&L, balance sheet |
| RPT-STOCK | Stock reports | Stock summary, movement |
| PRT-INVOICE | Invoice printing | Templates, thermal/A4, PDF |
| IO-IMPORT | Import | Excel/Tally/other import |
| IO-EXPORT | Export | Excel/PDF/Tally export |
| SYS-BACKUP | Backup / restore | Local and cloud backup |
| SYS-SYNC | Sync / mobile view | Multi-device sync, mobile companion |
| SYS-LANG | Languages | Hindi/regional UI and printing |
| SYS-LICENSE | Licensing model | Editions, activation (observed behaviour only) |
| ORD-SALES | Sales orders / challans | Quotations, orders, delivery challans |
| ORD-PURCHASE | Purchase orders | Purchase orders, goods receipt |
| POS-BILLING | Counter / POS billing | Fast billing, barcode, cash drawer |
| SCH-DISCOUNT | Schemes and discounts | Free quantity, slab discounts, price lists |
| SLS-SALESMAN | Salesman and routes | Salesman-wise orders, beats, commission |
| MFG-BOM | Manufacturing | Bill of materials, production entries |
| PAY-PAYROLL | Payroll | Employees, salary, PF/ESI |
| CUS-EXTEND | Customisation | Scripting/extension mechanisms (e.g. Tally TDL) |
| TAX-ITR | Income tax returns | ITR preparation, computation, e-filing |
| TAX-TDS | TDS / TCS returns | Deductions, challans, quarterly returns, certificates |
| TAX-AUDIT | Tax audit | Tax audit reports and annexures |
| CA-CLIENTS | CA practice management | Client master, assessment years, status tracking |
| FA-ASSETS | Fixed assets | Asset register, depreciation (book and tax), disposal |
| RPT-ANALYSIS | Ratio analysis | Liquidity, profitability, leverage, turnover dashboards |
| BUD-BUDGET | Budgeting | Budgets, budget vs actual, cash forecast |
| SYS-AUDIT | Audit trail | Immutable edit log, period lock, auditor access |
| SYS-FOREX | Multi-currency | Foreign-currency parties/banks, rates, period-end revaluation |
