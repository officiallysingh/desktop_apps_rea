# Interoperability spec (data migration)

The ONLY place where this app's data-format identifiers (table/column/field names, file layouts,
export formats) may be written — they are needed to read customers' own data for migration
(`_platform/data-migration.md`). Still no vendor code, no client data, no licence internals.

## Data locations
| Data | Where stored (file/DB/table) | Format/engine | Encrypted? |
| --- | --- | --- | --- |

## Built-in export options in the app
| Export | Menu path | Format | Covers |
| --- | --- | --- | --- |

## Field mapping to our migration format
| Our entity.field | Source location.field | Transform | Notes |
| --- | --- | --- | --- |

## Reconciliation reports in the app
Which reports to compare after migration (trial balance, stock summary, outstanding, GST summary)
and how to export them.

## Open questions
