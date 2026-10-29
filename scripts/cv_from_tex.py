#!/usr/bin/env python3
"""Convert the Overleaf CV (resume.tex in ChrisLvvvv/CV_Git) into _data/cv_tex.json.

The /cv page (_pages/cv.html) renders from that JSON, so the website always
matches the LaTeX source.

Expected LaTeX structure (the existing template):
  \\subsection*{\\Large <Section>}
  \\begin{itemize} ... \\item \\headerrow{A}{B} \\headerrow{C}{D} \\begin{itemize*} \\item ... \\end{itemize*}
  Extra \\headerrow pairs + itemize* inside one \\item become extra roles (e.g. two
  positions at the same company). The "Technical Skills" section uses
  \\item \\textbf{Label:} text.

The phone number is never exported.

Usage: python3 scripts/cv_from_tex.py path/to/resume.tex _data/cv_tex.json [source_sha]
"""
import html
import json
import re
import sys

# ---------------------------------------------------------------- utilities


def strip_comments(tex):
    out = []
    for line in tex.splitlines():
        m = re.search(r"(?<!\\)%", line)
        out.append(line[: m.start()] if m else line)
    return "\n".join(out)


def read_group(s, i, open_="{", close="}"):
    """s[i] must be `open_`; return (content, index after the closing brace)."""
    assert s[i] == open_, (s[i : i + 30], i)
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == open_:
            depth += 1
        elif c == close:
            depth -= 1
            if depth == 0:
                return s[i + 1 : j], j + 1
        j += 1
    raise ValueError("unbalanced group starting at %d" % i)


def skip_ws(s, i):
    while i < len(s) and s[i].isspace():
        i += 1
    return i


def read_args(s, i, n):
    """Read n mandatory {..} args (skipping optional [..] args) starting at i."""
    args = []
    while len(args) < n:
        i = skip_ws(s, i)
        if s[i] == "[":
            _, i = read_group(s, i, "[", "]")
            continue
        a, i = read_group(s, i)
        args.append(a)
    return args, i


# ---------------------------------------------------------- LaTeX -> HTML

MATH_SYMBOLS = {
    r"\times": "×", r"\mu": "µ", r"\cdot": "·", r"\rightarrow": "→", r"\to": "→",
    r"\leftarrow": "←", r"\approx": "≈", r"\le": "≤", r"\leq": "≤", r"\ge": "≥",
    r"\geq": "≥", r"\pm": "±", r"\sim": "~", r"\bullet": "•", r"\beta": "β",
    r"\gamma": "γ", r"\tau": "τ", r"\Omega": "Ω", r"\alpha": "α", r"\lambda": "λ",
    r"\%": "%", r"\,": "\u2009", r"\;": " ", r"\ ": " ",
}
SUPERSCRIPTS = str.maketrans("0123456789+-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻")


def math_to_html(m):
    m = m.strip()
    m = re.sub(r"\\mathrm\{([^{}]*)\}|\\text\{([^{}]*)\}", lambda x: x.group(1) or x.group(2), m)
    for k in sorted(MATH_SYMBOLS, key=len, reverse=True):
        m = m.replace(k, MATH_SYMBOLS[k])
    m = re.sub(r"\^\{([0-9+\-]+)\}|\^([0-9])", lambda x: (x.group(1) or x.group(2)).translate(SUPERSCRIPTS), m)
    m = re.sub(r"\^\{([^{}]*)\}", r"<sup>\1</sup>", m)
    m = re.sub(r"_\{([^{}]*)\}|_([A-Za-z0-9])", lambda x: "<sub>%s</sub>" % (x.group(1) or x.group(2)), m)
    m = re.sub(r"\\[A-Za-z]+", "", m)
    m = m.replace("{", "").replace("}", "")
    m = re.sub(r"\s+", " ", m)
    m = re.sub(r"\s*×\s*", " × ", m)
    return m.strip()


TEXT_COMMANDS = {  # command -> (html open, html close)
    "textbf": ("<strong>", "</strong>"),
    "emph": ("<em>", "</em>"),
    "textit": ("<em>", "</em>"),
    "underline": ("", ""),
    "textrm": ("", ""),
    "texttt": ("<code>", "</code>"),
    "mbox": ("", ""),
    "small": ("", ""),
}
ESCAPES = {"%": "%", "&": "&amp;", "_": "_", "#": "#", "$": "$", "{": "{", "}": "}", ",": "\u2009", " ": " ", "-": ""}
WORDS = {"LaTeX": "LaTeX", "TeX": "TeX", "CPP": "C++", "ldots": "…", "dots": "…", "textbullet": "•",
         "textendash": "–", "textemdash": "—", "textasciitilde": "~", "&": "&amp;"}
DROP = {"hfill", "newline", "linebreak", "nolinebreak", "hspace", "vspace", "raisebox", "Large",
        "large", "LARGE", "footnotesize", "small", "normalsize", "bf", "it", "noindent", "centering"}


def tex_to_html(s):
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == "$":
            j = s.index("$", i + 1)
            out.append(math_to_html(s[i + 1 : j]))
            i = j + 1
        elif c == "\\":
            if i + 1 < len(s) and not s[i + 1].isalpha():
                ch = s[i + 1]
                out.append(ESCAPES.get(ch, "") if ch != "\\" else " ")
                i += 2
                continue
            m = re.match(r"\\([A-Za-z]+)\*?", s[i:])
            name = m.group(1)
            i += m.end()
            if name in TEXT_COMMANDS:
                (arg,), i = read_args(s, i, 1)
                o, c2 = TEXT_COMMANDS[name]
                out.append(o + tex_to_html(arg) + c2)
            elif name == "href":
                (url, text), i = read_args(s, i, 2)
                out.append('<a href="%s">%s</a>' % (html.escape(url, quote=True), tex_to_html(text)))
            elif name == "url":
                (url,), i = read_args(s, i, 1)
                out.append('<a href="%s">%s</a>' % (html.escape(url, quote=True), html.escape(url)))
            elif name == "parbox":
                (_, text), i = read_args(s, i, 2)
                out.append(tex_to_html(text))
            elif name in ("hspace", "vspace"):
                _, i = read_args(s, i, 1)
            elif name in WORDS:
                out.append(WORDS[name])
                if i < len(s) and s[i : i + 2] == "{}":
                    i += 2
            elif name in DROP:
                pass
            else:  # unknown command: keep its argument text, if any
                pass
        elif c in "{}":
            i += 1
        elif c == "~":
            out.append("\u00a0")
            i += 1
        elif s.startswith("---", i):
            out.append("—")
            i += 3
        elif s.startswith("--", i):
            out.append("–")
            i += 2
        elif s.startswith("``", i) or s.startswith("''", i):
            out.append("“" if s[i] == "`" else "”")
            i += 2
        else:
            out.append(html.escape(c, quote=False))
            i += 1
    text = "".join(out)
    return re.sub(r"\s+", " ", text).strip()


# ---------------------------------------------------------- structure


def split_items(body):
    """Split an itemize body into top-level \\item chunks."""
    items, depth, start, i = [], 0, None, 0
    tokens = re.finditer(r"\\begin\{[^}]*\}|\\end\{[^}]*\}|\\item\b", body)
    for t in tokens:
        tok = t.group(0)
        if tok.startswith("\\begin"):
            depth += 1
        elif tok.startswith("\\end"):
            depth -= 1
        elif depth == 0:
            if start is not None:
                items.append(body[start : t.start()])
            start = t.end()
    if start is not None:
        items.append(body[start:])
    return items


def env_body(s, name, start=0):
    m = re.search(r"\\begin\{%s\}(\[[^\]]*\])?" % re.escape(name), s[start:])
    if not m:
        return None, None
    b = start + m.end()
    depth, i = 1, b
    for t in re.finditer(r"\\(begin|end)\{([^}]*)\}", s[b:]):
        depth += 1 if t.group(1) == "begin" else -1
        if depth == 0:
            return s[b : b + t.start()], b + t.end()
    raise ValueError("unterminated environment " + name)


def plain_header(tex):
    """Header fields get their styling from the site CSS, so drop bold/italic wrappers."""
    return re.sub(r"</?(strong|em)>", "", tex_to_html(tex)).strip()


def parse_entry(chunk):
    """An entry is a sequence of \\headerrow{L}{R} rows and itemize* bullet lists."""
    rows, i, roles = [], 0, []
    current = None
    while True:
        h = chunk.find("\\headerrow", i)
        b = chunk.find("\\begin{itemize*}", i)
        if h == -1 and b == -1:
            break
        if h != -1 and (b == -1 or h < b):
            (left, right), i = read_args(chunk, h + len("\\headerrow"), 2)
            rows.append((plain_header(left), plain_header(right)))
        else:
            inner, i = env_body(chunk, "itemize*", b)
            bullets = [tex_to_html(x) for x in split_items(inner) if x.strip()]
            roles.append({"rows": rows, "bullets": bullets})
            rows = []
    if rows:
        roles.append({"rows": rows, "bullets": []})
    if not roles:
        return []
    # First role: row 0 = title/meta, row 1 = subhead/meta. Later roles: one row = subhead/meta.
    first = roles[0]["rows"]
    title, meta1 = first[0]
    entries = []
    for k, role in enumerate(roles):
        rws = role["rows"] if k else role["rows"][1:]
        subheads = [l for l, _ in rws if l]
        meta = ([meta1] if meta1 else []) + [r for _, r in rws if r]
        entries.append({"title": title, "subheads": subheads, "meta": meta, "bullets": role["bullets"]})
    return entries


def parse(tex, source_sha=None):
    tex = strip_comments(tex)
    doc = tex[tex.index("\\begin{document}") :]

    data = {"name": "", "contact": {}, "sections": [], "source_sha": source_sha}
    m = re.search(r"\\LARGE\s*\\textbf\{([^}]*)\}", doc)
    if m:
        data["name"] = tex_to_html(m.group(1))
    m = re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", doc)
    if m:
        data["contact"]["email"] = m.group(0).lower()
    m = re.search(r"github\.com/([\w-]+)", doc)
    if m:
        data["contact"]["github"] = m.group(1)
    m = re.search(r"linkedin\.com/in/([\w-]+)", doc)
    if m:
        data["contact"]["linkedin"] = m.group(1)

    heads = list(re.finditer(r"\\subsection\*\{(?:\\Large\s*)?([^}]*)\}", doc))
    for n, h in enumerate(heads):
        title = tex_to_html(h.group(1))
        end = heads[n + 1].start() if n + 1 < len(heads) else doc.index("\\end{document}")
        body, _ = env_body(doc[h.end() : end], "itemize")
        if body is None:
            continue
        items = split_items(body)
        if "\\headerrow" not in body:  # skills-style section
            groups = []
            for it in items:
                if not it.strip():
                    continue
                mm = re.match(r"\s*\\textbf\{(.*?)\}\s*(.*)", it, re.S)
                if mm:
                    groups.append({"label": tex_to_html(mm.group(1)).rstrip(":"), "text": tex_to_html(mm.group(2))})
                else:
                    groups.append({"label": "", "text": tex_to_html(it)})
            data["sections"].append({"title": title, "kind": "skills", "groups": groups})
        else:
            entries = []
            for it in items:
                if it.strip():
                    entries.extend(parse_entry(it))
            data["sections"].append({"title": title, "kind": "entries", "entries": entries})
    return data


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    sha = sys.argv[3] if len(sys.argv) > 3 else None
    with open(src, encoding="utf-8") as f:
        data = parse(f.read(), sha)
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    n = sum(len(s.get("entries", s.get("groups", []))) for s in data["sections"])
    print("wrote %s: %d sections, %d entries/groups" % (dst, len(data["sections"]), n))
