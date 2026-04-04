# Using Gemma 4 as a Claude Code Backend

Claude Code can be pointed at any OpenAI-compatible API endpoint. llama-server implements this interface, allowing Gemma 4 to act as the backend model.

## Environment Variables

```bash
export ANTHROPIC_BASE_URL=http://<server-ip>:8081
export ANTHROPIC_AUTH_TOKEN=none
export ANTHROPIC_API_KEY=""
```

## Launch

```bash
ANTHROPIC_BASE_URL=http://<server-ip>:8081 \
ANTHROPIC_AUTH_TOKEN=none \
ANTHROPIC_API_KEY="" \
claude --model gemma4
```

Claude Code will send requests to llama-server as if it were the Anthropic API. No code changes or plugins are required.

## Model-Optimized System Prompt

Gemma 4 26B has ~4B active parameters per forward pass. Without guidance, it tends to:

- Attempt long tool-use chains that exceed its planning capacity
- Retry failed operations without changing approach
- Leave dead code from abandoned implementation paths

The [CLAUDE.md](../claude-config/CLAUDE.md) in this repo constrains these behaviors. Place it in the working directory before starting a Claude Code session. Key constraints:

1. **One tool call at a time** — prevents multi-step planning failures
2. **Read before write** — prevents edits based on assumed file contents
3. **Two-failure limit** — stops retry loops and escalates to the user
4. **Scope restriction** — prevents unsolicited refactoring

These constraints were developed through iterative testing and are specific to the 26B parameter class. Larger models may not need them.
