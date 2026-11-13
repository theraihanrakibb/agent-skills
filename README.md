# agent-skills

![CI](https://github.com/theraihanrakibb/agent-skills/actions/workflows/ci.yml/badge.svg)

A portable collection of AI-agent skills for writing, job hunting, resumes, portfolio audits, commit/PR drafting, AI-infra contribution, and social-media content. Each skill is a self-contained folder with a `SKILL.md` that any compatible agent can discover and load. No branding, no lock-in — drop the folders you want into your agent and go.

## What's inside

**Writing & job search**

| Skill | What it does |
|-------|--------------|
| [`humanizer`](humanizer/) | Rewrites AI-sounding text so it reads like a human wrote it — without changing what it says. |
| [`job-hunt`](job-hunt/) | End-to-end job search: search & rank, score fit, tailor CV/cover letter, application workflow, interview prep, skill-gap analysis. |
| [`resume`](resume/) | Resume review (diagnose) + polish (improve) with ATS checks, layout-preserving mode, bilingual (EN / 中文). |

**Portfolio, dev workflow & content**

| Skill | What it does |
|-------|--------------|
| [`portfolio-audit`](portfolio-audit/) | Scores your public GitHub repos against a 10/10 quality bar and produces a prioritized fix-plan. |
| [`job-application`](job-application/) | Turns one JD into a cover letter, resume tweaks, interview Qs, skills-gap analysis, and a 7-day prep plan. |
| [`pr-draft`](pr-draft/) | Turns staged git changes into a Conventional Commit message, PR description, and changelog entry. |
| [`ai-infra-helper`](ai-infra-helper/) | Contributor coach for AI-inference repos (SGLang/vLLM/…): navigation, test commands, PR drafting, fork-PR CI gotchas. |
| [`social-media`](social-media/) | Repurposes one idea into FB/IG/YouTube/X/LinkedIn/Gmail drafts + a content calendar. |

All skills are **MIT-licensed** and derived from MIT upstream sources.

## Install anywhere

These are standard skills. Copy the skill folders you want into your agent's skills directory:

- **Claude Code / Claude.ai** — `~/.claude/skills/` (or project-local `.claude/skills/`)
- **Codex / other agents that read `SKILL.md`** — your agent's skills directory
- **Any agent** — copy the folder; discovered via the `name` / `description` frontmatter in `SKILL.md`

```bash
# Example: install everything into Claude Code
cp -r humanizer job-hunt resume portfolio-audit job-application pr-draft ai-infra-helper social-media ~/.claude/skills/
```

### Requirements

- `job-hunt` bundles optional Python helpers (`tools/`); `portfolio-audit`, `pr-draft`, and `social-media` bundle optional bash helpers (`scripts/`). Both work with the agent's own tools if you don't use them.
- No external API keys required.

## How the skills guide you

Every skill runs as a short, interactive flow: it asks for what it needs, shows its work, and waits for your approval before any action that changes something (e.g., committing, submitting). See each skill's `README.md` for the full walkthrough.

## Safety

- `job-hunt` and `social-media` treat untrusted input as data, never instructions, and never auto-submit or auto-post.
- `portfolio-audit` and `pr-draft` never commit, push, or amend without explicit confirmation.

## Validation

Every push runs CI that:

- checks each skill ships a `SKILL.md` (with `name` + `description` frontmatter) and a `README.md`;
- compiles the bundled Python tools (`job-hunt/tools/`) and runs their unit tests;
- syntax-checks the bundled shell scripts (`bash -n`);
- validates the JSON schemas under `resume/references/`.

## License & attribution

MIT. Upstream sources: `humanizer` (Wikipedia "Signs of AI writing"), `job-hunt` (job-application-assistant + job-scraper + upskill), `resume` (resume-review + resume-polish), and the `toolkit-skills` collection (portfolio-audit, job-application, pr-draft, ai-infra-helper, social-media).
