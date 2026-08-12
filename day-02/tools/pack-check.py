#!/usr/bin/env python3
"""Check the generated Day 2 project pack.

Claude Code writes the pack. This tool checks file presence, required text,
status labels, and placeholder removal. Human review judges business choices.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_FILES = (
    "CLAUDE.md",
    "CONFLICTS.md",
    "FRAMING.md",
    "DATA-CONTRACT.md",
    "ARCHITECTURE.md",
    "SPEC.md",
    "SKILLS.md",
    "EVIDENCE.md",
    "adr/001-title.md",
    "adr/002-title.md",
    "adr/003-title.md",
)

REQUIRED_TEXT = {
    "CLAUDE.md": ("## Commands", "## Rules", "## Traps"),
    "CONFLICTS.md": ("status", "source", "owner"),
    "FRAMING.md": ("intent", "acceptance criteria"),
    "DATA-CONTRACT.md": ("source", "derived", "formula"),
    "ARCHITECTURE.md": ("data", "interface"),
    "SPEC.md": ("acceptance", "end-to-end"),
    "SKILLS.md": ("source", "skill", "hash"),
    "EVIDENCE.md": ("command", "output", "sign-off"),
}

STATUS_WORDS = {"OBSERVED", "DERIVED", "PROPOSED", "APPROVED", "OPEN"}
PLACEHOLDER = re.compile(r"<[^>\n]+>|\bTODO\b|\bTBD\b", re.I)


def check(pack: Path, project_file: Path) -> list[str]:
    errors: list[str] = []
    for name in REQUIRED_FILES:
        path = pack / name
        if not path.is_file():
            errors.append(f"missing file: {name}")
            continue
        content = path.read_text(encoding="utf-8")
        if PLACEHOLDER.search(content):
            errors.append(f"placeholder remains: {name}")
        for required in REQUIRED_TEXT.get(name, ()):
            if required.lower() not in content.lower():
                errors.append(f"missing text in {name}: {required}")

    if project_file.is_file():
        content = project_file.read_text(encoding="utf-8")
        if not any(word in content for word in STATUS_WORDS):
            errors.append(f"project file has no status labels: {project_file}")
    else:
        errors.append(f"missing project file: {project_file}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack", type=Path)
    parser.add_argument("--project-file", type=Path, default=Path("CLAUDE.md"))
    args = parser.parse_args()

    errors = check(args.pack, args.project_file)
    if errors:
        print(f"FAIL pack-check {args.pack}")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"PASS pack-check {args.pack}")
    print(f"  files: {len(REQUIRED_FILES)}")
    print(f"  project: {args.project_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
