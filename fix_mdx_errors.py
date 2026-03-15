import re
from pathlib import Path

BASE = Path("docs")

files = [
"ISO-13845/Licencia Previa de Funcionamiento/Notificaciones/notificacion-deficiencia-9170-ps.md",
"ISO-13845/Licencia Previa de Funcionamiento/Notificaciones/2024-07-09-oficio.md",
"ISO-13845/Licencia Previa de Funcionamiento/Notificaciones/2024-08-07-oficio.md",
"ISO-13845/Licencia Previa de Funcionamiento/Notificaciones/2024-08-14-oficio.md",
"ISO-13845/Licencia Previa de Funcionamiento/Notificaciones/2024-09-19-subsanaciones-oficio.md",
"ISO-13845/Licencia Previa de Funcionamiento/2024-06-20-oficio.md",
]

def sanitize_mdx(text):

    # eliminar macros {{...}}
    text = re.sub(r"\{\{.*?\}\}", "", text)

    # eliminar atributos pandoc {width=...} etc
    text = re.sub(r"\{[^{}\n]{1,200}\}", "", text)

    # eliminar jsx roto
    text = re.sub(r"<[A-Za-z][^>\n]*$", "", text, flags=re.M)

    # arreglar urls rotas
    text = re.sub(r"(https?://[^\s>\)]+)>", r"\1", text)

    return text


for f in files:

    path = BASE / f

    if not path.exists():
        print("❌ no existe:", path)
        continue

    print("🔧 limpiando:", path)

    content = path.read_text(encoding="utf-8")

    cleaned = sanitize_mdx(content)

    path.write_text(cleaned, encoding="utf-8")

print("\n✅ archivos reparados")
