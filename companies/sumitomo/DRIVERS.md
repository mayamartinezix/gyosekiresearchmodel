# Sumitomo Forestry (1911) - Key business drivers (interim write-up notes)
STARTER DRAFT from our research. Rewrite every section in your own words and delete what you disagree with. The 500-character submission is a short summary of this page.
Keep the same 5 sections every time.

## 1. Sources (with period/date)
- Q2 FY2026 Factbook (Aug 2026), Q2 briefing, Q2 analyst Q&A, Integrated Report 2026 (see companies/sumitomo/DATA.md for links)
- Q3 FY2026 materials (released Nov 5) - add

## 2. How the company works (sales and costs)
- Overseas Housing is about 79% of FY25 recurring income: US homes sold x price (now including Tri Pointe), plus Australia.
- Japan Housing: custom-home orders x price per home, delivered after construction (backlog about 399B yen).
- Also timber and building materials, real estate development, forestry/environment.
- Costs: lumber and materials, labor, US buyer incentives, Tri Pointe goodwill (about 10B yen a year) and interest (about 17B yen a year).

## 3. Explicit KPIs (measures and targets the company states itself)
- US: units sold (14,160 planned), average price (about US$520k), orders and backlog, incentive ratio (8.2%), absorption (sales per community per month, 2.4 vs 2.5 target), communities (398 planned)
- Australia: units sold (8,070 planned), target 10,000 units in 2030
- Japan: orders, units, price per home (about 48M yen)
- Targets: 1M hectares of forest, 1M m3 of Japanese timber by 2030

## 4. Implicit KPIs (indicators I add, from ALT_DATA.md)
Lag and noise are my first guesses. Confirm them with `framework/backtest.py`, then keep the best 1-2.
Lag = how early it moves before the company's results. Noise = how much it jumps around for reasons unrelated to the company.

| Indicator | Why it matters (one line) | Source | How often | History? | Lag / lead | Noise | Pro | Con |
|---|---|---|---|---|---|---|---|---|
| US 30-year mortgage rate | Higher rate = fewer US buyers, more incentives | FRED (Freddie Mac) | weekly | Yes | Leads US orders by 1-3 months | Low | Easy, clean, long history | Only one side of demand |
| Japan monthly orders and backlog | Orders today become sales in 6-12 months | Sumitomo Forestry IR | monthly | Yes | Leads Japan sales by 6-12 months | Low | Direct, company-specific | Japan is a smaller profit share |
| Lumber price | Moves material cost and timber profit | Futures (Trading Economics) | daily | Yes | Coincident to 3-month lead | Medium | Daily, long history | Company hedging/contracts blur the link |
| USD/JPY, AUD/JPY | Converts overseas profit into yen | FRED / BOJ | daily | Yes | Coincident | Medium | Directly in the numbers | Hard to forecast itself |
| Peer US builders' orders and cancellations | Early read on US demand and pricing | Peers' IR pages | quarterly | Yes | Leads by 0-1 quarter | Medium | Same market | Only a few data points a year |
| Family photo log (US communities) | Sold signs, incentives, traffic | Family | every 2 weeks | No | Coincident | High | Real-time, original | No history; small sample |

## 5. Pros / advantages and cons / roadblocks
Pros:
- Profit is spread across the US, Australia, and Japan.
- Japan orders up 14 months in a row; US backlog up (2,346 to 4,699 units, Dec to Jun).
- Weak yen lifts reported profit.
- Long-term forest and carbon strategy.
Cons:
- US profit margin falling (13.4% to 8.2%), more incentives, lower prices.
- Debt about 1.6T yen after Tri Pointe; interest and goodwill costs.
- US mortgage rate 7.4%, higher than the company's August view.
- US sawmill still losing money.
- Guidance cut in August in both FY25 and FY26.

## My own view (write this yourself, 3 sentences)
-
