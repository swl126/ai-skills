# AI Skills by Skylar Lyons

[![Validate catalog](https://github.com/swl126/ai-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/swl126/ai-skills/actions/workflows/validate.yml)
[![Verify linked skills](https://github.com/swl126/ai-skills/actions/workflows/verify-linked-skills.yml/badge.svg)](https://github.com/swl126/ai-skills/actions/workflows/verify-linked-skills.yml)
[![License: GPL-3.0-or-later](https://img.shields.io/badge/License-GPL--3.0--or--later-blue.svg)](LICENSE)

A one-clone collection, catalog, and quality framework for reusable AI-agent skills.

The goal is not to collect prompt snippets. It is to publish operational skills that an unfamiliar AI can discover, ingest, execute, test, and audit. This repository uses a hybrid distribution model: 20 skills are embedded for immediate local ingestion, while independently released skills retain their own versioned repositories and are indexed here.

## Repository status

| Measure | Current state |
| --- | ---: |
| Validated skills | 2 |
| Embedded skills | 20 |
| Approved proposals | 20 |
| Public license | GPL-3.0-or-later |
| Catalog format | JSON with schema |
| Validation | Local tests, GitHub Actions, and remote integrity checks |
| Repository version | 5.0.0 |

## Quick start for AI ingestion

Install the repository root once to expose the `ai-skills-hub` router and every embedded child package beneath it.

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo swl126/ai-skills \
  --path . \
  --name ai-skills-hub

# Or clone for development and repository-wide validation.
git clone https://github.com/swl126/ai-skills.git
cd ai-skills

python3 scripts/validate_embedded_skills.py
```

Invoke `$ai-skills-hub` after installation. The root [`SKILL.md`](SKILL.md) selects the smallest relevant child set and loads only those instructions. Directory aliases do not change a skill's invocation name; the YAML frontmatter name is authoritative.

## Independently validated releases

| Skill | Version | Capability | Validation |
| --- | ---: | --- | --- |
| [ENDGAME](https://github.com/swl126/endgame) | 1.1.0 | High-rigor orchestration with acceptance gates, selective routing, testing, adversarial review, and proof of completion | [Workflow](https://github.com/swl126/endgame/actions) |
| [Universal Spreadsheet Engine](https://github.com/swl126/Spreadsheet_runner) | 1.0.0 | Deterministic spreadsheet inspection, transformation, and reusable Python or R recipe generation | [Workflow](https://github.com/swl126/Spreadsheet_runner/actions) |

These are the only repositories currently represented as independently validated releases. They are separate from the 20 fully built embedded version `1.x` skills below; embedded status means locally ingestible and repository-tested, not independently production-validated.

## Twenty embedded skills

All 20 approved concepts are implemented as self-contained executable packages under [`skills/`](skills/README.md). Five priority security packages are version `2.0.0` with real offline domain analyzers; the model evaluation harness has its specialized engine; the remaining fourteen version `1.1.0` packages are explicitly normalized-evidence assessment tools. Every manifest declares runtime, network, filesystem, external-write, and destructive-action boundaries.

| Embedded skill | Primary use |
| --- | --- |
| [`model-evaluation-harness`](skills/model-evaluation-harness/SKILL.md) | Repeatable model, prompt, and agent evaluation |
| [`prompt-injection-tester`](skills/prompt-injection-tester/SKILL.md) | Authorized prompt-injection and indirect-injection testing |
| [`agent-permission-auditor`](skills/agent-permission-auditor/SKILL.md) | Least-privilege review for agent tools and credentials |
| [`api-contract-auditor`](skills/api-contract-auditor/SKILL.md) | API implementation and contract consistency |
| [`row-level-security-auditor`](skills/row-level-security-auditor/SKILL.md) | Tenant-isolation and RLS policy review |
| [`database-migration-guardian`](skills/database-migration-guardian/SKILL.md) | Safe schema migration planning and verification |
| [`secrets-hygiene-auditor`](skills/secrets-hygiene-auditor/SKILL.md) | Secret exposure detection and remediation planning |
| [`dependency-risk-auditor`](skills/dependency-risk-auditor/SKILL.md) | Dependency vulnerability and maintenance risk |
| [`sbom-builder`](skills/sbom-builder/SKILL.md) | Reproducible software bill of materials generation |
| [`configuration-drift-detector`](skills/configuration-drift-detector/SKILL.md) | Declared-versus-observed configuration comparison |
| [`incident-postmortem-builder`](skills/incident-postmortem-builder/SKILL.md) | Evidence-based, blameless incident analysis |
| [`disaster-recovery-exercise`](skills/disaster-recovery-exercise/SKILL.md) | Recovery drills and restoration evidence |
| [`observability-designer`](skills/observability-designer/SKILL.md) | Signals, service objectives, dashboards, and alerts |
| [`release-readiness-gate`](skills/release-readiness-gate/SKILL.md) | Evidence-backed go/no-go release decisions |
| [`architecture-decision-recorder`](skills/architecture-decision-recorder/SKILL.md) | Durable architecture decision records |
| [`policy-to-controls-mapper`](skills/policy-to-controls-mapper/SKILL.md) | Policy requirement to technical-control traceability |
| [`privacy-impact-assessor`](skills/privacy-impact-assessor/SKILL.md) | Personal-data flow and privacy-risk assessment |
| [`dataset-documenter`](skills/dataset-documenter/SKILL.md) | Dataset provenance, limitations, and intended use |
| [`synthetic-data-validator`](skills/synthetic-data-validator/SKILL.md) | Utility, fidelity, and disclosure-risk testing |
| [`reproducible-research-packager`](skills/reproducible-research-packager/SKILL.md) | Reconstructable research artifacts and provenance |

### Executable engines

Every embedded package exposes a dependency-free CLI declared in `skill-package.json`. The specialized model engine evaluates model outputs. Five domain tools scan local secrets, generate CycloneDX SBOMs from common manifests, compare JSON OpenAPI contracts, join SBOM components to offline advisories, and inspect PostgreSQL RLS DDL. The other packages evaluate normalized user-supplied evidence and must not be mistaken for collectors.

Evidence artifacts can be integrity-bound and reverified:

```bash
python3 scripts/evidence_envelope.py create result.json \
  --target-id app --target-version 1.0.0 --environment test \
  --collector-id sbom-builder --collector-version 2.0.0 --method offline \
  --out result.envelope.json
python3 scripts/evidence_envelope.py verify result.envelope.json result.json
```

```bash
cd skills/model-evaluation-harness
python3 scripts/eval_harness.py validate \
  --spec examples/fixtures/spec.json \
  --cases examples/fixtures/cases.jsonl
python3 tests/test_eval_harness.py

cd ../release-readiness-gate
python3 scripts/assess.py validate --input examples/fixtures/pass.json
python3 scripts/assess.py assess --input examples/fixtures/pass.json --out result.json --report report.md
python3 tests/test_assess.py
```

## Find a skill

Clone this catalog and use the dependency-free command-line search:

```bash
git clone https://github.com/swl126/ai-skills.git
cd ai-skills

python3 scripts/skills.py
python3 scripts/skills.py spreadsheet
python3 scripts/skills.py --status validated --json
```

The released catalog is available as both [human-readable documentation](SKILLS.md) and machine-readable [`catalog.json`](catalog.json).

## Install a released skill

Clone the individual repository and keep its complete directory. `SKILL.md` is the canonical instruction entry point, but referenced scripts, tests, examples, and supporting material are part of the portable skill.

```bash
git clone https://github.com/swl126/endgame.git
cd endgame
python3 scripts/validate_skill.py
```

Or:

```bash
git clone https://github.com/swl126/Spreadsheet_runner.git
cd Spreadsheet_runner
python3 -m unittest discover -s tests -v
```

Installation locations and adapter metadata vary by agent platform. See the [compatibility matrix](COMPATIBILITY.md) before treating platform adaptation as native support.

## Maturity and lifecycle

```mermaid
flowchart LR
    P["Proposed"] --> E["Built embedded v1.x"]
    E --> T["Tested candidate"]
    T --> V["Independent validation"]
    V --> G["Cataloged release"]
```

Embedding makes a skill portable and usable from one clone. It does not automatically promote that skill into the independently validated release catalog. Promotion requires documented provenance, compatible licensing, operational instructions, deterministic validation, and a passing default-branch workflow.

## ENDGAME governance

Substantial changes and releases use the canonical [ENDGAME](https://github.com/swl126/endgame) discipline. The hub pins the governing version and source commit rather than duplicating the skill. See [ENDGAME.md](ENDGAME.md), the machine-readable [ENDGAME.json](ENDGAME.json) evidence ledger, and the [acceptance gates](endgame/ACCEPTANCE_GATES.md).

## Quality contract

Every embedded skill must include valid YAML frontmatter, discriminating trigger guidance, required inputs, an actionable workflow, a defined output contract, and explicit safety and authority boundaries. The manifest, directory set, proposal provenance, names, versions, and distribution metadata must reconcile under automated validation.

In addition, every independently validated skill repository must include:

- a root `SKILL.md` with valid YAML frontmatter;
- concrete trigger conditions and important exclusions;
- required inputs, workflow, output contract, and completion gates;
- relevant safety and authority boundaries;
- a root `README.md`, `LICENSE`, `VERSION`, and `CHANGELOG.md`;
- contribution and security guidance;
- deterministic validation through scripts or tests;
- validation automation for pushes and pull requests.

The normative requirements are in [STANDARD.md](STANDARD.md). A reusable starting point is available in [`templates/SKILL.template.md`](templates/SKILL.template.md).

## Validation and trust

Run the complete catalog checks locally:

```bash
python3 scripts/validate_catalog.py
python3 scripts/validate_embedded_skills.py
python3 scripts/test_embedded_skills.py
python3 -m unittest discover -s tests -v
python3 scripts/endgame_audit.py
python3 scripts/verify_remote.py
```

The checks establish that required files exist, metadata is internally consistent, declared versions match public repositories, licenses contain GNU GPL text, tests pass, and linked public files remain reachable.

Validation does **not** guarantee that every output an AI produces is correct or that every platform interprets instructions identically. Review [TRUST.md](TRUST.md) before granting an agent credentials, external-write authority, network access, or destructive capabilities.

Build the minimal deterministic installation artifact with:

```bash
python3 scripts/build_distribution.py --out dist/ai-skills-hub.zip
```

## Architecture

```mermaid
flowchart TD
    H["ai-skills repository"] --> E["20 embedded skills"]
    H --> C["Release catalog"]
    H --> Q["Quality and governance"]
    E --> A["One-clone AI ingestion"]
    C --> L["Linked validated releases"]
    Q --> CI["Automated validation"]
    CI --> A
```

The repository contains executable instructions for the embedded collection as well as discovery and governance metadata for independently released skills.

## Repository map

| Resource | Purpose |
| --- | --- |
| [`catalog.json`](catalog.json) | Released, validated skill records |
| [`proposals.json`](proposals.json) | Original approved design provenance for the embedded skills |
| [`embedded-skills.json`](embedded-skills.json) | Installed embedded skills and canonical ingestion paths |
| [`skills/`](skills/README.md) | Twenty locally ingestible skill packages |
| [SKILLS.md](SKILLS.md) | Human-readable released catalog |
| [PROPOSED_SKILLS.md](PROPOSED_SKILLS.md) | Original prioritized design record for the embedded collection |
| [STANDARD.md](STANDARD.md) | Normative repository and admission requirements |
| [TRUST.md](TRUST.md) | Validation scope and maturity model |
| [COMPATIBILITY.md](COMPATIBILITY.md) | Cross-platform portability boundaries |
| [ROADMAP.md](ROADMAP.md) | Ecosystem development phases |
| [CANDIDATES.md](CANDIDATES.md) | Privacy-conscious candidate admission process |
| [docs/QUICKSTART.md](docs/QUICKSTART.md) | Short operational guide |
| [ENDGAME.md](ENDGAME.md) | High-rigor repository governance profile |
| [ENDGAME.json](ENDGAME.json) | Pinned source, gates, version, and audit evidence |
| [CHANGELOG.md](CHANGELOG.md) | Versioned hub changes |

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), conform the proposed repository to [STANDARD.md](STANDARD.md), run the validation suite, and submit the supplied pull-request checklist. New skill proposals can use the structured GitHub issue template.

Private repository names, contents, and audit findings are not published through the candidate process. A private project must be intentionally made public before it can enter public catalog review.

## License

This repository, including its embedded skills, is licensed under [GNU GPL version 3 or any later version](LICENSE). Each independently linked repository carries its own compatible license file.
