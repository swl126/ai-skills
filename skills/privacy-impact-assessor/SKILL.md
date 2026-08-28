---
name: privacy-impact-assessor
description: Assess personal-data flows, purposes, retention, sharing, user rights, and privacy risks for a system or change. Use for engineering and governance decisions; do not substitute the assessment for qualified legal approval.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Privacy Impact Assessor

## Purpose

Identify privacy risks early enough to change data collection, architecture, access, or retention.

## Required inputs

- system purpose and data-flow evidence
- data categories, subjects, jurisdictions, and recipients
- retention, security, and user-rights processes

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Map collection, derivation, storage, access, transfer, disclosure, and deletion by data category.
2. Test purpose necessity, proportionality, minimization, accuracy, and retention assumptions.
3. Identify sensitive data, children or vulnerable groups, automated decisions, cross-border transfers, and re-identification paths.
4. Assess notices, consent or other asserted basis, access controls, processor relationships, and rights handling.
5. Rank risks by likelihood, severity, scale, reversibility, and affected populations.
6. Recommend design changes, controls, owner decisions, and residual-risk escalation.

## Output contract

- data-flow and purpose inventory
- privacy risk register
- mitigation and decision log
- unresolved legal or governance questions

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Minimize personal data in assessment artifacts.
- Separate engineering findings from legal determinations.
- Escalate high-risk processing rather than normalizing it through documentation.

