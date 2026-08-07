# IDSNext ADLC workshop — materials

Hands-on materials for the *Advanced AI-Assisted Coding, Analytics and SDLC*
workshop. Days are added here as the workshop proceeds. Currently: **Day 1**.

## Start here

You need **git**, **Python 3**, and **Claude Code working inside VS Code**.

```bash
git clone https://github.com/datavedam/adlc-workshops-ids.git
cd adlc-workshops-ids/day-01/demo
./setup.sh
cd /tmp/adlc-demo
python3 -m unittest discover -s tests    # must end with OK
```

Prefer to let Claude Code do the setup for you? Paste the prompt in
**[day-01/SETUP-PROMPT.md](day-01/SETUP-PROMPT.md)**.

Then read **[day-01/PARTICIPANT.md](day-01/PARTICIPANT.md)**. It explains the
whole day and every command you will run.

## What is in this repository

```
day-01/
  PARTICIPANT.md     the day, part by part, with every command
  demo/              the demo project — your own working copy comes from here
  starter/           guard-rail starter pack: settings, hook, CLAUDE.md template
  tools/             baseline.py (measures your runs) · violation-test.sh (proves your guard-rails)
```

Everything runs locally. Nothing here needs network access, accounts, or any
production system.
