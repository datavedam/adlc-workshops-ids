# Let Claude Code run the Day 4 loop

Open Claude Code from the public repository root. Paste this prompt.

```text
Work inside day-04. Own every file edit and every command in this task.

## 1. Discover the inputs

1. Read `day-04/README.md`, `day-04/PARTICIPANT.md`, every file under
   `day-04/starter/`, and the help output of every tool in `day-04/tools/`.
2. Read `day-04/starter/loop-card.md`. It holds the eight stages and the stop
   rule. Follow both for the whole task.
3. List `../day-03/modules/` and `../day-02/modules/` in lexical order.
   Select the first directory that holds a `SPEC.md`.
4. When no module holds a specification, use module key `fnb`, and use
   `../day-02/data/fx1-sample.json` as the requirement source.
5. Record the selected module and every source path in
   `evidence/day-04/source-ledger.md`.
6. Record an absent confidential source as an `OPEN` item with an owner and a
   question. Continue with the available public source.

## 2. Create the workspace

1. Create `modules`, `evidence/day-04`, `reports`, and `.claude`.
2. Copy every file under `starter/.claude/` into `.claude/`. Then tell the
   participant to restart the session, because settings load at session start.
3. Copy `starter/loop-run.template.md` to `evidence/day-04/loop-run.md`.
4. Build the tracker: `python3 tools/make-tracker.py --out tracker.xlsx`.
5. Add the `starter/CLAUDE-DAY4-BLOCK.md` content to the project `CLAUDE.md`.
   Keep the file under 200 lines. Cut any line with no project reason.

## 3. Run the eight stages, in order

Stage 1 · understand. Read the requirement source. Write two lists in
`evidence/day-04/loop-run.md`: the facts with a path and a locator for each
one, and the points the source never answers.

Stage 2 · context. Put the durable project rules in `CLAUDE.md`. Keep the task
detail out of it.

Stage 3 · grill. Stop here. Ask the participant one question at a time.
Recommend an answer with every question. Record every stop:

    python3 tools/decision-log.py add --kind decision --stage 3 --question "..." --owner "..."
    python3 tools/decision-log.py add --kind lookup --stage 7 --question "..." --belongs-in <file>

Mark a stop `lookup` when the answer already sat in a file, in the source, or
in command output. Put that answer in the named file before you continue.

Stage 4 · decide. Write each answer as a decision record with context,
decision, the strongest case against, the failure conditions, and the outcome.
Append the same record to the `ADRs` sheet through `tools/tracker.py`.

Stage 5 · specify. Write `modules/<module>/SPEC.md` with intent, out of scope,
five or more EARS criteria, interfaces and data, and one end-to-end check with
an expected result. Stop for the scope boundary. Scope is a business choice.

Stage 6 · plan. Write small tasks. Give each task the files it touches, its
test, and its own check.

Stage 7 · build. Use one fresh subagent for each task. Run two reviews after
each task: first against the specification, then against code quality.

Stage 8 · prove. Run the tests and the end-to-end check. Save the exact output.

## 4. Keep the tracker

1. Propose the task rows:

    python3 tools/tracker.py propose --file tracker.xlsx --spec modules/<module>/SPEC.md --owner "<name>"

2. Fill columns AF to AP on your own rows: AI mode, harness, model, tokens from
   the meter, estimated cost, review rounds, defects found at review, EARS spec,
   the evidence path, and the tollgate.
3. Run `python3 tools/tracker.py gate --file tracker.xlsx` and show the
   participant every row that needs a person.
4. Set a row to `Completed` only after column AO names the check that proves it.
5. Run `python3 tools/tracker.py check --file tracker.xlsx` and save the output.

Never write columns Q to AE. Never write the `Team`, `Availability`,
`Utilization` or `Timeline` sheets. Never write a tollgate signature or date.
Never open a workbook file directly with a file write. The guard refuses it,
and that refusal is correct.

## 5. Install and use the selected skills

Use the skills.sh CLI with project scope. Save the exact output in
`evidence/day-04/skills-install.txt`:

    npx skills add https://github.com/mattpocock/skills --skill code-review --agent claude-code --copy -y
    npx skills add https://github.com/obra/superpowers --skill test-driven-development --agent claude-code --copy -y
    npx skills add https://github.com/obra/superpowers --skill writing-plans --agent claude-code --copy -y
    npx skills add https://github.com/obra/superpowers --skill verification-before-completion --agent claude-code --copy -y
    npx skills add https://github.com/mattpocock/skills --skill writing-great-skills --agent claude-code --copy -y
    npx skills list --json | tee evidence/day-04/skills-list.json

1. Read each installed `SKILL.md` before you use it.
2. Record each source, skill name, local path, lock hash, required parts, and
   stated refusals in `modules/<module>/SKILLS.md`.
3. Run the same task twice for one chosen skill. Keep the task words, the
   specification commit, the data and the reviewer fixed. Change the skill only.
4. Write both runs into the tracker as two rows, with the skill name in the
   harness column.

## 6. Hold the boundary

1. Confirm that `.claude/guard.sh` is present and executable.
2. Ask the participant to watch, then try three writes and save every result in
   `evidence/day-04/guard.txt`:
   a write outside the repository, a write with a credential in the content,
   and a normal write inside the repository.
3. Record the exit code for all three. The first two exit 2. The third succeeds.
4. Append the result to the `Gates` sheet with the change each rule stopped.

## 7. Close

1. Run `python3 tools/loop-check.py --file tracker.xlsx` and save the output.
2. Run `python3 tools/decision-log.py report` and save the output.
3. Show the participant: the selected module, the source ledger, every changed
   file, the tracker rows, the stop count with its split, and the four evidence
   paths.
4. Keep every business choice `PROPOSED` until a named person approves it.
5. Keep every absent fact `OPEN` with an owner and a question.
6. Prepare the commit. Write the commit hash into `evidence/day-04/loop-run.md`.
7. Stop at the review gate. Leave the TG4 signature and date empty. Day 5 fills
   them.

The agent owns discovery, the files, the plan, the build, the checks, the
tracker rows and the evidence. The human owns the answers at stages 3, 4 and 5,
the estimate corrections, the observation of the guard test, and the signature.
```
