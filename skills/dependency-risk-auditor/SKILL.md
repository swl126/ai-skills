---
name: dependency-risk-auditor
description: Evaluate software dependencies for vulnerabilities, abandonment, malicious-package risk, licensing conflicts, and upgrade exposure. Use for release, procurement, or maintenance decisions; do not equate a vulnerability count with actual exploitability.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Dependency Risk Auditor

## Purpose

Prioritize dependency risks using reachability, privilege, provenance, maintenance, and business impact.

## Required inputs

- lockfiles, manifests, and build graph
- runtime and deployment context
- license and risk policies

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Resolve direct and transitive dependencies from authoritative lock data.
2. Identify known vulnerabilities, suspicious provenance, name confusion, unmaintained packages, and version drift.
3. Assess runtime reachability, exposed attack paths, execution privilege, and available mitigations.
4. Check license obligations and conflicts against the distribution model.
5. Compare upgrade, replacement, isolation, patching, and acceptance options.
6. Produce a prioritized action plan with verification and expiry dates for exceptions.

## Output contract

- dependency inventory and risk register
- reachability-informed priorities
- license compatibility findings
- upgrade or replacement plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not execute unknown packages during inspection.
- Verify package identity and source before recommending upgrades.
- Separate known evidence from ecosystem reputation signals.

