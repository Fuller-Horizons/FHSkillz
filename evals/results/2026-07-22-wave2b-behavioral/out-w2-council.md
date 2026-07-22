# COUNCIL ANSWER — Is this memo claim accurate: "Section 179 lets a small business deduct the full cost of a $120k work truck in year one"?

**Lane:** MINI-COUNCIL (3 blind members, one anonymized review round, verification round fired, chairman synthesis — no rebuttal round)
**Tier:** B — different models, same provider (Anthropic: agent models `opus`, `sonnet`, `haiku`, each a fresh independent session). Not cross-provider; no Tier A claim.
**Chairman:** Fable 5 (the orchestrator session — strongest available model; **not** a council member).
**Epistemic mode:** Groundable — US federal tax law (IRC §179, §280F; IRS instructions and Revenue Procedures are retrievable primary sources). Counciled for tax years 2025–2026 (memo date 2026-07-22).

## Step 0 — Frame (what would make an answer WRONG)

An answer fails if it: misstates the §179 dollar limits for 2025/2026 (including missing the July 2025 OBBBA change); misses or misstates vehicle rules (GVWR classes, the §179(b)(5) heavy-SUV cap and its exemptions, §280F luxury-auto caps); misses the >50%-business-use requirement or business-use proration; misses the taxable-income limitation; conflates §179 with bonus depreciation; or returns an unqualified true/false a competent tax reviewer would flag.

---

## FINAL ANSWER

**Verdict: ACCURATE WITH CONDITIONS — do not publish the sentence as written.** (Council: 2 of 3 members; all 3 reviewers unanimously endorsed this verdict after review; the dissenting member's "INACCURATE" verdict rested on two factual errors refuted in the verification round.)

The result the sentence promises — a full $120k first-year write-off — is genuinely achievable for a typical heavy work truck, but only when specific conditions hold, and in one common configuration it is not achievable through Section 179 alone. The unqualified sentence overstates the law.

### The conditions, with per-claim confidence

1. **The overall §179 dollar cap is not the constraint.** [Fact — verified] For tax years beginning in 2025 the limit is **$2,500,000** (phase-out begins at $4,000,000), raised by the One Big Beautiful Bill Act (July 2025); for 2026 it is **$2,560,000** (phase-out $4,090,000). $120k is far below both. — **Confidence: High** (IRS Form 4562 Instructions 2025; Rev. Proc. 2025-32 §4.24).

2. **GVWR over 6,000 lbs is required.** [Fact — verified] Vehicles at or under 6,000 lbs GVWR are "passenger automobiles" under §280F and hit luxury-auto caps — for 2025, **$12,200** first year without bonus depreciation, **$20,200** with it (Rev. Proc. 2025-16) — which make a full $120k year-one deduction impossible. Vehicles over 6,000 lbs GVWR escape §280F entirely. — **Confidence: High**. That a $120k work truck exceeds 6,000 lbs GVWR is very likely but is an [Inference] — the memo should state the condition, not assume it. — **Confidence: Medium** as applied to an unspecified truck.

3. **Bed/body configuration decides whether §179 alone gets there.** [Fact — verified] Vehicles of 6,001–14,000 lbs GVWR are "SUVs" under §179(b)(5), capping the §179 deduction at **$31,300 (2025)** / **$32,000 (2026)** — *unless* the vehicle (a) has a cargo bed of at least 6 feet interior length not readily accessible from the passenger compartment (most long-bed work pickups), (b) seats more than 9 behind the driver, or (c) is a fully enclosed cargo van with no seating behind the driver. Vehicles over 14,000 lbs GVWR are outside the SUV definition and face neither cap. So: a long-bed heavy pickup or a >14,000-lb truck → full $120k is §179-eligible; a short-bed crew cab or SUV-style vehicle → §179 capped at $31,300/$32,000, with the balance typically reachable in year one only via **100% bonus depreciation** (a separate provision, restored at 100% for qualified property acquired after January 19, 2025). — **Confidence: High** on the caps, exemptions, and the 100%-after-1/19/2025 rule (IRS-verified); **Medium** on bonus depreciation being permanent with no scheduled phase-down (one reviewer flagged residual uncertainty; not verified to primary text in this round).

4. **More than 50% business use, and proration.** [Fact — unanimous] §179 for a vehicle requires >50% qualified business use, and the deduction is limited to the business-use percentage — "full cost" requires 100% business use (70% use → ~70% deductible). Business use later dropping to 50% or below triggers recapture. — **Confidence: High**.

5. **Taxable-income limitation.** [Fact — unanimous; IRC §179(b)(3)] The §179 deduction cannot exceed aggregate taxable income from active trades/businesses and cannot create a loss; the excess carries forward. A small business without ~$120k of business income cannot take the full amount in year one via §179 (bonus depreciation is not income-limited). — **Confidence: High**.

6. **§179 is not bonus depreciation.** [Fact — unanimous] Attributing every full first-year write-off to "Section 179" conflates two provisions with different mechanics (income limit, SUV cap apply to §179 only). — **Confidence: High**.

### Recommended memo wording (chairman synthesis of the two top-ranked rewrites)

> "A $120,000 work truck can generally be deducted in full in year one, but not automatically and not always through Section 179 alone. The truck must have a GVWR over 6,000 lbs and be used more than 50% for business (the deduction is limited to the business-use percentage), and the Section 179 portion cannot exceed the business's taxable income for the year. If the truck has a cargo bed at least six feet long not accessible from the cab — or is a qualifying cargo van or rated over 14,000 lbs GVWR — the full cost is Section 179-eligible; otherwise (e.g., a short-bed crew cab or SUV-type vehicle) Section 179 is capped at $31,300 for 2025 ($32,000 for 2026), with the balance typically deductible in year one under 100% bonus depreciation instead."

---

## DISSENT REGISTER

- **Resolved (not preserved as live dissent):** Member C held "INACCURATE," asserting §280F luxury-auto caps (~$12,200) apply to all trucks up to 14,000 lbs GVWR and that the 2025–26 §179 limit is ~$1.26–1.3M. All three reviewers independently rejected both claims; the verification round refuted them with primary sources (§280F line is 6,000 lbs GVWR; 2025 limit is $2,500,000 per IRS Form 4562 Instructions). Recorded as a caught error, not surviving dissent.
- **Live minority nuance — memo framing (held by 1 of 3, Member B):** B's rewrite presents §179 as capped ~$31k for the truck with the remainder reachable only via bonus depreciation; A's rewrite presents the truck as fully §179-deductible. Both are correct on different facts — **decided by the actual truck's GVWR and bed/body configuration**, which the client memo does not state. The chairman wording covers both branches; the advisor should pin down the vehicle's specs.
- **Live flag — permanence of 100% bonus depreciation (raised by 1 reviewer):** treated as current law for post-1/19/2025 acquisitions (IRS-verified) but its "permanent, no phase-down" character was not verified to primary text here. Decided by: reading OBBBA's amended §168(k) text or an IRS pronouncement.
- **Live gap — state conformity (raised by 1 reviewer):** no member addressed possible state-level decoupling from federal §179/bonus amounts; the memo's claim is federal-only. Decided by: the client's state.

---

## AUDIT APPENDIX

### Roster and independence tier
| Seat | Stage-1 member (blind answer) | Stage-3 reviewer (fresh session) |
|---|---|---|
| 1 | Anthropic `opus` (agent session a579729f) | Anthropic `opus` (fresh session a36ccc0e) |
| 2 | Anthropic `sonnet` (agent session acfb70e7) | Anthropic `sonnet` (fresh session a6d028f6) |
| 3 | Anthropic `haiku` (agent session a34e3ec3) | Anthropic `haiku` (fresh session a5fd56db) |

Tier B (distinct model families, one provider). Chairman: Fable 5 (orchestrator), not a member. Blindness: identical briefs, zero cross-talk, members barred from tools/retrieval (retrieval reserved for the verification round). Anonymization: answers shuffled by random draw (`shuf`) → **A = member 1 (opus), B = member 2 (sonnet), C = member 3 (haiku)** — mapping held by the orchestrator only; reviews ran in *fresh* sessions of the same three models so no reviewer could recognize its own answer.

### Blind verdicts (Stage 1)
A: ACCURATE WITH CONDITIONS · B: ACCURATE WITH CONDITIONS · C: INACCURATE

### Ranking table (Stage 3 — best-supported first)
| Reviewer | Ranking | Scores given (accuracy/completeness/reasoning/evidence) |
|---|---|---|
| R1 (opus) | **A, B, C** | A 9/9/9/9 · B 8/8/8/7 · C 3/3/2/3 |
| R2 (sonnet) | **A, B, C** | A 9/9/9/9 · B 8/9/9/8 · C 3/4/3/4 |
| R3 (haiku) | **A, B, C** | A 9/9/9/7 · B 8/9/9/7 · C 4/5/3/5 |

Unanimous ranking A > B > C. Rankings informed the synthesis but did not decide facts — the verification round did.

### Error-hunt results (mandatory per review; 3 reviewers × 3 answers = 9 hunts)
- **On A:** R1 — 2 findings (completeness gap: doesn't spell out >14,000-lb exemption; dollar figures were estimates, self-flagged). R2 — no factual error (listed what was checked: OBBBA cap, §280F threshold/figures, SUV cap + exceptions, proration/recapture, income limit, §179-vs-bonus); gaps: unquantified §179/bonus split, state decoupling. R3 — "none found" (bare; see protocol notes).
- **On B:** R1 — rewrite understates §179 for exempt long-bed pickups, contradicting B's own body text; >14,000-lb exemption unspelled. R2 — "§280F ceiling: a few thousand dollars/year" understates the ~$12,200/$20,200 caps; minor "9+" vs ">9" seating imprecision. R3 — "none found" (bare).
- **On C (material errors, caught by all 3 reviewers):** §280F threshold inverted (14,000 vs 6,000 lbs GVWR) causing a wrong verdict and a corrected wording that would itself mislead (it would deny an available deduction for common heavy pickups); stale pre-OBBBA §179 limit ($1.26–1.3M vs $2,500,000); §179(b)(5) SUV cap and its exemptions omitted; bonus depreciation omitted.
- **Count:** 11 distinct findings; 4 material (all on C), 2 moderate (both on B's deliverable wording), the rest gaps/precision notes. No review was a politeness pass.

### Verification round (fired — answers conflicted on load-bearing facts; evidence, not votes, settled them)
| Disputed fact | Positions | Verdict | Evidence (source · date accessed 2026-07-22) |
|---|---|---|---|
| §179 limit, TY2025 | A/B: $2.5M (OBBBA) · C: ~$1.26–1.3M | **A/B correct** | IRS Instructions for Form 4562 (2025): "$2,500,000", phase-out over "$4,000,000" — https://www.irs.gov/instructions/i4562 |
| §280F luxury-auto threshold | A/B: ≤6,000 lbs GVWR · C: ≤14,000 lbs | **A/B correct; C refuted** | Section179.org vehicle-deduction guide (≤6,000 lbs GVWR subject to luxury-auto limits; SUV cap tier is 6,001–14,000) — https://www.section179.org/section_179_vehicle_deductions/ ; consistent with IRC §280F(d)(5) and the §179(b)(5) structure all reviewers cited |
| §179(b)(5) SUV cap, 2025 | A: $31,300 · B: "low-$31,000s" (est.) | **$31,300 confirmed** | IRS Pub 946 ("maximum section 179 expense deduction for sport utility vehicles placed in service in tax years beginning in 2025 is $31,300") — https://www.irs.gov/publications/p946 ; also i4562 |
| 2026 indexed amounts (flagged Unknown by members) | — | **$2,560,000 limit / $4,090,000 phase-out / $32,000 SUV cap** | Rev. Proc. 2025-32 §4.24 — https://www.irs.gov/pub/irs-drop/rp-25-32.pdf |
| §280F first-year caps, 2025 | A: ~$12k/~$20k (est.) | **$12,200 without bonus / $20,200 with bonus** | Rev. Proc. 2025-16 as reported by The Tax Adviser (Feb 2025) — https://www.thetaxadviser.com/news/2025/feb/lower-auto-depreciation-limits-issued-for-first-time-in-at-least-3-years/ |
| Bonus depreciation 100% | A/B: 100%, post-1/19/2025 acquisitions | **Confirmed** | IRS Instructions for Form 4562 (2025): 100% for qualified property acquired after Jan 19, 2025 (40% transitional for earlier acquisitions) — https://www.irs.gov/instructions/i4562 |
| SUV-cap exemptions (6-ft bed / >9 seats / cargo van) | A and B identical | **Confirmed** | Section179.org (mirrors IRC §179(b)(5)(B)(ii)); unanimous across members and reviewers |

### Protocol notes (honesty items)
- R3 (haiku) returned bare "none found" for A and B without listing checks in the YAML field, a partial deviation from the "say what you checked" rule; its prose key-finding did describe verifying the GVWR-tier mapping. Weighted accordingly (R3's rankings agreed with the two compliant reviews, so nothing turned on it).
- Members answered from parametric knowledge only (tools barred) to keep blind answers independent; retrieval was reserved for the targeted verification round, per the mini-council lane.
- Chairman synthesis contains no claim absent from member answers, review records, or verification results. (Leasing/placed-in-service mechanics were never raised by any member and are therefore not covered — listed under unknowns.)

### Cost disclosure
3 blind member answers + 3 anonymized reviews (6 subagent sessions, ~274k subagent tokens total: members ~114k, reviewers ~160k) + 1 verification round (4 web searches + 4 page fetches) + chairman synthesis in the orchestrator session ≈ 7× the cost of a single-model answer. Invoking jail-council is itself the Rule-11 justification: this figure is going in a client memo.

---

```yaml
JAIL-HANDOFF:
  skill: jail-council
  status: complete
  facts:
    - "TY2025 §179 limit $2,500,000 / phase-out $4,000,000 (post-OBBBA) — IRS i4562 (2025)"
    - "TY2026 §179 limit $2,560,000 / phase-out $4,090,000 / SUV cap $32,000 — Rev. Proc. 2025-32"
    - "§179(b)(5) SUV cap 2025 = $31,300; exemptions: ≥6-ft interior bed not accessible from cab, >9 seats behind driver, enclosed cargo van; >14,000 lbs GVWR outside SUV definition — IRS Pub 946 / §179(b)(5)"
    - "§280F luxury-auto caps apply ≤6,000 lbs GVWR; 2025 first-year $12,200 / $20,200 with bonus — Rev. Proc. 2025-16"
    - "§179 requires >50% business use, prorated by business-use %; recapture if use falls ≤50%"
    - "§179 limited to active-business taxable income; excess carries forward"
    - "Bonus depreciation 100% for qualified property acquired after 2025-01-19 — IRS i4562"
  assumptions:
    - "Federal tax treatment, tax year 2025 or 2026; vehicle purchased and placed in service in the deduction year"
    - "'Work truck' at $120k is likely >6,000 lbs GVWR — inference, must be confirmed against the actual vehicle"
  unknowns:
    - "Actual truck GVWR and bed/body configuration (decides SUV-cap branch)"
    - "Client's business-use percentage and business taxable income"
    - "State conformity to federal §179/bonus amounts"
    - "Permanence (no phase-down) of 100% bonus depreciation — not verified to primary OBBBA text this round"
    - "Leasing/financing mechanics — outside council scope, never raised by members"
  outputs: ["/home/claude/work/wave2b/out-w2-council.md"]
  evidence:
    - "IRS Instructions for Form 4562 (2025) · 2025 §179 $2.5M/$4M, SUV $31,300, bonus 100% post-1/19/2025 · https://www.irs.gov/instructions/i4562 · 2026-07-22"
    - "IRS Rev. Proc. 2025-32 §4.24 · 2026 amounts $2,560,000/$4,090,000/$32,000 · https://www.irs.gov/pub/irs-drop/rp-25-32.pdf · 2026-07-22"
    - "IRS Pub 946 · SUV cap $31,300 (2025) · https://www.irs.gov/publications/p946 · 2026-07-22"
    - "The Tax Adviser on Rev. Proc. 2025-16 · 2025 §280F first-year $12,200/$20,200 · https://www.thetaxadviser.com/news/2025/feb/lower-auto-depreciation-limits-issued-for-first-time-in-at-least-3-years/ · 2026-07-22"
    - "Section179.org vehicle guide · 6,000-lb §280F line; SUV-cap exemptions; 2026 corroboration · https://www.section179.org/section_179_vehicle_deductions/ · 2026-07-22"
  risks:
    - "Publishing the sentence as written overstates the law (SUV-cap branch, business-use proration, income limit)"
    - "Adopting the rejected C position would wrongly deny full expensing for common heavy pickups"
  confidence: high
  next: "jail-verify (optional independent check of this synthesis) — and have the client's CPA confirm the specific vehicle's GVWR/bed configuration before the memo ships"
  approval_required: []
```
