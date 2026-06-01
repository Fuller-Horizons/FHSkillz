# FHSkillz — Setup & Cowork Project Instructions

A single GitHub repo (`Fuller-Horizons/FHSkillz`) that holds all your individually-created Claude skills and is loadable into **Claude Code** and **IDEs** with one command.

---

## Architecture decision

Bundle every skill into **one plugin** inside the repo, and register the repo as a **plugin marketplace**. This gives the "load everything at once" behavior you want:

```
/plugin marketplace add Fuller-Horizons/FHSkillz
/plugin install fh-skillz@fh-skillz      # loads ALL skills in the repo
```

A clone-and-symlink script (`scripts/install.sh`) covers any tool that reads `~/.claude/skills/` or `.claude/skills/` (Cursor, VS Code, Codex CLI, etc.), so you're not locked to one client.

---

## Final repo layout

```
FHSkillz/
├── .claude-plugin/
│   └── marketplace.json        # registers repo as a marketplace; lists every skill
├── skills/
│   ├── example-skill/
│   │   └── SKILL.md
│   └── <each-new-skill>/
│       ├── SKILL.md            # required
│       ├── scripts/            # optional helper scripts
│       └── references/         # optional reference docs/assets
├── scripts/
│   ├── new-skill.sh            # scaffold a new skill + auto-register it
│   ├── sync-marketplace.sh     # rebuild the skills[] array from skills/ folders
│   └── install.sh              # clone+symlink into ~/.claude/skills (IDE-agnostic)
├── .gitignore
├── CLAUDE.md                   # repo-level guidance for Claude when working in here
└── README.md
```

**Rule:** one skill = one folder under `skills/` containing a `SKILL.md`. Folder name = skill name (lowercase, hyphenated).

---

## Files to create

### `.claude-plugin/marketplace.json`

```json
{
  "name": "fh-skillz",
  "owner": {
    "name": "Fuller Horizons",
    "url": "https://github.com/Fuller-Horizons"
  },
  "metadata": {
    "description": "All Fuller Horizons Claude skills, bundled as one installable plugin."
  },
  "plugins": [
    {
      "name": "fh-skillz",
      "source": "./",
      "description": "Every Fuller Horizons skill. Installs all skills in one command.",
      "version": "0.1.0",
      "strict": false,
      "skills": [
        "./skills/example-skill"
      ]
    }
  ]
}
```

- `strict: false` + the `skills` array lets you ship raw `SKILL.md` folders **without** a per-skill `plugin.json`.
- The `skills` array is the single source of truth for "what loads." `scripts/sync-marketplace.sh` keeps it in sync with the folders so you never edit it by hand.

### `skills/example-skill/SKILL.md` (template for every skill)

```markdown
---
name: example-skill
description: One-to-three sentences describing EXACTLY when Claude should use this skill. Lead with concrete trigger phrases, file types, and task verbs — this text is the only thing the model sees when deciding to invoke. Be specific; vague descriptions never fire.
---

# Example Skill

## When to use
- Bullet the exact situations, inputs, and triggers.

## Instructions
1. Step-by-step procedure Claude should follow.
2. Reference any bundled files by relative path (e.g. `scripts/run.py`, `references/spec.md`).

## Notes / gotchas
- Constraints, edge cases, things to never do.
```

**Frontmatter rules (enforced):**
- `name` — required, lowercase letters/numbers/hyphens, **must match the folder name**.
- `description` — required, the trigger text. Write it like a router: what task, what inputs, what keywords. This is the highest-leverage line in the whole skill.
- Keep `SKILL.md` lean; push long material into `references/` and link to it.

### `scripts/new-skill.sh`

```bash
#!/usr/bin/env bash
# Usage: ./scripts/new-skill.sh my-skill-name
set -euo pipefail
NAME="${1:?Usage: new-skill.sh <skill-name>}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/skills/$NAME"
[ -d "$DIR" ] && { echo "Skill '$NAME' already exists."; exit 1; }
mkdir -p "$DIR"
cat > "$DIR/SKILL.md" <<EOF
---
name: $NAME
description: TODO — describe exactly when Claude should use this skill (triggers, inputs, task verbs).
---

# ${NAME//-/ }

## When to use
- TODO

## Instructions
1. TODO
EOF
echo "Created skills/$NAME/SKILL.md"
"$ROOT/scripts/sync-marketplace.sh"
echo "Registered in marketplace.json. Edit the description before committing."
```

### `scripts/sync-marketplace.sh`

```bash
#!/usr/bin/env bash
# Rebuilds the plugins[0].skills array from every folder under skills/.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MP="$ROOT/.claude-plugin/marketplace.json"
SKILLS=$(cd "$ROOT" && find skills -mindepth 1 -maxdepth 1 -type d \
  -exec test -f '{}/SKILL.md' ';' -print | sort | sed 's|^|./|')
# Build JSON array
ARR=$(printf '%s\n' "$SKILLS" | python3 -c 'import sys,json; print(json.dumps([l.strip() for l in sys.stdin if l.strip()], indent=6))')
python3 - "$MP" "$ARR" <<'PY'
import json, sys
mp_path, arr = sys.argv[1], json.loads(sys.argv[2])
mp = json.load(open(mp_path))
mp["plugins"][0]["skills"] = arr
json.dump(mp, open(mp_path, "w"), indent=2)
open(mp_path, "a").write("\n")
print(f"Synced {len(arr)} skills into marketplace.json")
PY
```

### `scripts/install.sh` (IDE-agnostic clone + symlink)

```bash
#!/usr/bin/env bash
# Clones FHSkillz and symlinks every skill into ~/.claude/skills/.
# Works for any tool that reads ~/.claude/skills (Claude Code, Cursor, Codex, etc.).
set -euo pipefail
REPO="https://github.com/Fuller-Horizons/FHSkillz.git"
SRC="${FH_SKILLZ_DIR:-$HOME/.fh-skillz}"
DEST="${1:-$HOME/.claude/skills}"   # pass .claude/skills to scope to a project
mkdir -p "$DEST"
if [ -d "$SRC/.git" ]; then git -C "$SRC" pull --ff-only; else git clone "$REPO" "$SRC"; fi
for d in "$SRC"/skills/*/; do
  name="$(basename "$d")"
  ln -sfn "$d" "$DEST/$name"
  echo "linked $name -> $DEST/$name"
done
echo "Done. Restart Claude Code / your IDE to load."
```

### `.gitignore`

```
.DS_Store
node_modules/
__pycache__/
*.pyc
```

### `README.md` (skeleton)

```markdown
# FHSkillz

Fuller Horizons' Claude skills, bundled and loadable in one command.

## Install (Claude Code)
\`\`\`
/plugin marketplace add Fuller-Horizons/FHSkillz
/plugin install fh-skillz@fh-skillz
\`\`\`
Restart Claude Code. Skills activate automatically by description.

## Install (any IDE / Codex / Cursor)
\`\`\`
curl -fsSL https://raw.githubusercontent.com/Fuller-Horizons/FHSkillz/main/scripts/install.sh | bash
\`\`\`
Or scope to one project: clone, then `./scripts/install.sh .claude/skills`.

## Add a skill
\`\`\`
./scripts/new-skill.sh my-skill
# edit skills/my-skill/SKILL.md
git add -A && git commit -m "add my-skill" && git push
\`\`\`
```

---

## COWORK PROJECT INSTRUCTIONS (paste this into the Cowork project)

> Copy everything in this block into the project's custom-instructions field.

```
You are the maintainer of the Fuller-Horizons/FHSkillz repository: a single GitHub
repo that bundles all of Fuller Horizons' Claude skills as one installable plugin
("fh-skillz") and registers itself as a Claude Code plugin marketplace.

REPO INVARIANTS (never violate):
- Every skill lives in skills/<skill-name>/ and contains a SKILL.md.
- Skill folder name == frontmatter `name`, lowercase-hyphenated, [a-z0-9-] only.
- SKILL.md frontmatter MUST have `name` and `description`. The description is the
  trigger text — write it as a router: concrete task verbs, input/file types, and
  keywords that should make Claude invoke it. Vague descriptions are rejected.
- .claude-plugin/marketplace.json is the install manifest. plugins[0].skills MUST
  list every skill folder, each as "./skills/<name>". Keep strict:false.
- Bump plugins[0].version (semver) on any release that changes skills.

WHEN ASKED TO CREATE A SKILL:
1. Run scripts/new-skill.sh <name> (creates folder + SKILL.md + registers it).
2. Write a strong description and instructions in the SKILL.md.
3. Run scripts/sync-marketplace.sh to confirm marketplace.json is in sync.
4. Validate (see CHECKS), then commit and push with message "add <name> skill".

WHEN ASKED TO EDIT/REMOVE A SKILL:
- Edit files in skills/<name>/. If removing, delete the folder, then run
  scripts/sync-marketplace.sh so marketplace.json no longer references it.
- Commit + push with a clear message.

CHECKS before every commit:
- Each skills/*/ has a SKILL.md with valid YAML frontmatter (name + description).
- Folder name matches frontmatter name. No spaces/uppercase/underscores in names.
- marketplace.json is valid JSON and skills[] exactly matches the folders present.
- No secrets/keys committed.

CONVENTIONS:
- Keep SKILL.md short; put long content in skills/<name>/references/ and link it.
- Put runnable helpers in skills/<name>/scripts/ and reference by relative path.
- Default git remote: https://github.com/Fuller-Horizons/FHSkillz (branch: main).

Always run the actual scripts and git commands rather than describing them.
After changes, tell me the exact /plugin commands to refresh the install.
```

---

## How it loads (for end users)

**Claude Code (one command, loads all skills):**
```
/plugin marketplace add Fuller-Horizons/FHSkillz
/plugin install fh-skillz@fh-skillz
```
After edits to the repo, refresh with:
```
/plugin marketplace update fh-skillz
```

**Any IDE / Cursor / Codex CLI (skills-directory fallback):**
```
curl -fsSL https://raw.githubusercontent.com/Fuller-Horizons/FHSkillz/main/scripts/install.sh | bash
```
Re-run anytime to pull latest and re-link. Restart the editor to pick up new skills.

---

## Maintenance loop

```
./scripts/new-skill.sh invoice-parser      # scaffold + auto-register
# …write skills/invoice-parser/SKILL.md…
./scripts/sync-marketplace.sh              # ensure manifest matches folders
git add -A && git commit -m "add invoice-parser skill" && git push
# in Claude Code: /plugin marketplace update fh-skillz
```

---

## Gotchas

- Skills are **model-invoked**: they fire based on the `description`, not by being installed. A weak description = a skill that never triggers. Treat the description as the product.
- `skills/` folders that lack a `SKILL.md` are ignored — keep one per folder.
- Cloning the repo into a subfolder of `~/.claude/skills/` does **not** auto-load nested skills; that's why `install.sh` symlinks each skill folder to the top level.
- After changing the repo, run `/plugin marketplace update fh-skillz` or installs stay stale.
- The plugin-marketplace JSON schema is still evolving; if `/plugin` reports a manifest error, check the current spec at the official marketplace repo (github.com/anthropics/claude-plugins-official) and the docs at code.claude.com/docs.
- Make the repo **public** (or configure auth) so `/plugin marketplace add` and the raw `install.sh` URL resolve.
