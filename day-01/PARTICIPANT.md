# Day 1 — harness, guard rules, and baseline

Day 1 shows how a project harness changes agent behavior. Claude Code performs
setup, writes the working `CLAUDE.md`, installs the selected skills, and saves
command evidence. The participant reviews the source mapping and observes the
guard test.

## Start

```bash
git clone https://github.com/datavedam/adlc-workshops-ids.git
cd adlc-workshops-ids/day-01/demo
./setup.sh
cd /tmp/adlc-demo
python3 -m unittest discover -s tests
```

Start the agent with [SETUP-PROMPT.md](SETUP-PROMPT.md). The agent creates the
working pack in `/tmp/adlc-demo`.

## Outcomes

| Part | Agent output | Human gate |
|---|---|---|
| 1 · Concepts and demo | prediction and failure evidence | Discuss the harness cause |
| 2 · Guard rules | `.claude/`, `CLAUDE.md`, and guard evidence | Watch and confirm the result |
| 3 · Baseline | three measured task runs | Review fixed inputs and measurements |
| 4 · TG1 | signed evidence | Lead signs the commit |

## Part 2 — guard rules and `CLAUDE.md`

Claude Code reads the source, tests, README files, and test output. It writes
`CLAUDE.md`, `evidence/source-inventory.md`, and
`evidence/CLAUDE-review.md`. Each rule, command, and trap has a source path,
locator, and status.

Run the guard test while the participant watches:

```bash
cd /tmp/adlc-demo
../tools/violation-test.sh | tee evidence/tg1-violation.txt
```

The agent records each attempt, response, exit code, and output. The
participant records the observed refusal in the evidence file.

## Skills.sh workflow

The agent uses project-scoped skills for `CLAUDE.md` review and verification:

```bash
npx skills add https://github.com/anthropics/claude-plugins-official --skill claude-md-improver --agent claude-code --copy -y
npx skills add https://github.com/obra/superpowers --skill verification-before-completion --agent claude-code --copy -y
npx skills list --json
```

The agent records each command, installed path, lock hash, review output, and
changed line in evidence. The participant reviews the result.

## Part 3 — baseline

The task is **DEMO-2: cancel a reservation**. Claude Code reads
`demo/task-baseline.md` and prepares the run commands. Keep the task,
acceptance criteria, source data, reviewer, and evidence fields fixed across
the three modes.

```bash
cd /tmp/adlc-demo
../tools/baseline.py start unassisted
../tools/baseline.py stop
../tools/baseline.py row
../tools/baseline.py evidence
```

The agent writes command output and the evidence record. The participant
records reviewed defects and provider token values.

## TG1 sign-off

A lead signs the evidence after these results exist:

- the test suite output ends with `OK`;
- `CLAUDE.md` has source references and review status;
- the participant watched the guard test and recorded the result;
- the three baseline runs use the same acceptance criteria;
- evidence files and configuration are committed.

The agent prepares the commit. The lead signs against its hash.
