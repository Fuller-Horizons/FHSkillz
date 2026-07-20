# FHSkillz

**Fuller Horizons' Claude skills — bundled as one installable plugin.**

FHSkillz packages every Fuller Horizons Claude skill into one plugin (`fh-skillz`) and registers this repo as a Claude **plugin marketplace**. Add the marketplace once and every skill installs together; skills then activate automatically based on their `description` — nothing to load by hand.

## Available skills

### Layer 1 — Reasoning kernel (governs all work)

| Skill | What it does |
|---|---|
| [`jail-prompt`](skills/jail-prompt/) | Pre-flight that turns a vague goal into a **STOP** or an engineered, verifiable, token-efficient prompt. |
| [`jail-task-contract`](skills/jail-task-contract/) | Executable task contracts before work begins; scope guarding after — material change = new contract. |
| [`jail-research`](skills/jail-research/) | Research into a citable evidence packet — tiered dated sources, contradictions weighed, honest gaps. |
| [`jail-verify`](skills/jail-verify/) | Independent verification against the contract, on real artifacts — never on an agent's say-so. |
| [`jail-decide`](skills/jail-decide/) | Decision packages: criteria first, do-nothing priced, reversibility named, change-conditions stated. |
| [`jail-red-team`](skills/jail-red-team/) | Adversarial pressure-testing — steelman first, three lenses, full bias sweep on consequential calls. |
| [`jail-orchestrate`](skills/jail-orchestrate/) | Multi-agent runs: delegation gates, scoped briefs, verified-node resume ledger, evidence-based merge. |
| [`jail-approval-gate`](skills/jail-approval-gate/) | Action tiers (never/per-action/batchable/auto), fail-closed, proper approval requests, audit trail. |
| [`jail-quarantine`](skills/jail-quarantine/) | Inbound data quarantined until adopted; protected data halts processing and fails closed. |
| [`jail-memory`](skills/jail-memory/) | Memory governance (six-check ingestion gate, supersede-don't-delete) + the learning-postmortem ritual. |
| [`jail-lab`](skills/jail-lab/) | Metric-driven experiment loops with an append-only audit ledger — adapted from karpathy/autoresearch (MIT). |
| [`jail-skill-miner`](skills/jail-skill-miner/) | Mines codebases/histories for plugin-worthy disciplines; dedupes against installed skills; stops for approval. |

### Layer 2 — Workflow skills

| Skill | What it does |
|---|---|
| [`jail-rate`](skills/jail-rate/) | Universal evidence-cited **0–10 rating of anything**, weighted rubric per subject type, current → projected. |
| [`jail-operationalize`](skills/jail-operationalize/) | Recommendations → 13-field operating workflows a named owner can run (trigger → testable completion). |
| [`jail-exec-brief`](skills/jail-exec-brief/) | Decision-ready executive communication; technical findings translated into business consequences. |
| [`jail-rate-skill`](skills/jail-rate-skill/) | Rates AI skills on a 10-category matrix + IDE/CLI compatibility, machine-readable record. |
| [`jail-prospect`](skills/jail-prospect/) | US private company as a sell-side/consulting prospect — free sources, cited one-page brief. |

### Layer 3 — Domain packs

| Skill | What it does |
|---|---|
| [`jail-pestle`](skills/jail-pestle/) | Evidence-grounded PESTLE tied to a subject + decision, with tripwires per factor. |
| [`jail-swot`](skills/jail-swot/) | Evidence-sorted SWOT → TOWS strategies; the misclassification traps enforced. |
| [`jail-bmc`](skills/jail-bmc/) | Nine-block BMC — validated vs hypothesis never blurred; riskiest assumptions get experiments. |
| [`jail-cpr`](skills/jail-cpr/) | Context·Purpose·Results meeting design; agendas reverse-engineered from testable Results. |

### JAIL-PY companions (optional; need code execution)

| Skill | Backs |
|---|---|
| [`jail-py-prompt-tools`](skills/jail-py-prompt-tools/) | jail-prompt — secret scan, prompt/chain/truth lint, dry-run. |
| [`jail-py-rate-tools`](skills/jail-py-rate-tools/) | jail-rate-skill — validate/save records, variance check, structure lint. |
| [`jail-py-lab`](skills/jail-py-lab/) | jail-lab — experiment ledger bookkeeping and reports. |

**System docs:** the [JAIL Constitution](docs/JAIL-CONSTITUTION.md) (12 rules + the handoff contract every kernel skill ends with) · the [skill graph](docs/skill-graph.md) (routing registry) · [wave-3 roadmap](docs/ROADMAP-wave3-domain-packs.md).

**House rule:** core skills are instruction-only (no bundled code); anything runnable ships as a `jail-py-*` companion skill the core references with a manual fallback.

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
