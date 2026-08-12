# ADR-002 — <agent writes the decision as a statement>

**Status:** PROPOSED · **Date:** <agent records date>
**Owner:** <agent records owner or OPEN>
**Source set:** <agent records paths and locators>

## Context

<Agent records the forces from source files, command output, and approved
scope. Every factual sentence has a path and locator.>

**Evidence:** <OBSERVED or DERIVED source record>

## Decision

<Agent writes one proposed action. The agent records a business assumption as a
proposal and gives it to the human for approval.>

**Status:** PROPOSED

## The case against

<Agent writes the strongest other view from source evidence and review input.>

**Status:** PROPOSED · **Source:** <path, locator, or review record>

## The agent's attack

**Skill:** <source and skill name, or OPEN>
**Prompt used:**

> Here is the proposed decision and its source evidence. Argue against it.
> Give the three strongest reasons it can fail. Name the evidence or condition
> that would prove each reason. Mark each claim OBSERVED, DERIVED, PROPOSED, or
> OPEN. Use the source files and command output only.

**Output record:** `evidence/adr-002-attack.md`

1. <agent records the strongest attack and source>
2. <agent records the second attack and source>
3. <agent records the third attack and source>

## Outcome

<Agent records the human response, the changed decision, or the open question.>

**Status:** PROPOSED / APPROVED / OPEN
**Approved by:** <human name or OPEN>
**Approved on:** <date or OPEN>
