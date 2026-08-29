---
name: secrets-hygiene-auditor
description: Audit repositories and operational practices for exposed credentials, unsafe examples, excessive token scope, weak rotation, and secret-handling gaps. Use for defensive review; do not print or redistribute discovered secret values.
metadata:
  version: "1.1.0"
  distribution: embedded
---

# Secrets Hygiene Auditor

## Purpose

Find and contain credential exposure while improving the lifecycle from creation through revocation.

## Required inputs

- authorized repositories or configurations
- secret stores and credential types
- rotation, logging, and incident procedures

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

1. Inventory expected secret types, storage locations, scopes, owners, and consumers.
2. Scan authorized content and history using value-redacting evidence; distinguish live secrets from placeholders.
3. Assess scope, lifetime, environment separation, logging exposure, CI handling, and developer workflows.
4. For suspected live exposure, prioritize revocation and rotation over cosmetic removal.
5. Recommend secret-manager use, short-lived credentials, detection hooks, and exception handling.
6. Record verification that replacement credentials work and old credentials are revoked without retaining values.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- redacted finding register
- containment and rotation plan
- lifecycle-control assessment
- preventive control recommendations

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Never reproduce a secret in the report or tool output.
- Treat repository deletion as insufficient after exposure.
- Do not rotate or revoke credentials without the required authority.
