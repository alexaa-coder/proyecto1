#!/usr/bin/env python3
"""
add_frontmatter.py
==================
Añade frontmatter YAML a todos los archivos .md de docs/ que no lo tengan.
Genera etiquetas, responsable, fecha de revisión y clasificación
inferidos del path y del contenido del archivo.

Ejecutar DESPUÉS de reorganizar_final.py:
    cd /home/usuario/documentacion-proyecto1
    python3 add_frontmatter.py

Genera add_frontmatter.log con cada operación.
"""

import re
import logging
from datetime import date
from pathlib import Path

DOCS    = Path("docs")
LOG     = Path("add_frontmatter.log")
TODAY   = date.today().isoformat()   # "2025-MM-DD"

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger(__name__)


# ══════════════════════════════════════════════════════════════════════════════
# Reglas de inferencia a partir del path
# ══════════════════════════════════════════════════════════════════════════════

# Mapeo de palabras clave del path → responsable
RESPONSABLE_RULES = [
    (["manual-de-calidad", "mq-"],        "Director de Calidad"),
    (["pnt-", "procedimientos-generales"],  "Director de Calidad"),
    (["esp-", "procedimientos-especificos"],"Director de Calidad"),
    (["auditoria", "auditorias"],           "Director de Calidad"),
    (["no-conformidades", "capas"],         "Director de Calidad"),
    (["revision-por-la-direccion"],         "Director General"),
    (["politicas", "plt-"],                 "Responsable del SGSI"),
    (["procedimientos", "pro-"],            "Responsable del SGSI"),
    (["normas", "nrm-"],                    "Responsable del SGSI"),
    (["analisis-de-riesgos", "adr-"],       "Responsable del SGSI"),
    (["comite-de-seguridad"],               "Jefe de Seguridad"),
    (["pentesting", "auditoria-de-codigo"], "Jefe de Seguridad"),
    (["continuidad-del-negocio"],           "Responsable del SGSI"),
    (["nda"],                               "Responsable de RRHH"),
    (["formacion", "for-"],                 "Responsable de RRHH"),
    (["puestos-de-trabajo", "rpt-"],        "Responsable de RRHH"),
    (["proveedores"],                       "Responsable Comercial"),
    (["gestion-riesgos"],                   "Director de Calidad"),
]

# Mapeo de sección → clasificación
CLASIFICACION_RULES = {
    "politicas":               "USO PÚBLICO",
    "procedimientos":          "USO INTERNO",
    "normas":                  "USO INTERNO",
    "analisis-de-riesgos":     "USO INTERNO RESTRINGIDO",
    "registros":               "USO INTERNO",
    "control-documentos":      "USO INTERNO RESTRINGIDO",
    "auditoria-interna":       "USO INTERNO RESTRINGIDO",
    "versiones-historicas":    "HISTÓRICO",
    "transversal":             "USO INTERNO",
    "words-fuentes":           "HISTÓRICO",
    "basura":                  "HISTÓRICO",
}

# Mapeo de sección docusaurus → etiquetas base
TAGS_RULES = [
    ("calidad-iso13485",            ["iso-13485", "calidad"]),
    ("seguridad-iso27001",          ["iso-27001", "seguridad"]),
    ("01-contexto-organizacion",    ["contexto", "alcance"]),
    ("02-liderazgo",                ["liderazgo", "politica"]),
    ("03-planificacion",            ["planificacion", "objetivos"]),
    ("04-soporte",                  ["soporte", "formacion"]),
    ("05-operacion",                ["operacion", "procedimiento"]),
    ("06-evaluacion-desempeno",     ["evaluacion", "auditoria", "registros"]),
    ("07-mejora",                   ["mejora", "capa"]),
    ("manual-de-calidad",           ["manual-calidad"]),
    ("procedimientos-generales",    ["pnt"]),
    ("procedimientos-especificos",  ["esp"]),
    ("politicas",                   ["politica"]),
    ("procedimientos",              ["procedimiento"]),
    ("analisis-de-riesgos",         ["riesgos", "aarr"]),
    ("continuidad-del-negocio",     ["continuidad", "cdn"]),
    ("seguridad-del-desarrollo",    ["desarrollo-seguro", "pentesting"]),
    ("nda",                         ["confidencialidad", "nda"]),
    ("formacion",                   ["formacion", "concienciacion"]),
    ("puestos-de-trabajo",          ["rrhh", "puestos"]),
    ("proveedores",                 ["proveedores"]),
    ("gestion-riesgos",             ["riesgos"]),
    ("no-conformidades",            ["no-conformidad", "capa"]),
    ("auditoria",                   ["auditoria"]),
    ("revision-por-la-direccion",   ["revision-direccion"]),
    ("medicion-procesos",           ["kpi", "medicion"]),
    ("registros",                   ["registros"]),
    ("versiones-historicas",        ["historico"]),
    ("transversal",                 ["transversal"]),
    ("en",                          ["english"]),
]


def inferir_responsable(path_str: str) -> str:
    p = path_str.lower()
    for keywords, resp in RESPONSABLE_RULES:
        if any(k in p for k in keywords):
            return resp
    return "Director de Calidad"


def inferir_clasificacion(path_str: str) -> str:
    p = path_str.lower()
    for kw, cls in CLASIFICACION_RULES.items():
        if kw in p:
            return cls
    # Por defecto según norma
    if "seguridad" in p:
        return "USO INTERNO"
    return "USO INTERNO"


def inferir_tags(path_str: str) -> list:
    p = path_str.lower()
    tags = set()
    for kw, tag_list in TAGS_RULES:
        if kw in p:
            tags.update(tag_list)
    # Añadir "en" si está en subcarpeta EN/
    if "/en/" in p or "\\en\\" in p:
        tags.add("english")
    return sorted(tags)


def inferir_titulo(filepath: Path, content: str) -> str:
    """Extrae el primer H1 del contenido, o genera un título desde el nombre del archivo."""
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    # Fallback: nombre del archivo humanizado
    name = filepath.stem
    name = re.sub(r'[-_]', ' ', name)
    name = re.sub(r'\s+', ' ', name)
    return name.title()


def has_frontmatter(content: str) -> bool:
    """Devuelve True si el archivo ya tiene frontmatter YAML."""
    return content.lstrip().startswith("---")


def build_frontmatter(filepath: Path, content: str) -> str:
    """Construye el bloque frontmatter para el archivo."""
    path_str = str(filepath)

    titulo        = inferir_titulo(filepath, content)
    responsable   = inferir_responsable(path_str)
    clasificacion = inferir_clasificacion(path_str)
    tags          = inferir_tags(path_str)

    # Idioma
    idioma = "en" if ("/en/" in path_str.lower() or "\\en\\" in path_str.lower()) else "es"

    # Construir lista de tags YAML
    if tags:
        tags_yaml = "\n".join(f"  - {t}" for t in tags)
    else:
        tags_yaml = "  - general"

    fm = f"""---
title: "{titulo}"
sidebar_label: "{titulo}"
responsable: "{responsable}"
clasificacion: "{clasificacion}"
fecha_revision: "{TODAY}"
idioma: "{idioma}"
tags:
{tags_yaml}
---

"""
    return fm


def process_file(filepath: Path):
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        log.warning(f"No se pudo leer {filepath}: {e}")
        return

    if has_frontmatter(content):
        log.info(f"SKIP (ya tiene FM): {filepath}")
        return

    fm = build_frontmatter(filepath, content)
    new_content = fm + content

    try:
        filepath.write_text(new_content, encoding="utf-8")
        log.info(f"FM  {filepath}")
    except Exception as e:
        log.warning(f"No se pudo escribir {filepath}: {e}")


# ══════════════════════════════════════════════════════════════════════════════
# Archivos a excluir (no son documentación navegable)
# ══════════════════════════════════════════════════════════════════════════════

EXCLUDE_PATTERNS = [
    "transversal/basura",
    "transversal/norma1-fat32",
    "transversal/words-fuentes",
    "-all-errors",
    "spika-tech---code-checker",
]


def should_skip(filepath: Path) -> bool:
    p = str(filepath).replace("\\", "/").lower()
    return any(pat in p for pat in EXCLUDE_PATTERNS)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    if not DOCS.exists():
        log.error("No se encuentra docs/. Ejecuta desde la raíz del proyecto.")
        return

    md_files = list(DOCS.rglob("*.md"))
    total    = len(md_files)
    skipped  = 0
    added    = 0

    log.info("═" * 60)
    log.info(f"  add_frontmatter.py — {total} archivos encontrados")
    log.info("═" * 60)

    for f in sorted(md_files):
        if should_skip(f):
            log.info(f"EXCLUIDO: {f}")
            skipped += 1
            continue
        before = f.read_text(encoding="utf-8", errors="replace")
        process_file(f)
        after  = f.read_text(encoding="utf-8", errors="replace")
        if before != after:
            added += 1

    log.info("═" * 60)
    log.info(f"  FIN — {added} archivos con FM añadido, {skipped} excluidos")
    log.info("═" * 60)


if __name__ == "__main__":
    main()
