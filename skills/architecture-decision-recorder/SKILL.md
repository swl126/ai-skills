---
name: architecture-decision-recorder
description: Create architecture decision records that preserve context, alternatives, tradeoffs, consequences, evidence, and reversal criteria. Use when a durable technical choice is being made or revisited; do not rewrite history after outcomes are known.
metadata:
  version: "1.1.0"
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

## Operating modes and local resources

- For substantive work, read [the operational playbook](references/playbook.md) before choosing tests, thresholds, or a decision.
- Use [the report template](assets/report-template.md) when a durable deliverable is requested. Preserve its evidence register and acceptance review even if the presentation format changes.
- Use [the example request](examples/request.md), [decision excerpt](examples/expected-output.md), and [validated worked report](examples/example-report.md) to calibrate scope and decisiveness, never as evidence for the current task.
- For a narrow question, apply only the relevant workflow steps and state which completion gates are outside scope.

## Executable engine

- Read [the executable contract](references/executable-contract.md) before supplying normalized evidence.
- Validate inputs with `python3 scripts/assess.py validate --input INPUT.json`.
- Produce a deterministic decision with `python3 scripts/assess.py assess --input INPUT.json --out RESULT.json --report REPORT.md`.
- Use `--fail-on-block` in automation. The engine analyzes supplied evidence and never connects to or mutates production systems.

## Evidence discipline

- Give material evidence stable identifiers and cite those identifiers in findings.
- Separate observed facts, interpretations, unknowns, and recommendations.
- Record the target version, environment, collection time, and tool or method when freshness or reproducibility matters.
- Never upgrade missing evidence into a passing result. Mark it blocked and name what would resolve it.

## Workflow

1. State the decision in neutral terms and identify the forces that materially constrain it.
2. Document viable alternatives, including continuing the current state.
3. Compare options using explicit criteria, uncertainty, costs, risks, and operational consequences.
4. Record the selected option, why it won, and what evidence would invalidate it.
5. Define adoption, migration, ownership, observability, and reversal conditions.
6. Preserve superseded decisions through links rather than overwriting their original context.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

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
