---
name: release-readiness-gate
description: Evaluate whether a software or AI release is safe to ship using tests, migrations, security findings, documentation, rollback, monitoring, and evidence. Use for explicit release decisions; do not convert unresolved critical risks into an averaged score.
metadata:
  version: "1.1.0"
  distribution: embedded
---

# Release Readiness Gate

## Purpose

Produce a defensible ship, conditional-ship, or block decision tied to evidence.

## Required inputs

- release scope and change set
- test, security, migration, and operational evidence
- risk tolerance and rollback requirements

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

1. Define mandatory gates and critical blockers before reviewing results.
2. Trace each material change to tests, documentation, migration needs, monitoring, and rollback.
3. Review failed, flaky, skipped, or stale evidence rather than accepting headline pass rates.
4. Assess open vulnerabilities, data risks, compatibility, dependencies, and operational readiness.
5. Record exceptions with owner, justification, compensating controls, and expiry.
6. Issue the decision with exact blockers or conditions and a post-release verification window.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- release gate matrix
- unresolved risk and exception register
- ship or block decision
- rollback and post-release verification plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Never average away a critical safety or security failure.
- Do not treat absence of evidence as passing evidence.
- Require explicit authority for risk acceptance.
