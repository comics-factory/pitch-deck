# GEMINI.md — Docs-as-source Pitch Deck Generator (CLI + Git)

> **Goal:** Generate professional, consistent pitch decks from **Markdown (docs-as-source)** stored in Git, exporting to **PPTX/PDF** via CLI.

## 1) Guiding principles

- **Docs-as-source**: Slide content lives in Markdown and is versioned in Git.
- **Design-as-code**: A small set of themes/templates controls look & feel (no ad-hoc styling per deck).
- **Repeatable builds**: A single CLI command builds the deck identically on any machine/CI.
- **Content model**: Product facts are structured (YAML/JSON) and rendered into slides.
- **Demo site with aesthetics**: https://comicsfactory.tech/
- **Virtual environments only**: Any code execution must happen inside an isolated virtual environment using `uv`.

## 2) Recommended toolchain

These are recommendations based on conversations I've done, also with other LLMs. Take into account, if applicable or offer a better solution:

### Option A — Marp CLI (Markdown → PPTX/PDF/HTML)
- Marp CLI converts Marp/Marpit Markdown into **PowerPoint (PPTX)** and other formats from the command line. citeturn1search15turn1search17
- Use it when you want clean Markdown authoring + CSS theme control.

### Option B — Pandoc (Markdown → PPTX) + reference.pptx
- Pandoc can generate **PPTX** from Markdown (`-t pptx`) and lets you apply a **reference PPTX** to control styling. citeturn1search22turn1search24
- Use it when you want maximal conversion flexibility and a PowerPoint-authored reference template.

> **Recommendation:** Start with **Marp CLI** for fastest iteration; add **Pandoc** later if you need more PowerPoint-native layout semantics.

## 3) Repository layout (suggested)

```
.
├─ decks/
│  ├─ investor/
│  │  ├─ deck.md
│  │  └─ deck.yaml
│  ├─ sales/
│  │  ├─ deck.md
│  │  └─ deck.yaml
│  └─ partner/
│     ├─ deck.md
│     └─ deck.yaml
├─ products/
│  ├─ acme-analytics.yaml
│  └─ ...
├─ themes/
│  ├─ marp-theme.css
│  └─ reference.pptx
├─ assets/
│  ├─ brand/
│  ├─ logos/
│  └─ screenshots/
├─ scripts/
│  ├─ build.py
│  └─ validate.py
├─ dist/
└─ README.md
```

### Content model
- `products/*.yaml` contains the single source of truth per product (value prop, features, proof points, metrics, links, images).
- `decks/*/deck.md` is the narrative for that audience.
- `decks/*/deck.yaml` holds deck-level settings (title, product id, locale, region, speaker notes toggle, etc.).

## 4) **MANDATORY**: Virtual environments for any code execution

When running or generating anything via Python scripts:

1. **Create a virtual environment** (do not use system Python):

```bash
python -m venv .venv
```

2. **Activate it**:

- macOS/Linux:

```bash
source .venv/bin/activate
```

- Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

3. **Install dependencies inside the venv only**:

```bash
python -m pip install -U pip
python -m pip install -r requirements.txt
```

4. **Run scripts using the venv interpreter**:

```bash
python scripts/build.py --help
```

> **Rule:** Any instruction that executes Python code must **explicitly** use the `.venv` environment.

### Optional: `uv` workflow (faster, reproducible)
If your team uses `uv`:

```bash
uv venv
uv pip install -r requirements.txt
uv run python scripts/build.py
```

## 5) Authoring slides in Markdown

### Marp frontmatter (example)

```markdown
---
marp: true
theme: custom
paginate: true
---

# {{ product.name }}

---

## Problem
- {{ product.problem_1 }}
- {{ product.problem_2 }}
```

### Slide separators
- Use `---` to split slides.
- Keep one primary message per slide.

### Assets
- Store images in `assets/` and reference with relative paths.
- Prefer SVG/PNG for logos; compress screenshots.

## 6) Build commands (CLI)

### Marp build

```bash
# Build PPTX
npx @marp-team/marp-cli@latest decks/investor/deck.md -o dist/investor.pptx --theme themes/marp-theme.css

# Build PDF
npx @marp-team/marp-cli@latest decks/investor/deck.md -o dist/investor.pdf --theme themes/marp-theme.css
```

Marp CLI supports exporting to PowerPoint and other formats via CLI. citeturn1search15turn1search17

### Pandoc build (using a reference PPTX)

```bash
pandoc decks/investor/deck.md -t pptx -o dist/investor.pptx --reference-doc=themes/reference.pptx
```

Pandoc supports PPTX output (`-t pptx`) and reference documents to influence styling. citeturn1search22turn1search24

## 7) Data binding (render product YAML into Markdown)

Use a tiny renderer to merge `products/<id>.yaml` into deck Markdown.

**Pattern:**
1) Render `deck.md` template → `dist/deck.rendered.md`
2) Convert rendered Markdown → `dist/deck.pptx`

Suggested tooling:
- Python: `jinja2` + `pyyaml`
- Node: `handlebars` + `js-yaml`

Example build script behavior:

```text
scripts/build.py
  - loads decks/<type>/deck.yaml
  - loads products/<product_id>.yaml
  - renders decks/<type>/deck.md (Jinja/Handlebars)
  - runs marp/pandoc to export
  - writes dist/<product>-<type>.pptx
```

## 8) Quality gates (highly recommended)

### Export to PDF in CI for review artifacts
If you need headless rendering to PDF for consistent review, LibreOffice can convert PPTX to PDF in headless mode. citeturn1search3

Example:

```bash
libreoffice --headless --convert-to pdf dist/investor.pptx --outdir dist/
```

### Checks
- Missing assets (broken image paths)
- Placeholder tokens left unresolved (`{{ ... }}`)
- Max text length per slide / overflow heuristics
- Spellcheck (optional)

## 9) CI/CD (example outline)

- On PR:
  - create venv
  - install deps
  - render Markdown
  - export PPTX + PDF
  - upload artifacts
- On release tag:
  - build all target decks
  - publish artifacts to a release page

## 10) Prompting guidelines for Gemini (how to behave in this repo)

When working in this repository, Gemini should:

1. **Prefer docs-as-source**: propose changes in Markdown/YAML rather than editing PPTX by hand.
2. **Keep styling in themes/templates** (`themes/`) and avoid per-slide formatting hacks.
3. **Use virtual environments** for *any* Python command execution (§4), and include the exact commands.
4. **Never install dependencies globally**; do not modify the system Python.
5. **Produce deterministic builds**: keep commands and file paths explicit.
6. **When suggesting new automation**: add a `scripts/` entry point and document it in README.

## 11) Quickstart

```bash
# 1) Create venv
python -m venv .venv
source .venv/bin/activate

# 2) Install deps
python -m pip install -U pip
python -m pip install -r requirements.txt

# 3) Build
python scripts/build.py --deck investor --product acme-analytics --engine marp

# 4) Output
ls dist/
```

---

**Notes**
- If you adopt Marp: ensure a Chromium-based browser is available on CI runners for rendering.
- If you adopt Pandoc: maintain `themes/reference.pptx` as the canonical branded reference.
