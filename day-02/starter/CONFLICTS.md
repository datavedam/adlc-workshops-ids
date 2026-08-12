# CONFLICTS — <agent writes the module name>

The agent fills this file from `python3 tools/conflict-scan.py <module>` and
source files. The human reviews each proposed decision.

## Source and run

- Source file: <agent records path>
- Source document: <agent records path or OPEN>
- Scan command: `python3 tools/conflict-scan.py <module>`
- Output record: `evidence/conflict-scan-<module>.txt`
- Status: OBSERVED

## Conflict register

| ID | Rule | What disagrees | Values | Source locator | Candidate | Status | Owner |
|---|---|---|---|---|---|---|---|
| C-1 | R1 / R2 / R3 | <agent fills> | <agent fills> | <path and locator> | <agent proposes> | PROPOSED / APPROVED / OPEN | <name> |

The agent adds one row for every scan result. The agent adds a row for every
source conflict the scan does not detect.

## Corrections

The agent adds a correction when source evidence proves the value.

### C-<n> — <agent writes the conflict>

- Decided value: <value>
- Arithmetic: <agent writes the formula>
- Source: <path and locator>
- Status: PROPOSED / APPROVED
- Approved by: <human name or OPEN>

## Stated assumptions

The agent adds an assumption when source evidence cannot prove the value.

### A-<n> — <agent writes the open choice>

- Chosen value: <agent proposes or OPEN>
- Source gap: <path and locator>
- Reason: <agent explains the evidence boundary>
- Client question: <agent writes the exact question>
- Owner: <name or OPEN>
- Status: PROPOSED / APPROVED / OPEN
- Approved by: <human name or OPEN>

## Review record

- Reviewed rows: <agent lists IDs>
- Open rows: <agent lists IDs>
- Human decision: <agent records the response>
- Human name: <name or OPEN>
- Date: <date or OPEN>
