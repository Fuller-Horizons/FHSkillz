#!/usr/bin/env python3
"""run-e2e-prompt-evals.py: does jail-prompt make the FINAL output better?

For each case (a task + its input data) and each final-run model:
  old arm ("raw"):  the user's plain request + inputs, sent straight to Claude.
  new arm ("jp"):   stage 1 asks jail-prompt (the plugin at --plugin) for an
                    engineered prompt for the task; stage 2 runs that prompt
                    + the same inputs on the same final model and settings.
Outputs land as outputs/<case>/<model>/<A|B>.md with a blind key in
private/key.json, so `run-live-evals.py grade-pack` and `score` grade them
exactly like the skill A/B runs (old = raw request, new = jail-prompt).

Usage:
  run-e2e-prompt-evals.py --cases FILE --plugin DIR --out DIR
      [--models sonnet,haiku] [--effort medium] [--jp-model claude-opus-5-5]
      [--jp-effort medium] [--jobs 3] [--timeout 900] [--seed 0]
Resume-safe: finished stages are reused; errored stages re-run.
Infrastructure (repo tooling), not skill content. Stdlib only.
"""
import argparse, importlib.util, json, os, re, subprocess, tempfile, shutil, threading
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("rle", os.path.join(HERE, "run-live-evals.py"))
rle = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rle)

STAGE1 = ("/{prefix}:jail-prompt {task}\n\n"
          "The data for this task will be supplied when the prompt runs, after the prompt, "
          "wrapped in <input> tags. What it looks like: {input_desc}\n"
          "Use the Instant lane: ask no questions, state assumptions. Return the engineered "
          "prompt as ONE fenced code block that I can run as-is.")


def call(prompt, model, effort, plugin, timeout, raw_path, tools):
    """Run claude -p once (or reuse a finished raw stream) -> parse_stream info."""
    if not rle.raw_has_result(raw_path):
        cmd = rle.claude_cmd() + ["-p", prompt, "--model", model,
                                  "--setting-sources", "project",
                                  "--output-format", "stream-json", "--verbose",
                                  "--allowedTools", tools]
        if effort:
            cmd += ["--effort", effort]
        if plugin:
            cmd += ["--plugin-dir", os.path.abspath(plugin)]
        ws = tempfile.mkdtemp(prefix="fhe2e-")
        try:
            try:
                p = subprocess.run(cmd, cwd=ws, capture_output=True, text=True,
                                   timeout=timeout, stdin=subprocess.DEVNULL)
                out = p.stdout or ""
            except subprocess.TimeoutExpired as e:
                so = e.stdout
                out = so.decode("utf-8", "replace") if isinstance(so, bytes) else (so or "")
        finally:
            shutil.rmtree(ws, ignore_errors=True)
        os.makedirs(os.path.dirname(raw_path), exist_ok=True)
        with open(raw_path, "w", encoding="utf-8") as f:
            f.write(out)
    with open(raw_path, encoding="utf-8", errors="replace") as f:
        return rle.parse_stream(f.read())


def extract_block(text):
    """Largest fenced code block in the jail-prompt reply (the engineered prompt)."""
    blocks = re.findall(r"```[a-zA-Z]*\n(.*?)```", text or "", flags=re.S)
    blocks = [b for b in blocks if "JAIL-HANDOFF" not in b[:40]]
    return max(blocks, key=len).strip() if blocks else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", required=True)
    ap.add_argument("--plugin", required=True, help="plugin dir holding jail-prompt")
    ap.add_argument("--out", required=True)
    ap.add_argument("--models", default="sonnet,haiku", help="final-run models")
    ap.add_argument("--effort", default="medium", help="final-run effort")
    ap.add_argument("--jp-model", default="claude-opus-5-5")
    ap.add_argument("--jp-effort", default="medium")
    ap.add_argument("--prefix", default="fh-skillz")
    ap.add_argument("--tools", default="Skill,Read,Glob,Grep,WebSearch,WebFetch")
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()

    cases = rle.read_json(a.cases, {})["cases"]
    os.makedirs(a.out, exist_ok=True)
    rle.write_json(os.path.join(a.out, "cases.json"),
                   {"cases": [{"id": c["id"], "skill": c["skill"], "assertions": c["assertions"],
                               "prompt": c["task"] + "\n\n<input>\n" + c["inputs"] + "\n</input>"}
                              for c in cases]})
    key = rle.ensure_key(a.out, cases, a.seed)
    models = [m.strip() for m in a.models.split(",") if m.strip()]
    lock = threading.Lock()
    runs_path = os.path.join(a.out, "runs.jsonl")

    def one(job):
        c, model, arm = job
        raw = lambda tag: os.path.join(a.out, "raw", f"{c['id']}__{model}__{tag}.jsonl")
        inputs = "<input>\n" + c["inputs"] + "\n</input>"
        rec = {"case": c["id"], "skill": c["skill"], "model": model,
               "version": "old" if arm == "raw" else "new"}
        cost = 0.0
        if arm == "raw":
            info = call(c["task"] + "\n\n" + inputs, model, a.effort, None, a.timeout,
                        raw("raw"), a.tools)
        else:
            s1 = call(STAGE1.format(prefix=a.prefix, task=c["task"], input_desc=c["input_desc"]),
                      a.jp_model, a.jp_effort, a.plugin, a.timeout, raw(f"jp1-{model}"), a.tools)
            cost += s1["cost"] or 0
            block = extract_block(s1["result"]) if s1["has_result"] and not s1["is_error"] else None
            rec["prompt_extracted"] = bool(block)
            if block:
                pdir = os.path.join(a.out, "prompts")
                os.makedirs(pdir, exist_ok=True)
                with open(os.path.join(pdir, f"{c['id']}__{model}.md"), "w", encoding="utf-8") as f:
                    f.write(block)
                info = call(block + "\n\n" + inputs, model, a.effort, None, a.timeout,
                            raw("jp2"), a.tools)
            else:
                info = {"has_result": False, "is_error": True, "result": None, "cost": 0,
                        "duration_ms": None, "turns": None}
        cost += info.get("cost") or 0
        label = next(l for l, v in key[c["id"]].items() if v == rec["version"])
        if info["has_result"]:
            od = os.path.join(a.out, "outputs", c["id"], rle.safe(model))
            os.makedirs(od, exist_ok=True)
            with open(os.path.join(od, label + ".md"), "w", encoding="utf-8") as f:
                f.write(info["result"] or "")
        rec.update({"run_id": f"{c['id']}__{model}__{rec['version']}", "label": label,
                    "cost": round(cost, 5), "is_error": (not info["has_result"]) or bool(info["is_error"])})
        with lock:
            with open(runs_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(rec) + "\n")
        print(f"[e2e] {rec['run_id']}: {'ERROR' if rec['is_error'] else 'ok'} ${rec['cost']}", flush=True)
        return rec

    jobs = [(c, m, arm) for c in cases for m in models for arm in ("raw", "jp")]
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        recs = list(ex.map(one, jobs))
    errs = sum(r["is_error"] for r in recs)
    print(f"[e2e] done: {len(recs)} runs, {errs} errors, ${sum(r['cost'] for r in recs):.2f} -> {a.out}")


if __name__ == "__main__":
    main()
