---
name: agent-permission-auditor
description: Audit an AI agent's tools, credentials, data access, approvals, and external-write authority against least privilege. Use when deploying or reviewing an agent with real capabilities; do not treat documentation alone as proof of enforcement.
metadata:
  version: "1.0.0"
  distribution: embedded
---

# Agent Permission Auditor

## Purpose

Expose authority that is unnecessary, ambiguous, unreviewed, or capable of compounding harm.

## Required inputs

- agent purpose and allowed outcomes
- tool and credential inventory
- permission, approval, and logging configuration

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

1. Map every capability to the user outcome that justifies it.
2. Classify reads, reversible writes, consequential writes, destructive actions, credential use, and delegation.
3. Identify wildcard scopes, ambient credentials, cross-tenant access, approval gaps, and tool combinations that amplify authority.
4. Test enforcement with harmless denied and allowed cases where authorized.
5. Define least-privilege scopes, just-in-time access, approval points, rate limits, and revocation paths.
6. Produce residual-risk decisions and owners for accepted exceptions.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- permission and tool inventory
- purpose-to-permission matrix
- findings with exploit paths
- remediation and exception register

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Never exercise destructive permissions merely to prove they exist.
- Do not copy credential values into reports.
- Distinguish configured policy from observed enforcement.
