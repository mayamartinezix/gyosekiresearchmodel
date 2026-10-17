#!/usr/bin/env python3
"""General Monte Carlo + stress-test model for ANY company.

Run:  python3 framework/gyoseki_mc.py companies/skylark/config.json
Options: --n 20000  --seed 1  --json out.json

No installs needed (standard library only).

How it works (plain words):
 1. Each segment's sales = last year's sales x (1 + volume growth) x (1 + price growth),
    then adjusted for currency if the segment earns in a foreign currency.
 2. Segment profit = sales x margin.
 3. Add fixed items (corporate costs), non-operating items, and one-offs.
 4. Net income = pre-tax profit x (1 - tax) x (1 - minority share) + after-tax one-offs.
 5. Repeat thousands of times with random draws. All segments share ONE "demand"
    draw (so they rise and fall together, as in real life) and ONE draw per currency.
 6. Stress tests = same thing, but with the average inputs pushed in a bad direction.

Every number in a config.json is an input YOU can change. Inputs marked
"ASSUMPTION" in the config's notes are guesses, not company facts.
"""
import argparse
import json
import math
import random
import statistics


def pct(sorted_vals, p):
    """p-th percentile of an already sorted list."""
    i = min(len(sorted_vals) - 1, max(0, int(round(p / 100 * len(sorted_vals))) - 1))
    return sorted_vals[i]


def normal(mean, sd):
    return random.gauss(mean, sd) if sd > 0 else mean


def draw_once(cfg, shifts):
    """One simulated year. Returns (revenue, profit, net_income)."""
    fx_cfg = cfg.get("fx", {})
    fx = {}
    for pair, v in fx_cfg.items():
        exp = v["expected"] + shifts.get("fx", {}).get(pair, 0.0)
        fx[pair] = normal(exp, v["sd"])

    z_common = random.gauss(0, 1)  # shared demand draw

    revenue = 0.0
    profit = 0.0
    for s in cfg["segments"]:
        name = s["name"]
        beta = s.get("demand_beta", 0.5)
        idio = math.sqrt(max(0.0, 1 - beta * beta))

        vg = s["volume_growth"]
        vol = (vg["mean"] + shifts.get("growth", {}).get(name, 0.0)
               + shifts.get("all_growth", 0.0)
               + vg["sd"] * (beta * z_common + idio * random.gauss(0, 1)))

        pg = s["price_growth"]
        price = (normal(pg["mean"], pg["sd"]) + shifts.get("price", {}).get(name, 0.0)
                 + shifts.get("all_price", 0.0))

        rev = s["revenue_base"] * (1 + vol) * (1 + price)

        f = s.get("fx")
        if f:
            rev *= 1 + f["exposure"] * (fx[f["pair"]] / fx_cfg[f["pair"]]["base"] - 1)

        m = s["margin"]
        margin = (normal(m["mean"], m["sd"]) + shifts.get("margin", {}).get(name, 0.0)
                  + shifts.get("all_margin", 0.0))

        revenue += rev
        profit += rev * margin

    for item in cfg.get("fixed_items", []):
        profit += normal(item["mean"], item["sd"])

    # pre-tax items below the profit measure
    below = 0.0
    no = cfg.get("non_operating")
    if no:
        below += normal(no["mean"], no["sd"])

    after_tax_extra = 0.0
    for o in cfg.get("one_offs", []):
        prob = shifts.get("oneoff_prob", {}).get(o["name"], o["prob"])
        scale = shifts.get("oneoff_scale", {}).get(o["name"], 1.0)
        if random.random() < prob:
            amt = normal(o["mean"], o["sd"]) * scale
            if o.get("stage", "pre_tax") == "pre_tax":
                below += amt
            else:
                after_tax_extra += amt

    pre_tax = profit + below
    tax = min(0.6, max(0.0, normal(cfg["tax_rate"]["mean"], cfg["tax_rate"]["sd"])))
    mino = min(0.9, max(0.0, normal(cfg["minority_share"]["mean"], cfg["minority_share"]["sd"])))
    # losses are not taxed in this simple version
    after_tax = pre_tax * (1 - tax) * (1 - mino) if pre_tax > 0 else pre_tax
    return revenue, profit, after_tax + after_tax_extra


def run(cfg, n, shifts=None):
    shifts = shifts or {}
    revs, profs, nis = [], [], []
    for _ in range(n):
        r, p, ni = draw_once(cfg, shifts)
        revs.append(r)
        profs.append(p)
        nis.append(ni)
    for lst in (revs, profs, nis):
        lst.sort()
    return revs, profs, nis


def summarize(label, revs, profs, nis, guidance):
    row = {"scenario": label}
    for key, lst in (("revenue", revs), ("profit", profs), ("net_income", nis)):
        row[key] = {
            "p5": pct(lst, 5), "p25": pct(lst, 25), "p50": pct(lst, 50),
            "p75": pct(lst, 75), "p95": pct(lst, 95),
            "mean": statistics.mean(lst), "stdev": statistics.pstdev(lst),
        }
    if guidance:
        for key, lst in (("revenue", revs), ("profit", profs), ("net_income", nis)):
            g = guidance.get(key)
            if g is not None:
                row[key]["prob_above_guidance"] = sum(1 for x in lst if x > g) / len(lst)
    return row


def fmt(x):
    return f"{x/1000:,.1f}"  # config numbers are in million yen -> print billions


def print_table(rows, cfg):
    g = cfg.get("guidance", {})
    unit = "billion yen"
    print(f"\n=== {cfg['company']} | profit measure: {cfg['profit_label']} | {unit} ===")
    if g:
        print("Company guidance: " + ", ".join(f"{k}={fmt(v)}" for k, v in g.items() if v is not None))
    for key, title in (("revenue", "REVENUE"), ("profit", cfg["profit_label"].upper()),
                       ("net_income", "NET INCOME")):
        print(f"\n{title}")
        print(f"{'scenario':32s} {'p5':>9s} {'p25':>9s} {'median':>9s} {'p75':>9s} {'p95':>9s} {'P(>guide)':>10s}")
        for r in rows:
            d = r[key]
            pg = d.get("prob_above_guidance")
            pgs = f"{pg*100:9.0f}%" if pg is not None else f"{'-':>10s}"
            print(f"{r['scenario']:32s} {fmt(d['p5']):>9s} {fmt(d['p25']):>9s} "
                  f"{fmt(d['p50']):>9s} {fmt(d['p75']):>9s} {fmt(d['p95']):>9s} {pgs}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--n", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--json")
    a = ap.parse_args()

    cfg = json.load(open(a.config))
    random.seed(a.seed)
    guidance = cfg.get("guidance")

    rows = [summarize("BASE (no stress)", *run(cfg, a.n), guidance)]
    for st in cfg.get("stress_tests", []):
        random.seed(a.seed)  # same random numbers -> fair comparison
        rows.append(summarize(st["name"], *run(cfg, a.n, st["shifts"]), guidance))

    print_table(rows, cfg)
    print("\nNotes:", cfg.get("notes", ""))
    if a.json:
        json.dump(rows, open(a.json, "w"), indent=2)


if __name__ == "__main__":
    main()
