---
topic: GS1 EPCIS 2.0 — supply-chain event traceability
capabilities: [STK-BATCH, STK-INVENTORY, MFG-BOM, ORD-SALES, ORD-PURCHASE, IO-EXPORT]
sources: [EPCIS]
---
# GS1 EPCIS 2.0 — traceability events

## In one paragraph
EPCIS (GS1, release 2.0, June 2022) is a standard for capturing and sharing **visibility
events**: what happened to which objects, when, where, why and how. It lets different
applications and companies exchange track-and-trace data. Version 2.0 adds a JSON/JSON-LD
syntax, the "how" (sensor) dimension and the AssociationEvent. Values for business steps,
dispositions etc. come from the companion **Core Business Vocabulary (CBV)**. [EPCIS ch.7]

## Event types [EPCIS §7.4]
| Event | Captures | Our equivalent |
| --- | --- | --- |
| ObjectEvent | Something observed/done to objects (instance EPCs or class + quantity), action ADD/OBSERVE/DELETE | Stock in/out, dispatch, receipt, expiry/destruction |
| AggregationEvent | Objects packed into / unpacked from a parent (case, pallet) | Packing cartons, shipper boxes |
| TransactionEvent | Objects linked to / unlinked from a business transaction (PO, invoice, despatch advice) | Linking batches to invoice / challan |
| TransformationEvent | Inputs consumed → outputs produced (linked by transformationID over time) | Manufacturing / repacking (BOM) |
| AssociationEvent | Objects associated with a parent object or location (e.g. a sensor to a container) | Asset/sensor tagging |

## Five dimensions [EPCIS §7.2.2]
- **What**: objects — instance identifiers (EPC, e.g. SGTIN = GTIN + serial) or class level
  (GTIN + lot) with quantity; parent/child for aggregation; inputs/outputs for transformation.
- **When**: event time, record time, time-zone offset.
- **Where**: read point (where observed) and business location (where objects are afterwards).
- **Why**: business step (e.g. shipping, receiving), disposition (e.g. in transit, sellable,
  expired), business transactions, source/destination parties.
- **How**: sensor readings (temperature etc.).
- **ILMD** (instance/lot master data, e.g. lot attributes such as expiry) may only be attached
  when the object comes into existence (ObjectEvent ADD, TransformationEvent). [EPCIS §7.3.8]

## What this means for our product
- Most relevant to pharma and FMCG distribution (Marg ERP's market): batch/lot, expiry, serial
  numbers, packing hierarchy, and recall ("which customers received batch X?").
- Design stock movements as events with what/when/where/why from day one; that makes batch
  traceability reports cheap and an EPCIS JSON export possible later (export-oriented pharma
  and regulated supply chains).
- Item master: GTIN/barcode per pack level; batch master: lot, mfg date, expiry (ILMD-like).
- [IN] Check current Indian pharma track-and-trace requirements (e.g. barcoding/QR on APIs and
  top brands, export traceability) before scoping — verify against official notifications.
