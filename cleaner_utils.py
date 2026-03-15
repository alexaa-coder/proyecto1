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

def balance_markdown_asterisks(text: str) -> str:
    """
    Balances broken bold/italic markers (like **text without closing asterisks).
    This prevents Docusaurus MDX parser from failing.
    """
    lines = text.split("\n")
    balanced_lines = []
    
    for line in lines:
        # Ignore lines that are headings or lists to prevent false positives
        if re.match(r'^(#|\* |\+ |- |> )', line.strip()):
            balanced_lines.append(line)
            continue
            
        original_line = line
        
        # Count formatting markers
        bold_count = len(re.findall(r'(?<!\*)\*\*(?!\*)', line))
        italic_count = len(re.findall(r'(?<!\*)\*(?!\*)', line))
        
        # If there's an odd number of double asterisks, try to close it at the end
        if bold_count % 2 != 0:
            # If the line ends with a marker, it's probably a stray. Just remove it.
            if line.rstrip().endswith("**"):
                line = line.rstrip()[:-2]
            else:
                # Otherwise, close it at the end of the line
                line = line + "**"
                
        # If there's an odd number of single asterisks, remove the stray one to be safe
        # (Balancing single asterisks is very prone to error because of list bullets)
        elif italic_count % 2 != 0:
            # Safest approach for odd italics is to strip stray asterisks at word boundaries
            if line.rstrip().endswith("*"):
                line = line.rstrip()[:-1]
                
        balanced_lines.append(line)
        
    return "\n".join(balanced_lines)

def mdx_safe_cleanup(text: str) -> str:
    """Universal HTML Purge for Docusaurus MDX compatibility with Macro protection."""
    if not text: return ""

    # 1. MACRO PROTECTION: Detect and protect {{macros}}
    # Find all {{...}} and replace them with a temporary alphanumeric placeholder
    macros = re.findall(r'(\{\{.*?\}\})', text)
    macro_map = {}
    for i, macro in enumerate(macros):
        placeholder = f"__PROTECTEDMACRO{i}__"
        macro_map[placeholder] = macro
        text = text.replace(macro, placeholder)

    # 2. Escape literal braces (MDX treats these as JS expressions)
    text = text.replace("{", "&#123;").replace("}", "&#125;")

    # 3. Fix corrupted URLs (URLs ending with a trailing HTML bracket)
    text = re.sub(r'(https?://[^\s\>\)]+)\>', r'\1', text)

    # 4. TRUNCATED HTML REMOVAL: Detect and erase tags missing closing >
    # Example: <strong texto... -> (removed)
    text = re.sub(r'<[a-zA-Z][^>\n]*$', '', text, flags=re.M)

    # 5. Convert Bold/Italic HTML tags to Markdown BEFORE stripping
    text = re.sub(r'<(?:strong|b)(?:\s+[^>]*|/?)>', r'**', text, flags=re.I)
    text = re.sub(r'</(?:strong|b)>', r'**', text, flags=re.I)
    text = re.sub(r'<(?:em|i)(?:\s+[^>]*|/?)>', r'*', text, flags=re.I)
    text = re.sub(r'</(?:em|i)>', r'*', text, flags=re.I)

    # 6. Universal Strip: Remove EVERY single tag starting with <
    text = re.sub(r'</?[a-zA-Z!][^>]*>', '', text, flags=re.S)

    # 7. Stray JSX Fixer
    text = re.sub(r'<[A-Za-z][^>]*$', '', text)

    # 8. Escape ALL remaining angle brackets
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    
    # 9. ASTERISK BALANCING: Fix broken markdown ** before restoring macros
    text = balance_markdown_asterisks(text)
    
    # 10. RESTORE MACROS
    for placeholder, original_macro in macro_map.items():
        text = text.replace(placeholder, original_macro)
    
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
