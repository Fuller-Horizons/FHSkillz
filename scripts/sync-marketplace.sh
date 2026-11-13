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
