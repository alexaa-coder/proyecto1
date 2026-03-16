# Portal de Cumplimiento Normativo
Plataforma centralizada para la gestión, migración y visualización de documentación normativa **ISO-13485** (Calidad en Productos Sanitarios) e **ISO-27001** (Seguridad de la Información).
El proyecto evoluciona desde una infraestructura base hacia una migración inteligente asistida por IA, orientada a estructuración semántica y futura optimización para búsquedas avanzadas.

---

## Estado del Proyecto

### ✅ Semana 1–2: Infraestructura Base
- Configuración del entorno local
- Contenedorización con Docker (multi-stage build)
- Configuración de Nginx
- Integración con Docusaurus v3

### ✅ Semana 4: Arquitectura de la Información
- Definición de estructura normativa
- Separación estructural ISO-13485 / ISO-27001
- Diseño de arquitectura optimizada para escalabilidad documental

### ✅ Semana 5–6: Pipeline de Conversión y Migración Documental

#### Investigación y selección de herramientas
- Evaluación y descarte de Pandoc (no acepta PDF), pdfplumber (sin jerarquía) y marker-pdf (demasiado pesado para VM)
- Selección de **pymupdf4llm** como librería principal de conversión
- Configuración del entorno virtual Python (`python3.12-venv`)
- Evaluación de Google NotebookLM: descartado para el procesamiento masivo por volumen y por implicaciones de seguridad al tratar documentación sensible ISO 27001

#### Procesamiento
- Desarrollo iterativo del script de conversión (más de 10 versiones probadas)
- Pruebas sobre 5 PDFs representativos de diferentes tipologías (tablas, imágenes, índices, firmas electrónicas, marcas de agua)
- Presentación al tutor y ajustes según sus recomendaciones

#### Transformación
- Pipeline modular Python con separación de responsabilidades:
  - `conversor.py` — detección de tipo de archivo y orquestación
  - `cleaner_images.py` — extracción y referenciado de imágenes a `static/img/`
  - `cleaner_tables.py` — detección y reconstrucción de tablas rotas
  - `cleaner_toc.py` — eliminación de índices duplicados y corrección MDX
- Conversión masiva de documentos: PDF, DOCX, XLSX, PPTX, PNG
- Script `limpiar_imagenes.py` para mantenimiento de imágenes huérfanas en `static/img/`

#### Validación
- Revisión manual del Markdown generado
- Corrección de:
  - Errores de compilación MDX (`<br>` → `<br />`, caracteres `<`, `>`, `{`, `}`)
  - Tablas mal formateadas
  - HTML incompatible
  - Jerarquías incorrectas de encabezados
- Script `reorganizar_final.py` para migración de documentos a la estructura de Docusaurus
- Integración progresiva en Docusaurus
- Control de versiones mediante Git (commits de scripts, `.gitignore` para `/venv`, README)

### ✅ Semana 7: Metadatos (Frontmatter) — Optimización para IA
- Desarrollo de `add_frontmatter.py`: recorre todos los `.md` de `docs/` e inyecta automáticamente frontmatter YAML
- Campos inferidos del path: `title`, `sidebar_label`, `responsable`, `clasificacion`, `fecha_revision`, `idioma`, `tags`
- Resultado: **642 archivos** con frontmatter añadido, **68 excluidos** (basura, fuentes duplicadas, archivos corruptos)

```yaml
---
title: "Título del documento"
sidebar_label: "Título"
responsable: "Responsable del SGSI"
clasificacion: "USO INTERNO"
fecha_revision: "2025-03-16"
idioma: "es"
tags:
  - iso-27001
  - operacion
  - procedimiento
---
```

---

## Descripción Técnica
El proyecto establece una infraestructura moderna de documentación normativa basada en:
- Generador estático (Docusaurus)
- Migración asistida por IA
- Estructuración Markdown limpia y validada
- Contenedorización reproducible
- Versionado y control de cambios

El objetivo es transformar documentación normativa tradicional en un portal navegable, estructurado y preparado para futuras mejoras semánticas.

---

## Flujo de Migración Actual

1. Documento normativo original (PDF, DOCX, XLSX, PPTX, PNG)
2. Conversión automática con `conversor.py` + módulos `cleaner_*.py`
3. Reorganización en estructura Docusaurus con `reorganizar_final.py`
4. Adición de metadatos con `add_frontmatter.py`
5. Validación manual y corrección de errores MDX
6. Integración en Docusaurus
7. Versionado con Git

---

## Tecnologías Utilizadas
- **Docusaurus v3** – Generador de documentación estática
- **Node.js 24 LTS** – Entorno de build
- **Docker & Docker Compose** – Contenedorización
- **Nginx (Alpine)** – Servidor web
- **Git** – Control de versiones
- **Markdown / MDX** – Documentación estructurada
- **Python 3.12** – Pipeline de conversión y migración
- **pymupdf4llm** – Conversión de PDF a Markdown estructurado
- **Google NotebookLM** – Evaluado durante la fase de investigación

---

## Puesta en Marcha

### Requisitos
- Docker 20.10+
- Docker Compose v2
- Git

### Clonar el repositorio
```bash
git clone https://github.com/alexaa-coder/proyecto1.git
cd proyecto1
```
