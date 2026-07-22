# COUNCIL ANSWER — Does US federal law require residential landlords to replace aluminum branch-circuit wiring?

**Lane:** FULL (explicit "convene the council" + legal question → 5 members per sizing guidance)
**Tier:** C — 5 independent same-model sessions (claude-fable-5). Only one model family is available in this environment, so cross-provider (Tier A) and cross-model (Tier B) seating were not possible. Tier C is the weakest independence tier; it still beats self-review because blindness, fresh contexts, and anonymized review survive even when the weights don't differ. Declared per protocol — this is part of the answer's credibility.
**Chairman:** the orchestrator session (claude-fable-5) — not a council member (submitted no blind answer), but the same model family as the members; disclosed as required.
**Epistemic mode (Step 0):** groundable — the question is about existing US federal statutes and regulations, all retrievable from primary sources. Blind round ran from trained knowledge only; the verification round used live primary sources (eCFR, Federal Register, cpsc.gov, hud.gov, full court opinions). The question can be wrong (a fabricated mandate, a category error, a misstated authority, or a materially incomplete bare "no"), so it is councilable — no STOP.
**Cost disclosure (charter):** invoking jail-council is itself the Rule-11 justification; accuracy outranks cost. Actual spend: 15 model calls ≈ 15× a single answer (details in appendix). Disclosed, not gated.
**Date of deliberation:** 2026-07-22.

---

## FINAL ANSWER

**No. There is no US federal statute and no binding federal regulation that requires private residential landlords to replace — or repair, disclose, or inspect — aluminum branch-circuit wiring in existing rental housing.** [Confidence: **High** — unanimous across 5 blind members, survived 25 adversarial error-hunts, and affirmatively grounded in the verification round: a CFR-wide full-text search returns zero hits for "aluminum wiring" and only one section for "aluminum conductors" (a new-construction standard); the CPSC's own list of mandatory standards and bans omits aluminum wiring; and the one federal document on point is expressly advisory.]

A bare "no" would mislead, though. Here is what federal law actually does, each claim labeled with the council's evidence-based confidence:

**1. The CPSC — the principal federal actor — has only advisory guidance.**
CPSC Publication 516, *Repairing Aluminum Wiring*, is guidance, not law. Verified verbatim from the official PDF (cpsc.gov, accessed 2026-07-22): "CPSC **recommends** a permanent repair of the connections"; replacement of aluminum branch conductors with copper "eliminates the primary cause of the potential hazards"; the COPALUM crimp connector is "a safe and permanent repair," with AlumiConn "the next best alternative"; ordinary wire-nut pigtailing "does not solve the problem of overheating"; CO/ALR devices are "at best, an incomplete repair." It also carries the famous risk finding, with attribution confirmed: a national survey by **Franklin Research Institute** for CPSC found pre-1972 aluminum-wired homes are **55 times more likely** to have connections reach "Fire Hazard Conditions" than copper-wired homes. No "must" or "required by law" language imposes any duty on owners or landlords. [Confidence: **High** — primary source, quoted.]

**2. The CPSC tried to compel repairs in the 1970s and never succeeded — but the litigation story most people (and most council members) tell is wrong in the details.**
Verified from the full opinions (accessed 2026-07-22):
- *Kaiser Aluminum & Chemical Corp. v. CPSC*, 574 F.2d 178 (**3d Cir.**), cert. denied, 439 U.S. 881 (1978), was a challenge to CPSC's **§ 7 safety-standard development proceeding** and public-information activities. The Third Circuit **reversed** the Delaware district court and held that aluminum branch-circuit wiring **IS a "consumer product"** — a win *for* CPSC on the threshold question, not the jurisdictional defeat several members recalled.
- The § 12 imminent-hazard suit seeking "an order requiring the permanent repair of residences wired with old technology aluminum wiring systems" was *CPSC v. Anaconda Co.*, 445 F. Supp. 498 (D.D.C. 1977) (jurisdiction upheld below), and it foundered on appeal: *CPSC v. Anaconda Co.*, 593 F.2d 1314 (D.C. Cir. 1979) held a § 12 order against wiring *systems* requires the systems themselves to be "distinct articles of commerce" sold to consumers — a showing CPSC could not make — and remanded. (*United States v. Anaconda Co.*, 445 F. Supp. 486 (D.D.C. 1977), was a separate subpoena-enforcement action, which *upheld* CPSC's investigative jurisdiction.)
- No repair order was ever entered, the § 7 standard was never promulgated (nothing exists in 16 CFR), and the effort was ultimately abandoned. [Confidence: **High** on the holdings and on "no binding requirement ever issued" (full opinions + CPSC's own mandatory-standards list); **Medium** on the precise post-remand endgame (~early-1982 abandonment rests on one secondary account — see Dissent Register).]

**3. The one binding federal provision that names aluminum branch wiring is a construction standard for new manufactured homes — not a landlord retrofit duty.**
Current operative text, verified three ways (eCFR, Cornell LII, GPO — character-identical): **24 CFR § 3280.801(e)**: "Aluminum conductors, aluminum alloy conductors, and aluminum core conductors such as copper clad aluminum; are not acceptable for use in branch circuit wiring in manufactured homes." This is a flat, size-independent ban — but it sits in the HUD Manufactured Home Construction and Safety Standards (42 U.S.C. § 5401 et seq.), which bind **manufacturers of new homes** (built on or after June 15, 1976; the sale prohibition at 24 CFR 3282.252 binds distributors/retailers and excludes used homes). Nothing in it requires any landlord to rewire an existing home. Note two corrections the verification round made: the ban is *not* at § 3280.808 (every member miscited it there), and it is *not* a "smaller than 8 AWG" rule (two members' hedged recollection). [Confidence: **High** — verbatim primary text.]

**4. Federally assisted housing: hazard-based program conditions, not general law — and nothing aluminum-specific.**
Landlords who choose to take HUD subsidies (Housing Choice Voucher / project-based Section 8, etc.) must pass HUD physical-condition inspections: historically HQS (pre-NSPIRE 24 CFR 982.401(f), "Illumination and electricity" — operative language "The electrical fixtures and wiring must ensure safety from fire"; the remembered phrase "no evidence of electrical hazards" actually lived in the pre-NSPIRE UPCS at 24 CFR 5.703(f)), now the NSPIRE standards (final rule, 88 FR 30442, May 11, 2023, codified at 24 CFR 5.703; current § 982.401 is a cross-reference to it). Verified against the standards themselves: NSPIRE's electrical deficiencies are purely condition-based (damaged/ungrounded outlets, exposed conductors, GFCI/AFCI items, service-panel access); **the word "aluminum" appears nowhere** in the electrical standards or the standards notice. Compliance timing, verified through today: HUD extended the HCV/PBV NSPIRE compliance date three times — to Oct 1, 2024 (88 FR 66882), Oct 1, 2025 (89 FR 55645), and currently **Feb 1, 2027** (90 FR 46911, Sept 30, 2025). All five members and all five reviewers had stale dates; the primary record settled it. Failing inspection costs the subsidy — it is a participation condition, not a command to private landlords generally, and a manifested hazard can be cured by repair rather than wholesale rewiring. [Confidence: **High** — primary documents.]

**5. The NEC is not federal law — and does not ban aluminum anyway.**
The National Electrical Code (NFPA 70) is a private model code with legal force only where states/localities adopt it (confirmed in verification); adoptions are generally prospective, grandfathering existing compliant installations. The NEC permits modern AA-8000-series aluminum alloy conductors and recognizes CO/ALR-rated devices for legacy 15/20-amp aluminum circuits. [Confidence: **High** on the not-federal-law status (verified); **Medium** on the AA-8000/CO-ALR content details (uniform member knowledge, unchallenged in review, not independently re-verified this run).]

**6. No federal disclosure duty either — the lead-paint contrast.**
Where Congress did act on a legacy residential hazard, it did so expressly: lead-based paint disclosure under 42 U.S.C. § 4852d (24 CFR part 35; 40 CFR part 745). No analogous statute exists for aluminum wiring — consistent with the verified zero-hit CFR search and statute searches. [Confidence: **High** for the contrast; the negative is the same well-searched absence as the core claim.]

**7. What actually compels aluminum-wiring remediation is not federal law.**
State/local codes and habitability law (repair of manifested hazards), voluntary federal program participation (item 4), FHA/VA/USDA loan-transaction property conditions, and — most powerfully in practice — insurers who refuse or surcharge coverage absent COPALUM/AlumiConn remediation or rewiring. These are state law, program conditions, and private contracts, respectively. OSHA's electrical rules bind employers as to workplaces, not landlords as to dwellings. [Confidence: **High** on the legal character of each instrument; **Medium** on insurer-practice specifics (market knowledge, uncontested); whether FHA/VA handbooks name aluminum specifically remains **Unknown**.]

**Practical bottom line:** a private US residential landlord has no federal-law duty to replace aluminum branch-circuit wiring. Any real compulsion will come from state/local enforcement, subsidy-program participation, lenders, or insurers — and the CPSC's advisory guidance (rewire, or COPALUM/AlumiConn every connection) is the safety benchmark those actors tend to use. This is legal information synthesized from cited sources, not legal advice for a specific property or jurisdiction (Constitution Rule 9).

---

## DISSENT REGISTER

- **On the core answer: none — unanimous after review.** The error-hunt records support saying so: all 25 reviews performed explicit error hunts; every hit landed on citations, dates, or litigation particulars, never on the bottom line; and the verification round then grounded the negative affirmatively (CFR-wide search, CPSC mandatory-standards list, Pub. 516's advisory framing). This is inspected agreement, not convergence theater.
- **Residual uncertainties preserved (not member-vs-member dissent, but honest gaps):**
  - *Post-remand endgame of the § 12 Anaconda suit* — the "abandoned ~early 1982" account rests on a single secondary source (a CPSC-hosted technical report that itself garbles Kaiser's outcome). Held at Medium. Would be decided by: the post-remand D.D.C. docket/disposition (PACER or a reported order). No source anywhere reports relief ever granted.
  - *Whether FHA/VA/USDA handbooks (e.g., HUD 4000.1) mention aluminum wiring by name* — Unknown; either way they are transaction conditions, not general law. Would be decided by: reading the current handbook text.
  - *Universal-negative caveat* — "no federal law requires X" is a well-searched absence (searches enumerated in appendix), not a provable absolute. Would be decided by: any counterexample statute/regulation surfacing.

---

## AUDIT APPENDIX

### Roster and tier
| Seat | Identity | Independence controls |
|---|---|---|
| Members M1–M5 | 5 fresh, independent sessions of claude-fable-5 | Identical protocol brief; blind (no cross-talk, no shared context); **no tools permitted** — trained knowledge only (verified: 0 tool uses per member) |
| Reviewers R1–R5 | 5 fresh, independent sessions of claude-fable-5 | Saw only the anonymized packet; no web access; required error hunt per answer |
| Verification V1–V4 | 4 fresh sessions with live web access | Targeted single-dispute briefs; primary sources required |
| Chairman | Orchestrator session (claude-fable-5), not a member | Synthesis restricted to reviewed material + verification results |

**Tier honesty notes:** (1) Tier C declared — same model family throughout; claiming stronger seating would be tier inflation. (2) Implementation disclosure: sessions here are stateless, so "each member reviews" was implemented as five fresh reviewer sessions (R1–R5) rather than literally re-invoking member sessions; this preserves (indeed strengthens) blindness and anonymity — no reviewer had an own-answer to favor — and is disclosed rather than papered over. (3) Chairman is the same model family as members — unavoidable in this environment; disclosed.

**Anonymization:** attribution stripped; letters assigned by a real random shuffle (`shuf`): **A=M5, B=M4, C=M2, D=M3, E=M1**. The mapping was withheld from all reviewers and is disclosed here post-synthesis only. Full anonymized answers preserved verbatim in `/home/claude/work/wave2b/council-packet-anon.md` (proof-of-work).

### Ranking table (reviewer × ranking, best-supported → weakest)
| Reviewer | Ranking |
|---|---|
| R1 | B > C > D > A > E |
| R2 | B > C > D > A > E |
| R3 | B > D > C > A > E |
| R4 | C > B > D > A > E |
| R5 | B > C > D > A > E |

Mean review scores (sum of accuracy+completeness+reasoning+evidence, /40): **B 36.0 · C 36.2 · D 35.0 · A 34.0 · E 31.6.** Consensus: B strongest on 4/5 rankings; E weakest on 5/5 (its confidently-vouched wrong circuit for *Kaiser* was the packet's clearest citation error). Chairman note — evidence beats votes, demonstrated twice: the synthesis did not simply adopt top-ranked B (verification corrected B's § 15 framing of *Kaiser*, its § 3280.808 cite, and its NSPIRE date), and the reviewers' own 5/5 consensus leanings (that *Kaiser* was a § 15 proceeding; that Oct 1, 2025 was the current NSPIRE date) were themselves overturned by the primary record.

### Verification round (Step 4 — reviews disagreed on load-bearing facts; synthesis was not permitted over the dispute)
| # | Disputed fact | Verdict | Key evidence (all accessed 2026-07-22) | Confidence |
|---|---|---|---|---|
| V1 | HUD Code aluminum restriction: flat ban vs "smaller than 8 AWG"; section number | **Flat ban — but at 24 CFR § 3280.801(e), not § 3280.808** (all five members miscited the section; A/C's 8-AWG version wrong; no size-based rule exists in part 3280 subpart I). New-construction standard confirmed; no retrofit duty (24 CFR 3282.1, 3282.252). Wording operative since 70 FR 72051 (2005)/71 FR 19639 (2006); 2024 amendments (89 FR 75704, effective Sept 15, 2025 per 90 FR 10593) left (e) unchanged | ecfr.gov (current § 3280.801); law.cornell.edu/cfr/text/24/3280.801; govinfo.gov CFR-2024 PDF — three-way character-identical | High |
| V2 | *Kaiser* circuit and vehicle; *Anaconda* holdings; any mandate ever | **3d Cir.** (E's 4th Cir. wrong). *Kaiser* was a **§ 7 standard-development + information-activities challenge — neither § 15 (B) nor § 12 (E)** — and the 3d Cir. **held wiring IS a consumer product** (reversing 428 F. Supp. 177 (D. Del. 1977)). 445 F. Supp. 486 (D.D.C. **1977**) = subpoena enforcement (jurisdiction upheld), not the § 12 dismissal C described; the § 12 repair suit is 445 F. Supp. 498 (D.D.C. 1977); *CPSC v. Anaconda*, 593 F.2d 1314 (D.C. Cir. 1979) imposed the "distinct article of commerce" test for systems and remanded. **No repair order, standard, or mandate ever issued** — confirmed | openjurist.org/574/f2d/178; courtlistener.com/c/F.2d/574/178; law.justia.com (445 F. Supp. 486; 445 F. Supp. 498; 593 F.2d 1314; 414 F. Supp. 1047; 428 F. Supp. 177); cpsc.gov 1976/1978/2003 releases; cpsc.gov FOIA Aronstein report (endgame — sole secondary source) | High (holdings); Medium (endgame) |
| V3 | NSPIRE rule cite; HCV/PBV compliance date; aluminum-specific items; HQS wording | 88 FR 30442 (May 11, 2023) **confirmed**. Compliance chain: Oct 1 2023 → **Oct 1 2024** (88 FR 66882) → **Oct 1 2025** (89 FR 55645) → **Feb 1 2027** (90 FR 46911, Sept 30 2025) — **all members and reviewers were stale**. NSPIRE electrical standards: condition-based; **"aluminum" appears nowhere**. 982.401(f) was "Illumination and electricity" ("wiring must ensure safety from fire"); "no evidence of electrical hazards" was UPCS 5.703(f); current 982.401 is a cross-reference (89 FR 38296) | federalregister.gov (2023-09693; 2023-21141; 2024-14718; 2025-19070; 2023-13293); hud.gov/reac/nspire-standards & nspire-notices; ecfr.gov 5.703, 982.401; govinfo 2023-edition PDFs | High |
| V4 | Core negative + Pub. 516 advisory status | **Supported, both halves.** Pub. 516 quoted verbatim ("CPSC recommends…"; COPALUM "safe and permanent"; AlumiConn "next best alternative"; pigtailing "does not solve the problem"; CO/ALR "incomplete repair"; 55×/Franklin Research Institute confirmed). Negative: eCFR full-text "aluminum wiring" = **0 hits CFR-wide**; "aluminum conductors" → only 24 CFR 3280.801; CPSC mandatory-standards list omits it; statute searches (govinfo/uscode/congress.gov) empty through July 2026; NEC confirmed private model code. **No counterexample found**, searches enumerated | cpsc.gov/s3fs-public/516.pdf; cpsc.gov safety-guide page; cpsc.gov Regulations-Mandatory-Standards-Bans; ecfr.gov search API; justia (Kaiser D. Del.) | High |

Chairman reconciliation note: V4 cited the *Kaiser* district-court posture ("not a consumer product") as part of its negative case without noting the Third Circuit's reversal; V2's fuller litigation account supersedes that framing. The bottom line (no mandate) is unaffected and independently supported by V4's CFR/statute searches. No claim in the synthesis rests on the superseded framing.

### Errors caught (proof the error-hunt rule ran)
25/25 reviews contained an explicit error hunt or "none found + what was checked." Distinct material issues raised in review — with verification outcomes:
1. **E: *Kaiser* attributed to the 4th Circuit inside a "courts are high-confidence" vouch** (caught by all 5 reviewers) → confirmed error; 3d Cir.
2. **A & C: § 3280 restriction as "smaller than 8 AWG"** (all 5) → confirmed wrong; flat ban.
3. **A/B/D: stale NSPIRE HCV dates (~Oct 2024)** (all 5, who leaned to C's Oct 1 2025) → everyone stale, reviewers included; current = Feb 1, 2027.
4. **E: conflating *Kaiser* with the § 12 suit** (all 5, flagged "probable") → confirmed conflation — but the reviewers' preferred § 15 account (B's) was **also** wrong: *Kaiser* was a § 7 proceeding challenge, and the 3d Cir. ruled *for* CPSC on the threshold question.
5. **C: "never issued — and could not issue —" jurisdictional overreach** (R3, R4) → partly confirmed: no rule was ever issued, but the flat "could not" overstates — CPSC won the consumer-product question as to the wire; the systems-level § 12 theory failed on the D.C. Circuit's narrower test.
6. **C: 445 F. Supp. 486 characterized as the § 12 dismissal** (R2 flagged the date; its 1978 guess was itself wrong — 1977) → confirmed mischaracterization; 486 was subpoena enforcement, and the § 12 court *upheld* jurisdiction.
Errors the review round **missed** and only verification caught: (7) all five members' § 3280.808 citation (actual: § 3280.801(e)); (8) the "free of electrical hazards" phrase attributed to 982.401 (actual home: UPCS 5.703(f)). Items 3, 4, 7, 8 are the run's standing exhibit against convergence theater and majority-vote truth: five same-model members and five same-model reviewers shared the same blind spots, and only primary evidence broke them — exactly the Tier-C weakness the protocol's verification round exists to compensate.

### Rebuttal round: not run (optional under Step 4; decision disclosed)
The sizing-guidance trigger (error-hunt hits landed) was met, but every hit was a citation/date-level issue settled conclusively by the primary-source verification round, the unanimous bottom line was never contested, and deliberation is bounded at two rounds by design. A member-revision round could add convergence pressure but no evidence the chairman did not already hold. Corrections were applied directly from the verified primary record instead.

### Cost disclosure
15 model calls total ≈ 15× a single answer (baseline estimate for a 5-seat FULL council was N+2 ≈ 7×; the 4-dispatch verification round and 5-seat review round account for the rest):
- 5 member answers (0 tool uses; ≈241k subagent tokens)
- 5 review passes (1 file-read each; ≈364k subagent tokens)
- 4 verification dispatches (124 tool uses incl. web search/fetch; ≈328k subagent tokens)
- 1 chairman synthesis (orchestrator session)
Total ≈ 933k subagent tokens + orchestration overhead. Per charter, cost was disclosed and was not a gate.

---

```yaml
JAIL-HANDOFF:
  skill: jail-council
  status: complete
  facts:
    - "No US federal statute or binding federal regulation requires private residential landlords to replace aluminum branch-circuit wiring — verified 2026-07-22 via CFR-wide full-text search (0 hits 'aluminum wiring'), CPSC's mandatory-standards list (absent), CPSC Pub. 516's advisory framing, and the 1970s litigation record"
    - "CPSC Pub. 516 is advisory: recommends copper rewire or per-connection COPALUM repair (AlumiConn alternative); rejects wire-nut pigtailing; calls CO/ALR devices 'an incomplete repair'; 55x fire-hazard finding attributed to Franklin Research Institute (cpsc.gov/s3fs-public/516.pdf)"
    - "24 CFR 3280.801(e) flatly bars aluminum (incl. copper-clad) branch-circuit conductors — but only as a construction standard for new manufactured homes (built on/after 1976-06-15); no landlord retrofit duty (eCFR/LII/GPO, three-way verbatim match)"
    - "Kaiser Aluminum v. CPSC, 574 F.2d 178 (3d Cir. 1978) held aluminum branch wiring IS a consumer product; the § 12 repair suit failed under CPSC v. Anaconda, 593 F.2d 1314 (D.C. Cir. 1979) distinct-article-of-commerce test; no repair order or 16 CFR standard ever issued"
    - "HUD assisted-housing standards (HQS/NSPIRE) are hazard-based participation conditions; 'aluminum' appears nowhere in the NSPIRE electrical standards; HCV/PBV NSPIRE compliance currently extended to 2027-02-01 (90 FR 46911)"
    - "NEC (NFPA 70) is a private model code — law only via state/local adoption; not federal law"
  assumptions:
    - "Scope as framed in Step 0: privately owned US residential rentals; 'federal law' = statutes + binding federal regulations, distinguished from model codes, state/local law, program conditions, and lender/insurer requirements"
  unknowns:
    - "Exact post-remand termination of the § 12 Anaconda suit (single secondary source: abandoned ~early 1982; no primary docket checked)"
    - "Whether FHA/VA/USDA handbook texts name aluminum wiring specifically (transaction conditions either way, not general law)"
    - "Universal-negative caveat: well-searched absence, not a provable absolute"
  outputs:
    - "out-c1-council.md (this council answer, with audit appendix)"
    - "council-packet-anon.md (anonymized blind answers A–E, audit trail)"
  evidence:
    - "CPSC Pub. 516 · advisory status + repair recommendations + 55x finding · https://www.cpsc.gov/s3fs-public/516.pdf · 2026-07-22"
    - "eCFR 24 CFR 3280.801(e) · verbatim aluminum branch-circuit ban, new manufactured homes · https://www.ecfr.gov/current/title-24/subtitle-B/chapter-XX/part-3280/subpart-I/section-3280.801 · 2026-07-22"
    - "574 F.2d 178 (3d Cir. 1978) · wiring IS a consumer product; § 7 posture · https://openjurist.org/574/f2d/178 · 2026-07-22"
    - "593 F.2d 1314 (D.C. Cir. 1979) · distinct-article test; repair relief never reached · https://law.justia.com/cases/federal/appellate-courts/F2/593/1314/111209/ · 2026-07-22"
    - "88 FR 30442; 88 FR 66882; 89 FR 55645; 90 FR 46911 · NSPIRE rule + HCV/PBV compliance-date chain to 2027-02-01 · federalregister.gov · 2026-07-22"
    - "eCFR full-text search · 'aluminum wiring' = 0 hits CFR-wide · https://www.ecfr.gov/api/search/v1/results?query=%22aluminum+wiring%22 · 2026-07-22"
  risks:
    - "Not legal advice: state/local codes, habitability doctrine, subsidy-program participation, lenders, or insurers can still compel remediation for a specific property"
    - "Tier C seating: same-model members share blind spots — demonstrated in-run (universal 3280.808 miscite; shared litigation misframe) and compensated by the primary-source verification round"
    - "Doing nothing about known pre-1972 aluminum wiring carries real fire risk and insurer consequences even though federal law is silent (Rule 12)"
  confidence: high
  next: "jail-verify — optional independent check of this synthesis if stakes warrant; jail-decide if choosing among remediation options (rewire vs COPALUM vs AlumiConn)"
  approval_required: []
```
