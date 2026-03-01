from pathlib import Path
import pdfplumber
import re

PDF_DIR = Path("pdf/Derecho")
OUTPUT_DIR = Path("pdf/output_derecho_pdfplumber_clean")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def clean_text(text):
    # Quita IDs raros como a64b0469ff35958ef4ab887a898bd50bdfbbe91a-3644169
    text = re.sub(r'\b[a-f0-9]{32,}-\d+\b', '', text)
    # Quita saltos de línea repetidos y espacios extra
    text = re.sub(r'\n\s*\n', '\n\n', text)
    # Limpia espacios al inicio/final de cada línea
    text = "\n".join(line.strip() for line in text.splitlines())
    # Detecta posibles títulos en mayúsculas y los convierte a Markdown
    text = re.sub(r'^([A-ZÁÉÍÓÚÑ]{3,}.*)$', r'## \1', text, flags=re.MULTILINE)
    return text.strip()

for pdf_file in PDF_DIR.glob("*.pdf"):
    print(f"🔄 Procesando: {pdf_file.name}")
    with pdfplumber.open(pdf_file) as pdf:
        all_text = "\n\n".join(
            page.extract_text() for page in pdf.pages if page.extract_text()
        )
    clean_md = clean_text(all_text)
    dest_file = OUTPUT_DIR / (pdf_file.stem + ".md")
    dest_file.write_text(clean_md, encoding="utf-8")
    print(f"✅ Convertido: {pdf_file.name} → {dest_file}")
