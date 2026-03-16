import os
import re

DOCS_DIR = "docs"
STATIC_DIR = "static"

img_pattern = re.compile(r'!\[.*?\]\((.*?)\)')

broken = []

for root, dirs, files in os.walk(DOCS_DIR):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            matches = img_pattern.findall(content)

            for img in matches:
                if img.startswith("/img/"):
                    real_path = os.path.join(STATIC_DIR, img.lstrip("/"))

                    if not os.path.exists(real_path):
                        broken.append((path, img))

print("\nIMÁGENES ROTAS:\n")

for md, img in broken:
    print(f"{md}  ->  {img}")

print(f"\nTotal rotas: {len(broken)}")
