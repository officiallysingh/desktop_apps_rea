# Knowledge base

Distilled, merged notes from reference books and official sources, in OUR words.
Used to (1) check business rules found by reverse engineering, (2) find features no app has,
(3) seed acceptance tests and the shared domain code.

- Source books are in `_reference/books/` (PDF) with extracted text in `_reference/text/`
  (`pdftotext -layout`), committed to this private repo. Each note cites `[Book short name, ch./section]`.
- One note per topic. When a second source covers the same topic, MERGE into the existing note
  (keep the clearest explanation, add only what is new, add the citation). No duplicate notes.
- Indian specifics (GST, TDS, Ind AS, Companies Act) override generic/US/IFRS material; mark
  each rule with its jurisdiction when it differs: `[IN]`, `[US]`, `[IFRS]`.

## Layout
- `concepts/`  accounting concepts and rules (double entry, inventory valuation, depreciation, ...)
- `standards/` standards and frameworks (IFRS/Ind AS, EPCIS, controls)
- `benchmarks/` feature and UX benchmarks from other products (e.g. QuickBooks)
- `index.md`   topic → note → capability IDs → sources
- `sources.md` every source used, with short name
- `wishlist.md` sources we don't have yet, in priority order

## Note template
See `_template.md`.
