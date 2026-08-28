# Recovery exercise report — worked example

## Decision summary

- **Decision:** FAIL: infrastructure met RTO, but missing identity keys delayed validated service by 95 minutes.
- **Scope and artifact identity:** EXAMPLE-disaster-recovery-exercise-v1
- **Evidence cutoff:** 2026-08-28
- **Decision owner:** Example review authority
- **Confidence:** Medium; bounded to the supplied fixture

## Evidence register

| Evidence ID | Source and version | Observation | Integrity or freshness | Limitation |
| --- | --- | --- | --- | --- |
| E-1 | Sanitized scenario fixture v1 | Exercise an isolated regional outage across identity, application, database, DNS, and communications. | Frozen example input | Does not represent a live system |
| E-2 | Acceptance policy v1 | The decisive condition has a predeclared threshold | Versioned example policy | Simplified for demonstration |

## Domain analysis

E-1 establishes the bounded target and observed condition. E-2 supplies the decision rule. The analysis does not extrapolate beyond this fixture and does not claim independent production validation.

## Findings and decisions

| ID | Finding | Severity | Evidence | Action | Owner | Due or expiry |
| --- | --- | --- | --- | --- | --- | --- |
| F-1 | FAIL: infrastructure met RTO, but missing identity keys delayed validated service by 95 minutes. | high | E-1, E-2 | Resolve the named condition and rerun the same acceptance check | Example owner | Before promotion |

## Acceptance review

- **PASS** — scope, target identity, and decision authority are explicit.
- **PASS** — material observations cite E-1 and the decision rule cites E-2.
- **PASS** — inference and fixture limitations remain visible.
- **PASS** — the critical condition remains explicit in the decision.
- **NOT APPLICABLE** — no external mutation or live-system test occurs in this example.

## Residual risk and follow-up

This worked example proves package operation only. A real engagement must replace E-1 and E-2 with current authorized evidence, identify accountable owners, and rerun the local validator.
