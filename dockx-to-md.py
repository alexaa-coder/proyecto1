import subprocess
from pathlib import Path

input_dir = Path("docx")
output_dir = Path("docs/normativa")

output_dir.mkdir(parents=True, exist_ok=True)

files = list(input_dir.glob("*.docx"))

if not files:
    print("No se encontraron archivos DOCX")

for file in files:

    output_file = output_dir / (file.stem + ".md")

    subprocess.run([
        "pandoc",
        str(file),
        "-t",
        "markdown",
        "-o",
        str(output_file)
    ])

    print(f"Convertido: {file} -> {output_file}")

