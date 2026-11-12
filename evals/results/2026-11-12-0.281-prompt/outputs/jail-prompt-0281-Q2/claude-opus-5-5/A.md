I don't have the earlier conversation. This session has no record of the v1 prompt or the two rounds of answers, and the Project tools needed to check the prompt library aren't available here. So I rebuilt the prompt from what you just restated (audience: owners, one page, plain English) and added the banking rule. If you paste the old version, I'll merge this rule into it instead.

**Before the prompt: a prompt alone shouldn't be what protects regulated data.** Telling the model not to name bank customers is a soft rule. It will hold most of the time, but not every time. And if customer names are in the data you feed it, they've already been sent to the AI vendor, whatever the report says. The safer setup has three steps, and the prompt is only the middle one:

1. **Remove the names before the model sees anything.** Replace customer names and account numbers with labels like "Customer A" in the export or spreadsheet. A find-and-replace or a short script does this reliably. If the data never contains names, the model can't leak them.
2. **The prompt below** acts as a second layer. It also catches indirect identification, such as "our only marina client in Montauk."
3. **A check on the finished report** searches it for every restricted name and for anything that looks like an account number. Any hit blocks sending. I can write this script if you want it.

Separately, someone at Signal Results Group should confirm that bank customer data is allowed to go to an AI tool at all under each bank's agreement and its data-protection obligations. I've listed that as a sign-off below.

---

### Monthly Client Report prompt (v2, full)

```
<client_profile>
{{client name, industry, owner's name, and REGULATED_BANK: yes/no}}
</client_profile>

<restricted_terms>
{{Bank clients only: every customer name, business name, and account identifier
that appears in the source data, one per line. Leave empty for non-bank clients.}}
</restricted_terms>

<monthly_data>
{{This month's numbers, notes, and project updates for this client.
For bank clients, use the de-identified export (Customer A, Customer B...) whenever possible.}}
</monthly_data>

<last_month_report>
{{Optional: last month's report, for continuity and month-over-month comparison}}
</last_month_report>

OBJECTIVE: Write this month's one-page report for the business owner in
<client_profile>. Say in plain English what happened, why it matters to their
business, and the one or two things they should do next.

CONTEXT: The readers are owners, not analysts. They read this in a few minutes
and judge whether our work is paying off. Some clients are banks. Information
about a bank's customer accounts is regulated, so no individual customer may be
identifiable in the report, whether by name, number, or description.

RULES FOR REGULATED_BANK: yes (these apply on top of everything else):
- Never name a customer, business customer, or account holder. Never include an
  account number, even partially (no "ending in 4417").
- Describe customers only in groups ("14 commercial accounts", "deposits from
  small-business customers rose 6%"). A small group can point to one customer,
  so any group of fewer than 5 is folded into a larger one or left out.
- Leave out details that could single out a customer even without a name
  (a unique industry/town pairing, an exact large balance, a specific dated event).
- If a key point can't be made without identifying a customer, write
  "[detail withheld: customer-specific; see reviewer notes]" and explain it in
  REVIEWER NOTES so the consultant can handle it directly.
- These rules cover the bank's customers only. The bank itself and its own staff
  may be named as usual.

QUALITY BAR (each line is pass/fail):
- An owner with no finance background understands every sentence: no jargon,
  and any unavoidable term is explained in a few words.
- Every number in the report appears in <monthly_data> or is calculated from it.
  Nothing is estimated or made up. If data is missing, say so.
- The report leads with what changed and why it matters, not a list of activities.
- Next steps are concrete: who does what, and by when.
- Bank clients: the report contains no item from <restricted_terms>, no account
  numbers, and no group smaller than 5.

SUCCESS TEST (machine-checkable):
- The REPORT section is 450 words or fewer (fits one page).
- It has exactly these headings: Headline / What Happened / What It Means for You /
  Next Steps.
- Bank clients: zero case-insensitive matches for any line in <restricted_terms>,
  and zero runs of 4 or more consecutive digits that aren't years or dollar amounts.

OUTPUT FORMAT:
=== REPORT (client-facing) ===
**Headline:** one sentence with the month's main takeaway.
**What Happened:** 3-5 short bullets, each with a number from the data.
**What It Means for You:** 2-3 sentences in plain English.
**Next Steps:** 1-3 bullets in the form "[Who] will [do what] by [date]."

=== REVIEWER NOTES (internal only; do not send) ===
- Facts used: each claim in the report and where it came from in <monthly_data>
- Inferences: interpretations that go beyond the data
- Unknowns: data that was missing or unclear
- Withheld: anything removed under the bank rules, and why
- Compliance self-check: "No restricted terms or account numbers present: yes/no"

Before returning, re-read the REPORT section against <restricted_terms> and the
bank rules, and fix anything that fails.

RUN SETTINGS: Claude Sonnet 5.5 · medium effort · no tools or web access ·
API max_tokens 3000
```

### QUICK version (for when you're pasting by hand)

```
<client>{{name, owner, bank yes/no}}</client>
<restricted_terms>{{bank customers' names and account IDs, or "none"}}</restricted_terms>
<data>{{this month's data}}</data>

Write a one-page (450 words or fewer), plain-English monthly report for this
client's owner with these headings: Headline / What Happened / What It Means for
You / Next Steps. Use only numbers from <data>. If the client is a bank, never
name or number any of its customers or accounts, describe customers only in
groups of 5 or more, and leave out details that could identify one. After the
report, add an internal "Reviewer notes" section listing sources, inferences,
unknowns, and anything withheld.
```

---

**3 questions. The prompt above already uses these defaults, so change them only if they're wrong:**
1. **What counts as "customer accounts"?** *Default: names, account numbers, and any detail that identifies an individual customer.* Should it also cover aggregate balances the bank treats as confidential?
2. **One report per client, or one combined report?** *Default: one report per client.* If one report goes to several clients, the bank rule would need to cover every section.
3. **Minimum group size of 5.** *Default: 5.* The banks' compliance teams may require a different threshold.

**UNTESTED: no sample monthly data in this session.** Test set to use once you share it:
- To refine the prompt: (1) a bank client whose data includes customer names; (2) a bank client where one customer drove the month's results, to check the withheld-detail placeholder; (3) a non-bank client, to make sure the bank rules don't spill over.
- Held back for a final check: (4) a bank client with a small group, e.g. 3 accounts in one segment; (5) a bank client whose customer name is also a common word or place name.
- Each test runs 3 times. Pass means every QUALITY BAR line and the SUCCESS TEST pass on all 3 runs, and the result is compared against the plain request "write a one-page monthly report for this client."

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [one report per client; reader = owner; one page = 450 words or fewer; bank rule = no names, account numbers, or identifying details; minimum group size 5; prior v1 not available, rebuilt from restated answers]
  unknowns: [earlier v1 prompt text; exact definition of "customer accounts" for each bank; whether each bank's agreement allows customer data to be sent to an AI tool]
  outputs: [engineered prompt v2 + QUICK version]
  next: share sample data to run the 5-input test, or paste the old v1 to merge; optionally build the de-identification and post-check script
  approval_required: [compliance sign-off on sending bank customer data to an AI tool at all; a human review of every bank report before it's sent]
  tested: untested - no sample data in session; 5-input test set defined above
```