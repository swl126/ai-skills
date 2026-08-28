---
name: configuration-drift-detector
description: Compare infrastructure, application, and security configurations across environments to identify undocumented or risky drift. Use for authorized environment reconciliation; do not overwrite differences until intent and ownership are resolved.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Configuration Drift Detector

## Purpose

Distinguish legitimate environment variance from accidental or unsafe divergence.

## Required inputs

- configuration snapshots or APIs
- declared baseline and environment roles
- approved exceptions and secret-handling rules

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Normalize representations while preserving semantically meaningful types and defaults.
2. Redact secret values but compare presence, source, version, and scope metadata.
3. Classify differences as expected, approved exception, unexplained drift, or critical control failure.
4. Trace drift to change history, ownership, and downstream behavioral impact.
5. Recommend reconciliation direction based on the declared baseline rather than majority state.
6. Produce repeatable comparison rules and exception expiry dates.

## Output contract

- normalized drift report
- risk-ranked unexplained differences
- approved exception register
- reconciliation and prevention plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not expose secrets in diffs.
- Do not apply production changes without explicit authorization.
- Account for intentional environment-specific values before labeling drift.

