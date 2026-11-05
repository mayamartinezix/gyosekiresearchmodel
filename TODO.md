# TODO (Phase 1: general model for all 3 companies)
Sumitomo-only list is saved in `companies/sumitomo/TODO.md` (paused).

## Key dates (CONFIRMED from the official rules v2, last updated Oct 28, 2026)
| Date (JST) | What |
|---|---|
| Nov 5, 3:30pm | Sumitomo Q3 results (update numbers) |
| Nov 11, 5:00pm | Workshop: Case Study with Fortress (hybrid) |
| Nov 25, 23:59 | Midterm Part 1 due: identify the key business drivers |
| Nov 25, 5:00pm | Workshop: Quantitative basics with Pronexus (online) |
| Dec 2, 5:00pm | Workshop: Communication with BlackRock (online) |
| Dec 3, 6:00pm | Workshop: Industry Map with Toyo Keizai (hybrid) |
| Dec 9, 5:00pm | Workshop: Alternative data with Nowcast (online) |
| Dec 11, 5:00pm | Workshop: Stock study with UBS (hybrid) |
| Dec 16, 23:59 | Midterm Part 2 due: collect P&L model data |
| Dec 16, 6:00pm | Workshop: Advanced quantitative / wrap-up (online) |
| Jan 3, 2027, 23:59 | Main submission |
| Mid-Feb / late Feb | Qualifying results / finalists announced |
| Mar 5 -> Mar 7 | Wildcard submission -> results |
| Mar 12 (Fri) | Final, in person |

Already passed: Oct 28 qualitative workshop (Saizeriya) and Nov 4 Point72 workshop. The old Nov 4 and Dec 9 task dates are gone (they were in the older Aug 20 rules).
Midterm tasks are considered for the interim selection (past finalists exempt).

## What the Jan 3 main submission asks
- Part 1: forecast operating income and net income for ALL 3 companies: this year's (FY2026) results AND next year's (FY2027) company GUIDANCE.
- Part 2: pick one company. Report (max 2,500 English words), financial model with P&L summary sheet, video under 3 minutes.
- Report scoring (earnings forecast = 40%): key revenue drivers, assumptions backed by data, a forecast of the company's INITIAL FY2027 guidance, and how you differ from guidance and consensus.
- So you must model HOW each company sets guidance (cautious or bold). Use the guidance-vs-actual history in each DATA.md.

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
