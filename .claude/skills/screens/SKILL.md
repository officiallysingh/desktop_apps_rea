---
name: screens
description: Capture and spec app screens (screenshots and UI trees to _raw, behaviour specs to the app folder). Use when documenting screens or a menu area.
argument-hint: <app-slug> [menu area]
---
Capture screens for: $ARGUMENTS. Follow CLAUDE.md.

For each screen in scope (ask the user to open screens; don't trigger saves or other actions):
1. Save a screenshot to `_raw/<app>/screens/<screen-slug>.png` (client data: not committed).
2. Read the UI tree (rea native UI observation, or FlaUInspect) → `_raw/<app>/screens/<screen-slug>.ui.json`.
3. Write `<app>/03-screens/<screen-slug>.spec.md` from `_templates/app/03-screens/_screen.spec.md`,
   using made-up example values.
4. Add UX friction points to `<app>/ux-friction.md`.
5. Keep `<app>/03-screens/index.md` updated: menu path → screen slug → capability IDs.
Update `<app>/PROGRESS.md` at the end.
