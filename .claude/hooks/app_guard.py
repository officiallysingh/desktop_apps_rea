#!/usr/bin/env python3
"""
PreToolUse guard for Claude Code: the analysed apps must keep working exactly as they are.

Blocks (exit code 2) only changes to the APPS and their DATA:
  * Write/Edit/delete/move/rename/redirect into app folders or files      (protected.json)
  * registry writes to app keys
  * stopping/killing/reconfiguring app processes and their DB services
  * SQL that writes to app databases (copies inside this repo are fine)
  * sqlite3 on a non-copy DB file without -readonly
  * uninstalling the apps

Everything else (installing tools, system settings, files elsewhere, rea runtime tools)
is allowed. What counts as "the app" is configured in .claude/protected.json.
Paths inside this repo are never protected.
"""
import json
import os
import re
import shlex
import sys

RAW_ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()


def norm(p: str) -> str:
    p = p.strip().strip('"').strip("'").replace("\\", "/")
    m = re.match(r"^/([a-zA-Z])/(.*)$", p)            # git-bash style /c/...
    if m:
        p = f"{m.group(1)}:/{m.group(2)}"
    p = re.sub(r"/+", "/", p)
    parts = []
    for seg in p.split("/"):
        if seg == "..":
            if parts:
                parts.pop()
        elif seg not in (".", ""):
            parts.append(seg)
    lead = "/" if p.startswith("/") else ""
    return (lead + "/".join(parts)).lower()


ROOT = norm(RAW_ROOT)


def is_abs(p: str) -> bool:
    q = p.strip().strip('"').strip("'")
    return bool(re.match(r"^([a-zA-Z]:[\\/]|/|\\\\|~|%|\$env:|\$home)", q, re.I))


def inside_repo(p: str) -> bool:
    q = p.strip().strip('"').strip("'")
    if not q:
        return True
    if re.match(r"^(~|%|\$env:|\$home|\\\\)", q, re.I):
        return False
    full = norm(q) if is_abs(q) else norm(RAW_ROOT.replace("\\", "/") + "/" + q)
    return full == ROOT or full.startswith(ROOT + "/")


def load_cfg() -> dict:
    try:
        with open(os.path.join(RAW_ROOT, ".claude", "protected.json"), encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


CFG = load_cfg()
KEYWORDS = [k.lower() for k in CFG.get("keywords", []) if k]
PATHS = [norm(p) for p in CFG.get("paths", []) if p]
DB_SERVICES = [k.lower() for k in CFG.get("db_services", [])]
DB_PROCESSES = [k.lower() for k in CFG.get("db_processes", [])]


def block(msg: str) -> None:
    print(f"BLOCKED by app-protection guard: {msg}. The analysed apps and their data must not change. "
          f"Work on a copy inside the repo (_raw/), or ask the user.", file=sys.stderr)
    sys.exit(2)


def is_regkey(t: str) -> bool:
    return bool(re.match(r"^\"?'?(hk(lm|cu|cr|u|cc)|hkey_)", t, re.I))


def protected(token: str) -> bool:
    """A path / registry key / process or service name belonging to a protected app.
    Paths inside this repo are never protected."""
    t = token.strip().strip('"').strip("'")
    if not t:
        return False
    low = t.lower()
    if is_regkey(t):
        return any(k in low for k in KEYWORDS)
    if re.search(r"[\\/]", t) or is_abs(t):
        if inside_repo(t):
            return False
        n = norm(t)
        if any(n == p or n.startswith(p + "/") for p in PATHS):
            return True
        return any(k in low or k in n for k in KEYWORDS)
    if os.path.exists(os.path.join(RAW_ROOT, t)):
        return False                                # a file/folder in this repo, e.g. tallyprime/
    return any(k in low for k in KEYWORDS)          # bare names: BahiKhata.exe, service names


def text_protected(seg: str) -> bool:
    return any(protected(t) for t in tokens(seg))


def tokens(seg: str):
    try:
        return shlex.split(seg, posix=False)
    except ValueError:
        return seg.split()


def segments(cmd: str):
    return [s for s in re.split(r"&&|\|\||;|\||\n", cmd) if s.strip()]


REG_WRITE = r"\breg(\.exe)?\s+(add|delete|import|copy|restore|load|unload)\b|\bregedit\b|\bregini\b|" \
            r"\b(new|set|remove|rename|clear|copy|move)-itemproperty\b|" \
            r"\b(set|new|remove|clear|rename|move)-item\b[^|;&]*\bhk(lm|cu|cr|u|cc)\b"
SVC_CTRL = r"\bsc(\.exe)?\s+(config|stop|start|delete|create|pause|continue|failure|sdset)\b|" \
           r"\bnet(\.exe)?\s+(stop|start|pause|continue)\b|" \
           r"\b(stop|start|restart|set|suspend|resume|remove)-service\b"
PROC_KILL = r"\btaskkill\b|\bstop-process\b|\bkill\b|\bwmic\b[^|;&]*\bprocess\b[^|;&]*\b(delete|terminate|call)\b"
UNINSTALL = r"\bmsiexec\b[^|;&]*(/x|/uninstall)|\bwinget\s+uninstall\b|\buninstall"
ACL = r"\bicacls\b|\bcacls\b|\btakeown\b|\battrib\b|\bset-acl\b"
FILE_MUTATORS = r"(^|\s)(rm|del|erase|rmdir|rd|mv|move|ren|rename|touch|tee|truncate|shred|" \
                r"remove-item|move-item|rename-item|new-item|set-content|add-content|clear-content|out-file|" \
                r"clear-item|set-item)(\s|$)"
COPIERS = r"(^|\s)(cp|copy|xcopy|robocopy|copy-item)(\s|$)"
SQL_SERVER_TOOLS = r"(^|\s|[\\/])(sqlcmd|osql|isql|isql-fb|bcp|mysql|psql|invoke-sqlcmd)(\.exe)?(\s|$)"
SQL_FILE_TOOLS = r"(^|\s|[\\/])(sqlite3|mdb-\w+)(\.exe)?(\s|$)"
SQL_WRITES = r"\b(insert|update|delete|drop|alter|create|truncate|merge|exec|execute|grant|revoke|deny|attach|" \
             r"detach|backup|restore|dbcc|replace|vacuum|reindex|shutdown|kill|reconfigure|bulk|into)\b|" \
             r"\bpragma\s+\w+\s*=|\b(sp|xp)_\w+|\.(import|restore|save|backup|clone|recover)\b|\bbcp\b[^|;&]*\bin\b"


def redirect_targets(seg: str):
    """Targets of > / >> that sit outside quotes (so XML like <A>b</A> inside quotes is ignored)."""
    out, q, i = [], None, 0
    while i < len(seg):
        ch = seg[i]
        if q:
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
        elif ch == ">":
            j = i + 1
            if j < len(seg) and seg[j] == ">":
                j += 1
            m = re.match(r"\s*(\"[^\"]+\"|'[^']+'|[^\s;&|]+)", seg[j:])
            if m:
                out.append(m.group(1))
                i = j + m.end()
                continue
        i += 1
    return out


def check_segment(seg: str) -> None:
    low = seg.lower()
    toks = tokens(seg.strip())

    if re.search(REG_WRITE, low) and text_protected(seg):
        block("registry write to an app key")

    if re.search(SVC_CTRL, low) and (text_protected(seg) or any(s in low for s in DB_SERVICES)):
        block("stopping/starting/reconfiguring an app or database service")

    if re.search(PROC_KILL, low) and (text_protected(seg) or any(p in low for p in DB_PROCESSES)):
        block("killing an app or database process")

    if re.search(UNINSTALL, low) and text_protected(seg):
        block("uninstalling an analysed app")

    if re.search(ACL, low) and any(protected(t) for t in toks[1:]):
        block("changing permissions/attributes of app files")

    # Tally XML/HTTP interface: export (read) requests only
    if re.search(r"(localhost|127\.0\.0\.1|::1)(:|%3a)9000", low) and re.search(r"import|alter|delete|cancel", low):
        block("Tally XML request that may import/alter/delete data (Export requests only)")

    # SQL
    if re.search(SQL_SERVER_TOOLS, low) and re.search(SQL_WRITES, low):
        block("SQL that may write to an app database (SELECT / catalog reads only)")
    if re.search(SQL_FILE_TOOLS, low):
        files = [t for t in toks[1:] if re.search(r"\.(db|sqlite3?|db3|mdb|accdb|fdb|gdb)\"?'?$", t, re.I)]
        live = [f for f in files if not inside_repo(f)]
        if live:
            if "-readonly" not in low and "mode=ro" not in low:
                block(f"opening an app database without -readonly: {live[0]} (copy it to _raw/ first)")
            if re.search(SQL_WRITES, low):
                block("SQL that may write to an app database")

    # find -delete / -exec rm on app folders
    if re.search(r"-delete\b|-exec(dir)?\s+(rm|del|mv)\b", low) and any(protected(t) for t in toks[1:]):
        block("deleting app files")

    # redirection into app folders
    for target in redirect_targets(seg):
        if target.lower() not in ("nul", "/dev/null", "$null", "&1", "&2") and protected(target):
            block(f"writing into an app file: {target}")

    if re.search(COPIERS, low):
        args = [t for t in toks[1:] if not t.startswith("-") and not re.match(r"^/[a-z]+(:\S*)?$", t, re.I)
                or re.match(r"^/[a-z]/", t, re.I)]
        if re.search(r"/(mov|move|mir|purge)\b|-move\b", low) and any(protected(a) for a in args):
            block("moving/mirroring app files")
        if args and protected(args[-1]):
            block(f"copying into an app folder: {args[-1]}")
        return

    if re.search(FILE_MUTATORS, low):
        hit = [t for t in toks[1:] if not t.startswith("-") and protected(t)]
        if hit:
            block(f"changing app files: {hit[0]}")


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        block("could not parse hook input (failing closed)")
    tool = data.get("tool_name", "") or ""
    inp = data.get("tool_input", {}) or {}

    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        path = inp.get("file_path") or inp.get("notebook_path") or ""
        if protected(path):
            block(f"{tool} on an app file: {path}")
        return

    cmd = inp.get("command")
    if isinstance(cmd, str) and cmd.strip():
        for seg in segments(cmd):
            check_segment(seg)


if __name__ == "__main__":
    main()
    sys.exit(0)
