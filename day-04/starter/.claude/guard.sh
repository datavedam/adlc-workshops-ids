#!/usr/bin/env bash
# PreToolUse guard for Day 4 — runs BEFORE the tool does.
#   exit 0 → allow.   exit 2 → BLOCK, and stderr goes back to the agent.
#
# Day 1 gave this hook two rules: stay inside the repository, and keep away from
# protected paths. Day 4 adds two more, and both come from the morning:
#   3. a credential must never reach a file
#   4. the tracker write contract is code, not advice
#
# A guard that only warns is worth nothing. By the second week nobody reads a
# warning. Every rule below refuses the action.
set -uo pipefail

payload=$(cat)
repo_root=$(git rev-parse --show-toplevel 2>/dev/null || pwd)

target=$(printf '%s' "$payload" | grep -o '"file_path"[[:space:]]*:[[:space:]]*"[^"]*"' \
         | head -1 | sed 's/.*:[[:space:]]*"//; s/"$//')
[ -z "$target" ] && exit 0

case "$target" in
  /*) abs="$target" ;;
  *)  abs="$repo_root/$target" ;;
esac
abs=$(python3 -c 'import os,sys; print(os.path.realpath(sys.argv[1]))' "$abs" 2>/dev/null || echo "$abs")
rel="${abs#"$repo_root"/}"

# ── 1. never write outside the repository ──────────────────────────────────
case "$abs" in
  "$repo_root"/*) ;;
  *) echo "BLOCKED  write outside the working directory" >&2
     echo "         target : $abs" >&2
     echo "         allowed: $repo_root/**" >&2
     exit 2 ;;
esac

# ── 2. never write to a protected path ─────────────────────────────────────
case "$rel" in
  .env|.env.*|secrets/*|.git/*|.github/workflows/*)
     echo "BLOCKED  protected path" >&2
     echo "         target : $rel" >&2
     exit 2 ;;
esac

# ── 3. never write a credential ────────────────────────────────────────────
# The content arrives in the same payload as the path, so the check costs
# nothing. Patterns stay narrow on purpose: a guard with false alarms gets
# switched off, and a guard that is off protects nothing.
content=$(printf '%s' "$payload" | python3 -c '
import json, sys
try:
    d = json.load(sys.stdin).get("tool_input", {})
except Exception:
    sys.exit(0)
parts = [d.get("content", ""), d.get("new_string", "")]
for e in d.get("edits", []) or []:
    parts.append(e.get("new_string", ""))
print("\n".join(p for p in parts if isinstance(p, str)))
' 2>/dev/null || true)

if [ -n "$content" ]; then
  secret=$(printf '%s' "$content" | grep -nEi \
    -e 'AKIA[0-9A-Z]{16}' \
    -e 'BEGIN [A-Z ]*PRIVATE KEY' \
    -e '(secret|password|passwd|api[_-]?key|token)[[:space:]]*[=:][[:space:]]*[A-Za-z0-9/+_-]{12,}' \
    -e 'xox[baprs]-[0-9A-Za-z-]{10,}' \
    -e 'gh[pousr]_[0-9A-Za-z]{20,}' | head -1 || true)
  if [ -n "$secret" ]; then
    echo "BLOCKED  the content carries a credential" >&2
    echo "         target : $rel" >&2
    echo "         line   : ${secret%%:*}" >&2
    echo "         Put the value in a secret store. Read it at run time." >&2
    exit 2
  fi
fi

# ── 4. the tracker write contract ──────────────────────────────────────────
# The agent proposes rows and records measurements. A delivery manager owns the
# capacity model. A workbook edit through a file write would bypass both.
case "$rel" in
  *.xlsx|*.xlsm)
     echo "BLOCKED  direct write to a workbook" >&2
     echo "         target : $rel" >&2
     echo "         Use tools/tracker.py. It writes A-P and AF-AP only," >&2
     echo "         and it never touches a formula column." >&2
     exit 2 ;;
esac

exit 0
