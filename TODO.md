# TODO (Phase 1: general model for all 3 companies)
Sumitomo-only list is saved in `companies/sumitomo/TODO.md` (paused).

## Key dates (updated Nov 5, 2026 from your Gyoseki deliverables page)
| Date | What |
|---|---|
| Nov 5, 3:30pm JST | Sumitomo Q3 results (update numbers) |
| Nov 25, 23:59 JST | Midterm Part 1: identify the key business drivers |
| Dec 16, 23:59 JST | Midterm Part 2: collect P&L model data |
| Jan 3, 2027, 23:59 JST | Main: Part 1 forecast operating income + net income for ALL 3 companies = (a) current FY2026 results and (b) NEXT FY (FY2027) company GUIDANCE. Part 2: pick one company; report (max 2,500 English words), model with P&L summary sheet, video under 3 min |
Note: older dates in this file (Nov 4 and Dec 9) came from an earlier read of the rules PDF and are replaced. Confirm the dates in the Gyoseki system.
Midterm results do not count toward the final score, but may be used to pick participants at the study-group venue.

IMPORTANT CHANGE: Part 1 asks for next year's company GUIDANCE (announced around Feb 2027), not next year's actual results. So you must also model HOW each company sets guidance (cautious or bold). Use the guidance-vs-actual history in each DATA.md.

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
