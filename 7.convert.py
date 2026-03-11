# converter.py
# Document Converter for Docusaurus - Refactored Edition
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
from typing import Optional, List, Tuple
from concurrent.futures import ThreadPoolExecutor

# --- CONFIGURATION & CONSTANTS ---
SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".xlsx", ".xls", ".txt"}
CLEANING_PIPELINE = [
    ("Hyphen Fix", lambda t: re.sub(r"([a-z])-\n([a-z])", r"\1\2", t, flags=re.I)),
    ("Index Cleaner", lambda t: re.sub(r"\s*\.{3,}\s*\d+", "", t)),
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

# --- UTILITIES ---

def slugify(text: str) -> str:
    """Converts a string to a lower-case string with dashes."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s\-]", "", text).strip().lower()
    return re.sub(r"[\s_]+", "-", text)

def get_docusaurus_frontmatter(filename: str) -> str:
    """Generates Docusaurus metadata for the markdown file."""
    doc_id = slugify(filename)
    title = filename.replace("-", " ").replace("_", " ").title()
    return f"---\nid: {doc_id}\ntitle: \"{title}\"\nsidebar_label: \"{title}\"\n---\n\n"

def mdx_safe_cleanup(text: str) -> str:
    """Ensures content is compatible with Docusaurus MDX."""
    # Escape MDX reserved braces
    text = text.replace("{", "&#123;").replace("}", "&#125;")
    # Ensure HTML-like tags are self-closing or escaped
    text = re.sub(r"<(?!/?(?:p|br|hr|img|div|span|strong|em|b|i|u|h\d)\b)", "&lt;", text)
    for tag in ["br", "hr"]:
        text = re.sub(fr"<{tag}\s*>", f"<{tag} />", text, flags=re.I)
    return text

def apply_justification(text: str) -> str:
    """Wraps text blocks in a div with text-align justify."""
    def wrapper(match):
        block = match.group(0).strip()
        # Skip wrapping if it contains MDX/Markdown elements or is too short
        if any(re.match(r"^(?:#|\-|\*|\d+\.|\||```|<|id:|title:|sidebar_label:|---)", l.strip()) for l in block.split('\n')) or len(block) < 60:
            return match.group(0)
        return f'\n<div style={{{{textAlign: "justify"}}}}>\n\n{block}\n\n</div>\n'
    return re.sub(r"((?:(?!\n\n).)+)", wrapper, text, flags=re.S)

# --- HANDLERS ---

def handle_pdf(file_path: Path, img_root: Path) -> Optional[str]:
    """Extracts text and images from PDF using pymupdf4llm."""
    try:
        import pymupdf4llm
    except ImportError:
        print("[ERROR] pymupdf4llm not installed.")
        return None

    doc_slug = slugify(file_path.stem)
    img_dir = img_root / doc_slug
    
    # Clean previous images for this document to avoid duplicates
    if img_dir.exists():
        shutil.rmtree(img_dir)
    img_dir.mkdir(parents=True, exist_ok=True)

    markdown = pymupdf4llm.to_markdown(str(file_path), write_images=True, image_path=str(img_dir))

    # Re-link images to Docusaurus static path (/img/[slug]/...)
    def relink(m):
        img_name = Path(m.group(2)).name
        return f'![{m.group(1)}](/img/{doc_slug}/{img_name})'
    
    return re.sub(r'\!\[(.*?)\]\((.*?)\)', relink, markdown)

def handle_docx(file_path: Path, img_root: Path) -> Optional[str]:
    """Uses Pandoc to convert DOCX to MD and extract images."""
    doc_slug = slugify(file_path.stem)
    img_dir = img_root / doc_slug
    
    if img_dir.exists():
        shutil.rmtree(img_dir)
    img_dir.mkdir(parents=True, exist_ok=True)

    output_temp = Path(tempfile.gettempdir()) / f"{doc_slug}.md"
    
    try:
        cmd = [
            "pandoc", str(file_path),
            "-t", "markdown",
            "--extract-media", str(img_dir),
            "-o", str(output_temp)
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        
        content = output_temp.read_text(encoding="utf-8")
        
        # Pandoc saves images in img_dir/media/image1.png. Move them up.
        media_subdir = img_dir / "media"
        if media_subdir.exists():
            for img_file in media_subdir.glob("*"):
                shutil.move(str(img_file), str(img_dir / img_file.name))
            shutil.rmtree(media_subdir)

        # Fix Pandoc image paths to Docusaurus format
        # Pandoc usually uses ![caption](path/to/image)
        def relink_pandoc(m):
            img_name = Path(m.group(2)).name
            return f'![{m.group(1)}](/img/{doc_slug}/{img_name})'
        
        return re.sub(r'\!\[(.*?)\]\((.*?)\)', relink_pandoc, content)
    except Exception as e:
        print(f"[ERROR] Pandoc failed for {file_path.name}: {e}")
        return None
    finally:
        if output_temp.exists():
            output_temp.unlink()

def handle_excel(file_path: Path) -> Optional[str]:
    """Converts Excel sheets to Markdown tables using Pandas."""
    try:
        import pandas as pd
        xl = pd.ExcelFile(file_path)
        pages = []
        for sheet in xl.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet)
            pages.append(f"## {sheet}\n\n{df.to_markdown(index=False)}")
        return "\n\n".join(pages)
    except ImportError:
        print("[ERROR] pandas or tabulate not installed.")
        return None

# --- MAIN ENGINE ---

def process_file(file_path: Path, output_dir: Path, img_root: Path):
    """Orchestrates the conversion of a single file."""
    ext = file_path.suffix.lower()
    content = None

    print(f"[*] Processing: {file_path.name}")

    if ext == ".pdf":
        content = handle_pdf(file_path, img_root)
    elif ext == ".docx":
        content = handle_docx(file_path, img_root)
    elif ext in [".xlsx", ".xls"]:
        content = handle_excel(file_path)
    elif ext == ".txt":
        content = file_path.read_text(encoding="utf-8", errors="ignore")

    if not content:
        return

    # Clean Content
    for name, step in CLEANING_PIPELINE:
        content = step(content)
    
    content = mdx_safe_cleanup(content)
    content = apply_justification(content)
    
    # Finalize MDX
    frontmatter = get_docusaurus_frontmatter(file_path.stem)
    final_output = (frontmatter + content).strip()
    
    # Save to Slugified Path
    target_path = output_dir / (slugify(file_path.stem) + ".md")
    target_path.write_text(final_output, encoding="utf-8")
    print(f"[+] Saved: {target_path.name}")

def main():
    parser = argparse.ArgumentParser(description="Multi-format document converter for Docusaurus.")
    parser.add_argument("--input", default="input", help="Directory containing documents to convert.")
    parser.add_argument("--output", default="docs", help="Docusaurus 'docs' directory.")
    parser.add_argument("--workers", type=int, default=4, help="Number of parallel workers.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    
    # Docusaurus images usually go in static/img
    # Try to find 'static' relative to output_path (assuming output is 'docs' inside a project)
    project_root = output_path.parent
    img_root = project_root / "static" / "img"
    img_root.mkdir(parents=True, exist_ok=True)
    output_path.mkdir(parents=True, exist_ok=True)

    files = [f for f in input_path.rglob("*") if f.suffix.lower() in SUPPORTED_EXTENSIONS]
    
    print(f"--- Starting Conversion ({len(files)} files) ---")
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        for f in files:
            executor.submit(process_file, f, output_path, img_root)

    print(f"--- Finished in {time.time() - start_time:.2f}s ---")

if __name__ == "__main__":
    main()
