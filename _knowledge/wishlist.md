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
| Income-tax **Rules** 2026 (forms 130–168) and old→new section mapping table — Act text obtained | incometax.gov.in | india/income-tax-tds.md |
| Schedule III (Div. I & II) + 2021 amendment | mca.gov.in | india/companies-act-icai.md |
| Companies (Accounts) Rules 2014 (Rule 3) | mca.gov.in | india/companies-act-icai.md |
| ICAI Accounting Standards compendium; **current** ICAI BoS study material (Accounting incl. Vol. 1, Taxation, Costing) — older Advanced Accounting Vol. 2 obtained | icai.org, BoS knowledge portal | many |
| Tally XML integration pages (save as PDF) | help.tallysolutions.com/xml-integration | .claude/skills/tally-xml-export |

## Books — purchase needed (copyrighted; cannot be downloaded)
| Book | Why |
| --- | --- |
| V.S. Datey — GST Ready Reckoner (Taxmann), **latest** edition — the copy we have is a June 2017 pre-launch printout | Practical GST with examples |
| Singhania & Singhania — Students' Guide to Income Tax including GST (Taxmann), edition for the 2025 Act | Income tax + GST; CompuTax domain |
| Tally Education — Official Guide to Financial Accounting using TallyPrime | Indian SMB practice, Tally's model |
Obtained and processed: Fowler (Analysis Patterns), Kleppmann (DDIA), Muller (Inventory), ICAI
Advanced Accounting Vol. 2 (covers most of Gupta & Radhaswamy's scope), Income-tax Act 2025 text.

Put PDFs in `_reference/books/`, extract text to `_reference/text/`, then run `/knowledge`.
