---
name: policy-to-controls-mapper
description: Translate policy statements into implementable controls, owners, evidence, tests, frequencies, and exception handling. Use for governance operationalization; do not claim certification or legal compliance from a mapping alone.
metadata:
  version: "0.1.0"
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

## Workflow

1. Decompose each normative statement into actor, required behavior, object, condition, and timing.
2. Resolve ambiguous terms with policy owners rather than inventing thresholds.
3. Map each requirement to preventive, detective, or corrective controls and responsible owners.
4. Define evidence artifacts, sampling, test procedure, frequency, and pass criteria.
5. Identify unmapped requirements, duplicate controls, conflicts, exceptions, and inherited dependencies.
6. Produce traceability from policy clause through control, evidence, test, result, and remediation.

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

