# Day 1 — what you are doing today

**Advanced AI-Assisted Coding, Analytics and SDLC workshop · Tollgate TG1**

Nobody is going to tell you that this works. Every part of today ends with
something you can point at: a refusal on your screen, a number the machine
measured, a commit in your repository.

---

## Before you walk in — 10 minutes, the night before

You need: **git**, **Python 3**, and **Claude Code working inside VS Code**.

```bash
git clone https://github.com/datavedam/adlc-workshops-ids.git
cd adlc-workshops-ids/day-01/demo
./setup.sh
```

`setup.sh` builds your own private working copy at `/tmp/adlc-demo`. It is a
small hotel-system codebase with its own git history. Everything you do today
happens inside that copy. Nothing you do can affect anyone else.

Confirm it works:

```bash
cd /tmp/adlc-demo
python3 -m unittest discover -s tests    # must end with OK
```

- [ ] The tests pass on your machine
- [ ] Claude Code opens in VS Code
- [ ] If either is a no, say so in the channel **tonight**, not at the start of the day

---

## The four parts

There are no fixed clock times. You will be told the running order on the day.

| Part | What happens | What proves it |
|---|---|---|
| Part 1 · Concepts and demo (about 90 minutes) | The trainer talks. Six topics, one live demonstration. | You name which part of the harness caused each of three failures |
| Part 2 · Build the guard-rails | You configure guard-rails and try to break them on purpose. | The violation test passes 3 of 3, and you commit the evidence |
| Part 3 · Measure the baseline | One task, three ways, with the numbers measured for you. | Twelve cells in the workbook, nothing invented |
| Part 4 · Evidence and sign-off | You publish your numbers and a lead signs the tollgate. | Your row is in the workbook, TG1 signed against your commit |

---

## Part 2 — the guard-rails

Work inside your own copy at `/tmp/adlc-demo`.

```bash
cd /tmp/adlc-demo
cp -r <path-to-clone>/day-01/starter/.claude .   # settings + the PreToolUse hook
cp <path-to-clone>/day-01/starter/CLAUDE.md .    # the template — then edit it
../tools/violation-test.sh
```

The violation test tries three dangerous actions against your guard-rails. The
first two must be refused. The third must be allowed. It writes down exactly
what happened — the attempt, the response, the exit code, the commit, your
name — into `evidence/tg1-violation.txt`. **Commit that file.** It is your
proof, and it is what gets re-run in front of the lead in Part 4.

```bash
git add -A && git commit -m "TG1: guard-rails and proof"
```

Commit all of it — the config, your `CLAUDE.md`, and the evidence file — before
Part 3 starts. The baseline tool measures your diff from the moment a run
starts, and uncommitted config would be counted as if it were task work.

**The pass bar: refused, with nothing to click.** A pop-up that asks for your
permission is not a guard-rail. By Wednesday, everyone approves pop-ups without
reading them.

Then edit `CLAUDE.md` until every line is true for the code it guards. Keep it
under 200 lines. Spend the lines on the traps — the things an agent cannot
learn by reading the code.

---

## Part 3 — the baseline

The task is **DEMO-2: cancel a reservation**. Read `day-01/demo/task-baseline.md`
first. It has the full acceptance criteria, the review rubric, and the branch
commands for each run.

You do the same task three times: on your own, with a chat window, and with the
agent. The tool measures the time and the diff for you. You only type the two
things it cannot see: defects found in review, and tokens from the meter.

```bash
cd /tmp/adlc-demo
../tools/baseline.py start unassisted
#   ...do the task...
../tools/baseline.py stop

# then the same for: chat, then agentic

../tools/baseline.py row        # one line — paste it into the workbook
../tools/baseline.py evidence   # writes the evidence file — commit it
```

Three rules keep the numbers honest:

- The **same acceptance criteria** in all three runs. If "done" changes, the comparison is dead.
- The unassisted run comes **first**. It is the control. Doing it last means you are typing from memory of the agent's answer.
- Out of time? **Skip the run.** The tool records SKIPPED. Never invent a number.

**Expect this:** the agent run is often the fastest, with the biggest diff and
the most defects. If your row looks like that, you measured it correctly. That
result is the finding, not a mistake.

---

## Part 4 — TG1

All five must be true:

- [ ] Your row is in the **Day 1 Baseline** sheet — twelve cells, nothing invented
- [ ] You have named the way you personally get caught out, with a moment from
      your own runs — not an adjective
- [ ] The violation test passes again, live, watched by someone who did not build it
- [ ] `.claude/` and `CLAUDE.md` are committed in your working copy
- [ ] A lead has signed in the **Tollgates** sheet, against your commit hash

Evidence is a moment, not an adjective:

> Not this: "the agent was a bit unreliable."
> This: "the agent run burned four times the tokens on a caching theory before
> it found the real filter bug." That is **confident-wrong debugging**, and now
> you know what to watch for later in the workshop.

If something cannot pass, that is fine, and it is not a quiet failure. It gets
an owner, a date, and a fix this week, on the **Risks** sheet, before Day 2
depends on it.

---

## One line before you go

*What will I verify differently tomorrow?* Bring it. Day 2 opens by reading
these out.
