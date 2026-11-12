#!/usr/bin/env python3
"""Stand-in for `claude -p ... --output-format json` used by test_select_models.
Candidate runs return '<model> answer'; grader runs pass every check for
outputs from models listed in FAKE_PASS (comma list), fail the rest."""
import json, os, re, sys
args = sys.argv[1:]
prompt = args[args.index("-p") + 1]
model = args[args.index("--model") + 1]
if "You grade AI outputs" in prompt:
    n = len(re.findall(r"(?m)^\d+\. ", prompt.split("<checks>")[1].split("</checks>")[0]))
    passing = [m for m in os.environ.get("FAKE_PASS", "").split(",") if m]
    res = {}
    for lab, body in re.findall(r'<output label="(\w)">\n(.*?)\n</output>', prompt, flags=re.S):
        ok = any(body.startswith(m + " ") for m in passing)
        res[lab] = [ok] * n
    print(json.dumps({"result": json.dumps(res), "total_cost_usd": 0.01, "is_error": False}))
else:
    print(json.dumps({"result": f"{model} answer", "total_cost_usd": 0.001, "is_error": False}))
