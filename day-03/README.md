# Day 3 — specification, project context, and TG3

**Module 3 · 4 contact hours · Week 2 · Tollgate TG3**

Day 3 turns one Day 2 module pack into a checkable specification and measured
project context. Claude Code performs discovery, writing, skill installation,
checks, and evidence capture. Participants review the result and approve the
business decisions.

## Day 3 result

Each participant has a module pack with:

- a source ledger;
- a `SPEC.md` with five or more EARS criteria;
- a project `CLAUDE.md`;
- a module skill and reconcile command;
- a fresh-agent cold-run record;
- a fixed-input rework report;
- a full-context and reduced-context token report;
- a TG3 evidence record tied to a commit hash.

## Day 2 input recap

The Day 3 agent reads these public Day 2 files:

```text
day-02/starter/CLAUDE.md
day-02/starter/CONFLICTS.md
day-02/starter/FRAMING.md
day-02/starter/DATA-CONTRACT.md
day-02/starter/ARCHITECTURE.md
day-02/starter/adr/001-title.md
day-02/starter/adr/002-title.md
day-02/starter/adr/003-title.md
```

The Day 2 TG2 requirement asks a fresh agent to build the Consolidated P&L
card from the project pack, write `day-02/out/pl.json`, run
`tools/reconcile.py`, and record the output.

## Four-part flow

| Part | Agent result | Participant gate |
|---|---|---|
| 1 · Recap and EARS | One source-linked behavior card | Review condition, result, and check |
| 2 · Specification | `SPEC.md` and cold-run evidence | Review source trace and lint output |
| 3 · Project context | `CLAUDE.md`, skill, command, rework report | Review fixed inputs and changed output |
| 4 · TG3 evidence | Token report and sign-off record | Review usage, quality, cost, and commit |

## Skills.sh workflow

The agent uses four project-scoped skills:

| Work area | Skill |
|---|---|
| `CLAUDE.md` review | `claude-md-improver` |
| ADR review | `architecture-decision-records` |
| Specification review | `requirements-clarity` |
| Evidence review | `verification-before-completion` |

The agent records source, skill name, local path, lock hash, command output,
and review result in `SKILLS.md` and `evidence/day-03/`.

## Tollgate TG3

- A fresh agent completes one EARS task.
- The cold-run record contains the task, session, questions, output, and check.
- The A/B record holds task, commit, data, criteria, reviewer, and evidence
  fields fixed between runs.
- The token report contains observed or labelled estimated values.
- The report states cost for each merged change.
- A named lead signs the evidence against the final commit hash.

## Public files

- [Participant guide](PARTICIPANT.md)
- [First EARS lesson](EARS.md)
- [Autonomous setup prompt](SETUP-PROMPT.md)
- [Starter files](starter/)
- [Local tools](tools/)
- FX1 data: `../day-02/data/fx1-sample.json`

The public repository contains participant material. Trainer slides,
presenter scripts, trainer keys, and client documents stay in the private
trainer repository.
