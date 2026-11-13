#!/usr/bin/env python3
"""build-external-index.py — regenerate external/INDEX.md from external/index.json.

The external library holds third-party skills reviewed for FHSkillz but not part
of the plugin. index.json is the source of truth; INDEX.md is the searchable view
Claude reads when a project needs something FHSkillz lacks.
Repo tooling (infrastructure), not skill content. Stdlib only.
Usage: build-external-index.py [--check]
"""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = os.path.join(ROOT, "external", "index.json"), os.path.join(ROOT, "external", "INDEX.md")
M = ["usability", "need", "efficiency", "speed", "accuracy", "safety"]
P = ["ChatGPT", "Codex", "Claude", "Claude Code", "OpenCode"]
ICON = {"y": "✓", "n": "✕", "q": "?"}


def render(d):
    L = ["# External skill index (generated from index.json)", "",
         f"Updated {d['updated']}. Search here when a project needs something FHSkillz doesn't cover; "
         "open the source only when you'll use it. Scores 0.0-10.0 (U usability, N need, E efficiency, "
         "S speed, A accuracy, Sf safety). Platforms: ✓ works, ? partial or unverified, ✕ doesn't.", "",
         "## Items", "",
         "| Skill | Repo | Date | Category | Used when | Keywords | U | N | E | S | A | Sf | Avg | Tested | " + " | ".join(P) + " | Type | Verdict | License |",
         "|" + "---|" * (14 + len(P) + 3)]
    for i in d["items"]:
        sc = i.get("scores", {})
        vals = [sc.get(k) for k in M]
        avg = round(sum(v for v in vals if v is not None) / max(1, sum(v is not None for v in vals)), 1) if any(v is not None for v in vals) else ""
        cp = i.get("compat", {})
        L.append(f"| {i['name']} ({i.get('version','')}) | [{i['repo']}](https://github.com/{i['repo']}/tree/main/{i.get('path','')}) | {i.get('date','')} | "
                 f"{i.get('category','')} | {i.get('used_when','')} | {', '.join(i.get('keywords', []))} | " + " | ".join("" if v is None else f"{v:.1f}" for v in vals) +
                 f" | {avg} | {i.get('tested','read')} | " + " | ".join(ICON.get(cp.get(p, 'q'), '?') for p in P) +
                 f" | {i.get('type','')} | {i.get('verdict','')} | {i.get('license','')} |")
    L += ["", "## Reviews", "", "| Repo | License | Commit | Reviewed | Outcome |", "|---|---|---|---|---|"]
    for r in d["reviews"]:
        L.append(f"| [{r['repo']}]({r['url']}) | {r.get('license','')} | {r.get('commit') or '—'} | {r.get('reviewed','')} | {r.get('verdict') or r.get('outcome','')} |")
    return "\n".join(L) + "\n"


def main():
    text = render(json.load(open(SRC, encoding="utf-8")))
    old = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
    if "--check" in sys.argv[1:]:
        if old != text:
            print("build-external-index: external/INDEX.md is stale, run scripts/build-external-index.py")
            return 1
        return 0
    open(OUT, "w", encoding="utf-8").write(text)
    print("build-external-index: wrote external/INDEX.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
