# Gemma 4 26B — Agentic Capability Scorecard

## Configuration
- **Model:** Q5_K_M, 262K context, turbo3 KV, FA on
- **Speed:** ~129 tok/s
- **Date:** 2026-04-04

## Results

| Test | Level | Pass | Tool Calls | Errors | Self-Recovery | Quality (1-5) | Notes |
|------|-------|------|------------|--------|---------------|---------------|-------|
| 1A Text stats | 1 | PASS | ~3 | 0 | N/A | 4 | Clean impl, handles edge cases |
| 1B Graph class | 1 | PASS | ~4 | 0 | N/A | 3 | Works but has_cycle has dead code from mid-stream approach change |
| 1C CSV transformer | 1 | PASS | ~4 | 0 | N/A | 4 | Clean argparse CLI, created sample data, verified with piped flags |
| 2A Add feature | 2 | PASS | ~3 | 0 | N/A | 4 | Read + edit preserved existing code. length_difference uses unique counts (minor) |
| 2B Add algorithm | 2 | PASS | ~4 | 0 | N/A | 4 | Clean refactor, shared setup code, correct Bellman-Ford, backward compatible |
| 2C Refactor | 2 | PASS | ~6 | 0 | N/A | 4 | Used plan mode unprompted, extracted 3 helpers, verified + cleaned up test script. 2m23s |
| 3A Write + run | 3 | PASS | ~7 | 5 | Yes | 3 | Correct code + verification, but 5 "Invalid tool parameters" errors after success before recovering |
| 3B Generate + process | 3 | PASS | ~6 | 1 | Yes | 4 | Installed faker autonomously when missing, then two-script chain worked cleanly |
| 3C HTTP endpoint | 3 | PASS | ~6 | 0 | N/A | 4 | Full start/test/stop lifecycle. Both endpoints verified with curl |
| 4A Runtime bug | 4 | PASS | ~5 | 0 | N/A | 5 | Found exact bug (append→extend) on first try, verified both algorithms |
| 4B Logic bugs | 4 | PASS | ~5 | 0 | N/A | 5 | Found both bugs (precedence swap + left-assoc >=) on first try. 1m27s |
| 4C Multi-error | 4 | PASS | ~5 | 0 | N/A | 5 | Found all 3 bugs (json.dump, int cast, filter inversion) cleanly. 1m55s |
| 5A Multi-file package | 5 | PASS | ~6 | 0 | N/A | 5 | 4 files, correct package structure, relative imports, sample stdev, all methods verified |
| 5B Config-driven app | 5 | PASS | ~8 | 1 | Yes | 3 | Self-recovered from config path error. Reloads config per request, standalone mode broken. Works end-to-end |
| 6A Test-driven impl | 6 | PASS | ~5 | 0 | N/A | 5 | All 20 tests passed first try. Clean implementation with proper dunder methods |

## Summary
- **Level 1 (Single file):** 3/3 passed
- **Level 2 (Read + modify):** 3/3 passed
- **Level 3 (Multi-step):** 3/3 passed
- **Level 4 (Debugging):** 3/3 passed
- **Level 5 (Multi-file):** 2/2 passed
- **Level 6 (Test-driven):** 1/1 passed
- **Total:** 15/15

## Agentic Ceiling
**Not found within this test suite.** Gemma 4 26B passed all 15 tests across all 6 levels. Minor issues observed:
- **3A:** 5 "Invalid tool parameters" errors after successful verification (tool loop exit problem)
- **5B:** Config path error requiring self-recovery; messy config reloading per request
- **1B:** Dead code left in has_cycle from mid-stream approach change

The tests may not be hard enough to find the ceiling. Weaknesses appear in:
1. Clean exit from tool-use loops (3A)
2. Cross-file state management at scale (5B was the weakest pass)
3. Code cleanup / dead code removal (1B)

Suggested harder tests: multi-file refactoring with shared state, error recovery chains (3+ consecutive failures), larger codebases (>500 LOC), concurrent file edits.

## Comparison Notes
_Run the same tests with Claude Opus to establish baseline._
