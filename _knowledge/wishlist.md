# Sources still to obtain

Notes from official sources were written on 2026-11-08 from secondary summaries (see
`india/`). The authoritative files themselves could not be downloaded from here (government sites
are blocked from this machine's shell). Download them manually into `_reference/official/` and run
`/knowledge` on each to replace "[verify]" tags with exact citations.

## Official / free — download manually
| File | Where | Replaces [verify] in |
| --- | --- | --- |
| CGST Act + CGST Rules (latest consolidated) | cbic-gst.gov.in → GST Acts / Rules | india/gst-core-rules.md |
| GST rate notifications (22 Sep 2025 onward) + HSN rate schedule | cbic-gst.gov.in → Notifications (Rate) | india/gst-core-rules.md |
| E-invoice schema (INV-01 JSON + validation rules) and API spec | einvoice1.gst.gov.in, einv-apisandbox.nic.in | india/gst-einvoice-ewaybill-returns.md |
| E-way bill API spec | ewaybillgst.gov.in (developer portal) | same |
| GSTR-1 / GSTR-2B / GSTR-3B JSON (offline tool + sample JSON) | gst.gov.in → Downloads → Offline tools | same |
| ITR JSON schemas + validation rules (current year) | incometax.gov.in → Downloads | india/income-tax-tds.md |
| TDS/TCS return file format (RPU/FVU) for new forms 138/140/143/144 | Protean (TIN) site | india/income-tax-tds.md |
| Income-tax Act 2025 + Rules 2026 (section mapping tables) | incometax.gov.in | india/income-tax-tds.md |
| Schedule III (Div. I & II) + 2021 amendment | mca.gov.in | india/companies-act-icai.md |
| Companies (Accounts) Rules 2014 (Rule 3) | mca.gov.in | india/companies-act-icai.md |
| ICAI Accounting Standards compendium; ICAI BoS study material (Accounting, Taxation, Costing) | icai.org, BoS knowledge portal | many |
| Tally XML integration pages (save as PDF) | help.tallysolutions.com/xml-integration | .claude/skills/tally-xml-export |

## Books — purchase needed (copyrighted; cannot be downloaded)
| Book | Why |
| --- | --- |
| V.S. Datey — GST Ready Reckoner (Taxmann), latest edition | Practical GST with examples |
| Singhania & Singhania — Students' Guide to Income Tax including GST (Taxmann), edition for the 2025 Act | Income tax + GST; CompuTax domain |
| R.L. Gupta & M. Radhaswamy — Advanced Accountancy (Sultan Chand) | Indian-format accounting (partnership, branches, consignment) |
| Tally Education — Official Guide to Financial Accounting using TallyPrime | Indian SMB practice, Tally's model |
| Martin Fowler — Analysis Patterns (accounting patterns) | Posting engine design (also free articles on martinfowler.com) |
| Max Muller — Essentials of Inventory Management, or David Piasecki — Inventory Management Explained | Inventory practice |
| Martin Kleppmann — Designing Data-Intensive Applications | Sync and replication |
Put PDFs in `_reference/books/`, extract text to `_reference/text/`, then run `/knowledge`.
