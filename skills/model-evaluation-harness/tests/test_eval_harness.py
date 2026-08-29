#!/usr/bin/env python3
"""Behavioral tests for the executable model evaluation harness."""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/eval_harness.py"
SPEC = importlib.util.spec_from_file_location("eval_harness", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def spec(minimum=0.5, critical=0, regression=0.0, slices=None):
    return {
        "schema_version": "1.0.0",
        "evaluation_id": "fixture-eval",
        "title": "Fixture evaluation",
        "thresholds": {
            "min_pass_rate": minimum,
            "max_critical_failures": critical,
            "max_regression_rate": regression,
        },
        "slice_thresholds": slices or {},
    }


def case(case_id="c1", checks=None, critical=False, slice_name="normal"):
    return {
        "id": case_id,
        "slice": slice_name,
        "critical": critical,
        "input": "fixture",
        "checks": checks or [{"id": "exact", "type": "exact", "value": "ok"}],
    }


def output(case_id="c1", value="ok", **extra):
    return {"case_id": case_id, "output": value, **extra}


class ContractTests(unittest.TestCase):
    def test_rejects_invalid_threshold(self):
        with self.assertRaisesRegex(MODULE.ContractError, "min_pass_rate"):
            MODULE.validate_spec(spec(minimum=1.1))

    def test_rejects_unknown_fields_instead_of_ignoring_typos(self):
        design = spec()
        design["threshholds"] = design["thresholds"]
        with self.assertRaisesRegex(MODULE.ContractError, "unknown fields"):
            MODULE.validate_spec(design)

    def test_rejects_duplicate_case_ids(self):
        with self.assertRaisesRegex(MODULE.ContractError, "duplicate case id"):
            MODULE.validate_cases([case(), case()])

    def test_rejects_invalid_regex_during_design_validation(self):
        with self.assertRaisesRegex(MODULE.ContractError, "invalid regex"):
            MODULE.validate_cases([case(checks=[{"id": "rx", "type": "regex", "pattern": "["}])])

    def test_rejects_missing_and_extra_outputs(self):
        cases = [case("c1"), case("c2")]
        with self.assertRaisesRegex(MODULE.ContractError, "missing outputs"):
            MODULE.validate_outputs([output("c1")], cases)
        with self.assertRaisesRegex(MODULE.ContractError, "unknown case"):
            MODULE.validate_outputs([output("c1"), output("c2"), output("c3")], cases)


class CheckTests(unittest.TestCase):
    def test_text_checks_honor_case_sensitivity(self):
        checks = [
            {"id": "all", "type": "contains_all", "values": ["ALPHA"], "case_sensitive": False},
            {"id": "none", "type": "contains_none", "values": ["secret"], "case_sensitive": False},
            {"id": "rx", "type": "regex", "pattern": "alpha.*beta", "flags": "i"},
        ]
        result = MODULE.score_evaluation(spec(minimum=1), [case(checks=checks)], [output(value="Alpha then beta")], "system")
        self.assertEqual("PASS", result["decision"])

    def test_json_and_metric_checks(self):
        checks = [
            {"id": "json", "type": "json_valid"},
            {"id": "fields", "type": "json_fields", "required": ["answer"]},
            {"id": "latency", "type": "latency_ms_max", "value": 100},
            {"id": "cost", "type": "cost_usd_max", "value": 0.01},
        ]
        result = MODULE.score_evaluation(
            spec(minimum=1), [case(checks=checks)],
            [output(value={"answer": 42}, latency_ms=99, cost_usd=0.009)], "system"
        )
        self.assertEqual("PASS", result["decision"])

    def test_manual_grade_requires_attribution_and_rationale(self):
        checks = [{"id": "quality", "type": "manual_score", "min_score": 0.8}]
        missing = MODULE.score_evaluation(spec(), [case(checks=checks)], [output()], "system")
        self.assertFalse(missing["case_results"][0]["passed"])
        graded = MODULE.score_evaluation(
            spec(minimum=1), [case(checks=checks)],
            [output(manual_scores={"quality": {"score": 0.9, "grader": "g1", "rationale": "Meets anchored rubric level four."}})],
            "system",
        )
        self.assertEqual("PASS", graded["decision"])

    def test_rejects_grade_for_unknown_check(self):
        with self.assertRaisesRegex(MODULE.ContractError, "unknown check ids"):
            MODULE.validate_outputs(
                [output(manual_scores={"stale-grade": {"score": 1, "grader": "g", "rationale": "stale"}})],
                [case()],
            )


class ScoringTests(unittest.TestCase):
    def test_critical_failure_blocks_high_average(self):
        cases = [case("safe", critical=True), case("normal")]
        outputs = [output("safe", "bad"), output("normal", "ok")]
        result = MODULE.score_evaluation(spec(minimum=0.5), cases, outputs, "system")
        self.assertEqual("BLOCK", result["decision"])
        self.assertEqual(1, result["summary"]["critical_failures"])

    def test_required_slice_cannot_disappear(self):
        result = MODULE.score_evaluation(spec(slices={"safety": 1.0}), [case()], [output()], "system")
        self.assertEqual("BLOCK", result["decision"])
        self.assertIn("required slice missing: safety", result["threshold_failures"])

    def test_wilson_interval_is_bounded_and_nontrivial(self):
        low, high = MODULE.wilson_interval(5, 10)
        self.assertGreater(low, 0)
        self.assertLess(high, 1)
        self.assertLess(low, 0.5)
        self.assertGreater(high, 0.5)

    def test_hashes_change_when_outputs_change(self):
        first = MODULE.score_evaluation(spec(), [case()], [output(value="ok")], "system")
        second = MODULE.score_evaluation(spec(), [case()], [output(value="different")], "system")
        self.assertNotEqual(first["outputs_sha256"], second["outputs_sha256"])


class ComparisonTests(unittest.TestCase):
    def test_regression_blocks_candidate(self):
        design = spec(minimum=0, critical=1, regression=0)
        cases = [case()]
        baseline = MODULE.score_evaluation(design, cases, [output(value="ok")], "base")
        candidate = MODULE.score_evaluation(design, cases, [output(value="bad")], "candidate")
        result = MODULE.compare_results(design, baseline, candidate)
        self.assertEqual("BLOCK", result["decision"])
        self.assertEqual(["c1"], result["regressions"])

    def test_comparison_rejects_different_case_sets(self):
        design = spec()
        baseline = MODULE.score_evaluation(design, [case("c1")], [output("c1")], "base")
        candidate = MODULE.score_evaluation(design, [case("c2")], [output("c2")], "candidate")
        with self.assertRaisesRegex(MODULE.ContractError, "cases_sha256"):
            MODULE.compare_results(design, baseline, candidate)

    def test_comparison_rejects_results_scored_under_another_spec(self):
        original = spec(minimum=0.5)
        relaxed = spec(minimum=0.0)
        baseline = MODULE.score_evaluation(original, [case()], [output()], "base")
        candidate = MODULE.score_evaluation(original, [case()], [output()], "candidate")
        with self.assertRaisesRegex(MODULE.ContractError, "specification hash"):
            MODULE.compare_results(relaxed, baseline, candidate)

    def test_comparison_rejects_tampered_summary(self):
        design = spec()
        baseline = MODULE.score_evaluation(design, [case()], [output()], "base")
        candidate = MODULE.score_evaluation(design, [case()], [output()], "candidate")
        candidate["summary"]["weighted_pass_rate"] = 0.123
        with self.assertRaisesRegex(MODULE.ContractError, "internally inconsistent"):
            MODULE.compare_results(design, baseline, candidate)


class FixtureIntegrationTests(unittest.TestCase):
    def test_cli_fixture_passes_baseline_and_blocks_candidate(self):
        fixtures = ROOT / "examples/fixtures"
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            baseline = target / "baseline.json"
            candidate = target / "candidate.json"
            comparison = target / "comparison.json"
            common = ["--spec", str(fixtures / "spec.json"), "--cases", str(fixtures / "cases.jsonl")]
            for system_id, source, destination in [
                ("baseline-v1", "baseline.outputs.jsonl", baseline),
                ("candidate-v2", "candidate.outputs.jsonl", candidate),
            ]:
                run = subprocess.run(
                    [sys.executable, str(MODULE_PATH), "score", *common, "--outputs", str(fixtures / source), "--system-id", system_id, "--out", str(destination)],
                    capture_output=True, text=True, check=False,
                )
                self.assertEqual(0, run.returncode, run.stderr)
            run = subprocess.run(
                [sys.executable, str(MODULE_PATH), "compare", "--spec", str(fixtures / "spec.json"), "--baseline", str(baseline), "--candidate", str(candidate), "--out", str(comparison)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(0, run.returncode, run.stderr)
            self.assertEqual("PASS", json.loads(baseline.read_text())["decision"])
            self.assertEqual("BLOCK", json.loads(candidate.read_text())["decision"])
            self.assertEqual("BLOCK", json.loads(comparison.read_text())["decision"])

    def test_fail_on_block_writes_evidence_then_exits_one(self):
        fixtures = ROOT / "examples/fixtures"
        with tempfile.TemporaryDirectory() as directory:
            result_path = Path(directory) / "candidate.json"
            run = subprocess.run(
                [sys.executable, str(MODULE_PATH), "score", "--spec", str(fixtures / "spec.json"), "--cases", str(fixtures / "cases.jsonl"), "--outputs", str(fixtures / "candidate.outputs.jsonl"), "--system-id", "candidate-v2", "--out", str(result_path), "--fail-on-block"],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(1, run.returncode)
            self.assertTrue(result_path.is_file())
            self.assertEqual("BLOCK", json.loads(result_path.read_text())["decision"])


if __name__ == "__main__":
    unittest.main()
