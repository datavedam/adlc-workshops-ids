# IDSNext ADLC workshop materials

This repository supports a hands-on workshop on agent-assisted development.
Claude Code performs the setup, inspection, writing, checking, and evidence
orchestration. A human reviews proposals and signs each tollgate.

The repository contains public sample data. The trainer supplies any
confidential business source through a local path.

## Start

You need `git`, Python 3, and Claude Code inside VS Code.

```bash
git clone https://github.com/datavedam/adlc-workshops-ids.git
cd adlc-workshops-ids
```

Use the setup prompt for the day you attend. Each prompt gives Claude Code the
source paths, commands, artifact list, and human review gates.

## Day 1 — harness, guard-rails, and baseline

```bash
cd day-01/demo
./setup.sh
cd /tmp/adlc-demo
python3 -m unittest discover -s tests
```

Read [day-01/PARTICIPANT.md](day-01/PARTICIPANT.md) and use
[day-01/SETUP-PROMPT.md](day-01/SETUP-PROMPT.md). Claude Code creates the
working `CLAUDE.md` from the demo source and records the observed checks.

## Day 2 — source conflicts, specifications, and decisions

```bash
cd day-02
python3 tools/conflict-scan.py
```

Read [day-02/PARTICIPANT.md](day-02/PARTICIPANT.md). Claude Code creates the
module pack from the starter files and the observed command output.

The pack contains `CLAUDE.md`, `CONFLICTS.md`, `FRAMING.md`, `DATA-CONTRACT.md`,
`ARCHITECTURE.md`, `SPEC.md`, three ADRs, `SKILLS.md`, and evidence records.
Human review changes proposal status to `APPROVED` or keeps the item `OPEN`.

Day 2 also has a short guide at [day-02/README.md](day-02/README.md).

## Day 3 — autonomous pack maintenance

Read [day-03/PARTICIPANT.md](day-03/PARTICIPANT.md) and use
[day-03/SETUP-PROMPT.md](day-03/SETUP-PROMPT.md). Day 3 uses a Day 2 module
pack as its source and makes the agent maintain the pack through evidence,
skills, review, and sign-off.

## Repository map

```text
day-01/
  PARTICIPANT.md       participant flow and gates
  SETUP-PROMPT.md      autonomous setup prompt
  demo/                throwaway hotel system
  starter/             guard-rail and CLAUDE.md starters
  tools/               local checks and measurements

day-02/
  PARTICIPANT.md       source-to-pack workflow
  SETUP-PROMPT.md      autonomous setup prompt
  data/                contradiction-preserving sample data
  starter/             pack templates and evidence contract
  tools/               conflict, criteria, reconciliation, and pack checks

day-03/
  PARTICIPANT.md       autonomous maintenance workflow
  SETUP-PROMPT.md      autonomous maintenance prompt
  starter/             source and review contract
```

## Network boundary

Local workshop commands use the Python standard library and local files.
The agent runs the four pinned skills.sh installs. Human review checks the
skill sources, lock hashes, and review results.
