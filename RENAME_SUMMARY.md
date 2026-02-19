# Renaming Summary: AI StoryBook → Comics Factory

## Files Renamed

### Product Definition
- `products/ai-storybook.yaml` → `products/comics-factory.yaml`

### Distribution Files
- `dist/ai-storybook-investor.*` → `dist/comics-factory-investor.*`
  - `.html` - Main presentation (125KB)
  - `.marp.md` - Rendered Markdown (6.8KB)
  - `.pandoc.md` - Pandoc version
  - `.pdf` - PDF export (2.2MB)
  - `.pptx` - PowerPoint export (1.8MB)
  - `.rendered.md` - Legacy rendered version

## Content Updates

### Product YAML (`products/comics-factory.yaml`)
- Updated `name: Comics Factory`
- All content references updated from "AI StoryBook" to "Comics Factory"

### Deck Template (`decks/investor/deck.md`)
- Updated header: `Comics Factory Pitch Deck`

### Documentation
- `README.md` - Updated title and build commands
- `BUILD_GUIDE.md` - Updated all file references and examples

## Removed Files

- `scripts/html_to_pdf.py` - Removed non-working HTML-to-PDF conversion script
- `dist/comics-factory-investor-updated.pdf` - Removed duplicate PDF

## Build Command

```bash
uv run python scripts/build.py --deck investor --product comics-factory
```

## Generated Outputs

- **HTML**: `dist/comics-factory-investor.html` - Full interactive presentation
- **Markdown**: `dist/comics-factory-investor.marp.md` - Source with product data
- **PDF/PPTX**: Generated via Marp CLI (requires browser)

All references to "AI StoryBook" have been replaced with "Comics Factory" across the codebase.
