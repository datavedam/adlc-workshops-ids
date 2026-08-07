#!/usr/bin/env bash
# Builds a throwaway working copy of the demo app at /tmp/adlc-demo, with two
# branches for the live comparison:
#   run-a — no CLAUDE.md, no .claude/         (no guard-rails)
#   run-b — CLAUDE.md + .claude/ from starter (guard-rails)
#
# Safe to re-run: it deletes and rebuilds the throwaway copy every time, so
# rehearsing again is just "run this script again".
set -euo pipefail

DEMO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORK_DIR="/tmp/adlc-demo"
STARTER_CLAUDE_DIR="$DEMO_DIR/../starter/.claude"
TOOLS_SRC="$DEMO_DIR/../tools"
TOOLS_DIR="$(dirname "$WORK_DIR")/tools"

echo "Removing any previous throwaway copy at $WORK_DIR ..."
rm -rf "$WORK_DIR" "$TOOLS_DIR"
mkdir -p "$WORK_DIR"

# baseline.py (used by task-baseline.md) is staged as a sibling of the
# throwaway copy, so "../tools/baseline.py" resolves from inside it — the
# same relative-path convention the real workshop repo uses.
# Stage the workshop tools next to the throwaway copy, so the commands in
# task-baseline.md and PARTICIPANT.md ("../tools/...") resolve from inside it.
if [ -d "$TOOLS_SRC" ]; then
    mkdir -p "$TOOLS_DIR"
    cp "$TOOLS_SRC/baseline.py" "$TOOLS_DIR/baseline.py"
    cp "$TOOLS_SRC/violation-test.sh" "$TOOLS_DIR/violation-test.sh"
    chmod +x "$TOOLS_DIR/baseline.py" "$TOOLS_DIR/violation-test.sh"
fi

echo "Copying app + tests into $WORK_DIR ..."
cp -r "$DEMO_DIR/app" "$WORK_DIR/app"
cp -r "$DEMO_DIR/tests" "$WORK_DIR/tests"
cp "$DEMO_DIR/.gitignore" "$WORK_DIR/.gitignore"

# app/ and tests/ may carry __pycache__ from local test runs in the source
# copy — strip it so the throwaway repo starts with only source files.
find "$WORK_DIR" -name '__pycache__' -type d -prune -exec rm -rf {} +

cd "$WORK_DIR"
git init -q
git config user.email "demo@datavedam.local"
git config user.name "ADLC Demo"
git add -A
git commit -q -m "Initial commit: mini hotel PMS demo app"

# Tag the start point so the baseline task (task-baseline.md) always has a
# stable ref to branch from, even after run-a/run-b pick up live-demo edits.
git tag baseline-start

# Rename whatever the default branch is (main/master, depending on the
# trainer's git config) directly to run-a, so no extra branch is left over.
git branch -m run-a

echo "Creating branch run-b (CLAUDE.md + .claude guard-rails) ..."
git checkout -q -b run-b
cp "$DEMO_DIR/CLAUDE.md.for-run-b" "$WORK_DIR/CLAUDE.md"
if [ -d "$STARTER_CLAUDE_DIR" ]; then
    cp -r "$STARTER_CLAUDE_DIR" "$WORK_DIR/.claude"
fi
git add -A
git commit -q -m "run-b: add CLAUDE.md and .claude guard-rails"

echo "Checking out run-a ..."
git checkout -q run-a

cat <<EOF

Setup complete.

  Working copy : $WORK_DIR
  Branches     : run-a (no guard-rails — currently checked out)
                 run-b (CLAUDE.md + .claude guard-rails)
  Start tag    : baseline-start (root commit — use this for task-baseline.md runs)

Next steps for the trainer (live demo — the folio-balance task):
  1. cd $WORK_DIR
  2. Open the folder in your editor / agent. You are on branch run-a.
  3. Type this prompt exactly:
       Add a function that returns the current folio balance for a reservation.
  4. Let the agent finish, then look at the diff:
       git diff --stat
       git diff
  5. Switch branches:
       git checkout run-b
  6. Type the exact same prompt again.
  7. Compare the diff the same way:
       git diff --stat
       git diff
  8. To rehearse again from a clean slate, just rerun this script:
       $DEMO_DIR/setup.sh

For the Part 3 baseline measurement (participants run the task three times,
alone / chat / agent) see task-baseline.md — it is a different task from the
one above, and it branches from the "baseline-start" tag, not from run-a/run-b.
EOF
