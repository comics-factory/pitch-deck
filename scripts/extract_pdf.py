#!/usr/bin/env python3
"""Extract text from ECC PDF using PyMuPDF."""
import fitz  # PyMuPDF
import json
from pathlib import Path

def extract_pdf_text(pdf_path: str):
    """Extract text from PDF slides."""
    doc = fitz.open(pdf_path)
    slides_data = []
    
    for page_num, page in enumerate(doc, 1):
        text = page.get_text()
        
        # Split into lines and clean
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        # Filter out common footer patterns
        lines = [l for l in lines if not l.startswith('© Copyright') and 
                 not l.startswith('Showeet.com') and
                 l not in ['Creative & Free PowerPoint Templates']]
        
        slide_info = {
            "slide_number": page_num,
            "text": lines,
            "full_text": "\n".join(lines)
        }
        
        slides_data.append(slide_info)
        
        if lines:
            print(f"Slide {page_num}:")
            for line in lines[:5]:  # First 5 lines
                print(f"  {line}")
            if len(lines) > 5:
                print(f"  ... ({len(lines) - 5} more lines)")
            print()
    
    doc.close()
    return slides_data

if __name__ == "__main__":
    data = extract_pdf_text("presentations/ECC Pitch Deck.pdf")
    
    # Save to JSON
    output_path = Path("assets/extracted_ecc/pdf_content.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Saved to {output_path}")
