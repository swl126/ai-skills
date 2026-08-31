---
name: row-level-security-auditor
description: Audit database row-level security policies for cross-tenant exposure, privilege escalation, missing operation coverage, and unsafe defaults. Use for authorized schema and policy review; do not claim isolation from policy text without enforcement tests.
metadata:
  version: "2.0.0"
  distribution: embedded
---

# Row Level Security Auditor

## Purpose

Verify that each role can access only the rows and operations permitted by the tenancy model.

## Required inputs

- schema, roles, and tenancy model
- RLS policies and helper functions
- authorized test identities or fixtures

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

1. Enumerate protected tables, views, operations, roles, ownership, security-definer functions, and bypass privileges.
2. Translate intended access rules into subject-action-object test cases.
3. Inspect USING and WITH CHECK logic for SELECT, INSERT, UPDATE, DELETE, joins, nulls, and tenant changes.
4. Test positive and negative cases with isolated fixtures where authorized.
5. Trace exposures through views, functions, service roles, foreign keys, and indirect references.
6. Deliver policy corrections and a regression matrix covering every protected operation.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- table-operation-role coverage matrix
- verified exposure findings
- corrected policy recommendations
- RLS regression cases

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Use non-production fixtures unless production testing is explicitly authorized.
- Never expose real tenant data in evidence.
- Do not confuse application filters with database-enforced isolation.
