# convert_pymupdf.py
# Conversor Rápido y Eficiente (PyMuPDF4LLM) -> Docusaurus
# Requiere: pip install pymupdf4llm

import os
from pathlib import Path
import pymupdf4llm
from slugify import slugify # pip install python-slugify (opcional, si no usa una función simple)

# Función simple de slug si no tienes librería
def simple_slug(text):
    return text.lower().replace(" ", "-").replace(".", "-").replace("_", "-")

def get_frontmatter(file_path: Path):
    """Genera la cabecera YAML para Docusaurus"""
    # ID: nombre del archivo sin extensión (slug)
    doc_id = simple_slug(file_path.stem)
    # Title: Nombre limpio con espacios
    title = file_path.stem.replace("-", " ").replace("_", " ").title()
    
    return f"""---
id: {doc_id}
title: {title}
sidebar_label: {title}
---

"""

def process_pdfs(input_dir: Path, output_dir: Path):
    print(f"🔄 Buscando PDFs en: {input_dir}")
    print(f"📂 Destino: {output_dir}")
    
    pdf_files = list(input_dir.rglob("*.pdf"))
    if not pdf_files:
        print("❌ No se encontraron archivos PDF.")
        return

    for pdf_path in pdf_files:
        try:
            # Calcular ruta relativa para mantener estructura
            rel_path = pdf_path.relative_to(input_dir)
            # Ruta de destino: cambiar .pdf por .md
            dest_path = output_dir / rel_path.with_suffix(".md")
            
            # Crear carpetas si no existen
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            print(f"📖 Convirtiendo: {pdf_path.name}...")
            
            # 1. Convertir PDF a Markdown
            md_content = pymupdf4llm.to_markdown(pdf_path)
            
            # 2. Añadir Frontmatter
            final_content = get_frontmatter(pdf_path) + md_content
            
            # 3. Guardar archivo
            dest_path.write_text(final_content, encoding="utf-8")
            print(f"✅ Guardado en: {dest_path}")
            
        except Exception as e:
            print(f"❌ Error convirtiendo {pdf_path.name}: {e}")

if __name__ == "__main__":
    # Configuración de carpetas (raíz del proyecto)
    ROOT_DIR = Path(__file__).parent.parent  # Asumiendo que el script está en una subcarpeta, ajústalo según donde lo ejecutes
    
    # Si ejecutas el script desde la raíz, usa "."
    # ROOT_DIR = Path(".") 
    
    PDF_DIR = Path("pdf")      # Carpeta de origen
    DOCS_DIR = Path("docs")    # Carpeta de destino (Docusaurus)
    
    if not PDF_DIR.exists():
        print(f"⚠️ La carpeta origen '{PDF_DIR}' no existe. Creándola para que metas tus PDFs...")
        PDF_DIR.mkdir()

    if not DOCS_DIR.exists():
        print(f"ℹ️ La carpeta destino '{DOCS_DIR}' no existe, se creará.")
    else:
        print(f"ℹ️ Usando carpeta destino existente: '{DOCS_DIR}'")
    
    process_pdfs(PDF_DIR, DOCS_DIR)
