# Federal vs. Long Island minimum wage: provisional answer

**Status: provisional.** I could not open any primary page this session. The fetch tool returned "proxy refused the connection" on all four attempts, and the Bash check of the proxy needed approval I didn't have. The rule is that a source I can't open isn't cited as fact. So everything below comes from the search engine's summaries of official pages and is labeled **Estimate**, not Fact. Please check the three links before the budget is final.

## Part 1: Answer

- **Federal:** The minimum wage is **$7.25/hour**, effective July 24, 2009. The search summary of the U.S. Department of Labor pages found no change to it [1]. *Estimate, medium-high confidence.* Search results consistently report this rate, and no result I saw shows a change.
- **Long Island:** Yes, it differs. New York sets a higher rate for Nassau and Suffolk, which is **$17.00/hour**. The rest of the state is $16.00 [2][3]. The search summary only stated this rate explicitly for Jan 1, 2027. I did not see a statement of the 2026 rate, so the 2026 figure rests on the 2027 text saying the rate "stays" at $17.00. *Estimate, medium confidence.*
- **Higher rate controls:** Where state and federal law both apply, the employee gets the higher rate [1]. For Long Island payroll, budget on the NY rate, not $7.25.
- **2027:** The summary says no inflation increase applies on Jan 1, 2027, because an "off-ramp" condition was met [3]. It also says Governor Hochul has *proposed* indexing that could raise Long Island to about $17.60 from March 1, 2027, if the Legislature approves [3]. *Estimate, low confidence.* I could not confirm whether it passed, so treat $17.60 as a possible scenario, not a planning rate.
- **Tipped workers (Long Island):** The summary lists a $14.15 cash wage for tipped service employees and $11.35 for tipped food service workers [2]. *Estimate, low-medium confidence.*
- **Home care aides** have a separate, higher rate, $20.00 on Long Island [3]. *Estimate, low-medium confidence.*

**Freshness window applied:** Wage rates are volatile, so the window is 3 months or less. Every source was surfaced by search on 2026-11-12, but none was opened, so I could not confirm the pages' own dates.

## Part 2: Evidence packet

```
EVIDENCE PACKET
Objective + consuming decision: Current federal and Long Island minimum wage,
  to set a client's payroll budget.
Q1: Current federal minimum wage?
    Answer: $7.25/hr, effective 7/24/2009 — Estimate · medium-high
    Evidence: [1]
    Limits: search summary only; page not opened; DOL pages may show old cached dates.
Q2: Does NY's Long Island rate differ?
    Answer: Yes, $17.00 vs. $7.25 federal; higher rate governs — Estimate · medium
    Evidence: [2][3]
    Limits: 2026 rate inferred from the 2027 "stays at $17" text; pages not opened.
Q3 (added): What changes in 2027?
    Answer: No Jan 1 increase; the Mar 2027 ~$17.60 is a proposal only — Estimate · low
    Evidence: [3]
Cross-cutting findings: No contradictions seen between sources.
Unresolved gaps (+ resolver):
  - Primary pages unopened → retry fetch when the proxy works, or open the 3 URLs by hand.
  - Whether the March 2027 increase passed → check dol.ny.gov/minimum-wage and the Governor's page.
  - Employer-specific rules (exemptions, overtime, tip credit eligibility) → not researched.
Source list (all accessed via search summary 2026-11-12; none opened):
  [1] US DOL Wage and Hour Division, Minimum Wage — federal $7.25; higher rate governs
      https://www.dol.gov/agencies/whd/minimum-wage
  [2] NY State DOL, "Your New York State Minimum Wage" — $17 LI; tipped rates
      https://dol.ny.gov/minimum-wage
  [3] NY Governor's Office, "New York State Minimum Wage for 2027" — 2027 flat; March proposal
      https://www.governor.ny.gov/new-york-state-minimum-wage-2027
```

**Pre-ship check:** The citations and labels pass the checks. Check 3 (each source line carries date accessed, URL, and the claim it backs) passes on form only, since the sources are unopened. Check 5 (the freshness window is named) also passes. The packet is not fully clean because the primary pages remain unopened. I did not run `cite-check.py`, so I walked the six assertions by hand.

```
JAIL-HANDOFF
status: provisional — verify primary sources before client use
next: jail-verify (after the 3 URLs are opened) or jail-summarize for the client copy
open items: 2026 LI rate confirmation; March 2027 indexing status
```

**Suggested budget rate:** $17.00/hr for Long Island non-exempt staff, with a sensitivity case at $17.60 for 2027. The rate is also the base for employer payroll taxes and overtime, so apply it there too.

Sources:
- [US DOL – Minimum Wage](https://www.dol.gov/agencies/whd/minimum-wage)
- [NY DOL – Your New York State Minimum Wage](https://dol.ny.gov/minimum-wage)
- [NY Governor – New York State Minimum Wage for 2027](https://www.governor.ny.gov/new-york-state-minimum-wage-2027)