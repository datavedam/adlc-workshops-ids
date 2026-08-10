#!/usr/bin/env python3
"""
criteria-lint.py — is your acceptance criterion one a check could judge?

It reads the "## Acceptance criteria" section of a FRAMING.md and tests each
numbered line against four rules:

  1  no soft words        correct, accurate, properly, user-friendly, fast,
                          intuitive, clean, robust, appropriate, reasonable
  2  a shape a check
     can follow           GIVEN/WHEN/THEN, or SHALL, or a comparison
  3  something to
     measure              a number, a percentage, a file name or a field name
  4  one criterion        one assertion per line, not three joined by "and"

The tool is blunt on purpose. It flags. You judge.

Run:
    python3 tools/criteria-lint.py modules/fnb/FRAMING.md
"""

import re
import sys

SOFT = ["correct", "accurate", "properly", "proper", "user-friendly", "friendly",
        "fast", "quick", "intuitive", "clean", "robust", "appropriate",
        "reasonable", "good", "nice", "seamless", "efficient", "as needed",
        "if necessary", "etc", "and so on", "should be able"]

SHAPE = [r"\bGIVEN\b.*\bWHEN\b.*\bTHEN\b", r"\bSHALL\b", r"\bMUST\b",
         r"\bequals?\b", r"\bmatch(es)?\b", r"\bis (greater|less) than\b",
         r"\bexits? (with )?(code )?\d", r"\breturns?\b", r"\bwithin\b"]

MEASURE = [r"\d",                                   # a number
           r"\b\w+\.(json|md|csv|html|py|sh)\b",     # a file
           r"`[^`]+`",                               # a named field or command
           r'"[^"]{2,}"',                            # an exact expected string
           r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten)\b"]


def criteria(text):
    """Pull the numbered or bulleted lines under an acceptance-criteria heading."""
    m = re.search(r"^#{1,4}\s*Acceptance criteria.*?$(.*?)(?=^#{1,4}\s|\Z)",
                  text, re.S | re.M | re.I)
    body = m.group(1) if m else text
    out = []
    for line in body.splitlines():
        s = line.strip()
        if re.match(r"^([-*+]|\d+[.)])\s+", s):
            out.append(re.sub(r"^([-*+]|\d+[.)])\s+", "", s))
    return out


def check(c):
    issues = []
    low = c.lower()
    hits = [w for w in SOFT if re.search(r"\b" + re.escape(w) + r"\b", low)]
    if hits:
        issues.append(f"soft word: {', '.join(hits)} — a person must judge this")
    if not any(re.search(p, c, re.I) for p in SHAPE):
        issues.append("no shape a check can follow — use GIVEN/WHEN/THEN or SHALL")
    if not any(re.search(p, c) for p in MEASURE):
        issues.append("nothing to measure — name a number, a field or a file")
    if len(re.findall(r"\band\b", low)) >= 2:
        issues.append("looks like more than one criterion — split it")
    return issues


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: criteria-lint.py <FRAMING.md>")
    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        cs = criteria(f.read())

    if not cs:
        sys.exit(f"no criteria found in {path} — expected a list under "
                 f"'## Acceptance criteria'")

    print(f"{path} — {len(cs)} criteria\n")
    bad = 0
    for i, c in enumerate(cs, 1):
        issues = check(c)
        mark = "  ok " if not issues else "  !! "
        print(f"{mark}{i}. {c[:96]}")
        for it in issues:
            print(f"        - {it}")
        if issues:
            bad += 1

    print(f"\n{len(cs) - bad} of {len(cs)} could be judged by a check.")
    if bad:
        print("Rewrite the flagged ones. A criterion a person must judge is a\n"
              "criterion two people will disagree about.")
    if len(cs) < 4:
        print(f"\nYou need at least 4. You have {len(cs)}.")
        bad += 1
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
