# COPILOT.md — Docs-as-source Pitch Deck Generator (CLI + Git)

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

```bash
uv venv
uv pip install -r requirements.txt
uv run python scripts/build.py
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
  - export HTML
  - upload artifacts
- On release tag:
  - build all target decks
  - publish artifacts to a release page

## 10) Prompting guidelines for COPILOT (how to behave in this repo)

When working in this repository, COPILOT should:

1. **Prefer docs-as-source**: propose changes in Markdown/YAML rather than editing PPTX by hand.
2. **Keep styling in themes/templates** (`themes/`) and avoid per-slide formatting hacks.
3. **Use virtual environments** for *any* Python command execution (§4), and include the exact commands.
4. **Never install dependencies globally**; do not modify the system Python.
5. **Produce deterministic builds**: keep commands and file paths explicit.
6. **When suggesting new automation**: add a `scripts/` entry point and document it in README.
