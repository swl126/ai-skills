# AI Skill Repository Standard

Version 1.0

## Required files

| Path | Requirement |
| --- | --- |
| `SKILL.md` | Required agent instructions with YAML frontmatter |
| `README.md` | Human documentation, examples, installation, and limitations |
| `LICENSE` | GPL-3.0-or-later license text |
| `VERSION` | Semantic version in `MAJOR.MINOR.PATCH` form |
| `CHANGELOG.md` | User-visible changes by version |
| `CONTRIBUTING.md` | Contribution and validation instructions |
| `SECURITY.md` | Vulnerability-reporting guidance |
| `.github/workflows/validate.yml` | Automated validation on pushes and pull requests |

## `SKILL.md` contract

The file must start with YAML frontmatter containing non-empty `name` and `description` fields. Its body must define:

- when the skill applies;
- when it does not apply;
- the required inputs and relevant assumptions;
- the operational workflow;
- expected outputs;
- validation or completion gates;
- safety, authority, or destructive-action boundaries where relevant.

Instructions must be specific enough for an unfamiliar compatible agent to execute without relying on hidden conversation context.

## Recommended structure

```text
repository/
├── .github/workflows/validate.yml
├── agents/openai.yaml
├── examples/
├── references/
├── scripts/
├── tests/
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── SKILL.md
└── VERSION
```

Only directories actually needed by the skill should be included.

## Quality gates

A catalog entry may be marked `validated` only when:

1. required files exist;
2. frontmatter parses and contains required fields;
3. every local reference from `SKILL.md` resolves;
4. included scripts compile or execute successfully;
5. included tests pass;
6. README claims match executable behavior;
7. licensing is internally consistent;
8. the default-branch validation workflow succeeds.

## Portability

Platform-specific metadata belongs in optional adapter files such as `agents/openai.yaml`. The root `SKILL.md` remains the canonical, portable instruction source.

## Versioning

Use semantic versioning:

- patch: clarification or compatible fix;
- minor: compatible capability addition;
- major: incompatible behavior or contract change.
