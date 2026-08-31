# Proposed Skill Record

These 21 concepts were approved as the development backlog and are now built as embedded executable skill packages under [skills/](skills/README.md). This document preserves their priority and intended capability. Embedded installation and repository testing do not imply independent release validation.

| Priority | Skill identifier | Category | Intended capability | Original status |
| ---: | --- | --- | --- | --- |
| 1 | `model-evaluation-harness` | AI assurance | Build repeatable evaluations with test cases, rubrics, baselines, graders, failure taxonomies, and regression thresholds. | Proposed |
| 2 | `prompt-injection-tester` | AI security | Test agents and retrieval systems against hostile instructions, data exfiltration, and tool manipulation. | Proposed |
| 3 | `agent-permission-auditor` | AI security | Evaluate agent tools, credentials, write access, approvals, and least-privilege boundaries. | Proposed |
| 4 | `api-contract-auditor` | Software engineering | Check OpenAPI contracts, implementations, examples, errors, versioning, and backward compatibility. | Proposed |
| 5 | `row-level-security-auditor` | Data security | Inspect RLS policies for cross-tenant exposure, privilege escalation, missing coverage, and unsafe defaults. | Proposed |
| 6 | `database-migration-guardian` | Data engineering | Plan and validate reversible migrations, backfills, compatibility windows, and rollback procedures. | Proposed |
| 7 | `secrets-hygiene-auditor` | Security engineering | Detect exposed credentials, unsafe examples, excessive scope, and weak rotation practices. | Proposed |
| 8 | `dependency-risk-auditor` | Supply-chain security | Evaluate vulnerabilities, abandonment, licensing conflicts, malicious-package risk, and upgrade exposure. | Proposed |
| 9 | `sbom-builder` | Supply-chain security | Produce and validate software bills of materials with provenance and dependency relationships. | Proposed |
| 10 | `configuration-drift-detector` | Platform engineering | Identify undocumented differences across infrastructure, application, and security configurations. | Proposed |
| 11 | `incident-postmortem-builder` | Reliability | Convert evidence and timelines into blameless, actionable incident reports. | Proposed |
| 12 | `disaster-recovery-exercise` | Resilience | Design and evaluate exercises for outages, ransomware, dependency failures, and regional disruptions. | Proposed |
| 13 | `observability-designer` | Reliability | Define useful logs, metrics, traces, dashboards, service indicators, and alerts. | Proposed |
| 14 | `release-readiness-gate` | Delivery assurance | Evaluate tests, migrations, security, documentation, rollback readiness, and release evidence. | Proposed |
| 15 | `architecture-decision-recorder` | Architecture | Record context, alternatives, tradeoffs, consequences, and reversal criteria for technical decisions. | Proposed |
| 16 | `policy-to-controls-mapper` | Governance | Convert policy language into controls, owners, evidence, tests, and exception handling. | Proposed |
| 17 | `privacy-impact-assessor` | Privacy engineering | Map personal-data flows, purposes, retention, sharing, user rights, and privacy risks. | Proposed |
| 18 | `dataset-documenter` | Data governance | Generate dataset cards describing provenance, population, collection, limitations, intended use, and bias. | Proposed |
| 19 | `synthetic-data-validator` | Data assurance | Evaluate utility, leakage, duplication, bias, and re-identification risk in synthetic datasets. | Proposed |
| 20 | `reproducible-research-packager` | Research engineering | Package data, code, environments, parameters, provenance, checksums, and reconstruction instructions. | Proposed |
| 21 | `writing-composition-engine` | Writing | Compose and audit evidence-traceable academic, technical, policy, proposal, and executive writing. | Proposed |

## Promotion path

Each proposal advances through:

```text
proposed → repository created → candidate → repaired/tested → validated → cataloged
```

No proposal enters `catalog.json` until its public repository passes [STANDARD.md](STANDARD.md).
