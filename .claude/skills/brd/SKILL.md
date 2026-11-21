---
name: brd
description: Build the platform BRD or an edition BRD from the capability matrix, overlap analyses, app specs and knowledge notes, with every requirement traced to a capability ID, evidence and knowledge source. Use when writing or updating a BRD.
argument-hint: platform | <edition name>
---
# Build a BRD

Scope: `$ARGUMENTS` (platform = whole product; or one edition from `_platform/editions.md`).
Write into `_platform/platform-BRD.md` (platform) or `_platform/brd/<edition>.md` (edition).

Run `python scripts/traceability_check.py` first and fix gaps it reports, so the BRD is built on
complete inputs.

Inputs (read these):
- `_platform/capability-taxonomy.md`, `_platform/capability-matrix.md`
- `_platform/overlaps/*.md` (merged "our design" per capability)
- each `<app>/` folder in scope (data model, screens, workflows, business rules, reports, nfr, ux-friction)
- `_knowledge/` (law, standards, patterns) for the correct behaviour
- `_platform/enhancements.md` (differentiators)

Structure each BRD:
1. **Purpose and scope** (India only, INR, Indian tax law; name the editions covered).
2. **Personas** (who uses it: shopkeeper, trader, pharma distributor, CA firm).
3. **Capabilities in scope** — one subsection per capability ID, each with:
   - what it must do, in plain requirement statements (SHALL);
   - data involved (link `02-data-model`), screens (link `03-screens`), rules (link `05-business-rules`);
   - the correct behaviour per `_knowledge/` (cite the note), flagged `[IN]` where law-specific;
   - how competitors do it + our improvement (from the overlap doc);
   - every requirement ends with a trace tag: `[cap: VCH-SALE] [evidence: ...] [knowledge: india/gst-core-rules.md]`.
4. **Data model** (link `_platform/shared-domain-model.md`).
5. **Integrations and data migration** (link `data-migration.md`; GST e-invoice/e-way bill, returns).
6. **Non-functional** (performance, offline, sync, backup, audit trail, security, languages).
7. **Out of scope** (say so explicitly, e.g. multi-currency).
8. **Open questions** (anything `[inferred]` or `[verify]` that must be confirmed before build).

Rules: our words only (clean-room); no vendor identifiers, no client data, made-up example values.
Every "the market does X" claim cites an app spec or a knowledge note. End with a Sources list of
the knowledge notes used. Offer to run the `brd` through the BA-review once drafted.
