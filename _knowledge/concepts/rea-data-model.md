---
topic: REA (Resources–Events–Agents) data modelling
capabilities: [LED-MASTER, VCH-SALE, VCH-PURCHASE, STK-INVENTORY, PTY-MASTER]
sources: [AIS]
---
# REA data model

## In one paragraph
REA models a business as **resources** (cash, inventory, assets), **events** (sale, receipt,
purchase, payment) and **agents** (customers, suppliers, employees). Each event links to at
least one resource and two agents (internal and external). **Economic duality**: every give
event pairs with a take event (sale ↔ cash receipt; purchase ↔ payment). The enterprise model is
built by modelling each cycle's view and integrating them. Pure REA derives the ledger from
events; most companies keep a traditional GL alongside. [AIS ch.10]

## Concepts and rules
- View modelling steps: identify events → resources changed → agents → associations and
  cardinalities; then integrate views, define keys, build tables and user views. [AIS ch.10]
- Duality links (e.g. invoice ↔ receipts, many-to-many) are what bill-by-bill settlement is.

## What this means for our product
- Our domain model should be event-first: business documents (invoice, receipt, GRN) are the
  source of truth; journal lines are **derived** from them by posting rules and stored for
  speed and audit. This lets us re-post if rules change and keeps the ledger consistent.
- Explicit duality/settlement table (receipt ↔ invoices, payment ↔ bills) instead of only
  running balances; drives ageing, interest and reminders.
- Agents are one Party entity with roles (customer, supplier, employee, salesman), so one
  person can be both buyer and seller (common for traders) with a net position report.
- Fits sync well: events are append-only and immutable once posted (see target architecture).
