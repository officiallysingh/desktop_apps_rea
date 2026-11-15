---
topic: Inventory management practice (replenishment, locations, counting)
capabilities: [STK-INVENTORY, STK-BATCH, ITM-MASTER, ORD-PURCHASE, RPT-STOCK, MFG-BOM]
sources: [MULLER]
---
# Inventory management practice

Operational side of inventory (valuation is in `inventory-and-cogs.md`), from Max Muller,
*Essentials of Inventory Management* (AMACOM). Our words.

## Concepts and rules
- Inventory is both a physical thing and money; **carrying cost** (capital, storage, handling,
  insurance, obsolescence, shrinkage) is often estimated as a % of inventory value per year
  ("K factor", commonly ~25%). [MULLER ch.2]
- **SKU** = each distinct item variant held; identify items and locations clearly and tie SKU
  numbers to location addresses. [MULLER ch.3]
- Location systems: **fixed** (each SKU has a home slot — easy to find, wastes space),
  **random/floating** (any free slot — space-efficient, needs a system to track), and
  combinations/zoning (e.g. fast movers near dispatch). [MULLER ch.3]
- **Independent demand** (finished goods, spares; driven by the market) → replenishment approach
  (order points). **Dependent demand** (components of a product) → requirements approach
  (BOM explosion, MRP). [MULLER ch.5]
- Order point = expected demand during lead time + safety stock; safety stock protects against
  demand and lead-time uncertainty. Min/max: reorder up to max when stock hits min. [MULLER ch.5]
- **EOQ** balances ordering cost against carrying cost. [MULLER ch.5]
- Cycle counting (instead of one annual stock-take): methods = control group, location audit,
  random selection, product category, and **ABC** (count A items most often). [MULLER ch.7]
- ABC analysis: rank SKUs by annual value usage; a small share of SKUs carries most value
  (Pareto). [MULLER ch.7]

## Formulas
- Order point (ROP) = average daily usage × lead time (days) + safety stock
- EOQ = √(2 × annual demand × cost per order / (unit cost × carrying-cost rate))
- Annual carrying cost = average inventory value × carrying-cost rate
- ABC: sort by (annual qty × unit cost) descending; cumulative ~80% value = A, next ~15% = B, rest = C (thresholds configurable)

## Worked example (made-up numbers)
Usage 20/day, lead time 7 days, safety stock 40 → ROP = 180. Annual demand 5,000, order cost
₹500, unit cost ₹100, carrying 25% → EOQ = √(2×5000×500 / 25) = √200,000 ≈ 447 units.

## What this means for our product
- Item master: reorder level, reorder qty (or EOQ helper), min/max, lead time per supplier,
  safety stock; purchase suggestions report driven by these.
- Godown/bin locations (optional) with fixed or floating assignment.
- ABC classification job and cycle-count planner (A monthly, B quarterly, C yearly — configurable),
  count sheets without book quantity (blind count), variance posting with approval.
- Carrying-cost and slow-moving/dead-stock reports (pharma: near-expiry too).
- BOM-driven requirements for manufacturing editions (dependent demand).
