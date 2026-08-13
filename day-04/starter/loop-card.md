# The loop card

Print one for each person. Keep it beside the screen.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ANY REQUIREMENT  →  EVIDENCE                                            │
├──────────────────────────────────────────────────────────────────────────┤
│  1  UNDERSTAND   read the source · facts with paths · the open points     │
│  2  CONTEXT      the durable rules go in CLAUDE.md                        │
│  3  GRILL        ◆ one question at a time · a human answers               │
│  4  DECIDE       ◆ each answer becomes a record with the case against     │
│  5  SPECIFY      ◆ EARS criteria · scope boundary · one check             │
│  6  PLAN         small tasks · each one has its own check                 │
│  7  BUILD        one subagent for each task · two reviews after each      │
│  8  PROVE        ✓ tests · review · evidence · then the row closes        │
├──────────────────────────────────────────────────────────────────────────┤
│  ◆ = a human answers      ✓ = a human signs                              │
├──────────────────────────────────────────────────────────────────────────┤
│  STOP FOR A CHOICE.  NEVER STOP FOR A FACT.                              │
│                                                                          │
│  OBSERVED · DERIVED   →  continue, record the path                        │
│  PROPOSED · OPEN      →  stop, ask one question, name the owner           │
│  APPROVED             →  it is a rule now, nobody asks again              │
├──────────────────────────────────────────────────────────────────────────┤
│  A LOOKUP QUESTION IS A GAP IN YOUR HARNESS, NOT A FAULT IN THE AGENT.    │
│  Put the answer in the file. Do not answer it twice.                      │
├──────────────────────────────────────────────────────────────────────────┤
│  A ROW CLOSES ONLY WHEN COLUMN AO NAMES THE CHECK THAT PROVES IT.         │
└──────────────────────────────────────────────────────────────────────────┘
```

## The four proofs Day 5 reads

| # | Proof | Path |
|---|---|---|
| 1 | The loop ran end to end | `evidence/day-04/loop-run.md` |
| 2 | The tracker holds real rows | `tracker.xlsx` |
| 3 | The stop count and its split | `evidence/day-04/decisions.json` |
| 4 | The guard held | `evidence/day-04/guard.txt` |

Run this before you leave:

```bash
python3 tools/loop-check.py --file tracker.xlsx
```
