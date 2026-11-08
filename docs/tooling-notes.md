# Tooling notes (Windows analysis machine)

Record which rea tools work on Windows and any workarounds.

| Capability | rea tool | Works? | Fallback | Notes |
| --- | --- | --- | --- | --- |
| Binary overview | binary_overview | | | |
| PE imports / resources | inspect_pe_imports / inspect_pe_resources | | | |
| .NET inspection | inspect_managed_artifact | | ilspycmd | |
| Native decompile | procedure_pseudo_code | | Ghidra | |
| SQLite | inspect_sqlite_database | | DB Browser | |
| Native UI observation | observe_native_ui | | FlaUInspect / Accessibility Insights | |
| Process scenario capture | capture_process_scenario | | ProcMon | |
| Runtime hooks | instrument_with_frida | | frida CLI | |
| Network | — | | Fiddler / Wireshark | |
