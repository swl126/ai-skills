---
name: dataset-documenter
description: Create dataset cards describing provenance, population, collection, transformations, exclusions, limitations, intended use, and known bias. Use when publishing or operationalizing a dataset; do not infer missing provenance or represent documentation as quality proof.
metadata:
  version: "1.1.0"
  distribution: embedded
---

# Dataset Documenter

## Purpose

Make a dataset's origin, fitness, limitations, and responsible-use boundaries visible to downstream users.

## Required inputs

- source and collection records
- schema, transformations, quality results, and population details
- intended uses, prohibited uses, and governance constraints

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

1. Identify dataset ownership, lineage, versions, licenses, consent or collection context, and update cadence.
2. Describe units of observation, population, sampling, coverage, exclusions, labels, and missingness.
3. Record transformations, joins, deduplication, imputation, filtering, and quality checks.
4. Analyze representation, measurement error, label uncertainty, temporal drift, leakage, and sensitive attributes.
5. Define suitable uses, unsuitable uses, access, retention, and monitoring expectations.
6. Mark unknowns and evidence gaps rather than filling them with plausible text.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- versioned dataset card
- lineage and transformation summary
- quality and bias limitations
- intended-use and governance boundaries

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not expose row-level personal or confidential data.
- Avoid unsupported fairness or representativeness claims.
- Preserve provenance and licensing uncertainty explicitly.
