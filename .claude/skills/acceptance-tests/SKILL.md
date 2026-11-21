---
name: acceptance-tests
description: Turn business rules from a knowledge note or an app's 05-business-rules into Given/When/Then acceptance tests with worked numbers, ready to become the product's first tests. Use when specifying tests for GST, rounding, TDS, numbering, inventory valuation, posting, etc.
argument-hint: <capability ID, knowledge note, or app/area>
---
# Write acceptance tests from business rules

Scope: `$ARGUMENTS`. Output to `_platform/acceptance-tests/<capability-or-area>.md`.

For each rule in scope (from `_knowledge/` and/or `<app>/05-business-rules/`):
1. State the rule in one line with its source (`[knowledge: ...]` or `[evidence: ...]`).
2. Write one or more scenarios in Given/When/Then with **concrete made-up numbers**:
   ```
   Scenario: Intra-state B2B sale splits GST into CGST+SGST
     Given a supplier in Rajasthan and a customer in Rajasthan
       And an item at 18% GST, taxable value 1000.00
     When the invoice is posted
     Then CGST = 90.00 and SGST = 90.00 and IGST = 0.00
       And invoice total = 1180.00
   ```
3. Cover the edge cases the rule names: boundaries (threshold crossings), rounding direction,
   zero/negative, back-dated entries, reverse charge, composition, no-PAN higher rate, etc.
4. For calculations, show the arithmetic once so the expected number is checkable.
5. Tag each scenario `[cap: <ID>]`.

Group by capability. These are specification tests (behaviour, not UI). Keep them framework-neutral
(plain Given/When/Then) so they map later to kotlin.test / Kotest in the product repo. Use only
made-up values — never numbers seen in a real client's data. End with the Sources list.
