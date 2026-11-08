---
name: checkpoint
description: Update PROGRESS.md and commit clean output after running the clean-room check. Use at the end of an analysis session.
argument-hint: <app-slug or "platform">
---
Checkpoint for: $ARGUMENTS.

1. Update `<app>/PROGRESS.md`: date, what was done, open questions, next step.
2. Run `python scripts/clean_room_check.py` (scans changed files for client personal data and
   vendor identifiers from `_raw/*/name-mapping.md`). Fix every finding, or use the
   `clean-room-reviewer` agent for judgement calls. Verify nothing under `_raw/`, no binaries,
   databases, captures or screenshots are staged.
3. `git add` only the clean folders, then commit with `<app>: <summary>`.
4. Ask before pushing.
