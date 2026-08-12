# Day 2 — autonomous project pack

Day 2 turns a source document and local command output into a reviewed project
pack. Claude Code writes the files. A human reviews every business proposal.

## Start

Run these commands from this directory:

```bash
python3 tools/conflict-scan.py | tee evidence/conflict-scan.txt
python3 tools/criteria-lint.py modules/<module>/FRAMING.md
python3 tools/pack-check.py modules/<module> --project-file CLAUDE.md
```

The setup prompt creates `evidence/`, copies the starter into the selected
module, and creates the project `CLAUDE.md` from source evidence.

## Agent-owned outputs

Claude Code creates or updates these files:

- `CLAUDE.md` from source files, commands, and observed output.
- `CONFLICTS.md` from the conflict scan and source references.
- `FRAMING.md` from the source purpose and approved scope.
- `DATA-CONTRACT.md` from observed fields and formulas.
- `ARCHITECTURE.md` from the files, commands, and data flow.
- `SPEC.md` from approved intent, requirements, data, and checks.
- three ADRs from source evidence and an adversarial review.
- `SKILLS.md` from skills.sh source, installation, lock, and use output.
- `EVIDENCE.md` and the `evidence/` records from commands and reviews.

Each statement carries one of these statuses:

| Status | Meaning |
|---|---|
| `OBSERVED` | A file or command shows this fact. |
| `DERIVED` | A formula or local check produces this result. |
| `PROPOSED` | The agent recommends this choice for review. |
| `APPROVED` | A named human accepted this choice. |
| `OPEN` | The source leaves a question for a named owner. |

## ADR review reference

Open `starter/adr/001-title.md` in the participant checkout. Point to these
sections during the review:

1. `Context` records the source forces.
2. `Decision` records the proposed action.
3. `The case against` records the strongest other view.
4. `The agent's attack` records the three strongest failure reasons.
5. `Outcome` records the human response or the changed decision.

Show `starter/adr/001-title.md`, `002-title.md`, and `003-title.md`. Claude
Code copies and fills these templates in the participant pack.

## Day 2 TG2

The named lead signs the commit that contains the pack after these checks:

- a fresh agent creates or updates one output from the pack;
- `CLAUDE.md` states its source, commands, rules, traps, and review status;
- `SPEC.md` has checkable requirements and source references;
- all scan results have a `PROPOSED`, `APPROVED`, or `OPEN` record;
- all three ADRs contain the five required sections and attack output;
- `SKILLS.md` records selected skills, lock hashes, and exact CLI output;
- `EVIDENCE.md` records human review and sign-off.

The lead records the name, date, decision, and commit hash. The agent writes
the record. The lead provides the approval.
