# Agent Instructions

## Research Tool Priority Chain (MANDATORY)

When researching ANY topic (external docs, model comparisons, best practices, library usage, etc.):

1. **Nia FIRST** — Always use Nia (`search.sh deep`, `oracle.sh`, `search.sh web`, `search.sh universal`). Nia provides the most accurate, complete context. **The developer pays for unlimited Nia access. Do NOT hesitate to use it. Use it aggressively for: up-to-date framework docs, API documentation, latest industry standards, library versions, best practices — ANYTHING that could be searched instead of hallucinated. Nia is the best context layer available — better than Exa. You have unlimited Nia. USE IT.**
2. **Exa web search SECOND** — If Nia fails (timeout, rate limit, error), fall back to `websearch_web_search_exa`. Exa is more limited than Nia.
3. **Context7 / Webfetch LAST** — Only if both Nia and Exa fail.

**CRITICAL**: NEVER skip Nia. NEVER go straight to Exa or Context7 when Nia is available.
**CRITICAL**: ALWAYS run Nia research via background subagents (`run_in_background=true`) or `task(subagent_type='librarian')` — NEVER block the main agent with synchronous Nia calls.
**CRITICAL**: When in doubt, search Nia instead of guessing. NEVER hallucinate when Nia can give you the real answer.

## Main Agent Must NEVER Block (CRITICAL)

The main agent must ALWAYS remain free to receive user messages. **NEVER run long-running operations synchronously.**

- **Nia research**: ALWAYS delegate to a background subagent with `run_in_background=true`. NEVER run `search.sh deep`, `oracle.sh`, or any Nia script directly from the main agent.
- **Any operation > 5 seconds**: Delegate to a subagent or run in background.
- **While waiting for results**: The main agent should be IDLE and responsive, not blocked on a tool call.
- **If you have nothing to do while waiting**: That's fine — just don't block. The user's next message is more important than any background result.

**Anti-pattern (BLOCKING — never do this):**
```
# WRONG: Main agent runs Nia directly and blocks for 2 minutes
bash ./scripts/search.sh deep "query" (timeout 120000)
```

**Correct pattern:**
```
# RIGHT: Delegate to librarian/explore subagent which runs Nia
task(subagent_type='librarian', run_in_background=true, prompt='Use Nia search.sh deep to research X')
# Main agent is now FREE to take user messages
```

## Background Task Handling & Context Window Protection

**NEVER use `block=true` when calling `background_output`.** Always `block=false`. No exceptions.

### Rules
- Launch background agents with `run_in_background=true`
- Wait for system `[BACKGROUND TASK COMPLETED]` notifications
- Only call `background_output` after receiving the completion notification, ALWAYS with `block=false`
- When the user sends a message while tasks are running, respond to the user FIRST, then collect results
- When working on long multi-step plans, use `run_in_background=true` for parallel exploration tasks so the main agent remains free to immediately respond to new user messages

**The main agent must NEVER do work that can be delegated to subagents.** Delegate: large file reads, implementation work, research, and sequential tool output processing. The main agent orchestrates, synthesizes, and decides. Subagents do the heavy lifting.

## Delegation Protocol

- Always use `delegate_task()` for implementation work
- One task per delegation — never batch multiple tasks
- Use `session_id` for retries and follow-ups (preserves context, saves tokens)
- Store every `session_id` returned from delegations

## Debug-First Development

Always include server-side logging when building new features. Don't wait for bugs to add observability.

### Server-Side (always include)
- Add `console.log` with a `[TAG]` prefix for every new feature (e.g., `[AUTH]`, `[SYNC]`, `[API]`)
- Log key decision points: function entry, external API calls, database writes, error paths
- Include relevant IDs in logs (userId, requestId, etc.) for traceability
- Log timing for operations that hit external services

### Client-Side (errors only)
- Do NOT add verbose console.log to client components in production
- Use `toast.error()` with a clear message when something fails
- For debugging during development, add temporary `console.log` with `[DEBUG]` prefix and remove before committing

### Lifecycle
1. Build feature WITH server-side logging from the start
2. During development, add temporary client-side `[DEBUG]` logs as needed
3. Once feature is verified working, remove `[DEBUG]` client logs but keep server-side logs
4. Server-side logs stay permanently — they cost nothing and save hours during incidents

## End-of-Session Protocol (CRITICAL)

At the end of EVERY session, without exception:

```bash
git add -A && git commit -m "chore: end-of-session commit" && git push origin main
```

Then verify `git status` shows a clean working tree before ending.

**This includes ALL agent infrastructure files** — `.agents/`, `.claude/`, `.sisyphus/`, `skills-lock.json` — everything tracked in git.

**NEVER end a session with a dirty working tree.**
