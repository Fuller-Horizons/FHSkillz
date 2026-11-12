# Review pages: HTML prototypes a person can point at

Load this for any **look/feel** question, and for logic or feasibility
questions whose answer is easier to judge on a page than in prose. A review
page is still a throwaway prototype: it answers the named question, then the
answer survives and the page is archived.

Review-loop ideas (pinpoint feedback, answer controls, revisions legend,
deliberate design direction, explicit page background, file-is-the-truth)
adapted from lavish-axi (github.com/kunchenguid/lavish-axi, MIT, © 2026 Kun
Chen), rewritten for a server-free, single-file prototype.

## 1. The file

- **One self-contained `.html` file** named `proto-<question-slug>.html` with
  `PROTOTYPE — wipe me` in the `<title>` and in a visible banner. It must
  render the same opened by double-click, in Claude's artifact view, or in
  lavish-axi: no build step, no server, no local asset files.
- **No outside requests** by default: inline CSS, inline JS, inline SVG for
  figures and icons. An external font or library only if the question needs
  it; say so in the page footer.
- **Explicit page background and text colour** on `html`/`body`, so the page
  never inherits a host's dark or transparent background.
- **`<meta name="viewport" content="width=device-width, initial-scale=1">`**
  and a layout that works at 360px wide: reviewers often look on a phone.
- **Sample data only**, labeled as such. Never real client records in a
  prototype, and nothing leaves the machine unless the user asks.

## 2. Design direction is chosen, never defaulted into

State the source in the page footer and the SPIKE VERDICT, in this order of
priority: (1) the client's or project's existing look (colours, type, logo
from their site or files), (2) a direction the user named, (3) a stated
neutral direction ("plain owner-report style: white page, one accent
colour, system fonts"). A page that looks random is a defect in the
prompt, not taste. Clean, white, readable beats decorative for client work.

## 3. The question at the top, the answer controls at the bottom

- **Top:** the design question in one sentence, the shape, and the timebox.
- **Variants (look questions):** exactly three, radically different, in
  `<section data-variant="A|B|C">`, switched by one control at the top
  (`data-variant-switch`). Only one shows at a time; the URL hash
  (`#variant-B`) opens a specific one.
- **Surfaced state (logic questions):** a visible state panel
  (`data-state-panel`) that re-renders after every action, so the reviewer
  sees what changed.
- **Numbered review points:** every block worth commenting on carries
  `data-review-id="1"`, `"2"` … and a small visible badge (`#1`, `#2`). The
  reviewer can then say "#3 is too dense" in any channel, even plain chat.
- **Answer controls** (`data-question` on each): native radios/checkboxes/
  text inputs for the questions that decide the verdict, e.g. *"Which variant
  answers the question?"*, *"What would an owner miss in 30 seconds?"*.
- **Copy-my-answers button** (`data-copy-feedback`): builds one plain-text
  block from the controls and any per-point notes and copies it, e.g.
  `PICK: B · #3: too dense · #5: rename "Leads" to "New inquiries"`. The
  reviewer pastes it back; that text, quoted verbatim, is the SPIKE VERDICT's
  EVIDENCE.

## 4. Review channels (use the first available)

1. **lavish-axi on the user's computer** (if installed or `npx` is
   available there): `npx -y lavish-axi proto-<slug>.html` opens it for
   in-page annotation; collect feedback with its poll command. The page
   works unchanged, because lavish-axi serves the saved file as-is.
2. **Claude app:** publish the page as a private artifact; the reviewer
   uses the answer controls and comments there.
3. **Anywhere else:** the user opens the file in a browser, presses Copy my
   answers, and pastes the block into the chat.

Never wait silently: say which channel you used and what to send back.

## 5. Revision rounds

- Each feedback round regenerates the **whole file** (never patch in place),
  bumps a revision, and fills the revisions legend:
  `<script type="application/json" data-revisions>[{"id":"r2","summary":"#3
  split into two rows; variant C dropped"}]</script>`, with
  `data-rev="r2"` on each changed block and a visible "What changed" note.
- Rounds count against the timebox: one round by default, one declared
  extension. Feedback that changes the question opens a new question.

## 6. Templates by question type

Pick the one that matches the question; one page may combine two.
- **Comparison** (which option?): the same 3–5 criteria in the same order
  for every option; differences highlighted; a pick control.
- **Plan / flow** (does this sequence hold?): steps as numbered cards with
  owner, input and output; the risky step marked; a "where does it break?"
  control.
- **Diagram** (does this structure make sense?): inline SVG with labeled,
  numbered nodes; a short legend; no decorative shapes.
- **Table / dashboard** (is this scannable?): the 5–7 numbers that matter,
  one highlighted; a "what did you read first?" control.
- **Form / input** (will people fill this in?): the real fields with sample
  data; a "which field would you skip?" control.
- **Explainer** (will the reader get it?): one idea per section; a "where did
  you get lost?" control.

## 7. Machine check

With **jail-py-toolkit**: `artifact-lint.py proto-<slug>.html` checks the
title and banner marking, viewport, explicit background, no outside
requests, unique review ids, exactly three variants with one switcher for
look questions, answer controls with a copy button, and that a revisions
legend parses. Fallback: check those by hand and say "manually checked".
