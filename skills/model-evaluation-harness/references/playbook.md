# Operational playbook

Read this reference when planning or executing a substantive **model-evaluation-harness** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Specification: turn product claims and risks into measurable behaviors before collecting results.
- Comparison: run a baseline and candidate against the same frozen cases and settings.
- Regression: convert confirmed failures into stable release gates without leaking the hidden set.

## Minimum evidence record

- System identifier, model and prompt versions, tool configuration, decoding settings, and evaluation timestamp.
- Case provenance and split; expected behavior; rubric anchors; critical-failure rules; grader identity and calibration.
- Raw outputs, deterministic check results, grader rationale, disagreements, reruns, exclusions, and aggregation formula.

## Decision rules

- Freeze the rubric and critical-failure rule before inspecting candidate scores.
- Report per-slice results and absolute counts; never rely on a single aggregate score.
- Separate capability, reliability, safety, latency, and cost so tradeoffs remain visible.
- Use paired cases for comparisons and preserve seeds when the system supports them.

## Common failure modes

- Test-set contamination or cases copied from tuning data.
- Uncalibrated model-as-judge scores presented as objective truth.
- Small samples with confident generalization or significance claims.
- Critical safety failures hidden by a high mean score.

## Acceptance checklist

- [ ] Every claim maps to at least one case and scoring rule.
- [ ] Baseline and candidate were run under comparable conditions.
- [ ] Critical failures and grader disagreements are individually reviewable.
- [ ] The recommendation follows predeclared thresholds and lists uncertainty.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
