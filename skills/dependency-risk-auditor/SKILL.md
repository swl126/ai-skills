---
name: dependency-risk-auditor
description: Evaluate software dependencies for vulnerabilities, abandonment, malicious-package risk, licensing conflicts, and upgrade exposure. Use for release, procurement, or maintenance decisions; do not equate a vulnerability count with actual exploitability.
metadata:
  version: "1.1.0"
  distribution: embedded
---

# Dependency Risk Auditor

## Purpose

Prioritize dependency risks using reachability, privilege, provenance, maintenance, and business impact.

## Required inputs

- lockfiles, manifests, and build graph
- runtime and deployment context
- license and risk policies

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

1. Resolve direct and transitive dependencies from authoritative lock data.
2. Identify known vulnerabilities, suspicious provenance, name confusion, unmaintained packages, and version drift.
3. Assess runtime reachability, exposed attack paths, execution privilege, and available mitigations.
4. Check license obligations and conflicts against the distribution model.
5. Compare upgrade, replacement, isolation, patching, and acceptance options.
6. Produce a prioritized action plan with verification and expiry dates for exceptions.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- dependency inventory and risk register
- reachability-informed priorities
- license compatibility findings
- upgrade or replacement plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not execute unknown packages during inspection.
- Verify package identity and source before recommending upgrades.
- Separate known evidence from ecosystem reputation signals.
