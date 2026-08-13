# Day 4 block for the project `CLAUDE.md`

Add this to the project file. It states the loop, the stop rule, and the
tracker write contract, so a fresh session knows all three without a prompt.

Keep the block short. Every line here is read on every task.

---

## The delivery loop

Run these eight stages in order for any new requirement.

1. **Understand** — read the source. Write the facts with a path for each one,
   and the points the source never answers.
2. **Context** — put the durable rules in this file. Keep the task detail out.
3. **Grill** — ask the human one question at a time. Recommend an answer with
   every question.
4. **Decide** — write each answer as a decision record with the strongest
   case against it.
5. **Specify** — write EARS criteria, the scope boundary, and one end-to-end
   check.
6. **Plan** — write small tasks. Give each task its own check.
7. **Build** — one fresh subagent for each task. Two reviews after each task:
   first against the specification, then against code quality.
8. **Prove** — run the tests and the review. Save the output. Then close the
   tracker row.

Stages 3, 4 and 5 need a human answer. Stage 8 needs a human signature.
Stages 1, 2, 6 and 7 need no human at all.

## When to stop and ask

Stop for a choice. Never stop for a fact.

| Status | Meaning | Action |
|---|---|---|
| `OBSERVED` | The source or command output states it | Continue. Record the path. |
| `DERIVED` | Arithmetic or a project rule gives it | Continue. Record the arithmetic. |
| `PROPOSED` | A business choice with no owner | Stop. Ask one question. |
| `OPEN` | No available source holds this fact | Stop. Name the owner and the question. |
| `APPROVED` | A named person agreed, with a date | Continue. Treat it as a rule. |

Record every stop:

```bash
python3 tools/decision-log.py add --kind decision --stage <n> \
    --question "<one question>" --owner "<name>"
python3 tools/decision-log.py add --kind lookup --stage <n> \
    --question "<one question>" --belongs-in <file that should hold the answer>
```

A `lookup` is a gap in this file. Put the answer here, then continue.

## The tracker write contract

The agent may:

- write columns A to P on a task row it created;
- write columns AF to AP on its own rows;
- append a row to the `ADRs`, `Risks` and `Gates` sheets.

The agent may never:

- write columns Q to AE. Those hold formulas and hidden filter helpers.
- write the `Team`, `Availability`, `Utilization` or `Timeline` sheets.
- write a tollgate signature or date. A named person signs.
- write a row that belongs to another person.
- open a workbook file directly. Use `tools/tracker.py`.

A task reaches `Completed` only when column AO names the check that proves it.
A command with its output path is evidence. A test name that fails without the
change is evidence. "Done" is not evidence.

## Commands

```bash
python3 tools/make-tracker.py --out tracker.xlsx
python3 tools/tracker.py show    --file tracker.xlsx
python3 tools/tracker.py propose --file tracker.xlsx --spec <SPEC.md> --owner "<name>"
python3 tools/tracker.py gate    --file tracker.xlsx
python3 tools/tracker.py check   --file tracker.xlsx
python3 tools/decision-log.py report
python3 tools/loop-check.py --file tracker.xlsx
```

## Traps

- Settings load when a session starts. Restart the session after any change to
  `.claude/`.
- Excel holds a workbook open. Close the file before a tool writes to it.
- The guard refuses a direct write to a workbook. That refusal is correct.
