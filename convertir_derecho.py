# convertir_derecho.py
import fitz  # PyMuPDF

pdf_path = "pdf/Derecho/wuolah-free-Derecho-civil.pdf"
md_path = "pdf/output/Derecho.md"

doc = fitz.open(pdf_path)
with open(md_path, "w", encoding="utf-8") as f:
    for i, page in enumerate(doc, 1):
        f.write(f"# Página {i}\n\n")
        f.write(page.get_text() + "\n\n")
