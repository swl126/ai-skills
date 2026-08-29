---
name: incident-postmortem-builder
description: Create blameless, evidence-grounded incident postmortems from timelines, logs, decisions, impacts, and recovery actions. Use after service or security incidents; do not invent causality when evidence is incomplete.
metadata:
  version: "1.1.0"
  distribution: embedded
---

# Incident Postmortem Builder

## Purpose

Turn an incident into defensible learning and owned corrective action rather than a narrative of individual blame.

## Required inputs

- time-stamped evidence and impact data
- response actions and decisions
- system context and prior related incidents

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

1. Build a normalized timeline separating observed facts, interpretations, and unknowns.
2. Define user, business, security, and operational impact with bounded estimates.
3. Trace contributing technical, process, detection, and organizational conditions without stopping at the triggering event.
4. Explain what worked, what delayed recovery, and where controls failed or were absent.
5. Create corrective actions tied to specific failure mechanisms, owners, evidence, and due dates.
6. Document unresolved questions and conditions that would change the conclusions.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- fact-based incident timeline
- impact and causal analysis
- corrective action register
- follow-up verification plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Remove credentials and unnecessary personal data.
- Avoid blame language and unsupported certainty.
- Coordinate disclosure of security details with remediation status.
