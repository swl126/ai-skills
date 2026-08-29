#!/usr/bin/env python3
"""Dependency-free validation, scoring, and comparison for AI evaluations."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0.0"
CHECK_TYPES = {
    "exact",
    "contains_all",
    "contains_none",
    "regex",
    "json_valid",
    "json_fields",
    "max_chars",
    "latency_ms_max",
    "cost_usd_max",
    "manual_score",
}


class ContractError(ValueError):
    """Raised when evaluation inputs violate the executable contract."""


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ContractError(f"cannot read JSON {path}: {exc}") from exc


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise ContractError(f"cannot read JSONL {path}: {exc}") from exc
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ContractError(f"invalid JSONL {path}:{number}: {exc.msg}") from exc
        if not isinstance(value, dict):
            raise ContractError(f"JSONL row must be an object at {path}:{number}")
        rows.append(value)
    if not rows:
        raise ContractError(f"JSONL file has no records: {path}")
    return rows


def canonical_hash(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{label} must be a non-empty string")
    return value


def require_number(value: Any, label: str, minimum: float | None = None, maximum: float | None = None) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ContractError(f"{label} must be a finite number")
    number = float(value)
    if minimum is not None and number < minimum:
        raise ContractError(f"{label} must be >= {minimum}")
    if maximum is not None and number > maximum:
        raise ContractError(f"{label} must be <= {maximum}")
    return number


def reject_unknown(value: dict[str, Any], allowed: set[str], label: str) -> None:
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise ContractError(f"{label} contains unknown fields: {', '.join(unknown)}")


def validate_spec(spec: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(spec, dict):
        raise ContractError("evaluation spec must be an object")
    reject_unknown(spec, {"$schema", "schema_version", "evaluation_id", "title", "description", "thresholds", "slice_thresholds", "metadata"}, "evaluation spec")
    if spec.get("schema_version") != SCHEMA_VERSION:
        raise ContractError(f"schema_version must be {SCHEMA_VERSION}")
    require_string(spec.get("evaluation_id"), "evaluation_id")
    require_string(spec.get("title"), "title")
    thresholds = spec.get("thresholds")
    if not isinstance(thresholds, dict):
        raise ContractError("thresholds must be an object")
    reject_unknown(thresholds, {"min_pass_rate", "max_critical_failures", "max_regression_rate"}, "thresholds")
    require_number(thresholds.get("min_pass_rate"), "thresholds.min_pass_rate", 0, 1)
    max_critical = thresholds.get("max_critical_failures")
    if isinstance(max_critical, bool) or not isinstance(max_critical, int) or max_critical < 0:
        raise ContractError("thresholds.max_critical_failures must be a non-negative integer")
    require_number(thresholds.get("max_regression_rate", 0), "thresholds.max_regression_rate", 0, 1)
    slice_thresholds = spec.get("slice_thresholds", {})
    if not isinstance(slice_thresholds, dict):
        raise ContractError("slice_thresholds must be an object")
    for name, threshold in slice_thresholds.items():
        require_string(name, "slice name")
        require_number(threshold, f"slice_thresholds.{name}", 0, 1)
    return spec


def validate_cases(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen_cases: set[str] = set()
    for index, case in enumerate(cases):
        prefix = f"cases[{index}]"
        reject_unknown(case, {"id", "slice", "critical", "weight", "input", "metadata", "checks"}, prefix)
        case_id = require_string(case.get("id"), f"{prefix}.id")
        if case_id in seen_cases:
            raise ContractError(f"duplicate case id: {case_id}")
        seen_cases.add(case_id)
        require_string(case.get("slice"), f"{prefix}.slice")
        if "input" not in case:
            raise ContractError(f"{prefix}.input is required")
        if "critical" in case and not isinstance(case["critical"], bool):
            raise ContractError(f"{prefix}.critical must be boolean")
        require_number(case.get("weight", 1), f"{prefix}.weight", minimum=0.000001)
        checks = case.get("checks")
        if not isinstance(checks, list) or not checks:
            raise ContractError(f"{prefix}.checks must be a non-empty array")
        seen_checks: set[str] = set()
        for check_index, check in enumerate(checks):
            if not isinstance(check, dict):
                raise ContractError(f"{prefix}.checks[{check_index}] must be an object")
            check_id = require_string(check.get("id"), f"{prefix}.checks[{check_index}].id")
            if check_id in seen_checks:
                raise ContractError(f"duplicate check id in {case_id}: {check_id}")
            seen_checks.add(check_id)
            kind = check.get("type")
            if kind not in CHECK_TYPES:
                raise ContractError(f"unsupported check type in {case_id}/{check_id}: {kind}")
            validate_check_contract(case_id, check)
    return cases


def validate_check_contract(case_id: str, check: dict[str, Any]) -> None:
    label = f"{case_id}/{check['id']}"
    kind = check["type"]
    common = {"id", "type", "weight", "case_sensitive"}
    type_fields = {
        "exact": {"value"},
        "contains_all": {"values"},
        "contains_none": {"values"},
        "regex": {"pattern", "flags"},
        "json_valid": set(),
        "json_fields": {"required"},
        "max_chars": {"value"},
        "latency_ms_max": {"value"},
        "cost_usd_max": {"value"},
        "manual_score": {"min_score"},
    }
    reject_unknown(check, common | type_fields[kind], label)
    if kind == "exact":
        if "value" not in check:
            raise ContractError(f"{label}: exact requires value")
    elif kind in {"contains_all", "contains_none"}:
        values = check.get("values")
        if not isinstance(values, list) or not values or not all(isinstance(item, str) for item in values):
            raise ContractError(f"{label}: {kind} requires a non-empty string array")
    elif kind == "regex":
        pattern = require_string(check.get("pattern"), f"{label}.pattern")
        try:
            re.compile(pattern, regex_flags(check.get("flags", "")))
        except re.error as exc:
            raise ContractError(f"{label}: invalid regex: {exc}") from exc
    elif kind == "json_fields":
        fields = check.get("required")
        if not isinstance(fields, list) or not fields or not all(isinstance(item, str) and item for item in fields):
            raise ContractError(f"{label}: json_fields requires a non-empty required array")
    elif kind in {"max_chars", "latency_ms_max", "cost_usd_max"}:
        require_number(check.get("value"), f"{label}.value", minimum=0)
    elif kind == "manual_score":
        require_number(check.get("min_score"), f"{label}.min_score", 0, 1)
    if "weight" in check:
        require_number(check["weight"], f"{label}.weight", minimum=0.000001)
    if "case_sensitive" in check and not isinstance(check["case_sensitive"], bool):
        raise ContractError(f"{label}.case_sensitive must be boolean")


def regex_flags(flags: str) -> int:
    if not isinstance(flags, str) or any(char not in "im" for char in flags):
        raise ContractError("regex flags may contain only i or m")
    value = 0
    if "i" in flags:
        value |= re.IGNORECASE
    if "m" in flags:
        value |= re.MULTILINE
    return value


def validate_outputs(outputs: list[dict[str, Any]], cases: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    case_ids = {case["id"] for case in cases}
    indexed: dict[str, dict[str, Any]] = {}
    for index, output in enumerate(outputs):
        reject_unknown(output, {"case_id", "output", "latency_ms", "cost_usd", "manual_scores", "metadata"}, f"outputs[{index}]")
        case_id = require_string(output.get("case_id"), f"outputs[{index}].case_id")
        if case_id in indexed:
            raise ContractError(f"duplicate output for case: {case_id}")
        if case_id not in case_ids:
            raise ContractError(f"output references unknown case: {case_id}")
        if "output" not in output:
            raise ContractError(f"output value missing for case: {case_id}")
        for metric in ("latency_ms", "cost_usd"):
            if metric in output:
                require_number(output[metric], f"{case_id}.{metric}", minimum=0)
        manual_scores = output.get("manual_scores", {})
        if not isinstance(manual_scores, dict):
            raise ContractError(f"{case_id}.manual_scores must be an object")
        case = next(item for item in cases if item["id"] == case_id)
        manual_ids = {check["id"] for check in case["checks"] if check["type"] == "manual_score"}
        unknown_grades = sorted(set(manual_scores) - manual_ids)
        if unknown_grades:
            raise ContractError(f"{case_id}.manual_scores contains unknown check ids: {', '.join(unknown_grades)}")
        indexed[case_id] = output
    missing = sorted(case_ids - set(indexed))
    if missing:
        raise ContractError(f"missing outputs for cases: {', '.join(missing)}")
    return indexed


def output_text(value: Any) -> str:
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def normalize_text(value: str, case_sensitive: bool) -> str:
    return value if case_sensitive else value.casefold()


def run_check(check: dict[str, Any], output: dict[str, Any]) -> dict[str, Any]:
    kind = check["type"]
    text = output_text(output["output"])
    case_sensitive = check.get("case_sensitive", True)
    actual = normalize_text(text, case_sensitive)
    passed = False
    score = 0.0
    detail = ""
    if kind == "exact":
        expected = output_text(check["value"])
        passed = actual == normalize_text(expected, case_sensitive)
        detail = "exact output matched" if passed else "exact output differed"
    elif kind == "contains_all":
        missing = [item for item in check["values"] if normalize_text(item, case_sensitive) not in actual]
        passed = not missing
        detail = "all required values present" if passed else f"missing values: {missing}"
    elif kind == "contains_none":
        present = [item for item in check["values"] if normalize_text(item, case_sensitive) in actual]
        passed = not present
        detail = "forbidden values absent" if passed else f"forbidden values present: {present}"
    elif kind == "regex":
        passed = re.search(check["pattern"], text, regex_flags(check.get("flags", ""))) is not None
        detail = "regex matched" if passed else "regex did not match"
    elif kind == "json_valid":
        try:
            json.loads(text) if isinstance(output["output"], str) else output["output"]
            passed = True
            detail = "valid JSON"
        except json.JSONDecodeError:
            detail = "invalid JSON"
    elif kind == "json_fields":
        try:
            value = json.loads(text) if isinstance(output["output"], str) else output["output"]
            if not isinstance(value, dict):
                detail = "JSON output is not an object"
            else:
                missing = [field for field in check["required"] if field not in value]
                passed = not missing
                detail = "required fields present" if passed else f"missing fields: {missing}"
        except json.JSONDecodeError:
            detail = "invalid JSON"
    elif kind == "max_chars":
        passed = len(text) <= check["value"]
        detail = f"characters={len(text)}, maximum={check['value']}"
    elif kind == "latency_ms_max":
        value = output.get("latency_ms")
        passed = isinstance(value, (int, float)) and not isinstance(value, bool) and value <= check["value"]
        detail = f"latency_ms={value}, maximum={check['value']}"
    elif kind == "cost_usd_max":
        value = output.get("cost_usd")
        passed = isinstance(value, (int, float)) and not isinstance(value, bool) and value <= check["value"]
        detail = f"cost_usd={value}, maximum={check['value']}"
    elif kind == "manual_score":
        grade = output.get("manual_scores", {}).get(check["id"])
        if not isinstance(grade, dict):
            detail = "manual grade missing"
        else:
            raw_score = grade.get("score")
            rationale = grade.get("rationale")
            grader = grade.get("grader")
            if isinstance(raw_score, bool) or not isinstance(raw_score, (int, float)) or not 0 <= raw_score <= 1:
                detail = "manual score must be between 0 and 1"
            elif not isinstance(rationale, str) or not rationale.strip() or not isinstance(grader, str) or not grader.strip():
                detail = "manual grade requires grader and rationale"
            else:
                score = float(raw_score)
                passed = score >= check["min_score"]
                detail = f"manual score={score}, minimum={check['min_score']}, grader={grader}"
    if kind != "manual_score":
        score = 1.0 if passed else 0.0
    return {"id": check["id"], "type": kind, "passed": passed, "score": score, "detail": detail}


def wilson_interval(passed: int, total: int, z: float = 1.959963984540054) -> list[float]:
    if total <= 0:
        return [0.0, 0.0]
    proportion = passed / total
    denominator = 1 + z * z / total
    center = (proportion + z * z / (2 * total)) / denominator
    margin = z * math.sqrt((proportion * (1 - proportion) + z * z / (4 * total)) / total) / denominator
    return [round(max(0.0, center - margin), 6), round(min(1.0, center + margin), 6)]


def aggregate(case_results: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(case_results)
    passed = sum(1 for result in case_results if result["passed"])
    weight = sum(result["weight"] for result in case_results)
    passed_weight = sum(result["weight"] for result in case_results if result["passed"])
    mean_score = sum(result["score"] * result["weight"] for result in case_results) / weight
    return {
        "total_cases": total,
        "passed_cases": passed,
        "failed_cases": total - passed,
        "pass_rate": round(passed / total, 6),
        "weighted_pass_rate": round(passed_weight / weight, 6),
        "weighted_mean_score": round(mean_score, 6),
        "pass_rate_wilson_95": wilson_interval(passed, total),
        "critical_failures": sum(1 for result in case_results if result["critical"] and not result["passed"]),
    }


def calculate_slices(case_results: list[dict[str, Any]]) -> dict[str, Any]:
    slices: dict[str, Any] = {}
    for name in sorted({result["slice"] for result in case_results}):
        slices[name] = aggregate([result for result in case_results if result["slice"] == name])
    return slices


def calculate_threshold_failures(spec: dict[str, Any], summary: dict[str, Any], slices: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    thresholds = spec["thresholds"]
    if summary["weighted_pass_rate"] < thresholds["min_pass_rate"]:
        failures.append("overall weighted pass rate below minimum")
    if summary["critical_failures"] > thresholds["max_critical_failures"]:
        failures.append("critical failures exceed maximum")
    for name, minimum in spec.get("slice_thresholds", {}).items():
        if name not in slices:
            failures.append(f"required slice missing: {name}")
        elif slices[name]["weighted_pass_rate"] < minimum:
            failures.append(f"slice below minimum: {name}")
    return failures


def score_evaluation(spec: dict[str, Any], cases: list[dict[str, Any]], outputs: list[dict[str, Any]], system_id: str) -> dict[str, Any]:
    validate_spec(spec)
    validate_cases(cases)
    indexed = validate_outputs(outputs, cases)
    require_string(system_id, "system_id")
    case_results: list[dict[str, Any]] = []
    for case in cases:
        output = indexed[case["id"]]
        checks = []
        for source in case["checks"]:
            check_result = run_check(source, output)
            check_result["weight"] = float(source.get("weight", 1))
            checks.append(check_result)
        check_weight = sum(float(check.get("weight", 1)) for check in case["checks"])
        score = sum(result["score"] * float(source.get("weight", 1)) for result, source in zip(checks, case["checks"])) / check_weight
        case_results.append({
            "id": case["id"],
            "slice": case["slice"],
            "critical": case.get("critical", False),
            "weight": float(case.get("weight", 1)),
            "passed": all(check["passed"] for check in checks),
            "score": round(score, 6),
            "checks": checks,
        })
    summary = aggregate(case_results)
    slices = calculate_slices(case_results)
    threshold_failures = calculate_threshold_failures(spec, summary, slices)
    decision = "PASS" if not threshold_failures else "BLOCK"
    return {
        "schema_version": SCHEMA_VERSION,
        "evaluation_id": spec["evaluation_id"],
        "system_id": system_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "spec_sha256": canonical_hash(spec),
        "cases_sha256": canonical_hash(cases),
        "outputs_sha256": canonical_hash(outputs),
        "decision": decision,
        "threshold_failures": threshold_failures,
        "summary": summary,
        "slices": slices,
        "case_results": case_results,
    }


def validate_score_result(result: dict[str, Any], label: str, spec: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(result, dict):
        raise ContractError(f"{label} score result must be an object")
    for field in ("evaluation_id", "system_id", "spec_sha256", "cases_sha256"):
        require_string(result.get(field), f"{label}.{field}")
    if result.get("decision") not in {"PASS", "BLOCK"}:
        raise ContractError(f"{label}.decision must be PASS or BLOCK")
    summary = result.get("summary")
    if not isinstance(summary, dict):
        raise ContractError(f"{label}.summary must be an object")
    for field in ("weighted_pass_rate", "weighted_mean_score"):
        require_number(summary.get(field), f"{label}.summary.{field}", 0, 1)
    cases = result.get("case_results")
    if not isinstance(cases, list) or not cases:
        raise ContractError(f"{label}.case_results must be a non-empty array")
    seen: set[str] = set()
    for index, case_result in enumerate(cases):
        if not isinstance(case_result, dict):
            raise ContractError(f"{label}.case_results[{index}] must be an object")
        case_id = require_string(case_result.get("id"), f"{label}.case_results[{index}].id")
        if case_id in seen:
            raise ContractError(f"{label} contains duplicate case result: {case_id}")
        seen.add(case_id)
        if not isinstance(case_result.get("passed"), bool):
            raise ContractError(f"{label}.{case_id}.passed must be boolean")
        require_string(case_result.get("slice"), f"{label}.{case_id}.slice")
        if not isinstance(case_result.get("critical"), bool):
            raise ContractError(f"{label}.{case_id}.critical must be boolean")
        require_number(case_result.get("weight"), f"{label}.{case_id}.weight", minimum=0.000001)
        checks = case_result.get("checks")
        if not isinstance(checks, list) or not checks:
            raise ContractError(f"{label}.{case_id}.checks must be a non-empty array")
        check_weight = 0.0
        weighted_score = 0.0
        for check_index, check in enumerate(checks):
            if not isinstance(check, dict) or not isinstance(check.get("passed"), bool):
                raise ContractError(f"{label}.{case_id}.checks[{check_index}] is invalid")
            score = require_number(check.get("score"), f"{label}.{case_id}.checks[{check_index}].score", 0, 1)
            weight = require_number(check.get("weight"), f"{label}.{case_id}.checks[{check_index}].weight", minimum=0.000001)
            check_weight += weight
            weighted_score += score * weight
        expected_pass = all(check["passed"] for check in checks)
        expected_score = round(weighted_score / check_weight, 6)
        if case_result["passed"] != expected_pass or case_result.get("score") != expected_score:
            raise ContractError(f"{label}.{case_id} case result is internally inconsistent")
    recalculated_summary = aggregate(cases)
    recalculated_slices = calculate_slices(cases)
    if result.get("summary") != recalculated_summary or result.get("slices") != recalculated_slices:
        raise ContractError(f"{label} aggregate summary or slices are internally inconsistent")
    expected_failures = calculate_threshold_failures(spec, recalculated_summary, recalculated_slices)
    expected_decision = "PASS" if not expected_failures else "BLOCK"
    if result.get("threshold_failures") != expected_failures or result.get("decision") != expected_decision:
        raise ContractError(f"{label} threshold decision is internally inconsistent")
    return result


def compare_results(spec: dict[str, Any], baseline: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    validate_spec(spec)
    validate_score_result(baseline, "baseline", spec)
    validate_score_result(candidate, "candidate", spec)
    expected_spec_hash = canonical_hash(spec)
    if baseline["evaluation_id"] != spec["evaluation_id"] or candidate["evaluation_id"] != spec["evaluation_id"]:
        raise ContractError("score results do not match the supplied evaluation_id")
    if baseline["spec_sha256"] != expected_spec_hash or candidate["spec_sha256"] != expected_spec_hash:
        raise ContractError("score results do not match the supplied specification hash")
    for field in ("evaluation_id", "spec_sha256", "cases_sha256"):
        if baseline.get(field) != candidate.get(field):
            raise ContractError(f"baseline and candidate differ on {field}")
    base_cases = {case["id"]: case for case in baseline.get("case_results", [])}
    cand_cases = {case["id"]: case for case in candidate.get("case_results", [])}
    if not base_cases or set(base_cases) != set(cand_cases):
        raise ContractError("baseline and candidate case sets differ")
    regressions = sorted(case_id for case_id in base_cases if base_cases[case_id]["passed"] and not cand_cases[case_id]["passed"])
    improvements = sorted(case_id for case_id in base_cases if not base_cases[case_id]["passed"] and cand_cases[case_id]["passed"])
    regression_rate = len(regressions) / len(base_cases)
    failures = list(candidate.get("threshold_failures", []))
    if regression_rate > spec["thresholds"].get("max_regression_rate", 0):
        failures.append("regression rate exceeds maximum")
    decision = "PASS" if candidate.get("decision") == "PASS" and not failures else "BLOCK"
    return {
        "schema_version": SCHEMA_VERSION,
        "evaluation_id": candidate["evaluation_id"],
        "baseline_system_id": baseline.get("system_id"),
        "candidate_system_id": candidate.get("system_id"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "decision": decision,
        "decision_failures": sorted(set(failures)),
        "weighted_pass_rate_delta": round(candidate["summary"]["weighted_pass_rate"] - baseline["summary"]["weighted_pass_rate"], 6),
        "weighted_mean_score_delta": round(candidate["summary"]["weighted_mean_score"] - baseline["summary"]["weighted_mean_score"], 6),
        "regression_rate": round(regression_rate, 6),
        "regressions": regressions,
        "improvements": improvements,
        "baseline_summary": baseline["summary"],
        "candidate_summary": candidate["summary"],
    }


def score_markdown(result: dict[str, Any]) -> str:
    summary = result["summary"]
    lines = [
        f"# Evaluation result: {result['evaluation_id']}", "",
        f"- **System:** {result['system_id']}",
        f"- **Decision:** {result['decision']}",
        f"- **Weighted pass rate:** {summary['weighted_pass_rate']:.3f}",
        f"- **Critical failures:** {summary['critical_failures']}",
        f"- **95% Wilson interval:** {summary['pass_rate_wilson_95'][0]:.3f}–{summary['pass_rate_wilson_95'][1]:.3f}", "",
        "## Slice results", "", "| Slice | Passed | Total | Weighted pass rate | Critical failures |", "| --- | ---: | ---: | ---: | ---: |",
    ]
    for name, value in result["slices"].items():
        lines.append(f"| {name} | {value['passed_cases']} | {value['total_cases']} | {value['weighted_pass_rate']:.3f} | {value['critical_failures']} |")
    lines.extend(["", "## Failed cases", ""])
    failed = [case for case in result["case_results"] if not case["passed"]]
    if not failed:
        lines.append("None.")
    for case in failed:
        details = "; ".join(check["detail"] for check in case["checks"] if not check["passed"])
        lines.append(f"- **{case['id']}** ({case['slice']}, critical={str(case['critical']).lower()}): {details}")
    lines.extend(["", "## Threshold failures", ""])
    lines.extend(f"- {item}" for item in result["threshold_failures"] or ["None."])
    return "\n".join(lines) + "\n"


def comparison_markdown(result: dict[str, Any]) -> str:
    return "\n".join([
        f"# Evaluation comparison: {result['evaluation_id']}", "",
        f"- **Baseline:** {result['baseline_system_id']}",
        f"- **Candidate:** {result['candidate_system_id']}",
        f"- **Decision:** {result['decision']}",
        f"- **Weighted pass-rate delta:** {result['weighted_pass_rate_delta']:+.3f}",
        f"- **Regression rate:** {result['regression_rate']:.3f}", "",
        "## Regressions", "",
        *(f"- {item}" for item in result["regressions"]),
        *( ["None."] if not result["regressions"] else []), "",
        "## Improvements", "",
        *(f"- {item}" for item in result["improvements"]),
        *( ["None."] if not result["improvements"] else []), "",
        "## Decision failures", "",
        *(f"- {item}" for item in result["decision_failures"]),
        *( ["None."] if not result["decision_failures"] else []),
    ]) + "\n"


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate", help="validate a specification and case set")
    validate.add_argument("--spec", type=Path, required=True)
    validate.add_argument("--cases", type=Path, required=True)
    score = sub.add_parser("score", help="score one system's JSONL outputs")
    score.add_argument("--spec", type=Path, required=True)
    score.add_argument("--cases", type=Path, required=True)
    score.add_argument("--outputs", type=Path, required=True)
    score.add_argument("--system-id", required=True)
    score.add_argument("--out", type=Path, required=True)
    score.add_argument("--report", type=Path)
    score.add_argument("--fail-on-block", action="store_true", help="exit 1 after writing outputs when the decision is BLOCK")
    compare = sub.add_parser("compare", help="compare pre-scored baseline and candidate results")
    compare.add_argument("--spec", type=Path, required=True)
    compare.add_argument("--baseline", type=Path, required=True)
    compare.add_argument("--candidate", type=Path, required=True)
    compare.add_argument("--out", type=Path, required=True)
    compare.add_argument("--report", type=Path)
    compare.add_argument("--fail-on-block", action="store_true", help="exit 1 after writing outputs when the decision is BLOCK")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        spec = validate_spec(load_json(args.spec))
        if args.command == "validate":
            cases = validate_cases(load_jsonl(args.cases))
            print(f"Evaluation contract valid: {spec['evaluation_id']} ({len(cases)} cases)")
            return
        if args.command == "score":
            result = score_evaluation(spec, load_jsonl(args.cases), load_jsonl(args.outputs), args.system_id)
            write_json(args.out, result)
            if args.report:
                args.report.write_text(score_markdown(result), encoding="utf-8")
            print(f"{result['decision']}: {result['evaluation_id']} / {args.system_id}")
            if args.fail_on_block and result["decision"] == "BLOCK":
                raise SystemExit(1)
            return
        result = compare_results(spec, load_json(args.baseline), load_json(args.candidate))
        write_json(args.out, result)
        if args.report:
            args.report.write_text(comparison_markdown(result), encoding="utf-8")
        print(f"{result['decision']}: {result['evaluation_id']} comparison")
        if args.fail_on_block and result["decision"] == "BLOCK":
            raise SystemExit(1)
    except ContractError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
