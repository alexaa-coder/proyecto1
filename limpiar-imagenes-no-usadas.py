#!/usr/bin/env python3
# Borra imágenes de static/img que ya no están referenciadas en docs/

import re
from pathlib import Path

DOCS_DIR = Path("docs")
IMG_DIR = Path("static/img")

img_regex = re.compile(r'!\[.*?\]\((.*?)\)|<img.*?src=["\'](.*?)["\']')

def obtener_imagenes_usadas():
    usadas = set()

    for md in DOCS_DIR.rglob("*.md"):
        texto = md.read_text(encoding="utf-8", errors="ignore")

        for m in img_regex.findall(texto):
            ruta = m[0] or m[1]

            if "/img/" in ruta:
                ruta = ruta.split("/img/")[-1]

            usadas.add(ruta)

    return usadas


def limpiar():
    usadas = obtener_imagenes_usadas()
    borradas = 0

    for img in IMG_DIR.rglob("*.*"):
        rel = img.relative_to(IMG_DIR).as_posix()

        if rel not in usadas:
            print(f"🗑️  Eliminando: {rel}")
            img.unlink()
            borradas += 1

    print(f"\n✅ Imágenes eliminadas: {borradas}")


if __name__ == "__main__":
    limpiar()
