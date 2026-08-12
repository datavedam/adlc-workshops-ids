# Let Claude Code build the Day 1 working pack

Open Claude Code anywhere and paste this prompt. Claude Code owns setup,
writing, skill installation, command runs, and evidence capture.

```text
Work inside the public clone's day-01 directory.

## 1. Build the demo workspace

1. Run `demo/setup.sh`.
2. Use the generated `/tmp/adlc-demo` workspace.
3. Copy every file under `starter/.claude/` into `/tmp/adlc-demo/.claude/`.
4. Copy `starter/CLAUDE.md` to `/tmp/adlc-demo/CLAUDE.md`.
5. Copy `starter/skills-lock.json` to `/tmp/adlc-demo/skills-lock.json`.
6. Create `/tmp/adlc-demo/evidence/`.
7. Read the demo source, tests, README files, and command help.
8. Run:

    cd /tmp/adlc-demo
    python3 -m unittest discover -s tests | tee evidence/setup-tests.txt

9. Write `evidence/source-inventory.md` with each rule, command, trap, path,
   locator, and status.
10. Use these statuses: `OBSERVED`, `DERIVED`, `PROPOSED`, `APPROVED`, `OPEN`.
11. Write and update `/tmp/adlc-demo/CLAUDE.md` from the source and test
    output. Write `evidence/CLAUDE-review.md` after the review.

## 2. Install and use the skills

Save exact output from these project-scoped commands:

    cd /tmp/adlc-demo
    npx skills add https://github.com/anthropics/claude-plugins-official --skill claude-md-improver --agent claude-code --copy -y | tee evidence/skills-install.txt
    npx skills add https://github.com/obra/superpowers --skill verification-before-completion --agent claude-code --copy -y | tee -a evidence/skills-install.txt
    npx skills list --json | tee evidence/skills-list.json

Read both installed `SKILL.md` files. Use `claude-md-improver` to review
`CLAUDE.md`. Use `verification-before-completion` to review the complete pack.
Compare the installed lock with `skills-lock.json`. Record the source, command,
local path, hash, review output, and changed lines in
`evidence/CLAUDE-review.md`.

## 3. Run the observed guard test

Run the guard test while the human watches the terminal:

    cd /tmp/adlc-demo
    ../tools/violation-test.sh | tee evidence/tg1-violation.txt

Record every attempt, response, exit code, and output. Record the observed
refusal in `evidence/EVIDENCE.md`.

## 4. Prepare the baseline

Read `demo/task-baseline.md` and prepare the commands for the three baseline
modes. Keep task, acceptance criteria, source data, reviewer, and evidence
fields fixed. Record the baseline command paths in `evidence/baseline-plan.md`.

## 5. Review and sign-off

Show the source ledger, generated `CLAUDE.md`, installed skills, lock hashes,
test output, guard output, baseline plan, and changed-file list.

Keep source facts `OBSERVED` or `DERIVED`. Keep business choices `PROPOSED`
until a named human approves them. Record missing inputs as `OPEN` with an
owner and a question.

Prepare the commit and sign-off fields. The human reviews source mappings,
skill hashes, guard output, and baseline inputs. Apply review answers and rerun
affected checks before the lead signs the commit hash.
```

Claude Code writes the working `CLAUDE.md` and evidence. The human reviews the
source mapping, observes the guard test, and signs the pack.
