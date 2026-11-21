#!/usr/bin/env python3
"""
Traceability check: find gaps before writing a BRD.

Reports, as plain lines (file:line: issue):
  * business rules with no [evidence: ...] / [inferred] / [static] tag
  * business rules / screens with no [cap: ID] or "Capability IDs:" reference
  * capability IDs used anywhere that are not defined in capability-taxonomy.md
  * capability IDs defined but absent from capability-matrix.md
  * matrix cells with a depth (B/A) but no link to a spec
  * overlap files with no "Our design" section
Exit code 1 if any gap is found. Advisory only; it never blocks.

Usage: python scripts/traceability_check.py
"""
import os, re, sys, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT)
findings = []
def add(f, n, msg): findings.append(f"{f}:{n}: {msg}")

def read(p):
    try:
        return open(p, encoding="utf-8", errors="ignore").read()
    except OSError:
        return ""

CAP_RE = re.compile(r"\b([A-Z]{2,4}-[A-Z0-9]{2,12})\b")
EVID_RE = re.compile(r"\[(evidence|inferred|static|verify|knowledge):", re.I)

# defined capability IDs
tax = read("_platform/capability-taxonomy.md")
defined = set()
for line in tax.splitlines():
    m = re.match(r"\|\s*([A-Z]{2,4}-[A-Z0-9]{2,12})\s*\|", line)
    if m: defined.add(m.group(1))

# apps in scope
apps = [d for d in os.listdir(".") if os.path.isfile(os.path.join(d, "PROGRESS.md")) and not d.startswith("_")]

# business rules: evidence + capability tags
for app in apps:
    for f in glob.glob(f"{app}/05-business-rules/*.md"):
        if os.path.basename(f).startswith("_"): continue
        txt = read(f)
        has_cap = "cap:" in txt or "Capability IDs" in txt or CAP_RE.search(txt)
        for n, line in enumerate(txt.splitlines(), 1):
            if re.match(r"^#{2,3}\s", line) and not EVID_RE.search(txt):
                add(f, n, "rule section without any evidence tag")
                break
        if not has_cap:
            add(f, 1, "no capability ID referenced")

# unknown capability IDs referenced anywhere in specs/platform
for f in glob.glob("*/0*-*.md") + glob.glob("*/0*/*.md") + glob.glob("_platform/*.md"):
    txt = read(f)
    for n, line in enumerate(txt.splitlines(), 1):
        for cid in CAP_RE.findall(line):
            if cid not in defined and cid not in ("CGST-ACT",):  # ignore source codes
                add(f, n, f"capability ID not in taxonomy: {cid}")
                break

# matrix coverage
matrix = read("_platform/capability-matrix.md")
in_matrix = set(CAP_RE.findall(matrix))
for cid in sorted(defined - in_matrix):
    add("_platform/capability-matrix.md", 1, f"capability not in matrix: {cid}")
for n, line in enumerate(matrix.splitlines(), 1):
    if "|" in line and re.search(r"\|\s*[BA]\b", line) and "](" not in line and not line.strip().startswith("| ID"):
        if re.match(r"\|\s*[A-Z]{2,4}-", line):
            add("_platform/capability-matrix.md", n, "matrix cell has depth B/A but no spec link")

# overlaps have a design
for f in glob.glob("_platform/overlaps/*.md"):
    if os.path.basename(f).startswith("_"): continue
    if "our design" not in read(f).lower():
        add(f, 1, "overlap has no 'Our design' section")

if findings:
    print("\n".join(findings))
    print(f"\ntraceability: {len(findings)} gap(s). Advisory — fix before writing the BRD.")
    sys.exit(1)
print(f"traceability: OK ({len(apps)} apps, {len(defined)} capabilities defined)")
