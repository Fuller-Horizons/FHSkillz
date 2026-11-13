I've written a 15-question questionnaire for Maria, saved as `/tmp/claude-0/-tmp-fhlive-2es84q2n/7ae42f93-09e8-4ae6-aff1-e0cec42cdbcc/scratchpad/bakery-listing-questionnaire.md`. It's a draft until you send it, and I haven't sent anything.

My first attempt to save it in your working folder was declined, so it's in the scratchpad. I haven't made a .docx copy either. Say the word and I'll convert it, or build a Docs artifact, which is a better fit for a client to fill in.

**Assumptions to correct if wrong**
- Maria answers on her own time and replies in about a week. I left `[date]` and `[your name]` as blanks.
- She is the owner and decides the price.

**What's in it, most important first**
- **Quick checks (3):** 14 employees, two locations and the $2.1M price, each phrased as "is this right?"
- **The numbers (5):** sales for the last 12 months and the 12 before that. Then profit before taxes and her own pay, her pay on its own, and the sales split between the two locations.
- **Price basis (1):** how she arrived at $2.1M.
- **Rent and debts (2):** years left on each lease, and loans or equipment leases to pay off at sale.
- **Running the bakery (1):** who runs it day to day, her or a manager.
- **Records (1):** whether she can share three years of tax returns and profit-and-loss statements. The question asks her to blank out SSN and EIN numbers.
- **Her plans (2):** why she's selling and when she wants it done.
- **Anything else:** one open question at the end. It's extra, so the numbered questions stay at 15.

**Check before sending**
- Every number you need to decide is covered: price support (profit, sales trend, pay), risk (leases, debt, who runs it) and her motive.
- The count is 15, so no second pass is needed.
- No question is compound.
- It asks for no passwords, account numbers or health details.

If you want the "why this matters" lines trimmed, or a short optional second pass added, tell me.

```
JAIL-HANDOFF:
  skill: jail-questionnaire
  status: partial   # waiting on Maria
  assumptions: [recipient is Maria, owner with the numbers; async reply in ~1 week; 14 employees / 2 locations / $2.1M taken from the user as known]
  unknowns: [deadline date, user's name for the From line, delivery format (.docx vs Docs artifact)]
  outputs: [questionnaire (Markdown draft), coverage map (above)]
  next: jail-decide
  approval_required: [sending to Maria]
  tested: n/a
```