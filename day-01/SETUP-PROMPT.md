# Let Claude Code do the setup

Open Claude Code (anywhere), paste this, and press enter:

```
Clone https://github.com/datavedam/adlc-workshops-ids.git into a folder of my
choice, run day-01/demo/setup.sh from inside day-01/demo, and then verify the
tests pass in /tmp/adlc-demo by running: python3 -m unittest discover -s tests
(it must end with OK). Then copy day-01/starter/.claude and
day-01/starter/CLAUDE.md from the clone into /tmp/adlc-demo. Do NOT edit the
CLAUDE.md content and do NOT run the violation test — I do those myself.
Tell me when you are done, show me the test output, and remind me to restart
my Claude Code session inside /tmp/adlc-demo so the settings load.
```

## What stays yours, on purpose

The agent does the plumbing. Three things it must not do for you, because they
are the evidence of the day:

1. **Editing `CLAUDE.md`.** The file's value is what only you know — the trap
   that burned your team. The agent does not know it.
2. **Running `../tools/violation-test.sh`.** The outcome of Part 2 is that
   *you watched it refuse*. Delegated, it is just a claim.
3. **The baseline runs.** The unassisted run is the control. The agent run is
   you driving. Both must be your hands.
