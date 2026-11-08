---
topic: Audits and audit trail
capabilities: [USR-ROLES, SYS-AUDIT]
sources: [ANA]
---
# Audits and audit trail

## In one paragraph
An audit is an independent examination of financial statements leading to an opinion on
whether they are fairly presented. Auditors rely on being able to trace every figure back to
source documents and every change to who made it. [ANA ch.11]

## Concepts and rules
- Types of auditors: external/independent, internal, government; standard (unqualified)
  opinion vs qualified, adverse, disclaimer. [ANA ch.11]
- Audits are useful even when not mandatory: lenders and investors rely on them. [ANA ch.11]
- [IN] Proviso to Rule 3(1), Companies (Accounts) Rules: from FY starting 1 Apr 2023 accounting
  software must keep an audit trail and edit log that cannot be disabled; retained 8 years;
  auditors report under Rule 11(g). Details: india/companies-act-icai.md.

## What this means for our product
- Immutable audit log: who, when, what changed (before/after), from which device; cannot be
  turned off; exportable for auditors.
- Posted vouchers never hard-deleted: cancellation/reversal with reason.
- Period lock (books closed up to a date) with role-based override that is itself logged.
- Auditor role: read-only access to everything incl. the audit log.
