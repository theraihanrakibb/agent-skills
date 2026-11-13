# ai-infra-helper

A contributor coach for AI-inference open-source repos (SGLang, vLLM, TensorRT-LLM, lmdeploy, …). Helps you navigate the codebase, find the right test/lint commands, and draft PRs — including the fork-PR CI gotchas.

## When to use

- "how is sglang structured", "where do I add a model in sglang", "what tests do I run before pushing", "draft a PR for this change", "why is my fork PR CI failing".

## Guided flow

1. **Name the repo.** If unclear, say which (SGLang fork? vLLM? other). The skill consults `references/ai-infra-repos.md` for a layout cheat-sheet.
2. **Find the change point.** It points at the likely file(s) from the cheat-sheet, then verifies with Grep / Glob before answering.
3. **Get the right test command.** It gives the minimal lint+test command (usually `pre-commit` + targeted path), not the full suite, and explains the fork-PR CI behavior (for SGLang, only `lint` gates your code; `pr-test-*` fails by design on forks).
4. **Draft the PR.** Reuses the `pr-draft` workflow (Conventional Commit + PR description from `templates/pr-description.md`).

## Rules

- Push only to your fork, never upstream.
- Don't run the full test suite just to "make CI green" — most failures are fork-only.

## Files

- `SKILL.md` — router + workflow.
- `references/ai-infra-repos.md` — SGLang/vLLM layout + CI behavior (authoritative).
- `templates/pr-description.md`.
