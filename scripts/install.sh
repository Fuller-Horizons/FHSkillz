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
