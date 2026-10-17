# TODO (Phase 1: general model for all 3 companies)
Sumitomo-only list is saved in `companies/sumitomo/TODO.md` (paused).

## Key dates
| Date | What |
|---|---|
| Oct 28 | Interim task details |
| Nov 4 | Task 1 due: key business drivers (all companies? check the rules text) |
| Nov 5, 3:30pm JST | Sumitomo Q3 results |
| Nov 25, 23:59 | Interim task due (500 chars) |
| Dec 9 | Task 2: P&L model data |
| Jan 3, 2027, 23:59 | Main submission (Part 1: all 3 forecasts) |

## Step 1 - Check the starter model (this week)
- [ ] Run all three configs. Read each `notes` line; it says which inputs are guesses.
- [ ] For each company, open its English IR page and check 3 numbers from `DATA.md`.

## Step 2 - Fill the gaps in each DATA.md (section "Gaps")
- [ ] Sapporo: Domestic vs Overseas segment numbers (new basis); real estate gain timing.
- [ ] Skylark: FY21-FY24 history, monthly sales page.
- [ ] Sumitomo: see `companies/sumitomo/DATA.md` section 3.

## Step 3 - Build signal data (monthly/quarterly)
Why: you need 12+ rows per company for a backtest to mean anything.
- [ ] Skylark: monthly same-store sales and customers (company releases).
- [ ] Sapporo: monthly beer shipments, summer temperature (JMA).
- [ ] Sumitomo: US mortgage rate, USD/JPY, lumber, Japan monthly orders.
- [ ] Put them in each `backtest_data.csv`.

## Step 4 - Backtest and pick 1-2 signals per company
- [ ] Run `framework/backtest.py`. Keep signals that beat the baseline AND make sense.
- [ ] Write one paragraph per company: why does this signal matter for this company? (Your words, for the decision log.)

## Step 5 - Re-run Monte Carlo with what you learned
- [ ] Update config inputs. Stress test what breaks it.

## Step 6 - Back to the Sumitomo deep dive
- [ ] Resume `companies/sumitomo/TODO.md`.

## Ask Gyoseki (contact@gyoseki.com)
- [ ] How is the Consensus made? Is FY2026 or FY2027 scored?
