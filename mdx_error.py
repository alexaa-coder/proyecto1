from pathlib import Path
import re

FILES = [
    "docs/pnt-013-01-auditorias-internas-externas.md",
    "docs/pnt-013-02-auditorias-internas-externas.md"
]

def fix_file(file):

    path = Path(file)
    print(f"Processing {path}")

    text = path.read_text(encoding="utf-8")

    # convertir HTML strong a markdown
    text = re.sub(r"<strong>", "**", text)
    text = re.sub(r"</strong>", "**", text)

    path.write_text(text, encoding="utf-8")

    print("Converted <strong> → **")

for f in FILES:
    fix_file(f)

print("Done.")
