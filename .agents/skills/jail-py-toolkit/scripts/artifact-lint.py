#!/usr/bin/env python3
"""artifact-lint.py — check a single-file HTML review page (jail-prototype).

A review page is a throwaway prototype a person can point at: it must render
the same anywhere (double-click, Claude artifact, lavish-axi), mark itself as
a prototype, and carry the review hooks the SPIKE VERDICT depends on.

Errors (exit 1):
  - no <title>, or title lacks "PROTOTYPE"            (--not-prototype skips)
  - no viewport meta
  - no explicit background on html / body / :root in a <style> block
  - outside requests: script/link/img/iframe/source/video/audio src or href
    starting http:, https: or //   (allow named hosts with --allow-host)
  - local asset files (relative src/href for script, stylesheet, img, ...):
    a review page is one self-contained file
  - duplicate data-review-id values
  - variants present but not exactly 3 distinct data-variant values, or not
    exactly one data-variant-switch control
  - data-question controls without a data-copy-feedback button
  - a data-revisions JSON legend that doesn't parse or lacks id/summary, or a
    data-rev value not in the legend
Warnings (exit 0 unless --strict):
  - no data-review-id points, no data-question controls, no visible
    "PROTOTYPE" text in the page body, --look given but no variants

Usage:  artifact-lint.py FILE [FILE ...] [--look] [--allow-host cdn.example.com] [--strict]
Exit codes: 0 = pass, 1 = fail, 2 = usage/IO error. Stdlib only.
Review-loop pattern adapted from lavish-axi (github.com/kunchenguid/lavish-axi, MIT, (c) 2026 Kun Chen).
"""
import argparse, json, re, sys
from html.parser import HTMLParser

ASSET_ATTRS = {("script", "src"), ("img", "src"), ("iframe", "src"), ("source", "src"),
               ("video", "src"), ("audio", "src"), ("embed", "src"), ("link", "href")}
BG = re.compile(r"(?is)(^|[},\s])(html|body|:root)\b[^{]*\{[^}]*\bbackground(-color)?\s*:")


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.in_title, self.in_style, self.in_script = "", False, False, False
        self.styles, self.body_text = [], []
        self.viewport = False
        self.assets = []          # (tag, attr, value)
        self.review_ids = []
        self.variants, self.switches, self.questions, self.copy_buttons = [], 0, 0, 0
        self.revs, self.rev_legends = [], []
        self._script_is_legend, self._legend_buf = False, []

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "title":
            self.in_title = True
        elif tag == "style":
            self.in_style = True
        elif tag == "script":
            self.in_script = True
            self._script_is_legend = "data-revisions" in a
            self._legend_buf = []
        if tag == "meta" and a.get("name", "").lower() == "viewport":
            self.viewport = True
        for (t, attr) in ASSET_ATTRS:
            if tag == t and attr in a:
                if tag == "link" and a.get("rel", "").lower() not in ("stylesheet", "icon", "preload", "modulepreload"):
                    continue
                self.assets.append((tag, attr, a[attr].strip()))
        if "data-review-id" in a:
            self.review_ids.append(a["data-review-id"].strip())
        if "data-variant" in a:
            self.variants.append(a["data-variant"].strip())
        if "data-variant-switch" in a:
            self.switches += 1
        if "data-question" in a:
            self.questions += 1
        if "data-copy-feedback" in a:
            self.copy_buttons += 1
        if "data-rev" in a:
            self.revs.append(a["data-rev"].strip())

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "style":
            self.in_style = False
        elif tag == "script":
            if self._script_is_legend:
                self.rev_legends.append("".join(self._legend_buf))
            self.in_script, self._script_is_legend = False, False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.in_style:
            self.styles.append(data)
        elif self.in_script:
            if self._script_is_legend:
                self._legend_buf.append(data)
        else:
            self.body_text.append(data)


def lint(text, look=False, allow_hosts=(), prototype=True):
    errors, warnings = [], []
    p = Page()
    p.feed(text)
    p.close()
    if not p.title.strip():
        errors.append("no <title>")
    elif prototype and "prototype" not in p.title.lower():
        errors.append('title does not mark the page as a PROTOTYPE')
    if not p.viewport:
        errors.append('no <meta name="viewport"> (page must work on a phone)')
    if not BG.search("\n".join(p.styles)):
        errors.append("no explicit background on html/body/:root (page may inherit a host's background)")
    for tag, attr, val in p.assets:
        low = val.lower()
        if low.startswith(("http:", "https:", "//")):
            host = re.sub(r"^(https?:)?//", "", low).split("/")[0]
            if host not in {h.lower() for h in allow_hosts}:
                errors.append(f"outside request: <{tag} {attr}=\"{val[:80]}\"> (inline it, or --allow-host {host})")
        elif not low.startswith(("data:", "#", "about:", "blob:")) and low:
            errors.append(f"local asset file: <{tag} {attr}=\"{val[:80]}\"> (a review page is one self-contained file)")
    dup = sorted({r for r in p.review_ids if p.review_ids.count(r) > 1})
    if dup:
        errors.append(f"duplicate data-review-id: {', '.join(dup)}")
    if not p.review_ids:
        warnings.append("no data-review-id points (reviewers can't point at blocks by number)")
    distinct = sorted(set(v for v in p.variants if v))
    if p.variants or p.switches:
        if len(distinct) != 3:
            errors.append(f"variants: found {len(distinct)} distinct data-variant values {distinct}; look questions need exactly 3")
        if p.switches != 1:
            errors.append(f"variants: found {p.switches} data-variant-switch controls; need exactly 1")
    elif look:
        warnings.append("--look given but no data-variant sections")
    if p.questions and not p.copy_buttons:
        errors.append("answer controls (data-question) but no data-copy-feedback button")
    if not p.questions:
        warnings.append("no data-question answer controls (the verdict has no structured reviewer input)")
    legend_ids = set()
    for raw in p.rev_legends:
        try:
            data = json.loads(raw)
            if not isinstance(data, list) or not all(isinstance(x, dict) and x.get("id") and x.get("summary") for x in data):
                raise ValueError("must be a list of {id, summary}")
            legend_ids |= {str(x["id"]) for x in data}
        except ValueError as e:
            errors.append(f"data-revisions legend invalid: {e}")
    unknown = sorted(set(r for r in p.revs if r) - legend_ids)
    if unknown:
        errors.append(f"data-rev values not in the revisions legend: {', '.join(unknown)}")
    if prototype and "prototype" not in " ".join(p.body_text).lower():
        warnings.append("no visible PROTOTYPE banner text in the page body")
    return errors, warnings


def main():
    ap = argparse.ArgumentParser(description="Check a single-file HTML review page.")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--look", action="store_true", help="look question: expect 3 variants")
    ap.add_argument("--allow-host", action="append", default=[], help="host allowed for outside requests")
    ap.add_argument("--not-prototype", action="store_true", help="skip the PROTOTYPE marking checks")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    rc = 0
    for f in a.files:
        try:
            text = open(f, encoding="utf-8").read()
        except OSError as e:
            print(f"error: cannot read {f}: {e}", file=sys.stderr)
            return 2
        errors, warnings = lint(text, a.look, a.allow_host, not a.not_prototype)
        for w in warnings:
            print(f"{f}: warning: {w}", file=sys.stderr)
        for e in errors:
            print(f"{f}: error: {e}", file=sys.stderr)
        if errors or (a.strict and warnings):
            rc = 1
            print(f"artifact-lint: {f}: FAIL ({len(errors)} error(s), {len(warnings)} warning(s))", file=sys.stderr)
        else:
            print(f"artifact-lint: {f}: PASS ({len(warnings)} warning(s))")
    return rc


if __name__ == "__main__":
    sys.exit(main())
