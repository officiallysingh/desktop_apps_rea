---
topic: Inventory and cost of goods sold
capabilities: [STK-INVENTORY, ITM-MASTER, RPT-STOCK, RPT-FINANCIAL]
sources: [AMS, FADM, IFRS]
---
# Inventory and cost of goods sold

## In one paragraph
COGS is the cost of the inventory sold in a period. Under the **periodic** method you count stock
at period end and derive COGS; under the **perpetual** method every movement updates stock and
COGS continuously. A **cost-flow assumption** (FIFO, LIFO, weighted average) decides which unit
costs go to COGS and which stay in closing stock.

## Concepts and rules
- Periodic: COGS = Opening stock + Purchases − Closing stock (from a physical count). [AMS ch.13]
- Perpetual: each unit tracked continuously; costlier to run but simpler/more accurate
  accounting. Software makes perpetual cheap. [AMS ch.13]
- FIFO: oldest units sold first. LIFO: newest first. Average cost: weighted average cost per
  unit available for sale. [AMS ch.13]
- Rising prices: FIFO gives the lowest COGS and highest closing stock, LIFO the opposite, weighted
  average in between; falling prices reverse FIFO/LIFO. [FADM ch.3]
- Inventories are shown at the lower of cost and net realisable value; the chosen method must be
  applied consistently. [FADM ch.3]
- COGS can be found by matching each sale to its cost (perpetual) or by adjusting purchases for
  opening and closing stock (periodic). [FADM ch.3]
- Cost includes purchase price plus conversion costs and other costs to bring stock to its present
  location and condition (freight, duties = landed cost), but not FX differences. NRV write-downs
  are expensed; reversals reduce the expense. [IFRS, IAS 2]
- [IN] AS 2 / Ind AS 2 do NOT permit LIFO; allowed: FIFO, weighted average (and specific
  identification for non-interchangeable items). Inventory valued at lower of cost and net
  realisable value. Verify against official text.

## Formulas
- COGS (periodic) = Opening inventory + Purchases (+ direct costs) − Closing inventory
- Weighted average unit cost = (Opening value + Purchase value) / (Opening qty + Purchase qty)
  (moving average when recomputed after each receipt)
- Gross profit = Sales − COGS

## Worked example (made-up numbers)
Opening 10 @ 100; buy 10 @ 120; sell 15.
- FIFO COGS = 10×100 + 5×120 = 1,600; closing = 5×120 = 600
- Weighted average = (1,000+1,200)/20 = 110 → COGS 1,650; closing 550

## What this means for our product
- Company setting: valuation method (FIFO / weighted average / moving average); no LIFO for India.
- Perpetual stock ledger per item (and per godown/batch) with quantity and value; stock
  valuation report reproducible for any date.
- Physical stock verification feature to post count differences (shortage/excess).
- Back-dated entries must trigger revaluation of later issues (a known pain point to test in
  every analysed app).
- Lower of cost and NRV check at year end (flag items whose selling price < cost).
