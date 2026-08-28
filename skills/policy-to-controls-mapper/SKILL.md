---
name: policy-to-controls-mapper
description: Translate policy statements into implementable controls, owners, evidence, tests, frequencies, and exception handling. Use for governance operationalization; do not claim certification or legal compliance from a mapping alone.
metadata:
  version: "1.0.0"
  distribution: embedded
---

# Policy To Controls Mapper

## Purpose

Turn aspirational policy language into testable, owned operational requirements.

## Required inputs

- authoritative policy text and scope
- systems, processes, roles, and risk context
- target framework or assurance objective if applicable

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Operating modes and local resources

- For substantive work, read [the operational playbook](references/playbook.md) before choosing tests, thresholds, or a decision.
- Use [the report template](assets/report-template.md) when a durable deliverable is requested. Preserve its evidence register and acceptance review even if the presentation format changes.
- Use [the example request](examples/request.md), [decision excerpt](examples/expected-output.md), and [validated worked report](examples/example-report.md) to calibrate scope and decisiveness, never as evidence for the current task.
- For a narrow question, apply only the relevant workflow steps and state which completion gates are outside scope.

## Evidence discipline

- Give material evidence stable identifiers and cite those identifiers in findings.
- Separate observed facts, interpretations, unknowns, and recommendations.
- Record the target version, environment, collection time, and tool or method when freshness or reproducibility matters.
- Never upgrade missing evidence into a passing result. Mark it blocked and name what would resolve it.

## Workflow

1. Decompose each normative statement into actor, required behavior, object, condition, and timing.
2. Resolve ambiguous terms with policy owners rather than inventing thresholds.
3. Map each requirement to preventive, detective, or corrective controls and responsible owners.
4. Define evidence artifacts, sampling, test procedure, frequency, and pass criteria.
5. Identify unmapped requirements, duplicate controls, conflicts, exceptions, and inherited dependencies.
6. Produce traceability from policy clause through control, evidence, test, result, and remediation.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- policy-to-control traceability matrix
- control and evidence specifications
- gap and ambiguity register
- testing and exception plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not represent a control design as operating effectiveness.
- Do not provide legal conclusions beyond sourced requirements.
- Preserve exact policy language alongside interpretations.
