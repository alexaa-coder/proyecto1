# convert_pymupdf_mejorado.py
# Conversor Mejorado con Limpieza de Markdown
# Requiere: pip install pymupdf4llm python-slugify

import os
import re
from pathlib import Path
import pymupdf4llm

def simple_slug(text):
    """Genera slug simple para IDs"""
    return text.lower().replace(" ", "-").replace(".", "-").replace("_", "-").replace("/", "-")

def limpiar_markdown(md_text: str) -> str:
    """
    Limpia el Markdown generado por pymupdf4llm
    Arregla problemas comunes: párrafos rotos, índices, espacios
    """
    
    # 1. FUSIONAR LÍNEAS ROTAS DE PÁRRAFOS
    # Si una línea no termina con punto, dos puntos, o signo de puntuación
    # y la siguiente no empieza con marcador Markdown, fusionarlas
    lineas = md_text.split('\n')
    lineas_limpias = []
    i = 0
    
    while i < len(lineas):
        linea_actual = lineas[i].rstrip()
        
        # Si es línea vacía, mantenerla
        if not linea_actual:
            lineas_limpias.append('')
            i += 1
            continue
        
        # Si es marcador Markdown (título, lista, tabla, código), mantenerla
        if (linea_actual.startswith('#') or 
            linea_actual.startswith('-') or 
            linea_actual.startswith('*') or 
            linea_actual.startswith('|') or 
            linea_actual.startswith('>') or 
            linea_actual.startswith('```') or
            re.match(r'^\d+\.', linea_actual)):  # Lista numerada
            lineas_limpias.append(linea_actual)
            i += 1
            continue
        
        # Si la línea actual no termina en puntuación de fin de frase
        # y hay una siguiente línea que no es Markdown, fusionar
        if i + 1 < len(lineas):
            linea_siguiente = lineas[i + 1].lstrip()
            
            # No fusionar si:
            # - Línea actual termina con puntuación final
            # - Siguiente línea es vacía
            # - Siguiente línea es marcador Markdown
            if (linea_actual.endswith(('.', ':', ';', '!', '?', ')')) or
                not linea_siguiente or
                linea_siguiente.startswith(('#', '-', '*', '|', '>', '```')) or
                re.match(r'^\d+\.', linea_siguiente)):
                lineas_limpias.append(linea_actual)
                i += 1
            else:
                # Fusionar con la siguiente
                lineas_limpias.append(linea_actual + ' ' + linea_siguiente.lstrip())
                i += 2  # Saltar la siguiente porque ya la fusionamos
        else:
            lineas_limpias.append(linea_actual)
            i += 1
    
    md_limpio = '\n'.join(lineas_limpias)
    
    # 2. ELIMINAR MÚLTIPLES LÍNEAS VACÍAS CONSECUTIVAS
    md_limpio = re.sub(r'\n{3,}', '\n\n', md_limpio)
    
    # 3. LIMPIAR ÍNDICES/TOC MAL FORMADOS
    # Patrón común: "1.2.3 Título ..... 15" → "1.2.3 Título"
    md_limpio = re.sub(r'(#+\s+[\d\.]+\s+[^\n]+?)\s*\.{3,}\s*\d+', r'\1', md_limpio)
    
    # 4. ELIMINAR NÚMEROS DE PÁGINA SUELTOS
    # Líneas que solo contienen un número (probablemente número de página)
    md_limpio = re.sub(r'^\s*\d+\s*$', '', md_limpio, flags=re.MULTILINE)
    
    # 5. ELIMINAR ENCABEZADOS/PIES DE PÁGINA REPETITIVOS
    # Detectar líneas que se repiten muchas veces (>3) y eliminarlas
    lineas = md_limpio.split('\n')
    contador_lineas = {}
    for linea in lineas:
        linea_limpia = linea.strip()
        if linea_limpia and len(linea_limpia) > 5:  # Ignorar líneas muy cortas
            contador_lineas[linea_limpia] = contador_lineas.get(linea_limpia, 0) + 1
    
    # Identificar líneas repetitivas (aparecen más de 3 veces)
    lineas_repetitivas = {linea for linea, count in contador_lineas.items() if count > 3}
    
    # Eliminar líneas repetitivas
    lineas_filtradas = []
    for linea in lineas:
        if linea.strip() not in lineas_repetitivas:
            lineas_filtradas.append(linea)
    
    md_limpio = '\n'.join(lineas_filtradas)
    
    # 6. LIMPIAR ESPACIOS EN BLANCO EXCESIVOS
    md_limpio = re.sub(r' {2,}', ' ', md_limpio)  # Múltiples espacios → uno solo
    md_limpio = re.sub(r'\t', '    ', md_limpio)  # Tabs → 4 espacios
    
    # 7. ARREGLAR ETIQUETAS HTML ROTAS (para Docusaurus/MDX)
    # Cambiar <br> por <br />
    md_limpio = re.sub(r'<br\s*>', '<br />', md_limpio)
    md_limpio = re.sub(r'<hr\s*>', '<hr />', md_limpio)
    
    # 8. LIMPIAR TABLAS MAL FORMADAS
    # Asegurar que separadores de tabla tienen guiones suficientes
    def arreglar_separador_tabla(match):
        num_cols = match.group(0).count('|') - 1
        return '|' + '---|' * num_cols
    
    md_limpio = re.sub(r'\|[\s\-:]+\|', arreglar_separador_tabla, md_limpio)
    
    # 9. ELIMINAR LÍNEAS QUE SOLO CONTIENEN PUNTOS/GUIONES (artefactos)
    md_limpio = re.sub(r'^[\.\-_]{3,}$', '', md_limpio, flags=re.MULTILINE)
    
    return md_limpio.strip()

def get_frontmatter(file_path: Path) -> str:
    """Genera la cabecera YAML para Docusaurus"""
    doc_id = simple_slug(file_path.stem)
    title = file_path.stem.replace("-", " ").replace("_", " ").title()
    
    return f"""---
id: {doc_id}
title: "{title}"
sidebar_label: "{title}"
---

"""

def process_pdfs(input_dir: Path, output_dir: Path, verbose: bool = True):
    """Procesa todos los PDFs encontrados"""
    if verbose:
        print(f"🔄 Buscando PDFs en: {input_dir}")
        print(f"📂 Destino: {output_dir}")
    
    pdf_files = list(input_dir.rglob("*.pdf"))
    if not pdf_files:
        print("❌ No se encontraron archivos PDF.")
        return

    exitos = 0
    errores = 0

    for pdf_path in pdf_files:
        try:
            # Calcular ruta relativa para mantener estructura
            rel_path = pdf_path.relative_to(input_dir)
            dest_path = output_dir / rel_path.with_suffix(".md")
            
            # Crear carpetas si no existen
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            if verbose:
                print(f"\n📖 Procesando: {pdf_path.name}")
            
            # 1. Convertir PDF a Markdown
            if verbose:
                print(f"   ⚙️  Extrayendo texto del PDF...")
            md_content = pymupdf4llm.to_markdown(pdf_path)
            
            # 2. Limpiar Markdown
            if verbose:
                print(f"   🧹 Limpiando Markdown...")
            md_limpio = limpiar_markdown(md_content)
            
            # 3. Añadir Frontmatter
            final_content = get_frontmatter(pdf_path) + md_limpio
            
            # 4. Guardar archivo
            dest_path.write_text(final_content, encoding="utf-8")
            
            if verbose:
                print(f"   ✅ Guardado: {dest_path}")
                print(f"   📊 Tamaño original: {len(md_content)} → Limpio: {len(md_limpio)} chars")
            
            exitos += 1
            
        except Exception as e:
            print(f"   ❌ ERROR: {e}")
            errores += 1

    print(f"\n{'='*60}")
    print(f"📊 RESUMEN")
    print(f"{'='*60}")
    print(f"✅ Éxitos: {exitos}")
    print(f"❌ Errores: {errores}")
    print(f"📁 Total PDFs procesados: {len(pdf_files)}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Conversor mejorado de PDF a Markdown para Docusaurus"
    )
    parser.add_argument(
        '--input',
        default='pdf',
        help='Carpeta de origen con PDFs (default: pdf/)'
    )
    parser.add_argument(
        '--output',
        default='docs',
        help='Carpeta de destino para Markdown (default: docs/)'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Modo silencioso (menos output)'
    )
    
    args = parser.parse_args()
    
    PDF_DIR = Path(args.input)
    DOCS_DIR = Path(args.output)
    
    if not PDF_DIR.exists():
        print(f"⚠️  La carpeta origen '{PDF_DIR}' no existe.")
        print(f"   Creándola... Por favor, coloca tus PDFs ahí.")
        PDF_DIR.mkdir(parents=True)
        exit(0)

    if not DOCS_DIR.exists():
        print(f"ℹ️  Creando carpeta destino: '{DOCS_DIR}'")
        DOCS_DIR.mkdir(parents=True)
    
    process_pdfs(PDF_DIR, DOCS_DIR, verbose=not args.quiet)

