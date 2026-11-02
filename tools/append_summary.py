#!/usr/bin/env python3
"""Append one illustrated chapter summary to sql_cookbook_summary.html.

The HTML file contains a <!-- NEXT CHAPTER --> marker. This tool inserts a
<section> before that marker, embeds any image tokens used by the fragment,
adds the chapter's recipe map from book_extracts/recipes.json, and updates the
table of contents / progress indicator.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import re
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "sql_cookbook_summary.html"
RECIPES_PATH = ROOT / "book_extracts" / "recipes.json"
IMG_DIR = ROOT / "book_extracts" / "images"

TOKEN_IMAGES = {
    "{{cover}}": ROOT / "book_extracts" / "renders" / "page_001.png",
    "{{lizard}}": IMG_DIR / "xref_97.png",
    "{{scorpion}}": IMG_DIR / "xref_100.png",
    "{{bird}}": IMG_DIR / "xref_2198.png",
    "{{knight}}": IMG_DIR / "xref_3695.png",
    "{{logo}}": IMG_DIR / "xref_112.png",
}


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def embed_tokens(text: str) -> str:
    for token, path in TOKEN_IMAGES.items():
        if token in text:
            text = text.replace(token, data_uri(path))
    return text


def recipe_items(chapter_prefix: str) -> list[str]:
    recipes = json.loads(RECIPES_PATH.read_text(encoding="utf-8"))
    key = next((k for k in recipes if k.startswith(chapter_prefix)), None)
    if not key:
        return []
    items = []
    for recipe in recipes[key]:
        title = recipe["title"]
        if "Summing Up" in title:
            continue
        page = recipe.get("page")
        suffix = f" <span>· p.{page}</span>" if page else ""
        items.append(f"<li>{title}{suffix}</li>")
    return items


def build_section(args: argparse.Namespace, body: str) -> str:
    body = embed_tokens(body)
    recipe_html = ""
    items = recipe_items(args.prefix)
    if items:
        recipe_html = (
            '<details class="recipe-map" open>'
            "<summary>Recipe map</summary>"
            f"<ul>{''.join(items)}</ul>"
            "</details>"
        )
    pic_html = ""
    if args.pic:
        pic_html = (
            f'<div class="chapter-pic pic-{args.pic}" role="img" '
            f'aria-label="{args.pic} illustration from the book"></div>'
        )
    return f"""
<section class="chapter" id="{args.id}">
  <div class="chapter-head">
    <div>
      <div class="chapter-kicker">{args.kicker}</div>
      <h2>{args.title}</h2>
      <p class="lede">{args.lede}</p>
    </div>
    {pic_html}
  </div>
  {body}
  {recipe_html}
</section>
"""


def update_nav(soup: BeautifulSoup, chapter_id: str) -> None:
    li = soup.select_one(f'li[data-target="{chapter_id}"]')
    if li is not None and "done" not in (li.get("class") or []):
        classes = li.get("class") or []
        classes.append("done")
        li["class"] = classes
    done = len(soup.select("section.chapter"))
    label = soup.find(id="progress-label")
    if label is not None:
        label.string = f"{done} of 16 sections complete"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", required=True, help="Section id, e.g. ch1 or apxa")
    parser.add_argument("--prefix", required=True, help="recipes.json chapter key prefix")
    parser.add_argument("--kicker", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--lede", required=True)
    parser.add_argument("--body", required=True, help="HTML fragment file")
    parser.add_argument("--pic", choices=["lizard", "scorpion", "bird", "knight"], default="")
    args = parser.parse_args()

    html = HTML_PATH.read_text(encoding="utf-8")
    if f'id="{args.id}"' in html:
        raise SystemExit(f"Section {args.id} already exists")
    if "<!-- NEXT CHAPTER -->" not in html:
        raise SystemExit("NEXT CHAPTER marker not found")

    body = Path(args.body).read_text(encoding="utf-8")
    section_html = build_section(args, body)

    soup = BeautifulSoup(html, "html.parser")
    marker = next(
        (n for n in soup.find_all(string=True) if isinstance(n, NavigableString) and "NEXT CHAPTER" in n),
        None,
    )
    if marker is None:
        raise SystemExit("NEXT CHAPTER marker not found after parsing")

    section_soup = BeautifulSoup(section_html, "html.parser").find("section")
    if section_soup is None:
        raise SystemExit("Failed to parse generated section")
    marker.insert_before(section_soup)
    update_nav(soup, args.id)

    HTML_PATH.write_text(str(soup), encoding="utf-8")
    print(f"Appended {args.id} -> {HTML_PATH} ({HTML_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
