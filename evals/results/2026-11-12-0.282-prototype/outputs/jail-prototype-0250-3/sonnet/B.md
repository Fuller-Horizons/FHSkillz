The page is built, but the question isn't answered yet. The team's picks on Thursday are what answer it, so the verdict stays open until then.

**Question:** Which weekly scorecard layout lets an owner see what needs attention in 30 seconds?

**Page:** `/tmp/claude-0/-tmp-fhlive-lynkp5d3/49e62817-4d2d-4703-8fb4-5761e3346fc7/scratchpad/proto-weekly-scorecard.html`. It is one self-contained file you open by double-click, and it has three layouts behind one switch.
- **A, Traffic-light list:** each metric is a row with a green, amber or red dot.
- **B, Headline + 3 tiles:** a one-sentence summary, three big tiles for what's off, and a small table for everything else.
- **C, Six-week trends:** a sparkline per metric, so direction shows rather than a single status.

Every commentable block carries a number (`#1` to `#7`). The bottom has a pick control, a "what did you read first?" box, and a **Copy my answers** button.

**Things to know:**
- **Sample data:** the company and numbers are invented, because I don't know which client or internal scorecard this is for. If you tell me, I'll regenerate with that metric set. Real data would stay out of the file anyway.
- **Look:** it uses a plain white owner-report style with one accent colour. I found no Signal Results Group brand files, so say if you want that look instead.
- **Ledger:** the project tools weren't available in this session, so I couldn't read `claude/spike-ledger.md`. I can't rule out that this question was already answered. Please check that file or tell me what it says.
- **Lint:** `artifact-lint` needed an approval that wasn't granted, so the page hasn't been machine-checked. I built it from the skill's template, but the only check on it so far is that read-through.
- **Browser check:** I haven't opened it in a browser, directly or in a sandboxed frame, so that is also unchecked.
- **Template quirk:** I couldn't copy the template file because of a permissions block, so I wrote the page directly. The only changes are the week date and the sample company name.

**Before Thursday:**
1. Open the file locally. Ask each person to pick a layout and press Copy my answers.
2. Paste their blocks back here (they look like `PICK: B · READ FIRST: … · NOTES: #3 too long`). That pasted text is the evidence for the verdict. I then write the SPIKE VERDICT and the ledger line.
3. If you'd rather the team review it inside Claude, I can publish it as a private artifact. I haven't, because that puts it on claude.ai. Tell me to go ahead if you want that.

```
JAIL-HANDOFF:
  skill: jail-prototype
  status: partial
  assumptions: [sample data stands in for the real scorecard; neutral design direction]
  unknowns: [ledger prior art; which client/metrics; team's pick]
  outputs: [review page: the scratchpad path above]
  evidence: []
  next: jail-decide
  approval_required: [publishing the page as an artifact; running artifact-lint]
  tested: untested - lint needs approval; no browser check yet
```