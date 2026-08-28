---
name: disaster-recovery-exercise
description: Design and evaluate disaster-recovery tabletop or technical exercises for outages, ransomware, dependency failures, and regional disruptions. Use to test recovery capability; do not disrupt production without separately approved execution authority.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Disaster Recovery Exercise

## Purpose

Reveal whether recovery objectives, backups, dependencies, communications, and decision rights work under pressure.

## Required inputs

- critical services and business priorities
- RTO, RPO, dependencies, and recovery procedures
- exercise type, participants, and safety constraints

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Choose a credible scenario that stresses the stated recovery objectives and hidden dependencies.
2. Define exercise boundaries, injects, observable decisions, success criteria, and stop conditions.
3. Run a tabletop or isolated technical exercise without coaching participants toward the desired answer.
4. Record decisions, missing information, recovery timing, data-loss estimates, and coordination failures.
5. Compare observed capability with RTO, RPO, and business continuity requirements.
6. Produce prioritized improvements and a retest plan.

## Output contract

- exercise plan and inject schedule
- observation and decision log
- objective-versus-observed scorecard
- corrective action and retest plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Keep production-impacting actions out of scope unless explicitly authorized.
- Use synthetic ransomware and data-loss scenarios.
- Do not expose sensitive infrastructure details beyond the exercise audience.

