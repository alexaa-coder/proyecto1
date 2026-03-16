# limpiar_frontmatter.py
import re
from pathlib import Path

DOCS_DIR = Path("docs")

def limpiar_markdown_en_yaml(texto):
    # Elimina ** y * del title y sidebar_label
    def limpiar_linea(match):
        clave = match.group(1)
        valor = match.group(2)
        valor_limpio = re.sub(r'\*+', '', valor).strip()
        return f'{clave}: "{valor_limpio}"'
    
    texto = re.sub(
        r'^(title|sidebar_label):\s*"([^"]*)"',
        limpiar_linea,
        texto,
        flags=re.MULTILINE
    )
    return texto

procesados = 0
for md in DOCS_DIR.rglob("*.md"):
    try:
        texto = md.read_text(encoding="utf-8", errors="ignore")
        if not texto.startswith("---"):
            continue
        nuevo = limpiar_markdown_en_yaml(texto)
        if nuevo != texto:
            md.write_text(nuevo, encoding="utf-8")
            print(f"✅ Limpiado: {md}")
            procesados += 1
    except Exception as e:
        print(f"❌ Error en {md}: {e}")

print(f"\nTotal procesados: {procesados}")
