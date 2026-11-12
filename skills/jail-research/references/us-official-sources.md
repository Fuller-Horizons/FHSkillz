# US official sources — claim class to best source

Use this map in Step 1 to name the likely best source for each question
before searching. It lists sources only; it carries no statistics. Open the
source this session, cite it with a date accessed, and state the data vintage
(reference year or release) of every figure you use. A source marked
**licensed** is a paid benchmark: use it only if the user or client already
has access, and say so in the packet. If the source cannot be opened this
session, the claim is Unknown and the resolver is the dataset named here.

Tier 1 = the client's own first-party data (see the last section). Tier 2 =
official government source. Tier 3 = licensed commercial benchmark.

Pairing tip: count questions ("how many firms?") usually need two sources
that cover different populations, for example employer firms and firms with
no employees, so name which population each figure covers.


## Market size and firm counts

| Source | What it answers | Access / cost | URL |
|---|---|---|---|
| County Business Patterns — U.S. Census Bureau | Establishments, employment, payroll by NAICS, county, ZIP | API / download; Free; Free key | https://www.census.gov/programs-surveys/cbp.html |
| Nonemployer Statistics — U.S. Census Bureau | Count and receipts of businesses with no employees | API / download; Free; Free key | https://www.census.gov/programs-surveys/nonemployer-statistics.html |
| Annual Business Survey — U.S. Census Bureau | Owner characteristics, technology/AI adoption, innovation, R&D | API / download; Free; Free key | https://www.census.gov/programs-surveys/abs.html |
| Economic Census — U.S. Census Bureau | Revenue, product lines, costs by NAICS and geography (every 5 yrs) | API / download; Free; Free key | https://www.census.gov/programs-surveys/economic-census.html |
| Business Formation Statistics — U.S. Census Bureau | New business applications - new-entrant pressure | Download; Free; None | https://www.census.gov/econ/bfs/index.html |
| Business Trends and Outlook Survey — U.S. Census Bureau | Biweekly business conditions, outlook, AI use by sector | Download; Free; None | https://www.census.gov/hfp/btos |
| NAICS code lookup — U.S. Census Bureau | Industry classification to join all datasets | Web; Free; None | https://www.census.gov/naics/ |
| SBA Office of Advocacy research — U.S. Small Business Administration | Small business profiles, survival rates, research | Web; Free; None | https://advocacy.sba.gov/ |
| SBA Size Standards — U.S. Small Business Administration | Official small-business definitions by NAICS | Web; Free; None | https://www.sba.gov/federal-contracting/contracting-guide/size-standards |
| IBISWorld industry reports — IBISWorld (licensed) | Industry size, growth, competition, key success factors | Subscription; Paid (often free via library); Account | https://www.ibisworld.com/ |
| BizMiner industry financial profiles — BizMiner (licensed) | Industry P&L/balance-sheet benchmarks incl. small firms | Subscription; Paid; Account | https://www.bizminer.com/ |
| DealStats — Business Valuation Resources (licensed) | Private-company sale multiples and deal terms | Subscription; Paid; Account | https://www.bvresources.com/products/dealstats |

## Employment, wages, and labor

| Source | What it answers | Access / cost | URL |
|---|---|---|---|
| Quarterly Census of Employment & Wages — Bureau of Labor Statistics | Employment and wages by industry and county | API / download; Free; None | https://www.bls.gov/cew/ |
| Occupational Employment & Wage Statistics — Bureau of Labor Statistics | Wages by occupation and metro - comp benchmarking | Download; Free; None | https://www.bls.gov/oes/ |
| Job Openings & Labor Turnover Survey — Bureau of Labor Statistics | Quit, hire, separation rates by industry - turnover benchmark | API; Free; Free key | https://www.bls.gov/jlt/ |
| National Compensation Survey (benefits) — Bureau of Labor Statistics | Benefit costs and access by industry and size | Download; Free; None | https://www.bls.gov/ncs/ |
| BLS Productivity statistics — Bureau of Labor Statistics | Labor productivity by industry | Download; Free; None | https://www.bls.gov/productivity/ |
| O*NET Web Services — U.S. DOL / O*NET | Tasks, skills, knowledge by occupation - job design and training | API; Free; Free registration | https://services.onetcenter.org/ |
| BLS Public Data API — Bureau of Labor Statistics | Programmatic access to all BLS series | API; Free; Free v2 key | https://www.bls.gov/developers/ |

## Prices and inflation

| Source | What it answers | Access / cost | URL |
|---|---|---|---|
| Consumer & Producer Price Indexes — Bureau of Labor Statistics | Inflation for customers (CPI) and inputs (PPI) | API; Free; Free key | https://www.bls.gov/ppi/ |
| BEA API — Bureau of Economic Analysis | GDP by industry and state, personal income by county | API; Free; Free key | https://apps.bea.gov/api/ |
| FRED API — Federal Reserve Bank of St. Louis | 800k+ macro series: rates, credit, sales, sentiment | API; Free; Free key | https://fred.stlouisfed.org/docs/api/fred/ |

## Macro and rates

| Source | What it answers | Access / cost | URL |
|---|---|---|---|
| FRED API — Federal Reserve Bank of St. Louis | 800k+ macro series: rates, credit, sales, sentiment | API; Free; Free key | https://fred.stlouisfed.org/docs/api/fred/ |
| BEA API — Bureau of Economic Analysis | GDP by industry and state, personal income by county | API; Free; Free key | https://apps.bea.gov/api/ |
| Treasury interest rate data — U.S. Treasury | Risk-free rate (yield curve) for WACC and DCF | Download / API; Free; None | https://home.treasury.gov/resource-center/data-chart-center/interest-rates |

## Public-company financials

| Source | What it answers | Access / cost | URL |
|---|---|---|---|
| SEC EDGAR APIs (data.sec.gov) — U.S. SEC | Public-company filings and XBRL financials for peers | API; Free; No key; User-Agent header required | https://www.sec.gov/search-filings/edgar-application-programming-interfaces |
| EDGAR full-text search — U.S. SEC | Search 10-Ks for competitor, risk and market language | Web; Free; None | https://www.sec.gov/edgar/search/ |
| Quarterly Financial Report — U.S. Census Bureau | Industry income statements and balance-sheet ratios | Download; Free; None | https://www.census.gov/econ/qfr/ |
| Annual Capital Expenditures Survey — U.S. Census Bureau | Capex by industry and asset type | Download; Free; None | https://www.census.gov/programs-surveys/aces.html |

## Regulation and enforcement

| Source | What it answers | Access / cost | URL |
|---|---|---|---|
| Federal Register API — National Archives (OFR) | Proposed and final rules, notices - regulatory change | API; Free; None | https://www.federalregister.gov/developers/documentation/api/v1 |
| eCFR API — National Archives (OFR) | Current text of federal regulations | API; Free; None | https://www.ecfr.gov/developers/documentation/api/v1 |
| Regulations.gov API — GSA | Rulemaking dockets and public comments | API; Free; Free key | https://open.gsa.gov/api/regulationsgov/ |
| DOL Open Data Portal (OSHA, WHD enforcement) — U.S. Department of Labor | OSHA inspections/violations, wage & hour cases by employer | API; Free; Free key | https://dataportal.dol.gov/ |
| EPA ECHO web services — U.S. EPA | Environmental compliance and enforcement by facility | API; Free; None | https://echo.epa.gov/tools/web-services |
| CFPB Consumer Complaint Database API — CFPB | Consumer complaints against financial companies | API; Free; None | https://cfpb.github.io/api/ccdb/ |
| FTC Business Guidance — Federal Trade Commission | Advertising, endorsement, privacy and Safeguards Rule guidance | Web; Free; None | https://www.ftc.gov/business-guidance |
| HHS HIPAA guidance — U.S. HHS | Privacy and Security Rule requirements | Web; Free; None | https://www.hhs.gov/hipaa/for-professionals/index.html |
| OFAC Sanctions List Search — U.S. Treasury | Sanctioned parties screening for vendors and partners | Web / download; Free; None | https://sanctionssearch.ofac.treas.gov/ |
| National Vulnerability Database API — NIST | Known vulnerabilities (CVEs) by product | API; Free; Free key | https://nvd.nist.gov/developers |
| CISA Known Exploited Vulnerabilities — CISA | Vulnerabilities actively exploited - patch priority | Download; Free; None | https://www.cisa.gov/known-exploited-vulnerabilities-catalog |
| PCAOB auditing standards — PCAOB | Internal control over financial reporting (SOX) standards | Web; Free; None | https://pcaobus.org/ |
| DOJ Fraud Section (FCPA guide, compliance program evaluation) — U.S. Department of Justice | FCPA guidance and how DOJ evaluates compliance programs | Web; Free; None | https://www.justice.gov/criminal/criminal-fraud |

## Intellectual property

| Source | What it answers | Access / cost | URL |
|---|---|---|---|
| USPTO Open Data Portal API — U.S. Patent and Trademark Office | Patents and trademarks - IP and innovation intel | API; Free; Free key | https://data.uspto.gov/apis/getting-started |

## Federal contracts and entity records

| Source | What it answers | Access / cost | URL |
|---|---|---|---|
| USAspending API — U.S. Treasury | Federal contract and grant awards by company/NAICS | API; Free; None | https://api.usaspending.gov/ |
| SAM.gov Entity API — GSA | Federal contractor registrations, exclusions | API; Free; Free key | https://open.gsa.gov/api/entity-api/ |
| State Secretary of State business search — Each state (directory via NASS) | Entity status, officers, UCC liens | Web; Free; None | https://www.nass.org/ |

## Small-business finance

| Source | What it answers | Access / cost | URL |
|---|---|---|---|
| Small Business Credit Survey — Federal Reserve Banks | SMB financial health, financing, top challenges | Download; Free; None | https://www.fedsmallbusiness.org/ |
| IRS Statistics of Income — Internal Revenue Service | Business tax-return aggregates by industry and size | Download; Free; None | https://www.irs.gov/statistics |
| QuickBooks Online / Xero Accounting APIs — Intuit / Xero | GL, P&L, balance sheet, AR/AP aging, invoices | API (OAuth); Free API; client subscription; OAuth, read-only scope | https://developer.intuit.com/app/developer/qbo/docs/get-started |
| RMA eStatement Studies — Risk Management Association (licensed) | SMB financial ratios by NAICS and revenue size | Subscription; Paid; Account | https://www.rmahq.org/estatement-studies/ |
| BizMiner industry financial profiles — BizMiner (licensed) | Industry P&L/balance-sheet benchmarks incl. small firms | Subscription; Paid; Account | https://www.bizminer.com/ |
| DealStats — Business Valuation Resources (licensed) | Private-company sale multiples and deal terms | Subscription; Paid; Account | https://www.bvresources.com/products/dealstats |

## Customer and demographic sizing

| Source | What it answers | Access / cost | URL |
|---|---|---|---|
| American Community Survey — U.S. Census Bureau | Population, income, households, commuting - customer sizing | API / download; Free; Free key | https://www.census.gov/programs-surveys/acs |
| Data.gov catalog — GSA | Find any other federal dataset | Web / API; Free; None | https://catalog.data.gov/ |

## Client first-party data (Tier 1, needs client consent)

| Source | What it answers | Access / cost | URL |
|---|---|---|---|
| Client document repository | Plans, contracts, SOPs, reports, emails | Connector / upload; Free; Client consent | https://developers.google.com/drive |
| QuickBooks Online / Xero Accounting APIs | GL, P&L, balance sheet, AR/AP aging, invoices | API (OAuth); Free API; client subscription; OAuth, read-only scope | https://developer.intuit.com/app/developer/qbo/docs/get-started |
| Client CRM API (HubSpot, Salesforce) | Contacts, deals, stages, activities, win/loss | API (OAuth/private app); Free API; client subscription; Read-only private app token | https://developers.hubspot.com/ |
| Stripe / Shopify commerce APIs | Transactions, subscriptions, MRR, churn, orders, products | API; Free API; client subscription; Restricted read-only key | https://docs.stripe.com/api |
| Payroll / HRIS export (Gusto, ADP, Paychex) | Headcount, tenure, comp, turnover | API / export; Client subscription; Admin export, PII minimized | https://docs.gusto.com/ |
| Google Analytics 4 Data API | Traffic, sources, conversions, landing pages | API; Free; Read-only service account | https://developers.google.com/analytics/devguides/reporting/data/v1 |
| Google Search Console API | Search queries, impressions, clicks, rankings | API; Free; Read-only user | https://developers.google.com/webmaster-tools |

Manual fallback: if no live search is available, copy the row for the claim class into the packet as the resolver of each Unknown.
