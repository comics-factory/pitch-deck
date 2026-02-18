import yaml
import jinja2
import argparse
import os
import subprocess
import re

def build_deck(deck_type, product_id, engine="marp"):
    # Load product data
    product_path = f"products/{product_id}.yaml"
    with open(product_path, 'r') as f:
        product_data = yaml.safe_load(f)

    # Load deck template
    template_path = f"decks/{deck_type}/deck.md"
    with open(template_path, 'r') as f:
        template_content = f.read()

    # Render template
    template = jinja2.Template(template_content)
    rendered_md = template.render(product=product_data)

    # Ensure dist directory exists
    os.makedirs("dist", exist_ok=True)

    if engine == "marp":
        # Save rendered markdown for Marp
        rendered_path = f"dist/{product_id}-{deck_type}.marp.md"
        with open(rendered_path, 'w') as f:
            f.write(rendered_md)

        output_pdf = f"dist/{product_id}-{deck_type}.pdf"
        output_pptx = f"dist/{product_id}-{deck_type}.pptx"
        output_html = f"dist/{product_id}-{deck_type}.html"
        theme_css = "themes/marp-theme.css"

        # Generate PDF via Marp CLI
        print(f"Generating PDF via Marp CLI: {output_pdf}")
        subprocess.run([
            "npx", "@marp-team/marp-cli@latest",
            rendered_path,
            "-o", output_pdf,
            "--theme", theme_css,
            "--allow-local-files"
        ], check=True)

        # Generate PPTX via Marp CLI
        print(f"Generating PPTX via Marp CLI: {output_pptx}")
        subprocess.run([
            "npx", "@marp-team/marp-cli@latest",
            rendered_path,
            "-o", output_pptx,
            "--theme", theme_css,
            "--allow-local-files"
        ], check=True)

        # Generate HTML for preview
        print(f"Generating HTML via Marp CLI: {output_html}")
        subprocess.run([
            "npx", "@marp-team/marp-cli@latest",
            rendered_path,
            "-o", output_html,
            "--theme", theme_css,
            "--allow-local-files"
        ], check=True)

    else:  # pandoc engine (legacy)
        # Pre-process Markdown for Pandoc
        # 1. Remove Marp frontmatter and directives
        rendered_md = re.sub(r'^---\nmarp: true.*?\n---\n', '', rendered_md, flags=re.DOTALL)
        rendered_md = re.sub(r'<!--.*?-->', '', rendered_md)
        
        # 2. Handle HTML divs (like .highlight) -> Convert to Blockquotes for simplicity
        rendered_md = rendered_md.replace('<div class="highlight">', '> **').replace('</div>', '**')

        # Save rendered markdown for Pandoc
        rendered_path = f"dist/{product_id}-{deck_type}.pandoc.md"
        with open(rendered_path, 'w') as f:
            f.write(rendered_md)

        output_pdf = f"dist/{product_id}-{deck_type}.pdf"
        output_pptx = f"dist/{product_id}-{deck_type}.pptx"
        theme_tex = "themes/beamer_theme.tex"

        # PDF via Pandoc + Beamer (XeLaTeX for fonts/colors)
        print(f"Generating PDF via Pandoc + XeLaTeX: {output_pdf}")
        subprocess.run([
            "pandoc",
            rendered_path,
            "-t", "beamer",
            "--pdf-engine=xelatex",
            "-H", theme_tex,
            "-V", "aspectratio:169",
            "-o", output_pdf
        ], check=True)

        # PPTX via Pandoc
        print(f"Generating PPTX via Pandoc: {output_pptx}")
        # Note: PPTX styling is limited without a reference doc, but we get the content.
        subprocess.run([
            "pandoc",
            rendered_path,
            "-o", output_pptx
        ], check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--deck", required=True)
    parser.add_argument("--product", required=True)
    parser.add_argument("--engine", default="marp", choices=["marp", "pandoc"])
    args = parser.parse_args()

    build_deck(args.deck, args.product, args.engine)