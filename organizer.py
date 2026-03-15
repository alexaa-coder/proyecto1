import os
import re
import shutil
from pathlib import Path
from typing import Optional, List

# --- CONFIGURATION ---
DOCS_ROOT = Path("docs")
ISO_13485_ROOT = DOCS_ROOT / "calidad-iso13485"
ISO_27001_ROOT = DOCS_ROOT / "seguridad-iso27001"

# Target branches to ignore during initial scan
TARGET_BRANCHES = {ISO_13485_ROOT.name, ISO_27001_ROOT.name}

# Mapping: (Target Subfolder, Pattern List)
ISO_13485_MAP = [
    ("01-contexto-organizacion", [r"mq-01-0[3-8]", r"licencia", r"pnt-011", r"manual-de-calidad"]),
    ("02-liderazgo", [r"compromiso-de-calidad"]),
    ("03-planificacion", [r"pnt-002", r"pnt-029", r"objetivos-de-calidad"]),
    ("04-soporte", [r"pnt-001", r"pnt-003", r"pnt-022", r"pnt-027"]),
    ("05-operacion", [r"esp-00[56]", r"pnt-012", r"pnt-020", r"pnt-015", r"pnt-026"]),
    ("06-evaluacion-desempeno", [r"pnt-013", r"pnt-010", r"pnt-009"]),
    ("07-mejora", [r"pnt-004", r"pnt-006", r"pnt-005"]),
    ("anexos", [r"certificado-iso", r"registro-de-distribucion", r"mapa-de-proceso"])
]

ISO_27001_MAP = [
    ("01-contexto-organizacion", [r"plt-002", r"pro-002"]),
    ("02-liderazgo", [r"plt-001", r"plt-003", r"politica-de-seguridad"]),
    ("03-planificacion", [r"pro-005", r"adr-00[12]"]),
    ("04-soporte", [r"pro-003", r"for-001", r"nda"]),
    ("05-operacion", [r"nrm-00[1-5]", r"pro-006", r"pro-013", r"pentesting"]),
    ("06-evaluacion-desempeno", [r"pro-017", r"auditoria-interna", r"auditoria-externa"]),
    ("07-mejora", [r"pro-015", r"pac", r"plan-de-acciones-correctivas"]),
    ("anexos", [r"guia-de-configuracion", r"microsoft-365", r"teams", r"norton", r"concienciacion"])
]

# Broad prefixes for catch-all classification
CALIDAD_PREFIXES = r"(mq|pnt|esp|calidad)"
SEGURIDAD_PREFIXES = r"(plt|pro|adr|for|nrm|nda|seguridad|nda|pentesting)"

def get_target_path(item: Path) -> Optional[Path]:
    """Determines the target path for a file based on its name."""
    name = item.name.lower()
    
    # Check ISO 13485 specific mapping
    for subfolder, patterns in ISO_13485_MAP:
        if any(re.search(p, name) for p in patterns):
            return ISO_13485_ROOT / subfolder
            
    # Check ISO 27001 specific mapping
    for subfolder, patterns in ISO_27001_MAP:
        if any(re.search(p, name) for p in patterns):
            return ISO_27001_ROOT / subfolder

    # Broad catch-all classification
    if re.search(CALIDAD_PREFIXES, name):
        return ISO_13485_ROOT
    if re.search(SEGURIDAD_PREFIXES, name):
        return ISO_27001_ROOT
        
    return None

def organize_recursive(source_dir: Path):
    """Recursively moves files and subdirectories to their target ISO locations."""
    for item in list(source_dir.iterdir()):
        # Skip target branches and system files
        if item.name in TARGET_BRANCHES or item.name == "intro.md" or item.name.startswith("."):
            continue
            
        if item.is_file():
            target_dir = get_target_path(item)
            if target_dir:
                target_dir.mkdir(parents=True, exist_ok=True)
                dest = target_dir / item.name
                shutil.move(str(item), str(dest))
                print(f"Moved File: {item.name} -> {target_dir.relative_to(DOCS_ROOT)}")
            else:
                print(f"Skipped File: {item.name} (No category match)")
                
        elif item.is_dir():
            # Strategy: see if the whole directory matches a category
            # We check the directory name first
            target_dir = get_target_path(item)
            if target_dir:
                # Move the entire directory
                target_dir.mkdir(parents=True, exist_ok=True)
                dest = target_dir / item.name
                if dest.exists():
                    # Merge if exists
                    for sub_item in item.iterdir():
                        shutil.move(str(sub_item), str(dest / sub_item.name))
                    item.rmdir()
                else:
                    target_dir.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(item), str(dest))
                print(f"Moved Directory: {item.name}/ -> {target_dir.relative_to(DOCS_ROOT)}")
            else:
                # Recurse into the directory to find individual matches
                organize_recursive(item)
                # If directory became empty, remove it
                if not any(item.iterdir()):
                    item.rmdir()

def main():
    print("--- Starting Intelligent Recursive Organization ---")
    if not DOCS_ROOT.exists():
        print(f"Error: {DOCS_ROOT} current directory not found.")
        return
        
    organize_recursive(DOCS_ROOT)
    print("--- Organization Finished ---")

if __name__ == "__main__":
    main()
