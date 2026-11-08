# Plan

The full plan (goal and phases, ground rules, Windows setup, workspace layout, per-app analysis,
cross-app synthesis, platform architecture, tech stack, design approach, roadmap) lives in the
Claude doc **"Desktop Apps — Reverse Engineering & Platform Plan"** in the *Desktop Apps*
project on claude.ai: https://claude.ai/artifact/XZxUZC1SuW64niU853kA8p

## Summary
1. Analyse each app on Windows with Claude Code + rea; write clean-room specs into `<app>/`.
2. Map every feature to `_platform/capability-taxonomy.md`; compare overlaps; design the superset.
3. Decide editions: one core + capability modules, packaged as separate apps or a suite.
4. Design system first, then module designs, in Claude Design (new versions, never overwrite).
5. Phase 1: desktop with Kotlin Compose Multiplatform (shared KMP domain + SQLite/SQLDelight).
6. Phase 2: mobile companions reusing the shared modules; Spring Boot Modulith backend for sync.
