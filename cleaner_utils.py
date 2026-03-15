import re
import unicodedata
from pathlib import Path

# Constants for Table Filtering
MAX_CELL_LENGTH = 1200
MAX_DUPLICATE_ROWS = 3

def slugify(text: str) -> str:
    """Converts a string to a lower-case string with dashes."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s\-]", "", text).strip().lower()
    return re.sub(r"[\s_]+", "-", text)

def normalize_row(line: str) -> str:
    """Normalizes a table row for duplicate detection."""
    cells = [c.strip().lower() for c in line.split("|") if c.strip()]
    return "|".join(cells)

def process_markdown_tables(text: str, filename: str, logger) -> str:
    """Detects, validates, and potentially omits Markdown tables. Uses image heuristic."""
    lines = text.split("\n")
    processed_lines = []
    i = 0
    table_counter = 0

    while i < len(lines):
        line = lines[i]
        if "|" in line:
            table_lines = []
            has_separator = False
            
            while i < len(lines) and "|" in lines[i]:
                current_line = lines[i]
                table_lines.append(current_line)
                if re.match(r"^\s*\|?\s*(?::?-+:?\s*\|)+\s*:?-+:?\s*\|?\s*$", current_line):
                    has_separator = True
                i += 1
            
            if has_separator and len(table_lines) >= 2:
                table_counter += 1
                omit = False
                reason = ""
                
                for tl in table_lines:
                    cells = [c.strip() for c in tl.split("|")]
                    if any(len(c) > MAX_CELL_LENGTH for c in cells):
                        omit = True
                        reason = "content too large to render"
                        break
                
                if not omit:
                    normalized_rows = [normalize_row(tl) for tl in table_lines if not re.match(r"^\s*\|?\s*(?::?-+:?\s*\|)+\s*:?-+:?\s*\|?\s*$", tl)]
                    for row in set(normalized_rows):
                        if normalized_rows.count(row) >= MAX_DUPLICATE_ROWS:
                            omit = True
                            reason = "duplicated data detected"
                            break
                
                if omit:
                    has_neighbor_image = False
                    for j in range(i, min(i + 5, len(lines))):
                        if lines[j].strip() == "": continue
                        if re.search(r"\!\[.*?\]\(.*?\)", lines[j]):
                            has_neighbor_image = True
                        break
                    
                    if has_neighbor_image:
                        logger.info(f"Omitted Table {table_counter} in {filename} (favoring nearby image).")
                    else:
                        processed_lines.append(f"\n> Table omitted (Table {table_counter}): {reason}.\n> Source document: {filename}\n")
                        logger.warning(f"Omitted Table {table_counter} in {filename} due to {reason}")
                else:
                    processed_lines.extend(table_lines)
            else:
                processed_lines.extend(table_lines)
            continue
        else:
            processed_lines.append(line)
        i += 1
    
    return "\n".join(processed_lines)

def mdx_safe_cleanup(text: str) -> str:
    """Universal HTML Purge for Docusaurus MDX compatibility."""
    if not text: return ""

    # 1. Escape literal braces (MDX treats these as JS expressions)
    text = text.replace("{", "&#123;").replace("}", "&#125;")

    # 2. Fix corrupted URLs (URLs ending with a trailing HTML bracket)
    # This fixes: http://rminv> -> http://rminv
    text = re.sub(r'(https?://[^\s\>\)]+)\>', r'\1', text)

    # 3. Convert Bold/Italic tags to Markdown BEFORE stripping
    text = re.sub(r'<(?:strong|b)(?:\s+[^>]*|/?)>', r'**', text, flags=re.I)
    text = re.sub(r'</(?:strong|b)>', r'**', text, flags=re.I)
    text = re.sub(r'<(?:em|i)(?:\s+[^>]*|/?)>', r'*', text, flags=re.I)
    text = re.sub(r'</(?:em|i)>', r'*', text, flags=re.I)

    # 4. Universal Strip: Remove EVERY single tag starting with <
    # We use a destructive regex that catches any tag structure.
    text = re.sub(r'</?[a-zA-Z!][^>]*>', '', text, flags=re.S)

    # 4b. Remove stray JSX-like tags that don't close (Unexpected EOF fix)
    text = re.sub(r'<[A-Za-z][^>]*$', '', text)

    # 5. Escape ALL remaining angle brackets
    # This is the fail-safe to ensure no raw < or > survives.
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    
    return text

def clean_unsupported_images(text: str) -> str:
    """Replaces links to unsupported image formats (.emf, .wmf) with a download link banner."""
    pattern = r'\!\[(?P<alt>.*?)\]\((?P<path>.*?\.(?i:emf|wmf))\)'
    replacement = r'\n\n> 📄 **Imagen en formato vectorial (`\g<path>`)**: Este diagrama no se puede previsualizar directamente en la web. [📌 Haz clic aquí para descargar/ver el archivo original](\g<path>)\n\n'
    return re.sub(pattern, replacement, text)

def get_cleaning_pipeline():
    """Returns a list of (name, function) tuples for text processing."""
    return [
        ("Hyphen Fixer", lambda t: t.replace("-\n", "").replace("- \n", "")),
        ("TOC Remover", lambda t: re.sub(r'(?mi)^#+\s*(Índice|Table of Contents|Lista de (tablas|figuras)).*(\n^.*)*', '', t)),
        ("Pandoc Attribute Cleaner", lambda t: re.sub(r'\{width=".*?"\s+height=".*?"\}', '', t)),
        ("Unsupported Image Filter", clean_unsupported_images)
    ]
