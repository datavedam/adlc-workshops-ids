# Day 4 — run the loop, keep the record, hold the boundary

Day 4 joins Day 1, Day 2 and Day 3 into one loop. Claude Code runs the loop.
It stops only when a human has to choose. The task tracker keeps the record.

## Outcomes

Each participant leaves with:

- one requirement carried through all eight loop stages, with a path for each
  stage;
- task rows in a tracker workbook, with harness, model, tokens, review rounds
  and an evidence cell;
- one stop log with the count and the decision share;
- one reviewed skill at one loop stage, with a before and after measurement;
- one guard that refused two violations and allowed a normal write;
- four evidence paths for the Day 5 TG4 review.

## The working agreement

Claude Code owns discovery, the files, the plan, the build, the checks and the
evidence. The participant answers the decisions and signs the evidence.

The agent stops for a choice. It never stops for a fact. A stop that a file
could have answered is a gap in the harness. Repair the file, then continue.

## Before the session

Run these from the public repository root:

```bash
cd adlc-workshops-ids/day-04
python3 -m pip install --user openpyxl
python3 tools/make-tracker.py --out tracker.xlsx
python3 tools/tracker.py --self-test
python3 tools/decision-log.py --self-test
python3 tools/loop-check.py --file tracker.xlsx
```

The last command reports four gaps. That is correct before the session starts.

Start Claude Code with [SETUP-PROMPT.md](SETUP-PROMPT.md).

## The eight stages

| # | Stage | The agent produces | A human is needed |
|---|---|---|---|
| 1 | Understand | The facts with paths, and the open points | no |
| 2 | Context | The durable rules in `CLAUDE.md` | no |
| 3 | Grill | One question at a time, each with a recommended answer | **yes** |
| 4 | Decide | A record with context, decision, case against, outcome | **yes** |
| 5 | Specify | EARS criteria, the scope boundary, one end-to-end check | **yes** |
| 6 | Plan | Small tasks, each with its own check | no |
| 7 | Build | One subagent for each task, two reviews after each | no |
| 8 | Prove | Tests, review, evidence, then the tracker row closes | **sign** |

## Part 1 — the loop

Give the agent one requirement and nothing else. Keep it small. If you have
nothing of your own, use [starter/SAMPLE-REQUIREMENT.md](starter/SAMPLE-REQUIREMENT.md).

Record every stop as a decision or a lookup:

```bash
python3 tools/decision-log.py add --kind decision --stage 3 \
    --question "Which figure does the report use?" --owner "<name>"
python3 tools/decision-log.py add --kind lookup --stage 7 \
    --question "Which command runs the tests?" --belongs-in CLAUDE.md
```

A lookup means the answer already existed. Put it in the named file. Do not
answer the same question twice.

## Part 2 — the tracker

The workbook uses the same sheets and the same task columns A to AP as the
IDSNext tracker. Columns AF to AP are appended after the hidden filter helpers,
so no column of yours moves and no formula of yours changes.

```bash
python3 tools/tracker.py show    --file tracker.xlsx
python3 tools/tracker.py propose --file tracker.xlsx --spec modules/<module>/SPEC.md --owner "<name>"
python3 tools/tracker.py gate    --file tracker.xlsx
python3 tools/tracker.py check   --file tracker.xlsx
```

`propose` writes one row for each EARS criterion. Every estimate arrives as
`PROPOSED`. A lead corrects it, and that correction is a decision.

`gate` prints only the rows that need a person. `check` fails when a row claims
`Completed` with an empty evidence cell.

Close the workbook in Excel before a tool writes to it.

### The write contract

The agent writes columns A to P on rows it created, columns AF to AP on its own
rows, and appends to the `ADRs`, `Risks` and `Gates` sheets.

The agent never writes columns Q to AE, never writes the `Team`,
`Availability`, `Utilization` or `Timeline` sheets, never writes a signature,
and never opens a workbook file directly.

### The evidence rule

A task reaches `Completed` only when column AO names the check that proves it.

Evidence is a command with its output path, or a test name that fails without
the change. "Done", "tested locally" and a pull request number are not
evidence.

## Part 3 — one skill at one stage

Pick the stage that costs the most time. Read the skill file before you install
it. Count its required parts. Write down what it refuses to do.

```bash
npx skills add https://github.com/mattpocock/skills --skill code-review --agent claude-code --copy -y
npx skills add https://github.com/obra/superpowers --skill test-driven-development --agent claude-code --copy -y
npx skills add https://github.com/obra/superpowers --skill writing-plans --agent claude-code --copy -y
npx skills add https://github.com/obra/superpowers --skill verification-before-completion --agent claude-code --copy -y
npx skills add https://github.com/mattpocock/skills --skill writing-great-skills --agent claude-code --copy -y
npx skills list --json | tee evidence/day-04/skills-list.json
```

Then run the same task twice. Once without the skill, once with it. Keep the
task words, the specification commit, the data and the reviewer fixed. Change
the skill only. Record both runs as two tracker rows.

Then draft one skill of your own for a job that no public skill knows. Give it
a name, a description that states the trigger, numbered steps with exact
commands, the refusals, and the check.

## Part 4 — MCP and the guard

Read the tool list of a server before you connect it. Write down every tool and
its scope. Connect with read access first.

Copy the guard into your repository and restart the session:

```bash
cp -r starter/.claude .
# restart the Claude Code session — settings load at session start
```

Then try three writes and save all three results:

```bash
# 1 outside the repository  → expect exit 2
# 2 content with a credential → expect exit 2
# 3 a normal file inside the repository → expect success
... | tee evidence/day-04/guard.txt
```

A guard that blocks everything is an outage. The third result matters as much
as the first two.

## TG4 evidence

Day 4 signs nothing. A named IDSNext lead signs TG4 on Day 5 against four
paths and a commit hash.

| # | Proof | Path |
|---|---|---|
| 1 | The loop ran end to end, with a path for each stage | `evidence/day-04/loop-run.md` |
| 2 | The tracker holds measured rows and no closed row without evidence | `tracker.xlsx` |
| 3 | The stop count, the decision share, and the repair list | `evidence/day-04/decisions.json` |
| 4 | Two refusals with exit 2, and one allowed write | `evidence/day-04/guard.txt` |

Run this before you leave:

```bash
python3 tools/loop-check.py --file tracker.xlsx
```

A clean run means Day 5 is a review. Anything thin is a repair tonight.
