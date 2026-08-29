# Executable evaluation contract

Read this reference when constructing cases, collecting outputs, running deterministic scoring, or comparing a candidate with a baseline.

## Design boundary

The harness deliberately does **not** execute a model, shell command, remote agent, or tool call. The evaluated system must be run separately within its authorized environment. Export one JSONL output record per frozen case, then score those records locally. This boundary prevents an evaluation package from silently acquiring execution authority.

## Files

| File | Purpose | Schema |
| --- | --- | --- |
| Evaluation specification | Frozen identity and release thresholds | `schemas/evaluation-spec.schema.json` |
| Cases JSONL | Inputs, slices, criticality, weights, and checks | `schemas/evaluation-case.schema.json` |
| Outputs JSONL | One system result per case | `schemas/system-output.schema.json` |
| Scored JSON | Reproducible result with hashes and per-case evidence | `schemas/score-result.schema.json` |

JSONL means one complete JSON object per non-empty line. Case IDs and check IDs must be stable. Every case requires at least one check.

## Deterministic checks

| Check type | Required configuration | Observed value |
| --- | --- | --- |
| `exact` | `value`; optional `case_sensitive` | output text |
| `contains_all` | non-empty `values`; optional `case_sensitive` | output text |
| `contains_none` | non-empty `values`; optional `case_sensitive` | output text |
| `regex` | `pattern`; optional flags `i` and `m` | output text |
| `json_valid` | none | output value or parsed text |
| `json_fields` | non-empty `required` field names | top-level JSON object |
| `max_chars` | numeric `value` | rendered output length |
| `latency_ms_max` | numeric `value` | `latency_ms` |
| `cost_usd_max` | numeric `value` | `cost_usd` |
| `manual_score` | `min_score` from 0 to 1 | attributed score, grader, and rationale |

A case passes only when every check passes. Its numeric score is the weighted mean of check scores. Overall weighted pass rate uses case weights; a failed case receives no pass weight. Critical failures remain separate and cannot be hidden by an aggregate.

Manual grades are external measurements, not ground truth. The output record must identify the grader and include a rationale. Calibrate graders outside the harness and retain disagreement before aggregating adjudicated results.

## Commands

Validate the frozen design:

```bash
python3 scripts/eval_harness.py validate \
  --spec examples/fixtures/spec.json \
  --cases examples/fixtures/cases.jsonl
```

Score two systems independently:

```bash
python3 scripts/eval_harness.py score \
  --spec examples/fixtures/spec.json \
  --cases examples/fixtures/cases.jsonl \
  --outputs examples/fixtures/baseline.outputs.jsonl \
  --system-id baseline-v1 \
  --out baseline.score.json \
  --report baseline.report.md

python3 scripts/eval_harness.py score \
  --spec examples/fixtures/spec.json \
  --cases examples/fixtures/cases.jsonl \
  --outputs examples/fixtures/candidate.outputs.jsonl \
  --system-id candidate-v2 \
  --out candidate.score.json \
  --report candidate.report.md
```

Compare scored results:

```bash
python3 scripts/eval_harness.py compare \
  --spec examples/fixtures/spec.json \
  --baseline baseline.score.json \
  --candidate candidate.score.json \
  --out comparison.json \
  --report comparison.md \
  --fail-on-block
```

Use `--fail-on-block` when a `BLOCK` decision must fail CI. The harness writes the JSON and Markdown evidence before exiting with status 1. Without that flag, a valid completed analysis exits successfully even when its domain decision is `BLOCK`.

## Interpretation

- `PASS` means the supplied outputs satisfy the frozen thresholds. It does not establish universal model quality.
- `BLOCK` identifies threshold failures or excessive regressions. Do not rewrite thresholds after seeing the candidate.
- The Wilson interval describes uncertainty in the unweighted binary pass proportion; it does not correct an unrepresentative case set.
- Hashes bind results to canonicalized content. They help detect mismatch, but do not prove source authenticity.

## Collection requirements

Run baseline and candidate with the same cases, system boundary, tool availability, context construction, grader policy, and collection procedure unless the comparison explicitly studies one of those changes. Retain raw outputs even when the Markdown report is sufficient for readers.
