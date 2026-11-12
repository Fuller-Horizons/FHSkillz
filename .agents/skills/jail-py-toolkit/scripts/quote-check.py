#!/usr/bin/env python3
"""quote-check.py — quote-before-claim: does each quote really appear in its source?

The strongest cheap guard against invented facts in document and research work:
every Fact claim carries a short verbatim quote and the id of the source it
came from; this script confirms the quote is actually in that source's text.
It never judges whether the claim follows from the quote (the model checker
does that); it proves the quote isn't made up.

Claims file: JSON array or JSONL of objects
  {"id": "c1", "claim": "...", "label": "Fact", "quote": "...", "source": "s1"}
  (`label` defaults to Fact; Inference/Estimate/Judgment/Unknown need no quote)
Sources: `--sources DIR` (file stem = source id, e.g. s1.txt / s1.md / s1.html)
  and/or `--source ID=FILE` (repeatable). Save fetched pages to files first
  (jail-prompt's fetch-once rule) so every agent and this check read the same copy.

Matching ignores case, whitespace runs, curly vs straight quotes, dash and
hyphen variants, HTML tags and HTML entities; nothing else. A quote of 3 words or fewer is too short
to prove anything; over 40 words is warned (keep quotes to 25 words or fewer).

Usage:  quote-check.py --claims claims.json --sources sources/ [--source s9=page.txt] [--strict]
Exit codes: 0 = every Fact quote found, 1 = missing/unmatched quotes, 2 = usage/IO error.
Never prints source text beyond the claim's own quote. Stdlib only.
"""
import argparse, html, json, os, re, sys

NEEDS_QUOTE = {"fact"}
TAG = re.compile(r"<[^>]+>")


def norm(t):
    t = html.unescape(TAG.sub(" ", t or ""))
    t = (t.replace("\u2010", "-").replace("\u2011", "-").replace("\u2012", "-").replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
          .replace("–", "-").replace("—", "-").replace(" ", " "))
    return re.sub(r"\s+", " ", t).strip().lower()


def load_claims(path):
    raw = open(path, encoding="utf-8").read().strip()
    if raw.startswith("["):
        return json.loads(raw)
    return [json.loads(l) for l in raw.splitlines() if l.strip()]


def load_sources(src_dir, pairs):
    out = {}
    if src_dir:
        for f in sorted(os.listdir(src_dir)):
            fp = os.path.join(src_dir, f)
            if os.path.isfile(fp):
                out[os.path.splitext(f)[0]] = norm(open(fp, encoding="utf-8", errors="replace").read())
    for p in pairs or []:
        sid, _, fp = p.partition("=")
        if not fp:
            raise ValueError(f"--source must be ID=FILE, got {p!r}")
        out[sid] = norm(open(fp, encoding="utf-8", errors="replace").read())
    return out


def check(claims, sources):
    errors, warnings = [], []
    for i, c in enumerate(claims, 1):
        cid = str(c.get("id") or f"#{i}")
        label = str(c.get("label") or "Fact").strip().lower()
        quote, sid = c.get("quote"), c.get("source")
        if label not in NEEDS_QUOTE:
            if quote and sid in sources and norm(quote) not in sources[sid]:
                errors.append(f"{cid}: quote not found in source {sid!r} (label {label})")
            continue
        if not quote:
            errors.append(f"{cid}: Fact with no quote (add a verbatim quote, or relabel Inference/Unknown)")
            continue
        if not sid:
            errors.append(f"{cid}: Fact quote has no source id")
            continue
        if sid not in sources:
            errors.append(f"{cid}: source {sid!r} not provided (save it to the sources folder)")
            continue
        words = len(norm(quote).split())
        if words <= 3:
            errors.append(f"{cid}: quote too short to prove the claim ({words} words)")
            continue
        if words > 40:
            warnings.append(f"{cid}: quote is {words} words; keep quotes to 25 words or fewer")
        if norm(quote) not in sources[sid]:
            errors.append(f"{cid}: quote NOT FOUND in source {sid!r}: \"{quote[:80]}\"")
    return errors, warnings


def main():
    ap = argparse.ArgumentParser(description="Verify quote-before-claim: every Fact quote appears in its source.")
    ap.add_argument("--claims", required=True)
    ap.add_argument("--sources", default=None, help="directory of source texts (file stem = source id)")
    ap.add_argument("--source", action="append", default=[], help="ID=FILE (repeatable)")
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    a = ap.parse_args()
    if not a.sources and not a.source:
        print("error: give --sources DIR and/or --source ID=FILE", file=sys.stderr)
        return 2
    try:
        claims = load_claims(a.claims)
        sources = load_sources(a.sources, a.source)
    except (OSError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    if not isinstance(claims, list):
        print("error: claims must be a JSON array or JSONL", file=sys.stderr)
        return 2
    errors, warnings = check(claims, sources)
    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    n_fact = sum(1 for c in claims if str(c.get("label") or "Fact").lower() in NEEDS_QUOTE)
    if errors or (a.strict and warnings):
        print(f"quote-check: FAIL ({len(errors)} error(s), {len(warnings)} warning(s); {n_fact} Fact claim(s)).",
              file=sys.stderr)
        return 1
    print(f"quote-check: PASS ({n_fact} Fact claim(s) verified, {len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
