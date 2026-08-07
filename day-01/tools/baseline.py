#!/usr/bin/env python3
"""
Day-1 baseline capture — the machine measures, you don't.

Slide 20 of Day 1 is the METR result: developers felt 20% faster and were
measured 19% slower. The lesson is that self-report is inadmissible. So this
tool takes the three numbers a human would otherwise estimate — elapsed time,
diff size, files touched — straight from the clock and from git, and asks you
only for the two it genuinely cannot see: defects found in a real review, and
tokens off the tool's own meter.

    ./baseline.py start unassisted      # begins a run, records the git ref
    ...do the task...
    ./baseline.py stop                  # captures time + diff, asks for defects

    ./baseline.py start chat
    ./baseline.py stop
    ./baseline.py start agentic
    ./baseline.py stop

    ./baseline.py row                   # prints your row, ready to paste into
                                        # the workbook's "Day 1 Baseline" sheet
    ./baseline.py evidence              # writes evidence/day1-baseline.json

State lives in .adlc/baseline.json inside the repo, so it survives a closed
terminal and can be committed as evidence.
"""

import json
import os
import subprocess
import sys
import time

MODES = ("unassisted", "chat", "agentic")
STATE_DIR = ".adlc"
STATE = os.path.join(STATE_DIR, "baseline.json")


def sh(*args):
    try:
        return subprocess.run(args, capture_output=True, text=True,
                              check=False, timeout=30).stdout.strip()
    except Exception:
        return ""


def repo_root():
    root = sh("git", "rev-parse", "--show-toplevel")
    if not root:
        sys.exit("not inside a git repository — run this from the practice repo")
    return root


def load():
    if os.path.exists(STATE):
        with open(STATE) as fh:
            return json.load(fh)
    return {"participant": "", "role": "", "task": "", "runs": {}, "open": None}


def save(d):
    os.makedirs(STATE_DIR, exist_ok=True)
    with open(STATE, "w") as fh:
        json.dump(d, fh, indent=2)


def diff_stat(since_ref):
    """Lines changed and files touched since the ref the run started from.
    Counts working-tree changes too, so it works before you commit."""
    out = sh("git", "diff", "--numstat", since_ref)
    added = removed = files = 0
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        if parts[2].startswith(".adlc/"):
            continue        # the tool's own state file is not task work
        files += 1
        a, r = parts[0], parts[1]          # "-\t-" for binary files
        added += int(a) if a.isdigit() else 0
        removed += int(r) if r.isdigit() else 0
    return added + removed, files


def ask(prompt, cast=int, allow_blank=True):
    while True:
        v = input(prompt).strip()
        if not v and allow_blank:
            return None
        try:
            return cast(v)
        except ValueError:
            print("  that isn't a number — try again, or press Enter to skip")


def cmd_start(mode):
    if mode not in MODES:
        sys.exit(f"mode must be one of: {', '.join(MODES)}")
    d = load()
    if d.get("open"):
        sys.exit(f"run '{d['open']['mode']}' is still open — ./baseline.py stop first")
    if not d["participant"]:
        d["participant"] = input("Your name: ").strip()
        d["role"] = input("Role (PM / Dev Lead / QA Lead / ...): ").strip()
        d["task"] = input("Task ID — the one controlled change: ").strip()
    ref = sh("git", "rev-parse", "HEAD")
    d["open"] = {"mode": mode, "t0": time.time(), "ref": ref}
    save(d)
    print(f"\n  {mode} run started. Clock is running.")
    print(f"  baseline is commit {ref[:8]}")
    print("  do the task, then: ./baseline.py stop\n")


def cmd_stop():
    d = load()
    run = d.get("open")
    if not run:
        sys.exit("no run is open — ./baseline.py start <mode>")
    minutes = round((time.time() - run["t0"]) / 60, 1)
    # New files start untracked, and `git diff` does not see untracked files.
    # The baseline task creates new files, so stage everything first — otherwise
    # the diff column under-reports exactly the work we are trying to measure.
    sh("git", "add", "-A")
    loc, files = diff_stat(run["ref"])
    print(f"\n  measured automatically")
    print(f"    time         {minutes} min")
    print(f"    diff size    {loc} lines across {files} file(s)")
    print("\n  the two the machine can't see —")
    print("  (defects: from a REAL review pass, not a glance. Enter to skip.)")
    defects = ask("    defects found in review: ", int)
    tokens = None
    if run["mode"] != "unassisted":
        tokens = ask("    tokens, off the tool's meter: ", int)
    d["runs"][run["mode"]] = {"minutes": minutes, "loc": loc, "files": files,
                              "defects": defects, "tokens": tokens}
    d["open"] = None
    save(d)
    done = [m for m in MODES if m in d["runs"]]
    print(f"\n  saved. runs complete: {', '.join(done)}")
    left = [m for m in MODES if m not in d["runs"]]
    print(f"  still to do: {', '.join(left)}\n" if left else
          "\n  all three done — ./baseline.py row\n")


def cmd_row():
    d = load()
    if not d["runs"]:
        sys.exit("nothing measured yet")
    g = lambda m, k: (d["runs"].get(m) or {}).get(k)
    fmt = lambda v: "SKIPPED" if v is None else v
    cells = [d["participant"], d["role"], d["task"],
             *[fmt(g(m, "minutes")) for m in MODES],
             *[fmt(g(m, "loc")) for m in MODES],
             *[fmt(g(m, "defects")) for m in MODES],
             fmt(g("chat", "tokens")), fmt(g("agentic", "tokens"))]
    print("\n  Your row — copy this whole line and paste into cell A5 (or the")
    print("  first empty row) of the 'Day 1 Baseline' sheet. Excel will split")
    print("  it across the columns by itself.\n")
    print("\t".join(str(c) for c in cells))
    missing = [m for m in MODES if m not in d["runs"]]
    if missing:
        print(f"\n  note: {', '.join(missing)} not run — those cells say SKIPPED,")
        print("  which is the honest answer. Do not invent a number.")
    print()


def cmd_evidence():
    d = load()
    os.makedirs("evidence", exist_ok=True)
    path = "evidence/day1-baseline.json"
    with open(path, "w") as fh:
        json.dump(d, fh, indent=2)
    print(f"\n  wrote {path}")
    print("  commit it — that file IS your evidence, not a screenshot.\n")
    print(f"    git add {path} && git commit -m 'Day 1 baseline: {d['participant']}'\n")


def cmd_status():
    d = load()
    print(f"\n  {d['participant'] or '(no name yet)'} · {d['role']} · task {d['task']}")
    for m in MODES:
        r = d["runs"].get(m)
        if r:
            tok = f" · {r['tokens']} tokens" if r["tokens"] is not None else ""
            dfx = "?" if r["defects"] is None else r["defects"]
            print(f"    {m:<11} {r['minutes']:>6} min · {r['loc']:>5} loc · {dfx} defects{tok}")
        else:
            print(f"    {m:<11} not run")
    if d.get("open"):
        el = round((time.time() - d["open"]["t0"]) / 60, 1)
        print(f"\n    '{d['open']['mode']}' is RUNNING — {el} min elapsed")
    print()


def main():
    repo_root()
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    cmd = args[0]
    if cmd == "start" and len(args) > 1:
        cmd_start(args[1])
    elif cmd == "stop":
        cmd_stop()
    elif cmd == "row":
        cmd_row()
    elif cmd == "evidence":
        cmd_evidence()
    elif cmd == "status":
        cmd_status()
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
