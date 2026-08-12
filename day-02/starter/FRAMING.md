# FRAMING — <agent writes the module name>

**Owner:** <agent records supplied name or OPEN>
**Module:** <agent records the JSON module key>
**Source:** <agent records source path>
**Status:** PROPOSED

## Intent

<Agent writes what the module tells its named user and which decision it
supports. Every factual claim has a source locator.>

## Scope

<Agent writes the behavior supported by source files and approved decisions.>

## Non-goals

<Agent writes behavior that the source does not support.>

- <agent records one source-backed boundary>
- <agent records one source-backed boundary>

## Acceptance criteria

The agent writes at least four criteria. Each criterion names a checkable value,
field, file, exit code, or exact output.

1. GIVEN <source condition> WHEN <command or action> THEN <measured result>.
2. GIVEN <source condition> WHEN <command or action> THEN <measured result>.
3. GIVEN <source condition> WHEN <command or action> THEN <measured result>.
4. GIVEN <source condition> WHEN <command or action> THEN <measured result>.

Run:

```bash
python3 tools/criteria-lint.py modules/<module>/FRAMING.md
```

## Source ledger

| Claim | Source path | Locator | Command | Status |
|---|---|---|---|---|
| <agent fills> | | | | OBSERVED / DERIVED / PROPOSED / APPROVED / OPEN |

## Human review

- Review result: <agent records output path>
- Approved by: <human name or OPEN>
- Approved on: <date or OPEN>
- Status: PROPOSED / APPROVED / OPEN
