#!/usr/bin/env node
// PreToolUse hook for the built-in Skill tool.
// Appends one JSONL line per skill invocation to the plugin's persistent data dir.
// Registered in hooks/hooks.json with matcher "Skill".
//
// Reads the PreToolUse event JSON from stdin. For the Skill tool, tool_input is:
//   { "skill": "<skill-name-or-/slash>", "args": "<optional args>" }
//
// Exits 0 always so it never blocks or breaks a skill invocation.

import { mkdirSync, appendFileSync } from "node:fs";
import { join } from "node:path";

function readStdin() {
  return new Promise((resolve) => {
    let data = "";
    process.stdin.setEncoding("utf8");
    process.stdin.on("data", (chunk) => (data += chunk));
    process.stdin.on("end", () => resolve(data));
    // Safety: if stdin never closes, resolve with whatever we have.
    setTimeout(() => resolve(data), 2000);
  });
}

try {
  const raw = await readStdin();
  let event = {};
  try {
    event = JSON.parse(raw || "{}");
  } catch {
    event = {};
  }

  const toolName = event.tool_name ?? "";
  // Only the Skill tool should reach here given the matcher, but guard anyway.
  if (toolName !== "Skill") process.exit(0);

  const input = event.tool_input ?? {};
  let skill = (input.skill ?? "").trim();
  if (skill.startsWith("/")) skill = skill.slice(1); // normalize /name -> name

  // CLAUDE_PLUGIN_DATA is exported into the hook process by Claude Code.
  // Falls back to a temp dir only if somehow unset (e.g. manual testing).
  const dataDir =
    process.env.CLAUDE_PLUGIN_DATA ||
    join(process.env.HOME || process.env.USERPROFILE || ".", ".fh-skillz-hooklog");

  mkdirSync(dataDir, { recursive: true });

  const line =
    JSON.stringify({
      ts: new Date().toISOString(),
      skill,
      args: input.args ?? "",
      session_id: event.session_id ?? "",
      cwd: event.cwd ?? "",
    }) + "\n";

  appendFileSync(join(dataDir, "skill-invocations.jsonl"), line, "utf8");
} catch {
  // Never fail the tool call because of logging.
}

process.exit(0);
