# 📚 Portal de Cumplimiento Normativo

Plataforma centralizada para gestionar documentación normativa **ISO-13485** (Calidad en Productos Sanitarios) e **ISO-27001** (Seguridad de la Información).

**Estado:** Semanas 1-2 completadas. Infraestructura lista para migración de contenido.

---

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Tecnologías](#-tecnologías)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación-y-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Comandos Útiles](#-comandos-útiles)
- [Mejoras Implementadas](#-mejoras-implementadas)
- [Semanas de Desarrollo](#-semanas-de-desarrollo)
- [Troubleshooting](#-troubleshooting)
- [Notas Técnicas](#-notas-técnicas)

---

## 📖 Descripción

Este proyecto crea un **portal web moderno** de documentación normativa usando tecnologías de **contenedorización** y **automatización**.

### Objetivos

✅ **Centralizar:** Normativa ISO-13485 e ISO-27001 en un único portal
✅ **Estructurar:** Documentación semánticamente organizada
✅ **Facilitar:** Consulta rápida y búsqueda integrada
✅ **Mantener:** Versionado con Git para control de cambios
✅ **Desplegar:** Infraestructura reproducible con Docker

---

## 🛠️ Tecnologías

| Tecnología | Versión | Propósito |
|-----------|---------|----------|
| **Docusaurus** | 2.x | Generador de documentación (React) |
| **Node.js** | 20 LTS | Runtime para build |
| **Nginx** | Alpine | Servidor web (multi-stage build) |
| **Docker** | 20.10+ | Conteinerización |
| **Docker Compose** | v2 | Orquestación |
| **Git** | 2.x | Control de versiones |
| **Markdown** | CommonMark | Formato de documentación |

---

## 📦 Requisitos

### Para ejecutar localmente
```
✓ Docker Engine 20.10+
✓ Docker Compose v2 (recomendado) o v1.29+
✓ Git 2.x
✓ Navegador moderno (Chrome, Firefox, Edge)
```

**NO necesitas:**
- ❌ Node.js local (está en el contenedor)
- ❌ npm local (está en el contenedor)
- ❌ Nginx local (está en el contenedor)

### Configuración Inicial

Agregar tu usuario al grupo docker (solo primera vez):
```bash
sudo usermod -aG docker $USER
exit
# Abre nueva terminal o reconéctate
```

Verifica que funciona:
```bash
docker ps
```

---

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/aleexa-coder/documentacion-proyecto1.git
cd documentacion-proyecto1
```

### 2. Levantar el servicio
```bash
docker-compose up -d
```

**Output esperado:**
```
Creating docs-proyecto1 ... done
```

### 3. Acceder al portal

Abre tu navegador:
```
http://localhost:8080
```

Deberías ver el portal con menú lateral y documentación de ejemplo.

### 4. Detener el servicio
```bash
docker-compose down
```

---

## 📁 Estructura del Proyecto
```
documentacion-proyecto1/
├── docs/                          # 📝 Documentación en Markdown
│   ├── intro.md                   # Página de inicio
│   ├── iso13485/                  # ISO-13485: Calidad
│   │   ├── intro.md
│   │   ├── requisitos-generales/
│   │   ├── documentacion/
│   │   ├── responsabilidad-direccion/
│   │   ├── gestion-recursos/
│   │   ├── realizacion-producto/
│   │   └── medicion-mejora/
│   └── iso27001/                  # ISO-27001: Seguridad
│       ├── intro.md
│       ├── control-acceso/
│       ├── criptografia/
│       ├── seguridad-fisica/
│       ├── operaciones-comunicaciones/
│       ├── gestion-incidentes/
│       └── cumplimiento/
│
├── src/                           # 🎨 Código custom de Docusaurus
│   ├── css/
│   ├── components/
│   └── pages/
│
├── static/                        # 📦 Archivos estáticos (imágenes, etc)
│
├── Dockerfile                     # 🐳 Multi-stage build
├── docker-compose.yml             # 🎼 Orquestación
├── nginx.conf                     # ⚙️ Configuración Nginx (seguridad, gzip)
├── docusaurus.config.js           # ⚙️ Configuración de Docusaurus
├── sidebars.js                    # 📋 Estructura del menú lateral
├── package.json                   # 📦 Dependencias de Node.js
├── .dockerignore                  # 🚫 Archivos que Docker ignora
├── .gitignore                     # 🚫 Archivos que Git ignora
├── README.md                      # 📖 Este archivo
└── .github/                       # (Futuro: CI/CD workflows)
```

---

## 🐳 Comandos Útiles

### Levantar el servicio
```bash
docker-compose up -d
```

### Ver logs en tiempo real
```bash
docker-compose logs -f
```

**Salir:** `Ctrl+C`

### Ver contenedores corriendo
```bash
docker ps
```

### Detener el servicio
```bash
docker-compose down
```

### Reconstruir la imagen (cambios en Dockerfile/package.json)
```bash
docker-compose build --no-cache
docker-compose up -d
```

### Entrar en el contenedor (debugging)
```bash
docker-compose exec documentacion sh
```

### Ver la imagen construida
```bash
docker images | grep documentacion
```

### Eliminar la imagen (si necesitas clean)
```bash
docker rmi documentacion-proyecto1:latest
```

---

## ✨ Mejoras Implementadas

### Semana 1: Scaffold Base

✅ Instalación de Node.js 20 LTS
✅ Generación de esqueleto Docusaurus
✅ Inicialización de Git con ramas main/dev
✅ Configuración básica de Docusaurus
✅ Primera estructura de directorios (ISO-13485, ISO-27001)

### Semana 2: Conteinerización

✅ **Dockerfile multi-stage build:**
- Etapa 1: Node.js para compilar
- Etapa 2: Nginx para servir (imagen final ~50MB)

✅ **docker-compose.yml:**
- Orquestación automática
- Reinicio automático si falla
- Mapeo de puertos

✅ **nginx.conf optimizado:**
- Headers de seguridad (nosniff, SAMEORIGIN, XSS Protection)
- Compresión gzip para assets
- Caché inteligente (1 año para archivos estáticos)
- Routing SPA (redirige a index.html)
- Logs limpios (sin favicon/robots.txt)

✅ **Seguridad:**
- Node.js 20 (LTS, sin vulnerabilidades)
- Alpine Linux (imagen pequeña y segura)
- .dockerignore para no copiar archivos innecesarios

### Otras Mejoras

✅ **README.md completo** con instrucciones claras
✅ **Configuración de permisos Docker** documentada
✅ **.dockerignore** para reducir tamaño de build
✅ **Commits descriptivos** en Git
✅ **Verificación de headers HTTP** (curl)

---

## 📅 Semanas de Desarrollo

| Semana | Estado | Tareas |
|--------|--------|--------|
| **1** | ✅ COMPLETA | Scaffold Docusaurus, Git, estructura base |
| **2** | ✅ COMPLETA | Docker, Nginx, optimizaciones |
| **3** | ⏳ A ESPERA | VPS (actualmente: docker-compose local) |
| **4** | ⏳ PENDIENTE | Arquitectura de información (requiere PDFs) |
| **5-7** | ⏳ PENDIENTE | Migración de contenido con IA |
| **8-10** | ⏳ PENDIENTE | Seguridad, búsqueda, integración IA |
| **11-12** | ⏳ PENDIENTE | Documentación final y cierre |

---

## 🔐 Seguridad

### Headers HTTP
```nginx
X-Content-Type-Options: nosniff          # Evita MIME sniffing
X-Frame-Options: SAMEORIGIN              # Previene clickjacking
X-XSS-Protection: 1; mode=block          # Protección XSS
```

### Compresión
```nginx
gzip on                                  # Ahorra ancho de banda
Content-Encoding: gzip                   # Transparente para usuario
```

### Imágenes

- **Node.js 20 LTS:** Sin vulnerabilidades críticas
- **Nginx Alpine:** Imagen mínima, menos superficie de ataque
- **No corre como root:** Contenedor usa usuario no privilegiado

### Versionado

- Git con ramas main (producción) / dev (desarrollo)
- Commits descriptivos para auditoría
- Historial completo de cambios

---

## 🐛 Troubleshooting

### Puerto 8080 ya está en uso
```bash
# Opción 1: Cambiar puerto en docker-compose.yml
ports:
  - "9090:80"  # Ahora usa puerto 9090

# Opción 2: Matar el proceso que usa puerto 8080
sudo lsof -i :8080
sudo kill -9 <PID>
```

### Cambios en docs no se reflejan
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Ver errores dentro del contenedor
```bash
docker-compose logs -f documentacion
```

### Nginx da error "add-header unknown directive"

Verifica que escribiste `add_header` (con guion bajo, no guion):
```nginx
✅ add_header X-Content-Type-Options nosniff;
❌ add-header X-Content-Type-Options nosniff;
```

### Docker no tiene permisos
```bash
sudo usermod -aG docker $USER
exit
# Reconéctate
```

### Imagen muy grande

Verifica `.dockerignore` contiene:
```
node_modules
.docusaurus
build
.git
```

---

## 📝 Notas Técnicas

### Multi-stage Build

La imagen final **solo contiene Nginx** (no Node.js):

1. **Builder stage:** Node.js instala dependencias y compila `build/`
2. **Runtime stage:** Nginx sirve solo los archivos precompilados

**Ventaja:** Imagen final ~50MB vs 1GB con Node.js incluido.

### SPA Routing
```nginx
location / {
    try_files $uri $uri/ /index.html;
}
```

Permite que Docusaurus (Single Page Application) funcione correctamente. Si una ruta no existe, sirve `index.html` y deja que React maneje el routing.

### Caché de Archivos Estáticos
```nginx
location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
    expires 1y;
}
```

Archivos con hash (generados por Docusaurus) se cachean 1 año. El navegador NO los descarga de nuevo si ya los tiene.

### Variables de Entorno
```yaml
environment:
  NODE_ENV: production
```

**Nota:** Se quitó porque Nginx no lo necesita (Node.js solo se usa en build).

---

## 🔗 Referencias

- [Docusaurus](https://docusaurus.io/)
- [Docker Documentation](https://docs.docker.com/)
- [Nginx Documentation](https://nginx.org/)
- [ISO-13485](https://www.iso.org/standard/59752.html)
- [ISO-27001](https://www.iso.org/standard/27001)

---

## 👤 Autor

Proyecto realizado como prácticas en empresa.

**Tecnologías aprendidas:** Docker, Docker Compose, Nginx, Docusaurus, Git, Linux, Markdown, Seguridad Web

---

## 📄 Licencia

Interno - VRCardio

---

## ✅ Checklist de Verificación

Antes de entregar:

- [x] `docker-compose up -d` funciona sin errores
- [x] Portal accesible en http://localhost:8080
- [x] Menú lateral muestra ISO-13485 e ISO-27001
- [x] Headers de seguridad presentes (`curl -I`)
- [x] Nginx comprime con gzip
- [x] Git tiene commits descriptivos
- [x] README.md completo y actualizado
- [x] `.dockerignore` configurado
- [ ] PDFs normativos migrados (Semana 4+)

---

## 📞 Soporte

En caso de problemas:

1. Revisa la sección **Troubleshooting**
2. Verifica `docker-compose logs -f`
3. Asegúrate de tener permisos Docker (`docker ps`)
4. Reconstruye con `docker-compose build --no-cache`

