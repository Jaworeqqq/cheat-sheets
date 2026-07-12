#!/usr/bin/env python3
"""MCP server exposing the cheat-sheets repo as searchable tools + resources.

Any MCP-capable client (Claude Desktop, IDE extensions, etc.) can search the
cheat sheets, pull a full sheet, or extract a single section — using the YAML
frontmatter (tags, mitre, platform, category, difficulty) for structured filters.

Run:  python server.py         (stdio transport)
Env:  CHEATSHEETS_DIR to override the repo root (defaults to the parent dir).
"""
from __future__ import annotations

import os
from pathlib import Path

import yaml
from mcp.server.fastmcp import FastMCP

REPO_ROOT = Path(os.environ.get("CHEATSHEETS_DIR", Path(__file__).resolve().parent.parent)).resolve()

mcp = FastMCP("cheat-sheets")


# ---------------------------------------------------------------------------
# Index
# ---------------------------------------------------------------------------
def _parse_frontmatter(text: str) -> tuple[dict, str]:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                meta = {}
            return (meta if isinstance(meta, dict) else {}), parts[2]
    return {}, text


def _as_list(v) -> list[str]:
    if v is None:
        return []
    if isinstance(v, list):
        return [str(x) for x in v]
    return [str(v)]


def build_index() -> list[dict]:
    items: list[dict] = []
    for path in sorted(REPO_ROOT.rglob("*.md")):
        rel = path.relative_to(REPO_ROOT).as_posix()
        # Skip repo meta docs; keep only cheat sheets and section indexes.
        if rel.startswith((".github/", "_templates/", "mcp/")):
            continue
        if path.name in {"README.md", "CONTRIBUTING.md"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        meta, body = _parse_frontmatter(text)
        section = rel.split("/", 1)[0]
        items.append(
            {
                "path": rel,
                "title": str(meta.get("title") or path.stem),
                "section": section,
                "category": str(meta.get("category") or section),
                "tags": _as_list(meta.get("tags")),
                "mitre": _as_list(meta.get("mitre")),
                "platform": str(meta.get("platform") or ""),
                "difficulty": str(meta.get("difficulty") or ""),
                "body": body,
                "_hay": "\n".join(
                    [
                        str(meta.get("title") or ""),
                        " ".join(_as_list(meta.get("tags"))),
                        " ".join(_as_list(meta.get("mitre"))),
                        str(meta.get("category") or section),
                        body,
                    ]
                ).lower(),
            }
        )
    return items


INDEX = build_index()


def _score(item: dict, terms: list[str]) -> int:
    title = item["title"].lower()
    tags = " ".join(item["tags"]).lower()
    mitre = " ".join(item["mitre"]).lower()
    cat = item["category"].lower()
    body = item["_hay"]
    score = 0
    for t in terms:
        if t in title:
            score += 10
        if t in tags or t in mitre:
            score += 5
        if t in cat:
            score += 3
        if t in body:
            score += 1
    return score


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------
@mcp.tool()
def search_cheatsheets(
    query: str,
    section: str = "",
    platform: str = "",
    tag: str = "",
    mitre: str = "",
    limit: int = 10,
) -> str:
    """Search cheat sheets by keyword, ranked by relevance.

    Optional filters (exact-ish match on frontmatter):
      section  – top-level folder, e.g. "red-team", "blue-team", "cloud-security"
      platform – e.g. "aws", "windows", "web", "linux"
      tag      – a frontmatter tag, e.g. "kerberos", "container"
      mitre    – an ATT&CK technique id, e.g. "T1558"
    Returns a ranked list of path · title · snippet.
    """
    terms = [t for t in query.lower().split() if t]
    results = []
    for item in INDEX:
        if section and item["section"] != section:
            continue
        if platform and platform.lower() not in item["platform"].lower():
            continue
        if tag and tag.lower() not in [t.lower() for t in item["tags"]]:
            continue
        if mitre and mitre.lower() not in [m.lower() for m in item["mitre"]]:
            continue
        s = _score(item, terms) if terms else 1
        if s > 0:
            results.append((s, item))
    results.sort(key=lambda r: r[0], reverse=True)
    if not results:
        return f"No cheat sheets matched '{query}'" + (f" (filters applied)." if any([section, platform, tag, mitre]) else ".")
    lines = [f"Found {len(results)} match(es); showing top {min(limit, len(results))}:\n"]
    for s, item in results[: max(1, limit)]:
        snippet = _first_snippet(item["body"], terms)
        lines.append(f"- **{item['title']}**  ·  `{item['path']}`  ·  [{item['category']}]")
        if item["mitre"]:
            lines[-1] += f"  ·  {', '.join(item['mitre'])}"
        if snippet:
            lines.append(f"    {snippet}")
    lines.append("\nUse get_cheatsheet(path) for the full sheet.")
    return "\n".join(lines)


def _first_snippet(body: str, terms: list[str], width: int = 160) -> str:
    low = body.lower()
    pos = -1
    for t in terms:
        pos = low.find(t)
        if pos != -1:
            break
    if pos == -1:
        # fall back to the TL;DR line
        for line in body.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                return line[:width]
        return ""
    start = max(0, pos - 40)
    return body[start : start + width].replace("\n", " ").strip()


@mcp.tool()
def get_cheatsheet(path: str) -> str:
    """Return the full markdown of a cheat sheet by its repo-relative path.

    Example path: "red-team/active-directory/kerberoasting.md"
    """
    target = (REPO_ROOT / path).resolve()
    if REPO_ROOT not in target.parents or target.suffix != ".md" or not target.is_file():
        return f"Not found or not allowed: {path}"
    return target.read_text(encoding="utf-8", errors="replace")


@mcp.tool()
def get_section(path: str, heading: str) -> str:
    """Return a single markdown section (e.g. 'Detection', 'Mitigation') of a cheat sheet.

    Matches a '## <heading>' line (case-insensitive, prefix match). Great for pulling
    just the Detection or Mitigation guidance for a technique.
    """
    target = (REPO_ROOT / path).resolve()
    if REPO_ROOT not in target.parents or target.suffix != ".md" or not target.is_file():
        return f"Not found or not allowed: {path}"
    _, body = _parse_frontmatter(target.read_text(encoding="utf-8", errors="replace"))
    want = heading.strip().lower().lstrip("#").strip()
    out: list[str] = []
    capturing = False
    for line in body.splitlines():
        if line.startswith("## "):
            title = line[3:].strip().lower()
            if capturing:
                break
            capturing = title.startswith(want) or want in title
            if capturing:
                out.append(line)
            continue
        if capturing:
            out.append(line)
    return "\n".join(out).strip() or f"Section '{heading}' not found in {path}"


@mcp.tool()
def list_sections() -> str:
    """List the top-level sections and how many cheat sheets each contains."""
    counts: dict[str, int] = {}
    for item in INDEX:
        counts[item["section"]] = counts.get(item["section"], 0) + 1
    lines = [f"{n:>4}  {s}" for s, n in sorted(counts.items(), key=lambda x: -x[1])]
    lines.append(f"\nTotal: {len(INDEX)} cheat sheets across {len(counts)} sections.")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Resources
# ---------------------------------------------------------------------------
@mcp.resource("cheatsheet://index")
def index_resource() -> str:
    """A compact index of every cheat sheet: path · title · tags."""
    lines = [f"{i['path']} — {i['title']} [{', '.join(i['tags'])}]" for i in INDEX]
    return "\n".join(lines)


@mcp.resource("cheatsheet://{path}")
def sheet_resource(path: str) -> str:
    """Read a cheat sheet by repo-relative path as a resource."""
    return get_cheatsheet(path)


if __name__ == "__main__":
    mcp.run()
