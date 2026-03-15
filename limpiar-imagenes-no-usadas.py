#!/usr/bin/env python3

import re
from pathlib import Path

DOCS_DIR = Path("docs")
IMG_DIR = Path("static/img")

# Assets del tema que nunca deben borrarse
PROTECTED_FILES = {
    "favicon.ico",
    "logo.svg",
    "docusaurus.png",
    "undraw_docusaurus_mountain.svg",
    "undraw_docusaurus_react.svg",
    "undraw_docusaurus_tree.svg"
}

PROTECTED_DIRS = {
    "tutorial"
}

IMG_REGEX = re.compile(r'!\[.*?\]\((.*?)\)|<img.*?src=["\'](.*?)["\']')


def obtener_imagenes_usadas():
    usadas = set()

    for md in DOCS_DIR.rglob("*.[mM][dDxX]*"):
        try:
            texto = md.read_text(encoding="utf-8", errors="ignore")
        except:
            continue

        for match in IMG_REGEX.findall(texto):
            ruta = match[0] or match[1]

            if "/img/" in ruta:
                ruta = ruta.split("/img/")[-1]

            usadas.add(ruta)

    return usadas


def limpiar_imagenes(usadas):
    eliminadas = 0

    for img in IMG_DIR.rglob("*.*"):

        if img.name in PROTECTED_FILES:
            continue

        if img.parts[2] in PROTECTED_DIRS:
            continue

        rel = img.relative_to(IMG_DIR).as_posix()

        if rel not in usadas:
            print(f"🗑 Eliminando: {rel}")
            img.unlink()
            eliminadas += 1

    return eliminadas


def eliminar_carpetas_vacias():

    for d in sorted(IMG_DIR.rglob("*"), reverse=True):

        if d.is_dir() and not any(d.iterdir()):
            print(f"📁 Eliminando carpeta vacía: {d.relative_to(IMG_DIR)}")
            d.rmdir()


def detectar_duplicados():

    carpetas = [d for d in IMG_DIR.iterdir() if d.is_dir()]
    nombres = {}

    for c in carpetas:

        base = re.sub(r'[^a-z0-9]', '', c.name.lower())

        if base in nombres:
            print(f"⚠ Posible duplicado: {nombres[base]} <-> {c}")
        else:
            nombres[base] = c


def main():

    print("🔎 Analizando imágenes usadas en documentación...\n")

    usadas = obtener_imagenes_usadas()

    eliminadas = limpiar_imagenes(usadas)

    eliminar_carpetas_vacias()

    detectar_duplicados()

    print(f"\n✅ Limpieza finalizada")
    print(f"📊 Imágenes eliminadas: {eliminadas}")


if __name__ == "__main__":
    main()
