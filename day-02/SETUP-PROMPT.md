# Let Claude Code build the Day 2 project pack

Open Claude Code in the parent folder and paste this prompt. Claude Code owns
discovery, writing, skill installation, command runs, and evidence capture.

```text
Work inside the public clone's day-02 directory.

## 1. Discover the inputs

1. Read `README.md`, every file under `starter/`, and command help for every
   local tool.
2. List `modules/` in lexical order.
3. Select the first module directory that contains source-backed files.
4. When `modules/` has no valid module, set `MODULE_KEY=fnb` and copy
   `starter/` into `modules/fnb/`.
5. Use `data/fx1-sample.json` as the available public source.
6. Search `../sources`, `../data`, `../../sources`, and `../../data` for an
   extra local source document.
7. Record every selected and absent source in `evidence/source-inventory.md`.
8. Record an absent confidential BRD as `OPEN` with an owner and a question.
   Continue with the available public source.

## 2. Create the pack

1. Create `evidence/`, `modules/<MODULE_KEY>/`, and `out/`.
2. Copy every file under `starter/` into `modules/<MODULE_KEY>/`.
3. Create or update the project `CLAUDE.md` from source files, local tools,
   command output, and the module pack.
4. Write every file in the module pack. Write `CONFLICTS.md`, `FRAMING.md`,
   `DATA-CONTRACT.md`, `ARCHITECTURE.md`, `SPEC.md`, three ADRs, `SKILLS.md`,
   and `EVIDENCE.md`.
5. Keep each source claim with a path and a page, line, JSON path, or command
   locator.
6. Use these statuses in every record: `OBSERVED`, `DERIVED`, `PROPOSED`,
   `APPROVED`, and `OPEN`.
7. Turn each missing source value into an `OPEN` item with an owner and a
   question. Continue the run with available evidence.
8. Keep `data/fx1-sample.json` unchanged.

## 3. Install and use the selected skills

Run these project-scoped commands. Save exact output in `evidence/skills-install.txt`:

    set -o pipefail

    npx skills add https://github.com/anthropics/claude-plugins-official --skill claude-md-improver --agent claude-code --copy -y | tee evidence/skills-install.txt
    npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill architecture-decision-records --agent claude-code --copy -y | tee -a evidence/skills-install.txt
    npx skills add https://github.com/davila7/claude-code-templates --skill requirements-clarity --agent claude-code --copy -y | tee -a evidence/skills-install.txt
    npx skills add https://github.com/obra/superpowers --skill verification-before-completion --agent claude-code --copy -y | tee -a evidence/skills-install.txt
    npx skills list --json | tee evidence/skills-list.json

1. Read each installed `SKILL.md`.
2. Compare `skills-lock.json` with `starter/skills-lock.json`.
3. Record source, skill name, local path, lock hash, command output, and use
   result in `modules/<MODULE_KEY>/SKILLS.md`.
4. Use `claude-md-improver` to review `CLAUDE.md`.
5. Use `architecture-decision-records` to review all three ADRs.
6. Use `requirements-clarity` to review `SPEC.md` and `FRAMING.md`.
7. Use `verification-before-completion` to review the complete project pack.
8. Save each review in `evidence/`.

## 4. Run the checks

    python3 tools/conflict-scan.py | tee evidence/conflict-scan.txt
    python3 tools/conflict-scan.py MODULE_KEY | tee evidence/conflict-scan-MODULE_KEY.txt
    python3 tools/criteria-lint.py modules/MODULE_KEY/FRAMING.md | tee evidence/criteria-lint.txt
    python3 tools/pack-check.py modules/MODULE_KEY --project-file CLAUDE.md | tee evidence/pack-check.txt
    git diff --check | tee evidence/diff-check.txt

Replace `MODULE_KEY` in commands with the selected key.

Run the Day 1 guard test while the human watches. Save its output in
`evidence/tg1-violation.txt`.

Run the Day 2 TG2 task in a fresh Claude Code session:

    Using only the project pack in this folder, build the Consolidated P&L card,
    write out/pl.json, run tools/reconcile.py, and record the command output.

Save the prompt, session identifier, questions, command output, result, and
reconciliation output in `evidence/tg2-cold-run.txt`.

## 5. Review gate

Show the selected module, source ledger, proposed decisions, installed skills,
lock hashes, exact check output, and changed-file list.

Keep source-backed facts `OBSERVED` or `DERIVED`. Keep business choices
`PROPOSED` until a named human approves them. Keep missing inputs `OPEN` with
an owner and a question.

Write the human name, date, decision, scope, and commit hash fields in
`modules/MODULE_KEY/EVIDENCE.md`. Apply review answers, rerun affected checks,
and update the evidence.

The agent owns every file edit and command. The human reviews citations,
business decisions, skill hashes, guard-test output, cold-run output, and
sign-off.
```
