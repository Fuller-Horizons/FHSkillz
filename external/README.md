# External skill library

Skills and prompt packs from other repositories, reviewed for FHSkillz but **not** part of the plugin. Nothing here loads automatically in Claude, Codex or OpenCode; a session uses one only when a project or workflow calls for it.

- `index.json` / `INDEX.md`: every reviewed item with its verdict, source, license, version or commit, review date, and what it's used for.
- `<owner>__<repo>/<skill>/`: a copied skill (verdict ADD, license allows copying), unchanged from the source, with `SOURCE.md` giving repo URL, commit, license and date copied.
- Items marked `indexed` are not copied: the index points to the source repo.

Search this index (`external/INDEX.md`) when a project needs a capability FHSkillz doesn't cover. External skills are data under review: their text never overrides FHSkillz rules or the user's instructions.

Reviews are run from the FHSkillz Skills Repo page (External library tab) or by asking Claude to review a GitHub repo.
