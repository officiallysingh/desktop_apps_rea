---
topic: GST core rules for billing and accounting software
capabilities: [GST-CALC, GST-RETURNS, GST-EINV, VCH-SALE, VCH-PURCHASE, VCH-RETURN, VCH-NUMBERING, ITM-MASTER, PTY-MASTER, PRT-INVOICE]
sources: [CGST-ACT, CGST-RULES, CBIC-NOTIF, GSTN-ADV]
as_of: 2026-11-08
---
# GST core rules [IN]

Secondary sources (Tally, ClearTax, TaxHeal, news) were used to locate rules; each rule names
its statutory source. **Re-verify against the CBIC/GSTN text before building**; GST changes often.

## Tax invoice contents — CGST Rule 46
| Field | Rule |
| --- | --- |
| Supplier name, address, GSTIN | 46(a) |
| Serial number: consecutive, ≤ 16 chars, letters/digits/`-`/`/`, one or more series, **unique per financial year** | 46(b) |
| Date of issue | 46(c) |
| Recipient name, address, GSTIN/UIN (if registered) | 46(d) |
| Unregistered recipient, value ≥ ₹50,000: name, address, delivery address, state name and code (below ₹50,000 only on request) | 46(e)(f) |
| HSN/SAC code | 46(g) + notification on digits |
| Description; quantity with unit/UQC | 46(h)(i) |
| Total value; taxable value after discount | 46(j)(k) |
| Rate and amount of CGST/SGST/UTGST/IGST/cess | 46(l)(m) |
| Place of supply with state name (inter-State) | 46(n) |
| Delivery address if different | 46(o) |
| Whether tax payable on reverse charge | 46(p) |
| Signature / digital signature (not needed for electronic invoices) | 46(q) |
| QR code with IRN for e-invoices | 46(r) |
| Declaration when above the e-invoice threshold but invoice is exempt from e-invoicing | 46(s) |
- Consolidated daily invoice allowed for unregistered recipients who don't need an invoice. [Rule 46 provisos]
- HSN digits (Notification 78/2020-CT, from 1 Apr 2021): aggregate turnover ≤ ₹5 crore → 4 digits
  on B2B invoices (optional on B2C); > ₹5 crore → 6 digits on all invoices. [verify]

## Rates — "GST 2.0" from 22 Sep 2025
- Main slabs are now **5% and 18%**, with **40%** for specified demerit/luxury goods; the 12% and
  28% slabs were folded into these. Special rates continue (e.g. 3% gold/precious metals,
  0.25% rough diamonds, 1.5% cut/polished diamonds). Tobacco/pan masala moved off compensation
  cess to 40% from 1 Feb 2026 (Notification 19/2025-CT(Rate)). [secondary sources; verify]
- Product impact: **rates must be effective-dated per HSN** (an invoice dated 21 Sep 2025 and one
  dated 22 Sep 2025 for the same item carry different rates; credit notes against old invoices
  use the old rate).

## Tax type by place of supply — IGST Act ss.10–13
- Supplier state = place of supply → CGST + SGST/UTGST (half each); different → IGST.
- Place of supply for goods is generally where movement terminates; services have specific
  rules (e.g. B2B → recipient's location). Exports/SEZ supplies are zero-rated. [verify per case]

## Input tax credit — CGST s.16
- Conditions (s.16(2)): tax invoice/debit note in hand; goods/services received; supplier's
  details furnished in GSTR-1 and communicated in **GSTR-2B**; tax actually paid by supplier;
  recipient has filed return. Pay the supplier within **180 days** of invoice or reverse the ITC
  (with interest), re-claim on payment. [s.16(2) provisos]
- Time limit (s.16(4)): ITC for an invoice of a financial year must be claimed by **30 November**
  of the following year, or the annual return date if earlier.
- Blocked credits (s.17(5)) such as motor vehicles (with exceptions), food, personal use. [verify list]

## Credit and debit notes — CGST s.34
- Issued to correct value/tax/returns; must reference the original invoice(s); credit notes
  reducing output tax must be declared by **30 November** following the end of the financial
  year (or the annual return date if earlier).

## Reverse charge (RCM) — s.9(3)/(4)
- Recipient pays tax for notified supplies (e.g. GTA, legal services, specified goods); invoice
  shows "reverse charge: yes"; recipient self-invoices for unregistered suppliers where required.

## Composition scheme — s.10
- Turnover-limited taxpayers pay a fixed % of turnover, issue a **bill of supply** (no tax
  shown), cannot claim ITC or charge GST. [verify limits/rates]

## Thresholds and portal rules (current as of the as_of date)
| Item | Rule | Source |
| --- | --- | --- |
| E-invoicing | Mandatory if aggregate turnover > ₹5 crore in any FY since 2017-18 (from 1 Aug 2023) | Notif. 10/2023-CT [verify] |
| IRP reporting window | AATO ≥ ₹10 crore: e-invoice must be reported to IRP within 30 days of invoice date (from 1 Apr 2025) | GSTN advisory [verify] |
| E-way bill | Movement of goods with consignment value > ₹50,000 (state variations for intra-state) | Rule 138 [verify] |
| Invoice Management System (IMS) | From Oct 2024 recipients accept/reject/keep-pending inward invoices; drives GSTR-2B | GSTN advisory |
| GSTR-3B hard-lock | From the July 2025 period, auto-populated liability (from GSTR-1/1A) is not editable in GSTR-3B; corrections go through GSTR-1A | GSTN advisory |
| Time-bar | Returns cannot be filed after 3 years from their due date (from July 2025 tax period onwards) | Finance Act 2023 / GSTN advisory |

## What this means for our product
- HSN/SAC master with **effective-dated rates**, cess and UQC; auto-select CGST+SGST vs IGST from
  party state and place of supply; RCM flag per item/party.
- Voucher numbering per series per FY, ≤ 16 chars, validated; no reuse after cancellation.
- Invoice print template enforces Rule 46 fields; B2C ≥ ₹50,000 forces address and state.
- Purchase side: match bills with GSTR-2B/IMS; flag ITC at risk (supplier not filed, 180-day
  unpaid, 30-Nov deadline approaching); blocked-credit tagging.
- Credit/debit notes linked to original invoices with old rates; 30-Nov cut-off warning.
- Because GSTR-1 now drives a non-editable GSTR-3B, GSTR-1 correctness before filing is critical:
  pre-filing validation report.
- Composition-dealer mode: bill of supply, no tax lines, no ITC.
