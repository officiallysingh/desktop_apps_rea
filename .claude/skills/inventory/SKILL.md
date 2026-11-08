---
name: inventory
description: Inventory an installed Windows app: install/data folders, registry, services, database, tech stack; registers it in .claude/protected.json. Use as the first analysis step for an app.
argument-hint: <app-slug>
---
Inventory the installed app `$ARGUMENTS`. Follow "Rule zero" in CLAUDE.md.

1. Ask the user for the install folder if `_platform/apps.md` doesn't list it. Look in
   `C:\ProgramData`, `%AppData%`, `%LocalAppData%`, the registry (`reg query`, `reg export` to
   `_raw/<app>/dumps/`) and Windows services for the vendor's entries.
2. **Register protection first:** add the app's install dir, data dirs, vendor/product keywords,
   registry key names and process/service names to `.claude/protected.json`.
3. Identify the tech stack with rea (binary overview, PE imports/resources, managed inspection):
   language/framework, bitness, UI toolkit, DB access library, third-party components,
   obfuscation/packing. Copy binaries into `_raw/<app>/bin/` if a tool needs a writable copy.
4. Find the database: engine, location or connection string, version. For file DBs, copy them to
   `_raw/<app>/db-copies/` (ideally with the app closed, for a consistent copy).
5. Note network endpoints from strings/config.
6. Write `<app>/01-tech-stack.md`; raw listings go to `_raw/<app>/dumps/`.
7. Update `<app>/PROGRESS.md` and recommend the next step (usually `/schema`).
