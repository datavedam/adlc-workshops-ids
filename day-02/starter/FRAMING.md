# FRAMING — <module name>

**Owner:** <your name> · **Module:** <module key from fx1-sample.json> · **Day 2**

## Intent
One paragraph. What this module tells a hotel general manager, and what
decision it helps them make. Write it in plain sentences.

## Non-goals
What you will not build. Be specific. "No live data" is weak. "No connection to
FX Suite; the module reads only data/fx1-sample.json" is a non-goal.

- ...
- ...

## Acceptance criteria
At least four. Each one must be a check a machine could run.
Use GIVEN / WHEN / THEN, or SHALL, and name a number, a field or a file.

1. GIVEN ... WHEN ... THEN ...
2. ...
3. ...
4. Every commentary string this module renders SHALL pass ste-check.py.

Test them:  python3 tools/criteria-lint.py modules/<mine>/FRAMING.md
