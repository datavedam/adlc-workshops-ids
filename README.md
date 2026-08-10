# IDSNext ADLC workshop — materials

Hands-on materials for the *Advanced AI-Assisted Coding, Analytics and SDLC*
workshop. Days are added here as the workshop proceeds. Currently: **Day 1** and
**Day 2**.

You need **git**, **Python 3**, and **Claude Code working inside VS Code**.

```bash
git clone https://github.com/datavedam/adlc-workshops-ids.git
```

## Day 1 — the harness and your baseline

```bash
cd adlc-workshops-ids/day-01/demo
./setup.sh
cd /tmp/adlc-demo
python3 -m unittest discover -s tests    # must end with OK
```

Prefer to let Claude Code do the setup for you? Paste the prompt in
**[day-01/SETUP-PROMPT.md](day-01/SETUP-PROMPT.md)**.

Then read **[day-01/PARTICIPANT.md](day-01/PARTICIPANT.md)**. It explains the
whole day and every command you will run.

## Day 2 — framing a real document, and the project harness

```bash
cd adlc-workshops-ids/day-02
python3 tools/conflict-scan.py           # must print a conflict report
```

Then read **[day-02/PARTICIPANT.md](day-02/PARTICIPANT.md)**.

You also need the **business requirements document** for Day 2. Your trainer
gives you that file directly — it is confidential and it is not in this
repository.

## What is in this repository

```
day-01/
  PARTICIPANT.md     the day, part by part, with every command
  demo/              the demo project — your own working copy comes from here
  starter/           guard-rail starter pack: settings, hook, CLAUDE.md template
  tools/             baseline.py (measures your runs) · violation-test.sh (proves your guard-rails)

day-02/
  PARTICIPANT.md     the day, part by part, with every command
  data/              the sample dataset — keeps its contradictions on purpose
  starter/           module folder template: framing, conflicts, contract, decisions
  tools/             conflict-scan.py · criteria-lint.py · reconcile.py
  modules/           you copy the starter in here, one folder per module you own
```

Everything runs locally. Nothing here needs network access, accounts, or any
production system.
