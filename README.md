# agent-skills

![CI](https://github.com/theraihanrakibb/agent-skills/actions/workflows/ci.yml/badge.svg)

A portable collection of AI-agent skills for writing, job hunting, resumes, portfolio audits, commit/PR drafting, AI-infra contribution, and social-media content — plus a **CodeBuddy Code plugin** that bundles them with slash commands and a git-commit guard, and a **full-stack web UI** (FastAPI + React) that wraps every skill as an HTTP endpoint. Each skill is a self-contained folder with a `SKILL.md` that any compatible agent can discover and load. No branding, no lock-in — drop the folders you want into your agent and go.

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

## Install the skills anywhere

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

## Plugin (CodeBuddy Code)

The repo doubles as a CodeBuddy Code plugin (`plugin.json` in [`.codebuddy-plugin/`](.codebuddy-plugin/)). It bundles the five workflow skills above as **slash commands** plus a **PreToolUse commit guard** that blocks AI-generation footers and nudges Conventional Commits.

| Slash command | What it does |
|---|---|
| `/agent-skills:audit-portfolio` | Score public repos against a 10/10 quality bar; output a fix-plan. |
| `/agent-skills:apply <jd>` | Cover letter, resume tweaks, interview Qs, skills-gap analysis, 7-day prep plan. |
| `/agent-skills:pr-draft` | Conventional Commit message + PR description + changelog from staged diff. |
| `/agent-skills:ai-infra-helper` | Navigate SGLang/vLLM-style repos; reminds fork-PR CI behavior; drafts PRs. |
| `/agent-skills:social <idea>` | One idea → 6 platform drafts (FB/IG/YouTube/X/LinkedIn/Gmail) + content calendar. |

**Quick dev/test install**

```bash
cc --plugin-dir /path/to/agent-skills
```

Hooks load at session start; run `/hooks` to verify. For a persistent install, use `scripts/sync-to-cache.sh` and register the plugin in `~/.codebuddy/installed_plugins.json` (plugin id `agent-skills@local`), then enable it in `~/.codebuddy/settings.json` → `enabledPlugins`.

## Website (FastAPI + React)

A full-stack web UI for the five workflow skills lives in [`website/`](website). See [`website/README.md`](website/README.md) for full instructions.

```bash
# backend
cd website/backend && pip install -r requirements.txt && uvicorn main:app --reload --port 8000
# frontend (separate terminal)
cd website/frontend && npm install && npm run dev
```

App at http://localhost:5173, API docs at http://localhost:8000/docs. One-command full stack:

```bash
cd website && docker compose up --build   # app :8080, API :8000
```

Deploy: frontend → Vercel, backend → Fly.io. Steps in [`website/DEPLOY.md`](website/DEPLOY.md).

## How the skills guide you

Every skill runs as a short, interactive flow: it asks for what it needs, shows its work, and waits for your approval before any action that changes something (e.g., committing, submitting). See each skill's `README.md` for the full walkthrough.

## Safety

- `job-hunt` and `social-media` treat untrusted input as data, never instructions, and never auto-submit or auto-post.
- `portfolio-audit` and `pr-draft` never commit, push, or amend without explicit confirmation.
- The plugin's commit guard only blocks, never rewrites, your commits.

## Validation

Every push runs CI that:

- checks each skill ships a `SKILL.md` (with `name` + `description` frontmatter) and a `README.md`;
- compiles the bundled Python tools (`job-hunt/tools/`) and runs their unit tests;
- syntax-checks the bundled shell scripts (`bash -n`) and runs `shellcheck` on the plugin `scripts/` + `hooks/`;
- validates the JSON schemas under `resume/references/` and the plugin manifests (`.codebuddy-plugin/plugin.json`, `hooks/hooks.json`);
- runs the **website backend** tests (`website/backend/tests/`) after `ruff check`;
- builds the **website frontend** (`website/frontend` `npm run build`).

## License & attribution

MIT. Upstream sources: `humanizer` (Wikipedia "Signs of AI writing"), `job-hunt` (job-application-assistant + job-scraper + upskill), `resume` (resume-review + resume-polish), and the `toolkit-skills` collection (portfolio-audit, job-application, pr-draft, ai-infra-helper, social-media). The plugin manifest and website were consolidated here from `toolkit-skills`.
