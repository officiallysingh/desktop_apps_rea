---
name: workflow
description: Trace a business workflow end to end (UI action, code, SQL) observe-only and write workflow and business-rule specs. Use for any business process like invoice save or stock transfer.
argument-hint: <app-slug> <workflow name, e.g. "sales invoice save">
---
Trace the workflow: $ARGUMENTS. Follow "Rule zero" in CLAUDE.md.

1. Start observe-only captures (rea process/UI scenario capture, Frida hooks that only log,
   ProcMon, SQL Profiler/Extended Events, Fiddler). Save raw captures to
   `_raw/<app>/captures/<workflow-slug>/`.
2. The USER performs the action in the app if and when they choose (it's their client data).
   You never click, type or trigger the action. If the user prefers not to, trace the code path
   statically and mark findings `[static]`.
3. Correlate UI action → handlers → validations/calculations → SQL → files/network, reading the
   logic with rea static tools.
4. Write `<app>/04-workflows/<workflow-slug>.md` from the template (steps, Mermaid sequence,
   states, errors) and rules in `<app>/05-business-rules/<area>.md` with evidence tags and worked
   examples using made-up numbers. Update `<app>/PROGRESS.md`.
