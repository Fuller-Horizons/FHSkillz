I built the mock-up as one HTML file with three tabs and sent it to you. The numbers are sample data, and the page says so in a banner. I haven't opened it in a browser, so I haven't checked how it renders.

**The three layouts**
- **A · Ledger table:** one row per metric, with this week, target, change vs last week, a 6-week trend line, status and owner. It's the densest option and the easiest to compare across metrics.
- **B · Tile board:** one large number per metric, with the off-track ones sorted to the top. It reads fast on a screen share but has no room for detail.
- **C · Exceptions-first brief:** a one-line headline ("3 of 8 on track…"), a strip of colored blocks, and a short note only on the metrics that are off track or on watch. The on-track metrics get one line.

Each tab is linked by `#A`, `#B` or `#C`, so you can send the team a direct link to a layout.

**What I couldn't do**
- **No spike-ledger check:** the project docs aren't reachable from this session, so I couldn't read `spike-ledger.md`. Check it for a prior scorecard decision before Thursday. If there is one, this question may already be answered.
- **Publish declined:** the hosted-page upload wasn't approved, so you have the file only. Tell me if you want me to retry the upload.

```
SPIKE VERDICT
QUESTION:     Which of three layouts makes the weekly scorecard scannable in under ten seconds?
SHAPE:        look
TIMEBOX:      one session → one session, no extension
LEDGER-CHECK: not checked (ledger unreachable from this session)
EVIDENCE:     "Open delivery risks 4 (≤ 2) ▲ 1 vs last — Off track"; "3 of 8 on track. 3 off track, 2 to watch." (sample data, not yet rendered or judged by the team)
VERDICT:      inconclusive
ARCHIVE:      /tmp/claude-0/-tmp-fhlive--9ih-b-j/a2e1a6ff-4c02-48c1-9ced-16128d378137/scratchpad/proto-weekly-scorecard.html
CONSUMER:     jail-decide
```

The verdict is `inconclusive` because the ledger check failed, and the verdict only changes once the team picks on Thursday. The EVIDENCE lines are what the page's code produces from the sample data. Neither was observed on a rendered page.

Suggested ledger line, to append once the ledger is writable:
`2026-11-12 · Which weekly scorecard layout is most scannable? · inconclusive · proto-weekly-scorecard.html (scratchpad) · supersedes:none`

Once you've picked a layout, I can build it on your real metrics. The prototype itself stays as an archive and isn't merged.