# Decision package (provisional: the evidence is thin)

**Decision:** How to protect the firm's 7-year-old server through tax season, and what it runs on for the next ~5 years.
**Owner:** The firm principal who signs the contract (you; confirm).
**Needed by:** Decision by Dec 1, 2026 (my suggestion). Hard date: Jan 15, 2027. That is 9 weeks away.

**Criteria (set before options, unweighted because the evidence is too thin for weights):**
1. Stays running Jan 15–Apr 15.
2. Line-of-business apps keep working (hard constraint).
3. Client data protected. The FTC Safeguards Rule likely applies to tax preparers: written security plan, MFA, encryption, vendor oversight. Confirm with your compliance advisor.
4. Five-year total cost.
5. Reversibility.
6. Staff disruption.

**Evidence:**
- *Facts (your input):* 9 users. Server is 7 years old. Server option is $13k including setup, ~5-year life. M365 is $38/user/month, or $4,104/year. IT lead says failure is possible any month (his judgment, not a measurement).
- *Unknown:* which apps run on the server, backup status, whether you already pay for Microsoft 365, and the actual failure odds.
- *Judged on assumption:* criterion 2 (app fit) and failure risk.

**Options**

| Option | Benefits | Costs | Risks | Door | Cost of delay |
|---|---|---|---|---|---|
| A. Keep old server, no change | No spend | $0 now; outage cost unpriced | Failure any month; restore untested | Failure is one-way | Full exposure every month |
| B. Bridge: verified backup + spare plan now, decide after Apr 15 | Cheap; protects the season | Small, unquoted | Old hardware can still fail | Two-way | Lower exposure, decision slips |
| C. New server | Local apps keep working | $13k, plus unquoted Windows, backup, and IT costs | Tight install window | One-way (capex) | Migration weeks add risk |
| D. Microsoft 365 + SharePoint (+ cloud desktop if apps need it) | No hardware; cloud backup | $4,104/yr quoted; migration labor | Apps needing a local server won't move | Contract two-way; data move mostly one-way | Must start by mid-Dec |

Outage cost: each down day ≈ 9 staff × 8 hr × loaded rate. At an assumed $50/hr (Estimate; replace with your number), that is ~$3,600/day. Missed-deadline penalties are not included.

**Recommendation:** B now, with C or D chosen by Dec 1. Cloud is cheaper on sticker price over 5 years ($20.5k vs. $13k before running costs), but the server's running costs narrow that gap. C vs. D is a tie on the evidence, broken by criterion 2 (app fit), then criterion 1 (no migration during the season). Price should not decide it; fit should.

**Confidence:** Low. App dependency and failure odds are unknown.

**Would change this call:**
1. Apps need a local Windows server or database → D works only with a cloud-hosted desktop, so price that or choose C.
2. IT lead says failure is weeks away, or the restore test fails → skip B and buy C now.
3. All-in M365 cost (migration, security add-ons) exceeds C's all-in 5-year cost → favor C.
4. Apps run in the cloud and the restore test passes → D, migrating after Apr 15.

**Approval required:** $13k spend; the M365 contract term; any data migration.

**Next actions:**
1. IT lead, by Nov 21: written list of apps and their OS/hardware needs, backup status, and his failure estimate.
2. IT lead, by Nov 30: full restore of the server to a spare machine or cloud copy, with proof it works.
3. You, by Dec 1: written quotes for (a) M365 with what $38 covers and migration, (b) cloud desktop if needed, (c) server with Windows, backup, and 5-year support. Then choose C or D.

Practical timing (my estimate): start any change by mid-December and freeze changes before the Jan 15 filing rush.

**Ship-check:** criteria-first PASS · do-nothing priced PASS · door type per option PASS · ≥2 change-conditions PASS · every number carries Fact/Estimate+source PASS · owner named PASS (by role; confirm the name) · council check recorded PASS

**Council:** Not convened. There is no disputed factual question; the gaps are facts only you and the IT lead can supply.

**Decision log (proposed):** context: 9-person accounting firm; 7-year-old server at risk before Jan 15, 2027 · decision: bridge now (B), choose C or D by Dec 1 · consequences: no migration during tax season; C vs. D decided by app fit · status: proposed

```
JAIL-HANDOFF
from: jail-decide
next: jail-research (app inventory, M365 scope, restore evidence) → jail-red-team (before any spend)
status: provisional, confidence low
```

I can draft the message to your IT lead with the three questions above if you want it.