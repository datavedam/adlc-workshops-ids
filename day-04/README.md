# Day 4 — one loop from requirement to evidence

**Module 4 · 4 contact hours · Week 2 · feeds Tollgate TG4 (signed on Day 5)**

Day 4 joins the first three sessions into one loop. Claude Code carries a
requirement through eight stages. It stops only when a human has to choose.
The task tracker keeps the record, in the sheet the delivery managers already
read.

## Day 4 result

Each participant has:

- one requirement through all eight stages, with an output path for each stage;
- task rows with harness, model, tokens, review rounds, defects and evidence;
- one stop log with the count, the decision share, and a repair list;
- one skill placed at one stage, with a before and after measurement;
- one draft skill of their own;
- one guard that refused two violations and allowed a normal write;
- four evidence paths ready for the Day 5 TG4 review.

## What each earlier day contributes

| Day | What it gave | Where it sits in the loop |
|---|---|---|
| 1 | The harness: context, tools, permissions, loop, skills | Every stage |
| 2 | The grill skill, `CLAUDE.md`, decision records | Stages 2, 3 and 4 |
| 3 | EARS criteria, the specification, subagent-driven work | Stages 5, 6 and 7 |
| 4 | The tracker, the stop rule, review and test skills, MCP, the guard | Stages 1 and 8, and the record |

## The loop

| # | Stage | Agent result | Human gate |
|---|---|---|---|
| 1 | Understand | Facts with paths, and the open points | — |
| 2 | Context | Durable rules in `CLAUDE.md` | — |
| 3 | Grill | One question at a time, each with a recommendation | **answers** |
| 4 | Decide | A record with the strongest case against | **approves** |
| 5 | Specify | EARS criteria, scope boundary, one check | **approves the boundary** |
| 6 | Plan | Small tasks, each with its own check | — |
| 7 | Build | One subagent for each task, two reviews after each | — |
| 8 | Prove | Tests, review, evidence, then the row closes | **signs** |

## Four parts

| Part | Agent result | Participant gate |
|---|---|---|
| 1 · Recap and the loop | One live run through all eight stages | Name the stage and the real decision |
| 2 · The tracker | Proposed task rows with measured columns | Correct the estimates, read another person's rows |
| 3 · Skills at each stage | One skill installed, one task run twice | Say which number moved, and by how much |
| 4 · MCP and the guard | A connected server and a live guard test | Watch both refusals and the allowed write |

## The number that carries forward

Count every stop the agent makes. Mark each one a **decision** or a **lookup**.

A decision needs a person: money, scope, risk, or a promise to a customer.
A lookup already had an answer in a file. A lookup is a gap in the harness.

The decision share is the measure. It moves up when lookups become file
content instead of repeat questions.

## Tollgate TG4

Day 4 signs nothing. Day 5 signs TG4 against these four paths and a commit hash:

1. `evidence/day-04/loop-run.md` — eight stages, one output path for each.
2. `tracker.xlsx` — measured rows, and no closed row with an empty evidence cell.
3. `evidence/day-04/decisions.json` — every stop marked, every lookup with a
   home file.
4. `evidence/day-04/guard.txt` — two refusals with exit 2, and one allowed write.

Run `python3 tools/loop-check.py --file tracker.xlsx` before the room leaves.

## Public files

- [Participant guide](PARTICIPANT.md)
- [Autonomous setup prompt](SETUP-PROMPT.md)
- [Starter files](starter/) — the guard, the settings, the `CLAUDE.md` block,
  the loop card, the run template
- [Local tools](tools/) — `make-tracker.py`, `tracker.py`, `decision-log.py`,
  `loop-check.py`

The public repository holds participant material. Trainer slides, presenter
scripts, trainer keys and client documents stay in the private trainer
repository.
