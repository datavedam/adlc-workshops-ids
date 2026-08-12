# Day 3 — specify, add project context, and prove TG3

Day 3 uses one public Day 2 module pack. Claude Code discovers the module,
writes the working files, installs the selected skills, runs the checks, and
saves the evidence. Participants review the source, decisions, checks, and
results.

## Outcomes

Each participant leaves with:

- one reviewed `SPEC.md` with five or more EARS criteria;
- one project `CLAUDE.md` with Day 2 rules and Day 3 checks;
- one module skill and one reconcile command;
- one cold-run record from a fresh agent session;
- one fixed-input rework comparison;
- one full-context and reduced-context token report;
- one evidence record with a commit hash and TG3 owner.

## The autonomous working agreement

Claude Code owns discovery, file creation, skill installation, command runs,
and evidence capture. The participant reviews source claims and proposed
business decisions. An absent source value becomes an `OPEN` item with an
owner and a question. A source-supported choice becomes `DERIVED`. A business
choice stays `PROPOSED` until a named lead approves it.

## Before the session

Run these commands from the public repository root:

```bash
cd adlc-workshops-ids/day-03
python3 tools/spec-lint.py starter/module/SPEC.md
python3 tools/rework-report.py --self-test
python3 tools/token-report.py --self-test
python3 tools/reconcile-report.py --self-test
```

Start Claude Code with [SETUP-PROMPT.md](SETUP-PROMPT.md). The agent selects
the first valid Day 2 module. The agent uses `fnb` when the Day 2 module area
has no valid pack. The agent records this selection in the source ledger.

## Day 2 recap: the inputs for Day 3

Open these public paths during the recap:

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

Open `day-02/starter/adr/001-title.md`. Point to these five sections:

1. `Context` records the forces from the source and the observed system.
2. `Decision` records the proposed project action.
3. `The case against` records the strongest competing option.
4. `The agent's attack` records failure reasons and test conditions.
5. `Outcome` records the response, revision, or open result.

Show all three starter ADR files. Connect them to the Day 2 TG2 requirement:

> A cold agent must build the Consolidated P&L card from the project pack,
> write `day-02/out/pl.json`, run `tools/reconcile.py`, and record the output.

The Day 2 pack carries decisions and constraints into the Day 3 specification.
The Day 3 specification adds one task behavior, one data contract, and one
end-to-end check.

## Part 1 — make one behavior checkable

Use the agent to rewrite one Day 2 criterion. The result has one condition,
one behavior, one source locator, and one exact check.

Use one EARS pattern:

- `The module SHALL ...`
- `WHEN ... the module SHALL ...`
- `WHILE ... the module SHALL ...`
- `IF ... the module SHALL ...`
- `WHERE ... the module SHALL ...`

The participant reviews the generated card. The agent saves the accepted card
in the specification evidence.

## Part 2 — build and cold-review `SPEC.md`

The agent writes these sections from the Day 2 pack:

1. Intent.
2. Out of scope.
3. At least five EARS acceptance criteria.
4. Interfaces and data.
5. One end-to-end check with an expected result.

Run:

```bash
python3 tools/spec-lint.py modules/<module>/SPEC.md
```

Use this exact cold task in a new agent session:

```text
Using only the module folder, the project CLAUDE.md, the local FX1 data file,
and the selected local skills:

1. Read SPEC.md and OUTPUT-CONTRACT.json.
2. Plan one build task.
3. Implement the smallest output that meets every criterion.
4. Run the end-to-end check in SPEC.md.
5. Record every question, command, output path, and result.
```

The reviewer records questions before the specification owner answers. A
question identifies an absent decision, field, file, or check.

## Part 3 — add project context and compare rework

The agent creates or updates:

```text
CLAUDE.md
.claude/skills/scaffold-module/SKILL.md
.claude/commands/reconcile.md
reports/rework.json
```

The agent runs the same task twice:

- Run A uses the task, specification, data, and review checklist.
- Run B uses the same inputs plus the reviewed knowledge base.

Keep the task text, specification commit, data, criteria, reviewer, and
evidence fields fixed. Record operator and session identifiers. Count a review
round after a changed output and a new check.

Run:

```bash
python3 tools/rework-report.py reports/rework.json
```

## Part 4 — measure context cost and close TG3

The agent runs the same task with full and reduced context. Record these
fields for both runs:

- input tokens;
- cached tokens;
- output tokens;
- wall-clock seconds;
- review rounds;
- defects;
- merged changes;
- provider rate and source.

Run:

```bash
python3 tools/token-report.py reports/tokens.json
```

## TG3 evidence

The agent saves:

- `modules/<module>/SPEC.md`;
- `modules/<module>/SKILLS.md`;
- `modules/<module>/EVIDENCE.md`;
- `evidence/day-03/source-inventory.md`;
- `evidence/day-03/cold-run.json`;
- `evidence/day-03/skills-list.json`;
- `reports/rework.json`;
- `reports/tokens.json`;
- the project `CLAUDE.md`;
- the module skill and reconcile command.

TG3 has three proofs:

1. A fresh agent completes one EARS task with the recorded question count.
2. The fixed-input A/B record shows the rework difference.
3. The token report shows usage, quality, and cost for both context budgets.

The named lead signs the evidence against the final commit hash.

## Source and data rules

Keep `../day-02/data/fx1-sample.json` unchanged. Use Day 2 `CONFLICTS.md`
decisions as source context. Record every unresolved value with a status,
owner, question, and source gap.
