# Shared domain model

Unified entities reconciled across all apps. Our names only.

```mermaid
erDiagram
    COMPANY ||--o{ FINANCIAL_YEAR : has
    COMPANY ||--o{ PARTY : has
    COMPANY ||--o{ LEDGER : has
    COMPANY ||--o{ ITEM : has
    FINANCIAL_YEAR ||--o{ VOUCHER : contains
    VOUCHER ||--|{ VOUCHER_LINE : has
    VOUCHER }o--|| PARTY : with
    VOUCHER_LINE }o--o| ITEM : for
```

## Entities
| Entity | Purpose | Source apps | Notes |
| --- | --- | --- | --- |

## Sync-readiness conventions
- UUID primary keys, `created_at`, `updated_at`, `version`, `deleted` (soft delete)
- Change log table per company for sync
