---
topic: Income tax, TDS/TCS and their file formats (Income-tax Act 2025 transition)
capabilities: [TAX-ITR, TAX-TDS, TAX-AUDIT, CA-CLIENTS, VCH-PAYMENT, VCH-PURCHASE, PAY-PAYROLL]
sources: [ITA-2025, IT-RULES-2026, EFILING, PROTEAN-TIN]
as_of: 2026-11-08
---
# Income tax and TDS/TCS [IN]

**The law changed on 1 April 2026.** The Income-tax Act, 2025 (with Income-tax Rules, 2026 and
Finance Act 2026) replaces the Income-tax Act, 1961. Located via secondary sources
(ClearTax, TaxGuru); **verify every section/form number against the Act, Rules and the
e-filing portal before building**.

## Key structural changes
- **"Tax year" = financial year**; the previous-year / assessment-year pair is gone for income of
  1 Apr 2026 onwards. Income of FY 2025-26 is still filed in AY 2026-27 under the 1961 Act.
- TDS/TCS consolidated: **s.392** salary TDS, **s.393** all other TDS (residents and
  non-residents, replacing 194C/194J/194I/194Q… as tables of payment types), **s.394** TCS.
  [verify the full mapping table]
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
- Tax audit (s.44AB under the 1961 Act; new section under 2025 Act [verify]) reports 3CA/3CB/3CD
  are also filed as schema-based JSON. [verify new form numbers]

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
