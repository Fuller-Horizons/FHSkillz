# Security Fixes: What to Fund This Month

*Audience: owner, non-technical (one-page brief).*

**Fund all five fixes this month, starting with the remote-access device. Three of the five should cost little more than staff time.**

## What we found
Each item below comes from our security review (User-provided). The "what it means" lines are our Judgment of the business impact.

1. **The remote-access device has a known, serious flaw that has not been fixed.** The device lets staff connect to the office from home (the VPN, CVE unpatched). Attackers actively look for devices like this. It is the front door to your network.
2. **QuickBooks Online asks for only a password.** It has no second check, such as a code sent to a phone (MFA). A stolen password would give someone your financial records.
3. **Nobody has tested the backups in 14 months.** They may work, but we don't know. A backup that fails on the day you need it is no backup.
4. **Everyone shares one administrator password.** We can't tell who did what, and one leak opens everything.
5. **Two former employees still have working email accounts.** Anyone who knows their passwords could read company mail or pose as your business.

## What we don't know (Unknown)
- Whether anyone has already used any of these gaps. The review found weaknesses, not break-ins.
- The dollar cost of each fix. We have no quotes yet.
- Whether the shared password is also used on customer-facing systems.

## Why it matters
Each gap could mean lost money, lost data, or a legal duty to notify customers. We can't put a dollar figure on that loss because we lack your data. The risk is real, and it grows the longer these stay open (Judgment).

## Your options
| Option | What you get | Cost |
|---|---|---|
| **A. Fix all five (recommended)** | Closes every gap found | Unknown until quoted. Items 2, 4 and 5 are mostly staff time; items 1 and 3 may need outside help (Judgment). |
| **B. Fix only items 1 and 3** | Covers the biggest break-in risk and the recovery risk | Lower, but leaves the money system, the shared password and the old accounts open |
| **C. Do nothing** | No spend now | Every gap stays open. A single incident could cost far more than the fixes (Judgment). |

## Recommendation
**Choose Option A.** Confidence: high that these fixes are worth doing, because they are standard basics (Judgment). Confidence is lower on cost until we get quotes.

Do them in this order:
1. Patch the remote-access device.
2. Turn on the second check for QuickBooks.
3. Close the two old email accounts.
4. Give each person their own admin login.
5. Run a real test restore of the backups.

## Decision needed
**Approve funding for Option A by November 30, 2026.** Each week of delay leaves the first gap open to attackers who are already scanning for it (Judgment).

## Next actions
| Who | What | When |
|---|---|---|
| Owner | Approve the funding decision | By Nov 30 |
| Our team | Get quotes for items 1 and 3 and send them to the owner | Within 3 business days of your go-ahead |
| Our team | Patch the remote-access device | Within 5 business days of approval |
| Our team | Turn on QuickBooks second check; close the two old accounts | Within 5 business days of approval |
| Our team | Set up individual admin logins; run the backup test | Within 15 business days of approval |

*These timelines are our Estimate. They start the day you approve, and we'll confirm them once quotes are in.*

**Technical appendix (for our team):** VPN firmware with an unpatched critical CVE (ID to be confirmed); QuickBooks Online without MFA; no backup test-restore in 14 months; one shared admin credential; two stale former-employee mailboxes.

*Readability check: done by hand (short sentences, acronyms explained). I did not run the script.*