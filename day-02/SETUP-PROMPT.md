# Let Claude Code do the setup

Open Claude Code (anywhere), paste this, and press enter:

```
Clone https://github.com/datavedam/adlc-workshops-ids.git into a folder of my
choice. From inside day-02, run: python3 tools/conflict-scan.py — it must print
a conflict report ending in a count. Then run: python3 tools/criteria-lint.py
starter/FRAMING.md — it is expected to flag most of the template's placeholder
lines, which is correct and shows the lint works. Then copy
day-01/starter/.claude into the repo root so the guard-rails are ready for
Part 3.

Do NOT edit day-02/data/fx1-sample.json — it contradicts itself on purpose.
Do NOT fill in anything under day-02/starter/ and do NOT create module folders.
Do NOT decide any conflict, and do NOT write a CLAUDE.md for me.

Tell me when you are done, show me the scan output, and remind me to restart my
Claude Code session so the settings load.
```

## What stays yours, on purpose

The agent does the plumbing. Five things it must not do for you, because they
are the evidence of the day:

1. **Deciding a conflict.** The scan does the arithmetic and cites the page.
   Which number survives is a judgement about a business, and the gate checks
   that a person made it.
2. **Writing your acceptance criteria.** A criterion is a promise about what
   "finished" means. Delegating it means you find out what you promised later.
3. **Writing your `CLAUDE.md`.** Its whole value is what only you know — the
   trap you hit this morning, the rule that would have prevented it. The agent
   was not there.
4. **Choosing your skills.** Installing something is a supply-chain decision. If
   you cannot say why this project needs it, do not install it.
5. **The Part 4 cold run.** The point is that *somebody else's* agent runs your
   pack, with no help from you. Run it yourself and you have proved nothing.

## If the setup fails

- `conflict-scan.py` prints nothing → you are not inside `day-02/`.
- The guard-rails do not block anything → **restart your session.** Config loads
  at session start. This is the most common problem by a distance.
- Anything else → say so at the start of the session rather than debugging alone.
  Somebody else in the room has the same problem.
