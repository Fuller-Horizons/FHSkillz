#!/usr/bin/env python3
"""Run the jail-prompt eval suites through the local authenticated `claude` CLI.

Triggering  : `claude` acts as an independent router-judge per query, deciding
              TRIGGER / NO from the skill's description alone, scored vs the
              labels in evals/trigger_evals.json.
Behavioral  : `claude` runs the skill on each prompt (SKILL.md supplied), then a
              second, independent `claude` call grades the response PASS/FAIL
              against the case's expected_output.

This is the closest reproducible harness to the production trigger mechanism that
works from a plain logged-in CLI. Results are written to evals/last-run.md.

Usage:
  python3 scripts/run_evals.py [--suite trigger|behavioral|all] [--model ID]
                               [--limit N] [--runs K]
  --runs K  repeat the behavioral suite K times to measure variance.
"""
import argparse
import datetime
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_PATH = os.path.join(ROOT, "skills", "jail-prompt", "SKILL.md")
TRIGGER_PATH = os.path.join(ROOT, "evals", "trigger_evals.json")
BEHAVIORAL_PATH = os.path.join(ROOT, "evals", "evals.json")
OUT_PATH = os.path.join(ROOT, "evals", "last-run.md")


def claude(prompt, model=None, timeout=180):
    cmd = ["claude", "-p", prompt, "--output-format", "text"]
    if model:
        cmd += ["--model", model]
    try:
        r = subprocess.run(
            cmd, capture_output=True, text=True,
            timeout=timeout, stdin=subprocess.DEVNULL,
        )
    except subprocess.TimeoutExpired:
        return "[timeout]"
    return (r.stdout or "").strip()


def preflight(model):
    out = claude("Reply with exactly: PONG", model=model, timeout=60)
    if "PONG" not in out.upper():
        print("Preflight FAILED — the `claude` CLI does not appear logged in.")
        print("Run `claude` once interactively to log in, then retry.")
        print("CLI said: " + out[:200])
        sys.exit(2)


def skill_description():
    for line in open(SKILL_PATH, encoding="utf-8").read().splitlines():
        if line.startswith("description:"):
            return line[len("description:"):].strip()
    return ""


def run_trigger(model, limit):
    desc = skill_description()
    cases = json.load(open(TRIGGER_PATH, encoding="utf-8"))
    if limit:
        cases = cases[:limit]
    rows, correct = [], 0
    for c in cases:
        prompt = (
            "You are a router deciding whether a Claude skill should activate. "
            "Decide ONLY from the description and the query.\n\n"
            "Skill description (the only activation signal):\n"
            '"""' + desc + '"""\n\n'
            'User query:\n"""' + c["query"] + '"""\n\n'
            "Answer with exactly one word on the first line: TRIGGER or NO."
        )
        out = claude(prompt, model=model).upper()
        verdict = "TRIGGER" if out.startswith("TRIGGER") else ("NO" if out.startswith("NO") else "?")
        expected = "TRIGGER" if c["should_trigger"] else "NO"
        ok = verdict == expected
        correct += ok
        rows.append((c["id"], expected, verdict, ok))
        print("  trig %2s: expected %-7s got %-7s %s" % (c["id"], expected, verdict, "ok" if ok else "MISS"))
    return rows, correct, len(cases)


def run_behavioral(model, limit):
    skill = open(SKILL_PATH, encoding="utf-8").read()
    cases = json.load(open(BEHAVIORAL_PATH, encoding="utf-8"))["evals"]
    if limit:
        cases = cases[:limit]
    rows, passes = [], 0
    for c in cases:
        exec_prompt = (
            "You are Claude with the jail-prompt skill ACTIVE. Follow this SKILL.md "
            "exactly to respond to the user. Be realistic and concise.\n\n"
            "<SKILL.md>\n" + skill + "\n</SKILL.md>\n\n"
            'User: """' + c["prompt"] + '"""'
        )
        resp = claude(exec_prompt, model=model, timeout=240)
        grade_prompt = (
            "You are a harsh, fair, INDEPENDENT grader. Score the response against the "
            "expected behavior. First line: exactly PASS or FAIL. Then one line why.\n\n"
            "EXPECTED BEHAVIOR: " + c["expected_output"] + "\n\n"
            'RESPONSE:\n"""' + resp[:6000] + '"""'
        )
        g = claude(grade_prompt, model=model).upper()
        verdict = "PASS" if g.startswith("PASS") else "FAIL"
        passes += verdict == "PASS"
        rows.append((c["id"], c["name"], verdict))
        print("  beh %2s %-30s: %s" % (c["id"], c["name"], verdict))
    return rows, passes, len(cases)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", choices=["trigger", "behavioral", "all"], default="all")
    ap.add_argument("--model", default=None, help="model id (default: CLI default)")
    ap.add_argument("--limit", type=int, default=0, help="cap cases per suite (0=all)")
    ap.add_argument("--runs", type=int, default=1, help="repeat behavioral suite K times for variance")
    a = ap.parse_args()
    limit = a.limit or None

    print("Preflight: checking `claude` CLI auth ...")
    preflight(a.model)
    print("OK.\n")

    report = ["# jail-prompt eval run — " + datetime.datetime.now().isoformat(timespec="seconds"),
              "Method: claude-CLI router-judge (triggering) + execute-then-independently-grade (behavioral).", ""]

    if a.suite in ("trigger", "all"):
        print("Triggering (router-judge vs labels):")
        rows, correct, total = run_trigger(a.model, limit)
        print("  => %d/%d correct\n" % (correct, total))
        report.append("## Triggering: %d/%d" % (correct, total))
        for i, e, v, ok in rows:
            report.append("- %s: expected %s, got %s %s" % (i, e, v, "ok" if ok else "MISS"))
        report.append("")

    if a.suite in ("behavioral", "all"):
        for run in range(1, a.runs + 1):
            tag = "" if a.runs == 1 else (" (run %d/%d)" % (run, a.runs))
            print("Behavioral%s (execute skill, independent grade):" % tag)
            rows, passes, total = run_behavioral(a.model, limit)
            print("  => %d/%d PASS\n" % (passes, total))
            report.append("## Behavioral%s: %d/%d PASS" % (tag, passes, total))
            for i, n, v in rows:
                report.append("- %s %s: %s" % (i, n, v))
            report.append("")

    open(OUT_PATH, "w", encoding="utf-8").write("\n".join(report) + "\n")
    print("Wrote " + OUT_PATH)


if __name__ == "__main__":
    main()
