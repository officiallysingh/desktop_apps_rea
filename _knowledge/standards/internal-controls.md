---
topic: Internal controls, fraud risks and IT controls
capabilities: [USR-ROLES, SYS-AUDIT, SYS-BACKUP, VCH-NUMBERING, PTY-MASTER]
sources: [AIS]
---
# Internal controls

## In one paragraph
Controls are preventive, detective or corrective (PDC model). The COSO / SAS 78 framework has
five components: control environment, risk assessment, information and communication,
monitoring, and control activities. The six physical control activities are transaction
authorisation, segregation of duties, supervision, adequate accounting records, access
control and independent verification. [AIS ch.3]

## Concepts and rules
- Employee fraud converts assets for personal gain by getting around controls; management
  fraud misstates reports by overriding controls. [AIS ch.3]
- Known schemes: **lapping** (hiding stolen customer cash by applying later receipts to earlier
  accounts), fictitious suppliers, duplicate payments, ghost employees, kickbacks. [AIS ch.3–6]
- Computers merge tasks that used to be separated (authorise vs process), so program integrity
  and access control replace some manual segregation. [AIS ch.4, ch.5]
- PC/SMB accounting systems' biggest exposures: no segregation of duties, weak access control,
  and backups that depend on people remembering. [AIS ch.4]
- Input controls: check digits on codes, validation (range, limit, reasonableness), batch
  totals and record counts; processing controls; output controls. [AIS ch.8, ch.16]
- Coding schemes for accounts/items: sequential, block, group, alphabetic, mnemonic — each
  with trade-offs in readability and room for growth. [AIS ch.8]

## What this means for our product
- Roles and permissions per action (create / approve / post / cancel / view cost price /
  edit past periods) and maker-checker approval for payments, credit notes, price changes.
- Built-in detective reports: duplicate supplier invoices (same supplier + number/amount/date),
  gaps in voucher numbers, receipts applied out of order (lapping pattern), new suppliers with
  bank details matching an employee, edits after posting.
- Party master change log (bank account changes are a top fraud vector) with approval.
- Automatic scheduled backups (pen drive / cloud) that don't rely on the user — confirmed
  by our target architecture.
- Validation everywhere: GSTIN check digit, PAN format, HSN validity, IFSC format.
- Period lock and immutable audit log (see concepts/audit-and-audit-trail.md).
