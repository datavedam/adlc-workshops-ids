# Let Claude Code build the Day 3 evidence pack

Open Claude Code from the public repository root. Paste this prompt.

```text
Work inside day-03. Own every file edit and every command in this task.

## 1. Discover the inputs

1. Read `day-03/README.md`, `day-03/PARTICIPANT.md`, `day-03/EARS.md`, every file under
   `day-03/starter/`, and command help for every local tool.
2. List `../day-02/modules/` in lexical order.
3. Select the first directory that contains `CONFLICTS.md`, `FRAMING.md`,
   `DATA-CONTRACT.md`, and `ARCHITECTURE.md`.
4. When the Day 2 module directory is empty, use module key `fnb` and copy
   `../day-02/starter/` into `../day-02/modules/fnb/`.
5. Record the selected module key and every source path in
   `evidence/day-03/source-inventory.md`.
6. Use `../day-02/data/fx1-sample.json` as the available FX1 source.
7. Search these local locations for an extra source document:
   `../sources`, `../data`, `../../sources`, and `../../data`.
8. Record an absent confidential BRD as an `OPEN` item with an owner and a
   question. Continue with the available public source.

## 2. Create the workspace

1. Create `modules`, `evidence/day-03`, `reports`, and `.claude`.
2. Copy the selected Day 2 module to `modules/<module-key>`.
3. Copy every file under `starter/module/` into `modules/<module-key>`.
4. Copy every file under `starter/.claude/` into `.claude/`.
5. Copy the starter report and evidence templates into their working paths.
6. Create or update the project `CLAUDE.md` from the Day 2 module rules and
   `starter/CLAUDE-DAY3-BLOCK.md`.
7. Create `modules/<module-key>/SPEC.md`, `SKILLS.md`, and `EVIDENCE.md`.
8. Keep every source claim with a path and a page, line, JSON path, or command
   locator.
9. Use these statuses in every record: `OBSERVED`, `DERIVED`, `PROPOSED`,
   `APPROVED`, and `OPEN`.
10. Turn each missing input into an `OPEN` item. Continue the run with the
    available evidence.

## 3. Install and use the selected skills

Use the skills.sh CLI. Run each command with project scope and save the exact
output in `evidence/day-03/skills-install.txt`:

    npx skills add https://github.com/anthropics/claude-plugins-official --skill claude-md-improver --agent claude-code --copy -y
    npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill architecture-decision-records --agent claude-code --copy -y
    npx skills add https://github.com/davila7/claude-code-templates --skill requirements-clarity --agent claude-code --copy -y
    npx skills add https://github.com/obra/superpowers --skill verification-before-completion --agent claude-code --copy -y
    npx skills list --json | tee evidence/day-03/skills-list.json

1. Read each installed `SKILL.md`.
2. Compare the generated `skills-lock.json` with
   `starter/skills-lock.json`.
3. Record each source, skill name, local path, hash, command result, and use
   result in `modules/<module-key>/SKILLS.md`.
4. Use `claude-md-improver` to review `CLAUDE.md`.
5. Use `architecture-decision-records` to review all three Day 2 ADRs.
6. Use `requirements-clarity` to review `SPEC.md`.
7. Use `verification-before-completion` to review the complete evidence pack.
8. Keep each skill review in `evidence/day-03/`.

## 4. Write and check the artifacts

1. Write `SPEC.md` from the Day 2 pack and the available source.
2. Write at least five EARS criteria. Each criterion names one condition,
   result, source, and check.
3. Write the end-to-end check and the expected result.
4. Write `CLAUDE.md`, the module skill, and the reconcile command from the
   selected Day 2 rules.
5. Run these checks and save exact output:

    python3 tools/spec-lint.py modules/<module-key>/SPEC.md | tee evidence/day-03/spec-lint.txt
    python3 tools/rework-report.py --self-test | tee evidence/day-03/rework-self-test.txt
    python3 tools/token-report.py --self-test | tee evidence/day-03/token-self-test.txt
    python3 tools/reconcile-report.py --self-test | tee evidence/day-03/reconcile-self-test.txt
    python3 tools/pack-check.py modules/<module-key> --project-file CLAUDE.md | tee evidence/day-03/pack-check.txt
    git diff --check | tee evidence/day-03/diff-check.txt

6. Run the fresh-agent cold task from a new session. Use the exact task in
   `PARTICIPANT.md`. Save the prompt, session identifier, questions, output,
   checks, and result in `evidence/day-03/cold-run.json`.
7. Run the same task as Run A and Run B. Keep the task, commit, data,
   criteria, reviewer, and evidence fields fixed. Change the knowledge base
   only between runs.
8. Write `reports/rework.json` and run `python3 tools/rework-report.py`.
9. Run the same task with full and reduced context. Record input, cached,
   output, time, defects, and merged changes for both runs.
10. Write `reports/tokens.json` and run `python3 tools/token-report.py`.

## 5. Prepare review and TG3

1. Show the selected module, source ledger, generated files, installed skills,
   exact checks, and full changed-file list.
2. Mark business choices `PROPOSED` until a named human approves them.
3. Keep missing source facts `OPEN` with an owner and a question.
4. Write the human name, date, decision, and commit hash fields in
   `modules/<module-key>/EVIDENCE.md`.
5. Run the Day 1 violation test while the human watches. Save the output.
6. Stop at the review gate. The human reviews citations, proposed choices,
   skill hashes, checks, and evidence before sign-off.
7. Apply review answers, rerun affected checks, and update evidence.

The agent owns discovery, writing, skill installation, command orchestration,
and evidence files. The human owns business approval, observation of the
guard test, and TG3 sign-off.
```
