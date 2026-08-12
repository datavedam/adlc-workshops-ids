---
name: day1-setup
description: Set up Day 1, generate the working CLAUDE.md from source evidence, and prepare human-observed checks.
---

# Day 1 workshop setup

Use this skill when a participant asks Claude Code to prepare Day 1.

## Steps

1. Clone `https://github.com/datavedam/adlc-workshops-ids.git` when the
   participant has no local clone.
2. Run `./setup.sh` from `day-01/demo/`.
3. Verify `/tmp/adlc-demo` with
   `python3 -m unittest discover -s tests`.
4. Copy `day-01/starter/.claude`, `day-01/starter/CLAUDE.md`, and
   `day-01/starter/skills-lock.json` into the working copy.
5. Read the demo source, tests, README files, and command output.
6. Fill the working `CLAUDE.md` from those sources.
7. Record source paths, commands, output, statuses, and review results under
   `evidence/`.
8. Install the two skills listed in `skills-lock.json` with project scope and
   copied files.
9. Read each installed `SKILL.md` and use its review procedure.
10. Record each source, command, path, hash, review result, and changed line.
11. Run the guard test while the human watches the terminal.
12. Show the changed files and pause at the human review gate.

## Status words

Use `OBSERVED`, `DERIVED`, `PROPOSED`, `APPROVED`, and `OPEN`.

Use `OBSERVED` for file or command facts. Use `DERIVED` for local formulas or
check results. Use `PROPOSED` for agent recommendations. Use `APPROVED` after a
named human decision. Use `OPEN` for a source gap with an owner and question.

## Human gates

The agent writes the artifacts and runs the commands. The human reviews source
references, reviews skill hashes, watches the guard test, reviews the baseline
plan, and signs the evidence.
