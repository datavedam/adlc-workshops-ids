# Day 2 — source to a reviewed project pack

Day 2 turns source files and command output into a project pack. Claude Code
discovers the inputs, writes every artifact, installs the selected skills, runs
the checks, and records evidence. Participants review the source and approve
business decisions.

## Outcomes

The agent creates a module pack with:

- `CLAUDE.md`;
- `CONFLICTS.md`;
- `FRAMING.md`;
- `DATA-CONTRACT.md`;
- `ARCHITECTURE.md`;
- `SPEC.md`;
- three ADRs;
- `SKILLS.md`;
- `EVIDENCE.md`;
- command output under `evidence/`.

## Autonomous working agreement

The agent selects the first valid module directory. The agent uses `fnb` when
the module area has no valid pack. The agent records the selection and every
source path.

The agent writes all project files. An absent source value becomes an `OPEN`
item with an owner and a question. A source-backed result becomes `OBSERVED`
or `DERIVED`. A business choice becomes `PROPOSED` and remains open until a
named human approves it.

## Start

Run from the public repository root:

```bash
cd adlc-workshops-ids/day-02
python3 tools/conflict-scan.py
python3 tools/criteria-lint.py starter/FRAMING.md
python3 tools/pack-check.py starter --project-file starter/CLAUDE.md
```

Start the agent with [SETUP-PROMPT.md](SETUP-PROMPT.md). The agent creates the
module pack and the evidence files.

## Day 2 flow

| Part | Agent result | Human gate |
|---|---|---|
| 1 · Source and evidence | Source ledger and scan output | Review paths and locators |
| 2 · Pack creation | Project files and three ADRs | Review every proposal and open question |
| 3 · Skills and challenge | Installed skills and review records | Review hashes and skill output |
| 4 · TG2 cold run | Fresh-agent output and reconciliation | Watch the run and sign evidence |

## ADR recap and review

Open `starter/adr/001-title.md`. Point to these sections:

1. `Context` records the source forces.
2. `Decision` records the proposed action.
3. `The case against` records the strongest competing option.
4. `The agent's attack` records three failure reasons and test conditions.
5. `Outcome` records the human response, revision, or open result.

Show these three starter ADR files:

```text
starter/adr/001-title.md
starter/adr/002-title.md
starter/adr/003-title.md
```

The agent fills all three records. The participant reviews the source and the
attack output. The participant records business approval in `EVIDENCE.md`.

## Skills.sh workflow

The agent uses these project-scoped skills:

| Work area | Skill |
|---|---|
| `CLAUDE.md` review | `claude-md-improver` |
| ADR review | `architecture-decision-records` |
| Specification review | `requirements-clarity` |
| Evidence review | `verification-before-completion` |

The agent records source, command, local path, lock hash, installed files,
review prompt, result, and status in `SKILLS.md` and `evidence/`.

## Checks

```bash
python3 tools/conflict-scan.py | tee evidence/conflict-scan.txt
python3 tools/conflict-scan.py <module> | tee evidence/conflict-scan-<module>.txt
python3 tools/criteria-lint.py modules/<module>/FRAMING.md | tee evidence/criteria-lint.txt
python3 tools/pack-check.py modules/<module> --project-file CLAUDE.md | tee evidence/pack-check.txt
git diff --check | tee evidence/diff-check.txt
```

The agent saves exact output. The participant reviews a failed result and the
source boundary for each claim.

## TG1 and TG2

The participant watches the Day 1 guard test. The agent saves the command and
observed refusal in `evidence/tg1-violation.txt`.

The agent starts a fresh session for the Day 2 TG2 task:

```text
Using only the project pack in this folder, build the Consolidated P&L card,
write out/pl.json, run tools/reconcile.py, and record the command output.
```

The agent saves the prompt, session, questions, output, and reconciliation
result in `evidence/tg2-cold-run.txt`. The participant watches the run and
records the observed result.

## Sign-off

The lead signs the commit after these records exist:

- source ledger with locators;
- `CLAUDE.md` with rules, traps, commands, and review status;
- checkable requirements in `SPEC.md`;
- conflict results with `PROPOSED`, `APPROVED`, or `OPEN` status;
- three ADRs with the five required sections and attack output;
- `SKILLS.md` with lock hashes and review results;
- `EVIDENCE.md` with watched commands and sign-off.

The agent writes the sign-off fields. The lead supplies the name, date,
decision, scope, and commit hash.
