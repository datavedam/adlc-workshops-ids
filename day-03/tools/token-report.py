#!/usr/bin/env python3
"""Calculate token cost and cost per merged change for two runs."""

from __future__ import annotations

import json
import sys
from pathlib import Path


RUNS = ("full", "reduced")
TOKEN_FIELDS = ("input_tokens", "cached_input_tokens", "output_tokens")
QUALITY_FIELDS = ("wall_clock_seconds", "review_rounds", "defects", "merged_changes")


def validate(data: dict) -> list[str]:
    issues: list[str] = []
    for key in ("task_id", "token_source", "rate_source", "rates_per_million", *RUNS):
        if key not in data:
            issues.append(f"missing field: {key}")
    rates = data.get("rates_per_million", {})
    for key in ("input", "cached_input", "output"):
        value = rates.get(key)
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
            issues.append(f"rates_per_million.{key} must be zero or positive")
    for run in RUNS:
        run_data = data.get(run, {})
        if not isinstance(run_data, dict):
            issues.append(f"run data must be an object: {run}")
            continue
        for key in (*TOKEN_FIELDS, *QUALITY_FIELDS):
            value = run_data.get(key)
            if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
                issues.append(f"{run}.{key} must be zero or positive")
        if isinstance(run_data.get("merged_changes"), (int, float)) and run_data.get("merged_changes", 0) == 0:
            issues.append(f"{run}.merged_changes must be greater than zero")
    return issues


def cost(data: dict, run: str) -> float:
    rates = data["rates_per_million"]
    values = data[run]
    return (
        values["input_tokens"] * rates["input"]
        + values["cached_input_tokens"] * rates["cached_input"]
        + values["output_tokens"] * rates["output"]
    ) / 1_000_000


def report(data: dict) -> None:
    print("TOKEN REPORT")
    print(f"task: {data['task_id']}")
    print(f"currency: {data.get('currency', 'USD')}")
    print(f"token source: {data['token_source']}")
    print(f"rate source: {data['rate_source']}")
    for run in RUNS:
        run_data = data[run]
        total_tokens = sum(run_data[key] for key in TOKEN_FIELDS)
        run_cost = cost(data, run)
        per_change = run_cost / run_data["merged_changes"]
        print(f"{run}: tokens={total_tokens} seconds={run_data['wall_clock_seconds']} defects={run_data['defects']}")
        print(f"{run}: cost={run_cost:.6f} cost_per_merged_change={per_change:.6f}")


def self_test() -> int:
    data = {
        "task_id": "test-task",
        "token_source": "test meter",
        "rate_source": "test rates",
        "rates_per_million": {"input": 1, "cached_input": 0.1, "output": 2},
        "full": {
            "input_tokens": 1_000_000,
            "cached_input_tokens": 100_000,
            "output_tokens": 100_000,
            "wall_clock_seconds": 10,
            "review_rounds": 1,
            "defects": 0,
            "merged_changes": 1,
        },
        "reduced": {
            "input_tokens": 500_000,
            "cached_input_tokens": 50_000,
            "output_tokens": 50_000,
            "wall_clock_seconds": 8,
            "review_rounds": 1,
            "defects": 0,
            "merged_changes": 1,
        },
    }
    if validate(data) or cost(data, "full") <= cost(data, "reduced"):
        print("FAIL token-report self-test")
        return 1
    report(data)
    print("PASS token-report self-test")
    return 0


def main(argv: list[str]) -> int:
    if argv == ["--self-test"]:
        return self_test()
    if len(argv) != 1:
        print("usage: token-report.py PATH | --self-test", file=sys.stderr)
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
