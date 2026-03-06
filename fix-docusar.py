#!/usr/bin/env python3
import os
import shutil
import re

# Configuración
PDF_DIR = "pdf/ISO-27001"  # ruta donde están los PNG originales
STATIC_IMG_DIR = "static/img/iso27001/organigramas"  # destino de las imágenes
DOCS_DIR = "docs"  # donde están los MD
IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg"]

os.makedirs(STATIC_IMG_DIR, exist_ok=True)

# 1️⃣ Copiar imágenes
copied_images = []
for root, dirs, files in os.walk(PDF_DIR):
    for f in files:
        if any(f.lower().endswith(ext) for ext in IMAGE_EXTENSIONS):
            src = os.path.join(root, f)
            dst = os.path.join(STATIC_IMG_DIR, f)
            shutil.copy2(src, dst)
            copied_images.append(f)

print(f"Se copiaron {len(copied_images)} imágenes a {STATIC_IMG_DIR}")

# 2️⃣ Reescribir MD
pattern = re.compile(r'!\[([^\]]*)\]\(\./([^)]+)\)')

fixed_count = 0

for root, dirs, files in os.walk(DOCS_DIR):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            def replace_func(match):
                alt_text, img_name = match.groups()
                img_name_only = os.path.basename(img_name)
                if img_name_only in copied_images:
                    return f"![{alt_text}](/img/iso27001/organigramas/{img_name_only})"
                return match.group(0)

            new_content = pattern.sub(replace_func, content)
            
            if new_content != content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                fixed_count += 1

print(f"Se actualizaron {fixed_count} archivos Markdown.")
