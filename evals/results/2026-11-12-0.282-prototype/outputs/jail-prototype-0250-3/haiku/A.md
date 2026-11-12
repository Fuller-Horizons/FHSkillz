I built three scorecard layouts in one throwaway HTML file. The team can click between them on Thursday. The numbers are placeholders, so the real KPIs still need to go in.

**File:** `/tmp/claude-0/-tmp-fhlive-kozoryjp/49f560c9-d4ec-403a-96dc-d5b1549c87c0/scratchpad/proto-scorecard-options.html`

Open it in a browser. Switch between layouts with the buttons or by adding `#A`, `#B` or `#C` to the URL. The default is set in one constant at the top of the script.

**Question being answered:** Which layout makes the weekly scorecard fastest to scan and act on?

- **A · Status table:** one row per KPI with owner, target, actual, gap, status pill and an 8-week sparkline. Densest, closest to a spreadsheet.
- **B · Headline tiles:** one large number per KPI with its status and trend. Best for a quick read, weakest for seeing gaps side by side.
- **C · Exceptions first:** off-target KPIs as cards with an owner action field, and on-target KPIs collapsed to one line. Built around what needs discussion Thursday.

All three show the same six KPIs: pipeline, proposals sent, discovery calls, win rate, utilization and on-time delivery. Each status is green at or above target, amber within 90%, and red below that.

**What I did not do:**
- **Ledger check:** the project tools aren't available in this session, and the working directory is empty, so I could not read the spike ledger or any existing scorecard doc. Nothing was written to the ledger.
- **Browser check:** I did not run the page. A syntax check was blocked by a permission prompt, so open it once to confirm it renders.

**Verdict block (provisional):**
```
SPIKE VERDICT
QUESTION:     Which of three layouts makes the weekly scorecard scannable and actionable?
SHAPE:        look
TIMEBOX:      one session → one session
LEDGER-CHECK: unverified (project ledger not accessible this session)
EVIDENCE:     not yet observed. Needs the team's pick on Thursday.
VERDICT:      inconclusive
ARCHIVE:      /tmp/claude-0/-tmp-fhlive-kozoryjp/49f560c9-d4ec-403a-96dc-d5b1549c87c0/scratchpad/proto-scorecard-options.html
CONSUMER:     jail-decide
```

It ships as inconclusive because the ledger check failed and no one has picked a layout yet. Once the team chooses, record the decision as a ledger entry and feed it to jail-decide.

**Needed from you:**
1. The real weekly KPIs, targets and owners. I can swap them into the data block.
2. Whether the team's direction is "higher is better" for every KPI. Some, like cost or days-to-close, need the status logic reversed.