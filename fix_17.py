import re
from pathlib import Path

DOCS_DIR = Path("docs")

def fix_strong_tags(text):
    # convertir <strong> a markdown
    text = text.replace("<strong>", "**")
    text = text.replace("</strong>", "**")

    # si queda un ** impar, lo cerramos
    if text.count("**") % 2 != 0:
        text += "**"

    return text


def fix_paragraph_tags(text):
    # eliminar <p> y </p>
    text = re.sub(r"</?p[^>]*>", "", text)

    # eliminar <em> y </em> convirtiendo a markdown
    text = text.replace("<em>", "*")
    text = text.replace("</em>", "*")

    return text


def fix_broken_jsx(text):
    # eliminar cualquier etiqueta HTML incompleta
    text = re.sub(r"<[A-Za-z][^>\n]*$", "", text, flags=re.MULTILINE)

    # eliminar tags HTML restantes
    text = re.sub(r"</?[A-Za-z][^>]*>", "", text)

    return text


def fix_pandoc_attributes(text):
    # eliminar {width="..." height="..."}
    text = re.sub(r'\{width=".*?"\s*height=".*?"\}', '', text)
    return text


def clean_file(path):

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    original = text

    text = fix_strong_tags(text)
    text = fix_paragraph_tags(text)
    text = fix_broken_jsx(text)
    text = fix_pandoc_attributes(text)

    if text != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print("✔ fixed:", path)
    else:
        print("• ok:", path)


def main():
    files = list(DOCS_DIR.rglob("*.md"))

    print(f"Scanning {len(files)} markdown files...\n")

    for f in files:
        clean_file(f)

    print("\nFinished fixing MDX errors.")


if __name__ == "__main__":
    main()
