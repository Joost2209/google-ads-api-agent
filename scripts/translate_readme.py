#!/usr/bin/env python3
"""Translate README.md while keeping fenced code blocks verbatim."""

from __future__ import annotations

import argparse
import re
import time
import unicodedata
from pathlib import Path

from deep_translator import GoogleTranslator

HEADER_LINE_COUNT = 8


def split_fenced_blocks(text: str) -> list[str]:
    parts: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        j = text.find("```", i)
        if j < 0:
            parts.append(text[i:])
            break
        parts.append(text[i:j])
        k = text.find("```", j + 3)
        if k < 0:
            parts.append(text[j:])
            break
        parts.append(text[j : k + 3])
        i = k + 3
    return parts


def github_heading_slug(text: str) -> str:
    t = text.strip().lower()
    t = "".join(ch for ch in unicodedata.normalize("NFKD", t) if not unicodedata.combining(ch))
    t = re.sub(r"[^\w\s\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af\u0400-\u04ff-]", "", t, flags=re.UNICODE)
    t = re.sub(r"\s+", "-", t.strip())
    t = re.sub(r"-+", "-", t)
    return t.strip("-")


def translate_hunks(text: str, target: str, sleep_s: float = 0.12) -> str:
    if not text.strip():
        return text
    tr = GoogleTranslator(source="en", target=target)
    n = 4200
    i = 0
    out: list[str] = []
    while i < len(text):
        chunk = text[i : i + n]
        if len(chunk) == n:
            cut = chunk.rfind("\n")
            if cut != -1 and cut > 800:
                chunk = chunk[: cut + 1]
        if not chunk.strip():
            out.append(chunk)
            i += len(chunk)
            continue
        try:
            translated = tr.translate(chunk)
        except Exception:
            time.sleep(2.5)
            translated = tr.translate(chunk)
        if not translated:
            translated = chunk
        out.append(translated)
        i += len(chunk)
        time.sleep(sleep_s)
    return "".join(out)


def translate_plain(text: str, target: str) -> str:
    return translate_hunks(text, target)


def postprocess_glued_fences(md: str) -> str:
    md = re.sub(r"^(##+[^\n`]+?)```([A-Za-z0-9_]*)$", r"\1\n\n```\2", md, flags=re.MULTILINE)
    md = re.sub(r"([:：])\s*```", r"\1\n\n```", md)
    md = re.sub(r"(\*\*[^*\n]+:\*\*)\s*```", r"\1\n\n```", md)
    md = re.sub(r"```(\*\*)", r"```\n\n\1", md)
    md = re.sub(r"(\S)```(\n-{3,})", r"\1\n```\2", md)
    return md


def postprocess_glued_headings(md: str) -> str:
    """Put headings back on their own line when MT glued them to table rows or sentences."""
    md = re.sub(r"(\|)\s*(#{2,6}\s+)", r"\1\n\n\2", md)
    md = re.sub(r"([.!?:。])\s*(#{2,6}\s+)", r"\1\n\n\2", md)
    return md


def rebuild_toc(md: str, toc_title_pattern: str) -> str:
    headings: list[tuple[int, str]] = []
    for m in re.finditer(r"^(#{2,3})\s+(.+)$", md, flags=re.MULTILINE):
        level = len(m.group(1))
        title = m.group(2).strip()
        headings.append((level, title))

    if not headings:
        return md

    try:
        toc_idx = next(i for i, (_, t) in enumerate(headings) if t == toc_title_pattern)
    except StopIteration:
        return md

    body_headings = headings[toc_idx + 1 :]
    toc_lines = ["", "## " + toc_title_pattern, ""]
    for level, title in body_headings:
        slug = github_heading_slug(title)
        indent = "  " if level >= 3 else ""
        toc_lines.append(f"{indent}- [{title}](#{slug})")
    toc_lines.append("")
    toc_lines.append("---")

    m = re.search(
        r"^##\s+" + re.escape(toc_title_pattern) + r"\s*\n(?:.*\n)*?^---\s*$",
        md,
        flags=re.MULTILINE,
    )
    if not m:
        return md
    new_toc = "\n".join(toc_lines) + "\n"
    return md[: m.start()] + new_toc + md[m.end() + 1 :]


def overlay_shared_header(dst: str, header_lines: list[str]) -> str:
    dl = dst.splitlines(keepends=True)
    if len(dl) < HEADER_LINE_COUNT + 1:
        return dst
    return "".join(header_lines[:HEADER_LINE_COUNT]) + "".join(dl[HEADER_LINE_COUNT:])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("outfile", type=Path)
    ap.add_argument("--toc-title", required=True)
    args = ap.parse_args()

    root = Path(__file__).resolve().parents[1]
    src = (root / "README.md").read_text(encoding="utf-8")
    header_lines = src.splitlines(keepends=True)[:HEADER_LINE_COUNT]

    pieces = split_fenced_blocks(src)
    out: list[str] = []
    for idx, piece in enumerate(pieces):
        if idx % 2 == 1:
            out.append(piece)
        else:
            out.append(translate_plain(piece, args.target))
    text = "".join(out)
    text = postprocess_glued_fences(text)
    text = postprocess_glued_headings(text)
    text = rebuild_toc(text, args.toc_title)
    text = overlay_shared_header(text, header_lines)
    args.outfile.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
