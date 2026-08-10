# CLAUDE.md — FX1 Executive Command Center

<!-- Part 3. You write this one. Keep it under 200 lines — aim for 60.
     Every line is read on every task and costs tokens every time.

     Test each line with one question:
         would this line have prevented a real bug we have already had?
     If not, cut it.

     Delete every angle-bracket placeholder before you commit. -->

## What this is

<Two lines. What the product is, and who reads it. Not what it is built with —
 the agent can see that. Who reads it changes what "good" means.>

## Commands

<The exact lines. Not a description of them. If you leave these out the agent
 guesses, and the first guess is wrong in every session from now on.>

```
<how you open it>
<how you run the checks>
python3 tools/reconcile.py
```

## Rules that do not bend

<Constraints where breaking one makes the build wrong, not untidy. Be specific.
 An agent cannot act on "follow best practice".

 You already know several of these. Some come from the document's own
 constraints. At least two come from what you found this morning — think about
 what would have to be true for those fourteen conflicts to be impossible to
 express rather than merely caught later.>

- ...
- ...
- ...

## Traps

<Where this project has already caught somebody out. The agent cannot read your
 git history, sit in your retro, or remember this morning. Left alone it will
 cheerfully walk back into it.

 Start with this question: if a fresh session opened the BRD tomorrow and
 believed it, what would it undo?>

- ...
- ...

## Conventions

<Only what the code does not already show. If the agent can work it out by
 opening two files, do not spend a line on it here.>

- ...

<!-- Check it before you commit:
       1. restart your session — config loads at session start
       2. ask: "What are the rules for this project?"
       3. ask: "What will you refuse to do in this repository?"
     If it cannot answer, this file is decoration. -->
