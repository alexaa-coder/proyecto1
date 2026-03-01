# convert_pymupdf_v3.py
# Conversor mejorado con expresiones regulares avanzadas
# Especializado en documentos normativos (ISO, UNE, EN, NIST, etc.)
# 100% GRATIS - Sin APIs de pago
#
# MEJORAS v3:
#   - simple_slug() soporta Unicode/acentos
#   - Limpieza de índices mejorada
#   - Normalización de referencias
#   - Eliminación de bloques duplicados
#   - Procesamiento paralelo
#   - MODO DEBUG añadido

import re
import time
import unicodedata
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import pymupdf4llm

# ---------------------------------------------------------------------------
# Configuración global para modo debug
# ---------------------------------------------------------------------------

_DEBUG_MODE = False

def set_debug_mode(enabled: bool):
    """Activa o desactiva el modo debug globalmente."""
    global _DEBUG_MODE
    _DEBUG_MODE = enabled

def debug_log(mensaje: str, **kwargs):
    """
    Imprime mensajes solo si el modo debug está activo.
    
    Uso:
        debug_log("Líneas extraídas: {lineas}", lineas=1234)
        debug_log("Tablas: {tablas}, OK: {ok}", tablas=5, ok=3)
    """
    if _DEBUG_MODE:
        if kwargs:
            texto = mensaje.format(**kwargs)
        else:
            texto = mensaje
        print(f"[DEBUG] {texto}")


# ---------------------------------------------------------------------------
# Clase para estadísticas de conversión (modo debug)
# ---------------------------------------------------------------------------

class EstadisticasConversion:
    """Almacena métricas de la conversión para el modo debug."""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.lineas_raw = 0
        self.lineas_limpias = 0
        self.chars_raw = 0
        self.chars_limpios = 0
        self.tablas_detectadas = 0
        self.tablas_convertidas = 0
        self.bloques_duplicados_eliminados = 0
        self.palabras_guionadas_unidas = 0
        self.referencias_normalizadas = 0
    
    def mostrar_resumen(self):
        """Imprime resumen de estadísticas en modo debug."""
        if not _DEBUG_MODE:
            return
        
        print("\n" + "─" * 60)
        print("📊 ESTADÍSTICAS DE CONVERSIÓN")
        print("─" * 60)
        print(f"📄 Líneas:")
        print(f"   Raw    : {self.lineas_raw:,}")
        print(f"   Limpias: {self.lineas_limpias:,}")
        print(f"   Reducción: {self.lineas_raw - self.lineas_limpias:,} líneas")
        print(f"\n📝 Caracteres:")
        print(f"   Raw    : {self.chars_raw:,}")
        print(f"   Limpios: {self.chars_limpios:,}")
        reduccion_pct = (self.chars_raw - self.chars_limpios) / self.chars_raw * 100 if self.chars_raw else 0
        print(f"   Reducción: {self.chars_raw - self.chars_limpios:,} chars ({reduccion_pct:.1f}%)")
        print(f"\n📊 Procesamiento:")
        print(f"   Palabras guionadas unidas      : {self.palabras_guionadas_unidas}")
        print(f"   Referencias normalizadas        : {self.referencias_normalizadas}")
        print(f"   Bloques duplicados eliminados   : {self.bloques_duplicados_eliminados}")
        print(f"\n📦 Tablas:")
        print(f"   Detectadas : {self.tablas_detectadas}")
        print(f"   Convertidas: {self.tablas_convertidas}")
        if self.tablas_detectadas > 0:
            tasa = self.tablas_convertidas / self.tablas_detectadas * 100
            print(f"   Tasa éxito : {tasa:.1f}%")
        print("─" * 60 + "\n")

# Instancia global de estadísticas
_stats = EstadisticasConversion()


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def simple_slug(text: str) -> str:
    """
    Genera slug seguro para IDs de Docusaurus.
    Normaliza acentos y caracteres Unicode antes de slugificar.
    """
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^\w\-]", "-", text.lower()).strip("-")


# ---------------------------------------------------------------------------
# Etapas del pipeline de limpieza
# ---------------------------------------------------------------------------

def unir_palabras_guionadas(texto: str) -> str:
    """Restaura palabras cortadas con guión de fin de línea."""
    contador = len(re.findall(r"([a-záéíóúüñA-ZÁÉÍÓÚÜÑ])-\n([a-záéíóúüñA-ZÁÉÍÓÚÜÑ])", texto))
    _stats.palabras_guionadas_unidas += contador
    debug_log("Uniendo {n} palabras guionadas", n=contador)
    
    return re.sub(r"([a-záéíóúüñA-ZÁÉÍÓÚÜÑ])-\n([a-záéíóúüñA-ZÁÉÍÓÚÜÑ])", r"\1\2", texto)


def limpiar_indice(texto: str) -> str:
    """Limpia entradas de tabla de contenidos."""
    RE_TIENE_DOTS = re.compile(r"\.{3,}\s*\d")
    RE_QUITAR_DOTS_NUM = re.compile(r"\s*\.{3,}\s*\d+")

    lineas = texto.split("\n")
    resultado = []
    lineas_eliminadas = 0

    for linea in lineas:
        if not RE_TIENE_DOTS.search(linea):
            resultado.append(linea)
            continue

        limpia = RE_QUITAR_DOTS_NUM.sub("", linea).strip()
        if limpia:
            resultado.append(limpia)
        else:
            lineas_eliminadas += 1

    debug_log("Índice: {n} líneas de numeración eliminadas", n=lineas_eliminadas)
    return "\n".join(resultado)


def separar_secciones_fusionadas(texto: str) -> str:
    """Separa entradas de índice fusionadas en una sola línea."""
    lineas_antes = texto.count("\n")
    
    # Paso 1: expandir texto fusionado
    lineas = texto.split("\n")
    lineas_expandidas = []

    for linea in lineas:
        if len(linea) > 60 and re.search(r"\d[A-ZÁÉÍÓÚÜÑ]", linea):
            linea = re.sub(r"(\d)([A-ZÁÉÍÓÚÜÑ])", r"\1 \2", linea)
            linea = re.sub(r"([a-záéíóúüñ])(\d)", r"\1\n\2", linea)
            linea = re.sub(r"([a-záéíóúüñ])([A-ZÁÉÍÓÚÜÑ])", r"\1\n\2", linea)
            for sub in linea.split("\n"):
                sub = sub.strip()
                if sub:
                    lineas_expandidas.append(sub)
        else:
            lineas_expandidas.append(linea)

    texto = "\n".join(lineas_expandidas)

    # Paso 2: separar secciones con espacios
    RE_SECCION = re.compile(
        r"(?:^|(?<=\s))"
        r"((?:[A-Z]\.)?\d+(?:\.\d+)*)"
        r"(\s+[A-ZÁÉÍÓÚÜÑ])",
    )

    lineas = texto.split("\n")
    resultado = []

    for linea in lineas:
        matches = list(RE_SECCION.finditer(linea))

        if len(matches) < 2:
            resultado.append(linea)
            continue

        posiciones = [m.start() for m in matches]
        pre = linea[:posiciones[0]].strip()
        if pre:
            resultado.append(pre)

        for idx, pos in enumerate(posiciones):
            if idx + 1 < len(posiciones):
                fragmento = linea[pos:posiciones[idx + 1]].strip()
            else:
                fragmento = linea[pos:].strip()
            if fragmento:
                resultado.append(fragmento)

    texto_final = "\n".join(resultado)
    lineas_despues = texto_final.count("\n")
    
    debug_log("Secciones fusionadas: {antes} → {despues} líneas", 
              antes=lineas_antes, despues=lineas_despues)
    
    return texto_final


def limpiar_encabezados_pies(texto: str) -> str:
    """Elimina encabezados y pies de página repetitivos."""
    patron_num_norma = r"^\s*\d+\s*[-–—]\s*[A-Za-z]{2,}[\w/\-\s.:]+\d{4,}\s*$"
    patron_norma_num = r"^[A-Za-z]{2,}[\w/\-\s.:]+\d{4,}\s*[-–—]\s*\d+\s*$"
    patron_pagina = r"^\s*\d+\s*$"

    lineas = texto.split("\n")
    lineas_eliminadas = 0
    resultado = []
    
    for linea in lineas:
        if (re.match(patron_num_norma, linea) or
            re.match(patron_norma_num, linea) or
            re.match(patron_pagina, linea)):
            lineas_eliminadas += 1
            continue
        resultado.append(linea)

    debug_log("Encabezados/pies eliminados: {n} líneas", n=lineas_eliminadas)
    return "\n".join(resultado)


def _es_linea_protegida(linea: str) -> bool:
    """Determina si una línea NO debe fusionarse."""
    MARCADORES_INICIO = ("#", "-", "*", "|", ">", "```")
    if linea.startswith(MARCADORES_INICIO):
        return True
    if re.match(r"^\d+(?:\.\d+)*\s", linea):
        return True
    if re.match(
        r"^(NOTA|NOTE|EJEMPLO|EXAMPLE|ATENCIÓN|AVISO|WARNING|CAUTION)\s*\d*\s*:",
        linea, re.IGNORECASE,
    ):
        return True
    if len(linea) < 60 and linea and linea[0].isupper():
        return True
    return False


def fusionar_parrafos_rotos(texto: str) -> str:
    """Fusiona líneas cortadas arbitrariamente por el PDF."""
    FIN_FRASE = (".", ":", ";", "!", "?", ")")

    lineas = texto.split("\n")
    lineas_fusionadas = 0
    resultado = []
    i = 0

    while i < len(lineas):
        linea = lineas[i].rstrip()

        if not linea:
            resultado.append("")
            i += 1
            continue

        if _es_linea_protegida(linea):
            resultado.append(linea)
            i += 1
            continue

        if linea.endswith(FIN_FRASE):
            resultado.append(linea)
            i += 1
            continue

        if i + 1 < len(lineas):
            sig = lineas[i + 1].lstrip()
            if not sig or _es_linea_protegida(sig):
                resultado.append(linea)
                i += 1
            else:
                resultado.append(linea + " " + sig)
                lineas_fusionadas += 1
                i += 2
        else:
            resultado.append(linea)
            i += 1

    debug_log("Párrafos fusionados: {n} líneas unidas", n=lineas_fusionadas)
    return "\n".join(resultado)


def normalizar_referencias(texto: str) -> str:
    """Limpia referencias cruzadas y citas normativas."""
    contador = 0
    
    # Referencias partidas
    nuevo, n1 = re.subn(
        r"(\b(?:véase|see|clause|cláusula|apartado|section)\b)\n(\d[\d\.]*)",
        r"\1 \2",
        texto,
        flags=re.IGNORECASE,
    )
    contador += n1
    
    # Espacios en citas ISO
    nuevo, n2 = re.subn(
        r"\[([A-Z]{2,}[/\-\w\s]+?)\s*:\s*(\d{4})\]",
        r"[\1:\2]",
        nuevo,
    )
    contador += n2
    
    # Separador coma-año
    nuevo, n3 = re.subn(
        r"\b(ISO|UNE|EN|NIST|IEC|IEEE)([\w/\-\s]+),\s*(\d{4})\b",
        r"\1\2:\3",
        nuevo,
    )
    contador += n3
    
    _stats.referencias_normalizadas += contador
    debug_log("Referencias normalizadas: {n}", n=contador)
    return nuevo


def limpiar_simbolos_pdf(texto: str) -> str:
    """Reemplaza símbolos Unicode mal extraídos."""
    reemplazos = [
        (r"\u00ad", "-"),
        (r"\u2010|\u2011|\u2012|\u2013|\u2014", "-"),
        (r"[\u201c\u201d\u201e\u201f]", '"'),
        (r"[\u2018\u2019\u201a\u201b]", "'"),
        (r"\u2026", "..."),
        (r"^[\u2022\u2023\u25e6\u2043\u2219]\s*", "- "),
        (r"\u00a0", " "),
        (r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", ""),
    ]

    for patron, reemplazo in reemplazos:
        if patron.startswith("^"):
            texto = re.sub(patron, reemplazo, texto, flags=re.MULTILINE)
        else:
            texto = re.sub(patron, reemplazo, texto)

    return texto


def arreglar_bold_roto(texto: str) -> str:
    """Arregla marcadores bold/negrita mal formados."""
    texto = re.sub(r"\*\*\s+(.+?)\s+\*\*", r"**\1**", texto)
    texto = re.sub(r"\*\*(.+?)\s+\*\*", r"**\1**", texto)
    texto = re.sub(r"\*\*\s+(.+?)\*\*", r"**\1**", texto)
    texto = re.sub(r"\*\*\s*\*\*", "", texto)
    texto = re.sub(r"\*{4,}(.+?)\*{4,}", r"**\1**", texto)
    return texto


def limpiar_espacios_multiples(texto: str) -> str:
    """Normaliza espacios múltiples y líneas en blanco."""
    texto = re.sub(r" {2,}", " ", texto)
    texto = re.sub(r"\t", "    ", texto)
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto


def arreglar_html_mdx(texto: str) -> str:
    """Convierte etiquetas HTML a forma JSX auto-cerrada."""
    texto = re.sub(r"<br\s*>", "<br />", texto, flags=re.IGNORECASE)
    texto = re.sub(r"<hr\s*>", "<hr />", texto, flags=re.IGNORECASE)
    texto = re.sub(r"<img([^>]+)(?<!/)>", r"<img\1 />", texto, flags=re.IGNORECASE)
    return texto


def limpiar_tablas(texto: str) -> str:
    """Normaliza líneas de separación de tablas Markdown."""
    lineas = texto.split("\n")
    resultado = []
    tablas_arregladas = 0
    
    for linea in lineas:
        if re.match(r"^\s*\|[\s\-:|]+\|\s*$", linea):
            num_pipes = linea.count("|")
            if num_pipes >= 2:
                num_cols = num_pipes - 1
                resultado.append("|" + "---|" * num_cols)
                tablas_arregladas += 1
            else:
                resultado.append(linea)
        else:
            resultado.append(linea)
    
    debug_log("Separadores de tabla arreglados: {n}", n=tablas_arregladas)
    return "\n".join(resultado)


def eliminar_bloques_duplicados(texto: str) -> str:
    """Detecta y elimina bloques de texto repetidos."""
    # Limpiar placeholders "ColN"
    texto = re.sub(r"\tCol\d+", "", texto)

    # Expandir líneas con tabs
    lineas = texto.split("\n")
    lineas_expandidas = []
    for linea in lineas:
        if "\t" in linea:
            segmentos = linea.split("\t")
            for seg in segmentos:
                seg = seg.strip()
                if seg:
                    lineas_expandidas.append(seg)
        else:
            lineas_expandidas.append(linea)

    texto = "\n".join(lineas_expandidas)

    # Deduplicar párrafos
    parrafos = re.split(r"\n{2,}", texto)
    vistos = set()
    resultado = []
    bloques_eliminados = 0

    for parrafo in parrafos:
        p_stripped = parrafo.strip()
        if not p_stripped:
            continue

        num_lineas = p_stripped.count("\n") + 1
        if num_lineas >= 3:
            clave = p_stripped
            if clave in vistos:
                bloques_eliminados += 1
                continue
            vistos.add(clave)

        resultado.append(p_stripped)

    _stats.bloques_duplicados_eliminados += bloques_eliminados
    debug_log("Bloques duplicados eliminados: {n}", n=bloques_eliminados)
    
    return "\n\n".join(resultado)


def reconstruir_tablas_tab(texto: str) -> str:
    """Detecta secuencias tab-separated y las convierte a tablas Markdown."""
    lineas = texto.split("\n")
    resultado = []
    buffer_tabla = []
    num_cols_actual = 0
    tablas_construidas = 0

    def flush_tabla():
        nonlocal buffer_tabla, num_cols_actual, tablas_construidas
        if len(buffer_tabla) >= 2 and num_cols_actual >= 2:
            for idx, fila in enumerate(buffer_tabla):
                celdas = [c.strip() for c in fila.split("\t")]
                while len(celdas) < num_cols_actual:
                    celdas.append("")
                resultado.append("| " + " | ".join(celdas) + " |")
                if idx == 0:
                    resultado.append("|" + "---|" * num_cols_actual)
            tablas_construidas += 1
            _stats.tablas_convertidas += 1
        else:
            for fila in buffer_tabla:
                resultado.append(fila)
        buffer_tabla = []
        num_cols_actual = 0

    for linea in lineas:
        num_tabs = linea.count("\t")
        if num_tabs >= 1:
            _stats.tablas_detectadas += 1
            cols = num_tabs + 1
            if buffer_tabla and cols != num_cols_actual:
                flush_tabla()
            num_cols_actual = cols
            buffer_tabla.append(linea)
        else:
            if buffer_tabla:
                flush_tabla()
            resultado.append(linea)

    if buffer_tabla:
        flush_tabla()

    debug_log("Tablas tab-separated: {detectadas} detectadas, {convertidas} convertidas", 
              detectadas=_stats.tablas_detectadas, 
              convertidas=tablas_construidas)
    
    return "\n".join(resultado)


def limpiar_artefactos(texto: str) -> str:
    """Elimina líneas de solo puntos/guiones y caracteres de control."""
    texto = re.sub(r"^[\.\-_]{3,}\s*$", "", texto, flags=re.MULTILINE)
    texto = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", texto)
    return texto


# ---------------------------------------------------------------------------
# Pipeline principal
# ---------------------------------------------------------------------------

def limpiar_markdown_completo(md_texto: str, verbose: bool = True) -> str:
    """Aplica el pipeline completo de limpieza."""
    # Resetear estadísticas
    _stats.reset()
    _stats.chars_raw = len(md_texto)
    _stats.lineas_raw = md_texto.count("\n") + 1
    
    debug_log("=" * 60)
    debug_log("INICIANDO PIPELINE DE LIMPIEZA")
    debug_log("=" * 60)
    
    pasos = [
        ("🔗 Uniendo palabras guionadas",          unir_palabras_guionadas),
        ("🧹 Limpiando símbolos PDF",              limpiar_simbolos_pdf),
        ("🧹 Limpiando índice",                    limpiar_indice),
        ("🧹 Separando secciones fusionadas",      separar_secciones_fusionadas),
        ("🧹 Eliminando encabezados/pies",         limpiar_encabezados_pies),
        ("🔗 Normalizando referencias",            normalizar_referencias),
        ("🧹 Arreglando bold/negrita roto",        arreglar_bold_roto),
        ("🧹 Fusionando párrafos rotos",           fusionar_parrafos_rotos),
        ("🧹 Limpiando espacios",                  limpiar_espacios_multiples),
        ("🧹 Arreglando HTML/MDX",                 arreglar_html_mdx),
        ("📦 Eliminando bloques duplicados",       eliminar_bloques_duplicados),
        ("📦 Reconstruyendo tablas tab",           reconstruir_tablas_tab),
        ("🧹 Arreglando tablas",                   limpiar_tablas),
        ("🧹 Eliminando artefactos",               limpiar_artefactos),
    ]

    texto = md_texto
    for nombre, fn in pasos:
        if verbose:
            print(f"      {nombre}...")
        texto = fn(texto)

    # Actualizar estadísticas finales
    _stats.chars_limpios = len(texto)
    _stats.lineas_limpias = texto.count("\n") + 1
    
    # Mostrar resumen en modo debug
    _stats.mostrar_resumen()
    
    return texto.strip()


# ---------------------------------------------------------------------------
# Frontmatter Docusaurus
# ---------------------------------------------------------------------------

def get_frontmatter(file_path: Path) -> str:
    """Genera el bloque YAML para Docusaurus."""
    doc_id = simple_slug(file_path.stem)
    title = file_path.stem.replace("-", " ").replace("_", " ").title()
    return f"""---
id: {doc_id}
title: "{title}"
sidebar_label: "{title}"
---

"""


# ---------------------------------------------------------------------------
# Conversión de un PDF
# ---------------------------------------------------------------------------

def convertir_pdf(pdf_path: Path, output_path: Path, verbose: bool = True) -> bool:
    """Convierte un único archivo PDF a Markdown limpio."""
    try:
        t_inicio = time.time()
        
        if verbose:
            print(f"\n📖 Procesando: {pdf_path.name}")
            print(f"   ⚙  Extrayendo texto del PDF...")

        md_raw = pymupdf4llm.to_markdown(str(pdf_path))

        if verbose:
            print(f"   📊 Texto extraído: {len(md_raw):,} caracteres")
            print(f"   🔧 Aplicando limpieza avanzada...")

        md_limpio = limpiar_markdown_completo(md_raw, verbose=verbose)
        contenido_final = get_frontmatter(pdf_path) + md_limpio

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(contenido_final, encoding="utf-8")

        t_total = time.time() - t_inicio
        
        if verbose:
            reduccion = len(md_raw) - len(md_limpio)
            pct = reduccion / len(md_raw) * 100 if md_raw else 0
            print(f"   ✅ Guardado: {output_path}")
            print(f"   📉 Reducción: {reduccion:,} chars ({pct:.1f}%)")
        
        debug_log("⏱  Tiempo de conversión: {t:.2f}s", t=t_total)

        return True

    except Exception as e:
        print(f"   ❌ ERROR en {pdf_path.name}: {e}")
        return False


# ---------------------------------------------------------------------------
# Procesamiento masivo
# ---------------------------------------------------------------------------

def procesar_carpeta(
    input_dir: Path,
    output_dir: Path,
    verbose: bool = True,
    workers: int = 1,
):
    """Procesa todos los PDFs de una carpeta."""
    separador = "=" * 70

    if verbose:
        print(f"\n{separador}")
        print(f"🔄 INICIANDO CONVERSIÓN — v3")
        print(f"{separador}")
        print(f"📁 Origen : {input_dir}")
        print(f"📂 Destino: {output_dir}")
        print(f"⚡ Workers: {workers}")
        if _DEBUG_MODE:
            print(f"🐛 Modo DEBUG: ACTIVO")

    pdf_files = list(input_dir.rglob("*.pdf"))

    if not pdf_files:
        print("❌ No se encontraron archivos PDF.")
        return

    print(f"📊 Total PDFs encontrados: {len(pdf_files)}\n")
    t_inicio = time.time()

    exitos = 0
    errores = 0

    def _tarea(pdf_path: Path):
        rel_path = pdf_path.relative_to(input_dir)
        out_path = output_dir / rel_path.with_suffix(".md")
        return convertir_pdf(pdf_path, out_path, verbose=(workers == 1 and verbose))

    if workers == 1:
        for pdf_path in pdf_files:
            if _tarea(pdf_path):
                exitos += 1
            else:
                errores += 1
    else:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futuros = {executor.submit(_tarea, p): p for p in pdf_files}
            procesados = 0
            for futuro in as_completed(futuros):
                procesados += 1
                nombre = futuros[futuro].name
                ok = futuro.result()
                estado = "✅" if ok else "❌"
                print(f"  [{procesados}/{len(pdf_files)}] {estado} {nombre}")
                if ok:
                    exitos += 1
                else:
                    errores += 1

    t_total = time.time() - t_inicio
    velocidad = len(pdf_files) / (t_total / 60) if t_total > 0 else 0

    print(f"\n{separador}")
    print(f"📊 RESUMEN FINAL")
    print(f"{separador}")
    print(f"✅ Conversiones exitosas : {exitos}")
    print(f"❌ Errores              : {errores}")
    print(f"📁 Total procesados     : {len(pdf_files)}")
    print(f"⏱  Tiempo total         : {t_total:.1f}s")
    print(f"⚡ Velocidad            : {velocidad:.1f} PDFs/min")
    print(f"📂 Archivos en          : {output_dir}")
    print(f"{separador}\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Conversor PDF → Markdown con limpieza avanzada (GRATIS) — v3",
        epilog=(
            "Ejemplos:\n"
            "  python convert_pymupdf_v3.py\n"
            "  python convert_pymupdf_v3.py --input mis-pdfs/ --output docs/\n"
            "  python convert_pymupdf_v3.py --workers 4\n"
            "  python convert_pymupdf_v3.py --debug\n"
            "  python convert_pymupdf_v3.py --quiet\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--input",   default="pdf",  help="Carpeta origen con PDFs  (default: pdf/)")
    parser.add_argument("--output",  default="docs", help="Carpeta destino Markdown  (default: docs/)")
    parser.add_argument("--workers", default=1, type=int,
                        help="Hilos paralelos para conversión masiva (default: 1)")
    parser.add_argument("--debug",   action="store_true", 
                        help="Modo debug: muestra estadísticas detalladas")
    parser.add_argument("--quiet",   action="store_true", help="Modo silencioso")

    args = parser.parse_args()

    # Activar modo debug si se especificó
    if args.debug:
        set_debug_mode(True)

    input_path  = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"⚠  Carpeta '{input_path}' no existe. Creándola...")
        input_path.mkdir(parents=True)
        print(f"   ℹ  Coloca tus PDFs en '{input_path}' y ejecuta de nuevo.")
        raise SystemExit(0)

    output_path.mkdir(parents=True, exist_ok=True)

    procesar_carpeta(
        input_path,
        output_path,
        verbose=not args.quiet,
        workers=args.workers,
    )
