#!/usr/bin/env python3
"""
Conversión simple PDF → Markdown SIN IA
"""
import fitz
import pymupdf4llm
from pathlib import Path
import sys

def pdf_to_markdown(pdf_path):
    """Convierte PDF a Markdown básico"""
    with fitz.open(pdf_path) as doc:
        md_text = pymupdf4llm.to_markdown(doc)
    return md_text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python convertir-pdf-simple.py archivo.pdf")
        sys.exit(1)
    
    pdf_file = Path(sys.argv[1])
    md_text = pdf_to_markdown(pdf_file)
    
    # Guardar
    output_file = pdf_file.with_suffix('.md')
    output_file.write_text(md_text, encoding='utf-8')
    
    print(f"✅ Convertido: {output_file}")
