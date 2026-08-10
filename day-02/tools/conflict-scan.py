#!/usr/bin/env python3
"""
conflict-scan.py — find the numbers in the FX1 data that disagree.

This tool does the ARITHMETIC. It does not make the DECISION.
It reports every place the data contradicts itself. Which number survives
is your judgement, and it goes in your CONFLICTS.md with the reason.

Three rules, applied to every module:

  R1  does the table add up?      sum the rows, compare with the stated total
  R2  does the derived number
      follow from its parts?      recompute it, compare with the stated value
  R3  do two places agree?        compare the same figure across modules

Run:
    python3 tools/conflict-scan.py                 # every module
    python3 tools/conflict-scan.py fnb             # one module
    python3 tools/conflict-scan.py --mine spa      # one module, exit 1 if any open
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "fx1-sample.json")
TOL = 0.05          # a rounding difference this small is not a conflict


def load():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


def rows_sum(table, key):
    return sum(r.get(key, 0) for r in table.get("rows", []) if isinstance(r.get(key), (int, float)))


def near(a, b, tol=TOL):
    return abs(a - b) <= tol


class Report:
    def __init__(self):
        self.items = []

    def add(self, rule, module, what, values, note=""):
        self.items.append({"rule": rule, "module": module, "what": what,
                           "values": values, "note": note})

    def show(self):
        if not self.items:
            print("no conflicts found.")
            return 0
        by_mod = {}
        for it in self.items:
            by_mod.setdefault(it["module"], []).append(it)
        for mod, items in by_mod.items():
            print(f"\n── {mod} ── {len(items)} conflict(s)")
            for it in items:
                print(f"   [{it['rule']}] {it['what']}")
                for label, val in it["values"]:
                    print(f"        {label:<42s} {val}")
                if it["note"]:
                    print(f"        → {it['note']}")
        print(f"\n{len(self.items)} conflict(s). "
              f"Decide every one of them in CONFLICTS.md.")
        return len(self.items)


# ── R1 · does the table add up? ─────────────────────────────────────────────
def rule_totals(d, rep, only):
    for mod, m in d["modules"].items():
        if only and mod != only:
            continue
        for tname, t in m.get("tables", {}).items():
            checks = [
                ("stated_total_rooms",      "rooms",      "rooms"),
                ("stated_total_bookings",   "bookings",   "bookings"),
                ("stated_total_treatments", "treatments", "treatments"),
                ("stated_total_share",      "share",      "%"),
                ("stated_total_revenue",    "revenue",    "L"),
            ]
            for stated_key, row_key, unit in checks:
                # only sum a column the rows actually carry — the P&L states its
                # revenue under "value" and is handled by the dedicated block below
                if stated_key in t and any(row_key in r for r in t.get("rows", [])):
                    got = rows_sum(t, row_key)
                    want = t[stated_key]
                    if not near(got, want, 0.15):
                        rep.add("R1", mod, f"{t['title']} does not add up",
                                [("sum of the rows", f"{got:g} {unit}"),
                                 ("the table states", f"{want:g} {unit}")])

            # the consolidated P&L is the one table with revenue and cost rows
            if "stated_gop" in t and any(r.get("kind") for r in t.get("rows", [])):
                rev = sum(r["value"] for r in t["rows"] if r.get("kind") == "revenue")
                cost = sum(r["value"] for r in t["rows"] if r.get("kind") == "cost")
                if not near(rev, t.get("stated_total_revenue", rev), 0.15):
                    rep.add("R1", mod, f"{t['title']} — revenue lines",
                            [("sum of the revenue lines", f"{rev:.1f} L"),
                             ("the table states", f"{t['stated_total_revenue']:g} L")])
                if not near(rev + cost, t["stated_gop"], 0.15):
                    rep.add("R1", mod, f"{t['title']} — GOP",
                            [("revenue less cost", f"{rev + cost:.1f} L"),
                             ("the table states", f"{t['stated_gop']:g} L")])

            # the USALI bridge: the same shape, expressed as signed lines
            if tname == "usali_bridge":
                tot = t["rows"][0]["value"]
                cost = sum(r["value"] for r in t["rows"][1:])
                if not near(tot + cost, t["stated_gop"], 0.15):
                    rep.add("R1", mod, f"{t['title']} does not reach the stated GOP",
                            [("revenue less the four cost blocks", f"{tot + cost:.1f} L"),
                             ("the table states", f"{t['stated_gop']:g} L")])
            if tname == "cost_structure":
                got = rows_sum(t, "value")
                if not near(got, t["stated_total_cost"], 0.15):
                    rep.add("R1", mod, f"{t['title']} does not match the bridge",
                            [("sum of the cost lines", f"{got:.1f} L"),
                             ("total cost from the bridge", f"{t['stated_total_cost']:g} L")],
                            "these lines add up to the whole revenue, which leaves no GOP")


# ── R2 · does the derived number follow? ────────────────────────────────────
def rule_derived(d, rep, only):
    keys = d["property"]["keys"]
    nights = keys * d["property"]["mtd_days"]

    if not only or only == "overview":
        ov = d["modules"]["overview"]
        pl = ov["tables"]["consolidated_pl"]
        rev = sum(r["value"] for r in pl["rows"] if r.get("kind") == "revenue")
        cost = sum(r["value"] for r in pl["rows"] if r.get("kind") == "cost")
        rooms = next(r["value"] for r in pl["rows"] if r["line"] == "Rooms")
        gop = rev + cost
        pairs = [
            ("RevPAR",  rooms * 1e5 / nights, ov["kpis"]["revpar"]["value"]),
            ("TRevPAR", rev * 1e5 / nights,   ov["kpis"]["trevpar"]["value"]),
            ("GOPPAR",  gop * 1e5 / nights,   ov["kpis"]["goppar"]["value"]),
        ]
        for name, computed, stated in pairs:
            if abs(computed - stated) > 5:
                rep.add("R2", "overview", f"{name} does not follow from the P&L",
                        [("computed from the P&L", f"₹{computed:,.0f}"),
                         ("the headline tile states", f"₹{stated:,.0f}"),
                         ("difference", f"₹{computed - stated:,.0f}")],
                        "section 2.1 promises these reconcile")

    if not only or only == "fnb":
        f = d["modules"]["fnb"]
        rev, cov = f["kpis"]["fnb_revenue"]["value"], f["kpis"]["covers"]["value"]
        stated = f["kpis"]["average_check"]["value"]
        computed = rev * 1e5 / cov
        if abs(computed - stated) > 5:
            rep.add("R2", "fnb", "Average check does not follow from revenue and covers",
                    [("computed", f"₹{computed:,.0f}"), ("stated", f"₹{stated:,.0f}")])

    if not only or only == "spa":
        s = d["modules"]["spa"]
        row = s["tables"]["services_vs_retail"]["rows"][0]
        computed = row["retail"] / (row["services"] + row["retail"]) * 100
        note = s["kpis"]["spa_revenue"].get("note", "")
        if "7%" in note and abs(computed - 7) > 1:
            rep.add("R2", "spa", "Retail share in the commentary does not match the table",
                    [("computed from the table", f"{computed:.1f}%"),
                     ("the commentary states", "7%"),
                     ("the retail attach tile states", f"{s['kpis']['retail_attach']['value']}%")])

    if not only or only == "front_office":
        fo = d["modules"]["front_office"]
        ooo = next(r["rooms"] for r in fo["tables"]["room_status"]["rows"]
                   if "Out of order" in r["status"])
        sellable = keys - ooo
        sold = fo["kpis"]["rooms_sold"]["value"]
        note = d["modules"]["overview"]["kpis"]["occupancy"]["note"]
        if "79%" in note:
            implied = round(keys * 0.79)
            if implied != sellable:
                rep.add("R2", "front_office",
                        "The occupancy ceiling implies a different sellable count",
                        [("ceiling of 79% implies sellable", f"{implied} rooms"),
                         ("room status implies sellable", f"{sellable} rooms"),
                         ("so rooms out of order would be", f"{keys - implied} not {ooo}")])
        if sellable > 0:
            rep.add("R2", "front_office", "Occupancy on sellable rooms",
                    [("computed from room status", f"{sold / sellable * 100:.1f}%"),
                     ("the overview commentary states", "67%")],
                    "these agree only if 20 rooms are out of order")


# ── R3 · do two places agree? ───────────────────────────────────────────────
def rule_cross(d, rep, only):
    m = d["modules"]

    # page references so every claim can be checked against the document
    pages = {x["id"]: x.get("source", {}) for x in d.get("cross_refs", [])}

    def emit(mod, xr, values, note=""):
        if only and mod != only:
            return
        src = pages.get(xr.split(" ")[0].rstrip("b"), {})
        if src:
            values = values + [("— check it in the BRD", " · ".join(sorted(set(src.values()))))]
        rep.add("R3", mod, f"{xr} — the same figure, stated more than once",
                values, note)

    pl = m["overview"]["tables"]["consolidated_pl"]
    pl_fnb = next(r["value"] for r in pl["rows"] if r["line"].startswith("Food"))
    emit("fnb", "XR-2 · Food & Beverage revenue",
         [("Overview P&L", f"₹{pl_fnb}L"),
          ("F&B module tile", f"₹{m['fnb']['kpis']['fnb_revenue']['value']}L"),
          ("sum of the outlets", f"₹{rows_sum(m['fnb']['tables']['revenue_by_outlet'], 'revenue'):.1f}L"),
          ("sum of the dayparts", f"₹{rows_sum(m['fnb']['tables']['revenue_by_daypart'], 'revenue'):.1f}L")],
         "four numbers, one month")

    emit("fnb", "XR-3 · Covers",
         [("F&B module tile", f"{m['fnb']['kpis']['covers']['value']:,}"),
          ("sum of the outlets", f"{rows_sum(m['fnb']['tables']['revenue_by_outlet'], 'covers'):,.0f}"),
          ("sum of the dayparts", f"{rows_sum(m['fnb']['tables']['revenue_by_daypart'], 'covers'):,.0f}")])

    emit("finance", "XR-4 · Total revenue, both labelled MTD",
         [("Overview P&L", f"₹{pl['stated_total_revenue']}L"),
          ("Finance tile", f"₹{m['finance']['kpis']['total_revenue']['value']}L"),
          ("ratio", f"{m['finance']['kpis']['total_revenue']['value'] / pl['stated_total_revenue']:.1f}x")])

    pl_banq = next(r["value"] for r in pl["rows"] if r["line"].startswith("Banquets"))
    emit("sales_catering", "XR-6 · Banquet revenue",
         [("Overview P&L", f"₹{pl_banq}L"),
          ("Sales & Catering tile", f"₹{m['sales_catering']['kpis']['banquet_revenue']['value']}L")])

    emit("sales_catering", "XR-6b · Confirmed events",
         [("the tile states", m["sales_catering"]["kpis"]["confirmed_events"]["value"]),
          ("its own commentary states", "14"),
          ("the benchmark states pipeline", "41")])

    emit("signals", "XR-8 · August rooms on the books",
         [("Overview booking pace, Aug",
           next(r["otb"] for r in m["overview"]["tables"]["booking_pace"]["rows"] if r["month"] == "Aug")),
          ("Signals pace, day 30",
           next(r["otb"] for r in m["signals"]["tables"]["booking_pace_month"]["rows"]
                if r["checkpoint"] == "Day 30"))])


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    strict = "--mine" in sys.argv
    only = args[0] if args else None
    d = load()
    if only and only not in d["modules"]:
        sys.exit(f"unknown module '{only}'. choose from: {', '.join(d['modules'])}")

    print(f"FX1 conflict scan — {d['property']['name']}, "
          f"{d['property']['keys']} keys, MTD = {d['property']['mtd_days']} days")
    print(f"module: {only or 'ALL'}")

    rep = Report()
    rule_totals(d, rep, only)
    rule_derived(d, rep, only)
    rule_cross(d, rep, only)
    n = rep.show()

    print("\nThis tool did the arithmetic. It did not decide anything.")
    print("Write the decision, and the reason for it, in CONFLICTS.md.")
    sys.exit(1 if (strict and n) else 0)


if __name__ == "__main__":
    main()
