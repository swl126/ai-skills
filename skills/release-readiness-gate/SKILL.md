---
name: release-readiness-gate
description: Evaluate whether a software or AI release is safe to ship using tests, migrations, security findings, documentation, rollback, monitoring, and evidence. Use for explicit release decisions; do not convert unresolved critical risks into an averaged score.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Release Readiness Gate

## Purpose

Produce a defensible ship, conditional-ship, or block decision tied to evidence.

## Required inputs

- release scope and change set
- test, security, migration, and operational evidence
- risk tolerance and rollback requirements

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Define mandatory gates and critical blockers before reviewing results.
2. Trace each material change to tests, documentation, migration needs, monitoring, and rollback.
3. Review failed, flaky, skipped, or stale evidence rather than accepting headline pass rates.
4. Assess open vulnerabilities, data risks, compatibility, dependencies, and operational readiness.
5. Record exceptions with owner, justification, compensating controls, and expiry.
6. Issue the decision with exact blockers or conditions and a post-release verification window.

## Output contract

- release gate matrix
- unresolved risk and exception register
- ship or block decision
- rollback and post-release verification plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Never average away a critical safety or security failure.
- Do not treat absence of evidence as passing evidence.
- Require explicit authority for risk acceptance.

