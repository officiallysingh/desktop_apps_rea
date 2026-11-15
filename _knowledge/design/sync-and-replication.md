---
topic: Local-first sync, replication and data evolution
capabilities: [SYS-SYNC, SYS-BACKUP, VCH-NUMBERING, SYS-AUDIT]
sources: [DDIA]
---
# Sync and replication design (DDIA)

Kleppmann's *Designing Data-Intensive Applications* frames our target architecture exactly:
every device holding a local database that accepts writes is **multi-leader replication with
offline clients** — "each device is a datacenter" with a very unreliable network, and the
history of broken calendar sync shows how hard it is to get right. [DDIA ch.5]

## Concepts and rules
- Replication purposes: availability, **disconnected operation**, latency, read scale. [DDIA ch.5]
- Approaches: single-leader, multi-leader, leaderless. Offline devices = multi-leader;
  replication lag can be hours or days. [DDIA ch.5]
- **Conflict avoidance**: route all writes for a record to one "home" leader — best strategy when
  possible; breaks down when the home changes. [DDIA ch.5]
- Convergence is mandatory: all replicas must end in the same state. Options: last-write-wins
  (simple but **silently loses data** — dangerous), merge values, record conflicts for the user,
  CRDTs, or app-specific merge. [DDIA ch.5]
- **Uniqueness needs consensus**: timestamps/causal ordering cannot guarantee that two nodes don't
  both claim the same unique value (the "unique username" example). Linearizable
  compare-and-set ≈ consensus. [DDIA ch.9]
- Causal consistency (happened-before, e.g. Lamport timestamps) is cheaper and tolerant of
  network problems; linearizability is slow under network delays. [DDIA ch.9]
- Encodings must be **backward and forward compatible** because old and new app versions run
  at the same time (devices upgrade at different times). JSON is loose on numbers — be careful
  with amounts; schema-based binary formats define compatibility rules. [DDIA ch.4]
- Treat the database's changes as a **log/stream** (change data capture, event sourcing);
  consumers derive state and can replay from an offset. [DDIA ch.11]
- Network requests can be retried: operations must be **idempotent** (dedupe with request ids). [DDIA ch.4, ch.12]

## What this means for our product
| Data | Strategy |
| --- | --- |
| Posted vouchers (invoices, receipts, journals) | **Append-only events, immutable once posted** → no write conflicts; corrections are new reversal/amendment events. Sync = exchange of new events. |
| Voucher numbers (GST needs unique numbers per FY) | Uniqueness needs coordination → avoid it: per-device series/prefix or number blocks leased from the hub (conflict avoidance), never "pick next number and hope". |
| Masters (party, item, ledger) | Field-level merge with version vectors; **flag true conflicts** (same field edited on two devices) for the user instead of silent LWW for important fields (GSTIN, bank details, rates). |
| Stock and balances | Derived from events; never synced as numbers; recomputed after merge. |
| Settings, price lists | Single "home" (the hub/admin) — conflict avoidance. |
- Every sync message carries an idempotency key; applying the same batch twice is harmless.
- Versioned sync schema with backward + forward compatibility; amounts as integer paise strings
  or integers, never floats.
- The change log doubles as the audit trail and the cloud-backup stream.
- Consider an existing engine (e.g. PowerSync, CRDT libraries) only where it supports these
  accounting-specific rules (immutable vouchers, numbering blocks).
