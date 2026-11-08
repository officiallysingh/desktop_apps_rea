---
name: knowledge
description: Distil a reference book or standard into _knowledge notes, merging with existing ones. Use when adding a new reference source.
argument-hint: <source short name or file in _reference/text/> [chapters/topics]
---
Distil: $ARGUMENTS

1. Find the extracted text in `_reference/text/` (extract with `pdftotext -layout` if missing).
2. Read the table of contents; pick chapters relevant to `_platform/capability-taxonomy.md`.
3. For each topic: if a note exists in `_knowledge/`, MERGE (keep the clearest explanation, add
   only new rules/examples/edge cases, add the citation). Otherwise create it from `_template.md`.
   Write in our own words; no long quotations.
4. Always fill "What this means for our product".
5. Update `_knowledge/index.md` and `_knowledge/sources.md`.
6. Add feature ideas found to `_platform/enhancements.md` with the source.
