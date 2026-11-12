# DECISION PACKAGE

**Decision:** How to keep the firm's files and software running through tax season. The choices are a new server, M365 + SharePoint, or the old server.
**Owner:** Managing partner (you)
**Needed by:** Jan 15 (your date). The real order date is earlier, so ask IT for the lead time.

**Criteria (unweighted, because the evidence is thin):**
1. Downtime risk, Jan 15 to Apr 15.
2. Change risk before the season, since 9 people would have to learn new workflows.
3. Five-year cost.
4. Works with our tax and accounting software.
5. Reversibility.

| Option | Costs | Risks | Door | Delay cost |
|---|---|---|---|---|
| **Do nothing (old server)** | $0 now (Fact) | The IT guy says it could die any month (Estimate, no diagnostics seen). If it fails in season, 9 people sit idle. Cost = idle hours × your billing rate (Unknown). | Two-way | Each week shrinks the window to fix it before Jan 15. |
| **Old server now, migrate after Apr 15** | $0 now, migration cost later (Unknown) | Same failure risk as above, through the whole season. | Two-way | Same as above. |
| **New server** | $13,000 up front (Fact, yours), about $2,600/yr over 5 years. Backup, licenses and support are excluded (Unknown). | Hardware lock-in. It could be wasted if you go cloud in 2027. | Mostly one-way (the money is sunk) | Low once ordered. |
| **M365 + SharePoint** | 9 × $38 × 12 = $4,104/yr, or $20,520 over 5 years (calc from your figure). Migration labor and hosted-app fees are excluded (Unknown). | A big workflow change in 9 weeks. M365 may not replace server-based tax or QuickBooks software. | Two-way (cancel any month), though the data move takes effort. | Moving 9 people's workflows during prep is the main risk. |

**Break-even:** On your stated numbers, the server is $7,520 cheaper over 5 years. M365 wins if the server's hidden yearly costs (backup, licenses, support, power) exceed about $1,500/yr.

**Recommendation:** Buy the new server now. Before Jan 15, the biggest losses come from downtime and from changing how 9 people work mid-prep. A like-for-like swap limits both. It is also cheaper on the numbers you gave, unless hidden costs pass $1,500/yr. You can still add M365 later for email and collaboration (two-way door).

**Confidence: Low.** Three facts that decide the call are not known. Those are which apps need a local server, what IT's "might die" is based on, and the server's true yearly extras.

**Would change this call:**
- Your tax and accounting software is already cloud-hosted, or the vendor offers hosting. That favors M365.
- Server extras come in above $1,500/yr. That favors M365.
- IT's diagnostics show healthy drives and a tested backup. That favors keeping the old server through the season.
- A new server can't be live by about Jan 5. That favors keeping the old server and stabilizing it.

**Approval required:** You authorize the $13k purchase.

**Next actions:**
1. **IT guy, this week:** run a full backup and a test restore of the old server, and send you the drive health report. This is worth doing under every option.
2. **You:** ask IT for the three missing facts and the vendor lead time.
3. **Jail-research:** check what your tax and accounting software requires for hosting.

**Council:** not convened. The gap is missing evidence, not a disputed fact.

**Ship-check:** criteria-first PASS · do-nothing priced PASS · door type per option PASS · ≥2 change-conditions PASS · every number carries Fact/Estimate+source PASS · owner named PASS · council check recorded PASS

**JAIL-HANDOFF**
- next: jail-research (missing facts), then jail-red-team (money at stake)
- open unknowns: the apps that need the server, the basis for IT's failure warning, the server's yearly extras, the vendor lead time
- decision log: `context: 9-person firm, 7-yr-old server, season Jan 15 · decision: new server (low confidence) · consequences: $13k, 5-yr lock-in · status: proposed`

I can save this to the Business Consulting Tools project or turn it into a client-ready document if you want either.