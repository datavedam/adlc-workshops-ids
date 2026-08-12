# ARCHITECTURE — <agent writes the project name>

The agent writes this map from repository files, commands, source data, and
approved decisions. The agent records an absent integration as OPEN.

## C4 level 1 — context

| Actor or system | Action | Evidence | Status |
|---|---|---|---|
| <agent fills> | <agent writes observed action> | <path and locator> | OBSERVED / PROPOSED / OPEN |

## C4 level 2 — containers

| Container | Responsibility | Input | Output | Evidence | Status |
|---|---|---|---|---|---|
| <agent fills> | <agent writes observed responsibility> | <path or field> | <file or result> | <path and locator> | OBSERVED / DERIVED / OPEN |

## Data flow

```text
<agent writes a source-backed flow with paths and commands>
```

## Interfaces

<Agent writes the module inputs, outputs, and local interfaces with paths.>

## Module placement

<Agent writes the instruction that places this module in the project. The
instruction names the directory, command, and source rule.>

**Status:** PROPOSED · **Source:** <path and locator>

## Review

- Missing evidence: <agent lists gaps>
- Open questions: <agent lists owners and questions>
- Approved by: <human name or OPEN>
- Approved on: <date or OPEN>
