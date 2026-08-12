# EVIDENCE — project pack

The agent writes this record from command output and review events. The human
watches the marked commands and signs the final record.

## Source inputs

| Input | Path | Locator or hash | Status |
|---|---|---|---|
| <agent fills> | <path> | <agent fills> | OBSERVED |

## Commands and outputs

| Command | Output file | Exit code | Status |
|---|---|---|---|
| <agent fills> | <agent fills> | <agent fills> | OBSERVED |

## Artifact review

| Artifact | Review output | Decision | Reviewer | Date |
|---|---|---|---|---|
| <agent fills> | <path> | PROPOSED / APPROVED / OPEN | <name or OPEN> | <date or OPEN> |

## Human-observed gates

| Gate | Command or session | Observed result | Human | Date | Status |
|---|---|---|---|---|---|
| Guard test | <command> | <agent records output> | <name or OPEN> | <date or OPEN> | OPEN |
| Cold run | <fresh session and prompt> | <agent records output> | <name or OPEN> | <date or OPEN> | OPEN |

## Sign-off

- Pack commit: <hash or OPEN>
- Decision: APPROVED / OPEN
- Signed by: <human name or OPEN>
- Signed on: <date or OPEN>
- Scope of approval: <agent records the reviewed files>
