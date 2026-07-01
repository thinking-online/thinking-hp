#!/usr/bin/env python3
"""Generate sample and purchaser portal pages for vocabulary test books."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS_SRC = Path(
    "/Users/tetta/.cursor/projects/Users-tetta-Documents-GitHub-thinking-hp/assets"
)

BOOKS = [
    {
        "slug": "sistan",
        "name": "システム英単語",
        "title": "システム英単語 問題集",
        "theme": "#2563eb",
        "theme_light": "#3b82f6",
        "theme_soft": "#eff6ff",
        "theme_border": "#bfdbfe",
        "theme_banner_end": "#1d4ed8",
        "theme_rgb": "37, 99, 235",
        "tagline": "単語を、得点力へ。",
        "secret": "58291473",
        "hero_file": "________-59092c3e-d1c5-453c-9683-993a69867d6e.png",
        "serial_desc": "読んだ範囲の確認用。システム英単語の並び順どおり。学校の週テスト対策や、覚えた直後の確認にどうぞ。",
        "chunk_label": "約50語ずつ",
    },
    {
        "slug": "sokudoku",
        "name": "速読英熟語",
        "title": "速読英熟語 問題集",
        "theme": "#ea580c",
        "theme_light": "#f97316",
        "theme_soft": "#fff7ed",
        "theme_border": "#fed7aa",
        "theme_banner_end": "#c2410c",
        "theme_rgb": "234, 88, 12",
        "tagline": "熟語と速読を、ひとつの流れで。",
        "secret": "39184726",
        "hero_file": "_________02-8557fd5f-2e09-4353-b6a6-959ae7b7ddd8.png",
        "serial_desc": "読んだ範囲の確認用。速読英熟語の並び順どおり。学校の週テスト対策や、覚えた直後の確認にどうぞ。",
        "chunk_label": "50語ずつ",
    },
    {
        "slug": "target1900",
        "name": "ターゲット1900",
        "title": "ターゲット1900 問題集",
        "theme": "#1d4ed8",
        "theme_light": "#2563eb",
        "theme_soft": "#eff6ff",
        "theme_border": "#bfdbfe",
        "theme_banner_end": "#1e3a8a",
        "theme_rgb": "29, 78, 216",
        "tagline": "単語学習を、最短で迷わず。",
        "secret": "62839417",
        "hero_file": "_________01-c50072b3-35f5-4acd-89cb-98146be6e580.png",
        "serial_desc": "50語ずつ／読んだ範囲の確認用。ターゲット1900の並び順どおり。学校の週テスト対策や、覚えた直後の確認にどうぞ。",
        "chunk_label": "50語ずつ",
    },
    {
        "slug": "target1000",
        "name": "英熟語ターゲット1000",
        "title": "英熟語ターゲット1000 問題集",
        "theme": "#dc2626",
        "theme_light": "#ef4444",
        "theme_soft": "#fef2f2",
        "theme_border": "#fecaca",
        "theme_banner_end": "#b91c1c",
        "theme_rgb": "220, 38, 38",
        "tagline": "熟語学習を、最短で迷わず。",
        "secret": "74628391",
        "hero_file": "_________05-4cf49bf4-d1fb-4ea2-b514-ae339b9e87c0.png",
        "serial_desc": "50語ずつ／読んだ範囲の確認用。英熟語ターゲット1000の並び順どおり。学校の週テスト対策や、覚えた直後の確認にどうぞ。",
        "chunk_label": "50語ずつ",
    },
    {
        "slug": "tetsubeki",
        "name": "鉄壁",
        "title": "鉄壁 問題集",
        "theme": "#1e3a5f",
        "theme_light": "#2563eb",
        "theme_soft": "#f0f4f8",
        "theme_border": "#cbd5e1",
        "theme_banner_end": "#0f172a",
        "theme_rgb": "30, 58, 95",
        "tagline": "最難関語彙を、深く確実に。",
        "secret": "83917264",
        "hero_file": "_________04-9850679e-883c-49ff-9d2c-c1a3153442d9.png",
        "serial_desc": "50語ずつ／読んだ範囲の確認用。鉄壁の並び順どおり。最難関語彙を深く確実に定着させるための確認にどうぞ。",
        "chunk_label": "50語ずつ",
    },
    {
        "slug": "eiken-pre1",
        "pdf_prefix": "pre1",
        "name": "英検準1級",
        "title": "英検準1級 問題集",
        "theme": "#7c3aed",
        "theme_light": "#8b5cf6",
        "theme_soft": "#f5f3ff",
        "theme_border": "#ddd6fe",
        "theme_banner_end": "#5b21b6",
        "theme_rgb": "124, 58, 237",
        "tagline": "英検準1級合格に必要な単語・熟語・表現を、効率よく確実にマスター。",
        "secret": "47281936",
        "hero_file": "EX__________-12587d56-bb9f-4ea8-941e-399902d4c674.png",
        "serial_desc": "50語ずつ／読んだ範囲の確認用。英検準1級の並び順どおり。学校の週テスト対策や、覚えた直後の確認にどうぞ。",
        "chunk_label": "50語ずつ",
    },
    {
        "slug": "eiken-2",
        "pdf_prefix": "eiken2",
        "name": "英検2級",
        "title": "英検2級 問題集",
        "theme": "#2563eb",
        "theme_light": "#3b82f6",
        "theme_soft": "#eff6ff",
        "theme_border": "#bfdbfe",
        "theme_banner_end": "#1d4ed8",
        "theme_rgb": "37, 99, 235",
        "tagline": "英検2級合格に必要な単語・熟語を効率的に学べる実践型ポータル。",
        "secret": "63847291",
        "hero_file": "EX_________-c19b94d2-2399-4d90-b366-82ee88c786b2.png",
        "serial_desc": "50語ずつ／読んだ範囲の確認用。英検2級の並び順どおり。学校の週テスト対策や、覚えた直後の確認にどうぞ。",
        "chunk_label": "50語ずつ",
    },
]

LINE_URL = (
    "https://liff.line.me/1656043253-rkMxPZMQ/landing?"
    "follow=%40499yrupi&lp=r8Dm9l&liff_id=1656043253-rkMxPZMQ"
)

SERIAL_RE = re.compile(r"^(.+)_(\d+)-(\d+)\.pdf$")
MIX_RE = re.compile(r"^(.+)_mix-(\d+)-(\d+)\.pdf$")
FINAL_RE = re.compile(r"^(.+)_final-(\d+)\.pdf$")


def parse_tests(slug: str, pdf_prefix: str | None = None) -> tuple[list[dict], list[dict], list[dict]]:
    prefix = pdf_prefix or slug
    test_dir = ROOT / "test" / slug
    serial: list[tuple[int, int, str]] = []
    mix: list[tuple[int, int, str]] = []
    final: list[tuple[int, str]] = []

    for path in sorted(test_dir.glob("*.pdf")):
        name = path.name
        if m := SERIAL_RE.match(name):
            if m.group(1) != prefix:
                continue
            serial.append((int(m.group(2)), int(m.group(3)), name))
        elif m := MIX_RE.match(name):
            if m.group(1) != prefix:
                continue
            mix.append((int(m.group(2)), int(m.group(3)), name))
        elif m := FINAL_RE.match(name):
            if m.group(1) != prefix:
                continue
            final.append((int(m.group(2)), name))

    serial.sort(key=lambda x: x[0])
    mix.sort(key=lambda x: x[0])
    final.sort(key=lambda x: x[0])

    serial_tests = [
        {
            "no": i + 1,
            "label": f"No.{start}〜{end}",
            "file": fname,
            "anchor": f"s-{start}",
        }
        for i, (start, end, fname) in enumerate(serial)
    ]
    mix_tests = [
        {
            "no": i + 1,
            "label": f"MIX No.{start}〜{end}",
            "file": fname,
            "anchor": f"m-{start}",
        }
        for i, (start, end, fname) in enumerate(mix)
    ]
    final_tests = [
        {
            "no": n,
            "label": f"総まとめテスト {n}",
            "file": fname,
            "anchor": f"f-{n}",
        }
        for n, fname in final
    ]
    return serial_tests, mix_tests, final_tests


def css_block(book: dict) -> str:
    rgb = book["theme_rgb"]
    return f"""  :root {{
    --teal: {book["theme"]};
    --teal-light: {book["theme_light"]};
    --teal-pale: {book["theme_soft"]};
    --teal-soft: {book["theme_soft"]};
    --navy: #0f172a;
    --navy-mid: #1e293b;
    --ink: #1e293b;
    --muted: #64748b;
    --line: #e2e8f0;
    --paper: #f8fafc;
    --card: #ffffff;
    --shadow: 0 8px 30px -10px rgba(15, 23, 42, 0.12);
    --shadow-sm: 0 2px 12px -4px rgba(15, 23, 42, 0.08);
    --radius: 16px;
    --radius-sm: 12px;
    --line-url: {LINE_URL};
  }}"""


def shared_styles(sample: bool) -> str:
    rgb_placeholder = "THEME_RGB"
    banner = ""
    if sample:
        banner = """
  .sample-banner {
    margin: 0 -16px;
    padding: 10px 16px;
    background: linear-gradient(90deg, var(--teal), var(--teal-banner-end));
    color: #fff;
    text-align: center;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .06em;
  }"""

    locked = ""
    if sample:
        locked = """
  .test-card--locked {
    background: #f8fafc;
    border-style: dashed;
    border-color: #cbd5e1;
    box-shadow: none;
    cursor: default;
    opacity: .88;
  }
  .test-card--locked::before { display: none; }
  .test-card--locked:hover {
    transform: none;
    border-color: #cbd5e1;
    box-shadow: none;
  }
  .test-card--sample {
    border-color: var(--teal-border);
    background: linear-gradient(180deg, #fff 0%, var(--teal-soft) 100%);
  }
  .test-card--sample::before { opacity: 1; }
  .test-card--locked .test-card-no { color: var(--muted); }
  .test-card--locked .test-card-range { color: var(--muted); }
  .test-card--locked .test-card-action { color: #94a3b8; }
  .sample-badge {
    position: absolute;
    top: 8px;
    right: 8px;
    padding: 2px 7px;
    border-radius: 6px;
    background: var(--teal);
    color: #fff;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: .04em;
  }
  .stat-chip--sample {
    background: #fff7ed;
    border-color: #fed7aa;
    color: #c2410c;
  }
  .purchase-note {
    margin-top: 36px;
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 22px 20px;
    text-align: center;
    box-shadow: var(--shadow-sm);
  }
  .purchase-note h2 {
    margin: 0 0 8px;
    font-size: 16px;
    font-weight: 900;
    color: var(--navy);
  }
  .purchase-note p {
    margin: 0;
    font-size: 13px;
    color: var(--muted);
    line-height: 1.75;
  }"""

    line_cta = ""
    if not sample:
        line_cta = """
  .line-cta {
    margin-top: 36px;
    background: linear-gradient(145deg, #ecfdf5, #f0fdfa);
    border: 1px solid #a7f3d0;
    border-radius: var(--radius);
    padding: 24px 20px;
    text-align: center;
    box-shadow: var(--shadow-sm);
  }
  .line-cta h2 {
    margin: 0 0 8px;
    font-size: 17px;
    font-weight: 900;
    color: var(--navy);
  }
  .line-cta p {
    margin: 0 0 16px;
    font-size: 13px;
    color: var(--muted);
    line-height: 1.75;
  }
  .btn-line {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 14px 28px;
    background: #06c755;
    color: #fff;
    border: none;
    border-radius: 12px;
    font-family: inherit;
    font-size: 15px;
    font-weight: 700;
    text-decoration: none;
    box-shadow: 0 6px 20px -6px rgba(6, 199, 85, 0.5);
    transition: transform .15s, box-shadow .15s;
  }
  .btn-line:hover,
  .btn-line:focus-visible {
    transform: translateY(-1px);
    box-shadow: 0 8px 24px -6px rgba(6, 199, 85, 0.55);
    outline: none;
  }
  .btn-line svg {
    width: 22px;
    height: 22px;
    flex: none;
  }"""

    return f"""
  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; scroll-padding-top: 64px; }}
  body {{
    margin: 0;
    font-family: "Noto Sans JP", system-ui, sans-serif;
    color: var(--ink);
    background: var(--paper);
    -webkit-font-smoothing: antialiased;
    line-height: 1.65;
  }}
  .wrap {{
    max-width: 720px;
    margin: 0 auto;
    padding: 0 16px 80px;
  }}
{banner}
  .hero {{
    position: relative;
    margin: 0 -16px;
    background: #fff;
    line-height: 0;
  }}
  .hero img {{
    width: 100%;
    height: auto;
    display: block;
  }}
  .hero-hotspots {{
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.5%;
    padding: 0 5.5% 7.5%;
    height: 22%;
  }}
  .hero-hotspot {{
    display: block;
    border-radius: 12px;
    text-decoration: none;
    transition: background .2s, box-shadow .2s;
  }}
  .hero-hotspot:hover,
  .hero-hotspot:focus-visible {{
    background: rgba({rgb_placeholder}, 0.08);
    box-shadow: inset 0 0 0 2px rgba({rgb_placeholder}, 0.35);
    outline: none;
  }}
  .hero-hotspot span {{
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
  }}
  .sitenav {{
    position: sticky;
    top: 0;
    z-index: 50;
    margin: 0 -16px 20px;
    padding: 10px 16px;
    background: rgba(248, 250, 252, 0.92);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--line);
  }}
  .sitenav-track {{
    display: flex;
    gap: 8px;
    overflow-x: auto;
    scrollbar-width: none;
    -webkit-overflow-scrolling: touch;
  }}
  .sitenav-track::-webkit-scrollbar {{ display: none; }}
  .sitenav a {{
    flex: 0 0 auto;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 8px 14px;
    border-radius: 999px;
    border: 1px solid var(--line);
    background: #fff;
    color: var(--muted);
    font-size: 12px;
    font-weight: 700;
    text-decoration: none;
    white-space: nowrap;
    transition: background .2s, border-color .2s, color .2s;
  }}
  .sitenav a:hover,
  .sitenav a.is-active {{
    background: var(--teal-soft);
    border-color: var(--teal-light);
    color: var(--teal);
  }}
  .sitenav-dot {{
    width: 7px;
    height: 7px;
    border-radius: 50%;
    flex: none;
  }}
  .sitenav a[data-nav="serial"] .sitenav-dot {{ background: var(--teal); }}
  .sitenav a[data-nav="mix"] .sitenav-dot {{ background: #6366f1; }}
  .sitenav a[data-nav="final"] .sitenav-dot {{ background: #f59e0b; }}
  .sitenav a[data-nav="line"] .sitenav-dot {{ background: #06c755; }}
  .intro {{
    margin-top: 4px;
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 20px 18px;
    box-shadow: var(--shadow-sm);
  }}
  .intro-kicker {{
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .14em;
    color: var(--teal);
    margin-bottom: 6px;
  }}
  .intro h1 {{
    margin: 0 0 10px;
    font-size: 20px;
    font-weight: 900;
    color: var(--navy);
    letter-spacing: .02em;
  }}
  .intro p {{
    margin: 0;
    font-size: 14px;
    color: var(--muted);
    line-height: 1.8;
  }}
  .intro-stats {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 14px;
  }}
  .stat-chip {{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 6px 12px;
    background: var(--teal-soft);
    border: 1px solid var(--teal-border);
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    color: var(--teal);
  }}
  .stat-chip b {{
    font-size: 15px;
    font-weight: 900;
    color: var(--navy);
  }}
  .section {{
    margin-top: 28px;
    scroll-margin-top: 72px;
  }}
  .section-head {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 14px;
  }}
  .section-num {{
    flex: none;
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 900;
    color: #fff;
  }}
  .section-num--serial {{ background: linear-gradient(135deg, var(--teal), var(--teal-banner-end)); }}
  .section-num--mix {{ background: linear-gradient(135deg, #6366f1, #4f46e5); }}
  .section-num--final {{ background: linear-gradient(135deg, #f59e0b, #d97706); }}
  .section-title {{
    margin: 0;
    font-size: 18px;
    font-weight: 900;
    color: var(--navy);
    line-height: 1.35;
  }}
  .section-desc {{
    margin: 4px 0 0;
    font-size: 13px;
    color: var(--muted);
    line-height: 1.7;
  }}
  .jump-bar {{
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 14px;
  }}
  .jump-btn {{
    padding: 6px 11px;
    border: 1px solid var(--line);
    border-radius: 8px;
    background: #fff;
    font-family: inherit;
    font-size: 11px;
    font-weight: 700;
    color: var(--muted);
    cursor: pointer;
    transition: background .15s, border-color .15s, color .15s;
  }}
  .jump-btn:hover,
  .jump-btn:focus-visible {{
    background: var(--teal-soft);
    border-color: var(--teal-light);
    color: var(--teal);
    outline: none;
  }}
  .test-grid {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 10px;
  }}
  @media (min-width: 540px) {{
    .test-grid {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
  }}
  .test-card {{
    display: flex;
    flex-direction: column;
    gap: 4px;
    padding: 14px 12px;
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: var(--radius-sm);
    text-decoration: none;
    color: inherit;
    box-shadow: var(--shadow-sm);
    transition: transform .15s, border-color .15s, box-shadow .15s;
    position: relative;
    overflow: hidden;
  }}
  .test-card::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: var(--teal);
    opacity: 0;
    transition: opacity .15s;
  }}
  .test-card--mix::before {{ background: #6366f1; }}
  .test-card--final::before {{ background: #f59e0b; }}
  .test-card:hover,
  .test-card:focus-visible {{
    transform: translateY(-2px);
    border-color: var(--teal-light);
    box-shadow: var(--shadow);
    outline: none;
  }}
  .test-card:hover::before,
  .test-card:focus-visible::before {{ opacity: 1; }}
  .test-card--mix:hover,
  .test-card--mix:focus-visible {{ border-color: #818cf8; }}
  .test-card--final:hover,
  .test-card--final:focus-visible {{ border-color: #fbbf24; }}
{locked}
  .test-card-no {{
    font-size: 10px;
    font-weight: 700;
    letter-spacing: .06em;
    color: var(--teal);
  }}
  .test-card--mix .test-card-no {{ color: #6366f1; }}
  .test-card--final .test-card-no {{ color: #d97706; }}
  .test-card-range {{
    font-size: 14px;
    font-weight: 700;
    color: var(--navy);
    line-height: 1.35;
  }}
  .test-card-action {{
    display: flex;
    align-items: center;
    gap: 4px;
    margin-top: 4px;
    font-size: 11px;
    font-weight: 700;
    color: var(--muted);
  }}
  .test-card-action svg {{
    width: 14px;
    height: 14px;
    flex: none;
  }}
  .test-card:hover .test-card-action,
  .test-card:focus-visible .test-card-action {{ color: var(--teal); }}
  .test-card--mix:hover .test-card-action,
  .test-card--mix:focus-visible .test-card-action {{ color: #6366f1; }}
  .test-card--final:hover .test-card-action,
  .test-card--final:focus-visible .test-card-action {{ color: #d97706; }}
  .final-grid {{
    display: grid;
    grid-template-columns: 1fr;
    gap: 10px;
  }}
  @media (min-width: 480px) {{
    .final-grid {{ grid-template-columns: repeat(3, 1fr); }}
  }}
  .final-card {{
    padding: 20px 16px;
    text-align: center;
  }}
  .final-card .test-card-range {{
    font-size: 16px;
  }}
{line_cta}
  .foot {{
    margin-top: 40px;
    text-align: center;
    font-size: 11px;
    color: var(--muted);
    letter-spacing: .08em;
    line-height: 1.8;
  }}
  @media (prefers-reduced-motion: reduce) {{
    html {{ scroll-behavior: auto; }}
    .test-card:hover {{ transform: none; }}
    .btn-line:hover {{ transform: none; }}
  }}"""


def js_block(
    slug: str,
    serial_tests: list[dict],
    mix_tests: list[dict],
    final_tests: list[dict],
    sample: bool,
) -> str:
    serial_json = json.dumps(serial_tests, ensure_ascii=False)
    mix_json = json.dumps(mix_tests, ensure_ascii=False)
    final_json = json.dumps(final_tests, ensure_ascii=False)
    serial_step = 5 if len(serial_tests) > 15 else 3
    mix_step = 3

    if sample:
        card_fn = """
  function createTestCard(test, type) {
    var free = isFreeTest(type, test);
    var el;
    var extraClass = type === "mix" ? " test-card--mix" : type === "final" ? " test-card--final final-card" : "";

    if (free) {
      el = document.createElement("a");
      el.className = "test-card test-card--sample" + extraClass;
      el.href = PDF_BASE + test.file;
      el.target = "_blank";
      el.rel = "noopener noreferrer";
    } else {
      el = document.createElement("div");
      el.className = "test-card test-card--locked" + extraClass;
      el.setAttribute("aria-disabled", "true");
    }
    el.id = test.anchor;

    if (free) {
      var badge = document.createElement("span");
      badge.className = "sample-badge";
      badge.textContent = "無料";
      el.appendChild(badge);
    }

    var no = document.createElement("span");
    no.className = "test-card-no";
    no.textContent = type === "final" ? "FINAL" : ("TEST " + String(test.no).padStart(2, "0"));

    var range = document.createElement("span");
    range.className = "test-card-range";
    range.textContent = test.label;

    var action = document.createElement("span");
    action.className = "test-card-action";
    action.innerHTML = free
      ? (PDF_ICON + " PDFを開く")
      : (LOCK_ICON + " 購入者限定");

    el.appendChild(no);
    el.appendChild(range);
    el.appendChild(action);
    return el;
  }"""
        sample_vars = """
  var IS_SAMPLE = true;

  function isFreeTest(type, test) {
    if (!IS_SAMPLE) return true;
    if (type === "serial") return test.no === 1;
    if (type === "mix") return test.no === 1;
    return false;
  }"""
        sections = '["serial", "mix", "final"]'
    else:
        card_fn = """
  function createTestCard(test, type) {
    var a = document.createElement("a");
    a.className = "test-card" + (type === "mix" ? " test-card--mix" : type === "final" ? " test-card--final final-card" : "");
    a.href = PDF_BASE + test.file;
    a.target = "_blank";
    a.rel = "noopener noreferrer";
    a.id = test.anchor;

    var no = document.createElement("span");
    no.className = "test-card-no";
    no.textContent = type === "final" ? "FINAL" : ("TEST " + String(test.no).padStart(2, "0"));

    var range = document.createElement("span");
    range.className = "test-card-range";
    range.textContent = test.label;

    var action = document.createElement("span");
    action.className = "test-card-action";
    action.innerHTML = PDF_ICON + " PDFを開く";

    a.appendChild(no);
    a.appendChild(range);
    a.appendChild(action);
    return a;
  }"""
        sample_vars = ""
        sections = '["serial", "mix", "final", "line"]'

    return f"""(function () {{
  var PDF_BASE = "/test/{slug}/";
{sample_vars}

  var PDF_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>';
  var LOCK_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>';

  var SERIAL_TESTS = {serial_json};
  var MIX_TESTS = {mix_json};
  var FINAL_TESTS = {final_json};
{card_fn}

  function renderJumpBar(container, tests, step) {{
    container.innerHTML = "";
    for (var i = 0; i < tests.length; i += step) {{
      (function (test) {{
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "jump-btn";
        btn.textContent = test.label.replace(/^MIX /, "").replace(/^No\\./, "");
        btn.addEventListener("click", function () {{
          var target = document.getElementById(test.anchor);
          if (target) target.scrollIntoView({{ behavior: "smooth", block: "center" }});
        }});
        container.appendChild(btn);
      }})(tests[i]);
    }}
  }}

  var serialGrid = document.getElementById("serial-grid");
  SERIAL_TESTS.forEach(function (t) {{
    serialGrid.appendChild(createTestCard(t, "serial"));
  }});
  renderJumpBar(document.getElementById("serial-jump"), SERIAL_TESTS, {serial_step});

  var mixGrid = document.getElementById("mix-grid");
  MIX_TESTS.forEach(function (t) {{
    mixGrid.appendChild(createTestCard(t, "mix"));
  }});
  renderJumpBar(document.getElementById("mix-jump"), MIX_TESTS, {mix_step});

  var finalGrid = document.getElementById("final-grid");
  FINAL_TESTS.forEach(function (t) {{
    finalGrid.appendChild(createTestCard(t, "final"));
  }});

  var sections = {sections};
  var navLinks = document.querySelectorAll(".sitenav a[href^='#']");
  function updateNav() {{
    var scrollY = window.scrollY + 80;
    var current = sections[0];
    sections.forEach(function (id) {{
      var sectionEl = document.getElementById(id);
      if (sectionEl && sectionEl.offsetTop <= scrollY) current = id;
    }});
    navLinks.forEach(function (link) {{
      var href = link.getAttribute("href").slice(1);
      link.classList.toggle("is-active", href === current);
    }});
  }}
  window.addEventListener("scroll", updateNav, {{ passive: true }});
  updateNav();
}})();"""


def render_page(
    book: dict,
    serial_tests: list[dict],
    mix_tests: list[dict],
    final_tests: list[dict],
    sample: bool,
) -> str:
    slug = book["slug"]
    name = book["name"]
    title = book["title"]
    tagline = book["tagline"]
    total = len(serial_tests) + len(mix_tests) + len(final_tests)
    first_serial = serial_tests[0]["label"] if serial_tests else ""
    first_mix = mix_tests[0]["label"].replace("MIX ", "") if mix_tests else ""

    css_root = css_block(book).replace(
        f"    --line-url: {LINE_URL};\n  }}",
        f"    --line-url: {LINE_URL};\n"
        f"    --teal-border: {book['theme_border']};\n"
        f"    --teal-banner-end: {book['theme_banner_end']};\n"
        "  }",
        1,
    )
    styles = shared_styles(sample).replace("THEME_RGB", book["theme_rgb"])

    if sample:
        head_extra = ""
        page_title = f"{title}｜サンプル｜THINKING"
        meta_desc = (
            f"{title}のサンプルページ。連番テスト・MIXテストを1回ずつ無料でお試しいただけます。"
        )
        banner_html = (
            '<div class="sample-banner">'
            "SAMPLE — お試し版（連番・MIX 各1回のみ開放）"
            "</div>\n\n  "
        )
        intro_kicker = "SAMPLE PORTAL"
        intro_h1 = f"{title}｜サンプル"
        intro_p = (
            f"問題集の品質を確認いただけるサンプルページです。"
            f"<strong>連番テスト {first_serial}</strong>と"
            f"<strong>MIXテスト {first_mix}</strong>の2回分を無料でお試しいただけます。"
            f"それ以外は購入者限定です。"
        )
        stats_html = (
            f'<span class="stat-chip stat-chip--sample">無料 <b>2</b>回</span>\n'
            f'      <span class="stat-chip">全収録 <b>{total}</b>回</span>'
        )
        sitenav_extra = ""
        purchase_html = f"""
  <section class="purchase-note">
    <h2>全{total}回は購入者限定ポータルで</h2>
    <p>ご購入いただいた方には、連番{len(serial_tests)}回・MIX{len(mix_tests)}回・総まとめ{len(final_tests)}回のすべてにアクセスできる専用ポータルをご案内しています。</p>
  </section>"""
        line_html = ""
        footer = f"{title} サンプルページ<br>\n    合同会社ARC / THINKING"
    else:
        head_extra = '<meta name="robots" content="noindex, nofollow">\n'
        page_title = f"{name} 専用ポータル｜THINKING 問題集"
        meta_desc = (
            f"{title}ご購入者専用。連番テスト・MIXテスト・総まとめテスト"
            f"（全{total}回）のPDFにいつでもアクセスできます。"
        )
        banner_html = ""
        intro_kicker = "PURCHASER PORTAL"
        intro_h1 = f"{title}｜収録テスト一覧"
        intro_p = (
            f"ご購入ありがとうございます。このページから、全部で<strong>{total}回分</strong>の"
            f"テスト（PDF）にいつでもアクセスできます。ブックマーク推奨です。"
            f"今後、追加・改訂した分もこのページに反映されます。"
        )
        stats_html = (
            f'<span class="stat-chip">連番 <b>{len(serial_tests)}</b>回</span>\n'
            f'      <span class="stat-chip">MIX <b>{len(mix_tests)}</b>回</span>\n'
            f'      <span class="stat-chip">総まとめ <b>{len(final_tests)}</b>回</span>\n'
            f'      <span class="stat-chip">合計 <b>{total}</b>回</span>'
        )
        sitenav_extra = (
            '      <a href="#line" data-nav="line"><span class="sitenav-dot"></span>LINEで連絡</a>\n'
        )
        purchase_html = ""
        line_html = f"""
  <section class="line-cta" id="line">
    <h2>ご要望・お問い合わせ</h2>
    <p>問題の誤り、追加のご希望、その他リクエストがあれば<br>下のボタンからLINEでお気軽にどうぞ。</p>
    <a class="btn-line" href="{LINE_URL}" target="_blank" rel="noopener noreferrer">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M19.365 9.863c.349 0 .63.285.63.631 0 .345-.281.63-.63.63H17.61v1.125h1.755c.349 0 .63.283.63.63 0 .344-.281.629-.63.629h-2.386c-.345 0-.627-.285-.627-.629V8.108c0-.345.282-.63.63-.63h2.386c.346 0 .627.285.627.63 0 .349-.281.63-.63.63H17.61v1.125h1.755zm-3.855 3.016c0 .27-.174.51-.432.596-.064.021-.133.031-.199.031-.211 0-.391-.09-.51-.25l-2.443-3.317v2.94c0 .344-.279.629-.631.629-.346 0-.626-.285-.626-.629V8.108c0-.27.173-.51.43-.595.06-.023.136-.033.194-.033.195 0 .375.104.495.254l2.462 3.33V8.108c0-.345.282-.63.63-.63.345 0 .63.285.63.63v4.771zm-5.741 0c0 .344-.282.629-.631.629-.345 0-.627-.285-.627-.629V8.108c0-.345.282-.63.63-.63.346 0 .628.285.628.63v4.771zm-2.466.629H4.917c-.345 0-.63-.285-.63-.629V8.108c0-.345.285-.63.63-.63.348 0 .63.285.63.63v4.141h1.756c.348 0 .629.283.629.63 0 .344-.282.629-.629.629M24 10.314C24 4.943 18.615.572 12 .572S0 4.943 0 10.314c0 4.811 4.27 8.842 10.035 9.608.391.082.923.258 1.058.59.12.301.079.766.038 1.08l-.164 1.02c-.045.301-.24 1.186 1.049.645 1.291-.539 6.916-4.078 9.436-6.975C23.176 14.393 24 12.458 24 10.314"/></svg>
      LINEで連絡する
    </a>
  </section>"""
        footer = f"{title} 購入者専用ポータル<br>\n    合同会社ARC / THINKING"

    serial_desc = f"{book['chunk_label']}／{book['serial_desc']}"

    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="{book["theme"]}">
{head_extra}<title>{page_title}</title>
<meta name="description" content="{meta_desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>
{css_root}
{styles}
</style>
</head>
<body>

<div class="wrap">

  {banner_html}<header class="hero">
    <img src="../assets/hero.png" alt="{name} 専用ポータル — {tagline}" width="1200" height="800">
    <nav class="hero-hotspots" aria-label="メインメニュー">
      <a class="hero-hotspot" href="#serial"><span>単語学習（連番テスト）</span></a>
      <a class="hero-hotspot" href="#mix"><span>復習（MIXテスト）</span></a>
      <a class="hero-hotspot" href="#final"><span>確認テスト（総まとめ）</span></a>
    </nav>
  </header>

  <nav class="sitenav" aria-label="ページ内ナビ">
    <div class="sitenav-track">
      <a href="#serial" data-nav="serial"><span class="sitenav-dot"></span>連番テスト</a>
      <a href="#mix" data-nav="mix"><span class="sitenav-dot"></span>MIXテスト</a>
      <a href="#final" data-nav="final"><span class="sitenav-dot"></span>総まとめ</a>
{sitenav_extra}    </div>
  </nav>

  <div class="intro">
    <div class="intro-kicker">{intro_kicker}</div>
    <h1>{intro_h1}</h1>
    <p>{intro_p}</p>
    <div class="intro-stats">
      {stats_html}
    </div>
  </div>

  <section class="section" id="serial">
    <div class="section-head">
      <div class="section-num section-num--serial">①</div>
      <div>
        <h2 class="section-title">連番テスト</h2>
        <p class="section-desc">{serial_desc}</p>
      </div>
    </div>
    <div class="jump-bar" id="serial-jump" aria-label="連番テスト ジャンプ"></div>
    <div class="test-grid" id="serial-grid"></div>
  </section>

  <section class="section" id="mix">
    <div class="section-head">
      <div class="section-num section-num--mix">②</div>
      <div>
        <h2 class="section-title">MIXテスト</h2>
        <p class="section-desc">100語ずつ／順番を混ぜた実力チェック。「並び順で覚えた気」を防ぎ、本当に定着しているかを炙り出します。模試前の総ざらいに最適。</p>
      </div>
    </div>
    <div class="jump-bar" id="mix-jump" aria-label="MIXテスト ジャンプ"></div>
    <div class="test-grid" id="mix-grid"></div>
  </section>

  <section class="section" id="final">
    <div class="section-head">
      <div class="section-num section-num--final">③</div>
      <div>
        <h2 class="section-title">総まとめテスト</h2>
        <p class="section-desc">全範囲からのファイナルチェック。入試直前・模試直前の最終確認に。</p>
      </div>
    </div>
    <div class="final-grid" id="final-grid"></div>
  </section>
{purchase_html}{line_html}
  <footer class="foot">
    {footer}
  </footer>

</div>

<script>
{js_block(slug, serial_tests, mix_tests, final_tests, sample)}
</script>
</body>
</html>
"""


def render_index(book: dict) -> str:
    slug = book["slug"]
    title = book["title"]
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}｜THINKING</title>
<meta http-equiv="refresh" content="0;url=/{slug}/sample/">
<link rel="canonical" href="https://thinking-online.com/{slug}/sample/">
<script>location.replace("/{slug}/sample/");</script>
</head>
<body>
<p><a href="/{slug}/sample/">{title}サンプルへ</a></p>
</body>
</html>
"""


def main() -> None:
    for book in BOOKS:
        slug = book["slug"]
        serial, mix, final = parse_tests(slug, book.get("pdf_prefix"))
        book_dir = ROOT / slug
        assets_dir = book_dir / "assets"
        sample_dir = book_dir / "sample"
        purchaser_dir = book_dir / book["secret"]

        assets_dir.mkdir(parents=True, exist_ok=True)
        sample_dir.mkdir(parents=True, exist_ok=True)
        purchaser_dir.mkdir(parents=True, exist_ok=True)

        hero_src = ASSETS_SRC / book["hero_file"]
        hero_dst = assets_dir / "hero.png"
        if hero_src.exists():
            shutil.copy2(hero_src, hero_dst)
            print(f"Copied hero: {hero_dst}")
        else:
            print(f"WARNING: hero not found: {hero_src}")

        (book_dir / "index.html").write_text(render_index(book), encoding="utf-8")
        (sample_dir / "index.html").write_text(
            render_page(book, serial, mix, final, sample=True), encoding="utf-8"
        )
        (purchaser_dir / "index.html").write_text(
            render_page(book, serial, mix, final, sample=False), encoding="utf-8"
        )

        total = len(serial) + len(mix) + len(final)
        print(
            f"{slug}: serial={len(serial)} mix={len(mix)} final={len(final)} "
            f"total={total} purchaser=/{slug}/{book['secret']}/"
        )


if __name__ == "__main__":
    main()
