#!/usr/bin/env python3
"""
render_booklet.py — igcse-revision-kit topic renderer.

    topic.md of every subtopic (+ assets/*)  ->  ONE html document  ->  headless Chromium  ->  PDF

Agents do not call this directly; `build_pdf.py` calls `render_topic()`. Subtopics flow on
continuously (no forced page breaks); each starts with its title and specification points.
Chromium builds the PDF bookmarks from the headings.

Never printed: `## Specification coverage`, `## What you must be able to do`, self-check /
test / answers sections, and `::: revision|test|answers|checklist` blocks. These are agent-facing
or banned; see AGENTS.md.

Requires: python3 with `markdown`, `pyyaml`, `playwright` (Chromium) and `pypdf` —
see tools/pdf/README.md for setup.
"""

from __future__ import annotations

import base64
import html as html_mod
import re
import sys
from pathlib import Path

import markdown
import yaml

HERE = Path(__file__).resolve().parent

CURRENT_META: dict = {}   # front matter of the document being rendered

# --------------------------------------------------------------------------
# callout vocabulary:  ::: <name>  ->  <div class="callout <css>"> + label
# --------------------------------------------------------------------------
CALLOUTS = {
    "definition":    ("definition",    "Definition"),
    "traps":         ("traps",         "Traps"),
    "trap":          ("traps",         "Traps"),
    "exam":          ("exam",          "Exam language"),
    "why":           ("why",           "Why it matters"),
    "note":          ("note",          "Note"),
    "advantages":    ("advantages",    "Advantages"),
    "disadvantages": ("disadvantages", "Disadvantages"),
}

# headings in legacy topic.md files that map onto booklet furniture
LEGACY_SECTIONS = {
    # agent-facing metadata, never printed
    "specification coverage":   "drop",
    "what you must be able to do": "drop",
    "common misunderstandings": ("callout", "traps", "Traps"),
    "common traps":             ("callout", "traps", "Traps"),
    "exam relevance":           ("callout", "exam", "Exam language"),
    # practice belongs in questions.md, never in the PDF: these headings are dropped
    "quick self-check":         "drop",
    "test yourself":            "drop",
    "answers and marking guidance": "drop",
}

DROPPED_BLOCKS = {"revision", "test", "answers", "checklist"}

MD_EXTENSIONS = ["extra", "sane_lists", "smarty", "attr_list"]
MD_CONFIG = {"smarty": {"smart_dashes": True, "smart_quotes": False}}


# ==========================================================================
# front matter
# ==========================================================================
def split_front_matter(text: str):
    if text.startswith("---\n"):
        end = text.find("\n---", 3)
        if end != -1:
            raw = text[4:end]
            rest = text[end + 4:].lstrip("\n")
            try:
                return (yaml.safe_load(raw) or {}), rest
            except yaml.YAMLError:
                pass
    return {}, text


# ==========================================================================
# ::: fenced blocks  ->  nested tree  ->  HTML
# ==========================================================================
FENCE_RE = re.compile(r"^(:{3,})\s*([A-Za-z0-9_-]*)\s*(?:\|\s*(.*?))?\s*$")


def parse_blocks(lines, depth=0, i=0):
    """Return (nodes, next_index). A node is ('text', str) or ('block', kind, arg, children)."""
    nodes, buf = [], []

    def flush():
        if buf:
            nodes.append(("text", "\n".join(buf)))
            buf.clear()

    while i < len(lines):
        m = FENCE_RE.match(lines[i])
        if m and m.group(2):                       # opening fence
            flush()
            fence = m.group(1)
            kind, arg = m.group(2).lower(), (m.group(3) or "").strip()
            children, i = parse_blocks(lines, len(fence), i + 1)
            nodes.append(("block", kind, arg, children))
            continue
        if m and not m.group(2) and depth:          # closing fence
            flush()
            return nodes, i + 1
        buf.append(lines[i])
        i += 1

    flush()
    return nodes, i


def md_to_html(text: str) -> str:
    return markdown.markdown(text, extensions=MD_EXTENSIONS, extension_configs=MD_CONFIG)


def label_html(label: str, cls: str) -> str:
    return f'<div class="{cls}">{html_mod.escape(label)}</div>' if label else ""


def render_nodes(nodes) -> str:
    out = []
    for node in nodes:
        if node[0] == "text":
            out.append(md_to_html(node[1]))
        else:
            out.append(render_block(node[1], node[2], node[3]))
    return "\n".join(x for x in out if x)


def render_block(kind, arg, children) -> str:
    inner = render_nodes(children)

    if kind in CALLOUTS:
        css, default_label = CALLOUTS[kind]
        return (f'<div class="callout {css}">'
                f'{label_html(arg or default_label, "callout-label")}{inner}</div>')

    if kind in ("grid", "columns", "cards"):
        return f'<div class="grid">{inner}</div>'

    if kind == "card":
        return f'<div class="card">{label_html(arg, "card-label")}{inner}</div>'

    if kind == "banner":
        title, _, sub = arg.partition("|")
        sub_html = f'<p class="banner-sub">{html_mod.escape(sub.strip())}</p>' if sub.strip() else ""
        return (f'<div class="banner"><div class="banner-title">{html_mod.escape(title.strip())}</div>{sub_html}</div>'
                f"{inner}")

    if kind in DROPPED_BLOCKS:
        # recap / self-test / answers / checklist blocks are not part of the PDF
        return ""

    if kind == "pagebreak":
        return '<div class="pagebreak"></div>'

    if kind == "specstrip":
        return spec_strip_from_html(inner, CURRENT_META)

    # unknown fence: pass content through untouched
    return inner


# ==========================================================================
# specification strip
# ==========================================================================
def spec_strip_from_pairs(pairs) -> str:
    cells = "".join(
        f'<div class="cell"><div class="label">{html_mod.escape(str(k))}</div>'
        f'<div class="value">{inline_md(str(v))}</div></div>'
        for k, v in pairs
    )
    return f'<div class="spec-strip">{cells}</div>' if cells else ""


def inline_md(text: str) -> str:
    out = md_to_html(text)
    return re.sub(r"^<p>|</p>$", "", out.strip())


def spec_strip_from_html(section_html: str, meta: dict) -> str:
    """First 2-column table in the section becomes the strip; anything else in
    the section (e.g. a Requirement/Section table) follows as a card."""
    tables = list(re.finditer(r"<table>.*?</table>", section_html, flags=re.S))
    if not tables:
        return section_html
    first = tables[0]
    pairs = []
    for row in re.findall(r"<tr>(.*?)</tr>", first.group(0), flags=re.S):
        cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, flags=re.S)
        if len(cells) != 2:
            continue
        key = re.sub(r"<[^>]+>", "", cells[0]).strip()
        if key.lower() in ("field", "value"):
            continue
        pairs.append((key, cells[1].strip()))
    if not pairs:
        return section_html

    # "Qualification" belongs in the eyebrow above the title, not in the strip
    kept = []
    for k, v in pairs:
        if k.lower() in ("qualification", "subject") and not meta.get("eyebrow"):
            meta["eyebrow"] = re.sub(r"<[^>]+>", "", v).strip()
        else:
            kept.append((k, v))
    kept = kept or pairs

    cells_html = "".join(
        f'<div class="cell"><div class="label">{html_mod.escape(k)}</div>'
        f'<div class="value">{v}</div></div>' for k, v in kept
    )
    strip = f'<div class="spec-strip">{cells_html}</div>'

    rest = (section_html[:first.start()] + section_html[first.end():]).strip()
    if rest:
        strip += f'<div class="card"><div class="card-label">The official statements</div>{rest}</div>'
    return strip


# ==========================================================================
# legacy-markdown preprocessing (files written before this pipeline existed)
# ==========================================================================
def preprocess_legacy(md_text: str) -> str:
    """Wrap well-known '## headings' in the matching ::: block, so that
    topic.md files authored before this pipeline still render as booklets."""
    lines = md_text.split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^##\s+(.+?)\s*$", line)
        key = m.group(1).strip().lower() if m else None
        rule = LEGACY_SECTIONS.get(key) if key else None
        if not rule:
            out.append(line)
            i += 1
            continue

        # collect the body of this section
        body, j = [], i + 1
        seen_table = False
        while j < len(lines) and not re.match(r"^##\s+", lines[j]):
            is_row = lines[j].lstrip().startswith("|")
            # the coverage section is only its table: anything after the table is content
            if key == "specification coverage" and seen_table and not is_row and lines[j].strip():
                break
            seen_table = seen_table or is_row
            body.append(lines[j])
            j += 1
        body_text = "\n".join(body).strip("\n")

        if rule == "drop":
            pass
        elif rule == "specstrip":
            out += ["::::: specstrip", body_text, ":::::", ""]
        elif rule[0] == "card":
            out += [f"::::: card | {rule[1]}", body_text, ":::::", ""]
        elif rule[0] == "callout":
            out += [f"::::: {rule[1]} | {rule[2]}", body_text, ":::::", ""]
        i = j
    return "\n".join(out)


# ==========================================================================
# headings:  "## 3. Cell differentiation — Paper 2 only"
# ==========================================================================
def style_headings(html_str: str) -> str:
    def fix_h2(m):
        text = m.group(1)
        badge = ""
        for pat, label in ((r"\s*[—-]\s*Paper\s*2\s*only\s*$", "Paper 2 only"),
                           (r"\s*\[P2\]\s*$", "Paper 2 only")):
            if re.search(pat, text, flags=re.I):
                text = re.sub(pat, "", text, flags=re.I)
                badge = f' <span class="badge p2">{label}</span>'
                break
        num = ""
        nm = re.match(r"^(\d+)[.)]\s+(.*)$", text)
        if nm:
            num = f'<span class="num" data-n="{nm.group(1)}"></span>'
            text = nm.group(2)
        return f'<h2 class="section">{num}<span>{text}{badge}</span></h2>'

    return re.sub(r"<h2>(.*?)</h2>", fix_h2, html_str, flags=re.S)




# ==========================================================================
# gentle auto-styling of prose patterns used before this pipeline existed
# ==========================================================================
DEF_P = re.compile(
    r"<p><strong>Definitions?\s*[—-]\s*(?P<term>[^<:]+?):?</strong>(?P<rest>.*?)</p>",
    flags=re.S | re.I)


BQ_LABEL = re.compile(
    r"<blockquote>\s*<p><strong>(?P<label>[A-Z][A-Za-z ]{1,30}?)[.:]?</strong>\s*(?P<rest>.*?)</blockquote>",
    flags=re.S)
BQ_CLASS = {"definition": "definition", "definitions": "definition", "trap": "traps",
            "traps": "traps", "exam language": "exam", "exam": "exam"}


def auto_style(html_str: str) -> str:
    # "> **Trap.** text" style blockquotes -> labelled callouts
    def bq(m):
        label = m.group("label").strip()
        css = BQ_CLASS.get(label.lower(), "note")
        return (f'<div class="callout {css}"><div class="callout-label">{html_mod.escape(label)}</div>'
                f'<p>{m.group("rest")}</div>')
    html_str = BQ_LABEL.sub(bq, html_str)

    # "**Definition — X:** ..." paragraph -> definition callout
    html_str = DEF_P.sub(
        lambda m: ('<div class="callout definition"><div class="callout-label">Definition</div>'
                   f'<p><strong>{m.group("term").strip()}</strong> —{m.group("rest")}</p></div>'),
        html_str)

    # "**Advantages**" / "**Disadvantages**" + following list -> paired panels
    pat = re.compile(
        r"<p><strong>Advantages</strong></p>\s*(?P<a><ul>.*?</ul>)\s*"
        r"<p><strong>Disadvantages</strong></p>\s*(?P<d><ul>.*?</ul>)", flags=re.S | re.I)
    html_str = pat.sub(
        lambda m: ('<div class="grid">'
                   '<div class="callout advantages"><div class="callout-label">Advantages</div>'
                   f'{m.group("a")}</div>'
                   '<div class="callout disadvantages"><div class="callout-label">Disadvantages</div>'
                   f'{m.group("d")}</div></div>'),
        html_str)
    return html_str


# ==========================================================================
# figures: inline local SVG, embed raster images, attach italic captions
# ==========================================================================
def embed_media(html_str: str, base: Path) -> str:
    def svg_markup(path: Path) -> str:
        svg = path.read_text(encoding="utf-8")
        svg = re.sub(r"<\?xml.*?\?>", "", svg, flags=re.S)
        svg = re.sub(r"<!DOCTYPE.*?>", "", svg, flags=re.S)
        svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S).strip()
        # let CSS size the drawing: drop fixed width/height, keep the viewBox
        head_end = svg.find(">")
        head, tail = svg[:head_end], svg[head_end:]
        head = re.sub(r'\s(?:width|height)="[^"]*"', "", head)
        if "preserveAspectRatio" not in head:
            head = head.replace("<svg", '<svg preserveAspectRatio="xMidYMid meet"', 1)
        return head + tail

    def one_img(m):
        src, alt = m.group("src"), m.group("alt") or ""
        path = (base / src).resolve()
        if not path.exists():
            sys.stderr.write(f"  ! missing asset: {src}\n")
            return f'<p class="callout note">Missing asset: {html_mod.escape(src)}</p>'
        if path.suffix.lower() == ".svg":
            return svg_markup(path)
        mime = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
                ".gif": "image/gif", ".webp": "image/webp"}.get(path.suffix.lower(), "image/png")
        data = base64.b64encode(path.read_bytes()).decode()
        return f'<img src="data:{mime};base64,{data}" alt="{html_mod.escape(alt)}">'

    img_pat = r'<img\s[^>]*?alt="(?P<alt>[^"]*)"[^>]*?src="(?P<src>[^"]+)"[^>]*?>'
    img_pat_alt = r'<img\s[^>]*?src="(?P<src>[^"]+)"[^>]*?alt="(?P<alt>[^"]*)"[^>]*?>'

    # image paragraph immediately followed by an italic caption paragraph
    combo = re.compile(
        r"<p>\s*(?P<img><img\s[^>]*?>)\s*</p>\s*<p>\s*<em>(?P<cap>.*?)</em>\s*</p>",
        flags=re.S)

    def figure_with_caption(m):
        img = m.group("img")
        for pat in (img_pat, img_pat_alt):
            new = re.sub(pat, one_img, img, count=1)
            if new != img:
                img = new
                break
        return f'<figure>{img}<figcaption>{m.group("cap")}</figcaption></figure>'

    html_str = combo.sub(figure_with_caption, html_str)

    # any remaining standalone image paragraph
    def figure_plain(m):
        img = m.group(1)
        for pat in (img_pat, img_pat_alt):
            new = re.sub(pat, one_img, img, count=1)
            if new != img:
                img = new
                break
        return f"<figure>{img}</figure>"

    html_str = re.sub(r"<p>\s*(<img\s[^>]*?>)\s*</p>", figure_plain, html_str, flags=re.S)
    # inline images left anywhere else
    for pat in (img_pat, img_pat_alt):
        html_str = re.sub(pat, one_img, html_str)
    return html_str


# ==========================================================================
# document assembly — ONE html document per top-level topic
# ==========================================================================
POINTS_RE = re.compile(r"Specification points?\s+(.+?)\s*(?:[—–-]\s|$)", re.S)


def spec_points(meta: dict) -> str:
    """'1.3–1.10' from a subtitle like 'Specification points 1.3–1.10 — what it covers'."""
    m = POINTS_RE.search(str(meta.get("subtitle") or ""))
    return m.group(1).strip().rstrip(".") if m else ""


def qualification(meta: dict, md_text: str) -> str:
    if meta.get("eyebrow"):
        return str(meta["eyebrow"])
    m = re.search(r"^\|\s*Qualification\s*\|\s*(.+?)\s*\|\s*$", md_text, flags=re.M | re.I)
    return re.sub(r"[*`]", "", m.group(1)).split(",")[0].strip() if m else ""


def read_part(source_dir: Path):
    raw = (source_dir / "topic.md").read_text(encoding="utf-8")
    meta, md_text = split_front_matter(raw)
    title = meta.get("title")
    m = re.match(r"^\s*#\s+(.+?)\s*\n", md_text)
    if m:
        title = title or m.group(1).strip()
        md_text = md_text[m.end():]
    return meta, str(title or source_dir.name.replace("_", " ")), md_text, raw


def part_body(md_text: str, base: Path) -> str:
    global CURRENT_META
    CURRENT_META = {}
    nodes, _ = parse_blocks(preprocess_legacy(md_text).split("\n"))
    body = render_nodes(nodes)
    body = style_headings(body)
    body = auto_style(body)
    return embed_media(body, base)


def split_title(topic_md: Path) -> str:
    return read_part(topic_md.parent)[1]


def build_topic_html(parts, topic_title: str) -> tuple[str, str]:
    """parts: list of subtopic source dirs. Returns (html, eyebrow)."""
    single = len(parts) == 1
    eyebrow, chunks = "", []
    for i, src in enumerate(parts):
        meta, title, md_text, raw = read_part(src)
        if i == 0:
            eyebrow = qualification(meta, raw)
        pts = spec_points(meta)
        if single:
            head = (f'<h1 class="doc-title">{html_mod.escape(title)}</h1>'
                    + (f'<p class="doc-points">Specification points {html_mod.escape(pts)}</p>' if pts else "")
                    + '<div class="title-rule"></div>')
        else:
            head = (f'<h1 class="sub-title" data-pts="{html_mod.escape(pts)}">'
                    f'<span>{html_mod.escape(title)}</span></h1>')
        chunks.append(f'<section class="subtopic">{head}{part_body(md_text, src)}</section>')

    header = []
    if eyebrow:
        header.append(f'<p class="eyebrow">{html_mod.escape(eyebrow).upper()}</p>')
    if not single:
        header.append(f'<div class="doc-title topic">{html_mod.escape(topic_title)}</div><div class="title-rule"></div>')

    shell = (HERE / "page_shell.html").read_text(encoding="utf-8")
    html = (shell.replace("{{CSS}}", (HERE / "topic_style.css").read_text(encoding="utf-8"))
                 .replace("{{TITLE}}", html_mod.escape(topic_title))
                 .replace("{{HEADER}}", "\n".join(header))
                 .replace("{{BODY}}", "\n".join(chunks))
                 )
    return html, eyebrow


# ==========================================================================
# render + metadata
# ==========================================================================
def render_pdf(html_str: str, out_pdf: Path, footer_left: str, work_dir: Path):
    from playwright.sync_api import sync_playwright

    tmp_html = work_dir / "_render.html"
    tmp_html.write_text(html_str, encoding="utf-8")
    footer = (HERE / "running_footer.html").read_text(encoding="utf-8")
    footer = footer.replace("{{FOOTER_LEFT}}", html_mod.escape(footer_left))

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--font-render-hinting=none"])
        page = browser.new_page()
        page.goto(tmp_html.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(out_pdf), format="A4", print_background=True,
            display_header_footer=True, header_template="<div></div>", footer_template=footer,
            margin={"top": "12mm", "bottom": "13mm", "left": "13mm", "right": "13mm"},
            prefer_css_page_size=False, outline=True, tagged=True,
        )
        browser.close()
    return tmp_html


def write_metadata(pdf: Path, title: str, subject: str):
    from pypdf import PdfReader, PdfWriter
    writer = PdfWriter(clone_from=str(pdf))          # keeps Chromium's bookmarks
    writer.add_metadata({"/Title": title, "/Subject": subject,
                         "/Author": "igcse-revision-kit"})
    tmp = pdf.with_suffix(".tmp.pdf")
    with open(tmp, "wb") as fh:
        writer.write(fh)
    tmp.replace(pdf)


def render_topic(parts, out_pdf: Path, topic_title: str, footer: str, keep_html: bool = False) -> int:
    """Render all subtopic sources of one topic into ONE continuous PDF. Returns page count."""
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    html_str, eyebrow = build_topic_html(parts, topic_title)
    import tempfile
    work = Path(tempfile.mkdtemp())
    tmp_html = render_pdf(html_str, out_pdf, footer, work)
    write_metadata(out_pdf, topic_title, eyebrow)
    if keep_html:
        tmp_html.replace(out_pdf.with_suffix(".html"))
    else:
        tmp_html.unlink(missing_ok=True)
    from pypdf import PdfReader
    return len(PdfReader(str(out_pdf)).pages)
