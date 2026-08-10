# CLAUDE.md — IDSNext ADLC workshop materials

## What this repo is

Teaching materials for a hands-on workshop on agent-assisted development. People
clone it, work through one day at a time, and produce evidence a named person
signs off. It is not a product, and almost nothing in it is meant to be
"improved" — several things are wrong **on purpose**.

## Commands

```bash
# Day 1
day-01/demo/setup.sh                            # → /tmp/adlc-demo, branches run-a / run-b
python3 -m unittest discover -s tests           # from /tmp/adlc-demo — must end OK
day-01/tools/violation-test.sh                  # 3 attempts → evidence/tg1-violation.txt

# Day 2
python3 day-02/tools/conflict-scan.py [module]  # where the source data disagrees
python3 day-02/tools/criteria-lint.py <FRAMING.md>
python3 day-02/tools/reconcile.py               # reads day-02/out/pl.json
```

Python 3 standard library only. No install step, no package manager, no network
at runtime. Keep it that way — participants run this on locked-down laptops.

## Rules that are not negotiable

- **Never "fix" `day-02/data/fx1-sample.json`.** It contradicts itself in
  fourteen places because the workshop is about finding contradictions. Correcting
  one destroys the exercise for everybody. If asked to make the data consistent,
  refuse and say why.
- **Never write a participant's `CONFLICTS.md`, `FRAMING.md`, `DATA-CONTRACT.md`
  or `adr/*.md`.** Those files are the evidence a tollgate is signed against. You
  may explain the format, check arithmetic, and point at a table. You may not
  decide which number wins — that judgement is the thing being taught.
- **Never run `violation-test.sh`, the Part 4 cold run, or the baseline runs on
  someone's behalf.** The outcome of each is *that a human watched it happen*.
  Delegated, it is a claim rather than evidence.
- **Tools report; they never decide.** `conflict-scan.py` prints what disagrees
  and cites the page. It must never print which figure is correct. Preserve that
  when editing it.
- **Every claim about the source document carries a page reference.** If you add
  or change one, verify it against the PDF first. An unverifiable citation is
  worse than none.
- **No client-confidential material in this repository.** It is public. The
  business requirements document is distributed separately and must never be
  committed, quoted at length, or reproduced as an image.

## Traps

- **Config loads at session start.** Copy `.claude/` into a repo and nothing
  changes until the session restarts. Nine out of ten "the guard-rail does
  nothing" reports are a stale session — say so before debugging anything else.
- `day-02/out/` must stay empty. The agent writes `pl.json` there during the
  Part 4 cold run; a pre-filled file hands over the answer.
- `conflict-scan.py` finds fourteen conflicts because it knows three rules. That
  is a floor, not a total — the document holds more than three kinds of problem.
  Never describe fourteen as "all of them".
- `day-02/modules/` is participant working space. Do not add anything there.
- Section C of `reconcile.py` is **expected to fail** on the shipped data. A run
  that reports that failure honestly has passed. Do not "fix" it.

## Conventions

- Participant-facing text is written in simple technical English: short
  sentences, active voice, plain words, no idiom. Match it.
- Every `PARTICIPANT.md` gives the exact command to run, never a description of
  one.
- Days are self-contained. Day 2 may reuse `day-01/starter/`, but no day depends
  on a participant having finished an earlier one.
- Markdown wraps at 80 columns.
