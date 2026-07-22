# Enhancement metrics contract — locked (pre-wave-1)

*2026-07-19 · Decided across 4+1 question rounds. This is the measurement constitution for all enhancement work; the JAIL Constitution governs behavior, this governs improvement.*

## Surfaces & audience
Priority surfaces: **OpenCode CLI · claude.ai web · chatgpt.com** (+ Claude Code/desktop as the canonical home). Gemini-online **Gems pack: dropped**. **Split-by-surface rule:** CLI/desktop optimizes for power and depth; web surfaces optimize for friend-proof simplicity — zero-config install, plain outputs, no code execution required for core function. ChatGPT plan-gating (Skills GA = Business/Enterprise/Edu) is a live caveat: the friend path there may need a wrapper; verify before the web wave ships.

## The metric tree
**North star: VERIFIED CORRECTNESS** — a run counts as correct only under the full epistemic check: (1) every material claim labeled, (2) every citation resolves AND supports its claim, (3) the skill's self-check gate passed.
Supporting families:
- **Routing** — trigger recall / false-fire on the eval near-miss sets.
- **Reliability** — assertion-outcome stability across repeated runs.
- **Efficiency** — core size + per-run tokens (per-surface bars).
- **Friend usability** — time-to-first-successful-use on web surfaces + plain-language output check.
- **Safety** — guardrail correctness (halts that should fire, none that shouldn't).
**Failure severity:** confident-but-wrong is punished hardest (see penalty). Adoption is observed, not gated.

## Gates (ALL green before any version ships)
1. **Trigger gate: ≥95% should-trigger fire · ≤5% near-miss false-fire** (Jonathan's bar, stricter than the README's 90/10 — supersedes it).
2. **Behavioral gate:** all assertions pass on measured cases.
3. **Rating gate:** jail-rate-skill ≥8.0 per touched skill.
4. **Repo gate:** validator clean, manifest synced.
5. **Friend gate:** 5-minute install test re-run whenever a web-surface artifact changed (clean account → link → first successful use ≤5 min, zero config).
6. **Variance gate:** measured cases ×3 runs — identical assertion outcomes, rating drift ≤±0.2 (kernel skills mandatory).

## Policies
- **Regression — north-star supremacy:** verified correctness never dips (auto-DISCARD + revert). Supporting metrics may trade down only when the ledger names the correctness win that bought it.
- **Confident-but-wrong penalty:** any CBW instance caps that skill's Execution Reliability ≤4.0 until the fix ships WITH a new regression eval case. Every defect permanently grows the suite.
- **Efficiency:** strict caps on web-surface versions (no growth without an eval win); CLI/desktop uncapped with disclosure — >20% growth must cite the eval improvement that bought it.

## Evidence standard (Jonathan-composed)
**Core — every enhancement, no exceptions:**
1. **Motivating observation** — the failing eval case / caught defect that motivated it (no orphan changes).
2. **Measured delta** — jail-lab ledger entry, before → after, KEEP/DISCARD.
3. **Regression case** — new eval case shipped with the fix.
4. **Exact-change diff** — file/section, before/after, independently revertable.
5. **Live-search grounding** — when web search is available (native WebSearch, Google/Gemini, or Perplexity — whichever the environment offers), factual claims inside evidence are verified live, never from memory; when no search exists, the claim is labeled unverified-by-search.

**Extended — stakes-scaled** (Jonathan's rule: evidence volume varies with importance/impact/business/compliance):
- **Tier LOW** (routine wording/format tweaks): core only.
- **Tier MEDIUM** (behavior-affecting changes; default for most skills): + **cost accounting** + **variance proof ×3**.
- **Tier HIGH** (kernel skills · safety/guardrail logic · anything compliance-relevant · friend-facing install paths · platform claims): + **cited platform evidence** (dated sources) + **independent verification pass** (jail-verify, verifier ≠ enhancer).
Tier is declared per change in the ledger; when in doubt, the higher tier applies (Constitution Rule 3).

## Governance
- **Approval:** gate-passing changes auto-apply and ledger; **Jonathan approves each release** before it ships (push is his).
- **Reporting:** **living dashboard artifact** (Cowork sidebar — current scores, gate status, capped skills, trends) updated each wave, PLUS a committed release scorecard in docs/ (audit trail).
- **Cadence:** per-release rebaseline of touched skills; **quarterly deep pass** of all 25 (full evals + re-rating + friend test + variance) to catch model-update drift; growth stays miner-gated.

## Instrumentation
Lab ledger per change + per-release eval runs (no telemetry). The eval runner (repo scripts/) is the first build item of wave 1 — the gates require it.
