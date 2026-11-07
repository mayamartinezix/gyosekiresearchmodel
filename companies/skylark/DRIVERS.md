# Skylark Holdings (3197) - Key business drivers (interim write-up notes)
STARTER DRAFT from our research. Rewrite every section in your own words and delete what you disagree with. The 500-character submission is a short summary of this page.
Keep the same 5 sections every time.

## 1. Sources (with period/date)
- Q2 FY2026 results (Aug 13, 2026), Q1 FY2026, FY2025 results, monthly sales releases (see companies/skylark/DATA.md)

## 2. How the company works (sales and costs)
- All sales are restaurants (Gusto, Bamiyan, Shabu-yo and others): stores x customers x average spend.
- Growth from new stores, brand conversions, price rises, and acquisitions (Shinpachi Shokudo).
- Costs: food, labor (rising), rent, utilities.
- Reports under IFRS: business profit (before one-offs) and operating profit.

## 3. Explicit KPIs (measures and targets the company states itself)
- Same-store sales (+6% planned; +6.5% in H1), customers (+1.6%), average spend (+4.8%)
- Store count (3,214), new stores (80), brand conversions (50), remodels (230-240)
- Medium-term: same-store growth 3-4% a year (third-party summary, verify)

## 4. Implicit KPIs (indicators I add, from ALT_DATA.md)
Lag and noise are my first guesses. Confirm them with `framework/backtest.py`, then keep the best 1-2.
Lag = how early it moves before the company's results. Noise = how much it jumps around for reasons unrelated to the company.

| Indicator | Why it matters (one line) | Source | How often | History? | Lag / lead | Noise | Pro | Con |
|---|---|---|---|---|---|---|---|---|
| Skylark monthly sales and customers | Early read on quarterly results | Company releases | monthly | Yes | Leads results by 0-3 months | Low | Direct and company-specific | Already public, so others use it too |
| Industry family-restaurant sales (JF) | Shows whether Skylark beats the market | JF | monthly | Yes | Coincident | Low | Clean benchmark | Industry, not company |
| Job postings: wage and openings | Early sign of wage cost pressure | Public job sites | weekly | No (start now) | Leads costs by 1-6 months | High | Unusual, forward-looking | No history; site terms to check |
| Rice/beef/oil prices | Food cost pressure | MAFF / e-Stat | monthly | Yes | Leads costs by 1-3 months | Medium | Official, long history | Company contracts delay the effect |
| Minimum wage | Labor cost step-up | MHLW | yearly | Yes | Known in advance | Low | Predictable | Only one data point a year |
| Photo log: menu prices, queues | Price changes and traffic | You | weekly | No | Coincident | High | Original, visible | Small sample; no history |

## 5. Pros / advantages and cons / roadblocks
Pros:
- Growing sales and profit; guidance raised in Aug 2026.
- Has beaten its own guidance (FY25).
- Many stores and brands; acquisitions add growth.
- Simple, single segment.
Cons:
- Wage and food cost inflation (staff costs +3.3B yen in Q1).
- Price rises may not be accepted by customers.
- Acquisition integration and debt.
- Weather and consumer mood.

## My own view (write this yourself, 3 sentences)
-
