---
topic: GST e-invoice (IRP), e-way bill and return file formats
capabilities: [GST-EINV, GST-RETURNS, VCH-SALE, VCH-RETURN, IO-EXPORT, IO-IMPORT]
sources: [IRP-SCHEMA, EWB-API, GSTN-RETURNS]
as_of: 2026-11-08
---
# E-invoice, e-way bill and GST return formats [IN]

Structure taken from the government e-invoice schema (INV-01, version 1.1) as reproduced by a GSP's
developer docs; official specs are on the NIC portals (einvoice1.gst.gov.in, einv-apisandbox.nic.in,
ewaybillgst.gov.in) and GST portal offline tool. Download the current schema and API spec from
those portals before building; versions change.

## E-invoice request (IRP "Generate IRN") — schema v1.1
| Section | Key fields |
| --- | --- |
| `Version` | "1.1" |
| `TranDtls` | `TaxSch` (GST), `SupTyp` (B2B, SEZWP, SEZWOP, EXPWP, EXPWOP, DEXP [verify list]), `RegRev` (Y/N reverse charge), `EcmGstin`, `IgstOnIntra` |
| `DocDtls` | `Typ` (INV, CRN, DBN), `No` (≤16 chars), `Dt` (dd/mm/yyyy) |
| `SellerDtls` / `BuyerDtls` | GSTIN, legal and trade name, address lines, location, PIN, state code; buyer also `Pos` (place of supply) |
| `DispDtls` / `ShipDtls` | Dispatch-from and ship-to when different |
| `ItemList[]` | `SlNo`, `PrdDesc`, `IsServc`, `HsnCd`, `Barcde`, `Qty`, `FreeQty`, `Unit`, `UnitPrice`, `TotAmt`, `Discount`, `PreTaxVal`, `AssAmt`, `GstRt`, `IgstAmt`, `CgstAmt`, `SgstAmt`, `CesRt`, `CesAmt`, `CesNonAdvlAmt`, state cess, `OthChrg`, `TotItemVal`, `OrdLineRef`, `OrgCntry`, `PrdSlNo`, `BchDtls` (batch name, expiry, warranty date), `AttribDtls` |
| `ValDtls` | `AssVal`, `CgstVal`, `SgstVal`, `IgstVal`, `CesVal`, `StCesVal`, `Discount`, `OthChrg`, `RndOffAmt`, `TotInvVal` |
| `PayDtls` | payee, account, mode, terms, credit days, paid amount, payment due |
| `RefDtls` | remarks, document period, preceding document (for CRN/DBN), contract refs |
| `AddlDocDtls`, `ExpDtls` | supporting docs; export shipping bill, port, country |
| `EwbDtls` | transporter id/name, distance, transport doc, vehicle no/type, mode → generates e-way bill with the IRN |

Response: `Irn` (SHA-256 of supplier GSTIN + doc no + doc type + financial year), `AckNo`,
`AckDt`, `SignedInvoice`, `SignedQRCode`, `Status` (ACT/CNL), optional `EwbNo`/`EwbDt`/`EwbValidTill`.
- One IRN per document number per FY: the same `DocDtls.No` cannot be registered twice.
- Cancellation via IRP within **24 hours**; after that, issue a credit note. [verify]
- Item-level validations: `AssAmt = TotAmt − Discount`, tax = `AssAmt × GstRt`, totals reconcile
  within small tolerances; HSN must be valid; state codes valid. [verify tolerances]

## E-way bill [verify all]
- Part A (invoice/party/goods/value/HSN) + Part B (transporter, vehicle). Generated via portal,
  API, or together with the e-invoice (`EwbDtls`).
- Validity by distance (regular cargo ≈ 1 day per 200 km; ODC lower); extension and
  cancellation (within 24 hours) rules; multi-vehicle and consolidated EWB.

## GST return files (portal offline tool / API JSON)
| Return | Content | Our data source |
| --- | --- | --- |
| GSTR-1 / IFF | Outward supplies: B2B, B2C large, B2C small (by state/rate), credit/debit notes (registered/unregistered), exports, advances received/adjusted, nil/exempt, **HSN summary** (B2B and B2C split), documents issued summary [verify section list] | Sales, returns, receipts-on-advance |
| GSTR-1A | Amendments before GSTR-3B (since GSTR-3B liability is locked) | Corrections |
| GSTR-2B | Auto-drafted inward ITC statement (from suppliers' GSTR-1 and IMS actions) — read-only, downloaded as JSON/Excel | Purchase reconciliation |
| IMS | Accept / reject / pending per inward invoice | Purchase approval workflow |
| GSTR-3B | Summary liability, ITC, tax payment | Computed from books + GSTR-1 + 2B |
| GSTR-9 / 9C | Annual return / reconciliation | Year-end |
| CMP-08 / GSTR-4 | Composition dealers | Composition mode |

## What this means for our product
- E-invoice: build the schema object from posted invoices/notes; integrate via a GSP/ASP API
  (direct IRP API needs eligibility) — store IRN, AckNo, signed QR; print QR on invoice;
  block edits after IRN; cancellation window timer then credit-note path.
- E-way bill from the same invoice (Part A from invoice, Part B from transport details).
- Batch/expiry flows into `BchDtls` (Marg/pharma).
- GSTR-1 JSON export with pre-filing validations (HSN summary consistent with invoices,
  doc-issued summary from voucher series incl. cancelled numbers).
- GSTR-2B import + matching engine (invoice no/date/GSTIN/value fuzzy match) with IMS actions.
- Keep the schema version as data so updates don't need code changes where possible.
