"""Simple Monte Carlo for Sumitomo Forestry. Pure Python, no installs.
Run: python3 monte_carlo.py
All numbers in assumptions.csv are PLACEHOLDERS until you replace them."""
import csv, random, statistics

N = 10000                      # number of simulated years
FX_BASE, FX_SD = 150.0, 8.0    # yen per US$ (placeholder)
random.seed(1)

rows = list(csv.DictReader(open("assumptions.csv")))
results = []
for _ in range(N):
    fx = random.gauss(FX_BASE, FX_SD)       # ONE fx draw shared by all segments
    fx_scale = fx / FX_BASE
    total = 0.0
    for r in rows:
        units = random.gauss(float(r["units_mean"]), float(r["units_sd"]))
        price = random.gauss(float(r["price_mean_million_yen"]), float(r["price_sd_million_yen"]))
        margin = random.gauss(float(r["margin_mean"]), float(r["margin_sd"]))
        sales = units * price                # million yen
        if r["fx_sensitive"] == "1":
            sales *= fx_scale                # weaker yen -> more yen sales
        total += sales * margin
    results.append(total / 1000)             # billion yen

results.sort()
pct = lambda p: results[int(p / 100 * N) - 1]
print("Recurring income (billion yen) - PLACEHOLDER INPUTS")
for p in (5, 25, 50, 75, 95):
    print(f"  {p}th percentile: {pct(p):.1f}")
print(f"  mean: {statistics.mean(results):.1f}  stdev: {statistics.stdev(results):.1f}")
