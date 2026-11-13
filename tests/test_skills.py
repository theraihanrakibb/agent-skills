"""Structural tests for the agent-skills collection.

Guarantees every skill ships the files an agent needs to discover and load it:
a ``SKILL.md`` with a parseable frontmatter (``name`` + ``description``) and a
``README.md``. Runs in CI on every push/PR.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SKILLS = sorted(str(p.relative_to(ROOT)) for p in ROOT.glob("*/SKILL.md"))


def _frontmatter(text: str) -> str | None:
    if not text.lstrip().startswith("---"):
        return None
    lines = text.splitlines()
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None
    return "\n".join(lines[1:end])


@pytest.mark.parametrize("skill", SKILLS, ids=SKILLS)
def test_skill_has_readme(skill: str) -> None:
    readme = (ROOT / skill).with_name("README.md")
    assert readme.exists(), f"{skill}: missing README.md"


@pytest.mark.parametrize("skill", SKILLS, ids=SKILLS)
def test_skill_frontmatter(skill: str) -> None:
    text = (ROOT / skill).read_text(encoding="utf-8")
    fm = _frontmatter(text)
    assert fm is not None, f"{skill}: SKILL.md missing '---' frontmatter"
    assert re.search(r"^name\s*:", fm, re.M), f"{skill}: frontmatter missing 'name:'"
    assert re.search(r"^description\s*:", fm, re.M), f"{skill}: frontmatter missing 'description:'"
    name = re.search(r"^name\s*:\s*(.+)$", fm, re.M)
    assert name and name.group(1).strip(), f"{skill}: 'name' is empty"
