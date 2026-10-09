#!/usr/bin/env python3
"""Build index.html from the entries and figures.

Usage: python3 build.py

Each Markdown file in entries/ is one question. This script converts the
entries to HTML (inlining any SVG figures they use) and places them, as JSON,
inside template.html. The result, index.html, is a single self-contained page.
No libraries needed beyond the Python standard library.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENTRY_DIR = ROOT / "entries"
TEMPLATE = ROOT / "template.html"
OUTPUT = ROOT / "index.html"

# The sections an entry may have after its options, in page order.
SECTIONS = ["Why it's tempting", "A better picture", "In the classroom",
            "Spotted in the wild", "Going deeper"]
LEVELS = {"junior", "senior"}


def fail(path, message):
    raise SystemExit(f"{path.name}: {message}")


# ---------------------------------------------------------------- reading

def read_entry(path):
    """Split an entry file into its front matter (a dict) and its sections."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not match:
        fail(path, "missing front matter between --- lines")
    meta = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            meta[key.strip()] = value.strip()
    sections = []
    for chunk in re.split(r"^## ", match.group(2), flags=re.M)[1:]:
        heading, _, body = chunk.partition("\n")
        sections.append((heading.strip(), body.strip()))
    return meta, sections


# ---------------------------------------------------------------- Markdown

def inline(text, titles):
    """Inline Markdown: maths, code, quotes, bold, italic and links."""
    kept = []

    def keep(m):
        kept.append(m.group(0))
        return f"\x00{len(kept) - 1}\x00"

    # Set maths and code aside so nothing below touches them.
    text = re.sub(r"\$\$.+?\$\$|\$[^$]+\$|`[^`]+`", keep, text)
    text = html.escape(text, quote=False)
    text = re.sub(r'(^|[\s(\[])"', "\\1\u201c", text).replace('"', "\u201d")
    text = re.sub(r"(^|[\s(\[])'", "\\1\u2018", text).replace("'", "\u2019")
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[\[([\w-]+)(?:\|(.+?))?\]\]",
                  lambda m: entry_link(m, titles), text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)

    def restore(m):
        piece = kept[int(m.group(1))]
        if piece.startswith("`"):
            return f"<code>{html.escape(piece[1:-1], quote=False)}</code>"
        return html.escape(piece, quote=False)

    return re.sub(r"\x00(\d+)\x00", restore, text)


def entry_link(m, titles):
    """[[entry-id]] or [[entry-id|text]] links to another entry."""
    target = m.group(1)
    if target not in titles:
        raise SystemExit(f"Link to unknown entry [[{target}]]")
    return f'<a href="#{target}">{m.group(2) or html.escape(titles[target])}</a>'


def figure(alt, src, caption, titles):
    """Inline an SVG figure so the page stays a single file."""
    path = ROOT / src
    if path.suffix != ".svg" or not path.exists():
        raise SystemExit(f"Figure not found, or not an SVG: {src}")
    svg = re.sub(r"<\?xml.*?\?>|<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S)
    label = html.escape(alt, quote=True)
    # Never draw a figure larger than its own viewBox: one unit, one pixel.
    viewbox = re.search(r'viewBox="[\d.]+ [\d.]+ ([\d.]+) [\d.]+"', svg)
    size = f' style="max-width:{viewbox.group(1)}px"' if viewbox else ""
    svg = svg.strip().replace("<svg", f'<svg class="fig" role="img" aria-label="{label}"{size}', 1)
    cap = f"<figcaption>{inline(caption, titles)}</figcaption>" if caption else ""
    return f"<figure>{svg}{cap}</figure>"


def render(text, titles):
    """Block Markdown: paragraphs, lists, figures, display maths, ### headings."""
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        block = block.strip()
        if not block:
            continue
        lines = block.splitlines()
        image = re.fullmatch(r'!\[(.*?)\]\((\S+?)(?:\s+"(.*)")?\)', block)
        if image:
            out.append(figure(image.group(1), image.group(2), image.group(3), titles))
        elif block.startswith("$$"):
            out.append(f'<div class="math-display">{html.escape(block, quote=False)}</div>')
        elif all(line.startswith("|") for line in lines):
            out.append(table(lines, titles))
        elif block.startswith("### "):
            out.append(f"<h3>{inline(block[4:], titles)}</h3>")
        elif block.startswith("- "):
            items = []
            for line in lines:
                if line.startswith("- "):
                    items.append(line[2:])
                else:
                    items[-1] += " " + line.strip()
            out.append("<ul>" + "".join(f"<li>{inline(i, titles)}</li>" for i in items) + "</ul>")
        else:
            out.append(f"<p>{inline(' '.join(l.strip() for l in lines), titles)}</p>")
    return "\n".join(out)


def table(lines, titles):
    """A simple Markdown table: header row, |---| divider, body rows."""
    rows = [[c.strip() for c in line.strip().strip("|").split("|")] for line in lines]
    head, body = rows[0], [r for r in rows[1:] if not set("".join(r)) <= set("-: ")]
    th = "".join(f"<th>{inline(c, titles)}</th>" for c in head)
    trs = "".join("<tr>" + "".join(f"<td>{inline(c, titles)}</td>" for c in r) + "</tr>" for r in body)
    return f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>"


def plain(html_text):
    """Rough plain text, for the search index."""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(html_text))).strip()


# ---------------------------------------------------------------- entries

def check_cues(path, options):
    """Warn when the correct option stands out by length, a cue that lets
    test-wise readers find the answer without the physics. Picture options
    are skipped. This only warns; the build carries on."""
    if all("<figure>" in o["html"] for o in options):
        return
    words = [len(plain(o["html"]).split()) for o in options]
    right = next(i for i, o in enumerate(options) if o["correct"])
    others = [w for i, w in enumerate(words) if i != right]
    if words[right] > 1.25 * max(others) and words[right] - max(others) >= 3:
        print(f"  warning, {path.name}: the correct option is the longest "
              f"({words[right]} words; others {others})")
    elif words[right] < 0.6 * min(others) and min(others) - words[right] >= 3:
        print(f"  warning, {path.name}: the correct option is much the shortest "
              f"({words[right]} words; others {others})")


def build_entry(path, titles):
    meta, sections = read_entry(path)
    for key in ("title", "misconception", "tagline", "topic", "levels"):
        if not meta.get(key):
            fail(path, f"front matter needs '{key}'")
    levels = [l.strip() for l in meta["levels"].split(",") if l.strip()]
    if not levels or not set(levels) <= LEVELS:
        fail(path, f"levels must be junior and/or senior, not '{meta['levels']}'")

    question, options, extra = None, [], []
    for heading, body in sections:
        if heading == "Question":
            question = body
        elif heading in ("Option", "Option (correct)"):
            lines = body.splitlines()
            choice = "\n".join(l for l in lines if not l.startswith(">"))
            feedback = "\n".join(re.sub(r"^> ?", "", l) for l in lines if l.startswith(">"))
            choice_html = render(choice, titles)
            # A one-paragraph option doesn't need its <p> wrapper.
            if choice_html.startswith("<p>") and choice_html.count("<p>") == 1:
                choice_html = choice_html[3:-4]
            options.append({
                "html": choice_html,
                "feedback": render(feedback, titles),
                "correct": heading == "Option (correct)",
            })
        elif heading in SECTIONS:
            extra.append({"heading": heading, "html": render(body, titles)})
        else:
            fail(path, f"unknown section '## {heading}'")

    if question is None:
        fail(path, "needs a '## Question' section")
    if len(options) < 2 or sum(o["correct"] for o in options) != 1:
        fail(path, "needs at least two options, exactly one marked (correct)")
    extra.sort(key=lambda s: SECTIONS.index(s["heading"]))

    check_cues(path, options)
    question_html = render(question, titles)
    related =[r.strip() for r in meta.get("related", "").split(",") if r.strip()]
    for r in related:
        if r not in titles:
            fail(path, f"related entry '{r}' does not exist")

    return {
        "id": path.stem,
        "order": int(meta.get("order", 999)),
        "title": meta["title"],
        "misconception": inline(meta["misconception"], titles),
        "tagline": inline(meta["tagline"], titles),
        "topic": meta["topic"],
        "levels": levels,
        "teaser": inline(question.split("\n\n")[0], titles),
        "search": " ".join([meta["title"], meta["topic"], meta.get("keywords", ""),
                            plain(question_html)]).lower(),
        "question": question_html,
        "options": options,
        "pictureOptions": all("<figure>" in o["html"] for o in options),
        "sections": extra,
        "related": [{"id": r, "title": titles[r]} for r in related],
        "credit": inline(meta["credit"], titles) if meta.get("credit") else "",
    }


def main():
    paths = sorted(ENTRY_DIR.glob("*.md"))
    titles = {p.stem: read_entry(p)[0].get("title", p.stem) for p in paths}
    entries = [build_entry(p, titles) for p in paths]
    entries.sort(key=lambda e: (e["order"], e["title"]))
    for number, entry in enumerate(entries, 1):
        entry["number"] = number

    # "</" is escaped so no entry text can close the <script> tag early.
    data = json.dumps({"entries": entries}, ensure_ascii=False).replace("</", "<\\/")
    template = TEMPLATE.read_text(encoding="utf-8")
    if template.count("__DATA__") != 1:
        raise SystemExit("template.html must contain __DATA__ exactly once")
    OUTPUT.write_text(template.replace("__DATA__", data), encoding="utf-8")
    print(f"Built {OUTPUT.name}: {len(entries)} entries.")


if __name__ == "__main__":
    main()
