import re
import os
import time
import shutil
import logging
import tempfile
import argparse
import subprocess
from pathlib import Path
from typing import Optional, List
from concurrent.futures import ThreadPoolExecutor

# Import cleaning utilities from external module
from cleaner_utils import (
    slugify, 
    mdx_safe_cleanup, 
    process_markdown_tables, 
    get_cleaning_pipeline
)

# --- CONFIGURATION & CONSTANTS ---
SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".xlsx", ".xls", ".txt"}

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
        def relink(m):
            img_name = Path(m.group('path')).name
            return f"![{m.group('alt')}](/img/{doc_slug}/{img_name})"

        img_pattern = r'\!\[(?P<alt>.*?)\]\((?P<path>.*?)\)'
        return re.sub(img_pattern, relink, markdown)
    except Exception as e:
        log.error(f"MuPDF failed for {file_path.name}: {e}")
        return None

def handle_docx(file_path: Path, img_root: Path) -> Optional[str]:
    """Uses Pandoc for DOCX with strictly compliant Markdown output."""
    doc_slug = slugify(file_path.stem)
    img_dir = img_root / doc_slug
    img_dir.mkdir(parents=True, exist_ok=True)
    
    with tempfile.TemporaryDirectory(prefix="pandoc_") as tmp_ext:
        tmp_dir = Path(tmp_ext)
        output_temp = tmp_dir / f"{doc_slug}.md"
        
        try:
            # PURITY OPTION: Using 'markdown_strict' to ensure 100% plain text output
            cmd = [
                "pandoc", str(file_path), 
                "-t", "markdown_strict", 
                "--extract-media", str(tmp_dir), 
                "-o", str(output_temp)
            ]
            subprocess.run(cmd, check=True, capture_output=True)
            
            content = output_temp.read_text(encoding="utf-8")
            
            # Move extracted images to permanent Docusaurus static folder
            media_subdir = tmp_dir / "media"
            if media_subdir.exists():
                for img_file in media_subdir.glob("**/*"):
                    if img_file.is_file():
                        # Extract everything (supported or not) so we can link to them
                        shutil.copy2(img_file, img_dir / img_file.name)

            # GLOBAL PATH REPLACEMENT: Fixes broken links from temp directories
            abs_tmp_prefix = str(tmp_dir).replace("\\", "/")
            content = content.replace(abs_tmp_prefix + "/media/", f"/img/{doc_slug}/")
            content = content.replace("media/", f"/img/{doc_slug}/")
            
            def relink_final(m):
                img_name = Path(m.group('path').split(" ")[0].strip('"')).name
                if doc_slug not in m.group('path'):
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

def process_file(file_path: Path, input_root: Path, output_root: Path, img_root: Path):
    """Processes a single file, preserving its relative directory structure."""
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
    for name, step in get_cleaning_pipeline():
        content = step(content)
    
    # Table Refinement (with image heuristic)
    content = process_markdown_tables(content, file_path.name, log)
    
    # MDX Adaptation
    content = mdx_safe_cleanup(content)
    
    # Calculate target path preserving subfolders from input_root
    rel_path = file_path.parent.relative_to(input_root)
    target_dir = output_root / rel_path
    target_dir.mkdir(parents=True, exist_ok=True)
    
    target_name = slugify(file_path.stem) + ".md"
    target_path = target_dir / target_name
    target_path.write_text(content.strip(), encoding="utf-8")
    log.info(f"Successfully converted: {file_path.name} -> {target_path}")

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
    parser = argparse.ArgumentParser(description="Structure-preserving document converter for Docusaurus.")
    parser.add_argument("--input", default="pdf", help="Directory containing documents.")
    parser.add_argument("--output", default="docs", help="Docusaurus 'docs' directory.")
    parser.add_argument("--workers", type=int, default=4, help="Parallel workers.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    
    # FIX: Correctly resolve the Docusaurus root folder to place images in /static/img globally
    # By resolving the output path, we reliably find the parent directory (project_root)
    project_root = output_path.resolve().parent
    img_root = project_root / "static" / "img"
    
    img_root.mkdir(parents=True, exist_ok=True)
    output_path.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        log.error(f"Input directory '{args.input}' not found.")
        return

    all_files = [f for f in input_path.rglob("*") if f.suffix.lower() in SUPPORTED_EXTENSIONS]
    files = filter_deduplicated_files(all_files)
    
    log.info(f"--- Starting Conversion ({len(files)} docs) ---")
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        for f in files: executor.submit(process_file, f, input_path, output_path, img_root)
    
    log.info(f"--- Finished Conversion in {time.time() - start_time:.2f}s ---")
    
    # NOTE: Automatic organizer step has been specifically removed to preserve 
    # original folder structures and allow external organization scripts.

if __name__ == "__main__":
    main()   
