# social-media

Repurpose one idea into platform-ready drafts for Facebook, Instagram, YouTube, X/Twitter, LinkedIn, and Gmail — plus a content-calendar entry. Drafting only; never auto-posts.

## When to use

- "draft a post for facebook", "write an instagram caption", "youtube title and description", "tweet this", "linkedin post", "gmail subject and body", "content calendar", "hashtag ideas".

## Guided flow

1. **Give the idea + tone.** Provide the idea; if tone isn't specified, the skill asks: `professional` / `casual` / `promotional` / `educational`.
2. **Per-platform drafts** (per `references/platform-specs.md`):
   - **Facebook** — 1–2 engaging sentences + emoji.
   - **Instagram** — caption ≤ 2200 chars, hook first line, CTA, 10–15 hashtags.
   - **YouTube** — title ≤ 100 chars, description with summary + timestamps + tags.
   - **X/Twitter** — ≤ 280 chars; optional thread.
   - **LinkedIn** — hook + 3–5 short paragraphs or bullets, ends with a question.
   - **Gmail** — subject ≤ 60 chars, greeting + 2–3 paragraphs + CTA + signature.
3. **Hashtags** for IG + YouTube (mix broad/niche; avoid banned tags).
4. **Content calendar** — runs `scripts/init-calendar.sh`, then appends a row to `templates/content-calendar.md`.
5. **You get all 6 drafts** in copy-paste blocks.

## Rules

- No auto-posting — drafts only, no OAuth/API to any platform.
- No fabricated stats, quotes, or testimonials.
- Respects each platform's length and convention limits.

## Files

- `SKILL.md` — router + workflow.
- `references/platform-specs.md` — char limits, tone presets.
- `templates/content-calendar.md`.
- `scripts/init-calendar.sh` — calendar initializer.
