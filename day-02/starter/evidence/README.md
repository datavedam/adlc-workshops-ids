# Evidence directory

Claude Code writes exact command output and review records here.

Use one file for each meaningful command or review. Include the command, date,
working directory, exit code, and output. Link each file from `EVIDENCE.md`.

Use these names when the matching step runs:

```text
source-inventory.md
conflict-scan.txt
criteria-lint.txt
pack-check.txt
diff-check.txt
skills-find-claude-md.txt
skills-find-adr.txt
skills-find-spec.txt
skills-find-review.txt
skills-list.json
claude-md-review.md
spec-review.md
pack-review.md
adr-001-attack.md
adr-002-attack.md
adr-003-attack.md
tg1-violation.txt
tg2-cold-run.txt
```

The agent writes each record. A human reviews the record and signs the gate.
