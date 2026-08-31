---
name: api-contract-auditor
description: Audit OpenAPI or equivalent API contracts against implementation behavior, examples, errors, versioning, and compatibility expectations. Use before integration or release; do not infer implementation conformance from a specification alone.
metadata:
  version: "2.0.0"
  distribution: embedded
---

# Api Contract Auditor

## Purpose

Find contract defects that cause unsafe, ambiguous, or breaking client-server behavior.

## Required inputs

- API specification and version
- implementation or captured responses
- compatibility and consumer requirements

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Operating modes and local resources

- For substantive work, read [the operational playbook](references/playbook.md) before choosing tests, thresholds, or a decision.
- Use [the report template](assets/report-template.md) when a durable deliverable is requested. Preserve its evidence register and acceptance review even if the presentation format changes.
- Use [the example request](examples/request.md), [decision excerpt](examples/expected-output.md), and [validated worked report](examples/example-report.md) to calibrate scope and decisiveness, never as evidence for the current task.
- For a narrow question, apply only the relevant workflow steps and state which completion gates are outside scope.

## Executable engine

- Run the domain analyzer declared as `domain_executable` in [skill-package.json](skill-package.json) to collect or analyze primary evidence before applying the normalized-evidence gate.
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

1. Parse resources, operations, authentication, parameters, schemas, status codes, and examples.
2. Check internal consistency: required fields, nullability, formats, discriminator use, pagination, idempotency, and error envelopes.
3. Compare the contract with observed implementation behavior using authorized test cases.
4. Classify changes as compatible, conditionally compatible, or breaking for real consumers.
5. Inspect security declarations, authorization boundaries, sensitive fields, rate limits, and replay risks.
6. Return exact contract changes, implementation fixes, and consumer migration guidance.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- operation-level conformance matrix
- breaking-change report
- security and ambiguity findings
- prioritized remediation plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not send mutating requests to production without authorization.
- Redact tokens and sensitive response data.
- Separate spec defects from implementation defects.
