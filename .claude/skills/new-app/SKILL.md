---
name: new-app
description: Scaffold a new app folder for reverse engineering from the template and register it. Use when starting analysis of a new desktop app.
argument-hint: <app-slug> [vendor] [product name]
---
Scaffold a new app for analysis. Arguments: $ARGUMENTS

1. Slug = first argument (lowercase, letters/digits/hyphens). Stop if `<slug>/` already exists.
2. Copy `_templates/app/` to `<slug>/` (keep the `_*.md` templates inside).
3. Create `_raw/<slug>/{bin,decompiled,dumps,captures,db-copies,screens}` and an empty `_raw/<slug>/name-mapping.md`.
4. Add a row to `_platform/apps.md` (slug, product, vendor, status = "not started").
5. Fill the header of `<slug>/PROGRESS.md` with product and vendor names.
6. Show the created tree and suggest running `/inventory <slug>` next.
