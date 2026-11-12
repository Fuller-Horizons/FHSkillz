#!/usr/bin/env python3
"""readability.py — Flesch-Kincaid grade check for client/owner-facing text.

Strips markdown noise (fenced code, headings markers, table rows, link URLs,
bold/italic marks, bracketed labels and citations), then computes:
  grade = 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59
and prints the grade, counts, and the longest sentences (rewrite those first).

Usage:  readability.py [--max-grade N] [--top K] [FILE ...]   (no FILE: stdin)
Exit codes: 0 = at or below --max-grade (or no limit), 1 = above it,
            2 = usage/IO error.
Manual fallback: keep sentences <= 20 words and explain or avoid jargon.
"""
import re
import sys
import argparse


def clean(text):
    out, in_code = [], False
    for line in text.splitlines():
        if re.match(r"^\s*```", line):
            in_code = not in_code
            continue
        if in_code or re.match(r"^\s*\|", line) or re.match(r"^\s*---+\s*$", line):
            continue
        line = re.sub(r"^\s*#{1,6}\s*", "", line)
        line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line)
        out.append(line)
    t = "\n".join(out)
    t = re.sub(r"\[([^\]\n]+)\]\([^)\n]*\)", r"\1", t)
    t = re.sub(r"https?://\S+", "", t)
    t = re.sub(r"\[[^\]\n]{1,40}\]", "", t)
    t = re.sub(r"[*_`]+", "", t)
    return t


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", w)))


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n\s*\n|\n", text)
    return [p.strip() for p in parts if re.search(r"[A-Za-z]", p)]


def analyze(text):
    sents = sentences(clean(text))
    counted = []
    for s in sents:
        words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'’-]*", s)
        if words:
            counted.append((s, words))
    nw = sum(len(w) for _, w in counted)
    ns = len(counted)
    if not nw or not ns:
        return None
    nsyl = sum(max(1, syllables(x)) if re.search(r"[A-Za-z]", x) else 1
               for _, w in counted for x in w)
    grade = 0.39 * nw / ns + 11.8 * nsyl / nw - 15.59
    longest = sorted(counted, key=lambda c: -len(c[1]))
    return {"grade": round(grade, 1), "words": nw, "sentences": ns,
            "longest": [(len(w), s) for s, w in longest]}


def main():
    ap = argparse.ArgumentParser(description="Flesch-Kincaid grade check.")
    ap.add_argument("files", nargs="*")
    ap.add_argument("--max-grade", type=float, default=None)
    ap.add_argument("--top", type=int, default=3)
    args = ap.parse_args()
    srcs = []
    try:
        if args.files:
            for f in args.files:
                with open(f, "r", encoding="utf-8", errors="replace") as fh:
                    srcs.append((f, fh.read()))
        else:
            srcs.append(("<stdin>", sys.stdin.read()))
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    bad = False
    for name, text in srcs:
        r = analyze(text)
        if r is None:
            print(f"readability: {name}: no sentences found", file=sys.stderr)
            return 2
        print(f"readability: {name}: grade {r['grade']} "
              f"({r['words']} words, {r['sentences']} sentences)")
        for n, s in r["longest"][:args.top]:
            print(f"  longest ({n} words): {s[:110]}")
        if args.max_grade is not None and r["grade"] > args.max_grade:
            print(f"{name}: grade {r['grade']} > max {args.max_grade}", file=sys.stderr)
            bad = True
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
