# Sources we don't have yet (priority order)

## Official / free (highest value: current, authoritative, machine-readable)
| Source | Why | Capabilities |
| --- | --- | --- |
| CBIC: CGST/IGST Acts, CGST Rules, rate notifications | GST rules (place of supply, ITC, credit/debit notes, RCM) | GST-CALC, GST-RETURNS |
| GSTN: GSTR-1 / GSTR-3B / GSTR-2B JSON schemas and offline tool | Exact return formats to generate/import | GST-RETURNS |
| NIC e-invoice (IRP) and e-way bill API specs and JSON schema | IRN, QR, e-way bill integration | GST-EINV |
| Income Tax Dept: ITR JSON schemas + utilities; TDS (Protean/TRACES) FVU file formats | CompuTax domain: ITR and TDS returns | TAX-ITR, TAX-TDS |
| ICAI: Accounting Standards (AS) compendium; Ind AS; Guidance Note on Schedule III; Guidance Note on audit trail | Indian rules that override IFRS/US material | RPT-FINANCIAL, SYS-AUDIT |
| ICAI Board of Studies study material (Foundation/Intermediate: Accounting, Taxation, Cost & Management Accounting) | Free, updated yearly, Indian syllabus incl. GST and income tax | many |
| MCA: Companies Act Schedule II (useful lives), Schedule III, Companies (Accounts) Rules (audit trail) | Depreciation and statement formats | FA-ASSETS, RPT-FINANCIAL, SYS-AUDIT |
| EPFO / ESIC / state professional-tax rules | Indian payroll statutory deductions | PAY-PAYROLL |
| Tally help (help.tallysolutions.com), TDL reference, XML/ODBC integration docs; BUSY and Marg help centres | Official feature behaviour of the apps we analyse; Tally XML is our read interface | all |

## Books
| Book | Why |
| --- | --- |
| V.S. Datey — *GST Ready Reckoner* (Taxmann) | Practical GST rules with examples |
| Vinod K. Singhania & Monica Singhania — *Students' Guide to Income Tax including GST* (Taxmann) | Income tax + GST together; good for CompuTax |
| Girish Ahuja & Ravi Gupta — *Systematic Approach to Income Tax* | Alternative income-tax reference |
| R.L. Gupta & M. Radhaswamy — *Advanced Accountancy* (Sultan Chand), or Shukla & Grewal — *Advanced Accounts* (S. Chand) | Indian-format accounting: partnerships, branches, consignment, hire purchase, Indian AS |
| Tally Education — *Official Guide to Financial Accounting using TallyPrime* | How Indian SMB accounting is done in practice, Tally's model |
| Martin Fowler — *Analysis Patterns* (accounting patterns: Account, Entry, Posting Rule) | Domain modelling for our posting engine |
| Max Muller — *Essentials of Inventory Management*; David Piasecki — *Inventory Management Explained* | Reorder logic, cycle counts, valuation in practice (Marg/BUSY) |
| Martin Kleppmann — *Designing Data-Intensive Applications*; Ink & Switch — "Local-first software" essay (free) | Sync, replication, conflict handling for our architecture |

Check editions: tax books must match the current assessment year / latest Finance Act.
