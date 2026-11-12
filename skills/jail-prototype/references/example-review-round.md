# Worked example: a look question, one review round

Synthetic scenario; the company and numbers are sample data. The page is
[example-scorecard-layouts.html](example-scorecard-layouts.html).

## Input

> I can't tell what the weekly scorecard for my HVAC clients should look
> like. Mock up some options so I can pick one before Thursday.

## Reply 1 (before building)

**Ledger:** searched the SPIKE LEDGER for scorecard layout questions; none
found (LEDGER-CHECK: none).

**Question (confirm or edit):** *Which weekly scorecard layout lets an owner
see what needs attention in 30 seconds?* That's a **look** question, so I'll
build one review page with three radically different layouts: a traffic-light
list, a headline with three tiles, and six-week trends. Timebox: one session
and one feedback round, with one extension declared in case the first round
is split.

**Design direction:** no client brand files were provided, so plain
owner-report style: white page, one accent colour, system fonts. Sample data
only.

## Reply 2 (page built)

Built `proto-weekly-scorecard.html` (single file, no outside requests).
`artifact-lint.py --look`: PASS, 0 warnings. Checked in a browser at desktop
and 360px phone width: variants switch, deep links (`#variant-B`) work,
Copy my answers produces the feedback line, nothing overflows.

**Review it (first available channel):** you're in the Claude app, so I
published it as a private artifact. Pick a layout, answer the three
questions at the bottom, press **Copy my answers**, and paste the line here.
On your computer with lavish-axi, `npx -y lavish-axi proto-weekly-scorecard.html`
also works and lets you click on any block.

## Reviewer's pasted answers

> PROTOTYPE FEEDBACK r1 · PICK: B · READ FIRST: the -7% tile · NOTES: #3 too long · #5 drop average ticket

## Reply 3 (verdict)

```
SPIKE VERDICT
QUESTION:     Which weekly scorecard layout lets an owner see what needs attention in 30 seconds?
SHAPE:        look
TIMEBOX:      1 session, 1 round → 1 session, 1 round · rounds: 1
LEDGER-CHECK: none
DESIGN:       plain owner-report style (no client brand files provided)
EVIDENCE:     "PICK: B · READ FIRST: the -7% tile · NOTES: #3 too long · #5 drop average ticket"
VERDICT:      answered
ANSWER:       Use the headline + three tiles layout (B): one-sentence headline under 20 words, three exception tiles, a short table of the rest without average ticket.
ARCHIVE:      artifact link (private) + scratch/proto-weekly-scorecard.html
CONSUMER:     jail-memory
```

Ledger line:
`2026-11-12 · weekly scorecard layout for owners · answered (B, headline + 3 tiles) · scratch/proto-weekly-scorecard.html · supersedes:none`

The answer goes into the real scorecard spec; the prototype page stays archived
and is not reused as the production template.

```yaml
JAIL-HANDOFF:
  skill: jail-prototype
  status: complete
  assumptions: [one reviewer's pick stands for the owner audience]
  unknowns: [whether other client owners read it the same way]
  outputs: [SPIKE VERDICT, review page]
  evidence: ["PICK: B · READ FIRST: the -7% tile · NOTES: #3 too long · #5 drop average ticket"]
  next: jail-memory
  approval_required: []
  tested: tested - artifact-lint pass; browser check desktop + 360px
```
