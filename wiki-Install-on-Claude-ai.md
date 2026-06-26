# Install the FHSkillz skills (the easy way)

No git, no terminal. About 2 minutes. This installs **every** Fuller Horizons skill at once as the `fh-skillz` plugin.

> You need a plan that supports custom skills/plugins (Pro, Max, Team, or Enterprise — not the free plan), and the Claude desktop app / Cowork or Claude Code.

---

## Step 1 — Turn on code execution

1. In Claude, open **Settings**.
2. Open **Capabilities**.
3. Turn **on** *Code execution & file creation*.

Skills won't run without this, so don't skip it.

---

## Step 2 — Install the plugin

**Desktop / Cowork (clicks only):**

1. Go to **Settings → Customize → Plugins**.
2. Find **fh-skillz** (by FHSkillz). If it isn't listed, add the marketplace first: choose **Add marketplace** and enter `Fuller-Horizons/FHSkillz`.
3. Click **Install**.

**Claude Code (commands):**

```
/plugin marketplace add Fuller-Horizons/FHSkillz
/plugin install fh-skillz@fh-skillz
```

That's it — all the skills come in together (jail-prompt, company-prospect-research, jail-rate, rate-skill).

---

## Step 3 — Try it

Restart / reload, then start a normal chat and type something like:

> *I want my landing page to convert better — help me prompt this the right way.*

The `jail-prompt` skill should kick in automatically. Skills fire on their own based on what you ask — there's nothing to turn on per skill.

---

## Updating later

When new skills or versions ship, refresh:

- **Desktop / Cowork:** Settings → Customize → Plugins → **fh-skillz** → **Update**.
- **Claude Code:**
  ```
  /plugin marketplace update fh-skillz
  /plugin update fh-skillz
  ```

Reload the app afterward so the new versions load.

---

## Notes

- Installed skills are **private to your account**. On Team/Enterprise plans an admin can share them org-wide.
- Only install skills from people you trust — skills can contain code.
- **Want just one skill on Claude.ai web (not the whole plugin)?** Build that skill's upload ZIP locally with `./scripts/build-zips.sh` and upload it under **Settings → Customize → Skills**. (ZIPs aren't kept in the repo — the plugin installer rejects nested ZIPs — so there's no `dist/` download link.)
