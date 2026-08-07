# The demo project

A small, self-contained hotel-system backend, built for this workshop. Two
properties, a few reservations, folio entries, and working tests. It stands in
for a real multi-property codebase, so nothing in this workshop needs access to
production code.

## Set up your own copy

```bash
./setup.sh
```

This builds a throwaway working copy at `/tmp/adlc-demo`, with its own git
history. Run it as many times as you like — it rebuilds the copy from scratch
every time, so you always start clean.

## Check it works

```bash
cd /tmp/adlc-demo
python3 -m unittest discover -s tests    # must end with OK
```

## What is in here

| File | What it is |
|---|---|
| `app/reservations.py` | The house pattern. Every rule the codebase lives by, shown in one function. |
| `app/db.py` | The database: schema and seed data. |
| `app/errors.py`, `app/log.py` | The house error types and the house logger. |
| `tests/` | The test suite. |
| `task-baseline.md` | **DEMO-2** — the measured task for Part 3. Read it before you start. |
| `CLAUDE.md.for-run-b` | A worked example of a good context file. |

The house rules, in one place: every query on guest data filters by
`property_id`. Money is `Decimal`, never `float`. Guest personal data never
appears in a log line. A missing record raises `NotFoundError`. Every new
public function ships with a test.

Requires only git and Python 3. No packages to install.
