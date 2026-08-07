# The controlled task — Part 3 baseline measurement

This is a different task from the live demo. The live demo (see
README-DEMO.md) uses the folio-balance task and compares run-a against
run-b. This task is used only for the Part 3 baseline measurement, where
each participant does the same change three times: alone, with a chat
window, and with an agent. Never run this task on the run-a or run-b
branches, and never run the folio-balance task on a baseline branch. Keeping
the two tasks apart is what makes both measurements trustworthy.

```
TASK ID        DEMO-2
TITLE          Cancel a reservation
MODULE         app/ (new file: app/cancellations.py)
START COMMIT   the tag "baseline-start", set by setup.sh on the initial
               commit of the throwaway copy
```

## What it does

Add a function `cancel_reservation(property_id, reservation_id)` in a new
file, `app/cancellations.py`. Calling it marks the given reservation as
cancelled. A reservation that is already cancelled cannot be cancelled
again — calling it a second time is an error, not a silent no-op. A caller
scoped to one property must never be able to cancel a reservation that
belongs to a different property.

## Acceptance criteria

- [ ] Cancelling an active reservation sets its `status` to `"cancelled"`
      and returns the updated reservation record.
- [ ] Cancelling a reservation that belongs to a different property raises
      `NotFoundError`. The error must never reveal that the reservation
      exists — the caller gets the same error as for an unknown id.
- [ ] Cancelling an unknown reservation id raises `NotFoundError`.
- [ ] Cancelling a reservation that is already cancelled raises
      `ValidationError`, not `NotFoundError` and not a silent success.
- [ ] The change ships with unittest coverage, including the
      cross-property case.
- [ ] The function logs through the house logger (`app/log.py`), and no
      guest name, email, phone number or card data appears in any log line.

## Out of scope

Do not touch refunds, folio changes, or notifications. Do not change any
existing endpoint or function. The only new file should be
`app/cancellations.py`, plus its test file. If the task tempts you to also
"clean up" something nearby, leave it — that adjacent work is exactly what
makes the size of three runs impossible to compare fairly.

## Review rubric

When the review pass counts defects at the end of the exercise, each of
these counts as one defect:

- missing or wrong `property_id` filter — the function can be made to act
  on a reservation belonging to another property
- the reservation's current status is never checked, so cancelling twice
  either succeeds silently or does something other than raise
  `ValidationError`
- an error case raises the wrong exception type (for example, a missing
  reservation raises an unhandled exception instead of `NotFoundError`)
- guest name, email, phone number or card data appears in a log line
- no test exists for the change, or the test would still pass against a
  broken implementation (for example, a test that never exercises the
  cross-property case)
- files outside `app/cancellations.py` and its test file were touched

## How to run it three times

Each run starts from the same commit (`baseline-start`), on its own branch,
so the three runs never build on each other:

```bash
cd /tmp/adlc-demo        # the throwaway copy created by ./setup.sh

git checkout -b baseline/<yourname>/unassisted baseline-start
../tools/baseline.py start unassisted
#   ...do the task by hand...
../tools/baseline.py stop

git checkout -b baseline/<yourname>/chat baseline-start
../tools/baseline.py start chat
#   ...same task, chat window open...
../tools/baseline.py stop

git checkout -b baseline/<yourname>/agentic baseline-start
# Bring your guard-rails and context file onto this branch, and commit them
# BEFORE starting the clock. The tool measures your diff from the moment the
# run starts — committed config is excluded, uncommitted config would be
# counted as task work.
cp -r /path/to/clone/day-01/starter/.claude .     # or your own edited copies
cp /path/to/your/CLAUDE.md CLAUDE.md
git add -A && git commit -m "guard-rails for the agent run"
../tools/baseline.py start agentic
#   ...same task, agent...
../tools/baseline.py stop

../tools/baseline.py row     # prints your row for the Day 1 Baseline sheet
```

`../tools/baseline.py` is staged next to the throwaway copy by `setup.sh`
(`$(dirname <working copy>)/tools/baseline.py`), the same relative-path
layout used in the real workshop repo — you do not need to install or copy
anything by hand.
