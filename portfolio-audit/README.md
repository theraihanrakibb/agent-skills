# portfolio-audit

Score your public GitHub repositories against a 10/10 quality bar and get a prioritized fix-plan. Useful before a job hunt, or any time you want your repos to look professional.

## When to use

- "audit my portfolio", "score my repos", "check repo quality", "which repos need improvement", or "fix my repos for a job hunt".

## Prerequisites

- Your public repos (the skill fetches them via `gh repo list <user>`, or you give local repo paths).
- The bundled `scripts/audit-repo.sh` is an optional bash helper (run via Git Bash / WSL) that gathers repo signals.

## Guided flow

1. **Pick what to audit.** Give a GitHub username (the skill lists your public repos) or a list of local repo paths.
2. **Signal gather + score.** For each repo it gathers signals — README, LICENSE, CI, tests, examples, `.gitignore`, description/topics — and scores 0–10 against `references/quality-bar.md`.
3. **You get a prioritized fix-plan:** repos ranked by lowest score, with the specific missing items tagged `[easy]` / `[medium]` / `[hard]`.
4. **Optional auto-fix.** It can scaffold LICENSE / README / `.gitignore` for the easy gaps — only after your explicit OK. Uses `templates/readme-scaffold.md`.
5. **Snapshot.** A dated snapshot (scores + plan) is saved so you can track progress over time.

## Rules

- Never commits or pushes without your explicit confirmation.
- Prefers `gh` CLI for remote repos; falls back to a local clone.

## Files

- `SKILL.md` — router + workflow.
- `references/quality-bar.md` — the 10/10 criteria (authoritative).
- `templates/readme-scaffold.md` — README template for auto-fixes.
- `scripts/audit-repo.sh` — repo signal gatherer.
