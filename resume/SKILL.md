---
name: resume
license: MIT
description: >
  Resume review and optimization in one skill: diagnose quality (expression, structure,
  credibility, JD match, truthfulness, ATS parseability) and polish/improve an existing
  resume while preserving facts and, optionally, a designed PDF layout. Merged from
  resume-review + resume-polish. Triggers on: review my resume, rate my resume, check
  my resume, polish my resume, optimize my resume, improve this resume, rewrite for a job.
allowed-tools: Read, Glob, Grep, WebFetch, WebSearch, Edit, Write, AskUserQuestion
---

# Resume (merged: review + polish)

One skill that does both: **review** (diagnose, never edit) and **polish** (improve, never fabricate). It is the consolidation of the upstream `resume-review` and `resume-polish` skills, with additions:

- **ATS / parseability check** (review): when you supply extracted PDF text (`pdfText`), it flags broken/split tokens, stray hyphens, ligature artifacts, and bilingual keyword duplication.
- **Internal number-consistency + Summary-to-body traceability** (review): credibility now has two mandatory sub-checks.
- **Layout-preserving mode** (polish): when the resume is a designed PDF you want kept intact, polish emits only before→after fragments, never a full rewrite.
- **Bilingual (EN + 中文) handling** in both modes.

## Which mode to run

| User says | Mode | Full instructions |
|---|---|---|
| "review my resume", "rate this", "what's wrong" | **review** | `references/review_SKILL.md` (+ `references/review_schema.json`) |
| "polish my resume", "optimize", "improve", "rewrite for X" | **polish** | `references/polish_SKILL.md` (+ `references/polish_schema.json`) |

Load the referenced file for the full workflow, dimensions, scoring, and output contract. This file is only the router.

## Key rules (both modes)

1. **review = diagnosis only.** Never rewrite, never restructure, never generate. Output JSON per `references/review_schema.json`.
2. **polish = improve in place.** Never fabricate numbers, tech stacks, hardware models, journal names, dates, or experiences. Edits trace to the original or `sourceTexts`.
3. **Preserve a designed PDF.** If the user has a custom layout or sets `preserveLayout`, polish may NOT emit a full markdown resume — only a compact before→after diff plus a note to apply edits in their source.
4. **Bilingual parity.** If the resume is EN + 中文, every change is mirrored in both languages, not just the chosen `language`.
5. **ATS is advisory in polish.** polish outputs Markdown, so it cannot fix PDF text-layer breaks; it must list any discovered text-layer issues in `suggestions` instead.
6. **Never submit or regenerate the PDF.** These skills produce text/diffs only.

## Typical loop

`review` → fix issues with `polish` (optionally `preserveLayout` to keep the PDF) → `review` again to confirm the score rose. Supply `jd` for targeted optimization, `sourceTexts` for anti-hallucination checks, and `pdfText` for the ATS check.
