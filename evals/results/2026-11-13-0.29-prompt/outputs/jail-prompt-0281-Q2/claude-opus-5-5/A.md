I can't see our earlier rounds or the v1 draft in this session, and nothing was saved in the working folder. So this v2 is rebuilt from the three answers you gave me (owners, one page, plain English) plus the new bank rule. If v1 had anything else in it, like section names or KPIs, paste it and I'll merge it in.

**Lane: Full.** This is a monthly, client-facing report, and two of the clients are now regulated.

**Gate: GO with one condition.** The prompt alone is not a safe enough guard for regulated bank data, because a model can repeat whatever it's given. So the plan has three layers:
1. Your team removes customer names and account numbers before the data goes in.
2. The prompt refuses to name anyone and lumps small groups together, so no customer can be picked out.
3. A plain text scan of the finished report runs before it goes out.

The prompt is layer 2 only. Separately, someone needs to confirm that each bank's agreement allows their data to go into an AI tool at all. I can't check that from here.

```
<client_profile>
{{Client name, industry, whether it is a REGULATED BANK CLIENT (yes/no), what the owners care about most}}
</client_profile>

<restricted_terms>
{{Bank clients only: customer names, account numbers, and any other identifiers that must never appear. Leave empty for non-bank clients.}}
</restricted_terms>

<month_data>
{{This month's numbers and notes. For bank clients, already stripped of customer names and account numbers.}}
</month_data>

<prior_month_summary>
{{Last month's report or key numbers, if available; otherwise "none"}}
</prior_month_summary>

OBJECTIVE: Write this month's one-page report for the business owners of the client above, in plain English, so they can see in two minutes how the month went, why, and what we recommend next.

CONTEXT: The readers are owners, not analysts. They want the bottom line first and no jargon. Two of our clients are banks. For them, anything about individual customer accounts is regulated, so the report talks only about groups and totals and never about an identifiable customer.

SUCCESS TEST:
- The report is 450 words or fewer, so it fits on one page.
- No string from <restricted_terms> appears in the report (case-insensitive).
- For bank clients, the report contains no run of 6 or more digits that isn't a dollar amount, percentage, or year.
- The report has exactly these four headings: Bottom Line · What Happened · Why It Matters · What We Recommend.
- Every number in the report appears in, or is directly calculated from, <month_data> or <prior_month_summary>.

QUALITY BAR:
- The first sentence of Bottom Line tells the owner whether the month was good, mixed, or bad, and gives the reason.
- No word an owner would need to look up. A term with no plain replacement gets explained in five words or fewer.
- Bank clients: customers show up only as totals, counts, or percentages for a group. If a group has fewer than 5 customers, fold it into a bigger group so nobody can be identified from the description ("one large commercial depositor left" counts as identifying).
- If <month_data> contains a customer name or account number anyway, the report leaves it out and the problem is flagged in PREPARER NOTES. It is never repeated.
- At most 3 recommendations, each one a concrete action the owner can say yes or no to.

OUTPUT FORMAT:
REPORT
Bottom Line: <2-3 sentences>
What Happened: <3-5 short bullets, each with a number and its change from last month>
Why It Matters: <2-3 sentences tying the numbers to the owner's goals>
What We Recommend: <1-3 numbered actions>

PREPARER NOTES (internal, never sent to the client)
- Facts used: <list of numbers and where in the data each came from>
- Inferences: <any judgment calls, labeled as inference>
- Unknowns: <gaps in the data the owner may ask about>
- Restricted-data flags: <"none", or what was found in the input and left out>

RUN SETTINGS: Claude Opus 5.5 · medium effort · no tools (work only from the supplied data) · API max_tokens 4000
```

**Quick version** (for non-bank clients when you're in a hurry):
```
<month_data>{{data}}</month_data>
Write a one-page (≤450 words) plain-English report for this client's business owners. Headings: Bottom Line, What Happened, Why It Matters, What We Recommend (max 3 actions). Use only numbers from the data. Never name an individual customer or include account numbers; use totals and percentages only. After the report, add PREPARER NOTES listing any data gaps and anything sensitive you left out.
```

**Round 3 questions** (the new context earns another round; unanswered ones take the recommended option):

1. **What counts as "by name"?**
   A) Customer names, account numbers, and any other identifier such as an address or tax ID *(recommended)*
   B) Customer names only
   C) Something else, in your words
2. **Small groups of customers:**
   A) Fold any group under 5 customers into a bigger one *(recommended; a group of one identifies someone without naming them)*
   B) Small counts are fine as long as there are no names
   C) Something else, in your words
3. **Who removes customer details before the data goes in?**
   A) Your team, before pasting it in, with the prompt as a second guard *(recommended)*
   B) The banks send data that's already anonymized
   C) The prompt is the only guard (I'd advise against this for regulated data)
   D) Something else, in your words

UNTESTED: I don't have a month of client data to run it on. Test set to run before the first real send:
- **Fix inputs:** (1) a non-bank client with a normal month; (2) a bank client with clean, already-redacted data; (3) a bank client with one customer name and one account number left in by mistake. The report should leave both out and flag them in PREPARER NOTES.
- **Held out:** (4) a bank client where one segment has only 2 customers; (5) a bad month with missing data.
- Run each input 3 times and compare against a plain request ("write a monthly report").

I can also write the scan from layer 3 as a small script that checks the report against the restricted terms and the digit rule. Just say if you want it.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [earlier v1 draft not visible here, so v2 is rebuilt from your answers (owners, one page, plain English); "one page" means 450 words or fewer; "by name" covers names, account numbers and other identifiers; groups under 5 customers get folded into bigger groups; customer details are removed before input]
  unknowns: [anything else that was in v1 (sections, KPIs); which data fields each client sends; whether the bank agreements allow processing by an AI tool]
  outputs: [engineered prompt v2 + QUICK version + round-3 questions + test set]
  next: answer round 3 → v3; run the 5-input test set; build the restricted-terms scan
  approval_required: [bank compliance or contract sign-off before any bank data goes into an AI tool; human review of every bank-client report before it is sent]
  tested: untested: no client data available; 5-input test set listed above
```