# job-application

Turn one job description into five ready-to-use application assets: a tailored cover letter, resume bullet tweaks, likely interview questions, a skills-gap analysis, and a 7-day prep plan.

## When to use

- Paste a JD or share a job URL and ask for a cover letter, resume tailoring, interview prep, skills-gap analysis, or a prep plan.

## Guided flow

1. **Hand over the JD** (pasted text or URL) and your resume (pasted text or a file path).
2. The skill produces, in order:
   - **Tailored cover letter** (250–350 words) using `templates/cover-letter.md`.
   - **Resume bullet tweaks** — sharper rewrites that front-load JD keywords (never invents experience).
   - **Likely interview questions** — 6 technical + 4 behavioral, each with a "what they're really checking" hint.
   - **Skills-gap analysis** — JD requirements you don't cover, tagged `[learnable-quickly]` / `[stretch]` / `[blocking]`.
   - **7-day prep plan** — day-by-day study, a mock question, one resume tweak.
3. **Log it** — appends a row to `templates/job-applications-log.md` (status `drafted`).

## Rules

- Never invents employers, metrics, or experience — only rephrases what you have.
- Drafts only; never auto-submits an application.

## Files

- `SKILL.md` — router + workflow.
- `templates/cover-letter.md`, `templates/job-applications-log.md`.
