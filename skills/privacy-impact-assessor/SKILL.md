---
name: privacy-impact-assessor
description: Assess personal-data flows, purposes, retention, sharing, user rights, and privacy risks for a system or change. Use for engineering and governance decisions; do not substitute the assessment for qualified legal approval.
metadata:
  version: "1.0.0"
  distribution: embedded
---

# Privacy Impact Assessor

## Purpose

Identify privacy risks early enough to change data collection, architecture, access, or retention.

## Required inputs

- system purpose and data-flow evidence
- data categories, subjects, jurisdictions, and recipients
- retention, security, and user-rights processes

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

1. Map collection, derivation, storage, access, transfer, disclosure, and deletion by data category.
2. Test purpose necessity, proportionality, minimization, accuracy, and retention assumptions.
3. Identify sensitive data, children or vulnerable groups, automated decisions, cross-border transfers, and re-identification paths.
4. Assess notices, consent or other asserted basis, access controls, processor relationships, and rights handling.
5. Rank risks by likelihood, severity, scale, reversibility, and affected populations.
6. Recommend design changes, controls, owner decisions, and residual-risk escalation.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- data-flow and purpose inventory
- privacy risk register
- mitigation and decision log
- unresolved legal or governance questions

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Minimize personal data in assessment artifacts.
- Separate engineering findings from legal determinations.
- Escalate high-risk processing rather than normalizing it through documentation.
