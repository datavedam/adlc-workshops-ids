# CONFLICTS — <module name>

Every conflict the scan found, and what you decided. None may be left open.

Find them:  python3 tools/conflict-scan.py <module>

| # | What disagrees | The numbers | Decision | Why |
|---|---|---|---|---|
| 1 | | | correct / assume | arithmetic, or the reason you cannot prove it |

## Corrections
For each one you can prove. Show the arithmetic.

**C-1 · <what>**
- Decided value: ...
- Proof: ...

## Stated assumptions
For each one you cannot prove. These go to IDS Next as open questions.

**A-1 · <what>**
- Chosen value: ...
- Why this one: ...
- Open question for the client: ...
