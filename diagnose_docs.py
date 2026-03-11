"""
diagnose_docs.py
Analiza todos los .md en tu carpeta de docs convertidos y reporta
los patrones problemáticos encontrados: {{}}, índices residuales, tablas rotas, etc.

Uso:
    python3 diagnose_docs.py docs/
"""
import re
import sys
from pathlib import Path
from collections import defaultdict

# ── Colores ANSI ──────────────────────────────────────────────────────────────
R = '\033[91m'; Y = '\033[93m'; G = '\033[92m'; C = '\033[96m'; RESET = '\033[0m'

# ── Patrones a buscar ─────────────────────────────────────────────────────────
CHECKS = [
    ("pf-cargo / Word fields",   re.compile(r'\{\{pf-[^}]+\}\}|&#123;&#123;pf-'), "❌"),
    ("Llaves huérfanas MDX",     re.compile(r'(?<!\{)\{(?!\{)(?!textAlign)[^}\n]{0,60}(?<!\})\}(?!\})'), "⚠️"),
    ("Título de índice",         re.compile(r'(?m)^#+\s*(Índice|ÍNDICE|CONTENIDO|Tabla de contenidos?)'), "⚠️"),
    ("Índice con puntitos",      re.compile(r'\.{4,}\s*(?:\d+|[ivx]+)\s*$', re.M), "⚠️"),
    ("Líneas negrita sola (TOC)",re.compile(r'(?m)^\*\*\d+(?:\.\d+)*\*\* \*\*[^\*\n]+\*\*\s*$'), "⚠️"),
    ("Tablas rotas (sin |sep|)", re.compile(r'(?m)^\|[^\-][^\n]*\n(?!\|[\-:])'), "❌"),
    ("Imágenes duplicadas",      None, "🔍"),   # Requiere análisis especial
    ("No puede enseñar tabla",   re.compile(r'No se puede enseñar la tabla'), "ℹ️"),
    ("Firma de Word restante",   re.compile(r'Firmado por|DIGITAL SIGN|Fdo\..*\n.*Fdo\.'), "ℹ️"),
]

def check_duplicate_images(text: str) -> list[str]:
    """Detecta imágenes que aparecen más de una vez con distinta ruta."""
    imgs = re.findall(r'!\[[^\]]*\]\((/img/[^\)]+)\)', text)
    names = [Path(p).name for p in imgs]
    seen, dupes = set(), []
    for n in names:
        if n in seen:
            dupes.append(n)
        seen.add(n)
    return dupes

def analyze_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    results = {}
    for label, pattern, icon in CHECKS:
        if pattern is None:
            dupes = check_duplicate_images(text)
            results[label] = (icon, dupes)
        else:
            matches = pattern.findall(text)
            results[label] = (icon, matches)
    return results

def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("docs")
    files = sorted(folder.rglob("*.md"))
    
    if not files:
        print(f"{R}No se encontraron archivos .md en '{folder}'{RESET}")
        return
    
    print(f"\n{C}{'='*80}")
    print(f"  DIAGNÓSTICO DE DOCUMENTOS CONVERTIDOS — {len(files)} archivos")
    print(f"{'='*80}{RESET}\n")
    
    summary = defaultdict(int)
    
    for path in files:
        results = analyze_file(path)
        has_issues = any(matches for _, matches in results.values())
        
        if not has_issues:
            print(f"{G}✔  {path.name}{RESET}")
            continue
        
        print(f"\n{Y}{'─'*80}")
        print(f"  📄 {path.name}")
        print(f"{'─'*80}{RESET}")
        
        for label, (icon, matches) in results.items():
            if not matches:
                continue
            summary[label] += len(matches)
            print(f"  {icon} {label}: {R}{len(matches)} ocurrencia(s){RESET}")
            for m in matches[:3]:  # Mostrar máximo 3 ejemplos por tipo
                preview = str(m).strip()[:100]
                print(f"       · {Y}{preview}{RESET}")
            if len(matches) > 3:
                print(f"       ... y {len(matches)-3} más")
    
    print(f"\n{C}{'='*80}")
    print(f"  RESUMEN GLOBAL")
    print(f"{'='*80}{RESET}")
    if summary:
        for label, count in sorted(summary.items(), key=lambda x: -x[1]):
            print(f"  {count:5d}  ·  {label}")
    else:
        print(f"  {G}✔  ¡No se encontraron problemas en ningún documento!{RESET}")
    print()

if __name__ == "__main__":
    main()
