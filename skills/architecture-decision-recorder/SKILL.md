---
name: architecture-decision-recorder
description: Create architecture decision records that preserve context, alternatives, tradeoffs, consequences, evidence, and reversal criteria. Use when a durable technical choice is being made or revisited; do not rewrite history after outcomes are known.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Architecture Decision Recorder

## Purpose

Make technical decisions inspectable, challengeable, and reversible where possible.

## Required inputs

- decision question and constraints
- considered options and evidence
- stakeholders, time horizon, and reversibility needs

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. State the decision in neutral terms and identify the forces that materially constrain it.
2. Document viable alternatives, including continuing the current state.
3. Compare options using explicit criteria, uncertainty, costs, risks, and operational consequences.
4. Record the selected option, why it won, and what evidence would invalidate it.
5. Define adoption, migration, ownership, observability, and reversal conditions.
6. Preserve superseded decisions through links rather than overwriting their original context.

## Output contract

- versioned architecture decision record
- option comparison
- consequence and risk register
- review and reversal triggers

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Separate facts, forecasts, and preferences.
- Do not hide dissent or discarded viable alternatives.
- Avoid embedding secrets or sensitive implementation details unnecessarily.

