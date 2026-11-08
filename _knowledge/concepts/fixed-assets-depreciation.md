---
topic: Fixed assets, depreciation, amortisation, disposal
capabilities: [FA-ASSETS, VCH-JOURNAL, RPT-FINANCIAL]
sources: [AMS, FADM, IFRS]
---
# Fixed assets, depreciation and amortisation

## In one paragraph
Long-lived assets are recorded at cost and their cost is spread over their useful life:
**depreciation** for tangible assets, **amortisation** for intangibles. Accumulated depreciation
is a contra-asset; net book value = cost − accumulated depreciation. On sale, the difference
between proceeds and net book value is a gain or loss.

## Concepts and rules
- Straight-line: (cost − salvage value) / useful life, equal amount each period. [AMS ch.11]
- Accumulated depreciation is a contra-asset account (credit balance). [AMS ch.11]
- Net book value = cost − accumulated depreciation. [AMS ch.11]
- Sale above NBV → gain; below → loss. [AMS ch.11]
- Inputs: cost (or fair value), useful life, residual value, method. Reducing-balance applies a
  fixed % to the carrying amount each year. Choose the method that reflects how the asset's
  benefits are consumed, and apply it consistently. [FADM ch.3]
- Depreciation allocates cost; it does not create a fund to replace the asset. [FADM ch.3]
- Borrowing costs directly attributable to building/acquiring a qualifying asset (one that
  takes substantial time to get ready) are capitalised; others are expensed. [FADM ch.7] [IAS 23]
- Acceptable methods include straight-line, diminishing balance and units of production, but not
  revenue-based; significant components with different patterns are depreciated separately;
  cost model or revaluation model after recognition. [IFRS, IAS 16]
- Other methods exist (e.g. declining balance); immaterial purchases are expensed. [AMS ch.11]
- Intangibles amortised over the shorter of legal life and expected useful life. [AMS ch.12]
- [IN] Companies Act Schedule II prescribes useful lives (SLM or WDV); Income-tax Act uses
  block-of-assets WDV rates with half-rate if put to use < 180 days in the year. Book and tax
  depreciation therefore differ. Verify rates against official text.

## Formulas
- SLM annual depreciation = (Cost − Salvage) / Useful life (years)
- WDV annual depreciation = Opening WDV × rate
- Gain/(loss) on sale = Sale proceeds − NBV

## Journal entries (Dr / Cr)
| Event | Debit | Credit |
| --- | --- | --- |
| Buy asset | Fixed asset | Bank / Supplier |
| Period depreciation | Depreciation expense | Accumulated depreciation |
| Sell asset at a gain | Bank; Accumulated depreciation | Fixed asset (cost); Gain on sale |
| Sell asset at a loss | Bank; Accumulated depreciation; Loss on sale | Fixed asset (cost) |

## Worked example (made-up numbers)
Machine 1,10,000, salvage 10,000, life 5 years → SLM 20,000/yr. After 2 years NBV = 70,000.
Sold for 75,000 → gain 5,000.

## What this means for our product
- Fixed asset register: cost, date put to use, method, life/rate, salvage, block (tax).
- Auto-generate period depreciation journals; keep **two books**: Companies Act and Income-tax.
- Disposal wizard computes gain/loss and posts the entry.
- Capitalisation threshold setting (below it, expense directly).
