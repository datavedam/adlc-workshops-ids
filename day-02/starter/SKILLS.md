# SKILLS — project configuration

Claude Code fills this file from skills.sh source output, installation output,
lock hashes, installed `SKILL.md` files, and review output.

## Install records

| Work area | Command | Output file | Status |
|---|---|---|---|
| CLAUDE.md improvement | `npx skills add ... --skill claude-md-improver ...` | `evidence/skills-install.txt` | OBSERVED |
| ADR | `npx skills add ... --skill architecture-decision-records ...` | `evidence/skills-install.txt` | OBSERVED |
| Requirements and specification | `npx skills add ... --skill requirements-clarity ...` | `evidence/skills-install.txt` | OBSERVED |
| Review and acceptance | `npx skills add ... --skill verification-before-completion ...` | `evidence/skills-install.txt` | OBSERVED |

## Selected skills

| Work area | Source | Skill name | Install command | Installed path | Lock hash | Status |
|---|---|---|---|---|---|---|
| <agent fills> | <source> | <skill> | <exact command> | <path> | <hash> | OBSERVED / OPEN |

## Use records

| Skill | Artifact | Prompt or task | Output file | Review result | Status |
|---|---|---|---|---|---|
| <agent fills> | <agent fills> | <agent fills> | <path> | <agent records> | OBSERVED / PROPOSED / APPROVED / OPEN |

## Human review

- Reviewed by: <human name or OPEN>
- Reviewed on: <date or OPEN>
- Risk or cost: <agent records the source risk>
- Review result: <agent records the result or OPEN>
