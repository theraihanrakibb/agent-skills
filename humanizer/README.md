# humanizer

Turn AI-sounding text into text that reads like a person wrote it — **without changing what it says**. It is a writing aid, not a fact-checker: it edits prose only and never invents details you don't have.

## When to use

Hand the skill text that feels generic, salesy, or "chatbot-y": drafts, documentation, blog posts, essays, commit/PR descriptions, cover letters. Trigger phrases: *"humanize this"*, *"make it sound human"*, *"remove the AI tone"*, *"fix the AI writing"*.

## What it fixes

26 concrete patterns, grouped so you can see the logic:

- **Staging instead of stating** — "not X but Y", one-line closers, sayings that sound deep, staged run-ups, arguing with no one.
- **Rhythm by rule** — forced triads, repeated openings, em-dashes everywhere, stacked qualifiers, hyphenated pairs, passive voice.
- **Inflation & borrowed authority** — overused AI words, inflated significance, vague links, sales language, unnamed "experts".
- **Formatting by rule** — bold-as-decoration, decorative headings, curly quotes.
- **Chat & draft leftovers** — chatbot residue, knowledge-cutoff disclaimers, text that describes itself.
- **Wrong reader** — re-explaining context the reader already has.

The full pattern catalog with before/after examples lives in [`SKILL.md`](SKILL.md).

## Guided flow

1. **Paste or point.** Paste the text, or name a file (e.g. `humanize my draft.md`). For a file, the skill reads the whole thing from disk first — even if you wrote it earlier this session.
2. **It marks the tells.** Every flagged pattern is noted, strongest first. It looks at paragraph shape too, not just sentences.
3. **It drafts.** The rewrite keeps every fact and your meaning; it only changes wording, structure, and rhythm. Where text is generic, it adds a specific true detail; where it lacks a detail, it asks or writes a simpler sentence.
4. **It checks.** It verifies no fact, number, name, date, quote, or claim was dropped, then re-scans for the patterns that survive rewrites (contrasts, closers, triads, dashes, bold labels).
5. **You get three things:** the cleaned draft, a short list of any patterns that remain, and the final rewrite.

## Rules it follows

- **Keeps your voice.** If you give a writing sample, the rewrite matches it — sentence length, word choice, punctuation, and even your dash usage.
- **Never touches non-prose.** In file mode it leaves code blocks, inline code, commands, paths, YAML metadata, data, and link targets exactly as they are.
- **Embedded mode.** When another task (a PR, commit message, or document) uses this skill, it returns only the final text.

## Limitations

- Edits prose only; it won't invent facts.
- It is a stylistic aid, not a source of truth — pair it with a fact-check when accuracy matters.
