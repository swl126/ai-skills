---
name: disaster-recovery-exercise
description: Design and evaluate disaster-recovery tabletop or technical exercises for outages, ransomware, dependency failures, and regional disruptions. Use to test recovery capability; do not disrupt production without separately approved execution authority.
metadata:
  version: "1.0.0"
  distribution: embedded
---

# Disaster Recovery Exercise

## Purpose

Reveal whether recovery objectives, backups, dependencies, communications, and decision rights work under pressure.

## Required inputs

- critical services and business priorities
- RTO, RPO, dependencies, and recovery procedures
- exercise type, participants, and safety constraints

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

1. Choose a credible scenario that stresses the stated recovery objectives and hidden dependencies.
2. Define exercise boundaries, injects, observable decisions, success criteria, and stop conditions.
3. Run a tabletop or isolated technical exercise without coaching participants toward the desired answer.
4. Record decisions, missing information, recovery timing, data-loss estimates, and coordination failures.
5. Compare observed capability with RTO, RPO, and business continuity requirements.
6. Produce prioritized improvements and a retest plan.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- exercise plan and inject schedule
- observation and decision log
- objective-versus-observed scorecard
- corrective action and retest plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Keep production-impacting actions out of scope unless explicitly authorized.
- Use synthetic ransomware and data-loss scenarios.
- Do not expose sensitive infrastructure details beyond the exercise audience.
