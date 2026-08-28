# Operational playbook

Read this reference when planning or executing a substantive **prompt-injection-tester** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Threat model: map trust boundaries, content channels, tools, data, and approval points.
- Controlled test: exercise direct, indirect, encoded, multi-turn, and retrieval-mediated cases with inert canaries.
- Regression: reduce confirmed bypasses into non-destructive repeatable cases.

## Minimum evidence record

- Written authorization, target boundary, excluded systems, rate limits, stop conditions, and test window.
- Instruction hierarchy, retrieval sources, tool schemas, approval logic, credential exposure paths, and logging behavior.
- Exact sanitized prompts, system responses, tool decisions, canary observations, and control configuration.

## Decision rules

- Use unique inert canaries; never use real credentials, personal data, or destructive payloads.
- Test whether an action occurred, not merely whether the model said it would occur.
- Stop on unexpected access, material instability, or impact outside the authorized target.
- Classify failures by violated trust boundary and confused authority, not clever wording alone.

## Common failure modes

- Testing a third-party target without explicit authorization.
- Treating a textual refusal as proof that tools or hidden data were protected.
- Publishing a reusable harmful payload when a sanitized reproduction is sufficient.
- Fixing one string pattern while leaving the authority boundary unchanged.

## Acceptance checklist

- [ ] Scope and authorization are recorded.
- [ ] Every test has an expected safe behavior and observable pass criterion.
- [ ] Evidence is redacted and replayable in the authorized environment.
- [ ] Mitigations address instruction/data/tool separation and have regression cases.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
