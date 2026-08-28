---
name: secrets-hygiene-auditor
description: Audit repositories and operational practices for exposed credentials, unsafe examples, excessive token scope, weak rotation, and secret-handling gaps. Use for defensive review; do not print or redistribute discovered secret values.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Secrets Hygiene Auditor

## Purpose

Find and contain credential exposure while improving the lifecycle from creation through revocation.

## Required inputs

- authorized repositories or configurations
- secret stores and credential types
- rotation, logging, and incident procedures

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Inventory expected secret types, storage locations, scopes, owners, and consumers.
2. Scan authorized content and history using value-redacting evidence; distinguish live secrets from placeholders.
3. Assess scope, lifetime, environment separation, logging exposure, CI handling, and developer workflows.
4. For suspected live exposure, prioritize revocation and rotation over cosmetic removal.
5. Recommend secret-manager use, short-lived credentials, detection hooks, and exception handling.
6. Record verification that replacement credentials work and old credentials are revoked without retaining values.

## Output contract

- redacted finding register
- containment and rotation plan
- lifecycle-control assessment
- preventive control recommendations

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Never reproduce a secret in the report or tool output.
- Treat repository deletion as insufficient after exposure.
- Do not rotate or revoke credentials without the required authority.

