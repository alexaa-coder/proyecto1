# Document Conversion Suite v7 (English & Optimized)

This suite is designed to convert multiple document formats (PDF, DOCX, Excel, PowerPoint, PNG) into clean, Docusaurus-compatible Markdown.

## Features
- **Multi-Format Support**: Handles .pdf, .docx, .xlsx, .xls, .pptx, .txt, .png.
- **Docusaurus Ready**: Outputs Markdown with Frontmatter and MDX-safe character escaping.
- **Table Protection**: Isolates tables during cleaning to preserve structural integrity.
- **Image Extraction**: Automatically extracts images from PDFs and saves them to a `static/img` folder for Docusaurus.
- **Signature Cleaning**: Removes digital certificate metadata from administrative PDFs.
- **Text Justification**: Applies CSS justification to continuous text blocks.

## Installation

### 1. Python Environment
It is recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. System Requirements (OCR)
If you need to process scanned PDFs or images, you must install **Tesseract OCR** on your system:
- **Windows**: Install Tesseract from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
- **Linux**: `sudo apt install tesseract-ocr tesseract-ocr-spa`

## Usage

Run the script specifying the input directory and output directory:

```bash
python convert_multi_format_v6.py --input ./my_docs --output ./docusaurus_docs/docs
```

### Arguments
- `--input`: Folder containing source documents (default: `pdf`).
- `--output`: Folder where Markdown will be saved (default: `docs`).
- `--workers`: Number of parallel processes (default: `1`).
- `--ocr`: Enable OCR for scanned PDFs and PNGs.
- `--debug`: Enable verbose logging and metrics.
- `--strict-tables`: Disable aggressive paragraph merging (safer for complex docs).

## Folder Structure (Output)
- `/docs`: Markdown files generated.
- `/docs/static/img`: Extracted images linked within the Markdown.
