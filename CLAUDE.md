# CLAUDE.md — IDSNext ADLC workshop materials

## What this repository contains

This repository contains the public workshop source, exercises, templates, and
local checks. Participants use Claude Code to produce a reviewed project pack.

The public checkout contains no client-confidential BRD. A trainer supplies any
confidential source file through a local path during the workshop.

## Commands

```bash
# Day 1
day-01/demo/setup.sh
python3 -m unittest discover -s tests
day-01/tools/violation-test.sh

# Day 2
python3 day-02/tools/conflict-scan.py [module]
python3 day-02/tools/criteria-lint.py <FRAMING.md>
python3 day-02/tools/reconcile.py
python3 day-02/tools/pack-check.py modules/<module> --project-file CLAUDE.md

# Day 3
python3 day-03/tools/pack-check.py <pack> --project-file CLAUDE.md
```

Run the Day 2 and Day 3 commands from the matching day directory. The tools
read local files and print evidence. Human review establishes business
decisions.

## Autonomous artifact workflow

Claude Code owns the writing and orchestration of the participant pack.

1. Read the source files, starter templates, and command help.
2. Run the available local checks and save their exact output.
3. Create or update `CLAUDE.md`, `SPEC.md`, ADRs, evidence records, and the
   skills configuration from source content and observed output.
4. Mark each statement as `OBSERVED`, `DERIVED`, `PROPOSED`, `APPROVED`, or
   `OPEN`.
5. Show the human the source path, command, output, and changed lines for each
   proposal.
6. Wait for human review before marking a proposal `APPROVED`.
7. Re-run the checks after every approved change.
8. Write the human name, date, scope, and commit hash in the sign-off record.

The agent discovers the module key from the first non-empty module directory.
When no module exists, the agent uses `fnb` and records that selection.
The agent discovers source files under the workspace and records absent sources
as `OPEN` items. The agent writes every artifact from available inputs.

## Source and decision rules

- Keep `day-02/data/fx1-sample.json` unchanged. The file preserves the exercise.
- Use page, line, JSON path, or command references for every source claim.
- Use the source document to establish facts. Use command output to establish
  observed behavior. Use human review to establish a business decision.
- Keep an unresolved item `OPEN` with an owner and a question. Keep a candidate
  decision `PROPOSED` until a human approves it.
- Keep `CONFLICTS.md`, `SPEC.md`, `CLAUDE.md`, and ADRs consistent after each
  approved change.
- Keep `day-02/out/` empty until the cold-run task asks the agent to write
  `pl.json`.
- Let `conflict-scan.py` and `reconcile.py` report results. Let a human judge
  what the results mean for the business.
- Keep client-confidential source files outside this public repository.

## Human gates

The agent may run commands, create evidence files, write the pack, and prepare a commit.

The human reviews source citations, confirms or changes proposed decisions,
reviews installed skill hashes, watches the evidence commands run, and signs
the final pack against its commit hash.

The guard configuration protects paths and commands. A human watches the
violation test and records the observed refusal in the evidence record.

## Skills from skills.sh

Skills installation is the only workshop step that may use the network.

The agent uses four pinned skills for `CLAUDE.md` improvement, ADR work,
requirements and specification work, and verification work.

The agent installs the pinned skills with project scope and copies their files
for repeatable local use. The agent records the source, skill name, command,
installed files, hash, risk, and CLI output in `SKILLS.md` and `evidence/`.

All other workshop commands use the local repository and Python standard
library. Participants can continue offline after the selected skills finish.

## Conventions

- Participant text uses short sentences and active voice.
- Markdown prose wraps at 80 columns where practical.
- Generated artifacts use the status words defined above.
- Claude Code fills each template from source evidence before the participant
  reviews the generated pack.
