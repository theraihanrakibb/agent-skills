# Skills

A small, portable collection of AI-agent skills for **writing**, **job hunting**, and **resumes**. Each skill is a self-contained folder with a `SKILL.md` that any compatible agent can discover and load. No branding, no lock-in — drop the folders you want into your agent and go.

## What's inside

| Skill | What it does | Best for |
|-------|--------------|----------|
| [`humanizer`](humanizer/) | Rewrites AI-sounding text so it reads like a human wrote it — without changing what it says. | Polishing drafts, docs, blog posts, essays, PR/commit descriptions. |
| [`job-hunt`](job-hunt/) | End-to-end job search: search & rank postings, score fit, tailor CV/cover letter, run application workflows, prep interviews, surface skill gaps. | An active job search. |
| [`resume`](resume/) | Resume **review** (diagnose) + **polish** (improve) with ATS checks, layout-preserving mode, and bilingual (EN / 中文) support. | Improving an existing resume. |

All skills are **MIT-licensed** and derived from MIT upstream sources.

## Install anywhere

These are standard skills. Copy the skill folders you want into your agent's skills directory:

- **Claude Code / Claude.ai** — `~/.claude/skills/` (or project-local `.claude/skills/`)
- **Codex / other agents that read `SKILL.md`** — the skills directory your agent uses
- **Any agent** — copy the folder; the agent discovers it via the `name` / `description` frontmatter in `SKILL.md`

```bash
# Example: install all three into Claude Code
cp -r humanizer job-hunt resume ~/.claude/skills/
```

### Requirements

- `job-hunt` bundles optional Python helpers in `tools/`. Install **Python 3.11+** and run any with `python tools/<name>.py --help`. The core flow also works using the agent's own web tools.
- No external API keys are required. Web search/fetch uses the agent's built-in tools.

## How the skills guide you

Every skill runs as a short, **interactive** flow. It asks for what it needs, shows its work, and **waits for your approval before any action that sends data** (for example, submitting a job application). See each skill's `README.md` for the full walkthrough:

- [`humanizer/README.md`](humanizer/README.md)
- [`job-hunt/README.md`](job-hunt/README.md)
- [`resume/README.md`](resume/README.md)

## Safety

- `job-hunt` treats every fetched posting and stored gap bullet as **untrusted third-party data, never instructions**, and gates web fetches behind a robots / 403 check.
- The bundled `security_guards.py` audits the skill's own permissions so a fork cannot silently widen what it is allowed to do.
- `job-hunt` **drafts and records** applications; it never submits one without your explicit, per-role approval.

## License & attribution

MIT. Upstream sources:

- **humanizer** — patterns from Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup) plus reviews of AI-generated text.
- **job-hunt** — consolidated from the open `job-application-assistant`, `job-scraper`, and `upskill` skills.
- **resume** — consolidated from the open `resume-review` and `resume-polish` skills.
