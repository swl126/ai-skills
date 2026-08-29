---
name: observability-designer
description: Design logs, metrics, traces, dashboards, service-level indicators, and alerts around real failure modes and user impact. Use when establishing or repairing observability; do not optimize for telemetry volume without decision value.
metadata:
  version: "1.1.0"
  distribution: embedded
---

# Observability Designer

## Purpose

Ensure operators can detect, explain, and act on meaningful system degradation.

## Required inputs

- service architecture and critical journeys
- failure modes and operational decisions
- telemetry platform, cost, privacy, and retention constraints

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

1. Identify user-visible outcomes, dependencies, and decisions operators must make.
2. Define SLIs and event semantics before dashboards; specify units, labels, cardinality, and ownership.
3. Map logs, metrics, and traces to failure hypotheses and correlation identifiers.
4. Design alerts around actionable symptoms, burn rates, or safety boundaries rather than raw noise.
5. Check privacy, secret leakage, retention, cost, sampling, and high-cardinality risks.
6. Validate with known failure scenarios and document runbook links and expected operator actions.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- telemetry specification
- SLI/SLO and alert definitions
- dashboard and runbook design
- coverage, cost, and privacy analysis

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not log secrets or unnecessary personal data.
- Prevent unbounded labels and telemetry cost explosions.
- Every page-level alert must have an owner and actionable response.
