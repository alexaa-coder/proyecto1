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

### 🔄 Semana 5–6: Migración Asistida con IA (Fase Actual)

#### Procesamiento
- Carga de PDFs normativos actuales en Google NotebookLM
- Preparación de documentos para conversión estructurada

#### Transformación
- Utilización de prompts técnicos para convertir la redacción normativa a Markdown limpio
- Eliminación de artefactos de formato provenientes del PDF
- Reconstrucción manual de tablas cuando es necesario
- Adaptación del contenido para compatibilidad con MDX (Docusaurus)

#### Validación (En Progreso)
- Revisión manual del Markdown generado
- Corrección de:
  - Errores de compilación MDX
  - Tablas mal formateadas
  - HTML incompatible
  - Jerarquías incorrectas de encabezados
- Integración progresiva en Docusaurus
- Control de versiones mediante Git

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

1. Documento normativo original (PDF)
2. Procesamiento en NotebookLM
3. Conversión asistida a Markdown
4. Limpieza técnica del formato
5. Validación manual
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
- **Google NotebookLM** – Migración asistida con IA

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
