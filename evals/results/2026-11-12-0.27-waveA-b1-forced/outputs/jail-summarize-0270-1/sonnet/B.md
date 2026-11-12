**Audience row used: Board/CEO (one page, decision first, technical identifiers moved to the appendix).**

# Security funding decision for this month

**Fund all five fixes now, starting with the VPN. Four of the five look cheap and quick, and together they close the most likely ways an outsider or an ex-employee could get into the business or stall it.** Please decide by **Friday, Nov 20**. The VPN fix should not wait for that date.

**What the review found (fact, from our security review):**
- The remote-access gateway that lets staff connect to the office has a known critical flaw that hasn't been fixed.
- QuickBooks Online, which holds your financial records, has no second sign-in step.
- Nobody has tested restoring from backups in 14 months.
- Everyone in the office shares one administrator password.
- Two former employees can still sign in to company email.

**What it means for the business (our analysis, not measured losses):**
- **Remote access flaw (liability, resilience).** This is an open door that attackers actively look for. If someone gets in, the cost is downtime, possible customer-notification obligations, and lost trust.
- **QuickBooks (control, cost).** A stolen password alone would be enough to see or change your books and payments.
- **Backups (resilience).** We have a backup but no proof it works. If ransomware or a failure hits, we could find out it doesn't work when the business is already stopped.
- **Shared admin password (control).** It's impossible to know who did what, and anyone who has ever had it, including people who left, may still have full control.
- **Former employees' email (liability, control).** Anyone with those logins can read company and customer email and send mail as your business.

**What we don't know yet (honest unknowns):**
- We haven't confirmed whether this particular flaw is being actively attacked in the wild.
- We have no sign of an actual break-in, but we also haven't checked.
- We haven't confirmed whether the backups would restore.
- **No quotes exist yet.** My expectation is that QuickBooks MFA, closing the two accounts, and replacing the shared password (via a password manager) cost mostly staff time plus a small per-user subscription. The VPN patch is likely a few hours of IT work, and the restore test a modest one-time effort. These are estimates until IT quotes them.

**Your options:**

| Option | What it buys | What it leaves exposed |
|---|---|---|
| **A. Fix all five this month (recommended)** | Closes every finding. Four are low-effort, so the extra cost over B is small (estimate). | Nothing from this review. |
| B. Fix only the VPN and QuickBooks | Closes the two doors an outsider is most likely to use. | Ex-employee access, the shared password and the untested backups stay open, so an insider mistake or a failure would still hurt. |
| C. Do nothing this month | Spends nothing now. | All five stay open. If something goes wrong, the downtime, liability and trust costs are unbudgeted and could far exceed the fix costs. |

**Recommendation: Option A.** Confidence is high on the direction, since these are standard and widely recommended fixes. It is moderate on cost until quotes arrive. If quotes come back far above my estimate, fall back to B plus the two free fixes (closing the old accounts and turning on QuickBooks MFA).

**Cost of delay:** each week of delay keeps the VPN flaw exposed. That one shouldn't wait for the funding decision.

**Next actions (owners and dates are my proposals, so please adjust):**
1. **IT lead:** patch the VPN firmware and confirm it, by **Nov 17**. Also disable the two former employees' accounts the same day.
2. **IT lead:** turn on MFA for QuickBooks Online and send written quotes for the remaining items, by **Nov 17**.
3. **Owner:** approve Option A or choose B, by **Nov 20**.
4. **IT lead:** replace the shared admin password with individual accounts and run a full backup test restore, by **Dec 4**. Report the restore result in writing.
5. **IT lead:** check logs for any sign of unauthorized access, covering the VPN and the two old accounts, by **Nov 24**.

**Appendix, for IT (technical detail):**
- VPN appliance firmware has an unpatched critical CVE. The CVE ID was not in the findings and needs to be added.
- MFA is not enabled on QuickBooks Online.
- Backup restore has not been tested in 14 months.
- A single shared admin credential is used across the office.
- Two terminated-user email accounts are still active.