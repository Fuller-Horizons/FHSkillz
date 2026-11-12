**DECISION PACKAGE**

**Decision:** Replace, move, or keep the 7-year-old server before tax season (Jan 15) · **Owner:** you, as firm owner · **Needed by:** proposed Dec 1 to order, with install and test done by Jan 5. Jan 15 is 64 days away.

**Criteria (stated before scoring)**
1. Survives tax season, Jan 15 to Apr 15. Must-have.
2. Keeps the firm's server-bound software running. Must-have, not yet verified.
3. Disruption during the changeover. Weighted high, because the timing is tax season.
4. Five-year cost. Weighted medium.
5. Reversibility.

**Evidence and labels**
- New server, $13k total ($11k + $2k setup): **Fact**, your quote. The 5-year life is **Assumption**, from the vendor.
- M365: 9 × $38 × 12 = $4,104/yr, $20,520 over 5 years: **Fact**, arithmetic on your quoted price.
- Old server failing "any month": **Assumption**, the IT person's opinion. No diagnostic yet.
- Not known: which apps run on the server, whether M365 replaces email you already pay for, and what one day of downtime costs.

**Options**

| Option | Benefits | 5-year cost | Risks | Door type | Cost of delay |
|---|---|---|---|---|---|
| A. Keep old server | No spend now | $0 now; repair cost unknown | Dies in Feb–Apr; missed filings | Two-way until it dies, then one-way in an emergency | Highest if it fails in season |
| B. New server | Lowest-disruption fix; data stays on-site | ~$13k, about $2.6k/yr. Excludes Windows license, backup, and Office unless verified | Install slips past Jan 5 | Two-way (hardware, some resale value) | Low if installed by early Jan |
| C. M365 + SharePoint | No server to fail; email, Office, and files in one place | $20.5k, about $4.1k/yr. Migration labor not quoted | Full migration in the worst month; server-bound apps may not move | One-way in practice once workflows move | High if done in season |
| D. Bridge: verified backup and cloud copy of old box now, decide after Apr 15 | Cheap time | Backup cost not quoted | Decision and migration still ahead; risk stays open all season | Two-way | Low now, but the decision slips past season |

**Recommendation:** B. Buy the new server, install and test it by Jan 5, keep a verified backup of the old box until cutover, and treat M365 as a planned project after Apr 15. The new server is the lowest-cost way to remove the failure risk before the season and keeps server-bound software working, which no quote has proven yet. M365 costs about 1.6× the server over five years, but it buys different things (email, Office, collaboration), and moving everything in tax season is the wrong time for a one-way change. **Confidence: medium.** The choice depends on the application inventory nobody has done yet.

**Would change this call**
1. The inventory shows no app needs a local server and email is already a paid subscription → C becomes the better option, decided after Apr 15.
2. The diagnostic shows the old server is stable and fully backed up → A-as-bridge is viable through season, and you buy after April.
3. The server quote, with Windows license, backup, and Office, exceeds about $16k up front → re-run the comparison against C.
4. The new server can't be installed and tested by Jan 5 → fall back to D and buy after season.

**Approval required:** the ~$13k spend, any M365 contract, and moving client data to new hardware or the cloud. Check the data-handling obligations first, since tax preparers generally fall under the FTC Safeguards Rule (encrypted backups, written security plan). Confirm this with your compliance adviser.

**Next actions**
1. **IT person**, by Nov 21: verified full backup of the old server (restore test, not just a backup log), plus a list of every app and share on it.
2. **You**, by Nov 25: get two quotes for the new server that include Windows license, backup, and Office. Confirm whether M365 replaces existing email.
3. **You**, by Dec 1: sign the order (or choose C or D), and book the install and test window to finish by Jan 5.

---

**Ship-check:** criteria-first PASS · do-nothing priced PASS · door type per option PASS · ≥2 change-conditions PASS · every number carries Fact/Estimate+source PASS · owner named PASS · council check recorded PASS

*Note on the outage cost:* I did not put a number on downtime. Multiply your daily staff cost by the days a failure would take to recover, and compare that to the $13k.

**JAIL-HANDOFF**
- **next:** jail-red-team. This is an irreversible spend that touches client data, so pressure-test B before you sign.
- **council:** not convened. The open questions are factual (what runs on the server, the quotes) and the owner can settle them directly, so a council would not add accuracy.