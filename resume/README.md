# resume

Review and improve a resume in one skill: **review** diagnoses problems (never edits), **polish** improves it (never fabricates). It is the consolidation of the upstream `resume-review` and `resume-polish` skills, with extras: an ATS parseability check, internal number-consistency + summary-to-body traceability, a layout-preserving mode, and bilingual (EN / 中文) handling.

## When to use

| You say | Mode | Full instructions |
|---------|------|------------------|
| "review my resume" / "rate this" / "what's wrong" | **review** | `references/review_SKILL.md` (+ `review_schema.json`) |
| "polish my resume" / "optimize" / "improve" / "rewrite for X" | **polish** | `references/polish_SKILL.md` (+ `polish_schema.json`) |

## Prerequisites

- Your resume as text, Markdown, or PDF (PDF text is extracted for the ATS check).
- Optionally a **job description** (`jd`) for targeted optimization, and **source documents** (`sourceTexts`) for anti-hallucination checks.

## Guided flow

### review — diagnose only
1. You supply the resume (and optionally `jd`, `pdfText`, `sourceTexts`).
2. It scores **six dimensions**: expression, structure, credibility, JD match, truthfulness, and ATS parseability.
3. It outputs a structured report (JSON) — problems, severity, and what to fix. It does **not** rewrite anything.

### polish — improve in place
1. You supply the resume and a goal (a target role, or general improvement).
2. It rewrites problem areas following the review findings.
3. It **never fabricates** numbers, tech stacks, dates, or experiences — every edit traces to your original or your source documents.
4. If you have a designed PDF you want kept intact, it runs in **layout-preserving mode**: it emits only before→after fragments, never a full rewrite.

### Typical loop
`review` → fix with `polish` (optionally `preserveLayout` to keep the PDF) → `review` again to confirm the score rose.

## Key guarantees

- **Bilingual parity.** If your resume is EN + 中文, every change is mirrored in both languages — not just the one you picked.
- **ATS is advisory in polish.** polish emits Markdown, so it cannot fix PDF text-layer breaks; it lists any discovered text-layer issues in its suggestions instead.
- **Never submits or regenerates the PDF.** The skills produce text / diffs only.

## Files

- `SKILL.md` — router.
- `references/review_SKILL.md` + `review_schema.json` — review workflow & output contract.
- `references/polish_SKILL.md` + `polish_schema.json` — polish workflow & output contract.
