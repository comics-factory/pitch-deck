# Image Display Fix - Summary

## Problem
Images were not displaying in the HTML presentation because:
1. **Incorrect relative paths** - Markdown used `assets/` instead of `../assets/` 
2. **PDF as image** - manga.pdf cannot be embedded as an image in HTML

## Solution Applied

### 1. Fixed Image Paths in Deck Template
Updated `decks/investor/deck.md` to use `../` prefix:
```markdown
![w:300](../{{ demo.input_image }})
![w:550](../{{ demo.output_image }})
```

This ensures paths work from `dist/` folder where HTML is generated.

### 2. Updated Product YAML
Changed `products/ai-storybook.yaml`:
- **Before:** `output_image: "assets/comics/manga.pdf"` ❌
- **After:** `output_image: "assets/comics/manga.jpg"` ✅
- Added note about PDF version availability

### 3. Verified Image Files
All images exist and are accessible:
```
assets/logo.svg                        (542 bytes)  - Company logo
assets/comics/manga.jpg                (110 KB)    - Manga demo
assets/comics/children_book.JPG        (1.2 MB)    - Children's book input
assets/comics/children_book_page_1.png (609 KB)    - Children's book output
```

## Current HTML Output

The HTML now contains **6 properly referenced images**:
1. Logo on title slide (150px width)
2. Manga input (300px)
3. Manga output (550px)  
4. Children's book input (300px)
5. Children's book output (550px)
6. Logo on thank you slide (120px)

Plus emoji icons from CDN.

## How to View

Open the updated presentation:
```bash
# In browser
open dist/ai-storybook-investor.html

# Or rebuild
uv run python scripts/build.py --deck investor --product ai-storybook --engine marp
```

## File Structure
```
pitch-deck/
├── dist/
│   └── ai-storybook-investor.html  ← HTML here
├── assets/
│   ├── logo.svg                     ← Images here (../)
│   └── comics/
│       ├── manga.jpg
│       ├── children_book.JPG
│       └── children_book_page_1.png
```

## What to Expect

When you open `dist/ai-storybook-investor.html`:
- ✅ Dark gradient background with website colors
- ✅ Lime yellow headings with glow
- ✅ Company logo on title and closing slides
- ✅ All demo images displaying correctly
- ✅ Two-column layout for input/output comparison
- ✅ Properly sized images (300px inputs, 550px outputs)

## Technical Details

**Path Resolution:**
- HTML location: `dist/ai-storybook-investor.html`
- Image reference: `../assets/comics/manga.jpg`
- Resolves to: `assets/comics/manga.jpg` ✓

**All image tags verified:**
```html
<img src="../assets/logo.svg" style="width:150px;" />
<img src="../assets/comics/manga.jpg" style="width:300px;" />
<img src="../assets/comics/manga.jpg" style="width:550px;" />
<img src="../assets/comics/children_book.JPG" style="width:300px;" />
<img src="../assets/comics/children_book_page_1.png" style="width:550px;" />
<img src="../assets/logo.svg" style="width:120px;" />
```

Images should now display correctly! 🎉
