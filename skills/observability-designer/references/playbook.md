# Operational playbook

Read this reference when planning or executing a substantive **observability-designer** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Greenfield design: derive telemetry from user outcomes and plausible failure modes.
- Gap assessment: compare existing signals with operator decisions and incident evidence.
- Alert tuning: evaluate actionability, sensitivity, noise, ownership, and runbook quality.

## Minimum evidence record

- Service boundaries, user journeys, dependencies, critical operations, owners, and reliability targets.
- Metric definitions, log schemas, trace propagation, label/cardinality rules, sampling, retention, and cost.
- Alert condition, evaluation window, severity, owner, notification route, runbook, and observed test behavior.

## Decision rules

- Define event semantics, units, and aggregation before implementation.
- Prefer user-impact symptoms and burn rates over infrastructure thresholds when possible.
- Include correlation IDs across service boundaries without leaking secrets or sensitive data.
- Every page must imply an immediate operator decision or action.

## Common failure modes

- Dashboards optimized for telemetry volume instead of diagnosis.
- High-cardinality labels such as user IDs added to metrics.
- Alerts with no owner, runbook, or actionable response.
- Averages that hide tail latency, partial failure, or subgroup impact.

## Acceptance checklist

- [ ] Critical user outcomes have SLIs and target interpretation.
- [ ] Named failure modes map to sufficient logs, metrics, and traces.
- [ ] Alerts have ownership, action, and tested routing.
- [ ] Privacy, retention, sampling, cardinality, and cost are addressed.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
