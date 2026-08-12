# DATA CONTRACT — <agent writes the module name>

The agent fills this file from observed source fields and source tables. The
human reviews the field meaning and approves the contract.

## Source set

- Data file: <agent records path>
- Source document: <agent records path or OPEN>
- JSON paths or page locators: <agent records them>
- Status: OBSERVED

## The rule

Store measured values as base fields. Compute derived values from base fields.
Record a source gap as OPEN.

## Fields this module reads

| Field | Kind | Unit | Source path or locator | Status |
|---|---|---|---|---|
| <agent fills> | base / derived | <unit> | <path and locator> | OBSERVED / DERIVED / OPEN |

## Outputs and formulas

| Output | Formula | Input fields | Check command | Status |
|---|---|---|---|---|
| <agent fills> | <agent writes formula> | <agent lists fields> | <agent writes command> | DERIVED / PROPOSED / APPROVED |

## Unknowns

| Question | Source gap | Owner | Status |
|---|---|---|---|
| <agent fills> | <path or locator> | <name or OPEN> | OPEN |

## Human review

- Reviewed by: <human name or OPEN>
- Reviewed on: <date or OPEN>
- Decision: APPROVED / OPEN
