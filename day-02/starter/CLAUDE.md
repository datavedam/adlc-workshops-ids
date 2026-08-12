# CLAUDE.md — <agent fills the project name from source>

<!--
Claude Code fills this file from source files, local commands, and observed
output. A human reviews the result. The agent keeps this file under 200 lines.
The agent keeps the module copy aligned with the project copy.
Use a status on every statement: OBSERVED, DERIVED, PROPOSED, APPROVED, OPEN.
-->

## Source inventory

| Claim | Source path | Page, line, or JSON path | Status |
|---|---|---|---|
| <agent records one source claim> | | | OBSERVED / DERIVED / PROPOSED / APPROVED / OPEN |

## What this project is

<Agent summary from the source. Name the user, output, and business purpose.>

**Status:** PROPOSED · **Source:** <path and locator>

## Commands

```bash
<agent writes the exact command to inspect the source>
<agent writes the exact command to run the checks>
python3 tools/reconcile.py
```

**Status:** OBSERVED · **Source:** <command output path>

## Rules that do not bend

<Agent writes rules that affect the result. Each rule has a source locator.>

- <rule> · <source path and locator> · OBSERVED / PROPOSED / APPROVED
- <rule> · <source path and locator> · OBSERVED / PROPOSED / APPROVED

## Traps

<Agent writes source contradictions, data gaps, and check behavior.>

- <trap> · <source path or command output> · DERIVED / OPEN / APPROVED
- <trap> · <source path or command output> · DERIVED / OPEN / APPROVED

## Update protocol

Claude Code reads the source files before each update. Claude Code runs the
affected local checks after each update. Claude Code records the output in
`evidence/`. Claude Code shows the human the changed lines.

## Human review

- Reviewed files: <agent lists files>
- Open questions: <agent lists owners and questions>
- Approved by: <human name or OPEN>
- Approved on: <date or OPEN>
- Commit: <hash or OPEN>

The agent writes this file. The human changes the review fields by approving
the agent's recorded proposal in the working session.
