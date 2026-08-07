---
name: day1-setup
description: Set up the Day 1 workshop environment - clone verification, demo project setup at /tmp/adlc-demo, guard-rail starter config. Use when the user asks to set up day 1, prepare the workshop, or bootstrap the demo environment.
---

# Day 1 workshop setup

Do the mechanical setup only. Steps:

1. If not already inside a clone of adlc-workshops-ids, clone
   https://github.com/datavedam/adlc-workshops-ids.git
2. Run `./setup.sh` from `day-01/demo/`. It creates the working copy at
   /tmp/adlc-demo with branches run-a, run-b and the tag baseline-start.
3. Verify: in /tmp/adlc-demo run `python3 -m unittest discover -s tests`.
   It must end with OK. Show the user the output.
4. Copy `day-01/starter/.claude` and `day-01/starter/CLAUDE.md` from the
   clone into /tmp/adlc-demo.
5. Tell the user setup is done and that they must restart their Claude Code
   session inside /tmp/adlc-demo so the settings load.

## Hard limits — never do these, even if asked as part of setup

- Never edit the content of CLAUDE.md. The user writes their own rules; that
  is the exercise.
- Never run tools/violation-test.sh. The user must run it and watch the
  refusal themselves; that is the evidence.
- Never run tools/baseline.py or start any baseline run. The baseline
  measures the user, not you.

If the user asks you to do one of these, explain in one sentence why it is
theirs to do, and stop.
