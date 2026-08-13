# Loop run — <module>

The agent fills this as it goes. Each stage needs a result and a path. A stage
with no path is a claim, and `tools/loop-check.py` reports it.

**Requirement source:** `<path or ticket>`
**Owner:** `<name>`   **Date:** `<YYYY-MM-DD>`   **Commit:** `<hash>`

| # | Stage | What the agent did | Output path | Human stop |
|---|---|---|---|---|
| 1 | understand | | `evidence/day-04/source-ledger.md` | no |
| 2 | context | | `CLAUDE.md` | no |
| 3 | grill | | `evidence/day-04/grill.md` | yes |
| 4 | decide | | `modules/<module>/adr/001-<title>.md` | yes |
| 5 | specify | | `modules/<module>/SPEC.md` | yes |
| 6 | plan | | `docs/plans/<date>-<module>.md` | no |
| 7 | build | | `evidence/day-04/build.txt` | no |
| 8 | prove | | `evidence/day-04/tests.txt` | sign |

## Facts found at stage 1

| Fact | Source path and locator | Status |
|---|---|---|
| | | `OBSERVED` |

## Points the source never answers

| Question | Owner | Status |
|---|---|---|
| | | `OPEN` |

## Stops

Total stops: `<n>`   Decisions: `<n>`   Lookups: `<n>`   Decision share: `<n>%`

Full record: `evidence/day-04/decisions.json`

## Result

- End-to-end check: `<command>`
- Output: `<path>`
- Tracker rows: `<task ids>`
- Rows closed with evidence: `<n>`
