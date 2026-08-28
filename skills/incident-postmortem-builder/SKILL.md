---
name: incident-postmortem-builder
description: Create blameless, evidence-grounded incident postmortems from timelines, logs, decisions, impacts, and recovery actions. Use after service or security incidents; do not invent causality when evidence is incomplete.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Incident Postmortem Builder

## Purpose

Turn an incident into defensible learning and owned corrective action rather than a narrative of individual blame.

## Required inputs

- time-stamped evidence and impact data
- response actions and decisions
- system context and prior related incidents

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Build a normalized timeline separating observed facts, interpretations, and unknowns.
2. Define user, business, security, and operational impact with bounded estimates.
3. Trace contributing technical, process, detection, and organizational conditions without stopping at the triggering event.
4. Explain what worked, what delayed recovery, and where controls failed or were absent.
5. Create corrective actions tied to specific failure mechanisms, owners, evidence, and due dates.
6. Document unresolved questions and conditions that would change the conclusions.

## Output contract

- fact-based incident timeline
- impact and causal analysis
- corrective action register
- follow-up verification plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Remove credentials and unnecessary personal data.
- Avoid blame language and unsupported certainty.
- Coordinate disclosure of security details with remediation status.

