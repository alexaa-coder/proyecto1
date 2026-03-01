# convert_derecho_pymupdf.py
# Conversor PDF -> Markdown usando pymupdf4llm
# Solo procesa la carpeta pdf/Derecho
# Requiere: pip install pymupdf4llm python-slugify

from pathlib import Path
import pymupdf4llm
from slugify import slugify  # opcional, puedes usar simple_slug

def simple_slug(text):
    """Slug básico si no quieres usar la librería slugify"""
    return text.lower().replace(" ", "-").replace(".", "-").replace("_", "-")

def get_frontmatter(file_path: Path):
    """Genera frontmatter YAML para Docusaurus"""
    doc_id = slugify(file_path.stem)
    title = file_path.stem.replace("_", " ").replace("-", " ").title()
    return f"""---
id: {doc_id}
title: {title}
sidebar_label: {title}
---

"""

def process_derecho_pdf(input_dir: Path, output_dir: Path):
    print(f"🔄 Procesando PDFs en: {input_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = list(input_dir.glob("*.pdf"))
    if not pdf_files:
        print("❌ No se encontraron PDFs en Derecho.")
        return

    for pdf_path in pdf_files:
        try:
            dest_path = output_dir / pdf_path.with_suffix(".md").name
            print(f"📖 Convirtiendo {pdf_path.name}...")
            # Convertir PDF a Markdown con pymupdf4llm
            md_content = pymupdf4llm.to_markdown(pdf_path)
            # Añadir frontmatter
            final_content = get_frontmatter(pdf_path) + md_content
            dest_path.write_text(final_content, encoding="utf-8")
            print(f"✅ Guardado en: {dest_path}")
        except Exception as e:
            print(f"❌ Error convirtiendo {pdf_path.name}: {e}")

if __name__ == "__main__":
    DERECHO_DIR = Path("pdf/Derecho")         # Carpeta con PDFs de Derecho
    OUTPUT_DIR = Path("pdf/output")           # Carpeta de salida
    process_derecho_pdf(DERECHO_DIR, OUTPUT_DIR)
