# AI StoryBook Pitch Deck Generator

A professional, docs-as-source pitch deck generator using Markdown, YAML, and Python.

## Quickstart

This project uses `uv` for Python environment management.

### 1. Install Dependencies
```bash
uv venv
uv pip install -r requirements.txt
```

### 2. Build the Deck
To generate the latest pitch deck in `dist/`:
```bash
uv run python scripts/build.py --deck investor --product ai-storybook
```

## Project Structure

- `decks/`: Markdown templates for different audiences (investor, sales, etc.).
- `products/`: Single source of truth for product data (YAML).
- `themes/`: Custom CSS themes for styling.
- `scripts/`: Python build logic.
- `dist/`: Generated artifacts (PPTX, PDF).

## Customization

- **Content:** Update `products/ai-storybook.yaml`.
- **Narrative:** Modify `decks/investor/deck.md`.
- **Styling:** Edit `themes/marp-theme.css`.
