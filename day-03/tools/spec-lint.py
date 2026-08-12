#!/usr/bin/env python3
"""Check the required structure of a Day 3 module specification."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = (
    "## Intent",
    "## Out of scope",
    "## Acceptance criteria",
    "## Interfaces and data",
    "## End-to-end check",
)
EARS_WORDS = re.compile(r"\b(SHALL|WHEN|WHILE|IF|WHERE)\b", re.I)
CRITERION = re.compile(r"^\s*(?:\d+[.)]|[-*])\s+(.+)$")
PLACEHOLDER = re.compile(r"<[^>\n]+>")


def section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    tail = text[start + len(heading):]
    next_heading = re.search(r"\n##\s+", tail)
    return tail[:next_heading.start()] if next_heading else tail


def validate(text: str) -> list[str]:
    issues: list[str] = []
    if not text.startswith("# SPEC"):
        issues.append("the file must start with '# SPEC'")
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            issues.append(f"missing heading: {heading}")

    if PLACEHOLDER.search(text):
        issues.append("placeholder text remains")

    scope = section(text, "## Out of scope")
    scope_items = [line for line in scope.splitlines() if re.match(r"^\s*[-*]\s+\S", line)]
    if len(scope_items) < 2:
        issues.append("out-of-scope needs at least two specific items")

    criteria = section(text, "## Acceptance criteria")
    criteria_items = [m.group(1) for line in criteria.splitlines() if (m := CRITERION.match(line))]
    if len(criteria_items) < 5:
        issues.append("acceptance criteria needs at least five items")
    if criteria_items and sum(bool(EARS_WORDS.search(item)) for item in criteria_items) < 5:
        issues.append("each acceptance criterion needs an EARS word")

    interfaces = section(text, "## Interfaces and data")
    if "|" not in interfaces:
        issues.append("interfaces and data needs a table")

    end_to_end = section(text, "## End-to-end check")
    if not re.search(r"python|command|check|expected", end_to_end, re.I):
        issues.append("end-to-end check needs a command or an observable result")
    return issues


def self_test() -> int:
    valid = """# SPEC — Test\n\n## Intent\nA decision.\n\n## Out of scope\n- One\n- Two\n\n## Acceptance criteria\n1. WHEN x the module SHALL y.\n2. WHILE x the module SHALL y.\n3. IF x the module SHALL y.\n4. WHERE x the module SHALL y.\n5. The module SHALL y.\n\n## Interfaces and data\n| a | b |\n|---|---|\n\n## End-to-end check\nRun `python3 check.py` and expect pass.\n"""
    if validate(valid):
        print("FAIL self-test")
        return 1
    if not validate(valid.replace("## Intent", "## Missing")):
        print("FAIL self-test")
        return 1
    print("PASS spec-lint self-test")
    return 0


def main(argv: list[str]) -> int:
    if argv == ["--self-test"]:
        return self_test()
    if len(argv) != 1:
        print("usage: spec-lint.py PATH | --self-test", file=sys.stderr)
        return 2
    path = Path(argv[0])
    if not path.is_file():
        print(f"FAIL {path}: file does not exist")
        return 1
    issues = validate(path.read_text(encoding="utf-8"))
    if issues:
        print(f"FAIL {path}")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print(f"PASS {path}: specification structure is complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
