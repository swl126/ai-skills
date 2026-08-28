---
name: prompt-injection-tester
description: Assess AI agents and retrieval systems for prompt injection, instruction conflicts, data exfiltration, and unsafe tool manipulation. Use for authorized defensive testing of a defined system; do not provide operational abuse against third-party systems.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Prompt Injection Tester

## Purpose

Determine whether untrusted content can override authority boundaries or cause unauthorized disclosure or actions.

## Required inputs

- authorized target and test scope
- system/tool authority model
- protected data and prohibited actions

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Map trusted instructions, untrusted content channels, tools, secrets, and approval boundaries.
2. Create safe test cases for direct, indirect, encoded, multi-turn, and retrieved-content injection.
3. Use inert canaries and reversible test actions; never use real secrets or destructive payloads.
4. Record whether the system follows, refuses, asks approval, leaks canaries, or calls tools.
5. Trace successful bypasses to the confused authority or missing isolation control.
6. Recommend layered mitigations and regression cases, then retest within the original authorization.

## Output contract

- attack-surface map
- reproducible test matrix and evidence
- severity-ranked findings
- mitigations and regression suite

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Require explicit authorization and stop at the defined boundary.
- Use synthetic secrets and non-destructive targets.
- Do not publish unpatched exploit details or credentials.

