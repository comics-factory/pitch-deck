import yaml
import jinja2
import argparse
import os
import subprocess

def build_deck(deck_type, product_id):
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

    # Save rendered markdown
    rendered_path = f"dist/{product_id}-{deck_type}.rendered.md"
    with open(rendered_path, 'w') as f:
        f.write(rendered_md)

    # Run Marp CLI
    output_pptx = f"dist/{product_id}-{deck_type}.pptx"
    output_pdf = f"dist/{product_id}-{deck_type}.pdf"
    theme_path = "themes/marp-theme.css"

    print(f"Generating PPTX: {output_pptx}")
    subprocess.run([
        "npx", "@marp-team/marp-cli@latest",
        rendered_path,
        "-o", output_pptx,
        "--theme", theme_path
    ])

    print(f"Generating PDF: {output_pdf}")
    subprocess.run([
        "npx", "@marp-team/marp-cli@latest",
        rendered_path,
        "-o", output_pdf,
        "--theme", theme_path
    ])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--deck", required=True)
    parser.add_argument("--product", required=True)
    args = parser.parse_args()

    build_deck(args.deck, args.product)
