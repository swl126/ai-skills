---
name: reproducible-research-packager
description: Package research data, code, environments, parameters, provenance, checksums, and execution instructions for independent reconstruction. Use when preparing a study artifact or computational appendix; do not redistribute restricted data or software.
metadata:
  version: "1.1.0"
  distribution: embedded
---

# Reproducible Research Packager

## Purpose

Enable another authorized analyst to reconstruct results and identify where judgment or unavailable inputs affect reproducibility.

## Required inputs

- analysis code, data, outputs, and environment
- method, parameters, seeds, and transformation history
- sharing, licensing, and confidentiality constraints

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

1. Define the exact claims and outputs the package must reconstruct.
2. Inventory inputs, code, dependencies, environments, parameters, seeds, and external services.
3. Separate redistributable artifacts from restricted inputs and provide lawful acquisition or substitution instructions.
4. Create ordered execution steps, checksums, expected intermediate outputs, and reconciliation checks.
5. Test reconstruction in a clean environment or document the precise untested dependency.
6. Record provenance, licenses, limitations, nondeterminism, and deviations from the reported analysis.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- structured research package
- environment and dependency lock information
- reconstruction guide and checksums
- provenance, restriction, and limitation report

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not package personal, confidential, proprietary, or licensed data without authority.
- Never fabricate unavailable inputs or successful reconstruction.
- Distinguish computational reproducibility from external scientific validity.
