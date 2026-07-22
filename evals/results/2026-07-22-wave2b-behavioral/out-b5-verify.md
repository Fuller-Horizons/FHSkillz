**Routing note:** a score out of 10 is a rating job, not a verification job. jail-verify checks finished work against its contract (pass/fail, ship or fix) and explicitly hands numeric quality scores to **jail-rate** — so that's the skill running now.

**One blocker before any number: the report never reached me.** There's no paste, attachment, or file in this conversation — "this finished report" points at nothing I can inspect. A rating has to come from evidence, and I won't invent a score for a document I haven't seen (an unsupported score would just be a confident guess dressed as a number).

**To score it, send me:**

1. **The report itself** — paste the text or attach the file.
2. **Purpose and audience** — who it's for and what it's supposed to accomplish (this tunes the rubric weights).
3. **The original ask or spec it was written against**, if one exists — so "completeness" is measured against something testable instead of my guess at the assignment.

**The rubric it will be scored against** — declared now, before any scoring, so you can challenge or reweight it. Default Content/media (report) rubric; weights sum to 100%:

| Dimension | Weight | What I'll check |
|---|:---:|---|
| Accuracy & grounding | 30% | Spot-check its claims against the sources it cites (and primary sources where consequential) |
| Depth & completeness | 20% | Coverage vs. what the ask/spec required and the best comparable treatments |
| Clarity & craft | 20% | Structure, prose quality, fit for the stated audience |
| Originality | 15% | What it adds beyond existing work on the topic |
| Usefulness / actionability | 15% | Whether the audience can actually do something with it |

What you'll get back: this rubric → an evidence-cited scorecard → **overall X.X/10** → ranked fixes → a projected score if the fixes land (current → potential, clearly labeled an estimate). If you only want the headline, say "quick take" and you'll get a single line — `X.X/10 — one-sentence why + strongest evidence` — with the full scorecard on offer.

**One flag worth raising:** you called it *finished*. If the real question behind this is "is it safe to send?" — claims hold up, nothing contradicts itself, numbers recompute, every deliverable from the original ask is present — that is exactly jail-verify's job, and I can run it in the same pass on the same inputs (item 3 matters most for that). Say "rate + verify" and you'll get both: the 0–10 score and a PASS / FAIL / PASS-WITH-FLAGS ship-check.

```yaml
JAIL-HANDOFF:
  skill: jail-rate            # routed here from jail-verify — numeric scores are outside verify's scope
  status: blocked
  facts: ["No report artifact is present in this session — no paste, attachment, or file (source: this conversation)"]
  unknowns: ["The report itself", "Its purpose and intended audience", "The spec/original ask it was written against"]
  outputs: ["Declared default rubric (Content/media) — awaiting the subject"]
  risks: ["Scoring without the artifact would fabricate a rating — declined until the report is supplied"]
  confidence: high            # in the routing and the blocker; no confidence is claimed in any score yet
  next: "You supply the report + context → jail-rate scores it; add the jail-verify ship-check on request"
  approval_required: []
```
