---
name: agent-permission-auditor
description: Audit an AI agent's tools, credentials, data access, approvals, and external-write authority against least privilege. Use when deploying or reviewing an agent with real capabilities; do not treat documentation alone as proof of enforcement.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Agent Permission Auditor

## Purpose

Expose authority that is unnecessary, ambiguous, unreviewed, or capable of compounding harm.

## Required inputs

- agent purpose and allowed outcomes
- tool and credential inventory
- permission, approval, and logging configuration

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Map every capability to the user outcome that justifies it.
2. Classify reads, reversible writes, consequential writes, destructive actions, credential use, and delegation.
3. Identify wildcard scopes, ambient credentials, cross-tenant access, approval gaps, and tool combinations that amplify authority.
4. Test enforcement with harmless denied and allowed cases where authorized.
5. Define least-privilege scopes, just-in-time access, approval points, rate limits, and revocation paths.
6. Produce residual-risk decisions and owners for accepted exceptions.

## Output contract

- permission and tool inventory
- purpose-to-permission matrix
- findings with exploit paths
- remediation and exception register

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Never exercise destructive permissions merely to prove they exist.
- Do not copy credential values into reports.
- Distinguish configured policy from observed enforcement.

