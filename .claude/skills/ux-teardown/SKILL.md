---
name: ux-teardown
description: Score UX friction per screen or workflow into a comparable table across the analysed apps, giving the design phase concrete targets (keystrokes, clicks, time, dead ends). Use when analysing screens or comparing apps' usability.
argument-hint: <app/screen or workflow>
---
# UX teardown

Scope: `$ARGUMENTS`. Append to `<app>/ux-friction.md` and, for cross-app views,
`_platform/ux-benchmark.md`.

For each screen or task, measure the common path (the user only navigates; you observe):
| Metric | How to count |
| --- | --- |
| Keystrokes to complete | count fields + confirmations for the typical case |
| Mouse clicks / taps | count pointer actions on the common path |
| Screens/dialogs traversed | count context switches |
| Time (seconds) | observed or estimated from steps |
| Dead ends / errors | states with no clear next action |
| Keyboard-only possible? | yes/no (Indian accounting users work keyboard-first) |

Then:
1. Rate severity H/M/L and write a one-line "our target" per issue (e.g. "voucher save in <=
   8 keystrokes, no mouse").
2. For a cross-app teardown of the same task, put each app in a column so the best and worst are
   visible; our design must beat the best.
3. Note what works well too — fast patterns worth keeping (e.g. Tally-style F-key shortcuts).

Screenshots stay in `_raw/`. Committed notes describe behaviour and counts, not vendor UI assets.
These friction numbers feed Claude Design: they are the measurable UX goals for the new screens.
