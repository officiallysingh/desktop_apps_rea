# desktop_apps_rea

Clean-room analysis of Windows desktop business apps used by Indian SMBs, done with
Claude Code + the **rea** reverse-engineering MCP server. The output is specs (data model,
screens, workflows, business rules, reports, integrations, UX friction) for building a new
modular, cross-platform product. Full plan: [docs/plan.md](docs/plan.md).

> **The apps hold REAL client data and must keep working exactly as they are.** A guard hook
> (`.claude/hooks/app_guard.py`) blocks any change to the apps listed in `.claude/protected.json`:
> their files, configs, registry keys, databases (write SQL), processes and DB services.
> Everything else on the machine is normal work. See "Rule zero" in [CLAUDE.md](CLAUDE.md).
>
> `_raw/` (decompiled code, dumps, DB copies, screenshots) is git-ignored and never leaves the
> analysis machine. Only clean specs in our own words are committed.

## Windows machine setup (one time)

1. Open an **elevated PowerShell** and run:
   ```powershell
   winget install --id Git.Git -e
   git clone https://github.com/officiallysingh/desktop_apps_rea.git C:\re\desktop_apps_rea
   cd C:\re\desktop_apps_rea
   powershell -ExecutionPolicy Bypass -File scripts\windows\setup-tools.ps1
   powershell -ExecutionPolicy Bypass -File scripts\windows\ensure-raw.ps1
   ```
   Keep the clone path short (e.g. `C:\re\`).
2. Make sure `python` on PATH is a real Python, not the Microsoft Store stub; the guard hook
   needs it (the setup script warns if not).
3. Install the manual tools the script lists (Ghidra, dnSpyEx, x64dbg, FlaUInspect, ...) under
   `C:\Tools`, and add a Defender exclusion for `C:\Tools`.
4. Install **rea** per its docs and register it under the name `rea`:
   ```powershell
   claude mcp add rea -- <rea launch command>
   ```
5. Start Claude Code in the repo:
   ```powershell
   cd C:\re\desktop_apps_rea
   claude
   ```
6. Verify before touching any app:
   - `/hooks` shows the PreToolUse guard; `/mcp` shows `rea` connected.
   - Ask Claude to run `echo x > "C:\Program Files\BahiKhata\guard-test.txt"` → it must be
     **BLOCKED**. If not, fix Python/the hook first.
   - Ask Claude to run `binary_overview` on `C:\Windows\notepad.exe` → works.
   - Record which rea tools work on Windows in `docs/tooling-notes.md`.
7. Check the toolchain any time: `scripts\windows\setup-tools.ps1 -CheckOnly`.

## Daily workflow (inside Claude Code)

| Step | Command | Output |
| --- | --- | --- |
| Scaffold an app | `/new-app <slug>` | `<slug>/`, `_raw/<slug>/` |
| Tech stack + register protection | `/inventory <slug>` | `01-tech-stack.md`, `.claude/protected.json` |
| Data model | `/schema <slug>` | `02-data-model/` |
| Screens | `/screens <slug> [menu area]` | `03-screens/` |
| Workflows + rules | `/workflow <slug> "<name>"` | `04-workflows/`, `05-business-rules/` |
| Cross-app synthesis | `/synthesize` | `_platform/` |
| Review before commit | `clean-room-reviewer` agent / `scripts/clean_room_check.py` | findings |
| Check rules vs knowledge base | `rule-checker` agent | verdict table |
| Save progress | `/checkpoint <slug>` | `PROGRESS.md` + git commit |

Then `git push` (Claude asks before pushing). On the Mac, `git pull` and use the specs for
Claude Design and the Compose Multiplatform build.

Tips: one app (or one module of an app) per session; `/compact` often; let Claude write
findings to files rather than keeping them in chat.

## Layout

```
CLAUDE.md               rules Claude follows in every session
.claude/settings.json   permissions + guard hook
.claude/hooks/          app_guard.py (blocks changes to the analysed apps)
.claude/protected.json  what the guard protects (paths, keywords, processes, DB services)
.claude/skills/         new-app inventory schema screens workflow synthesize knowledge checkpoint
                        tally-xml-export db-schema-dump   (also usable as /name)
.claude/agents/         clean-room-reviewer, rule-checker
scripts/clean_room_check.py   pre-commit scan for client data and vendor identifiers
_templates/app/         skeleton for each app
_platform/              taxonomy, capability matrix, overlaps, shared domain model, editions, BRD
<app>/                  clean specs per app (bahikhata/ is the first)
_raw/                   git-ignored raw material (created on the Windows machine)
scripts/windows/        setup-tools.ps1, new-app.ps1, ensure-raw.ps1
docs/                   plan and tooling notes
```

## Ground rules

- The analysed apps must keep working: no change to their data, files, configs, registry keys,
  processes or DB services. You decide what to do in the apps; Claude never performs actions in them.
- Runtime hooks are observe-only.
- Real client data stays in `_raw/` and never goes into git.
- Clean-room: no vendor code, identifiers, branding or UI assets in committed files.
- Every business rule cites evidence; inferred items are marked `[inferred]`.
