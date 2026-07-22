# APPROVAL GATE — run of 2026-07-22

**Standing profile 2026-07-10 applied — say "retier" to revise.**
Freshness check (jail-memory rule): nothing in today's instructions contradicts the profile, so it is applied as-is: outbound client emails = BATCHABLE after sample review · CRM writes = AUTO · spending = PER-ACTION.

**DIFF against the profile:** "auto-text clients via a new SMS gateway" is a **new action type this run**. The profile does not cover it, and the email tier does not stretch to SMS — a new channel is a new action type. It defaults to PER-ACTION until you tier it, and parts of it sit stricter than that (below).

---

## Step 1 — Action inventory (re-derived, not just your four bullets)

| # | Action | Touches the world how |
|---|--------|----------------------|
| 1 | Draft 30 renewal emails | Workspace-local drafting |
| 2 | Send 30 renewal emails | External communication, one-way |
| 3 | Update 200 CRM records | Durable writes to CRM |
| 4 | Purchase $340 mailing-list add-on | Spend, new vendor relationship |
| 5 | Email any recipients acquired via the add-on | External communication — **not part of today's batch** |
| 6 | Create account + API credentials on the new SMS gateway | Credential scope change, new external vendor |
| 7 | Load clients' cell numbers into the SMS gateway | Egress of protected data (PII) to an external provider |
| 8 | Auto-send SMS to clients | External communication on a new channel; consent basis unknown |

## Step 2 — Tier map

| # | Action | Tier | Source |
|---|--------|------|--------|
| 1 | Draft the 30 emails | **AUTO** | Reversible, workspace-local |
| 2 | Send the 30 emails | **BATCHABLE** (after sample review) | Profile 2026-07-10 |
| 3 | 200 CRM record updates | **AUTO** | Profile 2026-07-10 |
| 4 | $340 add-on purchase | **PER-ACTION** | Profile 2026-07-10 (spending) |
| 5 | Emailing add-on-sourced recipients | **PER-ACTION** (new request when it arises) | Batch is closed at approval; additions are new requests |
| 6 | SMS gateway account + credentials | **PER-ACTION** | DIFF default — new action type, plus credential scope change |
| 7 | Client cell numbers → SMS gateway | **NEVER** (this run) | jail-quarantine: protected data (Personal/PII class) to an external provider without explicit human authorization is NEVER-tier until a human reclassifies it |
| 8 | Auto-texting clients | **NEVER** (this run) | Consent basis unknown → possible TCPA violation; two tiers arguably apply, stricter wins |

Tiering notes, honestly applied (no tier inflation):

- **CRM (AUTO):** the profile covers CRM writes, 200 updates is squarely that type, so they proceed without prompting and are logged in the ledger. One guard: if any update values originate from newly purchased or imported data, that data passes the jail-quarantine adoption gate *before* it enters the CRM — AUTO covers the write, not adoption of untrusted inputs.
- **Email batch (BATCHABLE):** the batch is **closed at approval time at the 30 named recipients**. Names from the $340 mailing-list add-on are not in it; emailing them later is a new approval request (batch-smuggling guard).
- **SMS (NEVER this run):** not approvable mid-run. Unblocking is a human policy decision made outside the run: (a) you authorize the specific gateway as a destination for client phone numbers (vendor/compliance review — data processing terms, 10DLC registration), and (b) you confirm clients' SMS opt-in consent records exist. After both, say "retier" and we tier the action type properly (and can add it to the profile).

---

## Step 3 — Approval requests

Pending your response. **No response = not approved. Proceed-by-timeout is forbidden.**

```
APPROVAL REQUEST 1 — renewal email batch (BATCHABLE)
Action: Send 30 renewal emails from your account to the 30 clients on today's
        renewal list, exactly as drafted; the first draft comes to you as the
        sample for review, then one approval covers the closed batch of 30.
        No recipients added after approval.
Why: Today's renewal outreach objective.
Blast radius: 30 client inboxes and relationships; sender/domain reputation
        if the copy or list is wrong.
Reversibility: One-way — a sent email cannot be unsent.
Safer alternative: Per-email approval for all 30 (cost: 30 prompts), or send
        5, pause for spot-check, then release the rest (cost: minutes).
```

```
APPROVAL REQUEST 2 — mailing-list add-on purchase (PER-ACTION)
Action: Purchase the $340 mailing-list add-on from the vendor, charged to the
        company payment method, one time (recurrence unverified).
Why: Expand the outreach list beyond current contacts.
Blast radius: $340 of company funds; a new data-vendor relationship; any
        contacts it delivers arrive as quarantined data, not ready-to-email.
Reversibility: Treated as one-way until the vendor's refund terms are
        confirmed; two-way only if a refund window exists.
Safer alternative: Confirm refund terms and whether the charge recurs before
        buying, or defer until today's 30-email batch shows results
        (cost: a day or two of delay).
```

```
APPROVAL REQUEST 3 — SMS gateway groundwork (PER-ACTION, optional)
Action: Create an account and API credentials on the proposed SMS gateway —
        configuration only, zero client data loaded, no messages sent.
Why: Groundwork so the SMS channel is ready if you authorize it.
Blast radius: A new external credential surface and vendor account; any
        signup fee (would come back as its own spending approval).
Reversibility: Two-way — revoke the keys and close the account; no client
        data is involved at this step.
Safer alternative: Finish the vendor compliance review (consent handling,
        10DLC, data processing terms) before any account exists
        (cost: short delay, nothing to unwind if the vendor fails review).
```

**BLOCKED — NOT APPROVABLE IN THIS RUN (NEVER tier):** loading clients' cell numbers into the new SMS gateway, and auto-texting clients. I will not do either today regardless of other approvals. Unblock path (outside the run): authorize the gateway as a destination for client PII after vendor review, and confirm SMS opt-in consent; then say "retier".

---

## Step 4 — Audit trail (authorization ledger)

| Time (UTC) | Item | Tier | Assigned by | Approval status | Approver |
|---|---|---|---|---|---|
| 2026-07-22T10:39Z | Draft 30 emails | AUTO | gate (this run) | n/a — auto | — |
| 2026-07-22T10:39Z | Send 30 emails | BATCHABLE | profile 2026-07-10 | PENDING (sample + batch) | Jonathan |
| 2026-07-22T10:39Z | 200 CRM updates | AUTO | profile 2026-07-10 | n/a — auto, logged | — |
| 2026-07-22T10:39Z | $340 purchase | PER-ACTION | profile 2026-07-10 | PENDING | Jonathan |
| 2026-07-22T10:39Z | Email add-on recipients | PER-ACTION | gate — batch closure rule | Not requested yet | Jonathan |
| 2026-07-22T10:39Z | SMS account + credentials | PER-ACTION | gate — DIFF default | PENDING (optional) | Jonathan |
| 2026-07-22T10:39Z | Client numbers → gateway | NEVER | jail-quarantine rule B3 | Blocked — policy decision outside run | Jonathan |
| 2026-07-22T10:39Z | Auto-text clients | NEVER | gate — consent unknown, stricter wins | Blocked — policy decision outside run | Jonathan |

Every approval or denial you give gets appended here with its timestamp. A disputed action later is settled by this ledger, not by memory.

**Starting now (AUTO lane):** drafting the 30 renewal emails and running the 200 CRM updates. Everything else waits for you.

**Profile upkeep:** once you tier the SMS action type, I'll offer to write it into the standing profile — that write is itself PER-ACTION (it's durable), so it will come to you as its own request.

---

```yaml
JAIL-HANDOFF:
  skill: jail-approval-gate
  status: complete
  facts:
    - "User-provided fact: today's plan = 30 renewal emails, 200 CRM updates, $340 add-on purchase, new SMS-via-gateway channel (user message, 2026-07-22)"
    - "Verified fact: standing APPROVAL PROFILE dated 2026-07-10 — emails BATCHABLE after sample review; CRM writes AUTO; spending PER-ACTION"
    - "Verified fact: client cell numbers fall in the Personal/PII protected class (jail-quarantine table)"
  assumptions:
    - "The 30-recipient renewal list is final at batch approval — any addition reopens as a new request"
    - "$340 is a one-time charge — vendor terms showing recurrence would trigger a fresh spending request"
  unknowns:
    - "Clients' SMS opt-in consent records (TCPA basis)"
    - "SMS gateway vendor identity and compliance posture (10DLC, data processing terms)"
    - "Whether the mailing-list add-on yields new email recipients (all outside today's closed batch)"
    - "Refund/recurrence terms on the $340 add-on"
  outputs:
    - "Tier map for the run (8 inventoried actions)"
    - "3 approval request blocks (1 BATCHABLE, 2 PER-ACTION)"
    - "NEVER notice for the SMS lane with its unblock path"
    - "Authorization ledger, 2026-07-22"
  evidence:
    - "APPROVAL PROFILE (project memory ADR) · supports tiers for emails/CRM/spend · dated 2026-07-10 · loaded 2026-07-22"
    - "jail-quarantine SKILL.md rule B3 · supports NEVER tier on PII egress to unauthorized provider · accessed 2026-07-22"
  risks:
    - "Batch smuggling: add-on-sourced contacts must not ride the 30-email approval"
    - "SMS lane if forced: PII egress to an unvetted vendor plus possible TCPA exposure on unconsented texts"
  confidence: high
  next: "Human review — approve/deny Requests 1-3; make the SMS policy decision outside the run; say 'retier' to tier SMS and update the profile"
  approval_required:
    - "BATCHABLE: send 30 renewal emails after sample review (batch closed at the 30 listed recipients)"
    - "PER-ACTION: purchase the $340 mailing-list add-on"
    - "PER-ACTION (optional): create SMS gateway account + API credentials, zero client data"
    - "PER-ACTION (later, if it arises): email recipients sourced from the add-on — new batch, new request"
    - "PER-ACTION (after SMS is tiered): durable write adding the SMS tier to the standing profile"
    - "POLICY DECISION outside this run (NEVER-tier reclassification, not an in-run approval): authorize the gateway as a destination for client phone numbers and confirm SMS consent basis"
```
