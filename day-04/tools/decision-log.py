#!/usr/bin/env python3
"""
Record every stop the agent makes, and say whether it deserved one.

The Day 4 rule: the agent stops for a choice and never for a fact.

  DECISION  only a person can answer it — money, scope, risk, or a promise
            to a customer. A good stop.
  LOOKUP    the answer already sat in a file, in the source, or in command
            output. A fault in the harness, not in the agent.

The measure is the decision share. A harness that improves moves that share up,
because the lookups get written into the project file instead of asked again.

Run:  python3 tools/decision-log.py add --kind decision --stage 3 \
          --question "..." --answer "..." --owner "..."
      python3 tools/decision-log.py list
      python3 tools/decision-log.py report
      python3 tools/decision-log.py --self-test
"""

import argparse
import json
import os
import sys
import tempfile

DEFAULT = "evidence/day-04/decisions.json"
KINDS = ("decision", "lookup")
STAGES = {1: "understand", 2: "context", 3: "grill", 4: "decide",
          5: "specify", 6: "plan", 7: "build", 8: "prove"}


def load(path):
    if not os.path.exists(path):
        return {"module": "", "stops": []}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save(path, data):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def cmd_add(a):
    if a.stage not in STAGES:
        sys.exit(f"stage must be one of {sorted(STAGES)}")
    data = load(a.file)
    if a.module:
        data["module"] = a.module
    stop = {"n": len(data["stops"]) + 1, "stage": a.stage,
            "stage_name": STAGES[a.stage], "kind": a.kind,
            "question": a.question, "answer": a.answer, "owner": a.owner}
    if a.kind == "lookup":
        # A lookup is a harness gap. Naming the file that should have held the
        # answer is what turns the count into a repair list.
        stop["belongs_in"] = a.belongs_in or "UNNAMED — say which file should hold this"
    data["stops"].append(stop)
    save(a.file, data)
    print(f"stop {stop['n']} recorded as {a.kind.upper()} at stage "
          f"{a.stage} ({STAGES[a.stage]})")
    if a.kind == "lookup" and not a.belongs_in:
        print("this lookup has no home file. Name one with --belongs-in, "
              "then put the answer there.")
    return 0


def cmd_list(a):
    data = load(a.file)
    if not data["stops"]:
        print("no stops recorded yet")
        return 0
    for s in data["stops"]:
        mark = "D" if s["kind"] == "decision" else "L"
        print(f"[{mark}] {s['n']:>2}  stage {s['stage']} {s['stage_name']:<11} "
              f"{s['question'][:64]}")
        if s["kind"] == "lookup":
            print(f"        belongs in: {s.get('belongs_in', '')}")
    return 0


def summarise(data):
    stops = data["stops"]
    d = sum(1 for s in stops if s["kind"] == "decision")
    lookups = [s for s in stops if s["kind"] == "lookup"]
    share = (d / len(stops) * 100) if stops else 0.0
    return len(stops), d, lookups, share


def cmd_report(a):
    data = load(a.file)
    total, decisions, lookups, share = summarise(data)
    if not total:
        print("no stops recorded. Record one before the report.")
        return 1
    print(f"module: {data.get('module') or '(unnamed)'}")
    print(f"stops:           {total}")
    print(f"real decisions:  {decisions}")
    print(f"lookups:         {len(lookups)}")
    print(f"decision share:  {share:.0f}%")
    by_stage = {}
    for s in data["stops"]:
        by_stage.setdefault(s["stage_name"], [0, 0])
        by_stage[s["stage_name"]][0 if s["kind"] == "decision" else 1] += 1
    print("\nby stage:")
    for name, (d, lk) in sorted(by_stage.items()):
        print(f"  {name:<11} decisions {d:>2}   lookups {lk:>2}")
    if lookups:
        print("\nrepair list — put each answer in the named file:")
        for s in lookups:
            print(f"  {s.get('belongs_in', 'UNNAMED')}  <-  {s['question'][:58]}")
    else:
        print("\nno lookups. Every stop needed a person.")
    return 0


def self_test():
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "evidence", "day-04", "decisions.json")
        base = dict(file=path, module="overview", answer="", owner="A. Lead",
                    belongs_in=None)
        cmd_add(argparse.Namespace(kind="decision", stage=4,
                                   question="Round or truncate money?", **base))
        base["belongs_in"] = "CLAUDE.md"
        cmd_add(argparse.Namespace(kind="lookup", stage=7,
                                   question="Which command runs the tests?", **base))
        base["belongs_in"] = None
        cmd_add(argparse.Namespace(kind="decision", stage=5,
                                   question="Does export stay in scope?", **base))

        data = load(path)
        total, decisions, lookups, share = summarise(data)
        assert total == 3 and decisions == 2 and len(lookups) == 1, "bad counts"
        assert round(share) == 67, f"share should be 67, got {share}"
        assert lookups[0]["belongs_in"] == "CLAUDE.md", "a lookup keeps its home file"
        assert data["stops"][0]["stage_name"] == "decide", "stage name is wrong"
        try:
            cmd_add(argparse.Namespace(kind="decision", stage=99,
                                       question="x", **base))
            raise AssertionError("stage 99 must be refused")
        except SystemExit:
            pass
    print("self-test PASS")
    print("  3 stops recorded, 2 decisions and 1 lookup, share 67%")
    print("  the lookup kept the file that should have held the answer")
    print("  an unknown stage number was refused")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    sub = ap.add_subparsers(dest="cmd")

    p = sub.add_parser("add", help="record one stop")
    p.add_argument("--file", default=DEFAULT)
    p.add_argument("--kind", choices=KINDS, required=True)
    p.add_argument("--stage", type=int, required=True)
    p.add_argument("--question", required=True)
    p.add_argument("--answer", default="")
    p.add_argument("--owner", default="")
    p.add_argument("--module", default="")
    p.add_argument("--belongs-in", dest="belongs_in", default=None,
                   help="for a lookup: the file that should have held the answer")
    p.set_defaults(fn=cmd_add)

    p = sub.add_parser("list", help="print every stop")
    p.add_argument("--file", default=DEFAULT)
    p.set_defaults(fn=cmd_list)

    p = sub.add_parser("report", help="counts, the share, and the repair list")
    p.add_argument("--file", default=DEFAULT)
    p.set_defaults(fn=cmd_report)

    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not a.cmd:
        ap.print_help()
        return 2
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
