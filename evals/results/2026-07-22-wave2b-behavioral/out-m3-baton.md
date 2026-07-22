Got it — writing the baton now while state is still sharp. Two things I did deliberately, per baton rules:

1. **The Stripe key is not in this baton.** Secrets never ride in a baton — it's a file that travels further than the session. The key stays in the secret store / env where it's configured, and because its value was pasted into today's chat in plaintext, the baton flags it for rotation.
2. This is the **one-page version**, sized for a frontier-context recipient (tomorrow's session), weighted toward your stated next purpose — finish the remaining 40%, then reconcile. Everything else travels as pointers.

Save it as **`2026-07-22-client-records-migration.baton.md`** in the project folder, next to `migration-log.md`, so tomorrow's session finds it without hunting. It supersedes nothing (first baton for this work) and is superseded by whatever tomorrow writes.

---

# BATON — Client Records Migration
**Date:** 2026-07-22 · **From:** today's session (ended mid-work, out of time) · **To:** tomorrow's session
**Version:** one-page / frontier-context — references carry the detail
**File:** `2026-07-22-client-records-migration.baton.md`

## 1 · Objective + contract state
- **Objective:** migrate all client records from the legacy system to the new system, prove integrity via the reconciliation script, then notify affected clients.
- **Contract:** verbal / in-chat only — no written task-contract artifact exists yet. [Gap: tomorrow's session may want to pin one before the final batch.]
- **"Done" tests as:** (a) 100% of client records migrated, evidenced in `migration-log.md`; (b) reconciliation script runs clean over the full set; (c) affected clients emailed — **only after** the human approval in §8.

## 2 · State of play (ledger shape: node · scope · status · proving artifact)
| node | scope | status | proving artifact |
|---|---|---|---|
| migrate-batch-1 | first 60% of client records | done | `migration-log.md` (verified this session) |
| migrate-batch-2 | remaining 40% | not started | — |
| reconciliation | run reconciliation script over full set | not started — blocked on migrate-batch-2 | — |
| notify-clients | email affected clients | blocked — awaiting human approval (§8) | — |

**In-flight:** nothing reported mid-step; the session ended at the 60% checkpoint. Before resuming, tail `migration-log.md` to confirm the last batch closed clean and to read the resume offset — the log is the proof of "done," not this baton.

## 3 · Decisions so far, with why
- **Keep the legacy client IDs** — two downstream integrations parse the legacy ID format; minting new IDs would break both. *Superseded path:* generating new IDs — rejected for exactly that reason. Do not relitigate without first re-checking both integrations.
- **Sequence: finish the full migration, then reconcile** — reconciliation is only meaningful over the complete set, so it runs once, after the final 40% (set as the plan this session).

## 4 · References (pointed at, never pasted)
- `migration-log.md` — batch-by-batch evidence for the 60% done; source of the resume offset. Do not copy its contents anywhere.
- Reconciliation script — exists per this session's plan; exact path not restated in-chat. [Confirm path in the project repo/docs before step 3.]
- Stripe restricted live-mode key — lives in the environment's secret store / env config used this session, **not here** (see §5).
- Affected-client list / email draft — not sighted this session. [Confirm whether a draft exists before writing one.]

## 5 · Live constraints & gotchas
- **Legacy ID format is load-bearing.** Two integrations parse it. Migrate IDs byte-for-byte in the remaining 40% — no normalization, no reformatting.
- **Credential handling.** The migration authenticates to Stripe with a **restricted live-mode key**. Its value is **redacted from this baton by rule** — retrieve it from the secret store / env where it is configured. Additionally: the key's value was pasted in plaintext into today's chat, so treat it as exposed — **recommend rotating it in the Stripe dashboard** and storing the replacement only in the secret store (rotation needs a human go-ahead; see §8).
- **Ordering dependency.** Reconciliation runs only after 100% of records are migrated — never over a partial set.
- **No client-facing sends of any kind** until the §8 approval is explicitly granted.

## 6 · Next actions (sharpest first)
1. Open `migration-log.md`: verify the 60% checkpoint closed clean (no partial batch) and read the resume offset.
2. Migrate the remaining 40% with identical settings — legacy IDs preserved verbatim — appending evidence to `migration-log.md` as you go.
3. Run the reconciliation script over the full set; save its output as an artifact alongside the log.

**Known decision points ahead:** (a) if reconciliation reports mismatches → fix and re-run before any client notification; (b) client email is gated on §8 approval; (c) timing of the Stripe key rotation (before or after the final batch) — human's call, since other consumers of the key may exist.

## 7 · Suggested skills
- **jail-baton** — re-invoke at end of tomorrow's session if anything remains; that baton supersedes this one (clean up this file then).
- **jail-quarantine** — invoke before touching the Stripe key or the affected-client list/emails (credentials and client PII are protected classes). Fallback if unavailable: secrets stay in the secret store, PII stays out of transcripts and artifacts.
- **jail-memory** — one durable lesson routed there rather than stored here: *live keys pasted into chat are exposed keys — pull from the secret store, and rotate on exposure.* Fallback: note it in project docs.
- **jail-orchestrate** — optional: the §2 table is already in ledger shape and can seed an orchestrate resume directly if tomorrow's session parallelizes the work.

## 8 · Approval state (travels explicitly — nothing laundered into a yes)
- **PENDING — NOT granted:** human approval to email the affected clients. This baton confers no authority to send; tomorrow's session must obtain an explicit yes from the human before drafting-and-sending anything client-facing. Status at session end: awaiting the human's decision.
- **Newly surfaced, needs human sign-off:** rotating the exposed Stripe restricted key (§5) — recommended, but rotation can break other consumers of the key, so it is a human decision, not an assumed action.

---

Tomorrow's session starts at §6, step 1. If you want the 30-line small-context version as well, say so and I'll cut one from this.
