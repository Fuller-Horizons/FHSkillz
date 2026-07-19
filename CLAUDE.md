# FHSkillz — repo guidance for Claude

You are the maintainer of the Fuller-Horizons/FHSkillz repository: a single GitHub
repo that bundles all of Fuller Horizons' Claude skills as one installable plugin
("fh-skillz") and registers itself as a Claude Code plugin marketplace.

## REPO INVARIANTS (never violate)
- Every skill lives in `skills/<skill-name>/` and contains a `SKILL.md`.
- Skill folder name == frontmatter `name`, lowercase-hyphenated, `[a-z0-9-]` only.
- `SKILL.md` frontmatter MUST have `name` and `description`. The description is the
  trigger text — write it as a router: concrete task verbs, input/file types, and
  keywords that should make Claude invoke it. Vague descriptions are rejected.
- `.claude-plugin/marketplace.json` is the install manifest. `plugins[0].skills` MUST
  list every skill folder, each as `"./skills/<name>"`. Keep `strict:false`.
- Bump `plugins[0].version` (semver) on any release that changes skills.

## WHEN ASKED TO CREATE A SKILL
1. Run `scripts/new-skill.sh <name>` (creates folder + SKILL.md + registers it).
2. Write a strong description and instructions in the SKILL.md.
3. Run `scripts/sync-marketplace.sh` to confirm marketplace.json is in sync.
4. Validate (see CHECKS), then commit and push with message "add <name> skill".

## WHEN ASKED TO EDIT/REMOVE A SKILL
- Edit files in `skills/<name>/`. If removing, delete the folder, then run
  `scripts/sync-marketplace.sh` so marketplace.json no longer references it.
- Commit + push with a clear message.

## CHECKS before every commit
- Run `python3 scripts/validate-skills.py` (frontmatter, name==folder, link rot).
- Each `skills/*/` has a SKILL.md with valid YAML frontmatter (name + description).
- Folder name matches frontmatter name. No spaces/uppercase/underscores in names.
- marketplace.json is valid JSON and skills[] exactly matches the folders present.
- No secrets/keys committed.

## CONVENTIONS
- Keep SKILL.md short; put long content in `skills/<name>/references/` and link it.
- **Code-free core skills.** Core skills are instruction-only — no Python or other
  runnable code inside them. Runnable helpers live in dedicated `jail-py-*`
  companion skills (e.g. `jail-py-prompt-tools`, `jail-py-rate-tools`); a core
  skill references its companion by name and always states a manual fallback.
- Repo maintenance tooling (`scripts/`, `hooks/`) is infrastructure, not skill
  content — it may contain code.
- Default git remote: https://github.com/Fuller-Horizons/FHSkillz (branch: main).

Always run the actual scripts and git commands rather than describing them.
After changes, tell me the exact `/plugin` commands to refresh the install.
