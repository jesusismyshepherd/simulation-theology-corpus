"""Render research/SUMMARY.md to a print-styled PDF (research/SUMMARY.pdf).

Markdown -> HTML (python-markdown, tables) -> PDF (headless Edge or Chrome,
isolated profile). Relative links are rewritten to the GitHub copies so they
work inside the PDF.

Usage:
    python build_summary_pdf.py [--browser <path to msedge.exe or chrome.exe>]
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent
REPO_URL = "https://github.com/jesusismyshepherd/simulation-theology-corpus"
BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium",
]

CSS = """
@page { size: A4; margin: 22mm 20mm 22mm 20mm;
  @bottom-center { content: counter(page); font: 9pt "Segoe UI", Arial, sans-serif; color: #777; }
  @top-right { content: "Simulation Theology and the Kingdom"; font: 8.5pt "Segoe UI", Arial, sans-serif; color: #999; } }
@page :first { @bottom-center { content: none; } @top-right { content: none; } }
:root { --ink: #1d2430; --muted: #5b6575; --accent: #7a3e1d; --rule: #d9d3c7; --wash: #f7f4ee; }
html { font-size: 10.6pt; }
body { font-family: Cambria, Georgia, "Times New Roman", serif; color: var(--ink); line-height: 1.5; margin: 0; background: #fff; }
.cover { height: 247mm; display: flex; flex-direction: column; justify-content: center; page-break-after: always; }
.cover .kicker { font: 600 9.5pt "Segoe UI", Arial, sans-serif; letter-spacing: .14em; text-transform: uppercase; color: var(--accent); }
.cover h1 { font-size: 30pt; line-height: 1.12; margin: 10pt 0 14pt; border: none; }
.cover .sub { font-size: 13pt; color: var(--muted); max-width: 135mm; }
.cover .rule { width: 48mm; height: 3px; background: var(--accent); margin: 22pt 0; }
.cover .meta { font: 9.5pt "Segoe UI", Arial, sans-serif; color: var(--muted); line-height: 1.7; }
h1, h2, h3 { font-family: "Segoe UI", Arial, sans-serif; color: var(--ink); break-after: avoid; page-break-after: avoid; }
h2 { font-size: 15pt; margin: 22pt 0 8pt; padding-bottom: 4pt; border-bottom: 1.5px solid var(--rule); }
h2.break { break-before: page; page-break-before: always; margin-top: 0; }
h3 { font-size: 11.5pt; margin: 14pt 0 5pt; color: var(--accent); }
p { margin: 0 0 7pt; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 8pt; padding-left: 16pt; }
li { margin: 0 0 3.5pt; }
strong { color: #111; }
a { color: var(--accent); text-decoration: none; border-bottom: 0.5px solid #d8b9a5; }
code { font-family: Consolas, "Courier New", monospace; font-size: 9pt; background: var(--wash); padding: 0 2pt; border-radius: 2px; }
hr { border: none; border-top: 1px solid var(--rule); margin: 14pt 0; }
em:first-child { color: var(--muted); }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 11pt; font: 9pt/1.35 "Segoe UI", Arial, sans-serif; break-inside: avoid; page-break-inside: avoid; }
th { text-align: left; font-weight: 600; background: var(--wash); border-bottom: 1.5px solid #c9c0b0; padding: 4pt 6pt; }
td { border-bottom: 1px solid #ebe6dc; padding: 3.5pt 6pt; vertical-align: top; }
tr { break-inside: avoid; page-break-inside: avoid; }
.onepage ol > li { margin-bottom: 6pt; }
"""


def rewrite_links(md_text: str) -> str:
    def repl(m: re.Match) -> str:
        label, target = m.group(1), m.group(2)
        if re.match(r"^[a-z]+://", target) or target.startswith("#"):
            return m.group(0)
        path = (HERE / target).resolve()
        rel = path.relative_to(HERE.parent).as_posix()
        kind = "tree" if target.endswith("/") or path.is_dir() else "blob"
        return f"[{label}]({REPO_URL}/{kind}/main/{rel})"

    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", repl, md_text)


def build_html(md_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    title_match = re.match(r"#\s+(.+)\n", text)
    title = title_match.group(1).strip() if title_match else "Summary"
    body_md = text[title_match.end():] if title_match else text
    intro_match = re.match(r"\s*\*(.+?)\*\s*\n", body_md, re.S)
    intro = intro_match.group(1).strip() if intro_match else ""
    if intro_match:
        body_md = body_md[intro_match.end():]
    body = markdown.markdown(rewrite_links(body_md), extensions=["tables", "sane_lists"])
    body = body.replace("<hr />", "")
    # Major sections start on a new page, except the first after the cover.
    count = 0

    def h2(m: re.Match) -> str:
        nonlocal count
        count += 1
        cls = ""  # continuous flow; headings keep with their content
        return f"<h2{cls}>"

    body = re.sub(r"<h2>", h2, body)
    title_main, _, title_sub = title.partition(":")
    cover = (
        '<section class="cover">'
        '<div class="kicker">Research summary · October 2026</div>'
        f"<h1>{html.escape(title_main.strip())}</h1>"
        f'<div class="sub">{html.escape(title_sub.strip().capitalize())}</div>'
        '<div class="rule"></div>'
        f'<div class="meta">{markdown.markdown(rewrite_links(intro))}'
        f"Source: {REPO_URL}/tree/main/research</div>"
        "</section>"
    )
    return (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<title>{html.escape(title)}</title><style>{CSS}</style></head>"
        f"<body>{cover}<main class=\"onepage\">{body}</main></body></html>"
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--browser", default="")
    ap.add_argument("--input", default=str(HERE / "SUMMARY.md"))
    ap.add_argument("--output", default=str(HERE / "SUMMARY.pdf"))
    args = ap.parse_args()
    browser = args.browser or next((b for b in BROWSERS if Path(b).is_file()), "")
    if not browser:
        raise SystemExit("no Edge or Chrome found; pass --browser")
    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp) / "summary.html"
        html_path.write_text(build_html(Path(args.input)), encoding="utf-8")
        profile = Path(tmp) / "profile"
        cmd = [browser, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
               f"--user-data-dir={profile}", "--no-pdf-header-footer", f"--print-to-pdf={args.output}",
               html_path.as_uri()]
        subprocess.run(cmd, check=True, capture_output=True, timeout=180)
        shutil.copy(html_path, Path(args.output).with_suffix(".html")) if False else None
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
