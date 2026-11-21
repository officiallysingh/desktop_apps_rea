---
name: india-validators
description: Exact validation rules for Indian identifiers and document fields (GSTIN check digit, PAN, TAN, IFSC, HSN length, state codes, invoice-number format). Use when specifying validations, migration checks, or tests that involve these fields.
---
# Indian field validators

Reference specs for validating Indian identifiers. Use in specs, `interop/` migration validation,
`scripts/clean_room_check.py`-style checks, and acceptance tests. Verify against official sources
where tagged; see `_knowledge/india/` and `wishlist.md`.

## PAN
- Format: `[A-Z]{5}[0-9]{4}[A-Z]` (10 chars).
- 4th char = holder type (P individual, C company, H HUF, F firm, A AOP, T trust, B BOI, L local
  authority, J artificial juridical person, G government).
- 5th char = first letter of surname (individual) or entity name.

## GSTIN (15 chars)
- Format: `[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]`.
- Chars 1-2 = state code (see below); 3-12 = PAN of the registrant; 13 = entity number for that
  PAN in the state; 14 = `Z` (default); 15 = check digit.
- **Check digit (char 15)**: alphanumeric mod-36.
  - Alphabet: `0-9` then `A-Z` = values 0..35.
  - For each of the first 14 chars at position i (1-based): v = value(char); factor = 1 if i odd,
    2 if i even; p = v * factor; add (p / 36) + (p % 36) to the sum.
  - checksum = (36 - (sum % 36)) % 36; the 15th char must equal value->char(checksum).

## TAN (for TDS)
- Format: `[A-Z]{4}[0-9]{5}[A-Z]` (10 chars). First 3 = city code, 4th = first letter of deductor name.

## IFSC
- Format: `[A-Z]{4}0[A-Z0-9]{6}` (11 chars). Chars 1-4 = bank code, 5 = `0` (reserved), 6-11 = branch.

## HSN / SAC
- Numeric. Digits required on invoices depend on turnover (see `_knowledge/india/gst-core-rules.md`):
  <= Rs 5 crore -> 4 digits B2B; > Rs 5 crore -> 6 digits. SAC (services) is 6 digits.

## State codes (GST, char 1-2 of GSTIN) — key ones
01 J&K, 02 HP, 03 Punjab, 04 Chandigarh, 05 Uttarakhand, 06 Haryana, 07 Delhi, 08 Rajasthan,
09 UP, 10 Bihar, 19 West Bengal, 22 Chhattisgarh, 23 MP, 24 Gujarat, 27 Maharashtra, 29 Karnataka,
32 Kerala, 33 Tamil Nadu, 36 Telangana, 37 Andhra Pradesh. (Full list: verify against CBIC.)

## Invoice number (GST, CGST Rule 46)
- <= 16 chars; letters, digits, `-`, `/` only; unique per financial year per series.

Reference Python (illustrative; put real validators in the product repo):
```python
import re
_V = {c: i for i, c in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
def gstin_check_digit(first14: str) -> str:
    total = 0
    for i, ch in enumerate(first14):            # i = 0-based
        p = _V[ch] * (2 if (i + 1) % 2 == 0 else 1)
        total += p // 36 + p % 36
    return "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(36 - total % 36) % 36]
def valid_gstin(g: str) -> bool:
    return bool(re.fullmatch(r"[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]", g)) and g[14] == gstin_check_digit(g[:14])
```
