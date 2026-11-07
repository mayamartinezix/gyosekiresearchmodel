# Sapporo Holdings (2501) - Key business drivers (interim write-up notes)
STARTER DRAFT from our research. Rewrite every section in your own words and delete what you disagree with. The 500-character submission is a short summary of this page.
Keep the same 5 sections every time.

## 1. Sources (with period/date)
- Q2 2026 results, Q1 2026, FY2025 results, real estate sale news, medium-term plan 2027-2030 (see companies/sapporo/DATA.md)

## 2. How the company works (sales and costs)
- Domestic beer and drinks give most sales; Overseas (North America, Asia) about a quarter (estimate).
- Real estate is being sold and is now reported as discontinued.
- Costs: barley, aluminum cans, energy, marketing, US restructuring.
- Reports under IFRS: core operating profit (before one-offs), operating profit, net income.

## 3. Explicit KPIs (measures and targets the company states itself)
- Core operating profit (22.0B yen guided), domestic beer volume (+5% in H1), overseas Sapporo-brand volume (+15%)
- ROE target above 10% long term
- Restructuring (US, Stone brand transfer), Carlsberg partnership

## 4. Implicit KPIs (indicators I add, from ALT_DATA.md)
Lag and noise are my first guesses. Confirm them with `framework/backtest.py`, then keep the best 1-2.
Lag = how early it moves before the company's results. Noise = how much it jumps around for reasons unrelated to the company.

| Indicator | Why it matters (one line) | Source | How often | History? | Lag / lead | Noise | Pro | Con |
|---|---|---|---|---|---|---|---|---|
| Industry beer shipments | Domestic demand | Japan Brewers Association | monthly | Yes | Coincident to 1 month lead | Low | Clean, official | Industry, not Sapporo only |
| Summer temperature vs normal | Hot summers lift beer sales | JMA | daily | Yes | Coincident | Medium | Free, long history | Only matters for summer months |
| Aluminum price | Can cost | LME / FRED | daily | Yes | Leads costs by 1-6 months | Medium | Clear cost driver | Contracts and hedges delay it |
| Barley and energy prices | Input cost | Trade stats, METI | monthly | Yes | Leads costs by 1-6 months | Medium | Official | Weak link to profit |
| Rival results (Asahi, Kirin) | Market read | Their IR pages | quarterly | Yes | Coincident | Medium | Same market | Rivals' one-offs distort it |
| Photo log: shelf share, price tags | Share and pricing | You | weekly | No | Coincident | High | Original | No history; small sample |

## 5. Pros / advantages and cons / roadblocks
Pros:
- Core profit rising (+37% in H1); domestic volume up.
- Cash from the real estate sale for drinks growth and debt.
- Overseas brand growth; Carlsberg partnership.
- Brand strength in Japan.
Cons:
- Operating profit guided only 6.0B yen (restructuring, impairments).
- Net income dominated by a one-time gain (about 293B yen) - hard to forecast.
- Long-run decline of beer in Japan.
- US business is weak and being restructured.

## My own view (write this yourself, 3 sentences)
-
