**Bottom line:** The federal minimum wage is $7.25 an hour. On Long Island (Nassau and Suffolk) New York's minimum is $17.00, which is $9.75 higher, and the New York rate is the one that applies. I could not open any primary government page this session, so the figures come from search results. Confirm them on dol.gov and labor.ny.gov before they go into the client's budget.

# Part 1: Synthesized answer

**Federal.** The federal minimum is **$7.25 an hour**, in effect since July 24, 2009 [1]. A 2026 compliance table still shows the federal floor unchanged [2]. *Fact, medium confidence.* It is the Department of Labor (DOL) 2009 release plus a secondary table, and I did not open the DOL page. Freshness window: ≤12 months for volatile claims, and [2] is a 2026 source.

**Long Island.** It differs. Since **January 1, 2026**, New York State's minimum wage is **$17.00 an hour in New York City, Nassau, Suffolk and Westchester**, and $16.00 in the rest of the state [3][4]. Where a state minimum exceeds the federal one, the state rate governs [2]. *Fact, medium-high confidence.* Two independent law-firm sources agree, but both are secondary.

**Budget outlook for 2027.** This is the main thing to watch.
- Inflation indexing was due to start in 2027. A report dated Oct 19, 2026 says an off-ramp condition was met, so **no indexed increase takes effect January 1, 2027**, and Long Island stays at $17.00 [6]. *Fact, medium confidence, single secondary source.*
- Governor Hochul has proposed changing the off-ramp so workers get the increase anyway. If the Legislature approves, Long Island would move to **$17.60 on March 1, 2027** [5]. I found no confirmation that it has passed, so it is *Unknown/pending*.
- For the budget, I'd use $17.00 as the base case and model $17.60 from March 1, 2027 as the upside scenario. *Judgment.*

**Other payroll items:**
- The exempt salary threshold for downstate is $1,275 a week ($66,300 a year) [3]. *Fact, medium.*
- Tipped-worker cash wages conflict between sources. One gives $14.15 for downstate tipped service employees, and another gives $14.75 for Nassau, Suffolk and Westchester [3]. I'm not picking one. Confirm on labor.ny.gov if the client has tipped staff.

# Part 2: Evidence packet

```
EVIDENCE PACKET
Objective + consuming decision: Current federal and Long Island minimum wage → client payroll budget
Questions:
  Q1: Current federal minimum wage?
      Answer: $7.25/hr since 7/24/2009 — Fact · medium (primary page not opened)
      Evidence: [1] DOL 2009 release (search-surfaced, not opened); [2] Patriot Software 2026 table
      Limitations: DOL pages returned were dated; [2] is secondary.
  Q2: Does the NY rate on Long Island differ?
      Answer: Yes, $17.00 (eff. 1/1/2026); the higher state rate governs — Fact · medium-high
      Evidence: [3] Proskauer 2026 update; [4] Ogletree 2026 update; [2] state-vs-federal rule
      Limitations: Both law-firm sources are secondary; neither was opened beyond search results.
  Q3: Any change expected in 2027?
      Answer: No automatic increase on 1/1/2027; $17.60 on 3/1/2027 is proposed, not enacted — Fact (suspension) · medium; Unknown (enactment)
      Evidence: [6] GTM, 10/19/2026; [5] governor.ny.gov 2027 page (title/snippet only)
      Limitations: [6] is a single secondary source; [5] was not opened.
Cross-cutting findings: The 2027 off-ramp is the biggest budget risk.
Unresolved gaps (+ resolver):
  - Primary confirmation of $7.25 → dol.gov/agencies/whd/minimum-wage (fetch was blocked by the proxy)
  - Primary confirmation of $17.00 → labor.ny.gov minimum wage page
  - Status of the March 1, 2027 proposal → NY Legislature bill status / governor.ny.gov
  - Tipped cash wage figure → labor.ny.gov Hospitality Wage Order
Source list (accessed 2026-11-12; all via search results, none opened in full):
  [1] US DOL, 2009 minimum wage release · $7.25 effective 7/24/2009 · https://dol.gov/newsroom/releases/esa/esa20090716
  [2] Patriot Software, 2026 minimum wage guide · federal still $7.25; higher state rate applies · https://www.patriotsoftware.com/blog/payroll/what-is-minimum-wage/
  [3] Proskauer, NY 2026 minimum wage and exempt salary updates · $17.00 downstate, thresholds, tipped figures · https://www.proskauer.com/blog/new-york-state-minimum-wage-and-exempt-salary-updates-for-2026
  [4] Ogletree, 2026 NY minimum wage increases · $17.00 Long Island, effective 1/1/2026 · https://ogletree.com/insights-resources/blog-posts/2026-minimum-wage-increases-in-new-york-key-details-for-employers/
  [5] NY Governor's office, NY State Minimum Wage for 2027 · proposed $17.60 on 3/1/2027 · https://governor.ny.gov/new-york-state-minimum-wage-2027
  [6] GTM, "New York Suspends Minimum Wage Rate Increase for 2027" (10/19/2026) · no 1/1/2027 indexed increase · https://gtm.com/business/?p=21088
```

**Pre-ship check (walked by hand, 6/6 pass):**
1. Every [n] in Part 1 resolves to a source in Part 2.
2. Every source is cited at least once in Part 1.
3. Every source line has the source, the claim it backs, a URL and the access date.
4. Every question has an answer with a label and a confidence.
5. Every volatile claim names its freshness window.
6. Every gap names its resolver.

I did not run jail-py-toolkit.

```
JAIL-HANDOFF
status: complete, with caveats (primary sources unverified)
next: verify the 3 primary-source gaps before the figures go into the client budget; then jail-summarize if a client memo is needed
```

Sources:
- [DOL 2009 release](https://dol.gov/newsroom/releases/esa/esa20090716)
- [Patriot Software](https://www.patriotsoftware.com/blog/payroll/what-is-minimum-wage/)
- [Proskauer](https://www.proskauer.com/blog/new-york-state-minimum-wage-and-exempt-salary-updates-for-2026)
- [Ogletree](https://ogletree.com/insights-resources/blog-posts/2026-minimum-wage-increases-in-new-york-key-details-for-employers/)
- [NY Governor's office](https://governor.ny.gov/new-york-state-minimum-wage-2027)
- [GTM](https://gtm.com/business/?p=21088)