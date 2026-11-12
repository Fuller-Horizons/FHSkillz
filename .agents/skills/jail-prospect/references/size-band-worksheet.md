# Size-Band Worksheet — method only

Purpose: an **indicative size band** for a private company, built from public proxies. It is
**NOT a valuation** and not the company's revenue. This file gives a method and sources, not numbers.
Never write a revenue or EBITDA figure as a Fact. Actual financials stay **Unknown** (private company).

## Step 1 — Pick the NAICS code
Use the code from entity resolution (Stage 1). If two codes fit, run the band for both and report the wider one.

## Step 2 — Find a revenue-per-worker benchmark (pick one, record which)
Read the figure from the source table yourself. Do not recall it from memory.
| Company type | Source | What to pull | URL |
|---|---|---|---|
| Has paid employees | Economic Census (every 5 years; 2022 is the latest listed on the page, checked 2026-11-12) | Sales/receipts and number of employees for the NAICS code. Divide to get sales per employee. | https://www.census.gov/programs-surveys/economic-census.html |
| No paid employees (sole owner) | Nonemployer Statistics | Receipts and number of establishments. Divide to get receipts per establishment. | https://www.census.gov/programs-surveys/nonemployer-statistics.html |
| Employee counts by size class | SUSB (employment, payroll, firms by enterprise size) | Use to check the headcount class is typical for the NAICS code. It does not list receipts on its program page. | https://www.census.gov/programs-surveys/susb.html |
| Cross-check only | County Business Patterns (establishments, employment, payroll; no revenue) | Payroll per employee as a sanity check on the headcount. | https://www.census.gov/programs-surveys/cbp.html |

Label the benchmark **Fact** (a published table value, with table name, year, and access date). Its use for this
company is an **Estimate**, because the average firm is not this firm.

## Step 3 — Bound the headcount
Record a low and a high, each with its source and label.
- **Upper bound:** LinkedIn company-page headcount. It counts alumni and contractors, so treat it as a ceiling (**Estimate**). Company-controlled page.
- **Job posts:** number of open roles and how many staff roles the posts imply (**Inference**; date the posts).
- **Facility size:** square footage or bay/seat count from listings or the site, with a stated employees-per-footprint assumption (**Estimate**; the assumption goes in the `assumptions:` list).
- **Lower bound:** named staff on the site or in news, or a state or federal filing that shows a payroll size (**Fact** if cited).
If sources disagree by more than 2x, say so and widen the band. If you have no headcount source at all, the band is **Unknown**; stop.

## Step 4 — Do the arithmetic
```
low  = headcount_low  x benchmark_low_or_point
high = headcount_high x benchmark_high_or_point
```
- Use the same benchmark for both ends unless the source table gives a range.
- Add federal awards from USAspending only as a separate line (Fact, cited), never folded in silently.
- Round to two significant figures. Show the inputs next to the result.
- Manual fallback: do it by hand on paper; there is no script for this step.

## Step 5 — Record the band
Fill the brief's size-band section from this table:
| Input | Value | Label | Source and date |
|---|---|---|---|
| Headcount low | | | |
| Headcount high | | | |
| Benchmark (sales per employee) | | Fact | table, year, URL |
| Federal awards (optional) | | Fact | USAspending URL, date |
| Band low / high | | Estimate | the two products above |

Then add the line: "Indicative size band, NOT a valuation. Actual revenue and EBITDA: Unknown (private company)."

## Common mistakes
- Treating the band as what the owner earns or what the business is worth.
- Using a benchmark for the wrong NAICS code or a very different size class.
- Quoting a benchmark from memory. Open the table.
- Using LinkedIn headcount as the midpoint instead of the ceiling.
