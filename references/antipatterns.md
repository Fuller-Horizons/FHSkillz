# Prompt-engineering antipatterns

Before finalizing a prompt (or accepting a goal), sanity-check it against these named failure modes. Each has a **tell** (how to spot it) and a **fix**. This file teaches judgment — it is not a checklist to recite; use it to catch yourself.

## Premise & stance failures (check these first — they invalidate everything downstream)

**Validation bias / agreeableness.** *Tell:* you're about to praise, endorse, or build the user's idea because it's theirs, not because it's good — or the prompt asks the model to "confirm," "justify," or "support" a conclusion the user already holds. *Fix:* earn every endorsement. If the premise is flawed, say so plainly and engineer toward the *correct* goal, not the requested one. A prompt that flatters its author ships a wrong answer confidently.

**Leading the witness.** *Tell:* the prompt embeds the desired conclusion ("explain why X is the best option") so the model can only agree. *Fix:* ask the open question ("compare X, Y, Z on these criteria and recommend one") and let the evidence decide. Bake in the possibility that the answer is "none of these."

**Solving the wrong problem.** *Tell:* the prompt is technically excellent but aimed at a goal that won't get the user what they actually need (the XY problem). *Fix:* in framing, confirm the underlying need, not just the stated request.

## Specification failures

**Over-constraining.** *Tell:* you're dictating step-by-step *how* when the model could find a better path from the *what*. *Fix:* give criteria and a success test; let the model loop to them. Constrain outcomes, not keystrokes.

**Fake precision.** *Tell:* invented thresholds, made-up percentages, or false specificity ("exactly 7 reasons," "a 23% improvement") with no basis. *Fix:* specify only what the goal actually requires; mark anything you can't ground as an assumption.

**Kitchen-sink prompt.** *Tell:* everything and the kitchen sink, no priority, "also handle A, B, C just in case." *Fix:* one prompt, one job. Cut anything the success test doesn't require. If it's genuinely many jobs, decompose into a chain.

**Scope creep / speculative flexibility.** *Tell:* "make it extensible / future-proof / configurable" with no present need. *Fix:* build for the goal in front of you; premium ≠ bloated.

## Verification failures

**Unverifiable success test.** *Tell:* "make it good / compelling / professional" — nothing you could objectively check. *Fix:* write a test a stranger could grade: a named output, a measurable metric, a pass/fail condition.

**Confidence theater.** *Tell:* the prompt asks for a confidence number or "verified" stamp without requiring any actual grounding. *Fix:* tie confidence to evidence; require sources before any verification claim. No earned-confidence, no number.

**Stale-source blindness.** *Tell:* a time-sensitive task (prices, leaders, versions, law) with no recency requirement. *Fix:* set an explicit freshness window and require dated sources (see `sources.md`).

**Context starvation.** *Tell:* a strong ROLE and OBJECTIVE but none of the user-specific facts that would actually change the answer. *Fix:* front-load the gathered context (constraints, environment, what's been tried) in a CONTEXT line.

## Presentation failures

**Role cosplay.** *Tell:* an elaborate persona ("You are a world-renowned Nobel-winning...") that changes nothing about the output. *Fix:* use role only where it functionally shifts expertise, vocabulary, or standards. Otherwise drop it.

**Premature / over-formatting.** *Tell:* tables, headers, and bold everywhere, obscuring thin content. *Fix:* match format to the content and the user's chosen output shape; formatting serves readability, not the appearance of effort.
