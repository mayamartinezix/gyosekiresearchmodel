# Master alt data list (all 3 companies)
Gathered Oct 19, 2026. Trim later using the backtest (`framework/backtest.py`).
Columns: **History?** = free past data exists (can be backtested). **★** = my pick to keep first.
"Cluster" groups signals that likely move together (demand, cost, macro, qualitative). Keep 1-2 per cluster.
Source names are where to look; check each site's terms before collecting automatically.

## Skylark (3197)
| ★ | Signal | Cluster | History? | Frequency | Where |
|---|---|---|---|---|---|
| ★ | Skylark monthly sales (same-store sales, customers, spend) | demand | Yes | monthly | Skylark IR / TDnet releases |
| ★ | Japan Foodservice Association family-restaurant sales | demand | Yes | monthly | JF website |
| | Peer monthly sales (Saizeriya, Zensho) | demand | Yes | monthly | their IR pages |
| ★ | Job postings: posted hourly wage and number of jobs | cost | No (start now) | weekly | public job sites |
| | Minimum wage / wage index | cost | Yes | yearly/monthly | MHLW, e-Stat |
| ★ | Rice, beef, egg, oil wholesale/retail prices | cost | Yes | monthly | MAFF, e-Stat |
| | Beef/chicken import prices | cost | Yes | monthly | customs data (e-Stat) |
| | Inbound tourist arrivals | demand | Yes | monthly | JNTO |
| | Weather (heat, typhoons) | demand | Yes | daily | JMA |
| | Google Maps / Tabelog ratings and review counts (fixed stores) | qualitative | Limited | monthly | Google Maps, Tabelog |
| | Photo log: menu prices, queues, promotions | qualitative | No (start now) | weekly | you (`framework/PHOTO_LOG.md`) |
| | Rankings/point campaigns (restaurant deals on point apps) | demand | Limited | monthly | point apps, deal sites |
| | EDINET filings / securities reports | company | Yes | quarterly | EDINET |
| | Patents/trademarks (new brands, concepts) | qualitative | Yes | monthly | J-PlatPat |
| | Wording of the outlook text each quarter | qualitative | Yes | quarterly | results releases |
| | Consumer confidence, real wages, CPI | macro | Yes | monthly | Cabinet Office, MIC |
| | Yen (import costs) | macro | Yes | daily | FRED / BOJ |

## Sapporo (2501)
| ★ | Signal | Cluster | History? | Frequency | Where |
|---|---|---|---|---|---|
| ★ | Industry beer-type shipments | demand | Yes | monthly | Japan Brewers Association |
| ★ | Summer temperature vs normal | demand | Yes | daily | JMA |
| | Calendar effect (weekends/holidays per month) | demand | Yes | monthly | calendar |
| | Rivals' results (Asahi, Kirin) | demand | Yes | quarterly | their IR pages |
| ★ | Aluminum price | cost | Yes | daily | LME / FRED |
| | Barley and hop prices | cost | Yes | monthly | agriculture data, trade stats |
| | Electricity and gas prices, freight rates | cost | Yes | monthly | METI, shipping indices |
| | Packaging/can makers' price-rise notices | cost | Yes | irregular | their IR pages |
| | Google Trends: beer, brand names | demand | Yes | weekly | Google Trends |
| | Photo log: shelf share, price tags, draft taps | qualitative | No (start now) | weekly | you (`framework/PHOTO_LOG.md`) |
| | Rankings/point campaigns | demand | Limited | monthly | point apps |
| | Import/export data (beer exports to US/Asia) | demand | Yes | monthly | customs data (e-Stat) |
| | Real estate sale: stage and gain timing | company | Yes | event | Sapporo releases, EDINET |
| | Patents/trademarks | qualitative | Yes | monthly | J-PlatPat |
| | Yen, USD/JPY | macro | Yes | daily | FRED / BOJ |

## Sumitomo Forestry (1911)
| ★ | Signal | Cluster | History? | Frequency | Where |
|---|---|---|---|---|---|
| ★ | Japan monthly orders and backlog | demand | Yes | monthly | Sumitomo Forestry IR (monthly orders page) |
| | Japan housing starts (owner-built) | demand | Yes | monthly | MLIT |
| | Japan fixed home-loan rate (Flat 35) | macro | Yes | monthly | Japan Housing Finance Agency |
| ★ | US 30-year mortgage rate | macro | Yes | weekly | FRED (Freddie Mac) |
| | US builder confidence | demand | Yes | monthly | NAHB |
| | US mortgage applications | demand | Yes | weekly | MBA |
| | US new-home months of supply | demand | Yes | monthly | Census |
| | Peer builders' orders and cancellation rates (D.R. Horton, Lennar) | demand | Yes | quarterly | their IR pages |
| | Australia building approvals, central bank rate | demand | Yes | monthly | ABS, RBA |
| ★ | Lumber price (US futures) | cost | Yes | daily | Trading Economics / CME |
| | Bank of Japan wood price index | cost | Yes | monthly | BOJ |
| | Equipment makers' price-rise notices (LIXIL, TOTO, YKK AP, Panasonic) | cost | Yes | irregular | their IR pages |
| | Lumber producers' results (West Fraser, Weyerhaeuser, etc.) | cost/demand | Yes | quarterly | their IR pages |
| | Carpenter/construction labor shortage | cost | Yes | monthly | MLIT, MHLW |
| | US tariffs and duties on lumber | policy | Yes | event | US government notices |
| | USD/JPY, AUD/JPY | macro | Yes | daily | FRED / BOJ |
| | Google Earth old photos: Tri Pointe / sawmill / site progress | qualitative | Limited | occasional | Google Earth |
| | Family photo log: US communities (every 2 weeks) | qualitative | No (start now) | biweekly | family (`framework/PHOTO_LOG.md`) |
| | Housing exhibition park visit (Japan) | qualitative | No (start now) | monthly | you |
| | Google Trends: new homes | demand | Yes | weekly | Google Trends |
| | EDINET filings, patents (wood tech) | company | Yes | quarterly | EDINET, J-PlatPat |

## Dropped
- Online media scraping, and job postings for Sumitomo/Sapporo (kept only for Skylark).

## Rules for trimming
1. Write one line first: "this signal should move [driver] because [reason]".
2. Backtest. Drop anything that doesn't beat the baseline.
3. If two signals in a cluster move together, keep the better one.
4. Items marked "No (start now)" cannot be backtested. Use them only as a forward check.
