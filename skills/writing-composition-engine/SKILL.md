---
name: writing-composition-engine
description: Compose and audit evidence-traceable Markdown for academic, technical, policy, proposal, and executive writing using explicit audiences, purposes, sections, claims, and source identifiers. Use for substantive structured writing; do not invent evidence or treat structural checks as factual verification.
metadata:
  version: "1.0.0"
  distribution: embedded
---

# Writing Composition Engine

## Purpose

Produce coherent, audience-aware writing whose claims, evidence, structure, and remaining uncertainty can be inspected.

## Required inputs

- audience, purpose, genre, length, tone, and decision or learning objective
- source material and stable evidence identifiers when factual claims require support
- required sections, formatting rules, and prohibited content

If evidence or a decisive requirement is missing, preserve the gap instead of fabricating prose.

## Operating modes and local resources

- Read [the composition playbook](references/playbook.md) for genre selection, argument design, revision, and evidence handling.
- Use [the report template](assets/report-template.md) for a durable composition review.
- Use the [example request](examples/request.md), [expected output](examples/expected-output.md), and [worked report](examples/example-report.md) only for calibration.
- Use [the executable contract](references/executable-contract.md) before running the deterministic composer or auditor.

## Executable engine

- Compose Markdown from a strict brief with `python3 scripts/compose.py compose --brief BRIEF.json --out DRAFT.md --audit AUDIT.json`.
- Audit an existing Markdown draft with `python3 scripts/compose.py audit --input DRAFT.md --out AUDIT.json --fail-on-block`.
- The engine validates structure, source references, placeholders, repetition, and paragraph length. It does not verify that a source is genuine or that a factual claim is true.

## Evidence discipline

- Give every supplied source a stable identifier.
- Attach evidence identifiers to material factual claims.
- Separate sourced fact, interpretation, recommendation, and uncertainty.
- Preserve quotations exactly and never create a citation for an unavailable source.

## Workflow

1. Define audience, purpose, genre, required outcome, and constraints.
2. Inventory supplied evidence and identify unsupported claims or missing sources.
3. Build a section-level argument in which each section advances the purpose.
4. Draft paragraphs with one controlling idea and explicit evidence relationships.
5. Revise for coherence, transitions, redundancy, tone, and proportional emphasis.
6. Run the executable audit and resolve blocking structural or citation findings.
7. Deliver the composition with limitations and unresolved evidence clearly marked.

## Completion gates

- The opening establishes purpose, audience relevance, and scope.
- Section order reflects the argument rather than the order sources were received.
- Material claims resolve to supplied evidence or are explicitly qualified.
- No unfinished marker or unresolved citation survives.
- The conclusion answers the stated purpose without introducing unsupported claims.
- Required format and length constraints are satisfied.

## Output contract

- completed composition
- source and claim traceability
- machine-readable audit
- unresolved evidence or editorial decisions

## Safety and authority

- Do not fabricate sources, quotations, findings, credentials, or lived experience.
- Do not conceal uncertainty or transform allegations into established facts.
- Preserve confidential, legally privileged, personal, and controlled information boundaries.
- Structural passage does not certify factual, legal, academic, or policy correctness.
