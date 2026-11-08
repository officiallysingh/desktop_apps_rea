---
topic: Receivables, bad debts, credit control
capabilities: [CRD-UDHAAR, CRD-REMIND, PTY-MASTER, RPT-LEDGER, RPT-ANALYSIS]
sources: [AMS, ANA, FADM, IFRS]
---
# Receivables, bad debts and credit control

## In one paragraph
Credit sales create receivables (amounts customers owe). Some will never be collected, so at
period end an estimated **bad-debt expense** is recorded against an **allowance for doubtful
debts** (a contra-asset that reduces receivables). Actual write-offs later reduce both the
allowance and the receivable. Collection speed is measured by receivables turnover and days.

## Concepts and rules
- Bad debts are estimated (percentage of receivables from experience, or specific known
  accounts) and expensed in the period of the sale (matching). [ANA ch.6]
- Distinguish **bad** (reasonably certain not to pay → write off) from **doubtful** (create an
  allowance). [FADM ch.3]
- Under IFRS 9 / Ind AS 109, receivable impairment uses expected credit losses; the simplified
  approach (lifetime ECL, provision matrix by ageing) is from the IFRS 9 text, not the source summary — verify. [IFRS, IFRS 9]
- Bad-debt expense reduces net income without using cash. [ANA ch.6]
- Receivables turnover = credit sales / average receivables; collection period = 365 / turnover. [AMS ch.6]

## Journal entries (Dr / Cr)
| Event | Debit | Credit |
| --- | --- | --- |
| Credit sale | Customer (A/R) | Sales (+ GST output [IN]) |
| Period-end estimate | Bad debts expense | Allowance for doubtful debts |
| Write off a specific customer | Allowance for doubtful debts | Customer (A/R) |
| Direct write-off (small businesses) | Bad debts expense | Customer (A/R) |
| Recovery of a written-off debt | Bank | Bad debts recovered (income) |

## What this means for our product
- Party ledger with credit limit, credit days, and ageing buckets (0–30, 31–60, 61–90, 90+).
- Bill-by-bill tracking (which invoice a receipt settles) for accurate ageing and interest.
- Reminders (SMS/WhatsApp) driven by due dates; "udhaar" view for small shops is the same data.
- Bad-debt provisioning helper: suggest provision by ageing bucket; write-off wizard.
- [IN] Write-offs may affect GST (no automatic GST reversal on bad debt) — check before design.
