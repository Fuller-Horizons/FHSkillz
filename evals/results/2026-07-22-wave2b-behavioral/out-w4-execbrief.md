A note before the brief: the exec-brief standard I work to doesn't permit an "FYI — no action needed" framing unless no decision genuinely exists, and this material contains one. Someone must decide, now, whether four developer-days get spent before renewal season while breach-insurance coverage may hinge on it. Shipping this as an FYI would bury that decision. Below is the decision-forcing version, calibrated for the board (one page, technical detail in the appendix). If the fix is in fact already approved and scheduled, tell me and I'll reissue it as a declared FYI — "no decision required because remediation completes on [date]" — which is the only legitimate FYI form.

---

**BOARD BRIEF — Customer portal session security: approve immediate fix**
*Audience: Board (one-page format). Decision required at this meeting.*

**The finding and the ask.** Our penetration test found that customer portal sessions do not actually end at logout, and on one legacy web address those session credentials travel unencrypted. Together, these very likely fall short of the "reasonable session controls" our cyber policy requires for full breach coverage — our reading; broker confirmation pending. The fix is small: about four developer-days (engineering's estimate). We recommend the board endorse immediate remediation so the gap is closed and re-verified before renewal season opens in six weeks.

**Material facts.**
- Logging out does not invalidate a customer's session token — a stolen token keeps working after the customer believes they've left. (fact — pen-test finding)
- One legacy subdomain accepts these tokens over unencrypted connections, where they can be intercepted. (fact — pen-test finding)
- Fix effort: roughly four developer-days. (estimate — engineering)
- Renewal season starts in six weeks. (calendar)
- The cyber policy conditions full breach coverage on "reasonable session controls." (policy text)

**Assumptions and unknowns.** We assume the four-day estimate is roughly right; it has not been re-scoped. Unknown: whether this gap has ever been exploited — the pen-test proves exposure, not an incident, and log review has not yet been done. Unknown: whether the insurer would actually treat these findings as failing "reasonable session controls" — that is our interpretation of the policy, not a confirmed position.

**What it costs us while it stays open.** Liability: a breach through this path risks reduced or denied insurance recovery — costs we currently assume are insured would land on us. Revenue and timing: renewal conversations begin in six weeks, and an open, known security finding — or worse, an incident — lands in the middle of them. Control and trust: until fixed, logout does not do what customers believe it does.

**Options, priced.**
1. Fix now: about four developer-days; closed and re-tested well before renewals. Recommended.
2. Defer a quarter: saves those four developer-days of roadmap time; extends potentially under-insured breach exposure through the renewal window. Not recommended.

**Recommendation.** Option 1, with high confidence: the cost is four developer-days; the exposure is measured in insurance recovery and renewal-season trust. Decide at this meeting — each week of delay is another week a breach may be only partially covered, and pushes remediation closer to the renewal window.

**Next actions.**
- Engineering lead: schedule the fix immediately; target completion and re-test within two weeks (proposed), a month clear of renewals. Confirm this week whether unencrypted access to the legacy subdomain can be blocked as an interim stopgap.
- CFO / counsel: confirm with the broker how an open — then remediated — finding affects coverage now and at policy renewal; document remediation for the file.
- Security lead: re-run the pen-test checks after the fix and record closure for renewal-season customer security questionnaires.

**Appendix (operator detail).** Session tokens are not revoked server-side at logout; tokens are accepted over plain HTTP on one legacy subdomain. Remediation: server-side session invalidation on logout; enforce HTTPS (redirect plus HSTS) and reject tokens over cleartext on the legacy host; re-test both findings to confirm closure.
