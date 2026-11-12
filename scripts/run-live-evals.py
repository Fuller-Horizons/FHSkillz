#!/usr/bin/env python3
"""run-live-evals.py — live, blind A/B eval runner for FHSkillz (old vs new plugin).

Subcommands:
  run         execute every case x version(old/new) x model through `claude -p`
              in a fresh temp workspace; store raw stream-json, extract the
              result text to blind-labeled files (A/B), record run metadata.
  grade-pack  bundle prompts + assertions + blind A/B outputs per skill for a
              grader agent (no version info anywhere in the pack).
  score       join grader verdicts with the private key; per skill x version x
              model pass rates, disagreements, and a KEEP/REVERT verdict.

Env: FHSKILLZ_CLAUDE_BIN (default "claude"; may contain args, shlex-split).
Stdlib only, Python 3.8+. Exit: 0 ok - 2 error.
"""
import argparse
import json
import os
import random
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

VERSIONS = ("old", "new")
LABELS = ("A", "B")


def die(msg):
    print(f"[live-evals] ERROR: {msg}", file=sys.stderr)
    sys.exit(2)


def safe(s):
    return re.sub(r"[^A-Za-z0-9._-]+", "_", str(s))


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
        f.write("\n")


def read_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------- loading

def load_cases(paths, skills=None, max_per_skill=None):
    cases, seen, per_skill = [], set(), {}
    for p in paths:
        data = read_json(p)
        if data is None:
            die(f"cases file not found: {p}")
        for c in data.get("cases", []):
            for k in ("id", "skill", "prompt", "assertions"):
                if k not in c:
                    die(f"{p}: case missing '{k}': {c.get('id', '?')}")
            if c["id"] in seen:
                die(f"duplicate case id: {c['id']}")
            seen.add(c["id"])
            if skills and c["skill"] not in skills:
                continue
            n = per_skill.get(c["skill"], 0)
            if max_per_skill is not None and n >= max_per_skill:
                continue
            per_skill[c["skill"]] = n + 1
            cases.append({k: c[k] for k in ("id", "skill", "prompt", "assertions")})
    return cases


def check_plugin(path, label):
    if not os.path.isfile(os.path.join(path, ".claude-plugin", "plugin.json")):
        die(f"--{label} {path}: no .claude-plugin/plugin.json")


def claude_cmd():
    return shlex.split(os.environ.get("FHSKILLZ_CLAUDE_BIN", "claude"))


# ---------------------------------------------------------------- blind key

def assign_labels(case_id, seed):
    """Seeded per-case mapping label -> version."""
    order = list(VERSIONS)
    random.Random(f"{seed}:{case_id}").shuffle(order)
    return dict(zip(LABELS, order))


def load_key(out):
    return read_json(os.path.join(out, "private", "key.json"), {})


def ensure_key(out, cases, seed):
    key = load_key(out)
    for c in cases:
        if c["id"] not in key:  # never re-roll an existing mapping (resume safety)
            key[c["id"]] = assign_labels(c["id"], seed)
    write_json(os.path.join(out, "private", "key.json"), key)
    return key


# ---------------------------------------------------------------- stream parse

def parse_stream(text):
    """Parse stream-json lines -> dict(result, cost, turns, duration_ms, is_error,
    skills, tools, has_result)."""
    info = {"result": None, "cost": None, "turns": None, "duration_ms": None,
            "is_error": None, "skills": [], "tools": [], "has_result": False}
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        t = ev.get("type")
        if t == "assistant":
            content = (ev.get("message") or {}).get("content") or []
            if isinstance(content, list):
                for b in content:
                    if isinstance(b, dict) and b.get("type") == "tool_use":
                        name = b.get("name", "")
                        info["tools"].append(name)
                        if name == "Skill":
                            inp = b.get("input") or {}
                            sk = inp.get("skill") or inp.get("command")
                            if sk:
                                info["skills"].append(sk)
        elif t == "result":
            info["has_result"] = True
            info["result"] = ev.get("result") if isinstance(ev.get("result"), str) else ""
            info["cost"] = ev.get("total_cost_usd")
            info["turns"] = ev.get("num_turns")
            info["duration_ms"] = ev.get("duration_ms")
            info["is_error"] = bool(ev.get("is_error"))
    return info


def raw_has_result(path):
    if not os.path.exists(path):
        return False
    with open(path, encoding="utf-8", errors="replace") as f:
        info = parse_stream(f.read())
    # an errored result (usage limit, API error) is not a finished run: re-run it on resume
    return info["has_result"] and not info["is_error"]


# ---------------------------------------------------------------- run

def run_id(case, model, version):
    return f"{safe(case['id'])}__{safe(model)}__{version}"


def plan_runs(cases, models, dirs):
    return [{"case": c, "model": m, "version": v, "dir": dirs[v]}
            for c in cases for m in models for v in VERSIONS]


def execute_one(job, args, key, lock, done_ids):
    c, model, version = job["case"], job["model"], job["version"]
    rid = run_id(c, model, version)
    raw_path = os.path.join(args.out, "raw", rid + ".jsonl")
    label = next(l for l, v in key[c["id"]].items() if v == version)
    resumed = raw_has_result(raw_path)
    timed_out = False
    if not resumed:
        cmd = claude_cmd() + [
            "-p", (f"/{args.force_skill_prefix}:{c['skill']} " if args.force_skill_prefix else "") + c["prompt"],
            "--model", model,
            *(["--effort", args.effort] if getattr(args, "effort", None) else []),
            "--setting-sources", "project",
            "--plugin-dir", os.path.abspath(job["dir"]),
            "--output-format", "stream-json", "--verbose",
            "--allowedTools", args.allowed_tools]
        ws = tempfile.mkdtemp(prefix="fhlive-")
        out_text = ""
        try:
            try:
                p = subprocess.run(cmd, cwd=ws, capture_output=True, text=True,
                                   timeout=args.timeout, stdin=subprocess.DEVNULL)
                out_text = p.stdout or ""
            except subprocess.TimeoutExpired as e:
                timed_out = True
                so = e.stdout
                out_text = so.decode("utf-8", "replace") if isinstance(so, bytes) else (so or "")
            except OSError as e:
                out_text = ""
                print(f"[live-evals] cannot exec claude: {e}", file=sys.stderr)
        finally:
            shutil.rmtree(ws, ignore_errors=True)
        os.makedirs(os.path.dirname(raw_path), exist_ok=True)
        with open(raw_path, "w", encoding="utf-8") as f:
            f.write(out_text)
    with open(raw_path, encoding="utf-8", errors="replace") as f:
        info = parse_stream(f.read())
    if info["has_result"]:
        odir = os.path.join(args.out, "outputs", c["id"], safe(model))
        os.makedirs(odir, exist_ok=True)
        with open(os.path.join(odir, label + ".md"), "w", encoding="utf-8") as f:
            f.write(info["result"] or "")
    rec = {"run_id": rid, "case": c["id"], "skill": c["skill"], "model": model,
           "label": label, "version": version, "cost": info["cost"],
           "turns": info["turns"], "duration_ms": info["duration_ms"],
           "is_error": True if (timed_out or not info["has_result"]) else info["is_error"],
           "timed_out": timed_out, "resumed": resumed,
           "skills_invoked": info["skills"], "tools": sorted(set(info["tools"]))}
    with lock:
        if not (resumed and rid in done_ids):
            with open(os.path.join(args.out, "runs.jsonl"), "a", encoding="utf-8") as f:
                f.write(json.dumps(rec) + "\n")
            if info["has_result"]:
                done_ids.add(rid)
    return rec


def cmd_run(args):
    check_plugin(args.old, "old")
    check_plugin(args.new, "new")
    models = [m.strip() for m in args.models.split(",") if m.strip()]
    skills = set(s.strip() for s in args.skills.split(",")) if args.skills else None
    cases = load_cases(args.cases, skills, args.max_cases_per_skill)
    if not cases:
        die("no cases selected")
    jobs = plan_runs(cases, models, {"old": args.old, "new": args.new})
    if args.dry_run:
        print(f"[live-evals] DRY RUN - {len(cases)} cases x {len(VERSIONS)} versions "
              f"x {len(models)} models = {len(jobs)} runs (no claude calls)")
        print(f"  old={args.old}\n  new={args.new}\n  out={args.out}  jobs={args.jobs} "
              f"timeout={args.timeout}s seed={args.seed}")
        for j in jobs:
            print(f"  {run_id(j['case'], j['model'], j['version'])}  "
                  f"skill={j['case']['skill']}")
        print(f"[live-evals] planned runs: {len(jobs)}")
        return 0
    os.makedirs(os.path.join(args.out, "raw"), exist_ok=True)
    write_json(os.path.join(args.out, "cases.json"), {"cases": cases})
    key = ensure_key(args.out, cases, args.seed)
    done_ids = set()
    rp = os.path.join(args.out, "runs.jsonl")
    if os.path.exists(rp):
        with open(rp, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if not r.get("is_error"):
                    done_ids.add(r.get("run_id"))
    lock = threading.Lock()
    errs = 0
    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as ex:
        futs = [ex.submit(execute_one, j, args, key, lock, done_ids) for j in jobs]
        for fu in as_completed(futs):
            r = fu.result()
            errs += 1 if r["is_error"] else 0
            tag = "resumed" if r["resumed"] else ("ERROR" if r["is_error"] else "ok")
            print(f"[live-evals] {r['run_id']}: {tag}")
    print(f"[live-evals] done: {len(jobs)} runs, {errs} errors -> {args.out}")
    return 0


# ---------------------------------------------------------------- grade-pack

def cmd_grade_pack(args):
    cases = (read_json(os.path.join(args.out, "cases.json"), {}) or {}).get("cases")
    if not cases:
        die("no cases.json in --out (run `run` first)")
    by_skill = {}
    for c in cases:
        models = {}
        cdir = os.path.join(args.out, "outputs", c["id"])
        if os.path.isdir(cdir):
            for m in sorted(os.listdir(cdir)):
                outs = {}
                for l in LABELS:
                    p = os.path.join(cdir, m, l + ".md")
                    if os.path.exists(p):
                        outs[l] = open(p, encoding="utf-8").read()
                if len(outs) == 2:
                    models[m] = outs
        if models:
            by_skill.setdefault(c["skill"], []).append(
                {"case": c["id"], "prompt": c["prompt"],
                 "assertions": c["assertions"], "models": models})
    for skill, items in by_skill.items():
        write_json(os.path.join(args.out, "grading", safe(skill) + ".json"),
                   {"skill": skill, "cases": items})
        print(f"[live-evals] grading/{safe(skill)}.json: {len(items)} cases")
    if not by_skill:
        print("[live-evals] nothing to pack (no complete A/B outputs)")
    return 0


# ---------------------------------------------------------------- score

def load_grades(paths):
    rows = []
    for p in paths:
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
    return rows


def score_data(key, case_skill, grades):
    """Return (per_cell, disagreements, results).
    results[(case, model, version)] = {"assertions": [bool], "pass": bool, "n_graders": n}"""
    grouped = {}
    for g in grades:
        grouped.setdefault((g["case"], g["model"], g["label"]), []).append(g)
    results, disagreements = {}, []
    for (case, model, label), gs in grouped.items():
        if case not in key:
            continue
        version = key[case][label]
        lens = {len(g["assertion_results"]) for g in gs}
        n = max(lens)
        # assertion passes only if every grader says true
        merged = [all(len(g["assertion_results"]) > i and bool(g["assertion_results"][i])
                      for g in gs) for i in range(n)]
        per_grader_pass = [len(g["assertion_results"]) > 0 and all(g["assertion_results"])
                           for g in gs]
        differ = [i for i in range(n)
                  if len({bool(g["assertion_results"][i]) if i < len(g["assertion_results"])
                          else None for g in gs}) > 1]
        agree = len(set(per_grader_pass)) == 1
        if differ or not agree or len(lens) > 1:
            disagreements.append({"case": case, "model": model, "label": label,
                                  "version": version, "assertion_indexes": differ,
                                  "graders": [g.get("grader") for g in gs],
                                  "case_pass_by_grader": per_grader_pass})
        results[(case, model, version)] = {
            "assertions": merged,
            "pass": bool(merged) and all(merged) and agree and all(per_grader_pass),
            "n_graders": len(gs)}
    return results, disagreements


def cmd_score(args):
    key = load_key(args.out)
    if not key:
        die("no private/key.json in --out")
    runs = []
    rp = os.path.join(args.out, "runs.jsonl")
    if os.path.exists(rp):
        runs = [json.loads(l) for l in open(rp, encoding="utf-8") if l.strip()]
    case_skill = {r["case"]: r["skill"] for r in runs}
    cases = (read_json(os.path.join(args.out, "cases.json"), {}) or {}).get("cases", [])
    case_skill.update({c["id"]: c["skill"] for c in cases})
    results, disagreements = score_data(key, case_skill, load_grades(args.grades))

    cells = {}  # (skill, version, model) -> stats
    for (case, model, version), r in results.items():
        skill = case_skill.get(case, "?")
        c = cells.setdefault((skill, version, model),
                             {"cases": 0, "case_pass": 0, "assert_total": 0, "assert_pass": 0})
        c["cases"] += 1
        c["case_pass"] += 1 if r["pass"] else 0
        c["assert_total"] += len(r["assertions"])
        c["assert_pass"] += sum(r["assertions"])

    def rate(a, b):
        return round(a / b, 4) if b else None

    table = {}
    for (skill, version, model), c in sorted(cells.items()):
        table.setdefault(skill, {}).setdefault(version, {})[model] = {
            "cases": c["cases"], "case_pass_rate": rate(c["case_pass"], c["cases"]),
            "assertion_pass_rate": rate(c["assert_pass"], c["assert_total"])}

    verdicts = {}
    for skill in sorted({k[0] for k in cells}):
        tot = {v: [0, 0] for v in VERSIONS}
        for (s, v, m), c in cells.items():
            if s == skill:
                tot[v][0] += c["case_pass"]
                tot[v][1] += c["cases"]
        old_r, new_r = rate(*tot["old"]), rate(*tot["new"])
        # assertion regressions: index where new fails but old passes, counted by distinct case
        reg = {}
        for (case, model, version), r in results.items():
            if version != "new" or case_skill.get(case) != skill:
                continue
            o = results.get((case, model, "old"))
            if not o:
                continue
            for i, ok in enumerate(r["assertions"]):
                if not ok and i < len(o["assertions"]) and o["assertions"][i]:
                    reg.setdefault(i, set()).add(case)
        regressions = {str(i): sorted(cs) for i, cs in sorted(reg.items())}
        blocking = [i for i, cs in regressions.items() if len(cs) >= 2]
        better = old_r is not None and new_r is not None and new_r > old_r
        verdicts[skill] = {"verdict": "KEEP" if (better and not blocking) else "REVERT",
                           "old_case_pass_rate": old_r, "new_case_pass_rate": new_r,
                           "assertion_regressions": regressions,
                           "blocking_assertion_indexes": blocking}
    summary = {"table": table, "verdicts": verdicts,
               "disagreements": disagreements,
               "graded_outputs": len(results)}
    write_json(os.path.join(args.out, "summary.json"), summary)

    print(f"{'skill':<26}{'ver':<5}{'model':<9}{'cases':>6}{'case%':>8}{'assert%':>9}")
    for skill, vs in table.items():
        for v in VERSIONS:
            for m, s in sorted(vs.get(v, {}).items()):
                cp = "-" if s["case_pass_rate"] is None else f"{s['case_pass_rate']*100:.0f}"
                ap = "-" if s["assertion_pass_rate"] is None else f"{s['assertion_pass_rate']*100:.0f}"
                print(f"{skill:<26}{v:<5}{m:<9}{s['cases']:>6}{cp:>8}{ap:>9}")
    for skill, v in verdicts.items():
        extra = f" blocking assertion idx {v['blocking_assertion_indexes']}" \
            if v["blocking_assertion_indexes"] else ""
        print(f"VERDICT {skill}: {v['verdict']} (old {v['old_case_pass_rate']} -> "
              f"new {v['new_case_pass_rate']}){extra}")
    if disagreements:
        print(f"{len(disagreements)} grader disagreement(s) listed in summary.json")
    return 0


# ---------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--cases", nargs="+", required=True)
    r.add_argument("--old", required=True)
    r.add_argument("--new", required=True)
    r.add_argument("--models", default="haiku,sonnet")
    r.add_argument("--out", required=True)
    r.add_argument("--jobs", type=int, default=6)
    r.add_argument("--max-cases-per-skill", type=int, default=None)
    r.add_argument("--skills", default=None, help="comma list filter")
    r.add_argument("--allowed-tools", default="Skill,Read,Glob,Grep,WebSearch,WebFetch")
    r.add_argument("--timeout", type=int, default=600)
    r.add_argument("--effort", default=None, help="claude --effort level for every run (low|medium|high|xhigh|max)")
    r.add_argument("--seed", type=int, default=0)
    r.add_argument("--dry-run", action="store_true")
    r.add_argument("--force-skill-prefix", default=None,
                   help="FORCED arm: prefix each prompt with /<prefix>:<skill> so the skill "
                        "under test is always loaded (e.g. fh-skillz). Default: natural routing.")
    g = sub.add_parser("grade-pack")
    g.add_argument("--out", required=True)
    s = sub.add_parser("score")
    s.add_argument("--out", required=True)
    s.add_argument("--grades", nargs="+", required=True)
    args = ap.parse_args(argv)
    return {"run": cmd_run, "grade-pack": cmd_grade_pack, "score": cmd_score}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
