---
topic: Income tax, TDS/TCS and their file formats (Income-tax Act 2025 transition)
capabilities: [TAX-ITR, TAX-TDS, TAX-AUDIT, CA-CLIENTS, VCH-PAYMENT, VCH-PURCHASE, PAY-PAYROLL]
sources: [ITA-2025-TEXT, ITA-2025, IT-RULES-2026, EFILING, PROTEAN-TIN]
as_of: 2026-11-08
---
# Income tax and TDS/TCS [IN]

**The law changed on 1 April 2026.** The Income-tax Act, 2025 (with Income-tax Rules, 2026 and
Finance Act 2026) replaces the Income-tax Act, 1961. Sections below marked [ITA-2025 s.x] are
confirmed from the Act's text as amended by Finance Act 2026 (`_reference/official/`); form numbers
come from the Rules via secondary sources and still need checking against the Rules.

## Key structural changes
- **"Tax year"** = the 12-month financial year from 1 April (shorter for a new business/source).
  [ITA-2025 s.3] Income of FY 2025-26 is still filed in AY 2026-27 under the 1961 Act.
- TDS/TCS consolidated [ITA-2025 s.392–394]: **s.392** salary; **s.393** all other TDS as
  tables — s.393(1) payments to residents, s.393(2) non-residents, s.393(3) other specified cases,
  s.393(4) exemptions/no-deduction cases; **s.394** TCS (table). s.395 certificates for lower/nil
  deduction; s.397 TAN and furnishing; s.398 consequences of failure.
- TDS on residents is deducted on credit or payment, whichever is earlier, on the **entire
  amount** once the threshold is crossed. [ITA-2025 s.393(1)]

## s.393(1) table — payments to residents (most relevant rows) [ITA-2025]
| Sl. | Old section (approx.) | Nature | Rate | Threshold |
| --- | --- | --- | --- | --- |
| 1(i)/(ii) | 194D / 194H | Insurance commission / other commission or brokerage | rates in force / 2% | ₹20,000 |
| 2(i) | 194-IB | Rent paid by individuals/HUF not otherwise liable | 2% | ₹50,000 per month |
| 2(ii) | 194-I | Rent — plant/machinery / land, building, furniture | 2% / 10% | ₹50,000 per month |
| 3(i) | 194-IA | Immovable property purchase (not agricultural land) | 1% of higher of consideration and stamp value | ₹50 lakh |
| 5 | 194A | Interest (other than on securities) | as per table | as per table |
| 6(i) | 194C | Contractors (incl. labour supply) | 1% individual/HUF, 2% others | ₹30,000 single / ₹1,00,000 aggregate |
| 6(ii) | 194M | Contract/professional fees/commission paid by individual/HUF not otherwise liable | 2% | ₹50 lakh |
| 6(iii) | 194J | Professional fees, technical fees, director fees, royalty | 2% (technical, film royalty, call centre) / 10% others | ₹50,000 (director fees: nil) |
| 7 | 194 | Dividend by domestic company | 10% | nil |
| 8(ii) | 194Q | Purchase of goods > ₹50 lakh (buyer) | 0.1% on amount above ₹50 lakh | ₹50 lakh |
| 8(iv) | 194R | Business perquisites | 10% | ₹20,000 |
| 8(v) | 194-O | E-commerce operator on participant's sales | 0.1% | nil |
| 8(vi) | 194S | Virtual digital asset | 1% | nil |
- Contract work note: TDS on invoice value excluding material if material is shown separately. [s.393 note]
- "Old section" column is our mapping for orientation, not part of the Act.
- **No/invalid PAN**: higher of the specified rate, rates in force, or 20% (5% for 8(ii)/8(v));
  TCS: higher of twice the rate or 5%, capped at 20%. [ITA-2025, PAN provision in Chapter XIX-B]

## Other provisions the software touches [ITA-2025]
- **Tax audit — s.63**: business turnover > ₹1 crore (₹10 crore if cash receipts and cash
  payments each ≤ 5%); profession gross receipts > ₹50 lakh; presumptive cases declaring lower
  profit. (Replaces 1961 s.44AB.)
- **MSME payments — s.37(2)(g)**: amounts payable to micro/small enterprises beyond the MSMED Act
  s.15 time limit are deductible only when paid (no grace till return due date). (Was s.43B(h).)
- **Depreciation — s.33**: block-of-assets basis; additional depreciation on new plant 20%
  (10% if used < 180 days, balance next year).
- Some rates changed from 1 Apr 2026, e.g. TCS on scrap/liquor/minerals 2%, overseas tour
  packages and LRS education/medical 2%; manpower supply TDS 1%/2%. [verify]

## Form renumbering (applies where credit/payment is on or after 1 Apr 2026)
| Old (1961) | New (2025) | Purpose |
| --- | --- | --- |
| 24Q | 138 | Quarterly TDS return — salary |
| 26Q | 140 | Quarterly TDS return — non-salary, residents |
| 27Q | 144 | Quarterly TDS return — non-residents |
| 27EQ | 143 | Quarterly TCS return |
| 26QB/QC/QD/QE | 141 | PAN-based challan-cum-statements |
| 16 | 130 | Salary TDS certificate |
| 16A | 131 | Non-salary TDS certificate |
| 16B/C/D/E | 132 | PAN-based TDS certificates |
| 27D | 133 | TCS certificate |
| 15G/15H | 121 | Nil-deduction self-declaration |
| 13 | 128 | Lower/nil deduction certificate application |
| 15CA/15CB | 145/146 | Foreign remittance |
| 26AS | 168 | Annual tax statement |
- Quarterly return due dates unchanged: 31 Jul, 31 Oct, 31 Jan, 31 May. TDS deposit by the 7th of
  the next month (March: 30 April). Q4 of FY 2025-26 is filed on the old forms. [secondary source]

## File formats
- **TDS/TCS returns**: prepared with the Return Preparation Utility (RPU) into a text file in the
  NSDL/Protean file format, validated by the File Validation Utility (FVU), filed via TIN/e-filing.
  New FVU/file-format versions accompany the new forms — get the current file format spec from
  Protean (tin-nsdl / protean-tinpan) before building. Section/payment codes in masters must be
  updated for tax year 2026-27.
- **ITR**: each ITR form has a published **JSON schema** and validation rules on the e-filing
  portal (incometax.gov.in → downloads), released per year; offline utilities produce JSON for
  upload. Pre-filled data (AIS/TIS, Form 26AS/168) can be downloaded as JSON.
- Tax audit (1961 s.44AB → 2025 s.63) reports are also filed as schema-based JSON. [verify new form numbers]

## What this means for our product
- **Accounting editions**: TDS on purchases/expenses — party PAN and status, deductee type,
  payment-type code, threshold tracking per party per year, rate (incl. no-PAN higher rate,
  lower-deduction certificates), TDS payable ledger, challan entry, quarterly return data,
  certificates. TCS on sales similarly. Masters must carry **both** old section codes (FY 2025-26
  and earlier) and new codes (tax year 2026-27 onwards), effective-dated.
- **CompuTax-type edition** (CA practice): client master by PAN, multi-year; must support both
  laws side by side for the next few years (old-Act assessments/revisions continue); ITR JSON
  generation per year's schema; import AIS/26AS/168 JSON; TDS return RPU-format generation.
- Treat schemas, rates, thresholds and section codes as **versioned data**, not code.
