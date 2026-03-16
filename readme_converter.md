# Document Converter for Docusaurus

This script converts PDF, DOCX, and Excel files into Docusaurus-compatible MDX files. It is optimized for a direct integration workflow where files are reviewed in `docs/` and then organized manually.

## Features
- **Structure Preservation**: `converter.py` rigorously maintains your original subfolder hierarchy from the `pdf/` input directory straight into `docs/`.
- **DOCX Conversion**: High-quality GitHub Flavored Markdown (GFM) output via Pandoc to maximize table and list compatibility.
- **Absolute Pathing**: Centralized image management extracting to `static/img/` and linking via absolute paths (`/img/...`), ensuring images never break regardless of where the Markdown file is moved.
- **MDX Sanitization**: `cleaner_utils.py` applies a robust security pipeline: stripping broken HTML, balancing formatting markers, fixing bad URLs, and protecting macros (`{{...}}`) to prevent Docusaurus `acorn` parse errors.

## Modular Structure
1. `converter.py`: Orchestrates the conversion while strictly preserving your folder structure.
2. `cleaner_utils.py`: Centralized text, table, and MDX sanitization logic.

## Prerequisites
- **Python Dependencies**: Install via `pip install -r requirements.txt`.
- **Pandoc**: Must be installed on your system globally (e.g., `sudo apt install pandoc` or via standard installers).

## Usage

1. **Prepare**: Place your folder-organized documents in `pdf/` (e.g., `pdf/ISO-27001/doc.docx`).
2. **Convert**:
   ```bash
   python3 converter.py
   ```
3. **Site Check**: Run the Docusaurus development server with increased memory limits to prevent out-of-memory errors on large docs setups:
   ```bash
   NODE_OPTIONS=--max-old-space-size=4096 npm start
   ```

## Global Text Justification (CSS)

To justify your text globally in Docusaurus, add this to your `src/css/custom.css`:

```css
.markdown p {
  text-align: justify;
}
```

## Troubleshooting

Check **`conversion.log`** for a detailed record of every file processed, including any omitted tables or conversion errors.
