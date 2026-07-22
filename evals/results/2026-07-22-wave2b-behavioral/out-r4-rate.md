# JAIL-RATE — Accounting-firm client portal

> **Accounting-firm client portal (your private app) — software product — Overall: 4.3 / 10 → 6.6 / 10 projected (▲ +2.3)**

**Act on recommendation 1 this week regardless of the score.** Plaintext password storage in a portal holding accounting clients' financial documents is a live, critical exposure — and your firm sits inside the FTC Safeguards Rule's scope, which makes it a regulatory exposure too.

---

## Rubric used

Declared before scoring; weights sum to 100%. Base rubric: **software product** (jail-rate rubric library). Two weights adjusted for your context — this is a financial-data portal operated by a Safeguards-covered accounting firm for its own clients, not an app sold on the open market — so Security is raised 20% → 25% and Marketability lowered 15% → 10%; the other three keep library defaults.

| Dimension | Weight | Why this weight for this software product |
|---|:---:|---|
| Software quality | 25% | Everything else decays without it; the portal is a long-lived operational system for the firm. |
| Features | 20% | The portal's value is exactly what clients can accomplish in it versus alternatives they've seen elsewhere. |
| Usability | 20% | It is client-facing; adoption by non-technical accounting clients is the point. |
| Security | 25% | Raised from the 20% default: it stores credentials plus clients' financial documents inside an FTC Safeguards-covered business — one breach outweighs years of polish, and here it also triggers regulatory duties [3]. |
| Marketability | 10% | Lowered from the 15% default: an internal client-retention asset for one firm, not a product needing go-to-market strength. |

## Scorecard

| Dimension | Weight | Now | Projected | Evidence (label + source) |
|---|:---:|:---:|:---:|---|
| Software quality | 25% | 4.0 | 6.0 | **Fact [S]:** plaintext password storage shipped to production (owner-confirmed). **Inference:** a control this basic reaching production indicates no effective security review or engineering-safeguard gate in the delivery process. "Modern stack" and "fast" are **reported owner claims, not evidence** (unverifiable-claim tier per evidence standards). No repo, tests, CI, or incident history supplied. Confidence: Low. |
| Features | 20% | 5.5 | 6.5 | **Fact [S]:** feature set = login, document upload, invoice history, mobile-friendly (owner-supplied; owner is the primary source for a private app). **Fact [4]:** category-standard portals bundle e-signatures, secure messaging, payments, organizers/checklists, MFA, audit trails, role-based permissions, and QuickBooks/Xero integrations. **Inference:** a core-only set does the job but trails the category baseline. Confidence: Medium. |
| Usability | 20% | 6.5 | 7.0 | **Reported claims [S]:** clean UI, fast, mobile-friendly, 4.6-star client feedback — crowd-tier, single-channel, owner-reported, not independently inspectable, so discounted rather than taken at face value. **Judgment:** if the feedback is real, true usability is likely 7+; no independent review or accessibility audit exists to support that. Confidence: Low. |
| Security | 25% | **1.5** | 7.0 | **Fact [S]:** passwords stored in plaintext, confirmed by the owner. **Fact [1]:** OWASP — "Passwords should never be stored in plain text"; Argon2id is the recommended default. **Fact [2]:** NIST SP 800-63B — memorized secrets "SHALL be salted and hashed using a suitable one-way key derivation function." **Fact [3]:** tax/accounting firms are financial institutions under the FTC Safeguards Rule, which requires encrypting customer information and MFA, and mandates FTC breach notification within 30 days when ≥500 consumers' unencrypted information is acquired. **Inference:** any single database read — SQL injection, leaked backup, stolen laptop, insider — yields every client's credential in usable form, and password reuse extends the blast radius to clients' email and banking. **Critical flaw → ≤ 4.0 cap applied;** scored well below the cap because the flaw is maximal-severity for this data class and the rest of the posture (TLS config, document authorization, at-rest encryption, upload validation) is unassessed. Confidence: Medium — the negative finding itself is solidly evidenced; the unexamined remainder is not. |
| Marketability | 10% | 5.5 | 6.5 | **Reported claim [S]:** 4.6-star client sentiment is a genuine retention/differentiation signal if accurate (unverified). **Inference from [3] + [S]:** an accounting firm's product is trust; the latent breach plus Safeguards exposure is a reputational time bomb that undercuts the asset it markets. Confidence: Low. |

**Arithmetic (current):** 4.0×.25 + 5.5×.20 + 6.5×.20 + 1.5×.25 + 5.5×.10 = 1.000 + 1.100 + 1.300 + 0.375 + 0.550 = **4.325 → 4.3**
**Arithmetic (projected):** 6.0×.25 + 6.5×.20 + 7.0×.20 + 7.0×.25 + 6.5×.10 = 1.500 + 1.300 + 1.400 + 1.750 + 0.650 = **6.600 → 6.6**

## Why this score

The product surface is reportedly strong — clean, fast, mobile-friendly, with 4.6-star client feedback — but every positive is single-source and unverified, which limits how high those dimensions can score. The one owner-verified engineering fact, plaintext password storage, is a critical exploitable flaw that violates baseline OWASP and NIST standards [1][2] inside an FTC Safeguards-covered business [3]; it caps Security, drags Software quality (as evidence of a missing review process), and pulls the weighted total to 4.3. The feature set covers the core client-portal job but sits below the 2026 category baseline of e-sign, messaging, payments, and MFA [4].

## Top recommendations (ranked by impact × 1/effort)

1. **Replace plaintext storage with salted adaptive hashing now — Argon2id per OWASP (19 MiB memory, t=2, p=1), bcrypt acceptable as a transitional legacy option [1][2].** Because plaintext copies already existed at rest, lazy rehash-on-login is insufficient: force a global password reset, invalidate all active sessions, and purge plaintext remnants from backups, exports, and logs. *Dimension: Security (also Software quality). Impact: removes the critical flaw — the single largest mover in this rating. Effort: low (days: one auth module + migration script + reset flow).*
2. **Exposure audit and containment.** Review access logs, DB exports, and backup distribution for signs of prior unauthorized access; rotate application secrets. If ≥500 clients' unencrypted information was ever acquired, the FTC's 30-day notification clock applies [3] — get counsel involved on that determination. *Dimensions: Security, Marketability. Impact: high (bounds existing liability). Effort: low–medium.*
3. **Add MFA plus login rate-limiting and lockout.** MFA for anyone accessing customer information is an explicit Safeguards requirement [3] and a category-standard feature [4]. *Dimension: Security. Impact: high. Effort: low–medium.*
4. **Independent security review / penetration test of the remaining surface** — per-client document authorization (IDOR), upload validation, encryption of stored documents, TLS configuration, dependency audit — fix findings, and stand up the written information security program the Safeguards Rule requires [3]. *Dimensions: Security, Software quality. Impact: high. Effort: medium.*
5. **Add an engineering safety net: automated tests + CI with dependency and secret scanning.** This is what keeps fixes 1–4 from regressing. *Dimension: Software quality. Impact: medium. Effort: medium.*
6. **Close the top competitive feature gaps:** e-signatures, secure messaging/notifications, and online invoice payment — the three highest-leverage items from the category baseline [4]. *Dimensions: Features, Marketability. Impact: medium. Effort: medium–high.*
7. **Verify the experience claims:** a lightweight accessibility pass and a structured in-app feedback capture, turning the reported 4.6 stars into inspectable evidence. *Dimension: Usability. Impact: small–medium. Effort: low.*

## Projected rating (estimate)

Assuming the recommendations are implemented competently — not perfectly:

- **Security 1.5 → 7.0** (fixes 1–4): modern hashing, forced reset, MFA, rate limiting, a pen-tested surface, and a Safeguards-aligned program is a genuinely good posture. Not 8+ without an independent attestation and a clean track record over time.
- **Software quality 4.0 → 6.0** (fixes 4–5): review discipline, tests, and CI close the demonstrated process gap; breadth of quality remains unverified.
- **Features 5.5 → 6.5** (fix 6): e-sign, messaging, payments reach category-competitive; leaders keep depth (organizers, integrations, audit trails).
- **Usability 6.5 → 7.0** (fixes 3, 7): accessibility pass and verified feedback, with MFA friction implemented smoothly.
- **Marketability 5.5 → 6.5** (fixes 1–3, 6): the trust story becomes a sellable strength instead of a latent liability.

New total **6.6 / 10 (▲ +2.3)** — realistic, not a 10, because the projection assumes competent execution rather than perfection, independent verification and operating history would still be thin, and category leaders retain feature and maturity depth. Labeled an estimate; current and projected are never blended.

## Assumptions and unverified items

- Unverified (owner-reported only): clean UI, speed, mobile-friendliness, the 4.6-star feedback, and "modern stack."
- Unassessed entirely: TLS configuration, session management, per-client document authorization, at-rest encryption of uploaded documents, dependency health, hosting/backup practices.
- Assumed: the portal is in production with real client data (drives the urgency of recommendations 1–2).

## Sources

Subject-specific evidence: **rated from supplied materials only — external evidence on the app itself N/A (private subject).** Category and standards evidence was researched externally, per the private-subject split below.

- **[S]** Supplied materials — owner's description of the app (features, UI/speed/mobile claims, 4.6-star feedback) and the owner-confirmed finding that passwords are stored in plaintext. Primary source for a private app; self-reported claims labeled as such.
- **[1]** OWASP Password Storage Cheat Sheet — passwords must never be stored in plaintext; Argon2id recommended (min 19 MiB, t=2, p=1); bcrypt legacy-only; PBKDF2 for FIPS — [https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) — accessed 2026-07-22.
- **[2]** NIST SP 800-63B, Digital Identity Guidelines — memorized secrets "SHALL be salted and hashed using a suitable one-way key derivation function" — [https://pages.nist.gov/800-63-3/sp800-63b.html](https://pages.nist.gov/800-63-3/sp800-63b.html) — accessed 2026-07-22.
- **[3]** FTC, "Safeguards Rule: What Your Business Needs to Know" — tax preparation firms are covered financial institutions; encryption of customer information and MFA required; written information security program; FTC notification within 30 days for events involving ≥500 consumers' unencrypted information — [https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know](https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know) — accessed 2026-07-22.
- **[4]** Future Firm, "12 Great Client Portals for Accountants" — category-standard feature baseline (e-sign, secure messaging, payments, organizers, MFA, audit trails, integrations) — [https://futurefirm.co/client-portals-for-accountants/](https://futurefirm.co/client-portals-for-accountants/) — accessed 2026-07-22. Additional 2026 category roundups surfaced via search but not inspected (listed for corroboration of the category only): [SuiteFiles](https://www.suitefiles.com/accounting-firm-client-portal/), [Financial Cents](https://financial-cents.com/resources/articles/client-portals-for-accountants/).

Independent evidence that would upgrade this rating's confidence: read access to the repository and auth/storage code, a third-party penetration-test or audit report, and verifiable client-review data.

## Confidence

**Low** overall (weighted center of per-dimension confidences: Software quality Low, Features Medium, Usability Low, Security Medium, Marketability Low). The critical negative finding itself is well-evidenced — owner-confirmed and measured against Tier 1–2 standards — but nearly every positive rests on single-source owner claims. The one action that would most raise confidence: **an independent security audit with repository access** — it would move Security and Software quality evidence from supplied-materials-only to directly inspected and lift overall confidence to Medium–High.
