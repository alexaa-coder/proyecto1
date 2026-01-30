# Portal de Cumplimiento Normativo

Portal web para la gestión y visualización de documentación normativa **ISO-13485** (Calidad en Productos Sanitarios) e **ISO-27001** (Seguridad de la Información).

**Estado del proyecto:**  
✅ Semanas 1 y 2 completadas (estructura base y contenedorización).

---

## Descripción

El proyecto establece la **infraestructura técnica inicial** para un portal de documentación normativa, utilizando un generador estático moderno y contenedores Docker, dejando el entorno listo para la futura migración de contenido.

---

## Tecnologías Utilizadas

- **Docusaurus** – Generador de documentación
- **Node.js 20 LTS** – Entorno de build
- **Docker & Docker Compose** – Contenedorización
- **Nginx (Alpine)** – Servidor web
- **Git** – Control de versiones
- **Markdown** – Documentación

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
