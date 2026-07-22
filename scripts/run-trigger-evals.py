#!/usr/bin/env python3
"""run-trigger-evals.py — trigger-eval harness for FHSkillz.

Model-agnostic: this script does the deterministic halves (case loading,
accept-set normalization, blind-manifest generation, scoring vs the ship
gate); a model/agent does the judging in between.

Modes:
  manifest  — load evals/*.json, write judging batches (descriptions + queries,
              NO expected labels) to <out>/manifest-N.json
  score     — read judge picks (JSONL: {"id": ..., "pick": ...}) and compute
              fire-rate / false-fire vs the gate (>=95% / <=5%), per-suite and
              overall; write baseline-report.json; exit 0 pass / 1 fail

Usage:
  python3 scripts/run-trigger-evals.py manifest --repo . --out /tmp/evalrun [--batch 12]
  python3 scripts/run-trigger-evals.py score --out /tmp/evalrun --picks /tmp/evalrun/picks.jsonl

The accept-set map lives in evals/trigger-accept-map.json (case id ->
{"accept": [skill names or "none"], "kind": "fire"|"nofire"}). Cases missing
from the map are skipped with a warning (never silently scored).
Exit: 0 gate pass · 1 gate fail · 2 error.
"""
import argparse
import glob
import json
import os
import re
import sys


def die(msg):
    print(f"[trigger-evals] ERROR: {msg}", file=sys.stderr)
    sys.exit(2)


def load_descriptions(repo):
    descs = []
    for p in sorted(glob.glob(os.path.join(repo, "skills", "*", "SKILL.md"))):
        name = os.path.basename(os.path.dirname(p))
        m = re.match(r"^---\n(.*?)\n---", open(p, encoding="utf-8").read(), re.S)
        if not m:
            die(f"no frontmatter: {p}")
        fm = m.group(1)
        dm = re.search(r"description:\s*>-?\n((?:[ ]{2,}.*\n?)+)", fm) or re.search(
            r"description:\s*(.+)", fm)
        if not dm:
            die(f"no description: {p}")
        text = re.sub(r"\s+", " ", dm.group(1)).strip()
        descs.append({"name": name, "description": text})
    return descs


def load_cases(repo):
    cases = []
    amap_path = os.path.join(repo, "evals", "trigger-accept-map.json")
    if not os.path.exists(amap_path):
        die("evals/trigger-accept-map.json missing — write the accept map first")
    amap = json.load(open(amap_path, encoding="utf-8"))
    exclude = set(amap.get("_exclude_files", []))
    for p in sorted(glob.glob(os.path.join(repo, "evals", "*.json"))):
        base = os.path.basename(p)
        if base == "trigger-accept-map.json" or base in exclude:
            continue
        data = json.load(open(p, encoding="utf-8"))
        raw = []
        if isinstance(data, list):  # bare-list suite (e.g. trigger_evals.json)
            raw = data
        elif isinstance(data, dict):
            for key in ("cases", "should_trigger", "near_misses"):
                if isinstance(data.get(key), list):
                    raw.extend(data[key])
        for c in raw:
            cid = f"{base}::{c.get('id')}"
            prompt = c.get("prompt") or c.get("query")
            if not prompt:
                continue  # behavioral-only entries without prompts
            if cid not in amap:
                print(f"[trigger-evals] WARN unmapped case skipped: {cid}")
                continue
            cases.append({"id": cid, "prompt": prompt, **amap[cid]})
    if not cases:
        die("no mapped cases found")
    return cases


def cmd_manifest(args):
    descs = load_descriptions(args.repo)
    cases = load_cases(args.repo)
    os.makedirs(os.path.join(args.out, "private"), exist_ok=True)
    # scoring key lives in private/ — judges are pointed at out/ manifests only
    json.dump(cases, open(os.path.join(args.out, "private", "key.json"), "w"),
              indent=1)
    batches = [cases[i:i + args.batch] for i in range(0, len(cases), args.batch)]
    for n, b in enumerate(batches, 1):
        json.dump(
            {"skills": descs,
             "queries": [{"id": c["id"], "prompt": c["prompt"]} for c in b]},
            open(os.path.join(args.out, f"manifest-{n}.json"), "w"), indent=1)
    print(f"[trigger-evals] {len(cases)} cases → {len(batches)} manifests in {args.out}"
          f" · {len(descs)} skill descriptions")
    sys.exit(0)


def cmd_score(args):
    key = {c["id"]: c for c in
           json.load(open(os.path.join(args.out, "private", "key.json")))}
    picks = {}
    for line in open(args.picks, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        j = json.loads(line)
        picks[j["id"]] = (j.get("pick") or "none").strip().lower()
    fire_total = fire_ok = nofire_total = nofire_ok = 0
    failures = []
    for cid, c in key.items():
        if cid not in picks:
            failures.append({"id": cid, "why": "NO JUDGMENT RETURNED"})
            continue
        pick = picks[cid]
        accept = [a.lower() for a in c["accept"]]
        ok = pick in accept
        if c["kind"] == "fire":
            fire_total += 1
            fire_ok += ok
        else:
            nofire_total += 1
            nofire_ok += ok
        if not ok:
            failures.append({"id": cid, "pick": pick, "accept": c["accept"],
                             "kind": c["kind"], "prompt": key[cid]["prompt"]})
    fire_rate = fire_ok / fire_total if fire_total else 0.0
    false_fire = 1 - (nofire_ok / nofire_total) if nofire_total else 0.0
    gate = fire_rate >= 0.95 and false_fire <= 0.05
    report = {"fire_total": fire_total, "fire_ok": fire_ok,
              "fire_rate": round(fire_rate, 4),
              "nofire_total": nofire_total, "nofire_ok": nofire_ok,
              "false_fire_rate": round(false_fire, 4),
              "gate_95_5": "PASS" if gate else "FAIL",
              "failures": failures}
    out = os.path.join(args.out, "baseline-report.json")
    json.dump(report, open(out, "w"), indent=1)
    print(f"[trigger-evals] fire {fire_ok}/{fire_total} ({fire_rate:.1%}) · "
          f"false-fire {false_fire:.1%} · GATE(≥95/≤5): {report['gate_95_5']} · "
          f"failures: {len(failures)} → {out}")
    sys.exit(0 if gate else 1)


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    m = sp.add_parser("manifest")
    m.add_argument("--repo", default=".")
    m.add_argument("--out", required=True)
    m.add_argument("--batch", type=int, default=12)
    s = sp.add_parser("score")
    s.add_argument("--out", required=True)
    s.add_argument("--picks", required=True)
    args = ap.parse_args()
    {"manifest": cmd_manifest, "score": cmd_score}[args.cmd](args)


if __name__ == "__main__":
    main()
