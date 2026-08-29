---
name: prompt-injection-tester
description: Assess AI agents and retrieval systems for prompt injection, instruction conflicts, data exfiltration, and unsafe tool manipulation. Use for authorized defensive testing of a defined system; do not provide operational abuse against third-party systems.
metadata:
  version: "1.1.0"
  distribution: embedded
---

# Prompt Injection Tester

## Purpose

Determine whether untrusted content can override authority boundaries or cause unauthorized disclosure or actions.

## Required inputs

- authorized target and test scope
- system/tool authority model
- protected data and prohibited actions

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

1. Map trusted instructions, untrusted content channels, tools, secrets, and approval boundaries.
2. Create safe test cases for direct, indirect, encoded, multi-turn, and retrieved-content injection.
3. Use inert canaries and reversible test actions; never use real secrets or destructive payloads.
4. Record whether the system follows, refuses, asks approval, leaks canaries, or calls tools.
5. Trace successful bypasses to the confused authority or missing isolation control.
6. Recommend layered mitigations and regression cases, then retest within the original authorization.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- attack-surface map
- reproducible test matrix and evidence
- severity-ranked findings
- mitigations and regression suite

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Require explicit authorization and stop at the defined boundary.
- Use synthetic secrets and non-destructive targets.
- Do not publish unpatched exploit details or credentials.
