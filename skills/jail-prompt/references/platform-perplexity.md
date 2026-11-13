# Platform pack — Perplexity: Agent API, Sonar & the consumer app

**Verified: 2026-09-14** against the docs listed under *Sources* below. Re-verify before
relying on any lever here. Every line traces to a fetched doc page — if you can't cite
one, it doesn't belong here (see the Evidence contract in SKILL.md).

**Read the docs verbatim.** Every `docs.perplexity.ai` page has a raw-markdown twin —
append `.md`. Page index at `docs.perplexity.ai/llms.txt`. ⚠️ **None of Perplexity's
doc or Help Center pages expose a last-updated date**, so "current" here means "live
content at verification", not "dated content."

⚠️ **Platform fact that reframes everything below: Sonar Chat Completions is
deprecated.** "Sonar Chat Completions is now Agent API. Sonar will be supported until
**September 27, 2026**." The **Agent API Prompt Guide is now the primary artifact**; the
Sonar guide mainly documents one structural difference. Write new prompts against the
Agent API.

---

## Why this platform is different

**The prompt shapes retrieval, not just tone.** "Prompts that work well with single-shot
LLMs often underperform here, because the same text shapes tool selection, search query
generation, and final response together." And: "`input` holds the actual question. It
also seeds the first search query, so specificity here directly improves retrieval."

That one fact drives most of what follows: on Perplexity, a vague question is not a
style problem, it is a **retrieval** problem.

**On Sonar the system prompt does NOT affect search — verified, verbatim:** "Sonar runs a
web search before generating its answer, and only the user message is used to drive that
search. The system prompt is not visible to search; it reaches the model only at answer
time, when results are already in hand." And: "System messages only influence generation,
never retrieval." And: "a polished system prompt cannot rescue a vague user message. If
retrieval quality matters, invest there first."

**But this is Sonar-specific and expires with Sonar.** "This contrasts with the Agent
API, where `instructions` are re-read on every turn of the agent loop and shape both tool
calls and the final answer. In Sonar, `instructions` has no equivalent." Do not carry the
"system prompt doesn't affect search" rule into Agent API prompts.

---

## Levers that change how you write the prompt

**Be specific and use page vocabulary.** "Use natural language, but include the
vocabulary and context that would actually appear on relevant pages. Add a few words of
context to disambiguate when a term could mean multiple things."
✅ *"Compare energy efficiency ratings of heat pumps vs. traditional HVAC for residential
use"* ❌ *"Tell me which home heating is better"*.
Sonar's own pair: ✅ *"What guidance has the FDA issued on AI in medical devices in the
past year, and which device categories does it cover?"* ❌ *"Tell me about FDA AI rules."*

**Cap result counts explicitly.** "If you want a list, say how long. Without an explicit
cap, the model picks an arbitrary length." ✅ *"List the top 5 sushi restaurants in
Tokyo"*.

**Filters, not prose — this is the headline rule.** "For source, date, or region
constraints, prefer the `web_search` parameters over describing the constraint in prose.
Parameters are applied by the search backend on every call, while prose-based filters are
interpreted by the model and may not carry through every turn of the loop."
And bluntly: **"The search backend reads parameters; it does not read the system prompt."**

Documented filter surface:
- `search_domain_filter` — **max 20** entries; allowlist (bare domains) OR denylist
  (`-` prefix); "Use `search_domain_filter` in either allowlist mode or denylist mode,
  not both."
- `search_recency_filter` — `hour|day|week|month|year`; "cannot be combined with other
  date filters"; "Use `hour` for real-time data such as breaking news or live events."
- `search_after_date_filter` / `search_before_date_filter` (publication) and
  `last_updated_after_filter` / `last_updated_before_filter` (update) — all `%m/%d/%Y`.
- `search_language_filter` — ISO 639-1, max 10.
- `user_location` inside `web_search_options` — "Latitude and longitude must be provided
  together with country. They cannot be supplied on their own"; "City and region
  significantly improve location accuracy."

**`search_context_size` maps to real token budgets:** `low` = 300 tokens total / 300 per
page (simple facts); `medium` = 1,000 / 1,000 (general research); `high` = 4,000 / 4,000
(source-heavy answers). Overridable via `max_tokens` / `max_tokens_per_page`.
"You're charged for actual consumption, not requested budget." `max_results` 1–50.

**Academic / SEC on the Agent API are domain filters, not a mode flag.** `search_mode`
(`web|academic|sec`) exists only on the legacy Sonar endpoint; the current cookbook
articles achieve both modes with domain filters — academic: `arxiv.org`, `nature.com`,
`pubmed.ncbi.nlm.nih.gov`, `.edu`; SEC: `sec.gov`, `edgar.sec.gov`, `efts.sec.gov`.
*(No explicit deprecation of `search_mode` was found — that it is Sonar-only is
inference, so flag it as such.)*

**Read citations from structured fields, never from the prose.** Agent API: "Read URLs
and source metadata from the response payload, not from the model's written answer…
search results are inside `response.output[]` as items where `type == \"search_results\"` —
the response contains one such item per search the model ran, all sharing a single
citation `id` space, so collect the results from every item rather than only the first."
And: "The model has access to URLs from tool output and can include them in its response
if asked, but it's prone to mistyping or paraphrasing them." Sonar: sources are always in
top-level `citations` and `search_results`. Streaming: listen for
`response.reasoning.search_results` events.

**Grounding rules belong in `instructions`,** "because instructions are re-read on every
turn of the agent loop, so the same rule applies to the first search and to any
follow-ups." Two verbatim drop-ins — **these are directly reusable in jail-prompt's
SOURCES / CONSTRAINTS lines:**

> "If searches do not return relevant results after trying alternative phrasings, say so
> explicitly rather than providing speculative information."

> "If you find related but non-matching results (for example, a different year, a parent
> company, or a subsidiary), state the mismatch explicitly before answering."

Documented risk conditions: "Hallucination is most likely when the information isn't
web-accessible (posts that require authentication, private documents, paywalled content),
when repeated searches return related but non-matching results, or when very recent
information isn't indexed yet."

**`instructions` REPLACE a preset's system prompt — they do not append.** "Each preset
(`fast`, `low`, `medium`) already covers tool-call discipline, query construction,
citation, and formatting, so the preset's prompt should be overridden only when
app-specific behavior is needed." Also: "The API substitutes `{{current_date}}` only in a
preset's default instructions; placeholders in request-provided `instructions` are sent
literally."

**Keep `instructions` short** — "They are re-read on every turn of the agent loop, so
bloat compounds across tool calls." And: "Reach for `web_search` filters and
`response_format` before adding more instruction prose."

**Don't explain the built-in tools.** "Built-in tools like `web_search` and `fetch_url`
are tuned to work well without prompt-side guidance. You don't need to describe what they
do, when to call them, or how to construct queries. Adjust tool-call count with the
`max_steps` parameter." Custom function tools are the opposite — "the model relies on the
`description` and parameter schema you provide."

**The `instructions` vs `input` split rule:** "if a rule should still apply when the user
asks something completely different, it belongs in `instructions`… If it is about this
request, it belongs in `input`."

**Depth is a preset, not a model (Agent API).** `fast` (max_steps 1, web_search only),
`low` (5 steps), `medium` (15 steps), `high` (15 steps), `xhigh` (100 steps, web_search +
finance_search + sandbox), `wide-research` (100 steps). Legacy Sonar models remain:
`sonar`, `sonar-pro`, `sonar-reasoning-pro`, `sonar-deep-research`.

**Wide/deep research quality tracks prompt precision.** "Give it a concrete target…
clear qualification rules… a required source per record, and an explicit output shape."
Concretely: a numeric floor ("at least 70 companies"), qualification rules (date ranges,
geography, eligibility thresholds), "an authoritative page that names" each entity, and
"name the file and list the exact fields per row." **This is the closest documented match
to jail-prompt's SUCCESS TEST + OUTPUT FORMAT discipline — mirror it.**

**Structured outputs:** `response_format: {type: "json_schema", json_schema: {name,
schema}}`; `name` mandatory, 1–64 alphanumeric; "Properties in the schema's `required`
array will be enforced"; omitted properties "may resolve to JSON `null`".
⚠️ Latency caveat: "The first request with a new JSON Schema expects to incur delay on the
first token. Typically, it takes 10 to 30 seconds to prepare the new schema, and may
result in timeout errors." Include format hints in the prompt as well.

**Search API (distinct product) query style:** "Use highly specific queries for more
targeted results"; "Specific queries with context, time frames, and precise terminology
yield more relevant and actionable results." ❌ `"AI"` → ✅ `"artificial intelligence
machine learning healthcare applications 2024"`. Up to **5 queries per multi-query
request**; "Multi-query searches split this budget across reformulations."

---

## Consumer app specifics

**The golden rule:** "State your intent clearly and provide detail."

**Verbatim best-practice list:** State your intent clearly · Provide detailed information
· Be specific, not vague · **Give context about who you are and the purpose** ·
**Focus on one request at a time** · Specify desired format · Refine through iteration ·
Use plain, natural language.

**Prompt anatomy framework (5 parts):** *Instruction* ("Clearly say what you want
Perplexity to do") · *Context* · *Input* · *Keywords* · *Output format*. Summarised as
"start with a clear goal, use straightforward language, and provide enough background."

**Task + Context + Output** is the clearest official consumer template (Perplexity
Computer, Academy): Task — "Say what you want Computer to do, not just the topic you want
to explore." Context — "Include the context Computer needs to do the work well" (files,
connected tools, intended audience). Output — "Be specific about the output."
❌ *"help me understand churn"* → ✅ *"Analyze customer churn from our CRM data and
summarize the top three drivers"*; ❌ open-ended format → ✅ *"Create a five-bullet
summary"* / *"Build a dashboard spec."* Also: "Keep the task focused"; provide multiple
items "in clear order rather than all at once"; "Use the same thread to improve the
work"; "start a new task when the goal changes."

**Search vs Computer routing rule, verbatim:** "One-time answer, one clear question, use
Search. Multi-step work, connected tools, recurring output, use Computer." Search when
"the answer is the deliverable" and "the context fits in the query or an attached file";
Computer when "the task touches multiple apps or connected tools" or it "needs to run on
a schedule or monitor changes over time."

**Research mode:** "conducts in-depth research and analysis on your behalf," typically
under 3 minutes. Crucially: "Research uses a specific combination of models" and "you
cannot manually choose a specific model when using Research" — so model-selection advice
is inapplicable there. ✅ *"Research the environmental impact of fast fashion and suggest
sustainable alternatives."* ❌ *"Tell me about fashion."*

**Labs** is the 10+ minute tier with "deep web browsing, code execution, and chart and
image creation" plus "advanced file generation and mini-app creation," outputs collected
in an Assets section. **No prompting methodology is published for Labs** — the only
official source is the 2025-05-29 launch blog.

**Deliverable prompting:** "State file type explicitly. Describe structure and content.
Use follow-ups to refine." Exports DOCX/PDF/PPTX/XLSX. ✅ *"Create a professional PDF
report on renewable energy in the US, with charts and citations."* ❌ *"Write something
for me."*

**Projects (formerly Spaces)** — "a persistent, shareable workspace." Custom instructions
up to **8,000 characters** that "tell Computer how to work inside this Project", e.g.
"a preferred response format or a status file to keep updated." Settings set the default
mode (Search vs Computer) and a default orchestrator model. Projects are private
(Restricted) by default.

**Focus is gone.** "For Enterprise Pro users, Focus has been replaced with Choose
sources, allowing you to use Internal Knowledge Search by selecting between Web, Org
Files, Web + Org Files, or None." Also: "The system automatically classifies queries and
triggers appropriate search modes as needed, even without manual selection." The 2024
blog's "Refine with Focus" advice is **stale**. (Org Files retires 2026-10-01.)

**Source labels (Aug 2026):** Government · Academic · Trusted ("a broad category for
sites that appear often enough in results to receive a label"). Labels describe a whole
domain, not an article; "no label does not mean a site is low quality"; they are not
endorsements and "should never substitute for reading original sources yourself."
**Do not treat a Trusted label as a source tier** — map it through `references/sources.md`.

**Comet:** "Define exactly what you want to achieve and in what format" rather than
"Help me with my emails." Use **`@tab`** to point at specific pages ("Compare the pricing
information in @tab1 and @tab2"). "Break requests into clear sequential steps for best
results." ❌ *"Tell me about this company"* → ✅ *"As my research assistant, give me a
200-word investor-focused overview…"* — **the one place Perplexity endorses a role frame,
and it is paired with a length + audience constraint.** Comet "click[s], type[s], and
interact[s] for you under supervision" — supervision is the documented pattern.

---

## Documented anti-patterns

**The hard API warning, verbatim:** "Do not put search instructions in the system prompt.
Phrases like 'search only on Wikipedia' or 'look for the latest results' have no effect.
For hard constraints like domain, recency, or region, use the dedicated search filter
parameters on the request body rather than trying to express the constraint in prose."

**The labelled Avoid → Better pair:**
- `Avoid`: `input="Using only Wikipedia as a source, summarize the history of the Apollo
  program…"`
- `Better`: `input="Summarize the Apollo program history…"` +
  `tools=[{"type": "web_search", "allowed_domains": ["wikipedia.org"]}]`

**Don't few-shot written-out answers.** "Pasting a written-out example answer can cause
the search step to latch onto the example topic. Few-shotting *structure* is fine; for
guaranteed shape use `response_format`."
⚠️ **Provenance caveat:** the Sonar page attributes this to the Agent API guide, but the
current Agent API guide contains no few-shot text at all. **The rule is real and
quotable, but only from `/docs/sonar/prompt-guide` — a page 13 days from deprecation at
verification.** Re-verify whether it survives into the Agent API guide.

Other explicit warnings:
- ❌ Asking for URLs in the response text — "prone to mistyping or paraphrasing them" and
  it "fights the default citation format."
- ❌ Requesting links inside JSON — "may not always work reliably and can result in
  hallucinations or broken links."
- ❌ Leaving list length unspecified.
- ❌ Bloating `instructions` — "bloat compounds across tool calls."
- ❌ Describing built-in tools.
- ❌ Assuming `instructions` appends to a preset.
- ❌ Reading only the first `search_results` item.
- ❌ Filter mode collisions (allowlist + denylist; recency + date; lat/long without country).

**Consumer named failure modes:** "Avoid vagueness, overloading queries, or omitting
important context"; "Focus on one request at a time"; "Avoid multiple unrelated requests
simultaneously." The ❌ examples are themselves the anti-pattern set: *"Cars"* ·
*"Tell me about fashion"* · *"Make me a picture"* · *"Make a video"* · *"Write something
for me"* · *"help me understand churn"* · *"Help me with my emails"* ·
*"Tell me about this company"*.

**Comet named anti-patterns:** "Overly broad requests, ignoring available context, failing
to break complex workflows into steps, or neglecting to specify output format typically
yield generic responses."

---

## Gaps — state these rather than guessing

- **No last-updated dates** anywhere on docs or Help Center. Date-anchoring is only
  possible via the changelog and article-ID conventions.
- **`search_mode` status is ambiguous** — present in the Sonar API reference, absent from
  the filters guide, the Agent API `web_search` reference, and the academic/SEC cookbooks.
  No explicit deprecation statement found.
- **`sonar-deep-research` has no published prompting guidance** — description, pricing and
  use cases only.
- **Labs has no official prompting documentation.**
- **No structured-output per-model support matrix** in current docs.
- **No current consumer article enumerating source types** (Academic / Social / Video);
  the only documented selection surface is the Enterprise "Choose sources."
- Perplexity Academy's query best-practices lesson is **video-first** — the framework and
  examples above were extracted from the page; the video may contain more.

---

## Sources (fetched 2026-09-14)

- **Prompt Guide (Agent API)** — `docs.perplexity.ai/docs/agent-api/prompt-guide` — *the canonical guide now*
- Prompt Guide (Sonar, deprecating) — `docs.perplexity.ai/docs/sonar/prompt-guide`
- Prompt the agent — `…/docs/agent-api/building-agents/prompt-the-agent`
- Web Search tool — `…/docs/agent-api/tools/web-search`; Search Filters — `…/docs/sonar/filters`
- Output Control — `…/docs/agent-api/output-control`; Features — `…/docs/sonar/features`
- Presets — `…/docs/agent-api/presets`; Wide Research — `…/docs/agent-api/wide-research`
- Models — `…/docs/sonar/models`, `…/models/sonar-deep-research`
- Best Practices (Search API) — `…/docs/search/best-practices`
- POST Sonar reference — `docs.perplexity.ai/api-reference/sonar-post`
- Changelog — `…/docs/resources/changelog`; page index — `docs.perplexity.ai/llms.txt`
- Cookbooks — `…/docs/cookbook/articles/academic-search/README`, `…/docs/cookbook/examples/sec-filing-search/README`
- Tips for Getting Better Answers — `perplexity.ai/help-center/en/articles/13645819-…`
- Practical Tips for Using Perplexity — `…/articles/10352971-…`
- What are Projects? — `…/articles/10352961-what-are-spaces`
- What is Research mode? — `…/articles/10738684-…`; Focus replacement — `…/articles/10354759-…`
- Understanding source labels — `…/articles/20260806-understanding-source-labels`
- Computer Query Best Practices · Search vs Computer — `perplexity.ai/hub/academy/…`
- Getting the Best Answers from Comet — `perplexity.ai/comet/resources/articles/…`; Comet advice — `perplexity.ai/help-center/comet/en/articles/11732243-…`
- Introducing Perplexity Labs — `perplexity.ai/hub/blog/introducing-perplexity-labs` (2025-05-29)
