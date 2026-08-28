---
name: model-evaluation-harness
description: Design and run repeatable evaluations for AI systems using representative cases, explicit rubrics, baselines, graders, failure taxonomies, and regression gates. Use when comparing models, prompts, agents, or releases; do not use for informal one-off opinions.
metadata:
  version: "1.0.0"
  distribution: embedded
---

# Model Evaluation Harness

## Purpose

Produce decision-grade evidence about whether an AI system meets defined behavioral requirements.

## Required inputs

- the system or outputs being evaluated
- target users and high-value tasks
- known risks and an acceptable failure threshold

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

1. Translate product claims into observable behaviors and counterexamples.
2. Construct a balanced case set covering normal, boundary, adversarial, and abstention behavior; prevent test contamination.
3. Define rubric dimensions, scoring anchors, critical failures, and aggregation rules before scoring.
4. Choose deterministic checks where possible and calibrated human or model graders where judgment is necessary.
5. Run a baseline and candidate under the same conditions; retain raw outputs, grader rationale, and configuration.
6. Report confidence limits, disagreement, failure clusters, and release recommendation without hiding critical failures in averages.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- versioned evaluation specification and case set
- raw and summarized results
- failure taxonomy and regression thresholds
- ship, block, or investigate recommendation

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not claim statistical significance without a justified design.
- Do not use sensitive production data without authorization and minimization.
- Treat model graders as measurement instruments requiring calibration, not ground truth.
