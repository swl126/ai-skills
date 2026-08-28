# Policy-control traceability matrix — worked example

## Decision summary

- **Decision:** GAP: certification exists, but prompt removal has no event-driven control or measurable deadline.
- **Scope and artifact identity:** EXAMPLE-policy-to-controls-mapper-v1
- **Evidence cutoff:** 2026-08-28
- **Decision owner:** Example review authority
- **Confidence:** Medium; bounded to the supplied fixture

## Evidence register

| Evidence ID | Source and version | Observation | Integrity or freshness | Limitation |
| --- | --- | --- | --- | --- |
| E-1 | Sanitized scenario fixture v1 | Operationalize quarterly access review and prompt removal after role changes. | Frozen example input | Does not represent a live system |
| E-2 | Acceptance policy v1 | The decisive condition has a predeclared threshold | Versioned example policy | Simplified for demonstration |

## Domain analysis

E-1 establishes the bounded target and observed condition. E-2 supplies the decision rule. The analysis does not extrapolate beyond this fixture and does not claim independent production validation.

## Findings and decisions

| ID | Finding | Severity | Evidence | Action | Owner | Due or expiry |
| --- | --- | --- | --- | --- | --- | --- |
| F-1 | GAP: certification exists, but prompt removal has no event-driven control or measurable deadline. | medium | E-1, E-2 | Resolve the named condition and rerun the same acceptance check | Example owner | Before promotion |

## Acceptance review

- **PASS** — scope, target identity, and decision authority are explicit.
- **PASS** — material observations cite E-1 and the decision rule cites E-2.
- **PASS** — inference and fixture limitations remain visible.
- **PASS** — the critical condition remains explicit in the decision.
- **NOT APPLICABLE** — no external mutation or live-system test occurs in this example.

## Residual risk and follow-up

This worked example proves package operation only. A real engagement must replace E-1 and E-2 with current authorized evidence, identify accountable owners, and rerun the local validator.
