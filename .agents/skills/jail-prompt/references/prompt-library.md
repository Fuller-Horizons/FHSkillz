# Prompt library: reuse what already worked

Load this at the start of Phase 3 (check the library) and after a prompt passes
its tests (save it). A tested prompt that fits beats a new one.

## Where it lives

Use the first that exists:
1. The attached claude.ai Project: doc `claude/prompt-library.md`
   (visible in Claude Code, the Claude app, and chat).
2. The repo or working folder: `prompts/` with one file per prompt plus
   `prompts/INDEX.md`.
3. Neither: offer to create option 1 or 2. Never save without the user's OK.

## Before writing a new prompt

Search the library for the task type and keywords. If a saved prompt fits:
- Reuse it, filling in the new CONTEXT and inputs.
- Re-run its saved test set if the model or effort changed since it was tested.
- Say "reused <name> v<n>, tested <date>".

## Entry format (one per prompt)

```
## <name> v<n> — <one-line purpose>
Tested: <date> · <model> · effort <level> · score <passed>/<run> · baseline won <x>/<n>
Use when: <trigger, one line>
Inputs: <tag names>
Test set: <where the inputs are saved>
Changes: v<n>: <what changed and why>
<the full prompt block>
```

## Rules

- Save only prompts that passed their test set (prompt-testing.md). Untested
  drafts stay out, or are marked `untested`.
- Never save secrets, client personal data, or real customer records in a
  prompt or test set. Mask them first.
- A new version keeps the old one's entry (one line in Changes) so a
  regression can be rolled back.
- Retire an entry when a newer version beats it on the same test set.
