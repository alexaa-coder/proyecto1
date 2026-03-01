# convert_pdfminer_derecho.py
# Conversor PDF -> Markdown usando pdfminer.six
# Requiere: pip install pdfminer.six python-slugify

from pathlib import Path
from pdfminer.high_level import extract_text
from slugify import slugify

def get_frontmatter(file_path: Path):
    """Genera la cabecera YAML para Docusaurus"""
    doc_id = slugify(file_path.stem)
    title = file_path.stem.replace("_", " ").replace("-", " ").title()
    return f"""---
id: {doc_id}
title: {title}
sidebar_label: {title}
---

"""

def pdf_to_markdown(pdf_path: Path) -> str:
    """Convierte un PDF a Markdown con pdfminer"""
    text = extract_text(pdf_path)
    # Limpieza mínima: saltos de línea dobles entre párrafos
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    return "\n\n".join(paragraphs)

def process_derecho_pdf(input_dir: Path, output_dir: Path):
    print(f"🔄 Buscando PDFs en: {input_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = list(input_dir.glob("*.pdf"))
    if not pdf_files:
        print("❌ No se encontraron PDFs en Derecho.")
        return

    for pdf_path in pdf_files:
        try:
            dest_path = output_dir / pdf_path.with_suffix(".md").name
            print(f"📖 Convirtiendo {pdf_path.name}...")
            md_content = pdf_to_markdown(pdf_path)
            final_content = get_frontmatter(pdf_path) + md_content
            dest_path.write_text(final_content, encoding="utf-8")
            print(f"✅ Guardado en: {dest_path}")
        except Exception as e:
            print(f"❌ Error convirtiendo {pdf_path.name}: {e}")

if __name__ == "__main__":
    DERECHO_DIR = Path("pdf/Derecho")         # Solo la carpeta Derecho
    OUTPUT_DIR = Path("pdf/output")           # Salida
    process_derecho_pdf(DERECHO_DIR, OUTPUT_DIR)

