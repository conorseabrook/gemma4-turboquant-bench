# Agentic Capability Test Suite

15 tests across 6 difficulty levels, designed to measure a local LLM's ability to use tools (file I/O, shell commands, code execution) through Claude Code.

## Methodology

Each test is run in a fresh Claude Code session (`/clear` between tests). The model receives a natural language prompt and must complete the task using Claude Code's built-in tools: file read/write/edit, bash execution, and glob/grep search.

Tests are ordered by difficulty and have a dependency chain: Level 2 modifies files created by Level 1. Levels 3-6 are independent.

## Scoring Rubric

| Metric | Description |
|--------|-------------|
| Pass/Fail | Did the model produce a working result? |
| Tool Calls | Approximate count of tool invocations |
| Errors | Count of failed tool calls |
| Self-Recovery | Did the model recover from errors without user intervention? |
| Quality (1-5) | Code quality: correctness, edge cases, cleanliness |

## Levels

### Level 1: Single File Generation
Create one file from scratch. Tests basic code generation and file I/O.

### Level 2: Read + Modify
Read an existing file and make targeted changes. Tests comprehension and surgical editing.

### Level 3: Multi-Step with Verification
Write code, execute it, and verify the output matches expectations. Tests the observe-act loop.

### Level 4: Debugging
Find and fix intentional bugs in provided code. Tests error diagnosis and targeted repair.

### Level 5: Multi-File Coordination
Create or modify multiple files that must work together. Tests cross-file reasoning and import management.

### Level 6: Test-Driven Implementation
Write code to pass a pre-written test suite. Tests spec comprehension and iterative development.
