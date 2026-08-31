---
name: ai-skills-hub
description: Route complex AI, software, security, reliability, governance, privacy, data, and research work to one of twenty self-contained executable skills bundled in this repository. Use when the user invokes the hub or when a bundled specialist clearly matches; do not load every child skill.
metadata:
  version: "5.0.0"
  distribution: hub
---

# AI Skills Hub

This is the installable root router for the twenty skills indexed by [embedded-skills.json](embedded-skills.json). Select the smallest relevant set, then read each selected child `SKILL.md` completely before acting. Resolve all child paths relative to this file so the installed hub remains self-contained.

## Routing

- AI assurance: [model evaluation](skills/model-evaluation-harness/SKILL.md), [prompt injection](skills/prompt-injection-tester/SKILL.md), [agent permissions](skills/agent-permission-auditor/SKILL.md).
- Application and data security: [API contracts](skills/api-contract-auditor/SKILL.md), [row-level security](skills/row-level-security-auditor/SKILL.md), [secrets hygiene](skills/secrets-hygiene-auditor/SKILL.md).
- Delivery and platform engineering: [database migrations](skills/database-migration-guardian/SKILL.md), [dependency risk](skills/dependency-risk-auditor/SKILL.md), [SBOMs](skills/sbom-builder/SKILL.md), [configuration drift](skills/configuration-drift-detector/SKILL.md), [release readiness](skills/release-readiness-gate/SKILL.md).
- Reliability: [incident postmortems](skills/incident-postmortem-builder/SKILL.md), [disaster recovery](skills/disaster-recovery-exercise/SKILL.md), [observability](skills/observability-designer/SKILL.md).
- Architecture and governance: [architecture decisions](skills/architecture-decision-recorder/SKILL.md), [policy-control mapping](skills/policy-to-controls-mapper/SKILL.md), [privacy impact](skills/privacy-impact-assessor/SKILL.md).
- Data and research: [dataset documentation](skills/dataset-documenter/SKILL.md), [synthetic-data validation](skills/synthetic-data-validator/SKILL.md), [reproducible research](skills/reproducible-research-packager/SKILL.md).

## Execution rules

1. Identify the requested outcome and choose only directly applicable child skills.
2. Read the selected child entrypoints and any references they explicitly route to.
3. Preserve each child skill's required inputs, authority boundary, evidence rules, and completion gates.
4. Use its declared executable from `skill-package.json` when structured evidence is available.
5. Validate generated reports or machine outputs with the package's declared tests or validators.
6. If multiple child skills apply, state their order and reconcile conflicting findings without averaging away critical failures.

The hub grants no external-write authority. Installation makes local instructions and engines available; consequential actions still require the user's authorization.
