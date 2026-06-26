# FHSkillz

**Fuller Horizons' Claude skills — bundled as one installable plugin.**

FHSkillz packages every Fuller Horizons Claude skill into one plugin (`fh-skillz`) and registers this repo as a Claude **plugin marketplace**. Add the marketplace once and every skill installs together; skills then activate automatically based on their `description` — nothing to load by hand.

## Available skills

| Skill | What it does |
|---|---|
| [`jail-prompt`](skills/jail-prompt/) | Pre-flight workflow that turns a vague goal into either a **STOP** (when AI is the wrong tool or the idea is flawed) or an engineered, verifiable, token-efficient prompt — with prompt-chaining, epistemic truth-tagging, and built-in verification. |
| [`company-prospect-research`](skills/company-prospect-research/) | Researches a US private company as a sell-side brokerage / consulting prospect using only free, authoritative sources. Outputs a one-page brief with a Likelihood-to-Sell score, a Consulting-Opportunity score, red flags, an outreach hook, and a cited source appendix. |
| [`jail-rate`](skills/jail-rate/) | Rates a software product on a disciplined 0.0–10.0 scale across five weighted dimensions — quality, features, usability, marketability, security — with prioritized recommendations and a projected post-fix score. |
| [`rate-skill`](skills/rate-skill/) | Evaluates and rates another AI skill using a 10-category Skill Rating Matrix plus IDE/CLI compatibility matrices, with a machine-readable, validated JSON record tracked over time. |

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
│   └── scripts/                      # optional runnable helpers
├── scripts/                          # new-skill / sync-marketplace / install / build-zips
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
- Bump `plugins[0].version` (semver) in `marketplace.json` on any release that changes skills.
- **Never commit `.zip` files** (`dist/` is gitignored) — the plugin installer rejects nested ZIPs and the install will fail.
- Keep the repo **public** so `/plugin marketplace add` and the raw `install.sh` URL resolve.

## License

[MIT](LICENSE) © Fuller Horizons.
