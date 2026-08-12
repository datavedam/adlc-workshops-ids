## Day 3 rules

- Read the module `SPEC.md` before you plan a task.
- Use `../day-02/data/fx1-sample.json` as the local FX1 input.
- Keep the source data unchanged.
- Use `CONFLICTS.md` for source decisions.
- Compute derived metrics from base fields at render time.
- Run the end-to-end check before you report completion.
- Run `python3 ../day-02/tools/reconcile.py` before a merge when the task changes financial output.
- Keep written commentary within the workshop ASD-STE100 rule.
- Record the command and result in the evidence file.

## Agent-owned Day 3 workflow

- Discover the first valid Day 2 module in lexical order.
- Use module key `fnb` when the Day 2 module area has no valid pack.
- Write `SPEC.md`, `SKILLS.md`, `EVIDENCE.md`, and the project context files.
- Install the four skills listed in `starter/skills-lock.json`.
- Record source paths, command output, lock hashes, statuses, owners, and open questions.
- Keep source facts `OBSERVED` or `DERIVED`.
- Keep business choices `PROPOSED` until a named lead reviews them.
- Run the lint, reports, reconciliation check, and evidence review before sign-off.
