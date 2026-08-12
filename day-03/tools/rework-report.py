#!/usr/bin/env python3
"""Calculate rework changes between two fixed-task agent runs."""

from __future__ import annotations

import json
import sys
from pathlib import Path


MEASURES = ("questions", "review_rounds", "defects", "changed_diff_lines")
RUNS = ("without_knowledge_base", "with_knowledge_base")


def validate(data: dict) -> list[str]:
    issues: list[str] = []
    for key in ("task_id", "spec_commit", "operators", *RUNS):
        if key not in data:
            issues.append(f"missing field: {key}")
    for key in ("same_task", "same_criteria", "same_reviewer"):
        if data.get(key) is not True:
            issues.append(f"{key} must be true")
    operators = data.get("operators", {})
    for run in RUNS:
        if not isinstance(operators.get(run), str) or not operators[run].strip():
            issues.append(f"operator is required for {run}")
        run_data = data.get(run, {})
        if not isinstance(run_data, dict):
            issues.append(f"run data must be an object: {run}")
            continue
        if not str(run_data.get("session_id", "")).strip():
            issues.append(f"session_id is required for {run}")
        for measure in MEASURES:
            value = run_data.get(measure)
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                issues.append(f"{run}.{measure} must be a non-negative integer")
    return issues


def report(data: dict) -> None:
    without = data["without_knowledge_base"]
    with_kb = data["with_knowledge_base"]
    print("REWORK REPORT")
    print(f"task: {data['task_id']}")
    print(f"spec commit: {data['spec_commit']}")
    print("measure | without knowledge base | with knowledge base | delta")
    for measure in MEASURES:
        a = without[measure]
        b = with_kb[measure]
        print(f"{measure} | {a} | {b} | {a - b}")
    base_rounds = without["review_rounds"]
    if base_rounds:
        reduction = (base_rounds - with_kb["review_rounds"]) / base_rounds * 100
        print(f"review round reduction: {reduction:.1f}%")
    else:
        print("review round reduction: base run has zero rounds")
    print(f"limitation: {data.get('limitation', 'record the comparison limitation')}")


def self_test() -> int:
    data = {
        "task_id": "test-task",
        "spec_commit": "abc123",
        "same_task": True,
        "same_criteria": True,
        "same_reviewer": True,
        "operators": {run: "tester" for run in RUNS},
    }
    for run in RUNS:
        value = 2 if run == "without_knowledge_base" else 1
        data[run] = {"session_id": run, **{measure: value for measure in MEASURES}}
    if validate(data):
        print("FAIL rework-report self-test")
        return 1
    report(data)
    print("PASS rework-report self-test")
    return 0


def main(argv: list[str]) -> int:
    if argv == ["--self-test"]:
        return self_test()
    if len(argv) != 1:
        print("usage: rework-report.py PATH | --self-test", file=sys.stderr)
        return 2
    path = Path(argv[0])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL {path}: {exc}")
        return 1
    if not isinstance(data, dict):
        print(f"FAIL {path}: top-level value must be an object")
        return 1
    issues = validate(data)
    if issues:
        print(f"FAIL {path}")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    report(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
