#!/usr/bin/env python3
"""Backtest alt-data signals: which ones (or pairs) actually helped predict results?

Run:  python3 framework/backtest.py companies/skylark/backtest_data.csv
      python3 framework/backtest.py framework/examples/synthetic_backtest.csv

CSV columns (one row per period, oldest first):
  period, actual, baseline, signal_1, signal_2, ...
  - actual   = what really happened (e.g. operating profit)
  - baseline = what you would have guessed WITHOUT the signal (e.g. company guidance,
               or last year's actual). Leave blank to use the previous actual.
  - signals  = your alt-data numbers (e.g. % change in store traffic). Blank = missing.

Method ("walk-forward", no peeking):
  For each period t, using ONLY earlier periods, learn how much of the miss
  (actual - baseline) each signal explains. Then predict period t and record the error.
  A signal is kept if its error is smaller than the baseline's error.

Standard library only.
"""
import argparse
import csv
import itertools
import math


def solve(a, b):
    """Solve a x = b (small, Gaussian elimination with pivoting)."""
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(m[r][c]))
        if abs(m[p][c]) < 1e-12:
            return None
        m[c], m[p] = m[p], m[c]
        for r in range(c + 1, n):
            f = m[r][c] / m[c][c]
            for k in range(c, n + 1):
                m[r][k] -= f * m[c][k]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x


def fit_predict(train_x, train_y, x_new, ridge=1e-6):
    """Ridge regression through the origin on standardized signals."""
    k = len(x_new)
    means = [sum(r[j] for r in train_x) / len(train_x) for j in range(k)]
    sds = []
    for j in range(k):
        v = sum((r[j] - means[j]) ** 2 for r in train_x) / len(train_x)
        sds.append(math.sqrt(v) or 1.0)
    z = [[(r[j] - means[j]) / sds[j] for j in range(k)] for r in train_x]
    zn = [(x_new[j] - means[j]) / sds[j] for j in range(k)]
    a = [[sum(z[i][p] * z[i][q] for i in range(len(z))) + (ridge if p == q else 0)
          for q in range(k)] for p in range(k)]
    b = [sum(z[i][p] * train_y[i] for i in range(len(z))) for p in range(k)]
    w = solve(a, b)
    if w is None:
        return 0.0
    return sum(w[j] * zn[j] for j in range(k))


def corr(x, y):
    n = len(x)
    if n < 3:
        return float("nan")
    mx, my = sum(x) / n, sum(y) / n
    sx = math.sqrt(sum((a - mx) ** 2 for a in x))
    sy = math.sqrt(sum((b - my) ** 2 for b in y))
    if sx == 0 or sy == 0:
        return float("nan")
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)


def load(path):
    rows = list(csv.DictReader(open(path)))
    cols = list(rows[0].keys())
    sig_names = [c for c in cols if c not in ("period", "actual", "baseline")]

    def num(s):
        s = (s or "").strip()
        return float(s) if s else None

    data = []
    for r in rows:
        data.append({"period": r["period"], "actual": num(r["actual"]),
                     "baseline": num(r.get("baseline")),
                     "sig": {n: num(r[n]) for n in sig_names}})
    return data, sig_names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--min-train", type=int, default=4)
    ap.add_argument("--max-combo", type=int, default=2)
    a = ap.parse_args()

    data, sig_names = load(a.csv)
    # fill missing baselines with the previous actual
    for i, d in enumerate(data):
        if d["baseline"] is None and i > 0 and data[i - 1]["actual"] is not None:
            d["baseline"] = data[i - 1]["actual"]
    rows = [d for d in data if d["actual"] is not None and d["baseline"] is not None]
    n = len(rows)
    print(f"{n} usable periods, {len(sig_names)} signals.")
    if n < 12:
        print("WARNING: fewer than 12 periods. Results below are NOT reliable - "
              "with so little data a signal can look good by luck. Use quarterly "
              "or monthly data to get more rows, and treat this as a rough filter only.")

    base_err = [abs(d["actual"] - d["baseline"]) for d in rows[a.min_train:]]
    if not base_err:
        print("Not enough rows for the minimum training size.")
        return
    base_mae = sum(base_err) / len(base_err)
    print(f"Baseline-only average miss (MAE) over {len(base_err)} test periods: {base_mae:,.2f}\n")

    results = []
    for k in range(1, a.max_combo + 1):
        for combo in itertools.combinations(sig_names, k):
            errs = []
            base_errs = []
            for t in range(a.min_train, n):
                train = [r for r in rows[:t] if all(r["sig"][c] is not None for c in combo)]
                cur = rows[t]
                if len(train) < a.min_train or any(cur["sig"][c] is None for c in combo):
                    continue
                tx = [[r["sig"][c] for c in combo] for r in train]
                ty = [r["actual"] - r["baseline"] for r in train]
                pred = fit_predict(tx, ty, [cur["sig"][c] for c in combo])
                errs.append(abs(cur["actual"] - (cur["baseline"] + pred)))
                base_errs.append(abs(cur["actual"] - cur["baseline"]))
            if len(errs) >= 3:
                # baseline error measured on the SAME periods this combo was tested on
                results.append((sum(errs) / len(errs), combo, len(errs),
                                sum(base_errs) / len(base_errs)))

    results.sort(key=lambda x: x[0] / x[3])
    print(f"{'signals':45s} {'MAE':>10s} {'vs baseline':>12s} {'tests':>6s}")
    for mae, combo, cnt, bmae in results[:15]:
        imp = (1 - mae / bmae) * 100
        flag = "  <- helps" if imp > 10 else ("  <- no help" if imp < 0 else "")
        print(f"{' + '.join(combo):45s} {mae:10.2f} {imp:+11.1f}% {cnt:6d}{flag}")

    print("\nOverlap check (signals that move together count as ONE signal):")
    for x, y in itertools.combinations(sig_names, 2):
        pairs = [(r["sig"][x], r["sig"][y]) for r in rows
                 if r["sig"][x] is not None and r["sig"][y] is not None]
        c = corr([p[0] for p in pairs], [p[1] for p in pairs])
        if not math.isnan(c) and abs(c) >= 0.7:
            print(f"  {x} ~ {y}: correlation {c:+.2f}  -> keep the better one")
    print("\nTip: a signal that only helps in a combo but not alone is suspicious.")


if __name__ == "__main__":
    main()
