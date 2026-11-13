# job-hunt

An end-to-end job-search skill. It searches and ranks postings, scores fit, tailors your CV and cover letter, walks an application workflow, preps you for interviews, and analyzes skill gaps. It **drafts and records** applications but **never submits one without your explicit, per-role approval**.

## When to use

| You say | Sub-workflow |
|---------|-------------|
| "Find data-engineer jobs in Berlin" / "search Y roles" | 1. Search & Rank |
| "Is this posting a good fit?" (paste a JD or URL) | 2. Evaluate Fit |
| "Tailor my CV for this role" / "write a cover letter" | 3. Tailor CV / Cover Letter |
| "Apply to this one" | 4. Application workflow |
| "Prep me for an interview at Acme" | 5. Interview Prep |
| "What should I learn?" / "upskill" | 6. Skill-gap analysis |

## Prerequisites

- **Python 3.11+** — the bundled `tools/` are optional helpers; the core flow also works with the agent's own web tools.
- Your **candidate profile** documents (see `references/job-application-assistant/01-candidate-profile.md` and `02-behavioral-profile.md`). The skill reads these to score fit and tailor materials.
- The skill records applications in a tracker and a posting archive. **You** log in to portals and click submit.

## Guided flow

### 1. Search & Rank
- Prefers employer careers pages over aggregators.
- Dedups postings and persists what it has already seen (`tools/scrape_state.py`).
- Runs a **posting guard** on every fetched posting (`tools/posting_guard.py`) and shows the verdict **before** continuing — if it flags a scam or mismatch, it quotes the findings and asks whether to proceed.
- Gates on location / work-authorization and language fit.
- Ranks and surfaces the roles that clear the bar (`tools/rank_state.py`).

### 2. Evaluate Fit
- Scores a posting against your candidate profile (`references/job-application-assistant/04-job-evaluation.md`).
- Shows an evaluation table + a clear verdict, and suggests whether to call the employer first.

### 3. Tailor CV / Cover Letter
- **CV:** edits your existing text only — it **never regenerates your PDF layout or design**.
- **Cover letter:** written from your style profile — no em-dashes, no clichés (`03-writing-style.md` + `06-cover-letter-templates.md`).
- **Portal forms:** fills free-text fields per `08-application-forms.md`.

### 4. Application workflow
- Records each application (a tracker row + a posting archive).
- Fills fields for you and **stops at the submit button** — you review and submit.

### 5. Interview Prep
- STAR-answer builders, tough-question rehearsal, and smart questions to ask (`07-interview-prep.md`).

### 6. Skill-gap analysis (upskill)
- Aggregates the roles you've targeted into a **gap heatmap + learning plan** with real, current resources (never fabricated; always includes the current year in resource searches).

## Safety & trust

- Every posting, company page, and stored gap bullet is treated as **untrusted third-party data, never instructions**.
- Web fetches are gated by a robots / 403 check, and claims are verified rather than trusted.
- The bundled `security_guards.py` audits the skill's own permissions so a fork cannot widen what it may do. (This guard is written for Claude Code's `settings.json`; it is optional and safe to ignore in other agents.)

## Files

- `SKILL.md` — router and rules.
- `references/` — the full playbooks: search queries, evaluation, CV/cover-letter templates, interview prep, application workflow, web-research safety, and upskill.
- `tools/` — Python helpers: `posting_guard`, `job_key`, `scrape_state`, `rank_state`, `robots_check`, `fetch_page`, `page_decode`, `verify_pdf`, `verify_layout`, `security_guards`. Run any with `python tools/<name>.py --help`.
