# EARS — the first Day 3 lesson

EARS means **Easy Approach to Requirements Syntax**. Day 3 teaches EARS for the
first time. The pattern gives each requirement a visible condition, behavior,
result, and check.

Day 2 gives the source facts and project decisions. EARS turns one source
statement into one testable behavior.

## The four fields

| Field | Question | Example |
|---|---|---|
| Condition | What event, state, problem, or option starts the rule? | A user selects a KPI. |
| System | Which module acts? | The FX1 module. |
| Behavior | What SHALL the module do? | Open a drill-down. |
| Check | What gives pass or fail? | Observe the screen and list fields. |

Each requirement has one main behavior. Each result names a field, file, screen,
or response. Each check names a command or observation.

## The five EARS patterns

| Pattern | Use it for | Sentence shape | FX1 example |
|---|---|---|---|
| Ubiquitous | Every run | The module SHALL ... | The module SHALL read the local FX1 data file. |
| Event | A trigger | WHEN X, the module SHALL Y. | WHEN a user selects a KPI, the module SHALL open its detail view. |
| State | A state that stays true | WHILE X, the module SHALL Y. | WHILE a value lacks a source, the module SHALL show its status. |
| Unwanted | A problem | IF X, the module SHALL Y. | IF a field is absent, the module SHALL show the field name. |
| Optional | An available option | WHERE X, the module SHALL Y. | WHERE a benchmark exists, the module SHALL show the delta. |

Use the pattern that matches the source statement. Keep the condition and the
result visible in the sentence.

## Worked example

Source statement:

    Every KPI tile is clickable and opens a detailed report.

The phrase "detailed report" leaves the result open. The agent turns the source
into two EARS criteria.

    WHEN a user selects a KPI tile, the module SHALL open a drill-down.

    The drill-down SHALL show value, change versus LY, benchmark, trend chart,
    breakdown table, and commentary.

The check lists the six fields in the drill-down. A second check observes the
screen after a KPI selection.

## Agent task

Use this prompt for the first EARS card:

    Read the selected Day 2 source row, CONFLICTS.md, FRAMING.md, and
    DATA-CONTRACT.md.

    1. State the source path and locator.
    2. Select the EARS pattern.
    3. Draft one criterion with one condition and one result.
    4. Name the output field, file, screen, or response.
    5. Write one command or observation that gives pass or fail.
    6. Record an absent source value as OPEN with an owner and a question.

The agent writes the draft card. The participant reviews the source locator,
pattern, behavior, result, and check.

## Participant card

    Source sentence:
    Source path and locator:
    EARS pattern:
    Condition:
    System or module:
    Behavior:
    Result:
    Check command or observation:
    Expected result:
    Status:
    Owner:

## Review gate

A card passes the first lesson when:

- the source path and locator open;
- one EARS pattern matches the condition;
- the module or system is named;
- one behavior uses SHALL;
- one result names an observable artifact;
- one check gives a pass or fail result;
- each absent value has OPEN, an owner, and a question.

The agent carries the reviewed card into SPEC.md.
