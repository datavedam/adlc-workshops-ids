# Day 2 — what you are doing today

You take one module of a real business document, find the places where it
disagrees with itself, decide each one, and build the harness that keeps those
decisions in force. At the end, somebody else's agent runs your work with no
help from you.

**You write almost no product code today.** That is deliberate.

---

## Before you start — 5 minutes

```bash
git clone https://github.com/datavedam/adlc-workshops-ids.git
cd adlc-workshops-ids/day-02
python3 tools/conflict-scan.py            # must print a conflict report
```

If that prints a report, you are ready. You also need the **BRD** — the trainer
gives you that file directly. It is confidential and it is not in this
repository.

Prefer to let Claude Code do the setup for you? Paste the prompt in
**[SETUP-PROMPT.md](SETUP-PROMPT.md)**. It does the plumbing and refuses the
five things that are yours to do.

---

## The four parts

| Part | What you do | What proves it |
|---|---|---|
| 1 | Watch the demonstration | You wrote a prediction down |
| 2 | Frame one module | Conflicts closed · 4 criteria pass the lint |
| 3 | Build the harness | CLAUDE.md audited · skills chosen and justified |
| 4 | Prove it | Another person's agent runs your pack |

---

## Part 2 — frame one module

Pick one module and copy the starter folder into it.

```bash
cp -r starter modules/fnb          # or: overview front_office spa
                                   # sales_catering finance signals materials
```

### Task 1 — find the conflicts

```bash
python3 tools/conflict-scan.py fnb
```

The tool does the arithmetic. It never tells you which number is right.

It only knows three rules, so it finds fewer conflicts than your module holds.
Then read every table yourself and ask four questions:

1. **Does it add up?** Total the rows. Compare with the stated total.
2. **Does it agree elsewhere?** Find the same figure in another module.
3. **Does the maths follow?** Recompute every derived number from its parts.
4. **Does the note match?** Read the commentary against the table above it.

Question 2 finds the most. Contradictions live in the gaps between people.

### Task 2 — decide every conflict

Write them in `modules/<yours>/CONFLICTS.md`. There are two ways to close one:

- **Correct it** — you can prove which number is right. Write the value **and
  the arithmetic**. Without the arithmetic you have recorded an opinion.
- **State the assumption** — you cannot prove it. Write the value you chose, why
  you chose it, and the exact question the client must answer.

There is no third way. Do not leave one open.

> Do not edit `data/fx1-sample.json`. The data keeps its contradictions on
> purpose — another person runs your pack against it in Part 4.

### Task 3 — write four acceptance criteria

Put them in `modules/<yours>/FRAMING.md`, then:

```bash
python3 tools/criteria-lint.py modules/fnb/FRAMING.md
```

Write one for the totals, one for a missing number, one for the export, and one
for the words. The test for each: could somebody who knows nothing about hotels
tell you pass or fail, without asking a question?

The lint flags. It does not judge. A criterion can pass the lint and still be
useless.

---

## Part 3 — build the harness

Three layers, then TG1 gets signed.

### Guard-rails — what the agent is allowed to do

```bash
cp -r day-01/starter/.claude  <your repo>/
# then RESTART your session — settings load at session start
```

**Read both files before you copy them.** You are installing something that can
veto your commands. "I copied it from the workshop repo" is not a review.

Then attack it on purpose. Pick one:

- ask the agent to edit a file **outside the repository**
- ask it to run a **denylisted command** against an external host
- ask it to read a **protected secret path**

Expect **denied, with no prompt**. If it asked you and you said no, that is not
a block — that is you being careful, and you will not be careful every time.

```bash
day-01/tools/violation-test.sh     # 3 attempts → evidence/tg1-violation.txt
```

That evidence file is what TG1 is signed against. Not the config — anybody can
have a config.

### CLAUDE.md

Five sections:

| Section | What goes in it |
|---|---|
| What this is | Two lines. The product, and who reads it. |
| Commands | Build, test, run, check — the exact lines. |
| Rules that do not bend | Constraints that make the build wrong if broken. |
| Traps | Where this project has already caught somebody out. |
| Conventions | Only what the code does not already show. |

Test every line with one question: **would this line have prevented a real bug
we have already had?** If not, cut it. Aim for 60 lines. Never more than 200 —
it is read on every task and costs tokens every time.

Then audit it:

```bash
npx skills add anthropics/claude-plugins-official@claude-md-improver
```

It scores your file and gives you a report **before** it changes anything. Read
the report. Accept what is right. Reject what is wrong — it has never seen the
conflicts you found this morning.

### Skills

```bash
npx skills find "requirements analysis"
npx skills add <owner/repo@skill>
```

Choose at most three. Write one line for each: why this project needs it, and
what it costs you if it is wrong. Then commit `skills-lock.json` — it is a
dependency and it belongs in review.

**Read the actual SKILL.md before you install it.** The directory summary is
marketing. The instructions are the product.

Installing nothing is a defensible answer.

### The check, before you break

```bash
# restart your session first — config loads at session start
```

Then ask the agent: *"What are the rules for this project?"* and *"What will you
refuse to do in this repository?"* If it cannot answer, your CLAUDE.md is
decoration.

### TG1 — signed at the end of Part 3

A named IDS Next lead signs against a commit hash:

- [ ] Guard-rails **refused a violation** — watched, no click-through, captured
      in `evidence/tg1-violation.txt`
- [ ] `CLAUDE.md` committed, and after a restart the agent states the project's
      rules and what it will refuse to do
- [ ] Skills **chosen and justified** in writing, `skills-lock.json` committed
- [ ] A named IDS Next lead **has signed**

> The **baseline** is not in TG1 — it is homework before the next session. It is
> deferred, not dropped. Day 10 is measured against it.

---

## Part 4 — the cold run and TG2

Give your pack to the person on your right. Take the pack on your left.

Open a **new session with no history**, then paste this task exactly. Do not add
a word:

```
Using only the pack in this folder, build the Consolidated P&L card and write
out/pl.json. Then run tools/reconcile.py and report the result.
```

```bash
python3 tools/reconcile.py
```

Record every question the agent asks, and what was missing from the pack that
caused it.

**If you own the pack, say nothing.** No hints, no corrections, do not sit next
to them. The moment you explain your pack out loud you are testing yourself.

Section C of the check is **expected to fail** — the tiles and the P&L disagree
in the source data. An agent that reports that honestly has passed.

### TG2

A named IDS Next lead signs against a commit hash:

- [ ] A fresh agent ran one task from the pack with no extra prompting
- [ ] CLAUDE.md exists, was audited, and the agent states its rules after a restart
- [ ] Every acceptance criterion could be judged by a check
- [ ] Every conflict is closed — corrected, or stated as an assumption

Commit before the gate. We sign what is committed.

---

## Before the next session

1. Finish `CONFLICTS.md`. Every conflict closed, arithmetic beside each correction.
2. Write **three decisions** (`starter/adr/`). Write your own case against each
   one **before** you ask the agent to argue with you. If you ask first you will
   adopt its framing and stop thinking.
3. Finish `DATA-CONTRACT.md` for your module.
4. Run the cold task on your own pack again. Fix what it asks about.
5. **Your baseline.** One task, three ways — unassisted, then chat, then agentic.
   Four numbers each: time, diff lines, defects found in review, tokens. Do the
   unassisted run **first**, and commit your config before you start or it counts
   as task diff. This is the number Day 10 is measured against.

---

## One line before you go

Every conflict you leave open, the agent decides for you.
