#!/usr/bin/env bash
# PreToolUse guard — runs BEFORE the tool does.
#   exit 0 → allow.   exit 2 → BLOCK, and stderr goes back to the agent.
# The point of Hour 2 is to watch this fire. If it only prints a warning and
# lets the write through, it is theatre — by Wednesday nobody reads warnings.
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

# 1. never write outside the repo
case "$abs" in
  "$repo_root"/*) ;;
  *) echo "BLOCKED  write outside working directory" >&2
     echo "         target : $abs" >&2
     echo "         allowed: $repo_root/**" >&2
     exit 2 ;;
esac

# 2. never write to protected paths
case "${abs#$repo_root/}" in
  .env|.env.*|secrets/*|.git/*|.github/workflows/*)
     echo "BLOCKED  protected path" >&2
     echo "         target : ${abs#$repo_root/}" >&2
     exit 2 ;;
esac

exit 0
