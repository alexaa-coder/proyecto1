# Portal de Cumplimiento Normativo — VRCardio

Plataforma centralizada y segura para alojar la normativa **ISO 13485** (Calidad en Productos Sanitarios) e **ISO 27001** (Seguridad de la Información). El sistema permite el versionado de documentos mediante Git y está estructurado semánticamente para que agentes de IA puedan indexarlo y consultarlo de forma autónoma.

Construido con [Docusaurus 3.9.2](https://docusaurus.io/), contenedorizado con Docker y servido mediante Nginx. Incluye motor de búsqueda local (`docusaurus-lunr-search`) sin dependencias externas, y una prueba de concepto de consulta IA sobre la normativa con Ollama.

---

## Requisitos previos

| Componente | Versión mínima | Versión recomendada | Notas |
|-----------|---------------|-------------------|-------|
| Docker | 20.x | última estable | Incluye Docker Compose v2 |
| Docker Compose | v1 o v2 | v2 | El `docker-compose.yml` es compatible con ambas versiones |
| Node.js | 20.x | 22.x o 24.x (LTS activo) | Solo necesario para desarrollo local sin Docker |
| Git | cualquiera | última estable | |

> **Nota sobre Node.js:** La versión mínima es 20 por compatibilidad con Docusaurus 3.x. Se recomienda usar la 22 o la 24, ya que son las versiones LTS con soporte activo a largo plazo. La versión 20 recibe soporte de mantenimiento pero dejará de recibirlo antes.

---

## Despliegue rápido con Docker

Esta es la forma recomendada. Funciona igual en Linux, Windows y macOS.

### Linux

```bash
git clone https://github.com/alexaa-coder/proyecto1.git
cd proyecto1
docker compose up -d --build
```

### Windows

Requiere [Docker Desktop para Windows](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.

```powershell
git clone https://github.com/alexaa-coder/proyecto1.git
cd proyecto1
docker compose up -d --build
```

> Si usas Docker Compose v1 (comando separado `docker-compose`):
> ```powershell
> docker-compose up -d --build
> ```

### macOS

Requiere [Docker Desktop para Mac](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.

```bash
git clone https://github.com/alexaa-coder/proyecto1.git
cd proyecto1
docker compose up -d --build
```

---

Una vez levantado, el portal estará disponible en:

```
http://localhost:8080
```

---

## Desarrollo local sin Docker

Solo necesario si quieres editar el contenido y ver los cambios en tiempo real.

### Requisitos

- Node.js 20 o superior (recomendado 22 o 24)

### Linux / macOS

```bash
git clone https://github.com/alexaa-coder/proyecto1.git
cd proyecto1
npm install
npm start
```

El servidor de desarrollo arranca en `http://localhost:3000` con hot reload.

### Windows

```powershell
git clone https://github.com/alexaa-coder/proyecto1.git
cd proyecto1
npm install
npm start
```

> **Aviso:** El motor de búsqueda (`docusaurus-lunr-search`) solo funciona en el build de producción, no en `npm start`. Para probar la búsqueda, usa el despliegue con Docker.

---

## Estructura del proyecto

```
documentacion-proyecto1/
├── docs/
│   ├── calidad-iso13485/        # Normativa ISO 13485 por cláusulas
│   │   ├── 00-introduccion.md
│   │   ├── 01-contexto-organizacion/
│   │   ├── 05-operacion/
│   │   └── ...
│   ├── seguridad-iso27001/      # Normativa ISO 27001 por cláusulas
│   │   ├── 00-introduccion.md
│   │   ├── 04-soporte/
│   │   ├── anexoA-controles/
│   │   └── ...
│   └── manual-operaciones.md
├── static/
│   └── documentos-oficiales/    # PDFs originales
│       ├── iso13485/
│       └── iso27001/
├── scripts/
│   ├── actualizar.sh            # Reconstruye y reinicia el contenedor
│   └── backup.sh                # Genera backup comprimido de la documentación
├── Dockerfile                   # Build multietapa: Node (build) + Nginx (serve)
├── docker-compose.yml
├── nginx.conf
├── docusaurus.config.js
├── sidebars.js
└── poc_ia_normativa.py          # Prueba de concepto IA con Ollama
```

---

## Scripts de mantenimiento

Desde la raíz del proyecto:

```bash
# Reconstruir y reiniciar el contenedor tras modificar documentación
./scripts/actualizar.sh

# Crear backup comprimido de docs/ y configuración
./scripts/backup.sh
```

Los backups se guardan en `scripts/backups/` y se conservan los últimos 5 automáticamente. Los logs de cada operación se guardan en `scripts/logs/`.

---

## Añadir nueva documentación

```bash
# 1. Activar el entorno virtual Python
source venv/bin/activate

# 2. Convertir el documento
python conversor.py /ruta/al/documento.pdf

# 3. Mover al lugar correcto dentro de docs/
mv docs/transversal/documento.md docs/calidad-iso13485/05-operacion/

# 4. Regenerar frontmatter si es necesario
python add_frontmatter.py

# 5. Reconstruir el contenedor
./scripts/actualizar.sh
```

---

## Prueba de concepto IA

El repositorio incluye `poc_ia_normativa.py`, un script que carga el contenido del repositorio como contexto y lanza consultas en lenguaje natural sobre la normativa usando [Ollama](https://ollama.com/) con el modelo `llama3.2`. Todo el procesamiento es local, sin enviar datos a servicios externos.

```bash
# Requisitos: Ollama instalado y modelo descargado
ollama pull llama3.2

# Ejecutar
source venv/bin/activate
python poc_ia_normativa.py
```

---

## Decisiones técnicas relevantes

**Motor de búsqueda local en lugar de Algolia:** Algolia requiere enviar el contenido a indexar a servidores externos. Para un portal con documentación normativa confidencial, eso es incompatible con los controles de la ISO 27001. `docusaurus-lunr-search` genera el índice en tiempo de build y lo sirve como archivo estático junto al resto del sitio.

**Ollama en lugar de APIs externas:** Por el mismo motivo, la prueba de concepto de IA usa un modelo local. Ningún documento normativo sale de la máquina.

**Docker Compose compatible con v1 y v2:** El `docker-compose.yml` incluye el campo `version` para mantener compatibilidad con instalaciones que usen la versión 1 del comando. Docker Compose v2 lo ignora con un warning que puede descartarse.

**Node.js 20 como mínimo:** Docusaurus 3.x requiere Node 18 como mínimo absoluto, pero la versión 20 es la primera que garantiza compatibilidad con todas las dependencias del proyecto. Se recomienda 22 o 24 (LTS activo).

---

## Tecnologías utilizadas

| Componente | Versión | Función |
|-----------|---------|---------|
| Docusaurus | 3.9.2 | Generador del sitio estático |
| Node.js | 20+ (recomendado 22/24) | Runtime de build |
| Nginx | Alpine | Servidor web en producción |
| Docker | — | Contenedorización |
| docusaurus-lunr-search | — | Motor de búsqueda local |
| pymupdf4llm | — | Conversión PDF/DOCX a Markdown |
| Ollama + llama3.2 | — | Consulta IA local sobre normativa |

---

## Autora

**Daniela Diguay** — Alumna de 2º ASIR  
Proyecto de prácticas en Spika Tech
