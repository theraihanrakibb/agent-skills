# pr-draft

Turn staged git changes into a clean Conventional Commit message, a structured PR description, and a changelog entry.

## When to use

- "write a commit message", "draft a PR", "what should my commit message be", "summarize my diff", "make a PR description".

## Prerequisites

- A git repo with staged changes (or a recent commit to base the message on).
- The bundled `scripts/git-diff-staged.sh` is an optional bash helper (Git Bash / WSL) that fetches the staged diff.

## Guided flow

1. **Get the diff.** Runs `scripts/git-diff-staged.sh`; if nothing is staged, falls back to `git diff HEAD~1` or asks what to base it on.
2. **Produce three outputs:**
   - **Conventional Commit message** — `<type>(<scope>): <subject>` + body (types: feat, fix, docs, style, refactor, perf, test, chore, build, ci).
   - **PR description** — from `templates/pr-description.md` (Summary, Changes, Why, Testing, Screenshots).
   - **Changelog entry** — one Keep-a-Changelog line under Added / Changed / Fixed / Removed.
3. **Review & commit.** Presents the message; only runs `git commit` after your explicit OK. Never pushes or amends published commits.

## Files

- `SKILL.md` — router + workflow.
- `templates/pr-description.md` — PR description scaffold.
- `scripts/git-diff-staged.sh` — staged-diff fetcher.
