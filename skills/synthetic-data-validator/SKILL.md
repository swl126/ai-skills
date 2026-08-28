---
name: synthetic-data-validator
description: Evaluate synthetic datasets for utility, leakage, duplication, bias, and re-identification risk against the intended use. Use before sharing or relying on synthetic data; do not treat synthetic generation as automatic anonymization.
metadata:
  version: "1.0.0"
  distribution: embedded
---

# Synthetic Data Validator

## Purpose

Determine whether synthetic data is useful enough for its purpose without reproducing unacceptable privacy or bias risks.

## Required inputs

- real reference data under authorized access
- synthetic dataset and generation method
- intended use and privacy/utility thresholds

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

1. Confirm schema, types, constraints, support, and row-level validity.
2. Compare marginal, joint, conditional, temporal, and rare-event behavior relevant to the intended use.
3. Test downstream task performance and calibration against held-out real data.
4. Check exact and near duplicates, membership signals, attribute inference, memorization, and outlier leakage.
5. Compare subgroup representation and error to detect amplified or hidden bias.
6. Report tradeoffs and approve, restrict, regenerate, or reject against predeclared thresholds.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- utility and fidelity report
- privacy attack results
- subgroup and bias analysis
- use decision with thresholds and limitations

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Keep real reference data in its authorized environment.
- Do not publish attack examples that reveal actual records.
- Do not call a dataset anonymous without a justified threat model and evidence.
