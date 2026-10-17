# TODO - Sumitomo Forestry (1911) model
Each item: what to do, why, and where to look. Data collected so far is in `DATA.md`.

## Key dates
| Date | What |
|---|---|
| Oct 21 | Workshop (from earlier notes - confirm) |
| Oct 28 | Interim task details released |
| Nov 4 | Task 1 due: key business drivers |
| Nov 5, 3:30pm JST | Company Q3 results - update numbers |
| Nov 25, 23:59 | Interim task due (500 chars) |
| Dec 9 | Task 2 due: P&L model data |
| Jan 3, 2027, 23:59 | Main submission |

## 1. This week
- [ ] **Check DATA.md against the Factbook.**
  Why: I read the PDFs through a summarizer, so a number could be wrong.
  Where: [Factbook](https://sfc.jp/english/ir/library/statements/pdf/Factbook_20260810.pdf)
- [ ] **Fill the missing data (DATA.md section 3).** Segment history FY21-24, quarterly numbers.
  Why: you need 5 years of history to see trends.
  Where: [Segment page](https://sfc.jp/english/ir/zaimu/segment/), [Monthly Japan orders](https://sfc.jp/english/ir/zaimu/order/), [Highlights](https://sfc.jp/english/ir/zaimu/highlight/). These load in a browser, not for me.
- [ ] **Send Claude the text of "About Study Group & Interim Assignments".**
  Why: it says exactly what the interim task wants.
- [ ] **Read the Q2 briefing and Q&A once.** They explain why the forecast was cut.
  Where: [Briefing](https://sfc.jp/english/ir/library/statements/pdf/2026_2q_strategy_02_en.pdf), [Q&A](https://sfc.jp/english/ir/library/statements/pdf/2026_2q_qanda_en.pdf)

## 2. Task 1 (due Nov 4): key business drivers
A driver = a thing that moves sales or profit (example: number of US homes sold).
- [ ] List 3-5 drivers per segment. Start with Overseas Housing (about 79% of profit).
- [ ] Write why each matters, in your own words.
- [ ] Add one chart or table per driver.
- [ ] Draft the Tri Pointe section: goodwill about 10B yen/year, interest about 17B/year, fair-value write-off 19.7B this year then about 5B.

## 3. Questions to answer in your model
Why: these are where the company's numbers are unclear.
- [ ] Why does net income fall to 52% of recurring income in FY26F (was 56-64%)? Tax? Minority share?
- [ ] Is the US recovery really coming in 2027, with a mortgage rate of 7.4%? (Company said "mid-6%" in August.)
- [ ] Will the US sawmill turn profitable in Q4?
- [ ] Will incentives rise further in the US (8.2% now)?
- [ ] Do the 10 postponed US property sales happen next year?

## 4. Build the model (Google Sheets)
- [ ] Sheets in this order: Assumptions, Historicals, Revenue build, P&L, Scenarios.
- [ ] Revenue = units x price per unit (per segment).
- [ ] Bear / base / bull toggle.
- [ ] Replace placeholders in `assumptions.csv`, then run `python3 monte_carlo.py`.
  Why: it shows a range of results, not one number.
- [ ] Add check rows (totals must match the company's).
Colors: actuals blue, formulas black, assumptions green. This is a rule in the competition.

## 5. Test alt data
Alt data = non-standard signals (rankings, trade data, etc.).
- [ ] Pick 3-5 sources from your notebook.
- [ ] Test each against FY21-25 results. Keep only those that predict well.
- [ ] Log scores in `EVALUATE.md`.

## 6. Competition habits
- [ ] **Decision log:** each assumption plus why, in your own words.
  Why: judges penalize unexplained AI use.
- [ ] **Risk section:** what could break your thesis.
- [ ] **Source every number** (cell comment with link).
- [ ] **Email contact@gyoseki.com:** how is the Consensus made? Is FY2026 or FY2027 scored?

## 7. Not collected yet (DATA_CHECKLIST sections 3-4)
- [ ] Policy: Section 232 US lumber tariffs, EU deforestation rule, Japan housing rules, Australia housing.
- [ ] Gyoseki Consensus (once visible on the platform).
