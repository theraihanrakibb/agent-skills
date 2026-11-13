"""Unit tests for ``job-hunt/tools/fetch_page.py``.

Covers the pure, network-free behaviour that the module docstring says is
"pinned by tests/test_fetch_page.py". Network paths (actual GETs) are not
exercised here — those need live sites and are gated by robots.txt anyway.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parent.parent / "tools"
sys.path.insert(0, str(TOOLS))

import fetch_page  # noqa: E402


def test_strip_tags_removes_noise() -> None:
    html = (
        "<p>Hello <b>world</b></p>"
        "<!-- a comment -->"
        "<script>track()</script>"
        "<style>.x{}</style>"
    )
    out = fetch_page.strip_tags(html, 1000)
    assert "Hello" in out and "world" in out
    assert "a comment" not in out
    assert "track()" not in out
    assert ".x{}" not in out


def test_strip_tags_respects_limit() -> None:
    out = fetch_page.strip_tags("<p>" + "x" * 200 + "</p>", 10)
    assert len(out) <= 10


def test_default_out_lives_in_temp() -> None:
    out = fetch_page._default_out("https://example.com/a")
    assert out.parent == Path(tempfile.gettempdir())


def test_inside_repo_detection(tmp_path: Path) -> None:
    # A path under the repo root is detected.
    assert fetch_page._inside_repo(fetch_page.ROOT / "somefile.md") is True
    # A path in the system temp dir is not.
    assert fetch_page._inside_repo(tmp_path / "x.html") is False


def test_non_http_scheme_is_rejected() -> None:
    rc = fetch_page.main(["ftp://example.com"])
    assert rc == 2
