I can't see the earlier draft. This session has no record of it, and nothing is saved in the working folder or scratchpad. So below is **v2 rebuilt from what you've told me**: written for owners, one page, plain English, and now bank-safe. If you paste the earlier version, I'll merge in anything this one dropped.

**Gate: GO, with one change to the method.** An instruction in a prompt is not a compliance control. If customer names or account numbers reach the model, telling it "don't print them" only reduces the risk. The safe setup has three layers:
1. **Strip names and account numbers before the data goes in.** Replace them with tokens such as `[CUST-01]`, or send totals only. Then the model never sees anything regulated.
2. **The prompt below** writes only at the total level, as a second safeguard.
3. **A local check after the run.** A small script searches the report for the customer-name list, account-number patterns and any leftover tokens. The name list never goes to the AI.

This is client-facing, regulated and recurring, so it's Full lane. Opus 5.5 at medium effort fits.

```
<client_profile>
{{client name, industry, REGULATED: yes|no, owner names, goals for the year}}
</client_profile>

<period_data>
{{this month's figures, notes, project status. For REGULATED clients, customer
identities must already be replaced with tokens like [CUST-01] or rolled up to totals.}}
</period_data>

<prior_report>
{{last month's report, for comparison; optional}}
</prior_report>

OBJECTIVE: Write this month's one-page report for the client's owners in plain English:
what changed, why it matters to them, and what to do next.

CONSTRAINTS:
- If REGULATED is yes, the client is a bank, and anything about its customers' accounts
  is regulated. Never name a customer, give an account number or token, or describe a
  single customer in a way that could identify them. Report totals and trends only. If a
  group has fewer than 5 customers, write "fewer than 5" instead of a number or detail.
  If a point can't be made without identifying someone, leave it out and add the line
  "Detail held back for confidentiality; available on request."
- The readers are owners, not analysts. Use short sentences, explain any term the first
  time it appears, and use no jargon.
- Use only figures that appear in <period_data> or <prior_report>. If something the
  owner would expect is missing, put it under "Open items" rather than estimating it.

SUCCESS TEST:
- 450 words or fewer, which fits on one page
- All four headings below appear, in order
- Zero matches when checked against the customer-name list, the token pattern
  \[CUST-\d+\], and any run of 6 or more digits (this check runs locally)
- Flesch-Kincaid grade level 9 or below

QUALITY BAR:
- The first sentence of the summary says whether things got better or worse, and by how much.
- Every number can be traced to the inputs.
- Each next step has an owner and a date.
- Nothing in the report would let a reader work out which customer is being discussed.

OUTPUT FORMAT:
## The month in one line
## What changed (3-5 bullets, each: fact → why it matters to you)
## What we recommend next (2-3 actions: what, who, by when)
## Open items (missing data or anything held back; write "None" if empty)

RUN SETTINGS: Claude Opus 5.5 · medium effort · no tools · max_tokens 4000
```

**QUICK version:** "Write a one-page, plain-English report for the owners from <period_data>, under the headings above. If REGULATED is yes, use totals only: no customer names, account numbers, tokens or groups smaller than 5. Use only the figures you were given, and put any gaps under Open items."

**Questions for this round.** These are new questions prompted by the bank detail. Reply "yes" to accept the first option for all three.

1. **What does "never by name" cover?** (A) Names, account numbers, and any detail that points to one customer, including groups smaller than 5. *(recommended)* (B) Names and account numbers only. (C) Also leave the bank's own name off the report. (D) Something else, in your words.
2. **Where do names get stripped?** (A) Before the data reaches the AI: your team replaces names with tokens or sends totals only. *(recommended)* (B) Rely on the prompt plus the output check. (C) The banks send totals only. (D) Something else.
3. **One prompt or two?** (A) One prompt for all clients, with a REGULATED switch. *(recommended)* (B) A separate prompt just for the banks. (C) Something else.

**UNTESTED: no sample client data in this session.** The test set I'd use is 5 runs, 3 to fix problems and 2 held back, each run 3 times and compared with a plain request:
- a bank month with a customer name planted in the data
- a bank month with a group of 3 customers
- a non-bank month
- a month with missing figures
- a bank month with a raw account number left in by mistake (held back)

If you send sample data with fake names, I'll run the tests and write the local check script.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [earlier v1 not available, so v2 is rebuilt from your summary; "regulated" means customer account information at the 2 bank clients; groups smaller than 5 are hidden; one page = 450 words or fewer; plain English = grade 9 or below]
  unknowns: [earlier v1 text, answers to Q1-Q3, input data format, bank compliance team's exact rules]
  outputs: [engineered prompt v2 + QUICK version]
  next: answer Q1-Q3 and paste v1 → v3; send fake-name sample data → test run + local check script
  approval_required: [bank compliance team signs off on the redaction approach before live use, with no real customer data used in testing]
  tested: untested: no sample data; test set defined above
```