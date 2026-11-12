# Call Recap: Dana (owner), Rob (ops mgr), Jon (consultant)
**Call:** Wed 11 Nov 2026 · **Lane:** DEBRIEF (no pre-call CPR existed, so there is no Results audit)

I didn't build a DOCX because the docx skill isn't available here. This is the same content as Markdown.

## 1. Decisions made

| # | Decision | By | Source |
|---|---|---|---|
| D1 | Effective Monday (16 Nov), the office coordinator does all scheduling and estimators only quote. The goal is same-day quoting, down from 4 days. | Dana | L5–6, L7 |
| D2 | Lease the truck at $1,150/mo rather than buy for $58,000 cash. Cash is tight until the March invoices clear. | Dana ("Final answer") | L11–13 |

## 2. Actions with an owner and a date

| Action | Owner | Deadline | Source |
|---|---|---|---|
| Tell the estimators about the scheduling change | Dana | Fri 13 Nov (Friday huddle), before the Monday start | L8–9 |
| Call the dealer for the lease paperwork | Rob | Wed 18 Nov ("by Wednesday") | L14 |
| Send a one-page comparison of the two crew-software vendors | Jon | "Next Friday." This is probably 20 Nov, but it could be read as 13 Nov, so confirm. | L26 |
| Send this recap | Jon | Today, 12 Nov | L36 |

## 3. Unowned: needs assignment
Each of these was discussed, but no one took it and no date was set.

- **Website form routing.** Leads go to a dead inbox and have since summer, so you are likely losing leads now. Dana said "somebody should" and "we'll see who has time" (L17–20). Jon flagged that it shouldn't be left hanging, and it was left hanging.
- **Train the coordinator on the estimating sheet.** Rob wants it and Dana agreed (L31–32). Nobody was named to do the training, and there is no date. Because D1 starts Monday, this is time-sensitive.
- **Holiday schedule for the crews.** Dana said "sure, normal stuff" (L28–29). Nobody owns it and there is no date.

## 4. Not decided
- **Crew software vendor.** Dana said "I think we landed on the second one, but let's see what the price looks like first" (L23). That is conditional, so I did not record it as a decision. Rob also has no quote from that vendor yet (L24), and the follow-up was left at "we'll circle back" with no date. The next step is Jon's comparison.

## 5. Gaps and flags
- **Unrecorded recap.** At L33–35 Jon started a recap and Dana and Rob confirmed it, but the recap itself isn't in the transcript. I can't treat those confirmations as covering the unowned items above.
- **Lease terms.** The length, down payment and dealer were never discussed.
- **Unnamed.** The office coordinator and the two software vendors aren't named in the transcript.

## 6. Suggested text for the client recap
> **Decided**
> 1. From Monday 16 Nov, the office coordinator handles all scheduling and estimators only quote, with a same-day quoting goal.
> 2. We're leasing the truck at $1,150/month.
>
> **Actions**
> - Dana: tell the estimators at Friday's huddle (13 Nov)
> - Rob: call the dealer for the lease paperwork by Wed 18 Nov
> - Jon: send the one-page software vendor comparison by Fri [20 Nov]
>
> **Needs an owner and a date (please reply with names)**
> - Fix the website form routing (leads are going to a dead inbox)
> - Train the coordinator on the estimating sheet before Monday
> - Crew holiday schedule
>
> **Still open:** the crew software vendor, pending a price quote.

Before you send it, confirm that "next Friday" means 20 Nov.

## Routing
- Decisions D1 and D2 can be stored through jail-memory as decision records.
- The form-routing gap and the training gap point to a process problem, so they can go to jail-plan.
- I haven't written anything to the project or to memory. Tell me if you want D1 and D2 saved.

```
JAIL-HANDOFF
lane: cpr/DEBRIEF · cpr_exists: false · results_audit: n/a
decisions: D1 (scheduling→coordinator, eff. 2026-11-16), D2 (lease truck, $1,150/mo)
actions_owned: Dana→huddle 11-13 · Rob→dealer 11-18 · Jon→vendor comparison "next Fri" (confirm date) · Jon→recap 11-12
unowned: form routing · coordinator training · holiday schedule
not_decided: crew software vendor (conditional on quote)
gate: PASS (every action has owner+deadline or is listed unowned)
```