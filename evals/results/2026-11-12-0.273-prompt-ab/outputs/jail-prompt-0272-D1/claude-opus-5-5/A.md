The prompts are written but untested. They're in `prompts.md`, with the wiring in `manifest.json`. I chose the Full lane because the client will see the output.

**Is it worth doing?** Yes, with two caveats:
- **"Biggest" can't mean revenue.** These companies are private, so revenue figures are rarely public. The prompts rank them by public size signals instead: headcount, crews or fleet, number of locations, and named commercial clients. The review has to say this up front.
- **Expect most published pricing to come back "Unknown".** Commercial landscaping is usually priced by bid. To get some real numbers anyway, the prompts also search public bid awards from Suffolk County, its towns and school districts for grounds work and snow removal.

**How the run is set up:**
1. **discover** (Opus): screens at least 12 candidates and ranks the top five, with the evidence behind each rank. This step has to finish first, because the next step needs the list.
2. **profile-1 to profile-5** (Sonnet, in parallel): one company each, covering services, service area, reviews and pricing. A profile that fails its check gets one re-run on Opus.
3. **quote check**: a script confirms that every quoted fact actually appears in the page it cites. Any that don't are changed to "Unknown".
4. **merge** (Opus, high effort): produces `competitors.json`, a comparison table in `review.md`, and a list of gaps in `gaps.md`.
5. **verify** (Fable 5.2, a different model): checks every fact and every rank against its live source. It never sees the other agents' work, only their output.

**Why subagents beat one prompt here:** the five profiles don't depend on each other, so they can run at the same time. The final check also needs to come from an agent that didn't do the research. The file includes a short single-agent version if you'd rather go cheaper.

**Assumptions** (change them in the `<params>` block at the top of the lead prompt):
- **Client name:** you need to fill in `{{CLIENT_NAME}}` so the client's own company is left out of the five.
- **Geography:** a company counts if it has its headquarters or a main yard in Suffolk and has commercial accounts there.
- **Seasonal work:** snow removal and holiday lighting are recorded as services but don't affect the ranking.

**Guardrails:** agents never contact a company (no forms, calls or quote requests), they treat fetched pages as data rather than instructions, and the whole run stops at 60 minutes.

UNTESTED: client-facing research run, not yet executed. Two lint scripts weren't run either: chain-lint needed an approval this session didn't get, so I checked the manifest by hand, and I didn't run prompt-lint on the briefs. Suggested test before trusting it on client work: run discover alone, check the five it picks against what you know of the local market, then run one profile and spot-check two of its facts.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [ranking by public size signals rather than revenue, HQ or main yard in Suffolk, snow and lighting recorded but not ranked, public sources only]
  unknowns: [client name to exclude, whether competitors publish any pricing, whether Google review pages can be fetched]
  outputs: [delegation set]
  next: jail-orchestrate
  approval_required: [running chain-lint and quote-check, approving the paid multi-agent run]
  tested: untested - not executed; chain-lint checked by hand, prompt-lint not run
```

I can save this to the project's prompt library (marked untested) or run it now, once you give me the client name.