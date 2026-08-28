---
name: observability-designer
description: Design logs, metrics, traces, dashboards, service-level indicators, and alerts around real failure modes and user impact. Use when establishing or repairing observability; do not optimize for telemetry volume without decision value.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Observability Designer

## Purpose

Ensure operators can detect, explain, and act on meaningful system degradation.

## Required inputs

- service architecture and critical journeys
- failure modes and operational decisions
- telemetry platform, cost, privacy, and retention constraints

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Identify user-visible outcomes, dependencies, and decisions operators must make.
2. Define SLIs and event semantics before dashboards; specify units, labels, cardinality, and ownership.
3. Map logs, metrics, and traces to failure hypotheses and correlation identifiers.
4. Design alerts around actionable symptoms, burn rates, or safety boundaries rather than raw noise.
5. Check privacy, secret leakage, retention, cost, sampling, and high-cardinality risks.
6. Validate with known failure scenarios and document runbook links and expected operator actions.

## Output contract

- telemetry specification
- SLI/SLO and alert definitions
- dashboard and runbook design
- coverage, cost, and privacy analysis

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not log secrets or unnecessary personal data.
- Prevent unbounded labels and telemetry cost explosions.
- Every page-level alert must have an owner and actionable response.

