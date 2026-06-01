#!/usr/bin/env bash
# Packages every skill into dist/<name>.zip, ready to upload to Claude.ai.
# Each archive's ROOT is the skill folder (so it contains <name>/SKILL.md).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST="$ROOT/dist"
mkdir -p "$DIST"
count=0
for d in "$ROOT"/skills/*/; do
  [ -f "$d/SKILL.md" ] || continue
  name="$(basename "$d")"
  tmp="$(mktemp -d)"
  # zip from inside skills/ so the folder itself is the archive root
  ( cd "$ROOT/skills" && zip -rq "$tmp/$name.zip" "$name" \
      -x '*/.DS_Store' '*/__pycache__/*' '*.pyc' )
  # write into dist/ via truncate (works even where unlink is blocked)
  cat "$tmp/$name.zip" > "$DIST/$name.zip"
  rm -rf "$tmp"
  echo "built dist/$name.zip"
  count=$((count+1))
done
echo "Done. $count skill zip(s) in dist/."
