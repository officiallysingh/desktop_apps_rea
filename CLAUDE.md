# Desktop Apps RE — Claude instructions

## Purpose
Analyse Windows desktop business apps used by Indian SMBs (first: Bahi-Khata by Kamra Softwares)
and produce clean-room specifications for building a new modular, cross-platform product
(Compose Multiplatform desktop first, mobile companions later). We are NOT cloning: we capture
what each app does and why, then design a better superset.

Full plan: see `docs/plan.md`.

## Rule zero: the analysed apps must keep working exactly as they are
The apps on this machine hold REAL client data. Reading them is fine; changing them is not.
- Never change app data: no INSERT/UPDATE/DELETE/DDL on app databases, no `sqlite3` on an app
  DB file without `-readonly`. Do anything heavier on COPIES in `_raw/<app>/db-copies/`.
- Never change app files, configs or registry keys: no writes, deletes, moves or renames in app
  install/data folders. Copying FROM app folders INTO `_raw/` is fine (`reg export` too).
- TallyPrime: read through its XML/ODBC interface (localhost:9000) with Export requests only;
  never Import/Alter/Delete requests.
- Never stop, kill or reconfigure app processes or their database services (SQL Server, Firebird).
  Never uninstall or repair an app.
- Never perform business actions in the apps (save, post, delete, sync, print, send SMS/WhatsApp,
  backup/restore). The user decides what to do in the apps.
- rea runtime tools (Frida, capture, tracing) are allowed. Hooks must only OBSERVE: never modify
  arguments, return values or memory, and never call app functions. Prefer attaching while the
  app is idle, not during a save.
- `.claude/hooks/app_guard.py` enforces this for what `.claude/protected.json` lists. Add each
  app's install dir, data dirs, registry key names and process names there during /inventory.
  If the guard blocks a call, don't work around it: use a copy or ask the user.

Everything else on the machine (installing tools, settings, files outside the apps) is normal work.

## Real client data
- Don't commit real client data: screenshots, UI dumps and report outputs stay in `_raw/`
  (git-ignored). Committed specs use made-up example values.
- Keep client rows out of the conversation where possible: prefer schema, counts and
  `SELECT DISTINCT` on code/status columns over `SELECT *`.

## Other rules
1. **Clean-room.** Everything under `<app>/` and `_platform/` describes behaviour in OUR words.
   Never copy decompiled code, vendor table/column/class names, branding, icons, text or UI
   assets there. Vendor-to-our-name mappings live only in `_raw/<app>/name-mapping.md`.
2. **`_raw/` never leaves this machine.** It is git-ignored (vendor code + client data).
   Never `git add -f` it. Never commit binaries, installers, databases, captures or screenshots.
3. **No circumvention.** Never bypass, patch or analyse licence checks, dongles, anti-debug or
   licence encryption. Skip those code paths and note "licensing — out of scope".
4. **Evidence for every rule.** Each business rule, calculation or validation cites evidence:
   `[evidence: screen <name>]`, `[evidence: sql _raw/<app>/captures/<file>]`,
   `[evidence: fn <address or method> in _raw/<app>/...]`, or `[evidence: observed]`.
   Mark anything inferred as `[inferred]`.
5. **Capability IDs.** Every feature found is tagged with an ID from
   `_platform/capability-taxonomy.md` (e.g. `VCH-SALE`). If none fits, add one there first.
6. **Check against the knowledge base.** Compare every business rule found with `_knowledge/`.
   Record mismatches as `[deviates from _knowledge/<note>]` (app bug, local practice, or gap).
7. **Designs are versioned.** Never overwrite an earlier design; create a new version.

## Repo layout
```
_raw/<app>/            git-ignored: decompiled/, dumps/, captures/, db-copies/, screens/, name-mapping.md
_templates/app/        skeleton copied for each new app (/new-app)
_platform/             cross-app synthesis: taxonomy, matrix, overlaps, domain model, editions, BRD
<app>/                 clean spec per app (folder name = short lowercase slug, e.g. bahikhata)
  PROGRESS.md          session log + what's next (update before ending every session)
  01-tech-stack.md
  02-data-model/       schema.sql (our names), er.mmd, entity-dictionary.md
  03-screens/          <screen>.spec.md, index.md (screenshots + UI dumps stay in _raw/<app>/screens/)
  04-workflows/        <workflow>.md with Mermaid sequence diagrams
  05-business-rules/   one file per rule area (gst, rounding, numbering, validations, ...)
  06-reports/          <report>.md, sample-outputs/ (from sample data only)
  07-integrations/     sync API, printing, SMS/WhatsApp, import/export
  08-nfr.md            performance, backup, licensing model, multi-user, installer
  ux-friction.md       pain points with counts (keystrokes, clicks, waits)
scripts/windows/       setup and helper PowerShell scripts
_knowledge/            distilled notes from books/standards
_reference/            books/ (PDF) and text/ (extracted) — read text/ for deeper detail via /knowledge
```

## Skills and agents (`.claude/`)
- Skills (auto-used when a task matches, or type `/name`): `new-app`, `inventory`, `schema`,
  `screens`, `workflow`, `synthesize`, `knowledge`, `checkpoint`, `tally-xml-export`,
  `db-schema-dump`.
- Subagents: `clean-room-reviewer` (run before every commit), `rule-checker` (run after
  business rules change). They review independently; act on their findings.
- `python scripts/clean_room_check.py` scans changed files for client data and vendor names.

## Workflow per app (in order)
1. `/new-app <slug>` — scaffold folders, register in `_platform/apps.md`.
2. `/inventory <slug>` — locate install dir, ProgramData/AppData, registry, services, DB;
   identify tech stack → `01-tech-stack.md`.
3. `/schema <slug>` — DDL, ER diagram, entity dictionary → `02-data-model/`.
4. `/screens <slug> [menu area]` — one spec per screen → `03-screens/`.
5. `/workflow <slug> <name>` — rea captures while the user works in the app (or static analysis
   of the code path) → `04-workflows/`, `05-business-rules/`.
6. Reports, integrations, NFR → `06`–`08`.
7. `/synthesize` — update capability matrix, overlaps and shared domain model.
8. `/checkpoint` — update PROGRESS.md and commit the clean output.

## How to use rea (reverse-engineering MCP server, registered as `rea`)
- Static first: binary overview, PE imports/resources, managed (.NET) inspection, decompile,
  strings, sqlite inspection. Put bulk output in `_raw/<app>/`, never in the chat.
- Runtime: native UI observation, process/scenario capture and Frida hooks, observe-only
  (see Rule zero). Bulk output goes to `_raw/<app>/captures/`.
- Prefer `trace_feature` / correlating static and runtime to tie a UI action to its code.
- If a rea tool is unavailable on Windows, say so and fall back to the standalone tools
  (ILSpy/ilspycmd, Ghidra, ProcMon, SQL Profiler, Fiddler, FlaUI) listed in README.md.

## Screen spec = behaviour, not layout
Each `03-screens/<screen>.spec.md` follows `_templates/app/03-screens/_screen.spec.md`:
intent, fields (type, required, default, validation), actions + shortcuts, rules, navigation,
UX friction. Screenshots are reference only; we are redesigning the UI.

## Context and session discipline
- One app, or one module of an app, per session. Write findings to files as you go.
- Keep large tool output out of context: save to `_raw/` and summarise.
- Before ending a session: update `<app>/PROGRESS.md` (done, open questions, next step).

## Git
- Only stage `<app>/`, `_platform/`, `_templates/`, `docs/`, `scripts/`, root config files.
- Before committing, run `git status` and check nothing from `_raw/` or any binary/database is staged.
- Commit messages: `<app>: <what was analysed>` or `platform: <what changed>`.
- Push only when the user asks.

## Style
Markdown, short sentences, tables for fields and comparisons, Mermaid for ER, sequence and state
diagrams. Use our domain names (Party, Ledger, Voucher, Item, Tax, Company, FinancialYear).
