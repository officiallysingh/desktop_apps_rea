---
topic: Transaction cycles (revenue, expenditure, payroll, fixed assets, conversion, GL)
capabilities: [ORD-SALES, VCH-SALE, VCH-RECEIPT, VCH-RETURN, ORD-PURCHASE, VCH-PURCHASE, VCH-PAYMENT, PAY-PAYROLL, FA-ASSETS, MFG-BOM, STK-INVENTORY, RPT-FINANCIAL]
sources: [AIS]
---
# Transaction cycles

## In one paragraph
Business activity repeats in cycles. Each cycle is a chain of documents and steps, each step
done by a different role, each leaving an audit trail, and each ending in journal entries.
Good software models the **document chain** explicitly instead of isolated vouchers. [AIS ch.2, 4–8]

## Revenue cycle [AIS ch.4]
| Step | Document | Control point | Accounting effect |
| --- | --- | --- | --- |
| Customer order | Sales order (our: quotation → sales order) | Customer exists, items valid | none |
| Credit check | Credit authorisation | Credit limit / overdue check before accepting | none |
| Pick and ship | Stock release, packing slip, bill of lading (our: delivery challan) | Ship only what was ordered and approved | Stock out (perpetual) |
| Bill | Sales invoice | Price from price list, matches shipped qty | Dr Customer / Cr Sales (+ tax) |
| Returns | Return slip, credit memo (our: credit note) | Approval, goods actually received back | Reverse sale and stock |
| Cash receipt | Remittance advice, deposit slip | Separate who receives cash from who updates receivables | Dr Bank / Cr Customer |

## Expenditure cycle: purchases and payments [AIS ch.5]
| Step | Document | Control point | Accounting effect |
| --- | --- | --- | --- |
| Need detected | Purchase requisition (stock falls to **reorder point**) | Authorised requester | none |
| Order | Purchase order to an approved supplier | Approved supplier, authorised buyer | none |
| Receive | Receiving report (our: GRN / inward) | Count and inspect; blind count | Stock in |
| Supplier bill | Supplier invoice | **Three-way match**: PO = receiving report = invoice (qty, price) | Dr Purchases/Stock (+ input tax) / Cr Supplier |
| Pay | Payment voucher / cheque, on due date | Separate approver and payer; cancel paid documents | Dr Supplier / Cr Bank |

## Payroll [AIS ch.6]
Time cards / attendance → payroll register → deductions (tax, statutory) → payment → journal.
Controls: separate timekeeping, payroll preparation and payment; watch for ghost employees;
imprest (separate) payroll bank account.

## Fixed assets [AIS ch.6]
Three procedure groups: acquisition (capital approval, register entry), maintenance
(depreciation, improvements, transfers between locations), disposal (approval, gain/loss).

## Conversion cycle (manufacturing) [AIS ch.7]
Production planning (bill of materials, routing), material issue, work in progress, finished
goods receipt; costing by standard cost, activity-based or value-stream; MRP/MRP II/ERP plan
material and capacity.

## General ledger and reporting [AIS ch.8]
Subsidiary systems post summaries to the GL; GL feeds the financial reporting system;
management (discretionary) reports follow responsibility accounting (cost/profit centres).

## What this means for our product
- Model the document chain with conversions: Quotation → Sales order → Delivery challan →
  Sales invoice → Receipt; Purchase order → GRN → Purchase invoice → Payment; each step
  pre-filled from the previous one and linked (partial conversions, pending-qty reports).
- Credit-limit and overdue checks at order/invoice time (configurable: warn or block).
- Three-way match on purchase invoices with tolerance; flag mismatches.
- Reorder level / reorder quantity per item → auto purchase suggestions.
- Delivery challans move stock without revenue; invoice later (common in Indian trade).
- Cost centres for management reports.
- Manufacturing (BOM, production entry, WIP) as a separate module/plugin.
