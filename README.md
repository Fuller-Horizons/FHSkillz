# FHSkillz

**Fuller Horizons' Claude skills — bundled as one installable plugin.**

FHSkillz is a bundle of 26 Claude skills for real work. It is built for consultants, founders, ops leads, and anyone who runs decisions, research, or client work through Claude and needs careful reasoning, not just a fast answer.

Each skill covers one job. One skill helps you decide between two options and defend the pick. Another checks a finished deliverable against real evidence before you ship it. A third turns a scraped contact list into something safe to load into your CRM. Install the whole set once (`fh-skillz`), and this repo registers itself as a Claude **plugin marketplace**. Skills then activate on their own, based on the `description` field in each one — nothing to load by hand.

## Available skills

The skills sort into four groups below. Every skill name links to its own folder, and every skill's own README shows a full, real worked example — the tables here just point you to it.

### Layer 1 — Reasoning kernel (governs all work)

| Skill | Use it when | What you get |
|---|---|---|
| [`jail-prompt`](skills/jail-prompt/) | You have a goal but no real prompt written for it yet | A go/stop verdict, then a copyable prompt with a built-in pass/fail test |
| [`jail-task-contract`](skills/jail-task-contract/) | A request is vague, risky, or has many threads, and you want scope agreed before work starts | A 14-field contract naming the goal, the risks, and a testable finish line |
| [`jail-research`](skills/jail-research/) | You need a real, sourced answer before a decision, not just an opinion | A short cited answer plus an evidence packet listing every source and date |
| [`jail-verify`](skills/jail-verify/) | Someone says a task is done and you want proof, not their word for it | One verdict — pass, fail, or pass-with-flags — backed by a count of real checks |
| [`jail-decide`](skills/jail-decide/) | You have to pick between options and need to defend the choice | A decision package with priced options, one pick, and the facts that would flip it |
| [`jail-red-team`](skills/jail-red-team/) | A costly plan is about to ship and you want real holes found first | A ranked list of flaws, each with a fix and a cheap test to prove it right or wrong |
| [`jail-council`](skills/jail-council/) | A call is contested and being wrong would be expensive | One final answer with confidence, sources, and any real disagreement left standing |
| [`jail-orchestrate`](skills/jail-orchestrate/) | A job needs several agents, or spans many sessions, and you can't lose your place | A step-by-step ledger with proof behind each step, and one merged result |
| [`jail-approval-gate`](skills/jail-approval-gate/) | An agent is about to send, spend, publish, or delete something on its own | A risk tier for every action, approval requests for the risky ones, and an audit log |
| [`jail-quarantine`](skills/jail-quarantine/) | You just scraped or received outside data and don't fully trust it yet | A report of what's held for review, what's missing, and what got halted for safety |
| [`jail-memory`](skills/jail-memory/) | You want to save a lesson for later, or check what you already decided | Each saved entry with its source, or a plain reason it was refused |
| [`jail-lab`](skills/jail-lab/) | You want to test changes one at a time and track what actually worked | A declared metric and budget, plus a ledger of every try with a keep-or-discard call |
| [`jail-skill-miner`](skills/jail-skill-miner/) | You want to know if your own codebase hides a reusable skill worth building | A short table of candidates, each with evidence and whether it's new or a duplicate |
| [`jail-diagnose`](skills/jail-diagnose/) | A bug is real but the cause won't pin down, or a first fix didn't hold | A diagnosis with the proven cause, the fix, and a permanent test so it can't come back |
| [`jail-prototype`](skills/jail-prototype/) | Your team is stuck arguing over one design question that talking can't settle | A one-page verdict answering that one question; the throwaway code then gets deleted |
| [`jail-handoff`](skills/jail-handoff/) | You're ending a session and want to resume later without re-explaining everything | A short baton file: the goal, what's done, what's next, and why you chose each thing |
| [`jail-plan`](skills/jail-plan/) | You have a decision to turn into a real process (**OPERATE** lane), or a big goal with no clear starting point (**MAP** lane) | A 13-field workflow with a named owner and finish line, or a map of the open decisions |

### Layer 2 — Workflow skills

| Skill | Use it when | What you get |
|---|---|---|
| [`jail-rate`](skills/jail-rate/) | You need a fair, evidence-based score on software, a product, or an idea | A weighted scorecard with sourced evidence and a ranked list of fixes |
| [`jail-summarize`](skills/jail-summarize/) | You have technical findings and need the business version for a busy executive | A short brief that opens with the outcome and ends with one clear recommendation |
| [`jail-rate-skill`](skills/jail-rate-skill/) | You want to know if an AI skill is ready to ship, or which of two is better | A 10-category score table, one concrete fix per row, and a re-scored total |
| [`jail-prospect`](skills/jail-prospect/) | You want to know if a business owner might sell, or where a consulting angle fits | A one-page brief with two 0–100 scores, red flags, and every source used |

### Layer 3 — Domain packs

| Skill | Use it when | What you get |
|---|---|---|
| [`jail-strategy`](skills/jail-strategy/) | You need a SWOT, a macro scan, or both, tied to one real decision | Sorted SWOT and/or PESTLE tables, plus a table of moves you can act on |
| [`jail-bmc`](skills/jail-bmc/) | You need a business model canvas that separates proof from hope before a raise or a pivot | A nine-block canvas with proven-vs-guessed labels, and the riskiest guesses to test first |
| [`jail-cpr`](skills/jail-cpr/) | Your meetings decide nothing and you want an agenda built backward from real outputs (**DESIGN**), or you want a personal/team commitment contract for a set period with no meeting at all (**COMMIT**) | A timed agenda where every item names an owner and output — or a dated, testable Results contract for the period — plus a scored debrief/audit after (**DEBRIEF**) |

### JAIL-PY companions (optional; need code execution)

These two are optional. They run real code to back checks that `jail-prompt`, `jail-rate-skill`, and `jail-lab` would otherwise do by hand. Skip them if you don't run Python — the core skills still work without them, just less mechanically.

| Skill | Use it when | What you get |
|---|---|---|
| [`jail-py-toolkit`](skills/jail-py-toolkit/) | You want a real script to catch secrets, weak prompts, or a broken skill folder before you ship | A pass-or-fail report per script, with an exit code your CI or commit hook can read |
| [`jail-py-lab`](skills/jail-py-lab/) | You're running a jail-lab experiment and want the ledger and math kept for you | A ledger file that grows one line per try, plus a KEEP or DISCARD call on each one |

**System docs:** the [JAIL Constitution](docs/JAIL-CONSTITUTION.md) (12 rules + the handoff contract every kernel skill ends with) · the [skill graph](docs/skill-graph.md) (routing registry) · [wave-3 roadmap](docs/ROADMAP-wave3-domain-packs.md).

**House rule:** core skills are instruction-only (no bundled code); anything runnable ships as a `jail-py-*` companion skill the core references with a manual fallback.

## See it work

Every example in this repo, including the three below, is copied straight from a real run of the skill. None of it is written by hand. We picked one reasoning-kernel skill, one domain-pack skill, and one JAIL-PY companion, to show the range of what's in here.

**[`jail-decide`](skills/jail-decide/)** (Layer 1) — a VP of Sales needs to decide between renewing Salesforce, negotiating a discount, or switching to HubSpot before a contract deadline. Real excerpt from the skill's output:

```
Ship-check: criteria-first PASS · do-nothing priced PASS · door type per option PASS · ≥2 change-conditions PASS · every number carries Fact/Estimate+source PASS · owner named PASS · council check recorded PASS

DECISION PACKAGE
Decision: Renew Salesforce as-is, negotiate a discounted 2-year renewal, or switch to HubSpot before the Salesforce contract auto-renews on Sept 30 · Owner: Maria Chen, VP of Sales · Needed by: Aug 15, 2026 (45-day notice deadline)

Criteria (weighted):
1. Cut SaaS spend toward the CFO's 20% target [High]
2. Protect Q4 pipeline — $2.1M open [High]
3. Keep the territory management and forecasting the 40 reps use [Medium]
4. Minimize lock-in [Medium]

Options table:

| Option | Benefits | Costs | Risks | Reversibility | Delay cost |
|---|---|---|---|---|---|
| Do-nothing (renew as-is) | No disruption; team trained | $65,520/yr [Fact, AE email 7/20]; $131K/2yr [Estimate, flat renewal] | Misses the 20% target; spend keeps climbing | Two-way — revisit next cycle | Resets the clock another year |
| Negotiate 2-yr renewal | 15% off; zero migration risk | $55,692/yr avg, $111K/2yr [Estimate, AE verbal 7/20, unconfirmed] | 5 points short of target; discount unconfirmed; ~40% early-term penalty [Estimate, standard clause] | One-way, 2 yrs (termination penalty) | Offer expires at the 9/30 renewal |
| Switch to HubSpot | $28,800/yr, hits target; ties to Marketing Hub | $28,800/yr + $23K one-time [Fact 7/18 / Estimate 7/22]; pays back in ~8 months | No territory management [Fact, demo 7/19]; risks $2.1M Q4 pipeline [Fact, 7/21] | One-way ~1 yr (~$15K [Estimate] to reverse) | Must finish by 9/30 or lose the Q4-safe window |
...
Confidence: medium — discount isn't in writing yet; savings only partly meets the CFO's target.
```

Full run: [`skills/jail-decide/README.md`](skills/jail-decide/README.md).

**[`jail-plan`](skills/jail-plan/)** (Layer 1, OPERATE lane) — a decision to go proactive on at-risk customer accounts needs to become a workflow the customer-success team can actually run every week. Real excerpt from the skill's output:

```
Gate check: all 13 fields filled or justified PASS · field 6 resolved per step (2 items sent for explicit approval, marked pending below) PASS · every action step is a yes/no-checkable verb PASS

OPERATING WORKFLOW: At-Risk Account Proactive Outreach — Fernbank Metrics CS team

Upstream decision: 2026-07-14 jail-decide package — "Launch proactive at-risk-account outreach instead of waiting for cancellation notices." Recommendation: proactive outreach, confidence high, not contested — jail-red-team not invoked.

1. **Trigger** — ChurnZero fires a "usage-drop" alert when a paying account's weekly active-seat usage falls 40% or more week-over-week for two consecutive weeks (two weeks, not one, to filter out single bad weeks from holidays or vacations).
...
6. **Approval** — tiered per jail-approval-gate (the gate skill was not separately invoked this run; tiers are stated here and approvals requested inline, per the fail-closed fallback):
   - Steps 1-3 (review alert, send check-in, log outcome): reversible, matches an existing CS motion, homogeneous across accounts → tier **BATCHABLE**, approved as a pattern via the request below.
   - Step 4 (any account credit or discount): spend → tier **PER-ACTION**, no threshold exception under jail-approval-gate. Every credit needs Sam Diaz's sign-off before it is applied, regardless of size.
   - Steps 5-6 (internal review, internal reporting): reversible and workspace-internal → tier **AUTO**.
```

Full run: [`skills/jail-plan/README.md`](skills/jail-plan/README.md).

**[`jail-py-toolkit`](skills/jail-py-toolkit/)** (JAIL-PY companion) — before committing a new skill draft, its scripts scan a config file for secrets, lint a prompt, and check the folder structure. This one shows real terminal output and real exit codes, not prose:

```
Ran the three backing scripts against the drafted files, from inside the draft folder.

$ python3 "C:/Dev/FHSkillz/skills/jail-py-toolkit/scripts/secret-scan.py" invoice_config.py
secret-scan: 2 potential secret(s) found:

  invoice_config.py:7: Stripe secret key -> sk_live_51Hj…
  invoice_config.py:8: OpenAI/Anthropic key -> sk-abcdefghi…

Replace these with environment variables (e.g. os.environ['API_KEY']) and use a restricted, read-only credential before generating the prompt.
EXIT:1

$ python3 "C:/Dev/FHSkillz/skills/jail-py-toolkit/scripts/prompt-lint.py" invoice_prompt.txt
prompt-lint: PASS (0 warning(s)).
EXIT:0

$ python3 "C:/Dev/FHSkillz/skills/jail-py-toolkit/scripts/validate-skill-structure.py" invoice-parser
[+] Skill structure valid (1 checked).
EXIT:0

Summary — fix before you commit:
- secret-scan.py: fail. Two hardcoded keys in invoice_config.py, line 7 (Stripe) and line 8 (OpenAI). Move both to environment variables before this ships.
- prompt-lint.py: pass. All five required sections are present, the SUCCESS TEST is machine-verifiable, and OUTPUT FORMAT shows a worked JSON example.
- validate-skill-structure.py: pass. SKILL.md has frontmatter name + description, and the folder name matches.
```

Full run: [`skills/jail-py-toolkit/README.md`](skills/jail-py-toolkit/README.md).

## Install

**Claude Code or Cowork (loads every skill):**

```
/plugin marketplace add Fuller-Horizons/FHSkillz
/plugin install fh-skillz@fh-skillz
```

Restart / reload. Skills activate automatically based on their `description`. Update later with:

```
/plugin marketplace update fh-skillz
/plugin update fh-skillz
```

**Cowork / desktop — no commands:** **Settings → Customize → Plugins**, find **fh-skillz**, and click **Install** (or **Update** if it's already added). This installs every skill in the plugin from this repo's `main` branch.

**OpenCode CLI:**

OpenCode discovers skills from `~/.claude/skills` and `.claude/skills` natively, so the standard installer works with no extra configuration:

```
curl -fsSL https://raw.githubusercontent.com/Fuller-Horizons/FHSkillz/main/scripts/install.sh | bash
```

Prefer OpenCode's own skill paths? Pass one as an argument — global `… | bash -s -- ~/.config/opencode/skills`, or per-project `… | bash -s -- .opencode/skills`. Re-run anytime to pull latest and re-link.

Skills stay model-invoked as everywhere else; an agent can also load one explicitly with OpenCode's native `skill` tool — `skill({ name: "jail-council" })`.

**OpenCode is the only CLI where a Tier-A (cross-provider) `jail-council` is native.** Each subagent can be pinned to a different provider with `"model": "provider/model-id"` in `opencode.json`, so a council of Claude + GPT + Gemini is real rather than three sessions of the same model. Run `opencode models` to list what your configured providers offer, then follow the verified config and protocol in [`skills/jail-council/references/opencode-runbook.md`](skills/jail-council/references/opencode-runbook.md). Watch the headline gotcha: omitting `model:` on a member makes it inherit the caller's model, silently collapsing the council to Tier C while still reporting as cross-provider.

**Any IDE / Cursor / Codex CLI (skills-directory fallback):**

```
curl -fsSL https://raw.githubusercontent.com/Fuller-Horizons/FHSkillz/main/scripts/install.sh | bash
```

Scope to a single project instead: clone, then `./scripts/install.sh .claude/skills`. Re-run anytime to pull latest and re-link.

> **Single-skill upload to Claude.ai web?** The plugin install above is the supported path. Per-skill upload ZIPs are **not** committed to this repo (the plugin installer rejects nested ZIPs), so build one locally with `./scripts/build-zips.sh` and upload it under **Settings → Customize → Skills**, or have a maintainer attach ZIPs to a GitHub Release.

## How it works

Each skill lives in `skills/<name>/` with a `SKILL.md`. Skills are **model-invoked** — Claude fires them based on the `description` field. `.claude-plugin/marketplace.json` lists every skill and is the single source of truth for what loads; `.claude-plugin/plugin.json` is the plugin manifest.

```
FHSkillz/
├── .claude-plugin/
│   ├── marketplace.json              # install manifest (lists every skill)
│   └── plugin.json                   # plugin manifest (name, version, author)
├── skills/<name>/
│   ├── SKILL.md                      # required — the skill + its trigger description
│   ├── references/                   # optional reference docs (progressive disclosure)
│   └── scripts/                      # jail-py-* companion skills only — core skills are code-free
├── scripts/                          # repo tooling: new-skill / sync-marketplace / validate-skills / install / build-zips
├── docs/                             # legacy + design documents (not part of the plugin)
└── CLAUDE.md                         # repo guidance for Claude when maintaining this repo
```

The marketplace entry uses `strict: false` with an explicit `skills[]` array, so each skill ships as a raw `SKILL.md` folder with **no per-skill `plugin.json`** required. ZIP build artifacts are written to a gitignored `dist/` and are **never committed** — the GitHub plugin installer zips the whole repo and rejects nested `.zip` files.

## Add a skill

```
./scripts/new-skill.sh my-skill        # scaffold skills/my-skill/SKILL.md + auto-register
# edit skills/my-skill/SKILL.md  — write a strong description; it's the trigger
./scripts/sync-marketplace.sh          # ensure the manifest matches the folders
# bump plugins[0].version in .claude-plugin/marketplace.json (and plugin.json)
git add -A && git commit -m "add my-skill skill" && git push
# then refresh:  /plugin marketplace update fh-skillz
```

The **description is the product** — a weak description means a skill that never triggers. Write it as a router: concrete task verbs, file/input types, and trigger keywords.

## Conventions

- One skill = one folder under `skills/` containing a `SKILL.md`. Folder name == frontmatter `name`, lowercase-hyphenated (`[a-z0-9-]` only).
- `SKILL.md` frontmatter requires `name` and `description`. Keep `SKILL.md` lean; push long material into `references/` and link it.
- **Core skills are instruction-only.** Runnable code ships in `jail-py-*` companion skills; a core skill referencing one always states a manual fallback.
- Bump `plugins[0].version` (semver) in `marketplace.json` on any release that changes skills.
- **Never commit `.zip` files** (`dist/` is gitignored) — the plugin installer rejects nested ZIPs and the install will fail.
- Keep the repo **public** so `/plugin marketplace add` and the raw `install.sh` URL resolve.

## License

[MIT](LICENSE) © Fuller Horizons.
