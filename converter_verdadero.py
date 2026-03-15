# converter.py
# Document Converter for Docusaurus - Refined Edition
# Supports: PDF (MuPDF), DOCX (Pandoc), XLSX (Pandas), TXT

import re
import os
import time
import shutil
import logging
import tempfile
import argparse
import subprocess
import unicodedata
from pathlib import Path
from typing import Optional, List, Tuple, Set
from concurrent.futures import ThreadPoolExecutor

# --- CONFIGURATION & CONSTANTS ---
SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".xlsx", ".xls", ".txt"}
MAX_CELL_LENGTH = 1200
MAX_DUPLICATE_ROWS = 3

CLEANING_PIPELINE = [
    ("Hyphen Fix", lambda t: re.sub(r"([a-z])-\n([a-z])", r"\1\2", t, flags=re.I)),
    ("Index Cleaner", lambda t: re.sub(r"\s*\.{3,}\s*\d+", "", t)),
    ("TOC Remover", lambda t: re.sub(
        r"(?i)^#*\s*(Index|Índice|Table of Contents|Tabla de contenidos)[\s\S]+?(?=\n#\s|\n##\s|\Z)", 
        "", t, flags=re.M
    )),
    ("Header/Footer Removal", lambda t: "\n".join([
        line for line in t.split("\n") 
        if not any(re.match(p, line) for p in [
            r"^\s*\d+\s*[-–—]\s*[A-Za-z]{2,}.*\d{4,}\s*$", 
            r"^[A-Za-z]{2,}.*\d{4,}\s*[-–—]\s*\d+\s*$", 
            r"^\s*\d+\s*$"
        ])
    ])),
    ("Multi-space Cleaner", lambda t: re.sub(r" {2,}", " ", t))
]

# --- LOGGING SETUP ---
def setup_logging():
    logger = logging.getLogger("Converter")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("conversion.log", encoding="utf-8")
    fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

log = setup_logging()

# --- TABLE PROCESSING LOGIC ---

def normalize_row(line: str) -> str:
    """Normalizes a table row for duplicate detection."""
    cells = [c.strip().lower() for c in line.split("|") if c.strip()]
    return "|".join(cells)

def process_markdown_tables(text: str, filename: str) -> str:
    """Detects, validates, and potentially omits Markdown tables."""
    lines = text.split("\n")
    processed_lines = []
    i = 0
    table_counter = 0

    while i < len(lines):
        line = lines[i]
        # Detect start of a table (line with |)
        if "|" in line:
            table_lines = []
            has_separator = False
            
            # Extract consecutive table lines
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
                
                # Validation 1: Cell Length
                for tl in table_lines:
                    cells = [c.strip() for c in tl.split("|")]
                    if any(len(c) > MAX_CELL_LENGTH for c in cells):
                        omit = True
                        reason = "content too large to render"
                        break
                
                # Validation 2: Duplicated Rows
                if not omit:
                    normalized_rows = [normalize_row(tl) for tl in table_lines if not re.match(r"^\s*\|?\s*(?::?-+:?\s*\|)+\s*:?-+:?\s*\|?\s*$", tl)]
                    for row in set(normalized_rows):
                        if normalized_rows.count(row) >= MAX_DUPLICATE_ROWS:
                            omit = True
                            reason = "duplicated data detected"
                            break
                
                if omit:
                    processed_lines.append(f"\n> Table omitted (Table {table_counter}): {reason}.\n> Source document: {filename}\n")
                    log.warning(f"Omitted Table {table_counter} in {filename} due to {reason}")
                else:
                    processed_lines.extend(table_lines)
            else:
                processed_lines.extend(table_lines)
            continue # Already advanced i
        else:
            processed_lines.append(line)
        i += 1
    
    return "\n".join(processed_lines)

# --- UTILITIES ---

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s\-]", "", text).strip().lower()
    return re.sub(r"[\s_]+", "-", text)

def mdx_safe_cleanup(text: str) -> str:
    text = text.replace("{", "&#123;").replace("}", "&#125;")
    text = re.sub(r"<(?!/?(?:p|br|hr|img|div|span|strong|em|b|i|u|h\d)\b)", "&lt;", text)
    for tag in ["br", "hr"]:
        text = re.sub(fr"<{tag}\s*>", f"<{tag} />", text, flags=re.I)
    return text

# --- HANDLERS ---

def handle_pdf(file_path: Path, img_root: Path) -> Optional[str]:
    """Extracts PDF text and images safely. Ensures Docusaurus compatible paths."""
    try:
        import pymupdf4llm
    except ImportError:
        log.error("pymupdf4llm not installed.")
        return None

    doc_slug = slugify(file_path.stem)
    img_dir = img_root / doc_slug
    img_dir.mkdir(parents=True, exist_ok=True)

    try:
        # muPDF produces markdown with internal image links
        markdown = pymupdf4llm.to_markdown(str(file_path), write_images=True, image_path=str(img_dir))
        
        # Global path replacement for MuPDF (catches all styles)
        # MuPDF usually uses relative paths like "image.png" in its output
        # Here we only relink established Markdown images to be safe
        def relink(m):
            img_name = Path(m.group('path')).name
            return f"![{m.group('alt')}](/img/{doc_slug}/{img_name})"

        img_pattern = r'\!\[(?P<alt>.*?)\]\((?P<path>.*?)\)'
        return re.sub(img_pattern, relink, markdown)
    except Exception as e:
        log.error(f"MuPDF failed for {file_path.name}: {e}")
        return None

def handle_docx(file_path: Path, img_root: Path) -> Optional[str]:
    """Uses Pandoc for DOCX. Robustly handles 'media/' subfolders and concurrency."""
    doc_slug = slugify(file_path.stem)
    img_dir = img_root / doc_slug
    img_dir.mkdir(parents=True, exist_ok=True)
    
    # Use temp dir for extraction to prevent race conditions during parallel writes
    with tempfile.TemporaryDirectory(prefix="pandoc_") as tmp_ext:
        tmp_dir = Path(tmp_ext)
        output_temp = tmp_dir / f"{doc_slug}.md"
        
        try:
            cmd = ["pandoc", str(file_path), "-t", "markdown", "--extract-media", str(tmp_dir), "-o", str(output_temp)]
            subprocess.run(cmd, check=True, capture_output=True)
            
            content = output_temp.read_text(encoding="utf-8")
            
            # Pandoc puts images in {tmp_dir}/media/
            media_subdir = tmp_dir / "media"
            if media_subdir.exists():
                for img_file in media_subdir.glob("**/*"):
                    if img_file.is_file():
                        shutil.copy2(img_file, img_dir / img_file.name)

            # GLOBAL PATH REPLACEMENT:
            # We must catch both ![](/tmp/...) AND [ref]: /tmp/... (Pandoc often uses reference-style)
            # We also handle both absolute and relative paths that Pandoc might generate
            
            # 1. Replace absolute temporary paths
            abs_tmp_prefix = str(tmp_dir).replace("\\", "/")
            content = content.replace(abs_tmp_prefix + "/media/", f"/img/{doc_slug}/")
            
            # 2. Replace relative paths Pandoc might use if it thinks it is in the temp dir
            content = content.replace("media/", f"/img/{doc_slug}/")
            
            # 3. Final cleanup for any missed Markdown image syntax
            def relink_final(m):
                img_name = Path(m.group('path').split(" ")[0].strip('"')).name
                if doc_slug not in m.group('path'): # Only rewrite if not already updated
                    return f"![{m.group('alt')}](/img/{doc_slug}/{img_name})"
                return m.group(0)

            img_pattern = r'\!\[(?P<alt>.*?)\]\((?P<path>.*?)\)'
            return re.sub(img_pattern, relink_final, content)
            
        except Exception as e:
            log.error(f"Pandoc failed for {file_path.name}: {e}")
            return None

def handle_excel(file_path: Path) -> Optional[str]:
    try:
        import pandas as pd
        xl = pd.ExcelFile(file_path)
        pages = []
        for sheet in xl.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet)
            pages.append(f"## {sheet}\n\n{df.to_markdown(index=False)}")
        return "\n\n".join(pages)
    except ImportError:
        log.error("pandas or tabulate not installed.")
        return None

# --- MAIN ENGINE ---

def process_file(file_path: Path, output_dir: Path, img_root: Path):
    ext = file_path.suffix.lower()
    content = None
    log.info(f"Processing: {file_path.name}")

    if ext == ".pdf": content = handle_pdf(file_path, img_root)
    elif ext == ".docx": content = handle_docx(file_path, img_root)
    elif ext in [".xlsx", ".xls"]: content = handle_excel(file_path)
    elif ext == ".txt": content = file_path.read_text(encoding="utf-8", errors="ignore")

    if not content:
        log.warning(f"No content extracted for {file_path.name}")
        return

    # Cleaning Pipeline
    for name, step in CLEANING_PIPELINE:
        content = step(content)
    
    # Table Refinement
    content = process_markdown_tables(content, file_path.name)
    
    # MDX Adaptation
    content = mdx_safe_cleanup(content)
    
    # Save
    target_path = output_dir / (slugify(file_path.stem) + ".md")
    target_path.write_text(content.strip(), encoding="utf-8")
    log.info(f"Successfully converted: {file_path.name} -> {target_path.name}")

def filter_deduplicated_files(files: List[Path]) -> List[Path]:
    filtered = []
    file_map = {}
    for f in files:
        key = (f.parent, f.stem)
        if key not in file_map: file_map[key] = set()
        file_map[key].add(f.suffix.lower())
    for f in files:
        if f.suffix.lower() == ".pdf" and ".docx" in file_map[(f.parent, f.stem)]:
            log.info(f"Skipping redundant PDF: {f.name}")
            continue
        filtered.append(f)
    return filtered

def main():
    parser = argparse.ArgumentParser(description="Multi-format document converter for Docusaurus.")
    parser.add_argument("--input", default="pdf", help="Directory containing documents.")
    parser.add_argument("--output", default="docs", help="Docusaurus 'docs' directory.")
    parser.add_argument("--workers", type=int, default=4, help="Parallel workers.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    project_root = output_path.parent
    img_root = project_root / "static" / "img"
    img_root.mkdir(parents=True, exist_ok=True)
    output_path.mkdir(parents=True, exist_ok=True)

    all_files = [f for f in input_path.rglob("*") if f.suffix.lower() in SUPPORTED_EXTENSIONS]
    files = filter_deduplicated_files(all_files)
    
    log.info(f"--- Starting Conversion ({len(files)} docs) ---")
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        for f in files: executor.submit(process_file, f, output_path, img_root)
    log.info(f"--- Finished in {time.time() - start_time:.2f}s ---")

if __name__ == "__main__":
    main()
