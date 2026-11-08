#!/usr/bin/env python3
"""
Clean-room check: run before committing.

Scans files that git would commit (changed + untracked, excluding .gitignore'd paths) for:
  1. Real-looking client personal data: PAN, GSTIN, Aadhaar, Indian mobile numbers, e-mail, IFSC + account.
  2. Vendor identifiers: every vendor name listed in _raw/*/name-mapping.md (first column of tables,
     and `vendor_name -> our_name` lines).
  3. Files that must never be committed (binaries, databases, captures, screenshots in app folders).

Usage:  python scripts/clean_room_check.py [--all] [paths...]
        --all   scan every tracked + untracked file, not just changed ones
Exit code 1 if anything is found. Allow a false positive by adding `clean-room: ok` on that line.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEXT_EXT = {".md", ".sql", ".mmd", ".json", ".txt", ".csv", ".kt", ".java", ".xml", ".yml", ".yaml", ".py", ".ps1"}
FORBIDDEN_EXT = {".exe", ".dll", ".msi", ".mdb", ".accdb", ".mdf", ".ldf", ".fdb", ".gdb", ".db", ".sqlite",
                 ".sqlite3", ".dbf", ".bak", ".pml", ".pcap", ".pcapng", ".saz", ".dmp", ".har", ".apk"}
SKIP_DIRS = ("_raw/", "_reference/", ".git/", "_templates/", "_knowledge/_template.md")

PATTERNS = {
    "PAN": re.compile(r"\b[A-Z]{3}[PCHFATBLJG][A-Z][0-9]{4}[A-Z]\b"),
    "GSTIN": re.compile(r"\b[0-3][0-9][A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]\b"),
    "Aadhaar": re.compile(r"\b[2-9][0-9]{3}[ -]?[0-9]{4}[ -]?[0-9]{4}\b"),
    "Mobile": re.compile(r"(?<![\d.])(?:\+91[ -]?|0)?[6-9][0-9]{4}[ -]?[0-9]{5}(?![\d.])"),
    "Email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "IFSC": re.compile(r"\b[A-Z]{4}0[A-Z0-9]{6}\b"),
}
# Obvious placeholders / examples we write ourselves
ALLOW_VALUES = re.compile(r"(ABCDE1234F|AAAAA0000A|22AAAAA0000A1Z5|27ABCDE1234F1Z5|9999999999|9876543210|"
                          r"example\.(com|in)|noreply@anthropic\.com|@example|XXXX)", re.I)


def git_files(all_files: bool):
    def run(*args):
        r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
        return [l for l in r.stdout.splitlines() if l.strip()]
    if all_files:
        files = run("ls-files") + run("ls-files", "--others", "--exclude-standard")
    else:
        files = run("diff", "--name-only", "HEAD") if run("rev-parse", "--verify", "HEAD") else []
        files += run("diff", "--name-only", "--cached")
        files += run("ls-files", "--others", "--exclude-standard")
    return sorted(set(files))


def vendor_terms():
    terms = set()
    raw = os.path.join(ROOT, "_raw")
    if not os.path.isdir(raw):
        return terms
    for app in os.listdir(raw):
        p = os.path.join(raw, app, "name-mapping.md")
        if not os.path.isfile(p):
            continue
        with open(p, encoding="utf-8", errors="ignore") as f:
            for line in f:
                m = re.match(r"^\s*\|\s*`?([^|`]+?)`?\s*\|", line)
                if m and not set(m.group(1).strip()) <= set("-: ") and m.group(1).strip().lower() not in ("vendor", "vendor name", "vendor table/column", "vendor identifier"):
                    terms.add(m.group(1).strip())
                m = re.match(r"^\s*[-*]?\s*`?([A-Za-z_][\w.]{3,})`?\s*(->|→)", line)
                if m:
                    terms.add(m.group(1))
    # ignore very short or generic terms
    return {t for t in terms if len(t) >= 4 and not t.isdigit()}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = args or git_files("--all" in sys.argv)
    terms = vendor_terms()
    term_re = re.compile(r"(?<![A-Za-z0-9_])(" + "|".join(re.escape(t) for t in sorted(terms, key=len, reverse=True)) + r")(?![A-Za-z0-9_])") if terms else None
    findings = []
    for rel in files:
        rel_n = rel.replace("\\", "/")
        if rel_n.startswith(SKIP_DIRS) or rel_n.endswith("clean_room_check.py"):
            continue
        ext = os.path.splitext(rel_n)[1].lower()
        if ext in FORBIDDEN_EXT:
            findings.append((rel_n, 0, "forbidden file type", ext))
            continue
        if re.search(r"/03-screens/.*\.(png|jpe?g|json)$|/sample-outputs/(?!\.gitkeep)", rel_n):
            findings.append((rel_n, 0, "screenshot/UI dump/report output in app folder", "move to _raw/"))
            continue
        if ext not in TEXT_EXT:
            continue
        path = os.path.join(ROOT, rel_n)
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8", errors="ignore") as f:
            for no, line in enumerate(f, 1):
                if "clean-room: ok" in line:
                    continue
                for kind, rx in PATTERNS.items():
                    for m in rx.finditer(line):
                        if not ALLOW_VALUES.search(m.group(0)):
                            findings.append((rel_n, no, kind, m.group(0)))
                if term_re:
                    for m in term_re.finditer(line):
                        findings.append((rel_n, no, "vendor identifier", m.group(0)))
    if not findings:
        print(f"clean-room check: OK ({len(files)} files, {len(terms)} vendor terms)")
        return 0
    for rel, no, kind, val in findings:
        print(f"{rel}:{no}: {kind}: {val}")
    print(f"\nclean-room check: {len(findings)} finding(s). Fix them, or mark a false positive with 'clean-room: ok'.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
