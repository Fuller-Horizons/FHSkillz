# Keep FHSkillz current everywhere

A release reaches each tool the moment it is merged to `main` (only tested versions are merged). Set each tool up once; after that, every version bump flows through.

| Tool | How it updates | One-time setup |
|---|---|---|
| **claude.ai and the Claude app** | Automatic. The account marketplace syncs `main` within minutes of a merge; new chats load the new version. | Add the plugin once: Settings → Customize → Plugins → **fh-skillz** → Install. |
| **Claude Code** | Automatic once auto-update is on: checks after each launch, then asks you to run `/reload-plugins`. | See below. |
| **Codex CLI** | Pulls from the repo's Codex marketplace (`.agents/plugins/marketplace.json`, `.codex-plugin/plugin.json`, generated). | See below. |
| **OpenCode** | Reads the repo's HTTP skill catalog (`skills/index.json`, generated); a skill's version bump triggers a refresh. | See below. |
| **ChatGPT** | Manual. ChatGPT Skills can't follow a repo; each release attaches upload-ready zips. Business, Enterprise, Healthcare and Edu plans only. | Upload the changed skills' zips from the latest release. |

## Claude Code
Turn on auto-update for the marketplace (third-party marketplaces start with it off): run `/plugin`, open **Marketplaces**, pick **fh-skillz**, choose **Enable auto-update**. Or add this to `~/.claude/settings.json`:
```json
{
  "extraKnownMarketplaces": {
    "fh-skillz": {
      "source": { "source": "github", "repo": "Fuller-Horizons/FHSkillz" },
      "autoUpdate": true
    }
  }
}
```
The check runs in the background after launch; when it finds a new version, run `/reload-plugins` (or just start a new session). Updates are keyed on the plugin version, which every release bumps.
Manual refresh any time: `claude plugin marketplace update fh-skillz` then `claude plugin update fh-skillz@fh-skillz`.

## Codex CLI
```
codex plugin marketplace add Fuller-Horizons/FHSkillz
codex plugin add fh-skillz
```
Refresh: `codex plugin marketplace upgrade fh-skillz`. Codex keys its cache on the plugin version, which every release bumps.

## OpenCode
Add the catalog to `~/.config/opencode/opencode.json`:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["https://raw.githubusercontent.com/Fuller-Horizons/FHSkillz/main/skills/"]
}
```
OpenCode re-downloads a skill when its `version` in the catalog changes.

## ChatGPT
Each merge to `main` with a new plugin version publishes a GitHub release (`.github/workflows/release.yml`) with one zip per skill. In ChatGPT, open Skills and upload the zips for the skills that changed (the release's CHANGELOG entry lists them).

## Why it stays in step
- `scripts/build-catalogs.py` regenerates the Codex manifests, the OpenCode catalog and `docs/SKILL-INDEX.md` from the skills; `validate-skills.py` fails if any is stale, so nothing ships out of sync.
- Every release bumps skill and plugin versions; all four auto-updating tools refresh on a version change.
