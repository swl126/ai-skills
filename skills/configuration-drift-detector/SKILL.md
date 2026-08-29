---
name: configuration-drift-detector
description: Compare infrastructure, application, and security configurations across environments to identify undocumented or risky drift. Use for authorized environment reconciliation; do not overwrite differences until intent and ownership are resolved.
metadata:
  version: "1.1.0"
  distribution: embedded
---

# Configuration Drift Detector

## Purpose

Distinguish legitimate environment variance from accidental or unsafe divergence.

## Required inputs

- configuration snapshots or APIs
- declared baseline and environment roles
- approved exceptions and secret-handling rules

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

1. Normalize representations while preserving semantically meaningful types and defaults.
2. Redact secret values but compare presence, source, version, and scope metadata.
3. Classify differences as expected, approved exception, unexplained drift, or critical control failure.
4. Trace drift to change history, ownership, and downstream behavioral impact.
5. Recommend reconciliation direction based on the declared baseline rather than majority state.
6. Produce repeatable comparison rules and exception expiry dates.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- normalized drift report
- risk-ranked unexplained differences
- approved exception register
- reconciliation and prevention plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not expose secrets in diffs.
- Do not apply production changes without explicit authorization.
- Account for intentional environment-specific values before labeling drift.
