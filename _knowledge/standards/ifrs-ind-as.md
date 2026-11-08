---
topic: IFRS / Ind AS standards that shape accounting software
capabilities: [RPT-FINANCIAL, STK-INVENTORY, FA-ASSETS, VCH-SALE, VCH-RETURN, CRD-UDHAAR, SYS-FOREX]
sources: [IFRS]
---
# IFRS / Ind AS for software design

Source is a 2023 summary of IFRS ("IFRS in your pocket"). India's **Ind AS** are converged with
IFRS (numbering: IAS n → Ind AS n, IFRS n → Ind AS 10n, e.g. IFRS 15 → Ind AS 115). Ind AS apply
to listed and larger companies; most SMB users follow **Indian Accounting Standards (AS)** under
the Companies (Accounting Standards) Rules, or no formal standard (proprietors). [IN] Verify
applicability thresholds against ICAI/MCA texts.

## Standards that matter for an SMB product
| Standard | Rule that affects software | Note |
| --- | --- | --- |
| IAS 1 Presentation | Complete set: financial position, P&L + OCI, changes in equity, cash flows, notes; comparatives for prior period required [IFRS, IAS 1] | Schedule III in India |
| IAS 2 Inventories | Lower of cost and NRV; cost = purchase + conversion + costs to bring to present location/condition (not FX differences); FIFO or weighted average; **LIFO not permitted**; specific identification for non-interchangeable items; write-down to NRV is an expense, reversal reduces expense [IFRS, IAS 2] | Merged into concepts/inventory-and-cogs.md |
| IAS 7 Cash flows | Operating/investing/financing; direct or indirect | concepts/financial-statements.md |
| IAS 16 PP&E | Initial cost incl. all costs to get ready for use (+ borrowing costs per IAS 23); cost model or revaluation model; depreciation by consumption pattern (SL, diminishing, units of production; **not revenue-based**); separate depreciation of significant components; residual value and useful life reviewed [IFRS, IAS 16] | concepts/fixed-assets-depreciation.md |
| IAS 21 Foreign exchange | Record at transaction-date rate; at period end retranslate **monetary items** (receivables, payables, bank) at closing rate; non-monetary at historical rate; differences to P&L [IFRS, IAS 21] | Needed for exporters/importers |
| IFRS 15 Revenue | Five steps: identify contract → performance obligations → transaction price (incl. variable consideration, constrained) → allocate by stand-alone selling price → recognise when/as control transfers; guidance for returns rights, over-time recognition [IFRS, IFRS 15] | Bundles, returns, schemes |
| IFRS 9 Financial instruments | Expected credit loss (ECL) model: 12-month ECL, lifetime ECL if credit risk rose significantly [IFRS, IFRS 9]; simplified lifetime-ECL approach for trade receivables (verify against IFRS 9 text) | concepts/receivables-and-bad-debts.md |
| IAS 37 / IAS 38 / IFRS 16 | Provisions, intangibles, leases | concepts/provisions-contingencies-leases.md |
| IFRS for SMEs | Simplified standard for non-listed entities (third edition in progress, 2022 ED) [IFRS] | Not adopted in India; AS fill this role |

## What this means for our product
- Inventory: support landed cost (freight, duties, other costs added to stock value), NRV
  write-down entries and their reversal; no LIFO option.
- Fixed assets: component accounting optional; methods SL / WDV / units of production; never
  revenue-based.
- Multi-currency: party and bank ledgers in foreign currency, rate per transaction, period-end
  revaluation journal for monetary items, realised vs unrealised FX gain/loss.
- Revenue: schemes and bundles (free quantity, buy-x-get-y) need allocation of price across
  items; sales with right of return may need a refund liability (Ind AS users).
- Receivables: provision matrix by ageing bucket (simplified ECL) as a year-end helper.
- Statements: comparative columns always; statement of changes in equity for companies.
