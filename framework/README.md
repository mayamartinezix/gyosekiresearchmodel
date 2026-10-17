# Framework (works for any company)

## 1. Monte Carlo + stress test
`python3 framework/gyoseki_mc.py companies/skylark/config.json`
- Reads one `config.json` per company (segments, growth, margins, currency, one-offs, tax).
- Prints a range (5th to 95th percentile) for revenue, profit, and net income.
- Runs the stress tests listed in the config and shows how each changes the range.
- `P(>guide)`: share of simulated years above the company's own guidance.
- Options: `--n 20000` (more draws), `--seed 2`, `--json out.json`.

## 2. Backtest
`python3 framework/backtest.py companies/<name>/backtest_data.csv`
- Tests which signals (alt data) or pairs of signals would have improved on a baseline guess, using only past data at each step.
- Flags signals that are copies of each other.
- Try it now on `framework/examples/synthetic_backtest.csv` (FAKE data: signal A truly works, B is noise, C copies A).

## How to use the two together (your plan)
1. Collect quarterly/monthly signals and actuals into `backtest_data.csv`.
2. Backtest. Keep the 1-2 signals that help.
3. Put what they tell you into the config (for example a better volume growth), and rerun the Monte Carlo.
4. Stress test what breaks the result.
5. For Sumitomo, go deeper on the signals that survived.

## Honest limits
- Annual data gives only 3-5 rows. Backtests on that are weak. Use quarterly or monthly data.
- Starter configs are calibrated to company guidance, so the BASE median equals the company's view. Your edge comes from changing the inputs.
- Segment splits for Sapporo are estimates until you pull the segment note.
