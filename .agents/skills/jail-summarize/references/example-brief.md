# Worked example — owner brief (technical finding to funded decision)

Synthetic data. Company, owner, and figures are invented for illustration.

## Input

Request: "Summarize this for the owner. She is not technical and needs to decide what to fund this month."

Source finding (from a short IT review, operator wording):

- The accounting system (QuickBooks Online) has no multi-factor authentication. Five staff log in with a password only. One of them is the bookkeeper, who can approve vendor payments.
- Other findings in the review (VPN patching, untested backups, shared admin password, ex-employee mailboxes) are out of scope for this brief and are listed in the appendix as "not yet briefed".
- User-provided: average monthly vendor payments are about $85,000. Cyber insurance renews in 61 days.
- The fix is turning on a sign-in step that needs a phone code. About 2 hours of work. No new software cost.

## Output

Audience row: **Owner, client-facing. Plain language, grade 9 or below. Closest row: Operating exec, brief only.**

**Brief: Turn on a second sign-in step for the accounting system this month**

Anyone who learns one staff password can move your money, and today a single password is all that protects the accounting system. [Fact] Five people sign in to it with a password and nothing else, and one of them can approve vendor payments. [User-provided] Your payments run about $85,000 a month.

What this means for the business:

- **Cost.** A stolen password could let someone approve a fake vendor payment. Our estimate is that one bad payment could be a large share of a normal month. Money sent on a real approval may be hard to get back. [Estimate]
- **Liability.** Your cyber insurance renews in 61 days. [User-provided] Insurers may ask whether a second sign-in step is on for finance systems. We have not seen your application, so we cannot say how yours will treat it. [Unknown]
- **Control.** Right now you cannot tell a real login from a stolen one.

Your options:

1. **Turn it on now.** About 2 hours of work and no software cost. [Fact] Staff enter a phone code at sign-in. Expect a few days of small complaints.
2. **Wait until the other findings are fixed.** No cost today, but the exposure stays open for months and the renewal question stays unanswered.
3. **Do nothing.** The risk stays as it is. We do not recommend it.

We assume the five staff all have smartphones they will use for the code. [Assumption] If not, we need a small hardware key for each person, and the price changes.

**Recommendation:** choose option 1. We are fairly sure of this, because the fix is cheap and fast and the harm is large. [Judgment]

**Decision for you:** approve option 1 by Friday 20 November 2026. Each week of delay is a week in which one stolen password can move money. Delay also leaves less time to show your insurer the fix before renewal.

Next actions:

- Owner: say yes to option 1 by 20 November 2026.
- IT advisor: turn it on for all five users and test it by 25 November 2026.
- Bookkeeper: confirm phone setup with the advisor by 25 November 2026.

Pre-ship check: answer first, labels on facts, each risk has a consequence, one recommendation, owners and dates on actions, audience row named, no confidential data crossed. All pass.

## Readability check

```
python3 skills/jail-py-toolkit/scripts/readability.py --max-grade 9 brief.md
```

Brief body measured at grade 4.6. Limit is 9 for owners.

## JAIL-HANDOFF

```yaml
JAIL-HANDOFF:
  skill: jail-summarize
  status: complete
  facts:
    - Five staff sign in to the accounting system with a password only
    - One of the five can approve vendor payments
  assumptions:
    - All five staff have smartphones they will use for sign-in codes
  unknowns:
    - How the insurer will treat this control at renewal
  outputs: [owner brief, one page]
  risks:
    - A stolen password could approve a fake vendor payment
  confidence: medium
  next: jail-verify
  approval_required:
    - Owner approval to enable the second sign-in step
  checks:
    readability.py: pass
    label-lint.py: pass
```
