---
name: synthesize
description: Update the cross-app capability matrix, overlap analyses and shared domain model. Use after finishing analysis of a module or app.
argument-hint: [capability ID or area]
---
Update the cross-app synthesis. Scope: $ARGUMENTS (default: everything changed since last run).

1. Read all `<app>/` folders listed in `_platform/apps.md`.
2. Update `_platform/capability-matrix.md` (depth per app + links to specs).
3. For each capability implemented by 2+ apps, create/update `_platform/overlaps/<ID>.md`
   from `_platform/overlaps/_overlap-template.md` and propose our merged design.
4. Update `_platform/shared-domain-model.md` reconciling entities across apps.
5. List new differentiator ideas in `_platform/enhancements.md`.
