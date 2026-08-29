---
name: sbom-builder
description: Build and validate a software bill of materials with components, versions, suppliers, provenance, licenses, hashes, and dependency relationships. Use for release evidence or supply-chain review; do not invent unresolved component metadata.
metadata:
  version: "1.1.0"
  distribution: embedded
---

# Sbom Builder

## Purpose

Create a traceable inventory that downstream security and compliance processes can reproduce.

## Required inputs

- build manifests and lockfiles
- built artifacts or container images
- target SBOM format and scope

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

1. Define the shipped artifact boundary and included development or runtime components.
2. Extract components from authoritative build and package metadata; reconcile duplicates and aliases.
3. Record versions, package URLs, suppliers, licenses, hashes, and dependency edges where supported.
4. Mark unknowns explicitly and preserve generator version and timestamp.
5. Validate schema, internal references, root component, and correspondence with the actual artifact.
6. Report coverage limitations and emit the requested SPDX or CycloneDX representation.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

## Output contract

- machine-readable SBOM
- human coverage summary
- unresolved component register
- validation evidence

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not claim completeness when ecosystems or generated artifacts were not inspected.
- Avoid embedding credentials, internal URLs, or unnecessary personal data.
- Keep observed license metadata separate from legal conclusions.
