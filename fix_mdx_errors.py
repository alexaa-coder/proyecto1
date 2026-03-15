import re
from pathlib import Path

DOCS_DIR = Path("docs")

def fix_content(text):
    
    # 1. Eliminar URLs corruptas tipo http://rminv>
    text = re.sub(r'http://[^\s>]*>', '', text)

    # 2. Corregir <strong> sin cerrar
    open_strong = text.count("<strong>")
    close_strong = text.count("</strong>")
    if open_strong > close_strong:
        text += "</strong>" * (open_strong - close_strong)

    # 3. Corregir <p> sin cerrar
    open_p = text.count("<p>")
    close_p = text.count("</p>")
    if open_p > close_p:
        text += "</p>" * (open_p - close_p)

    # 4. Eliminar etiquetas HTML raras que rompen MDX
    text = re.sub(r'<[^>\n]*$', '', text)

    # 5. Eliminar JSX roto tipo <tag
    text = re.sub(r'<[A-Za-z0-9_-]+\s*$', '', text)

    return text


def process_file(path):

    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
        fixed = fix_content(content)

        if fixed != content:
            path.write_text(fixed, encoding="utf-8")
            print("Fixed:", path)

    except Exception as e:
        print("Error:", path, e)


def main():

    print("Scanning markdown files...\n")

    for md in DOCS_DIR.rglob("*.md"):
        process_file(md)

    print("\nFinished cleaning MDX errors.")


if __name__ == "__main__":
    main()
