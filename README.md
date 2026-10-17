# Gyoseki Research Model (Sumitomo Forestry 1911, Sapporo 2501, Skylark 3197)

**Status:** Phase 1 = general framework for all three companies. The Sumitomo deep dive is PAUSED (not deleted): see `companies/sumitomo/`.

## Where things are
- `OVERVIEW.md` - standing of each company, what can move it, what to test.
- `TODO.md` - current plan.
- `EVALUATE.md` - what to evaluate and how.
- `framework/` - Monte Carlo + stress test (`gyoseki_mc.py`) and backtest (`backtest.py`). See `framework/README.md`.
- `companies/<name>/` - `DATA.md` (public data and sources), `config.json` (model inputs), `backtest_data.csv` (template).
- `companies/sumitomo/` also keeps the earlier work: `DATA_CHECKLIST.md`, `TODO.md`, `assumptions.csv`, `monte_carlo.py`.

## Quick start
```
python3 framework/gyoseki_mc.py companies/sumitomo/config.json
python3 framework/gyoseki_mc.py companies/skylark/config.json
python3 framework/gyoseki_mc.py companies/sapporo/config.json
python3 framework/backtest.py framework/examples/synthetic_backtest.csv
```
No installs needed (Python 3).
