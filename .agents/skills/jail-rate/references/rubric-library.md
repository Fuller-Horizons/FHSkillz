# Rubric library — per-type dimensions, weights, and evidence sources

Load this at Step 2. Each rubric: dimensions, default weights (sum 100%), and
where empirical evidence for that type lives. Weights are defaults — adjust for
the user's context (say so), or use the user's weights when supplied.

## Software product (app / SaaS / website)
| Dimension | Weight | Evidence to seek |
|---|:---:|---|
| Software quality | 25% | Repo/CI state, test coverage, issue tracker, changelog cadence, incident history |
| Features | 20% | Docs/feature matrix vs top 2–3 competitors, roadmap, release notes |
| Usability | 20% | Independent reviews, app-store/G2/Capterra themes, a11y audit, onboarding walk-through |
| Security | 20% | CVEs, disclosed breaches, pen-test/SOC2/ISO attestations, dependency audit, auth model |
| Marketability | 15% | Traffic/rank data, pricing vs alternatives, positioning clarity, traction signals |

*Why:* quality leads because everything else decays without it; security equals
usability because one breach outweighs years of polish.

## Codebase / code (a repo, module, PR, or snippet)
| Dimension | Weight | Evidence to seek |
|---|:---:|---|
| Correctness | 30% | Tests pass/exist, bug density, issue tracker, reproducible behavior vs spec |
| Maintainability & readability | 25% | Structure, naming, docs, coupling, dead code, onboarding cost |
| Security | 20% | Injection/authz/secrets handling, dependency CVEs, input validation |
| Performance & efficiency | 15% | Benchmarks, complexity hot spots, resource profile |
| Tooling & operability | 10% | CI/CD, lint/format, observability, build reproducibility |

*Why:* code that's wrong is worthless (30%); code that can't be changed safely
is next-worst (25%).

## Hardware / physical product
| Dimension | Weight | Evidence to seek |
|---|:---:|---|
| Performance (vs spec & class) | 25% | Independent lab benchmarks (RTINGS-class), teardown reports, spec-vs-measured |
| Reliability & build quality | 25% | Failure-rate data, warranty terms, recall records, long-term reviews, teardowns |
| Ergonomics & usability | 20% | Hands-on reviews, accessibility, setup experience |
| Value for money | 15% | Street price vs measured performance of alternatives |
| Serviceability & support | 15% | Repairability scores (e.g. iFixit), parts availability, firmware-update record, support SLAs |

*Why:* hardware can't be patched like software — reliability carries weight
equal to performance; serviceability matters because it sets total cost of
ownership.

## Person — professional/public role ONLY (see SKILL.md and people-boundaries.md first)
| Dimension | Weight | Evidence to seek (public only) |
|---|:---:|---|
| Role competence & track record | 35% | Documented outcomes, shipped work, published results, tenure milestones |
| Domain expertise | 20% | Publications, talks, credentials, recognized contributions |
| Execution & delivery | 20% | Completed projects/terms, measurable results vs goals stated for the role |
| Communication & public leadership | 15% | Public writing/speaking, documented team/organizational outcomes |
| Professional conduct | 10% | On-the-record conduct in the role (regulatory findings, formal sanctions — adjudicated, not alleged) |

*Why:* outcomes in the role dominate (35%); conduct is weighted low but a
disqualifying adjudicated integrity issue triggers the critical-flaw cap
regardless. Rumor and allegations are never evidence.

## Idea / concept / business plan
| Dimension | Weight | Evidence to seek |
|---|:---:|---|
| Problem significance | 25% | Market/user research, incidence data, willingness-to-pay signals |
| Feasibility | 25% | Comparable implementations, technical precedent, resource realism |
| Differentiation & defensibility | 20% | Existing alternatives (search them — they usually exist), moat logic |
| Economics | 20% | Comparable unit economics, cost structures, pricing benchmarks |
| Timing & risk | 10% | Market/regulatory tailwinds or headwinds, dependency risks |

*Why:* a big problem that can't be built (or a buildable non-problem) both die —
significance and feasibility lead equally.

## Program / initiative (policy, nonprofit, internal program)
| Dimension | Weight | Evidence to seek |
|---|:---:|---|
| Outcomes vs stated goals | 30% | Published metrics, evaluations, audits, before/after data |
| Cost-effectiveness | 20% | Budget vs outcomes, benchmark programs, cost-per-result |
| Execution quality | 20% | Delivery record, timeline adherence, stakeholder reports |
| Sustainability | 15% | Funding durability, dependency on individuals, succession |
| Stakeholder value & equity | 15% | Beneficiary feedback, coverage/access data |

## Service / business (as an operating entity)
| Dimension | Weight | Evidence to seek |
|---|:---:|---|
| Service/product quality | 30% | Review platforms (Google/Yelp/BBB/Trustpilot) — themes, not averages; complaint records |
| Operations & reliability | 20% | Fulfillment/delivery record, capacity signals, certifications |
| Customer experience | 20% | Response patterns, support channels, review-response quality |
| Financial health signals | 15% | Public filings/liens/tenure (free sources; never fabricate private financials) |
| Market position | 15% | Share-of-voice, differentiation, competitive set |

*For a pursue/pass prospecting decision, use jail-prospect instead.*

## Content / media (article, video, course, book, report)
| Dimension | Weight | Evidence to seek |
|---|:---:|---|
| Accuracy & grounding | 30% | Spot-check its claims against primary sources |
| Depth & completeness | 20% | Coverage vs the best comparable treatments |
| Clarity & craft | 20% | Structure, prose/production quality, audience fit |
| Originality | 15% | What it adds beyond existing work on the topic |
| Usefulness/actionability | 15% | Can the audience do something with it |

## Small business (diagnostic) — owner-run SMB, for an owner, buyer, or advisor
| Dimension | Weight | Evidence to seek |
|---|:---:|---|
| Financial health | 20% | Owner financials (P&L, balance sheet, tax returns, 3 years), margin and cash trend, customer concentration, receivables; compare to industry benchmarks (Census/BLS data; RMA ratios where licensed) |
| Sales & marketing engine | 20% | CRM or lead log, pipeline and win rate, lead sources, review platforms (themes, count, recency), website and search presence, referral share |
| Operations | 15% | Process documentation, capacity vs demand, fulfillment record, key-person and key-technician dependence, supplier terms |
| People & leadership | 15% | Org chart, tenure and turnover, owner hours and delegation, hiring pipeline, succession depth |
| Technology & data | 15% | Systems inventory (CRM, accounting, scheduling), data quality, integrations, backups, how much runs from the owner's head |
| Risk & compliance | 15% | Customer/supplier concentration, licenses and insurance, contracts, legal or regulatory findings, single points of failure |

*Why:* money and the engine that refills it lead (20% each). The rest decide
whether the business survives losing a person, a customer, or a system. A
material concentration or key-person risk is a critical flaw: cap the
dimension it hits at 4.0 and say which fact triggered it. For a buyer, say so
in the declared rubric; for an owner, keep weights as listed. Owner financials
without statements or returns are **User-provided**; confidence Low until
corroborated. This rubric is for a diagnostic rating; a pursue/pass sell-side
call is jail-prospect.

## Sales & marketing function (a team, system, or program inside a business)
| Dimension | Weight | Evidence to seek |
|---|:---:|---|
| Strategy & positioning | 15% | Defined target customer, offer, message; competitor comparison |
| Pipeline & lead generation | 20% | Lead volume by source, cost per lead, pipeline coverage vs target |
| Conversion & sales process | 20% | Stage definitions, win rate, cycle length, follow-up speed, proposal quality |
| Brand, reputation & content | 15% | Reviews, case studies, content cadence and reach, message consistency |
| Retention & expansion | 15% | Repeat rate, churn, referral share, account growth |
| Measurement & tooling | 15% | CRM hygiene, attribution, a report someone reads every week |

*Why:* pipeline and conversion are where revenue is made (20% each). Claimed
numbers (win rate, "leads per month") without an export or report are
**User-provided**; downgrade until seen.

## Leadership team — professional role ONLY (see SKILL.md boundaries first)
| Dimension | Weight | Evidence to seek (documented, role-related) |
|---|:---:|---|
| Results vs role goals | 30% | Targets set for the role vs results delivered; board or owner reports |
| Strategic clarity | 20% | Written plan, priorities that match resource use, decisions explained |
| Team development & retention | 20% | Promotions, turnover, hiring record, engagement data |
| Decision quality & accountability | 15% | Decisions and their outcomes, how misses were handled, cadence of reviews |
| Bench & succession | 15% | Named deputies, delegation, what happens if the leader leaves |

*Why:* delivery against the role's own goals dominates. Never score personal
traits, health, or private life; see
[people-boundaries.md](people-boundaries.md).

## Deriving a rubric for an unlisted type (meta-procedure)
1. **State the subject's purpose** in one sentence — what does success look
   like, for whom?
2. **List the 4–6 factors** that most determine that success. Prefer factors an
   outside observer could evidence; merge overlapping ones.
3. **Weight by consequence:** for each factor ask "if this were terrible, how
   badly does the subject fail its purpose?" Rank, then assign weights summing
   to 100% — heaviest ≤ 35%, lightest ≥ 5%, so no single factor decides alone
   and none is decorative.
4. **Name the evidence source for each factor** before scoring; a factor with
   no conceivable evidence source is a bad factor — replace it.
5. **Declare the derived rubric in the output** exactly like a built-in one,
   marked "derived," so the user can challenge it before the scores land.
