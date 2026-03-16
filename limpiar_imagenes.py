def limpiar_imagenes(usadas):
    eliminadas = 0

    for img in IMG_DIR.rglob("*.*"):

        if img.name in PROTECTED_FILES:
            continue

        # Evitar borrar archivos en carpetas protegidas
        if any(p in PROTECTED_DIRS for p in img.parts):
            continue

        rel = img.relative_to(IMG_DIR).as_posix()

        if rel not in usadas:
            print(f"🗑 Eliminando: {rel}")
            img.unlink()
            eliminadas += 1

    return eliminadas
