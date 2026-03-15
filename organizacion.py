#!/usr/bin/env python3
"""
reorganizar_final.py
====================
Reorganiza docs/ desde la estructura ACTUAL (post-v3-fallido) al plan definitivo.
Estado actual:
  - docs/ISO-13845/  → toda la documentación de calidad sin mover
  - docs/ISO-27001/  → toda la documentación de seguridad sin mover
  - docs/calidad-iso13485/    → solo index.md vacíos por sección
  - docs/seguridad-iso27001/  → solo index.md vacíos por sección

Ejecutar desde la raíz del proyecto Docusaurus:
    cd /home/usuario/documentacion-proyecto1
    python3 reorganizar_final.py

Genera reorganizar_final.log con cada operación.
HACER BACKUP ANTES de ejecutar.
"""

import shutil
import logging
from pathlib import Path

DOCS = Path("docs")
LOG  = Path("reorganizar_final.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger(__name__)

# ── Helpers ────────────────────────────────────────────────────────────────────

def mk(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def mv(src, dst):
    src, dst = Path(src), Path(dst)
    if not src.exists():
        log.warning(f"NO EXISTE  : {src}")
        return
    mk(dst.parent)
    if dst.exists():
        log.warning(f"YA EXISTE  : {dst}  (saltado)")
        return
    shutil.move(str(src), str(dst))
    log.info(f"MOV {src}  →  {dst}")

def mv_tree(src, dst):
    """Mueve una carpeta entera. Si dst ya existe, fusiona archivo por archivo."""
    src, dst = Path(src), Path(dst)
    if not src.exists():
        return
    if not dst.exists():
        mk(dst.parent)
        shutil.move(str(src), str(dst))
        log.info(f"MVTREE {src}  →  {dst}")
    else:
        for item in list(src.rglob("*.md")):
            rel = item.relative_to(src)
            mv(item, dst / rel)
        rm_tree(src)

def rm_tree(p: Path):
    if Path(p).exists():
        shutil.rmtree(str(p))
        log.info(f"RMTREE {p}")

def rm_empty(root: Path):
    for d in sorted(Path(root).rglob("*"), reverse=True):
        if d.is_dir():
            try:
                d.rmdir()
                log.info(f"RMD {d}")
            except OSError:
                pass


# ══════════════════════════════════════════════════════════════════════════════
# CALIDAD — mueve ISO-13845/ → calidad-iso13485/
# ══════════════════════════════════════════════════════════════════════════════

def migrate_calidad(docs: Path):
    src = docs / "ISO-13845"
    cal = docs / "calidad-iso13485"
    if not src.exists():
        log.info("ISO-13845/ no encontrado, saltando calidad")
        return

    # ── 01-contexto-organizacion ──────────────────────────────────────────
    c01 = cal / "01-contexto-organizacion"

    mv_tree(src / "certificado ISO 13485",
            c01 / "certificados")

    lp_src = src / "Licencia Previa de Funcionamiento"
    lp_dst = c01 / "licencia-previa"
    if lp_src.exists():
        # Mover todo excepto la subcarpeta Notificaciones/ primero
        for f in lp_src.glob("*.md"):
            mv(f, lp_dst / f.name)
        mv_tree(lp_src / "Notificaciones", lp_dst / "notificaciones")
        rm_tree(lp_src)

    # Normas de referencia (están en registros/Normas/ de ISO-13845)
    normas_src = src / "registros" / "Normas"
    mv_tree(normas_src, c01 / "normas-referencia")

    mv(src / "guia-uso.md", cal / "anexos" / "guia-uso.md")

    # ── 02-liderazgo ──────────────────────────────────────────────────────
    c02 = cal / "02-liderazgo"

    # Manual de Calidad: MQ_01.08 → vigente, el resto → versiones-historicas
    mq_base = src / "Manual de Calidad"
    for ver_dir in sorted(mq_base.iterdir()) if mq_base.exists() else []:
        if not ver_dir.is_dir():
            continue
        if ver_dir.name == "MQ_01.08_MANUAL DE CALIDAD":
            mv_tree(ver_dir, c02 / "manual-de-calidad")
        else:
            mv_tree(ver_dir, cal / "anexos" / "versiones-historicas" / ver_dir.name)
    if mq_base.exists():
        rm_tree(mq_base)

    # Compromiso calidad por la dirección
    mv_tree(src / "registros" / "Compromiso calidad por la dirección",
            c02 / "compromiso-direccion")

    # Puestos de trabajo
    pdt_src = src / "registros" / "Puestos de trabajo"
    if pdt_src.exists():
        mv_tree(pdt_src / "Asignaciones",  c02 / "puestos-de-trabajo" / "asignaciones")
        mv_tree(pdt_src / "Descripciones", c02 / "puestos-de-trabajo" / "descripciones")
        rm_tree(pdt_src)

    # ── 03-planificacion ──────────────────────────────────────────────────
    c03 = cal / "03-planificacion"
    mv_tree(src / "registros" / "Objetivos", c03 / "objetivos")
    mv_tree(src / "recursos documentación" / "Plantillas", c03 / "recursos" / "plantillas")

    # ── 04-soporte ────────────────────────────────────────────────────────
    c04 = cal / "04-soporte"
    mv_tree(src / "registros" / "Formación",      c04 / "formacion")
    mv_tree(src / "registros" / "Gestión de Pnts", c04 / "gestion-pnts")
    mv(src / "listado-pnts.md", c04 / "gestion-pnts" / "listado-pnts.md")

    # ── 05-operacion ──────────────────────────────────────────────────────
    c05 = cal / "05-operacion"

    # Procedimientos generales
    mv_tree(src / "procedimientos generales", c05 / "procedimientos-generales")

    # Procedimientos específicos
    mv_tree(src / "procedimientos específicos", c05 / "procedimientos-especificos")

    # Gestión de riesgos
    gr_src = src / "registros" / "Gestión de Riesgos"
    if gr_src.exists():
        mv_tree(gr_src / "Sistema de gestión de calidad",
                c05 / "gestion-riesgos" / "sgc")
        mv_tree(gr_src / "Software VrCardio",
                c05 / "gestion-riesgos" / "software-vrcardio")
        rm_tree(gr_src)

    # Proveedores
    mv_tree(src / "registros" / "Proveedores", c05 / "proveedores")

    # Retirada de producto
    mv_tree(src / "registros" / "Retirada de producto", c05 / "retirada-de-producto")

    # Validación Software
    mv_tree(src / "registros" / "Validación Software", c05 / "validacion-software")

    # ── 06-evaluacion-desempeno ───────────────────────────────────────────
    c06 = cal / "06-evaluacion-desempeno"

    mv_tree(src / "registros" / "Auditorías", c06 / "auditorias")
    mv_tree(src / "registros" / "Análisis de datos", c06 / "analisis-de-datos")
    mv_tree(src / "registros" / "Gestión de Pnts",
            c06 / "gestion-pnts-registros")  # los cuadernos
    mv_tree(src / "registros" / "Informes revisión por la dirección",
            c06 / "revision-por-la-direccion")
    mv_tree(src / "registros" / "Medición de procesos", c06 / "medicion-procesos")
    mv_tree(src / "registros" / "No conformidades",     c06 / "no-conformidades")

    # ── Limpiar ISO-13845/ ────────────────────────────────────────────────
    rm_empty(src)
    if src.exists():
        rm_tree(src)

    log.info("✓ Calidad migrada")


# ══════════════════════════════════════════════════════════════════════════════
# SEGURIDAD — mueve ISO-27001/ → seguridad-iso27001/
# ══════════════════════════════════════════════════════════════════════════════

def migrate_seguridad(docs: Path):
    src = docs / "ISO-27001"
    seg = docs / "seguridad-iso27001"
    if not src.exists():
        log.info("ISO-27001/ no encontrado, saltando seguridad")
        return

    cnt = src / "Continuidad del negocio"
    doc27 = src / "Documentación ISO 27001"

    # ── 01-contexto-organizacion ──────────────────────────────────────────
    s01 = seg / "01-contexto-organizacion"
    # Políticas de alcance (PLT-002)
    for f in ["plt-00201-alcance-spika-tech.md", "plt-00202-alcance-spika-tech.md"]:
        mv(doc27 / "Políticas" / "USO INTERNO RESTRINGIDO" / f, s01 / f)
    mv(doc27 / "Políticas" / "USO INTERNO RESTRINGIDO" / "Versiones antiguas" /
       "plt-00201-alcance-spika-tech.md",
       s01 / "versiones-historicas" / "plt-00201-alcance-spika-tech.md")

    # ── 02-liderazgo ──────────────────────────────────────────────────────
    s02 = seg / "02-liderazgo"

    # Comité de seguridad
    cs = src / "Comité de seguridad"
    mv(cs / "acta-constitucion-comite-seguridad.md",
       s02 / "comite-de-seguridad" / "acta-constitucion-comite-seguridad.md")
    mv(cs / "acta-de-revision-por-el-comite-de-seguridad.md",
       s02 / "comite-de-seguridad" / "acta-de-revision-por-el-comite-de-seguridad.md")
    mv_tree(cs / "Minutas", s02 / "comite-de-seguridad" / "minutas")
    # Minuta extra en Reuniones
    mv(cnt / "Reuniones" / "2025-03-25" / "minuta-reunion-25-03-2025-planificacion-iso-27001---fase-2.md",
       s02 / "comite-de-seguridad" / "minutas" / "minuta-reunion-25-03-2025-planificacion-iso-27001---fase-2.md")

    # Políticas vigentes
    plt_vigentes = {
        "USO PÚBLICO":            ["plt-00102-seguridad-de-la-informacion-signed.md"],
        "USO INTERNO":            ["plt-00302-liderazgo-y-compromiso.md",
                                   "plt-00401-continuidad-de-negocio.md",
                                   "plt-00501-desconexion-digital.md",
                                   "plt-00601-contrasenas.md"],
    }
    for cls, files in plt_vigentes.items():
        for f in files:
            mv(doc27 / "Políticas" / cls / f, s02 / "politicas" / f)
    # Versiones históricas de políticas
    for cls in ["USO INTERNO", "USO INTERNO RESTRINGIDO", "USO PÚBLICO"]:
        va = doc27 / "Políticas" / cls / "Versiones antiguas"
        if va.exists():
            for f in va.glob("*.md"):
                mv(f, s02 / "politicas" / "versiones-historicas" / f.name)

    # Puestos de trabajo: RPTs completos de Gestión del personal
    rpt_src = cnt / "Gestión del personal" / "Estructura del personal" / "RPT"
    mv_tree(rpt_src, s02 / "puestos-de-trabajo" / "asignaciones")

    # ── 03-planificacion ──────────────────────────────────────────────────
    s03 = seg / "03-planificacion"
    aarr = src / "Análisis de riesgos"
    if aarr.exists():
        mv(aarr / "adr-00201-plan-de-tratamiento-de-riesgos.md",
           s03 / "analisis-de-riesgos" / "adr-00201-plan-de-tratamiento-de-riesgos.md")
        mv(aarr / "adr-00201-anexo-a-plan-de-tratamiento-de-riesgos-2024.md",
           s03 / "analisis-de-riesgos" / "adr-00201-anexo-a-plan-de-tratamiento-de-riesgos-2024.md")
        mv_tree(aarr / "Análisis de riesgos de componentes de Spika Tech",
                s03 / "analisis-de-riesgos" / "componentes")
        mv_tree(aarr / "Versiones antiguas",
                s03 / "analisis-de-riesgos" / "versiones-historicas")
        rm_tree(aarr)

    # ── 04-soporte ────────────────────────────────────────────────────────
    s04 = seg / "04-soporte"

    # Normas
    for cls in ["USO INTERNO", "USO INTERNO RESTRINGIDO"]:
        d = doc27 / "Normas" / cls
        if d.exists():
            for f in d.glob("*.md"):
                mv(f, s04 / "normas" / f.name)

    # Transversales
    mv_tree(doc27 / "Transversales" / "USO INTERNO", s04 / "transversales")

    # Formación / concienciación
    mv_tree(src / "Formación" / "Documentos" / "USO INTERNO", s04 / "formacion" / "documentos")

    # Registros de formación (por personas, CCN/CEA/PMI)
    rep_form = cnt / "Gestión del personal" / "Reporte formación"
    if rep_form.exists():
        mv_tree(rep_form, s04 / "formacion" / "certificados")

    # NDAs y configuración segura
    cfg = src / "Configuración segura"
    if cfg.exists():
        # Guía general
        mv(cfg / "ccn-cert-bp-06-navegadores-web.md",
           s04 / "configuracion-segura" / "ccn-cert-bp-06-navegadores-web.md")
        # Subcarpetas de herramientas
        app_map = {
            "Google Chrome":       "google-chrome",
            "Microsoft Edge":      "microsoft-edge",
            "Microsoft Office 365":"microsoft-office-365",
            "Microsoft OneDrive":  "microsoft-onedrive",
            "Microsoft Outlook":   "microsoft-outlook",
            "Microsoft Sharepoint":"microsoft-sharepoint",
            "Microsoft Teams":     "microsoft-teams",
            "Norton 360":          "norton-360",
        }
        for old, new in app_map.items():
            mv_tree(cfg / old, s04 / "configuracion-segura" / new)
        # Turnos: guía + NDAs
        turnos = cfg / "Turnos"
        if turnos.exists():
            mv(turnos / "guia-de-instalacion-y-uso-de-turnos.md",
               s04 / "configuracion-segura" / "turnos" / "guia-de-instalacion-y-uso-de-turnos.md")
            mv_tree(turnos / "NDA", s04 / "nda")
            # Norma 1 (nombres truncados FAT32) → transversal/basura
            mv_tree(turnos / "Norma 1", seg / "transversal" / "norma1-fat32")
            rm_tree(turnos)
        rm_tree(cfg)

    # ── 05-operacion ──────────────────────────────────────────────────────
    s05 = seg / "05-operacion"

    # Procedimientos (vigentes y versiones históricas)
    for cls in ["USO INTERNO", "USO INTERNO RESTRINGIDO"]:
        d = doc27 / "Procedimientos" / cls
        if d.exists():
            for f in d.glob("*.md"):
                mv(f, s05 / "procedimientos" / f.name)
            va = d / "Versiones antiguas"
            if va.exists():
                for f in va.glob("*.md"):
                    mv(f, s05 / "procedimientos" / "versiones-historicas" / f.name)

    # Continuidad del negocio
    mv_tree(cnt / "Protocolos", s05 / "continuidad-del-negocio" / "protocolos")
    mv_tree(cnt / "BIAs",       s05 / "continuidad-del-negocio" / "bias")

    # Seguridad del desarrollo
    sdev = cnt / "Seguridad del desarrollo"
    if sdev.exists():
        aud = sdev / "Auditoría de código"
        if aud.exists():
            for f in aud.glob("*.md"):
                mv(f, s05 / "seguridad-del-desarrollo" / "auditoria-de-codigo" / f.name)
            mv_tree(aud / "Reportes Code Checker",
                    s05 / "seguridad-del-desarrollo" / "auditoria-de-codigo" / "reportes")
            rm_tree(aud)
        pent = sdev / "Pentesting"
        if pent.exists():
            for f in pent.glob("*.md"):
                mv(f, s05 / "seguridad-del-desarrollo" / "pentesting" / f.name)
            mv_tree(pent / "2025-04-15",
                    s05 / "seguridad-del-desarrollo" / "pentesting" / "2025-04-15")
            mv_tree(pent / "2025-06-27",
                    s05 / "seguridad-del-desarrollo" / "pentesting" / "2025-06-27")
            rm_tree(pent)
        mv(sdev / "security-assessment-report.md",
           seg / "anexos" / "security-assessment-report.md")
        rm_tree(sdev)

    # Inteligencia de amenazas
    mv_tree(src / "Inteligencia de amenazas", s05 / "inteligencia-de-amenazas")

    # Protección de proyectos IT
    proy = cnt / "Protección de proyectos IT"
    if proy.exists():
        cls_proy = proy / "Clausula de protección de proyectos IT"
        if cls_proy.exists():
            for f in cls_proy.glob("*.md"):
                mv(f, s05 / "proteccion-proyectos-it" / f.name)
            rm_tree(cls_proy)
        sla = proy / "SLA"
        if sla.exists():
            for f in sla.glob("*.md"):
                mv(f, s05 / "proteccion-proyectos-it" / f.name)
            rm_tree(sla)
        rm_tree(proy)

    # Proveedores ISO 27001 (evaluaciones en registros de calidad/06)
    # No hay subcarpeta Proveedores en ISO-27001; los de calidad ya se migraron.

    # ── 06-evaluacion-desempeno ───────────────────────────────────────────
    s06 = seg / "06-evaluacion-desempeno"

    # Auditoría AENOR externa
    aenor = cnt / "Auditorías" / "Externa" / "AENOR - Marzo 2025"
    if aenor.exists():
        mv_tree(aenor / "Fase 1", s06 / "auditoria-aenor-2025" / "fase-1")
        mv_tree(aenor / "Fase 2", s06 / "auditoria-aenor-2025" / "fase-2")
        pac = aenor / "PAC"
        if pac.exists():
            mv(pac / "plan-de-acciones-correctivas-iso-27001.md",
               s06 / "auditoria-aenor-2025" / "pac" / "plan-de-acciones-correctivas-iso-27001.md")
            mv(pac / "informe-fase-2-de-certificacion-iso27001-spikatech.md",
               s06 / "auditoria-aenor-2025" / "pac" / "informe-fase-2-de-certificacion-iso27001-spikatech.md")
            inner_pac = pac / "PAC"
            if inner_pac.exists():
                for f in inner_pac.glob("*.md"):
                    mv(f, s06 / "auditoria-aenor-2025" / "pac" / f.name)
                for anexo in inner_pac.iterdir():
                    if anexo.is_dir():
                        mv_tree(anexo, s06 / "auditoria-aenor-2025" / "pac" / anexo.name)
                rm_tree(inner_pac)
            rm_tree(pac)
        rec = aenor / "Recursos necesarios" / "Reporte auditoría interna"
        if rec.exists():
            for f in rec.glob("*.md"):
                mv(f, s06 / "auditoria-interna-cyberxia-2025" / f.name)
            rm_tree(aenor / "Recursos necesarios")
        rm_tree(aenor)

    # Auditoría interna Cyberxia
    cyb = cnt / "Auditorías" / "Interna" / "2025 - Marzo (Cyberxia)"
    if cyb.exists():
        for f in cyb.glob("*.md"):
            mv(f, s06 / "auditoria-interna-cyberxia-2025" / f.name)
        rm_tree(cyb)
    mv(cnt / "Auditorías" / "plan-de-acciones-correctivas-iso27001.md",
       s06 / "auditoria-aenor-2025" / "pac" / "plan-de-acciones-correctivas-iso27001.md")

    # Control de documentos
    mv_tree(doc27 / "Control de documentos y evidencias", s06 / "control-documentos")

    # Registros RGS
    rgs_int = doc27 / "Registros" / "USO INTERNO"
    if rgs_int.exists():
        for f in rgs_int.glob("*.md"):
            mv(f, s06 / "registros" / f.name)
        mv_tree(rgs_int / "NORMATIVA APLICABLE", s06 / "registros" / "normativa-aplicable")
    rgs_rest = doc27 / "Registros" / "USO INTERNO RESTRINGIDO"
    if rgs_rest.exists():
        for f in rgs_rest.glob("*.md"):
            mv(f, s06 / "registros" / f.name)

    # Informes revisión por la dirección
    mv_tree(cnt / "Gestión del personal" / "Reporte formación" / "..",
            s06 / "transversal-personal")  # ya movido arriba; no hacer nada más aquí

    # Medición de procesos: están en calidad-iso13485 (son de ambas normas)
    # No hay en ISO-27001/ directamente.

    # ── 07-mejora ─────────────────────────────────────────────────────────
    s07 = seg / "07-mejora"
    plan_cap = cnt / "Planificaciones" / "Plan de capacidad"
    if plan_cap.exists():
        mv_tree(plan_cap, s07 / "plan-de-capacidad")
    mv(cnt / "Planificaciones" / "formacion-y-concienciacion.md",
       s07 / "planificaciones" / "formacion-y-concienciacion.md")
    mv(cnt / "Planificaciones" / "gastos.md",
       s07 / "planificaciones" / "gastos.md")
    mv(cnt / "Planificaciones" / "planificacion-recursos.md",
       s07 / "planificaciones" / "planificacion-recursos.md")

    # ── Transversal ───────────────────────────────────────────────────────
    tv = seg / "transversal"
    mv(cnt / "Gestión del personal" / "matriz-de-segregacion-de-funciones.md",
       tv / "matriz-de-segregacion-de-funciones.md")
    mv(cnt / "Gestión del personal" / "reporte-de-tareas.md",
       tv / "reporte-de-tareas.md")
    mv(cnt / "Gestión del personal" / "Plan de revisiones" / "plan-de-revision-de-dispositivos.md",
       tv / "plan-de-revision-de-dispositivos.md")
    mv_tree(cnt / "Medio ambiente", tv / "medio-ambiente")
    mv(src / "-all-errors.md",  tv / "-all-errors.md")
    mv_tree(src / "__Continuidad del negocio", tv / "basura")
    mv_tree(src / "WORDS", tv / "words-fuentes")

    # ── Limpiar ISO-27001/ ────────────────────────────────────────────────
    rm_empty(src)
    if src.exists():
        rm_tree(src)

    log.info("✓ Seguridad migrada")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    if not DOCS.exists():
        log.error("No se encuentra docs/. Ejecuta desde la raíz del proyecto.")
        return

    log.info("═" * 60)
    log.info("  reorganizar_final.py — INICIO")
    log.info("═" * 60)

    migrate_calidad(DOCS)
    migrate_seguridad(DOCS)

    log.info("── Limpieza de directorios vacíos ──")
    rm_empty(DOCS)

    log.info("═" * 60)
    log.info("  FIN — revisa reorganizar_final.log")
    log.info("═" * 60)


if __name__ == "__main__":
    main()
