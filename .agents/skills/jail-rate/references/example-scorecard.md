# Worked example — small-business rating for a prospective buyer

Synthetic data. "Harbor Ridge HVAC Services" is a made-up business; every
number below came from the fact sheet in the input, not from outside research.

## Input

> Rate this business 0–10 for a prospective buyer.
>
> Fact sheet (from the owner): revenue $1.42M, $1.58M, $1.71M for the last three
> years. Top customer is 38% of revenue. Owner works about 70 hours a week.
> No CRM; jobs tracked in a spreadsheet. 4.7 stars from 212 Google reviews.
> Two senior technicians do most of the complex installs.

## Output

> **Harbor Ridge HVAC Services — small business (diagnostic), buyer lens — Overall: 4.8 / 10 → 6.4 / 10 projected (▲ +1.6)**

**Rubric used** (declared before scoring; weights sum to 100%)

| Dimension | Weight | Why this weight for a small business bought by an outsider |
|---|:---:|---|
| Financial health | 20% | A buyer pays for earnings; trend and concentration decide what they are worth |
| Sales & marketing engine | 20% | The engine that refills revenue after the owner leaves |
| Operations | 15% | Whether work gets done without the owner on every job |
| People & leadership | 15% | Key-person risk is the main way a sale fails after closing |
| Technology & data | 15% | Records a buyer can inspect, and systems that outlive the owner's memory |
| Risk & compliance | 15% | Concentration, contracts, licenses, insurance: what can break the deal |

**Scorecard**

| Dimension | Weight | Now | Projected | Evidence (label + source) |
|---|:---:|:---:|:---:|---|
| Financial health | 20% | 5.5 | 6.5 | User-provided (owner): revenue grew $1.42M → $1.58M → $1.71M. Inference: growth is steady, but 38% from one customer makes the top line fragile. Unknown: margins, cash, debt; no statements or tax returns seen. |
| Sales & marketing engine | 20% | 6.5 | 7.5 | User-provided (owner): 4.7 stars from 212 Google reviews. Not opened or checked, so the review base is asserted, not proven. Inference: strong reputation, but no CRM means lead sources and win rate are unmeasured. |
| Operations | 15% | 5.0 | 6.0 | User-provided (owner): jobs tracked in a spreadsheet; two technicians do the complex installs. Inference: capacity depends on two people. |
| People & leadership | 15% | 4.0 | 6.0 | User-provided (owner): about 70 hours a week. Inference: the business runs through the owner, which is a transfer risk. Judgment: no second manager is described. |
| Technology & data | 15% | 3.0 | 6.0 | User-provided (owner): no CRM. Inference: customer history, pipeline, and job data are not in a system a buyer can inspect. |
| Risk & compliance | 15% | 4.0 | 6.0 | User-provided (owner): top customer is 38% of revenue. Inference: losing it would remove over a third of revenue, a material concentration risk, so the critical-flaw cap (≤ 4.0) applies. Unknown: contract term, licenses, insurance. |

**Why this score.** Revenue growth and a strong review profile are real
positives. Three things hold the score down: 38% of revenue from one customer,
a business that depends on the owner's 70-hour weeks and two technicians, and
no system of record. All inputs are owner statements, so the score is a
screening read, not a valuation.

**Top recommendations (ranked)**
1. Get the top customer on a written multi-year agreement and add new
   accounts until no customer is above 25% (Risk & compliance, Financial
   health; high impact, 6–12 months).
2. Put job and customer records into a CRM and report lead source and win rate
   monthly (Technology & data, Sales & marketing; medium impact, 1–2 months).
3. Document the install process and train a third technician; move the owner
   to a set weekly schedule (People & leadership, Operations; high impact,
   3–9 months).

**Projected rating.** The projected 6.4 assumes only the three fixes above land
competently. It stays below 7 because margins, contracts, and compliance are
still unverified. **Estimate**, method: re-scored each dimension against the
same anchors assuming the stated facts change.

**Sources.** None external. Rated from supplied materials only (private
subject). For a real run, compare against industry benchmarks from Census and
BLS small-business data, and open the Google review profile directly, before
relying on any figure here.

**Confidence — Low.** Every input is a User-provided owner statement. One
action would most raise it: obtain three years of tax returns and a profit and
loss statement, plus the top customer's contract, which would move Financial
health and Risk & compliance toward Medium or High.

## Arithmetic check

Now: 5.5×0.20 + 6.5×0.20 + 5.0×0.15 + 4.0×0.15 + 3.0×0.15 + 4.0×0.15
= 1.10 + 1.30 + 0.75 + 0.60 + 0.45 + 0.60 = 4.80.
Projected: 6.5×0.20 + 7.5×0.20 + 6.0×0.15 + 6.0×0.15 + 6.0×0.15 + 6.0×0.15
= 1.30 + 1.50 + 0.90 + 0.90 + 0.90 + 0.90 = 6.40.

## JAIL-HANDOFF

```yaml
JAIL-HANDOFF:
  skill: jail-rate
  status: complete
  facts: []
  assumptions: ["Rating is a screening read for a prospective buyer, not a valuation", "Owner fact sheet is accurate"]
  unknowns: ["Margins, cash, and debt", "Top customer contract term", "Licenses and insurance", "Actual Google review profile"]
  outputs: [scorecard, rubric]
  evidence: ["Owner fact sheet (User-provided), supplied in the request"]
  risks: ["38% revenue concentration in one customer", "Owner 70-hour dependence and two key technicians"]
  confidence: low
  next: none
  approval_required: []
  checks:
    score-check.py: pass
```
