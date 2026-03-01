# convert_pymupdf_v3.py
# Conversor mejorado con expresiones regulares avanzadas
# Especializado en documentos normativos (ISO, UNE, EN, NIST, etc.)
# 100% GRATIS - Sin APIs de pago
#
# MEJORAS respecto a v2:
#   - simple_slug() soporta Unicode/acentos (evita IDs rotos en Docusaurus)
#   - limpiar_indice() usa patrón más seguro que no elimina números de texto real
#   - limpiar_encabezados_pies() es genérico (cualquier norma, no solo UNE-ISO)
#   - unir_palabras_guionadas() nueva: restaura palabras cortadas con guión
#   - fusionar_parrafos_rotos() protege bloques NOTA/EJEMPLO/AVISO
#   - normalizar_referencias() nueva: limpia referencias ISO partidas o mal formateadas
#   - limpiar_simbolos_pdf() nueva: reemplaza símbolos Unicode mal extraídos
#   - Procesamiento paralelo con ThreadPoolExecutor para conversión masiva
#   - Resumen de conversión con tiempo total y velocidad (PDFs/min)

import re
import time
import unicodedata
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import pymupdf4llm


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def simple_slug(text: str) -> str:
    """
    Genera slug seguro para IDs de Docusaurus.
    Normaliza acentos y caracteres Unicode antes de slugificar.
    Ejemplo: "Índice General" → "indice-general"
    """
    # NFKD separa la letra base del acento: "é" → "e" + combining accent
    text = unicodedata.normalize("NFKD", text)
    # Descartar los bytes no ASCII (los acentos combinados)
    text = text.encode("ascii", "ignore").decode("ascii")
    # Reemplazar todo lo que no sea alfanumérico/guión por guión
    return re.sub(r"[^\w\-]", "-", text.lower()).strip("-")


# ---------------------------------------------------------------------------
# Etapas del pipeline de limpieza
# ---------------------------------------------------------------------------

def unir_palabras_guionadas(texto: str) -> str:
    """
    Restaura palabras cortadas con guión de fin de línea (muy frecuente en PDFs).
    Ejemplo:
        "nor-\\nnalización" → "normalización"
        "inter-\\noperabilidad" → "interoperabilidad"
    Solo actúa si tanto el prefijo como el sufijo son letras (no guiones de lista).
    """
    return re.sub(r"([a-záéíóúüñA-ZÁÉÍÓÚÜÑ])-\n([a-záéíóúüñA-ZÁÉÍÓÚÜÑ])", r"\1\2", texto)


def limpiar_indice(texto: str) -> str:
    """
    Limpia entradas de tabla de contenidos: quita puntos y números de página
    pero NUNCA elimina el texto descriptivo.

    Solo actúa sobre líneas que contengan "....N" (3+ puntos + dígito).
    Elimina cada ocurrencia de puntos suspensivos + número de página.
    Si la línea queda vacía, se descarta.
    """
    RE_TIENE_DOTS = re.compile(r"\.{3,}\s*\d")
    RE_QUITAR_DOTS_NUM = re.compile(r"\s*\.{3,}\s*\d+")

    lineas = texto.split("\n")
    resultado = []

    for linea in lineas:
        if not RE_TIENE_DOTS.search(linea):
            resultado.append(linea)
            continue

        limpia = RE_QUITAR_DOTS_NUM.sub("", linea).strip()
        if limpia:
            resultado.append(limpia)

    return "\n".join(resultado)


def separar_secciones_fusionadas(texto: str) -> str:
    """
    Separa entradas de índice (o secciones) que pymupdf4llm fusionó en una
    sola línea. Actúa sobre TODAS las líneas, no solo las que tenían puntos.

    Maneja DOS casos:
    ① Texto completamente pegado sin espacios (pymupdf4llm lo extrajo así):
       "Prólogo0Introducción0.1Generalidades" → líneas separadas
    ② Texto con espacios pero secciones en la misma línea:
       "4 Contexto 4.1 Comprensión" → líneas separadas

    Solo actúa en líneas largas (>60 chars) con 2+ patrones de sección
    para no romper texto normal.
    """

    # ── Paso 1: expandir texto completamente fusionado ──────────────────
    # Solo en líneas largas que contengan patrón dígito+mayúscula pegados
    lineas = texto.split("\n")
    lineas_expandidas = []

    for linea in lineas:
        # Detectar si la línea tiene texto fusionado (>60 chars y dígito pegado a mayúscula)
        if len(linea) > 60 and re.search(r"\d[A-ZÁÉÍÓÚÜÑ]", linea):
            # Insertar espacio entre dígito y mayúscula: "0Introducción" → "0 Introducción"
            linea = re.sub(r"(\d)([A-ZÁÉÍÓÚÜÑ])", r"\1 \2", linea)
            # Insertar salto de línea entre minúscula y dígito: "Prólogo0" → "Prólogo\n0"
            linea = re.sub(r"([a-záéíóúüñ])(\d)", r"\1\n\2", linea)
            # Insertar salto de línea entre minúscula y mayúscula pegadas:
            # "ÍndicePrólogo" → "Índice\nPrólogo"
            linea = re.sub(r"([a-záéíóúüñ])([A-ZÁÉÍÓÚÜÑ])", r"\1\n\2", linea)
            # Expandir las nuevas líneas generadas
            for sub in linea.split("\n"):
                sub = sub.strip()
                if sub:
                    lineas_expandidas.append(sub)
        else:
            lineas_expandidas.append(linea)

    texto = "\n".join(lineas_expandidas)

    # ── Paso 2: separar secciones con espacios en la misma línea ────────
    RE_SECCION = re.compile(
        r"(?:^|(?<=\s))"
        r"((?:[A-Z]\.)?\d+(?:\.\d+)*)"  # número de sección
        r"(\s+[A-ZÁÉÍÓÚÜÑ])",           # espacio + mayúscula
    )

    lineas = texto.split("\n")
    resultado = []

    for linea in lineas:
        matches = list(RE_SECCION.finditer(linea))

        if len(matches) < 2:
            resultado.append(linea)
            continue

        # Múltiples secciones fusionadas → separar
        posiciones = [m.start() for m in matches]

        # Conservar texto antes de la primera sección
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

    return "\n".join(resultado)


def limpiar_encabezados_pies(texto: str) -> str:
    """
    Elimina encabezados y pies de página repetitivos.

    MEJORA v3: patrones genéricos que funcionan con cualquier norma
    (ISO, UNE, EN, NIST, IEEE, IEC, GDPR, etc.) en lugar de solo UNE-ISO/IEC.

    Detecta:
      "    3 - ISO/IEC 27001:2022"
      "UNE-EN 9001:2015 - 12"
      "NIST SP 800-53 Rev. 5 — 7"
      Líneas que son solo un número de página
    """
    # Número + separador + identificador de norma
    patron_num_norma = r"^\s*\d+\s*[-–—]\s*[A-Za-z]{2,}[\w/\-\s.:]+\d{4,}\s*$"
    # Identificador de norma + separador + número
    patron_norma_num = r"^[A-Za-z]{2,}[\w/\-\s.:]+\d{4,}\s*[-–—]\s*\d+\s*$"
    # Solo número de página
    patron_pagina = r"^\s*\d+\s*$"

    lineas = texto.split("\n")
    resultado = []
    for linea in lineas:
        if (
            re.match(patron_num_norma, linea)
            or re.match(patron_norma_num, linea)
            or re.match(patron_pagina, linea)
        ):
            continue
        resultado.append(linea)

    return "\n".join(resultado)


def _es_linea_protegida(linea: str) -> bool:
    """
    Determina si una línea NO debe fusionarse con la anterior/siguiente.
    Protege:
      - Marcadores Markdown (#, -, *, |, >, ```)
      - Líneas que empiezan con número de sección (0 , 4.1 , 10.2.3 )
      - Bloques normativos (NOTA:, EJEMPLO:, etc.)
      - Líneas cortas (<60 chars) que empiezan con mayúscula: son títulos
        o entradas de índice, NO párrafos cortados.
        (Los párrafos cortados por el PDF son típicamente líneas largas
        que ocupaban el ancho completo de la página.)
    """
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
    # Líneas cortas que empiezan con mayúscula → probablemente títulos, no párrafos rotos
    if len(linea) < 60 and linea and linea[0].isupper():
        return True
    return False


def fusionar_parrafos_rotos(texto: str) -> str:
    """
    Fusiona líneas que fueron cortadas arbitrariamente por el extractor del PDF.
    Lógica: si una línea no termina en puntuación de cierre Y la siguiente
    no es una línea protegida, se unen con un espacio.

    Líneas protegidas (NO se fusionan):
      - Marcadores Markdown
      - Líneas que empiezan con número de sección
      - Bloques normativos (NOTA, AVISO, etc.)
      - Líneas cortas (<60 chars) que empiezan con mayúscula (títulos)
    """
    FIN_FRASE = (".", ":", ";", "!", "?", ")")

    lineas = texto.split("\n")
    resultado = []
    i = 0

    while i < len(lineas):
        linea = lineas[i].rstrip()

        if not linea:
            resultado.append("")
            i += 1
            continue

        # Si la línea actual es protegida, no fusionar con nada
        if _es_linea_protegida(linea):
            resultado.append(linea)
            i += 1
            continue

        # Si termina en puntuación, no fusionar
        if linea.endswith(FIN_FRASE):
            resultado.append(linea)
            i += 1
            continue

        # Intentar fusionar con la siguiente
        if i + 1 < len(lineas):
            sig = lineas[i + 1].lstrip()
            if not sig or _es_linea_protegida(sig):
                resultado.append(linea)
                i += 1
            else:
                resultado.append(linea + " " + sig)
                i += 2
        else:
            resultado.append(linea)
            i += 1

    return "\n".join(resultado)


def normalizar_referencias(texto: str) -> str:
    """
    NUEVA en v3: limpia referencias cruzadas y citas normativas.
    
    Corrige:
      - Referencias partidas entre líneas: "(véase\\n6.1.2)" → "(véase 6.1.2)"
      - Citas ISO con espacios: "[ISO 27001 : 2022]" → "[ISO 27001:2022]"
      - Citas con año separado: "ISO/IEC 27001, 2022" → "ISO/IEC 27001:2022"
    """
    # Referencias partidas (véase / see clause + salto de línea + número)
    texto = re.sub(
        r"(\b(?:véase|see|clause|cláusula|apartado|section)\b)\n(\d[\d\.]*)",
        r"\1 \2",
        texto,
        flags=re.IGNORECASE,
    )
    # Espacios extra alrededor de los dos puntos en citas: [ISO 27001 : 2022]
    texto = re.sub(
        r"\[([A-Z]{2,}[/\-\w\s]+?)\s*:\s*(\d{4})\]",
        r"[\1:\2]",
        texto,
    )
    # Normalizar separador coma-año: "ISO/IEC 27001, 2022" → "ISO/IEC 27001:2022"
    texto = re.sub(
        r"\b(ISO|UNE|EN|NIST|IEC|IEEE)([\w/\-\s]+),\s*(\d{4})\b",
        r"\1\2:\3",
        texto,
    )
    return texto


def limpiar_simbolos_pdf(texto: str) -> str:
    """
    NUEVA en v3: reemplaza símbolos Unicode mal extraídos por equivalentes ASCII/Markdown.
    Por ejemplo, viñetas especiales, flechas, comillas tipográficas, etc.
    """
    reemplazos = [
        # Flechas
        (r"→",  "→"),   # ya correcta, se mantiene
        (r"←",  "←"),
        (r"↔",  "↔"),
        # Guiones y rayas que PyMuPDF extrae como caracteres raros
        (r"\u00ad", "-"),   # soft hyphen
        (r"\u2010|\u2011|\u2012|\u2013|\u2014", "-"),  # varios tipos de guión/raya
        # Comillas tipográficas → comillas simples/dobles estándar
        (r"[\u201c\u201d\u201e\u201f]", '"'),
        (r"[\u2018\u2019\u201a\u201b]", "'"),
        # Puntos suspensivos tipográficos → tres puntos
        (r"\u2026", "..."),
        # Viñetas raras → guión de lista Markdown
        (r"^[\u2022\u2023\u25e6\u2043\u2219]\s*", "- ", ),
        # Espacio sin salto → espacio normal
        (r"\u00a0", " "),
        # Caracteres de control
        (r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", ""),
    ]

    for patron, reemplazo in reemplazos:
        if patron.startswith("^"):
            texto = re.sub(patron, reemplazo, texto, flags=re.MULTILINE)
        else:
            texto = re.sub(patron, reemplazo, texto)

    return texto


def arreglar_bold_roto(texto: str) -> str:
    """
    Arregla marcadores bold/negrita mal formados que genera pymupdf4llm.

    Problemas que corrige:
      - Espacio antes del cierre:  **3 **  → **3**
      - Espacio después de apertura: ** 3** → **3**
      - Bold vacío o solo espacios:  ** **  → (eliminado)
      - Bold anidado innecesario:    ****texto**** → **texto**
    """
    # 1. Quitar espacios internos al inicio/final del bold: ** texto ** → **texto**
    texto = re.sub(r"\*\*\s+(.+?)\s+\*\*", r"**\1**", texto)
    # 2. Espacio solo al final: **texto ** → **texto**
    texto = re.sub(r"\*\*(.+?)\s+\*\*", r"**\1**", texto)
    # 3. Espacio solo al inicio: ** texto** → **texto**
    texto = re.sub(r"\*\*\s+(.+?)\*\*", r"**\1**", texto)
    # 4. Bold vacío (solo espacios): ** ** o **** → eliminar
    texto = re.sub(r"\*\*\s*\*\*", "", texto)
    # 5. Bold anidado: ****texto**** → **texto**
    texto = re.sub(r"\*{4,}(.+?)\*{4,}", r"**\1**", texto)
    return texto


def limpiar_espacios_multiples(texto: str) -> str:
    """Normaliza espacios múltiples, tabulaciones y líneas en blanco consecutivas."""
    texto = re.sub(r" {2,}", " ", texto)
    texto = re.sub(r"\t", "    ", texto)
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto


def arreglar_html_mdx(texto: str) -> str:
    """Convierte etiquetas HTML vacías a su forma JSX auto-cerrada (requerido por MDX/Docusaurus)."""
    texto = re.sub(r"<br\s*>", "<br />", texto, flags=re.IGNORECASE)
    texto = re.sub(r"<hr\s*>", "<hr />", texto, flags=re.IGNORECASE)
    texto = re.sub(r"<img([^>]+)(?<!/)>", r"<img\1 />", texto, flags=re.IGNORECASE)
    return texto


def limpiar_tablas(texto: str) -> str:
    """Normaliza las líneas de separación de tablas Markdown."""
    lineas = texto.split("\n")
    resultado = []
    for linea in lineas:
        if re.match(r"^\s*\|[\s\-:|]+\|\s*$", linea):
            num_pipes = linea.count("|")
            if num_pipes >= 2:
                num_cols = num_pipes - 1
                resultado.append("|" + "---|" * num_cols)
            else:
                resultado.append(linea)
        else:
            resultado.append(linea)
    return "\n".join(resultado)


def eliminar_bloques_duplicados(texto: str) -> str:
    """
    Detecta y elimina bloques grandes de texto que se repiten.

    Artefacto común de pymupdf4llm con tablas complejas: para cada fila,
    vuelca TODO el contenido de la columna completa, generando repeticiones
    masivas del mismo bloque de texto.

    Estrategia:
      1. Dividir el texto en párrafos (bloques separados por línea vacía).
      2. Si un párrafo de 3+ líneas aparece más de una vez, conservar solo
         la primera ocurrencia.
      3. También detectar repeticiones dentro de una misma línea larga
         separada por tabs (celdas de tabla volcadas).
    """
    # ── Paso 1: limpiar placeholders "ColN" de cabeceras rotas ──────────
    texto = re.sub(r"\tCol\d+", "", texto)

    # ── Paso 2: deduplicar bloques idénticos separados por tabs ─────────
    # Cuando pymupdf4llm mete bloques enteros dentro de "celdas" separadas
    # por tab, primero descomponerlos.
    lineas = texto.split("\n")
    lineas_expandidas = []
    for linea in lineas:
        if "\t" in linea:
            # Separar por tabs y tratar cada segmento
            segmentos = linea.split("\t")
            for seg in segmentos:
                seg = seg.strip()
                if seg:
                    lineas_expandidas.append(seg)
        else:
            lineas_expandidas.append(linea)

    texto = "\n".join(lineas_expandidas)

    # ── Paso 3: deduplicar párrafos repetidos ───────────────────────────
    # Un "párrafo" = bloque de líneas no vacías consecutivas
    parrafos = re.split(r"\n{2,}", texto)
    vistos = set()
    resultado = []

    for parrafo in parrafos:
        p_stripped = parrafo.strip()
        if not p_stripped:
            continue

        # Solo deduplicar párrafos de 3+ líneas (los pequeños pueden ser
        # legítimamente repetidos, ej: encabezados de sección)
        num_lineas = p_stripped.count("\n") + 1
        if num_lineas >= 3:
            clave = p_stripped
            if clave in vistos:
                continue  # duplicado → saltar
            vistos.add(clave)

        resultado.append(p_stripped)

    return "\n\n".join(resultado)


def reconstruir_tablas_tab(texto: str) -> str:
    """
    Detecta secuencias de líneas con el mismo número de tabs y las convierte
    en tablas Markdown con delimitadores |.

    Solo actúa si hay 2+ líneas consecutivas con 2+ columnas tab-separated.
    """
    lineas = texto.split("\n")
    resultado = []
    buffer_tabla = []  # líneas que parecen ser filas de tabla
    num_cols_actual = 0

    def flush_tabla():
        nonlocal buffer_tabla, num_cols_actual
        if len(buffer_tabla) >= 2 and num_cols_actual >= 2:
            # Construir tabla Markdown
            for idx, fila in enumerate(buffer_tabla):
                celdas = [c.strip() for c in fila.split("\t")]
                # Rellenar celdas faltantes
                while len(celdas) < num_cols_actual:
                    celdas.append("")
                resultado.append("| " + " | ".join(celdas) + " |")
                if idx == 0:
                    resultado.append("|" + "---|" * num_cols_actual)
        else:
            # No es tabla suficiente → devolver como texto
            for fila in buffer_tabla:
                resultado.append(fila)
        buffer_tabla = []
        num_cols_actual = 0

    for linea in lineas:
        num_tabs = linea.count("\t")
        if num_tabs >= 1:  # al menos 2 columnas
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

    return "\n".join(resultado)


def limpiar_artefactos(texto: str) -> str:
    """Elimina líneas de solo puntos/guiones y caracteres de control residuales."""
    texto = re.sub(r"^[\.\-_]{3,}\s*$", "", texto, flags=re.MULTILINE)
    texto = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", texto)
    return texto


# ---------------------------------------------------------------------------
# Pipeline principal
# ---------------------------------------------------------------------------

def limpiar_markdown_completo(md_texto: str, verbose: bool = True) -> str:
    """
    Aplica el pipeline completo de limpieza en el orden correcto.
    El orden importa: primero unir guiones (nivel carácter), luego limpiar
    estructura, luego fusionar párrafos.
    """
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

    return texto.strip()


# ---------------------------------------------------------------------------
# Frontmatter Docusaurus
# ---------------------------------------------------------------------------

def get_frontmatter(file_path: Path) -> str:
    """Genera el bloque YAML que Docusaurus necesita al inicio del archivo .md."""
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
    """Convierte un único archivo PDF a Markdown limpio con frontmatter."""
    try:
        if verbose:
            print(f"\n📖 Procesando: {pdf_path.name}")
            print(f"   ⚙️  Extrayendo texto del PDF...")

        md_raw = pymupdf4llm.to_markdown(str(pdf_path))

        if verbose:
            print(f"   📊 Texto extraído: {len(md_raw):,} caracteres")
            print(f"   🔧 Aplicando limpieza avanzada...")

        md_limpio = limpiar_markdown_completo(md_raw, verbose=verbose)
        contenido_final = get_frontmatter(pdf_path) + md_limpio

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(contenido_final, encoding="utf-8")

        if verbose:
            reduccion = len(md_raw) - len(md_limpio)
            pct = reduccion / len(md_raw) * 100 if md_raw else 0
            print(f"   ✅ Guardado: {output_path}")
            print(f"   📉 Reducción: {reduccion:,} chars ({pct:.1f}%)")

        return True

    except Exception as e:
        print(f"   ❌ ERROR en {pdf_path.name}: {e}")
        return False


# ---------------------------------------------------------------------------
# Procesamiento masivo (con soporte de paralelismo)
# ---------------------------------------------------------------------------

def procesar_carpeta(
    input_dir: Path,
    output_dir: Path,
    verbose: bool = True,
    workers: int = 1,
):
    """
    Procesa todos los PDFs de una carpeta (recursivamente).

    Parámetros
    ----------
    workers : int
        Número de hilos paralelos. 1 = secuencial (por defecto).
        Para conversión masiva usa workers=4 o más según tu CPU.
        NOTA: pymupdf4llm no usa GIL de forma intensiva, así que
        el paralelismo funciona bien.
    """
    separador = "=" * 70

    if verbose:
        print(f"\n{separador}")
        print(f"🔄 INICIANDO CONVERSIÓN — v3")
        print(f"{separador}")
        print(f"📁 Origen : {input_dir}")
        print(f"📂 Destino: {output_dir}")
        print(f"⚡ Workers: {workers}")

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
        # Modo secuencial — mantiene output limpio
        for pdf_path in pdf_files:
            if _tarea(pdf_path):
                exitos += 1
            else:
                errores += 1
    else:
        # Modo paralelo — ideal para conversión masiva (decenas o cientos de PDFs)
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
    print(f"⏱️  Tiempo total         : {t_total:.1f}s")
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
            "  python convert_pymupdf_v3.py --quiet\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--input",   default="pdf",  help="Carpeta origen con PDFs  (default: pdf/)")
    parser.add_argument("--output",  default="docs", help="Carpeta destino Markdown  (default: docs/)")
    parser.add_argument("--workers", default=1, type=int,
                        help="Hilos paralelos para conversión masiva (default: 1)")
    parser.add_argument("--quiet",   action="store_true", help="Modo silencioso")

    args = parser.parse_args()

    input_path  = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"⚠️  Carpeta '{input_path}' no existe. Creándola...")
        input_path.mkdir(parents=True)
        print(f"   ℹ️  Coloca tus PDFs en '{input_path}' y ejecuta de nuevo.")
        raise SystemExit(0)

    output_path.mkdir(parents=True, exist_ok=True)

    procesar_carpeta(
        input_path,
        output_path,
        verbose=not args.quiet,
        workers=args.workers,
    )
