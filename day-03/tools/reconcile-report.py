#!/usr/bin/env python3
"""Check one module output against its input data and output contract."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def check(contract_path: Path) -> list[str]:
    issues: list[str] = []
    try:
        contract = load(contract_path)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"contract read failed: {exc}"]

    module_key = contract.get("module_key", "")
    if not isinstance(module_key, str) or not module_key or "<" in module_key:
        issues.append("module_key needs a real value")
        return issues
    input_path = Path(contract.get("input_file", ""))
    output_path = Path(contract.get("output_file", ""))
    if not input_path.is_file():
        issues.append(f"input file does not exist: {input_path}")
    if not output_path.is_file():
        issues.append(f"output file does not exist: {output_path}")
    if issues:
        return issues

    try:
        source = load(input_path)
        output = load(output_path)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"data read failed: {exc}"]

    source_module = source.get("modules", {}).get(module_key)
    if not isinstance(source_module, dict):
        issues.append(f"module key is absent from source data: {module_key}")
    required = contract.get("required_fields", [])
    if not isinstance(output, dict):
        issues.append("output must be a JSON object")
        return issues
    for field in required:
        if field not in output:
            issues.append(f"missing output field: {field}")
    if output.get("module_key") != module_key:
        issues.append("output.module_key does not match the contract")
    if output.get("source_file") != str(input_path):
        issues.append("output.source_file does not match the contract input path")
    if isinstance(source_module, dict) and output.get("title") != source_module.get("title"):
        issues.append("output.title does not match source module title")
    if output.get("property_code") != source.get("property", {}).get("code"):
        issues.append("output.property_code does not match source property code")
    if output.get("as_of_days") != source.get("property", {}).get("mtd_days"):
        issues.append("output.as_of_days does not match source mtd_days")
    metrics = output.get("metrics")
    if not isinstance(metrics, list) or not metrics:
        issues.append("output.metrics needs at least one item")
    return issues


def self_test() -> int:
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = root / "data.json"
        contract = root / "contract.json"
        output = root / "view.json"
        source.write_text(json.dumps({
            "property": {"code": "5768", "mtd_days": 4},
            "modules": {"fnb": {"title": "Food and Beverage"}},
        }), encoding="utf-8")
        output.write_text(json.dumps({
            "module_key": "fnb",
            "property_code": "5768",
            "title": "Food and Beverage",
            "as_of_days": 4,
            "metrics": [{"name": "revenue", "value": 1}],
            "source_file": str(source),
        }), encoding="utf-8")
        contract.write_text(json.dumps({
            "module_key": "fnb",
            "input_file": str(source),
            "output_file": str(output),
            "required_fields": ["module_key", "property_code", "title", "as_of_days", "metrics", "source_file"],
        }), encoding="utf-8")
        if check(contract):
            print("FAIL reconcile-report self-test")
            return 1
    print("PASS reconcile-report self-test")
    return 0


def main(argv: list[str]) -> int:
    if argv == ["--self-test"]:
        return self_test()
    if len(argv) != 1:
        print("usage: reconcile-report.py PATH | --self-test", file=sys.stderr)
        return 2
    issues = check(Path(argv[0]))
    if issues:
        print("FAIL reconciliation")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print("PASS reconciliation: output matches the source contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
