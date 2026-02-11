# Portal de Cumplimiento Normativo

Plataforma centralizada para la gestión y visualización de documentación normativa **ISO-13485** (Calidad en Productos Sanitarios) e **ISO-27001** (Seguridad de la Información).

---

## Estado del Proyecto

* **Semana 1-2**: Configuración del entorno inicial y contenedorización
  * Configuración del entorno local
  * Contenedorización con Docker (multi-stage build)
  * Servidor Nginx
* **Semana 4**: Arquitectura de la información y estructura normativa
  * Definición de la arquitectura de la información
  * Separación estructural entre ISO-13485 e ISO-27001
  * Diseño semántico optimizado para indexación por IA

---

## Descripción

El proyecto establece la **infraestructura técnica inicial** para un portal de documentación normativa, utilizando un generador estático moderno y contenedores Docker, dejando el entorno listo para la futura migración de contenido y gestión semántica.

---

## Tecnologías Utilizadas

- **Docusaurus v3** – Generador de documentación
<<<<<<< HEAD
- **Node.js 24 LTS** – Entorno de build
=======
- **Node.js 20 LTS** – Entorno de build
>>>>>>> 05742ec (semana 4, primera version)
- **Docker & Docker Compose** – Contenedorización
- **Nginx (Alpine)** – Servidor web
- **Git** – Control de versiones
- **Markdown** – Documentación editable

---

## Puesta en Marcha

### Requisitos
- Docker 20.10+
- Docker Compose v2
- Git

### Ejecución
```bash
git clone https://github.com/aleexa-coder/documentacion-proyecto1.git
cd documentacion-proyecto1
docker-compose up -d

