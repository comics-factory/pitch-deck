# Build Guide - Enhanced Pitch Deck

## Overview

The pitch deck now uses the website's design system with:
- **Dark gradient backgrounds** (#0a0a0a to #1a1a1a)
- **Lime yellow accents** (#eaff6b) for titles
- **Vibrant color palette** from comicsfactory.tech
  - Purple (#7f5af0), Pink (#f15bb5), Cyan (#00cfff), Green (#2cb67d)
- **Inter font family** for professional typography
- **Improved image positioning** with proper sizing and layouts
- **Logo integration** from website assets

## Quick Start

Build the deck with the enhanced Marp theme:

```bash
# Using uv (recommended)
uv run python scripts/build.py --deck investor --product comics-factory --engine marp
```

## Output Files

The build generates:
- `dist/comics-factory-investor.html` - Interactive HTML presentation with full styling
- `dist/comics-factory-investor.marp.md` - Rendered Markdown with product data

## Viewing the Deck

### HTML (Best Option)
Open `dist/comics-factory-investor.html` in any web browser for the fully styled presentation.

### Generate PDF/PPTX (Requires Browser)
To export PDF or PPTX, you need a browser installed (Chrome, Firefox, or Edge):

```bash
# Install Chromium (example for Debian/Ubuntu)
sudo apt install chromium-browser

# Then build with Marp
uv run python scripts/build.py --deck investor --product comics-factory --engine marp
```

Marp will automatically generate:
- PDF with all styling preserved
- PPTX for PowerPoint editing

## Design Elements

### Colors from Website
- **Background**: Dark gradient (#0a0a0a → #1a1a1a)
- **Primary text**: Light grey (#cccccc)
- **Headings**: Lime yellow (#eaff6b)
- **Accents**: Purple, Pink, Cyan, Green
- **Code blocks**: Dark (#222) with lime text

### Typography
- **Font**: Inter (Google Fonts)
- **H1**: 64px with purple underline
- **H2**: 48px with glow effect
- **Body**: 26px, line-height 1.6

### Layout Features
- **Two-column layouts** for demo slides
- **Emphasis boxes** with gradient backgrounds
- **Rounded images** with shadows
- **Logo placement** on title and thank you slides

## Customization

### Modify Theme
Edit `themes/marp-theme.css` to adjust:
- Colors and gradients
- Font sizes
- Spacing and padding
- Image styling

### Update Content
Edit `decks/investor/deck.md` to change:
- Slide structure
- Image sizes (`![w:300]` for width)
- Column layouts
- Emphasis blocks

### Change Product Data
Edit `products/comics-factory.yaml` to update:
- Problem statements
- Solutions
- Market data
- Team information

## Assets

Website assets copied to main assets folder:
- `assets/logo.svg` - Company logo
- `assets/hesdi.jpg` - Sample character photo
- `assets/qr_code.png` - QR code

Comic demo assets:
- `assets/comics/manga.jpg` - Manga input
- `assets/comics/children_book.JPG` - Children's book input
- `assets/comics/children_book_page_1.png` - Generated output

## Technology Stack

- **Marp CLI**: Modern Markdown to presentation converter
- **Jinja2**: Template rendering for product data
- **uv**: Fast Python package management
- **CSS**: Custom theme matching website design

## Troubleshooting

### Images not displaying
**Fixed!** Images now use correct relative paths (`../assets/`) from the `dist/` folder.
- Verify files exist in `assets/` folder
- HTML references use `../assets/` prefix
- Image formats must be web-compatible (JPG, PNG, SVG, not PDF)

### "No suitable browser found"
Install Chrome, Firefox, or Edge to enable PDF/PPTX export. HTML output always works without a browser.

### Theme not applied
Verify `theme: comics-factory` is in the frontmatter and `themes/marp-theme.css` exists.

## Next Steps

1. **View the HTML** - Open `dist/comics-factory-investor.html` to see the enhanced styling
2. **Install a browser** - For PDF/PPTX export if needed
3. **Customize** - Adjust colors, layouts, and content to your needs
4. **Present** - Use HTML in browser presentation mode or export to your preferred format
