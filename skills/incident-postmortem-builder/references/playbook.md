# Operational playbook

Read this reference when planning or executing a substantive **incident-postmortem-builder** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Timeline reconstruction: normalize logs, alerts, tickets, changes, communications, and decisions.
- Causal analysis: identify contributing conditions and control failures without collapsing to a single root cause.
- Corrective action: tie work to observed failure mechanisms and measurable completion evidence.

## Minimum evidence record

- Incident identifier, declared window, systems, responders, sources, timezone, and clock-offset assumptions.
- Timestamped events with source references, actor/system, observed fact, confidence, and competing interpretations.
- Impact measures, detection and recovery milestones, decisions, mitigations, validation, and unresolved questions.

## Decision rules

- Label facts, inference, and unknowns; do not silently resolve conflicting evidence.
- Distinguish trigger, contributing conditions, failed defenses, detection gaps, and recovery constraints.
- Blameless does not mean accountability-free: name system and process ownership without personal blame.
- Actions must change a failure mechanism, have an owner, due date, priority, and verification method.

## Common failure modes

- Stopping at operator error or a triggering deployment.
- Using the incident channel transcript as a reliable ordered timeline without normalization.
- Action items such as 'be more careful' or 'improve monitoring' with no testable completion.
- Publishing sensitive security details beyond the intended audience.

## Acceptance checklist

- [ ] Timeline sources and uncertainties are reviewable.
- [ ] Impact and key durations are calculated from cited events.
- [ ] Causal claims are supported or explicitly tentative.
- [ ] Each corrective action maps to a finding and completion test.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
