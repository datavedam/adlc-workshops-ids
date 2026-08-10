#!/usr/bin/env python3
"""
reconcile.py — the check the cold run must pass (Part 4).

Section 2.1 of the BRD promises that the Consolidated P&L sums the departmental
data and reconciles to the headline totals. This tool tests that promise.

The agent builds out/pl.json from the pack. This tool reads it and checks it.
Expected shape:

    {
      "total_revenue": 30.3,          INR Lakh
      "total_cost":   -17.5,          INR Lakh, negative
      "gop":           12.8,          INR Lakh
      "revpar":      4842,            INR
      "trevpar":     7974,            INR
      "goppar":      3358             INR
    }

Run:
    python3 tools/reconcile.py                 # reads out/pl.json
    python3 tools/reconcile.py path/to/pl.json

Exit 0 = every assertion held. Exit 1 = at least one failed.
A FAIL is a legitimate result. It means the agent computed honestly from data
that does not reconcile. Read the failures before you call it a defect.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "fx1-sample.json")
TOL_LAKH = 0.15      # rounding on a figure printed to one decimal
TOL_RUPEE = 5        # rounding on a per-room figure


def fail(msg):
    print(f"  FAIL  {msg}")
    return 1


def ok(msg):
    print(f"  pass  {msg}")
    return 0


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "out", "pl.json")
    if not os.path.exists(out_path):
        sys.exit(f"no output to check at {out_path}\n"
                 f"the agent must write out/pl.json — see the shape in this file's header")

    with open(DATA, encoding="utf-8") as f:
        d = json.load(f)
    with open(out_path, encoding="utf-8") as f:
        got = json.load(f)

    keys = d["property"]["keys"]
    nights = keys * d["property"]["mtd_days"]
    pl = d["modules"]["overview"]["tables"]["consolidated_pl"]
    kpi = d["modules"]["overview"]["kpis"]

    src_rev = sum(r["value"] for r in pl["rows"] if r.get("kind") == "revenue")
    src_cost = sum(r["value"] for r in pl["rows"] if r.get("kind") == "cost")
    src_gop = src_rev + src_cost

    print(f"reconcile — {d['property']['name']}, {keys} keys, "
          f"{nights} available room-nights\n")

    bad = 0
    print("A · the P&L sums the departmental data")
    bad += ok(f"total revenue {got.get('total_revenue')} = sum of the five lines {src_rev:.1f}") \
        if abs(got.get("total_revenue", 0) - src_rev) <= TOL_LAKH \
        else fail(f"total revenue is {got.get('total_revenue')}, the five lines sum to {src_rev:.1f}")
    bad += ok(f"GOP {got.get('gop')} = revenue less the four cost blocks {src_gop:.1f}") \
        if abs(got.get("gop", 0) - src_gop) <= TOL_LAKH \
        else fail(f"GOP is {got.get('gop')}, revenue less cost is {src_gop:.1f}")

    print("\nB · the per-room figures follow from the P&L")
    for name, base in (("revpar", "Rooms"), ("trevpar", None), ("goppar", None)):
        if base:
            amount = next(r["value"] for r in pl["rows"] if r["line"] == base)
        else:
            amount = src_rev if name == "trevpar" else src_gop
        want = amount * 1e5 / nights
        have = got.get(name, 0)
        bad += ok(f"{name.upper()} {have:,.0f} = {want:,.0f}") \
            if abs(have - want) <= TOL_RUPEE \
            else fail(f"{name.upper()} is {have:,.0f}, computed from the P&L it is {want:,.0f}")

    print("\nC · section 2.1 — the P&L reconciles to the headline tiles")
    for name in ("revpar", "trevpar", "goppar"):
        tile = kpi[name]["value"]
        have = got.get(name, 0)
        bad += ok(f"{name.upper()} matches the tile ({tile:,})") \
            if abs(have - tile) <= TOL_RUPEE \
            else fail(f"{name.upper()} is {have:,.0f}, the headline tile states {tile:,} "
                      f"(difference ₹{have - tile:,.0f})")

    print(f"\n{'RECONCILED' if not bad else str(bad) + ' ASSERTION(S) FAILED'}")
    if bad:
        print("\nA failure in section C is expected on the raw BRD data. It is the\n"
              "conflict your pack had to decide. Check that your CONFLICTS.md says\n"
              "which figure survives, and why.")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
