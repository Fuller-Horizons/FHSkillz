Good instinct — the pull to start building is exactly the signal the map exists to catch. It usually means part of the way has cleared. Let me take thirty seconds to check *which* part, because "the first part" currently sits on two open decisions.

**Where the map stands** (`WAYFIND-client-onboarding.md` — destination: a locked spec + rollout plan):

Decided:
- **"New clients only, or expansions too?"** — new clients only for v1
- **"One onboarding path, or tiered by plan?"** — one path, with an enterprise add-on checklist

Still open:
- **"Which system owns onboarding state — HubSpot or Asana?"** — blocks the intake build and handoff automation
- **"Kickoff: self-serve portal or scheduled white-glove call?"** — blocks the first-part flow
- **"What counts as 'onboarded' (definition of done)?"** — blocks the spec's success gate
- **"Rollout: pilot cohort or big-bang cutover?"** — blocks the rollout plan only

The first part — intake through kickoff — sits directly on the first two open tickets. If I build it today I'm not skipping those decisions, I'm making them silently: whatever I ship hard-codes an answer to both. That's the classic way to end up with a confident, finished, *wrong* artifact — say, a self-serve portal built the week before you conclude kickoff should be a white-glove call.

So here's what I can actually do, in order of preference:

**1. Start the fog-proof slice today.** The intake question set and the welcome-sequence content survive every open ticket — they're identical no matter which tool hosts them or how kickoff runs. That slice is genuinely at the map's edge, so it gets a proper handoff: I'll scope it as a task contract (jail-task-contract) and start now. Note I'm *not* adding "build the first part" to the map — build tasks don't live there; they get handed off.

**2. Clear the two blockers, then build the rest of the first part safely.** One you can settle in a sentence right now: **self-serve portal or white-glove call?** The other — **which system owns onboarding state** — needs a short evidence pass on automation and API constraints (jail-research); I can run it as the next ticket and bring you a recommendation. Both get recorded on their tickets (decision, why, evidence) and one-lined into the map. After that, the entire first part is decision-free and building it is a handoff, not a gamble.

**3. If you want the full first part built regardless** — that's your call to make. But I won't smuggle it: I'd mark both open tickets as *decided by the build*, with the why, because building it **is** deciding them. I just want that to be a choice you're making, not a side effect you inherit.

My recommendation: 1 and 2 together. Give me the kickoff call in one line and I start the fog-proof slice immediately, with the system-of-record recommendation ready next session. The map stays the spine either way — handoff recorded, remaining tickets open, destination unchanged (locked spec + rollout plan), and this session still ends with the map current and a baton pointing at it.

So: portal, or white-glove call?
