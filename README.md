# 📚 Proyecto 1: Gestor Documental de Compliance "AI-Ready"

**Duración**: 10-12 Semanas (2-3 meses)  
**Perfil**: Estudiantes de Grado Superior en Sistemas (ASIR/DAM)  
**Tecnologías**: Docusaurus, Docker, Nginx, Linux, NotebookLM

---

## 🎯 Objetivo del Proyecto

Crear una plataforma centralizada y segura que aloje normativa ISO-13485 (Calidad Productos Sanitarios) e ISO-27001 (Seguridad de la Información), con versionado de documentos y estructurada semánticamente para que agentes de IA puedan indexarla y consultarla de manera autónoma.

---

## 📋 Requisitos Previos

Para ejecutar este proyecto necesitas tener instalado:

- **Docker** (versión 20.x o superior)
- **Docker Compose** (versión 2.x o superior)
- **Git**
- **Node.js 16+** (solo si vas a desarrollar localmente sin Docker)

### Verificar instalación:

```bash
docker --version
docker-compose --version
git --version
```

---

## 🚀 Instalación y Despliegue Rápido

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd documentacion-proyecto1
```

### 2. Levantar el contenedor

```bash
docker-compose up -d
```

### 3. Verificar que está corriendo

```bash
docker-compose ps
```

Deberías ver algo como:
```
     Name                   Command               State                  Ports                
----------------------------------------------------------------------------------------------
docs-proyecto1   /docker-entrypoint.sh ngin ...   Up      0.0.0.0:8080->80/tcp,:::8080->80/tcp
```

### 4. Acceder a la aplicación

Abre tu navegador en: **http://localhost:8080**

---

## 🛠️ Comandos Útiles

### Gestión del contenedor:

```bash
# Ver logs en tiempo real
docker-compose logs -f

# Parar el contenedor
docker-compose down

# Reiniciar el contenedor
docker-compose restart

# Reconstruir la imagen (después de cambios en código)
docker-compose up -d --build

# Ver estado de los contenedores
docker-compose ps

# Ver uso de recursos
docker stats docs-proyecto1
```

### Gestión de Docker:

```bash
# Ver todas las imágenes
docker images

# Ver todos los contenedores (incluso parados)
docker ps -a

# Limpiar recursos no utilizados
docker system prune -a

# Ver espacio utilizado
docker system df
```

---

## 📁 Estructura del Proyecto

```
documentacion-proyecto1/
├── docs/                      # Contenido de la documentación (Markdown)
│   ├── intro.md
│   └── ...
├── src/                       # Configuración y componentes de Docusaurus
│   ├── css/
│   └── pages/
├── static/                    # Archivos estáticos (imágenes, PDFs)
│   └── img/
├── Dockerfile                 # Configuración multi-stage build
├── docker-compose.yml         # Orquestación de servicios
├── nginx.conf                 # Configuración del servidor Nginx
├── package.json               # Dependencias de Node.js
├── package-lock.json          # Lock file de dependencias
├── docusaurus.config.js       # Configuración principal de Docusaurus
├── sidebars.js                # Configuración de la barra lateral
├── babel.config.js            # Configuración de Babel
├── .gitignore                 # Archivos ignorados por Git
└── README.md                  # Este archivo
```

---

## 🏗️ Arquitectura Técnica

### Multi-Stage Build

El proyecto utiliza **Docker Multi-Stage Build** para optimizar el tamaño de la imagen final:

#### ¿Qué es Multi-Stage Build?

Es dividir el Dockerfile en **múltiples etapas (stages)**, donde cada una puede usar una imagen base diferente. Esto permite:
- Usar herramientas pesadas solo durante la compilación
- Copiar únicamente los archivos necesarios a producción
- Reducir drásticamente el tamaño de la imagen final

#### Nuestro Dockerfile explicado:

```dockerfile
# ============================================
# STAGE 1: BUILD (Compilación)
# ============================================
FROM node:16-alpine AS builder
# Imagen base: Node.js 16 en Alpine Linux (ligera)
# Alias: "builder" para referenciarla después

WORKDIR /app
# Directorio de trabajo dentro del contenedor

COPY package*.json ./
# Copia solo package.json y package-lock.json primero
# (Aprovecha la caché de Docker si no cambian las dependencias)

RUN npm install
# Instala todas las dependencias de Node.js

COPY . .
# Copia el resto del código fuente

RUN npm run build
# Ejecuta el comando de build de Docusaurus
# Genera archivos HTML/CSS/JS estáticos en /app/build

# ============================================
# STAGE 2: PRODUCTION (Servidor web)
# ============================================
FROM nginx:alpine
# Nueva imagen base: Nginx en Alpine (mucho más ligera)
# NO incluye Node.js ni herramientas de desarrollo

COPY --from=builder /app/build /usr/share/nginx/html
# Copia SOLO los archivos compilados desde el stage anterior
# Los archivos van al directorio que Nginx usa para servir contenido

COPY nginx.conf /etc/nginx/conf.d/default.conf
# Copia nuestra configuración personalizada de Nginx

EXPOSE 80
# Expone el puerto 80 (HTTP)

CMD ["nginx", "-g", "daemon off;"]
# Comando para iniciar Nginx en primer plano
```

#### Ventajas del Multi-Stage Build:

| Aspecto | Sin Multi-Stage | Con Multi-Stage |
|---------|----------------|-----------------|
| **Tamaño de imagen** | ~900 MB | ~40 MB |
| **Tiempo de descarga** | Lento | Rápido |
| **Seguridad** | Incluye herramientas dev | Solo archivos necesarios |
| **Rendimiento** | Node.js sirviendo estáticos | Nginx optimizado |

---

## 🐳 Docker Compose

El archivo `docker-compose.yml` orquesta el despliegue:

```yaml
version: '3.8'

services:
  documentacion:
    build: .                          # Construye desde el Dockerfile local
    container_name: docs-proyecto1    # Nombre del contenedor
    ports:
      - "8080:80"                     # Puerto host:contenedor
    restart: always                   # Reinicia automáticamente si falla
    environment:
      NODE_ENV: production            # Variable de entorno
```

**Explicación:**
- `build: .` → Construye la imagen usando el Dockerfile en el directorio actual
- `ports: "8080:80"` → Mapea el puerto 80 del contenedor al 8080 del host
- `restart: always` → Si el contenedor se detiene, Docker lo reinicia automáticamente

---

## 🔧 Configuración de Nginx

El archivo `nginx.conf` configura cómo Nginx sirve los archivos:

```nginx
server {
    listen 80;
    server_name localhost;

    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    # Configuración adicional para Docusaurus
    location ~* \.(?:css|js|jpg|jpeg|gif|png|ico|svg|woff|woff2|ttf|eot)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

**Funciones clave:**
- Sirve archivos desde `/usr/share/nginx/html`
- Redirige todas las rutas a `index.html` (para SPA - Single Page Application)
- Configura caché para archivos estáticos (mejora rendimiento)

---

## 🧠 ¿Por qué Node.js en el Proyecto?

### Node.js es OBLIGATORIO para Docusaurus porque:

1. **Docusaurus está construido con Node.js**
   - Es un framework JavaScript/React
   - Necesita Node.js como runtime de ejecución

2. **Gestión de dependencias**
   - NPM descarga e instala +1000 paquetes necesarios
   - Gestiona versiones y compatibilidad

3. **Proceso de compilación (Build)**
   - Transforma Markdown → HTML
   - Compila componentes React → JavaScript optimizado
   - Optimiza CSS, imágenes y assets
   - Genera archivos estáticos para producción

4. **Servidor de desarrollo**
   - `npm start` levanta servidor local con hot-reload
   - Permite desarrollo en tiempo real

### ¿Por qué NO usamos Node.js en producción?

```
┌─────────────────────────────────────────────────────┐
│  DESARROLLO LOCAL (Node.js)                         │
│  npm start → localhost:3000                         │
│  - Hot reload                                       │
│  - Modo desarrollo                                  │
│  - Archivos sin optimizar                           │
└─────────────────────────────────────────────────────┘
                      ↓
                npm run build
                      ↓
┌─────────────────────────────────────────────────────┐
│  PRODUCCIÓN (Nginx)                                 │
│  Archivos estáticos HTML/CSS/JS                     │
│  - Optimizados y minificados                        │
│  - Sin dependencias de Node.js                      │
│  - Imagen 20x más pequeña                           │
│  - Mayor rendimiento                                │
└─────────────────────────────────────────────────────┘
```

**Nginx es superior a Node.js para servir archivos estáticos:**
- Consume menos memoria
- Maneja más conexiones simultáneas
- Mayor velocidad de respuesta
- Mejor para caché y compresión

---

## ✅ Checklist de Progreso

### FASE 1: Infraestructura y Despliegue Base ✅

- [x] **Semana 1: Configuración del entorno local**
  - [x] Instalación de Node.js
  - [x] Generación del esqueleto base de Docusaurus
  - [x] Inicialización del repositorio Git
  - [x] Configuración de ramas (main, dev)
  - [x] Personalización de docusaurus.config.js

- [x] **Semana 2: Containerización**
  - [x] Creación de Dockerfile con multi-stage build
  - [x] Configuración de docker-compose.yml
  - [x] Verificación de persistencia
  - [x] Pruebas en localhost:8080

- [ ] **Semana 3: Despliegue en VPS** (No requerido para evaluación)
  - Se omite en este proyecto ya que el tutor evaluará clonando el repositorio

### FASE 2: Migración de Contenido ⏳

- [ ] **Semana 4: Arquitectura de la Información**
- [ ] **Semana 5-6: Migración Asistida con IA (NotebookLM)**
- [ ] **Semana 7: Metadatos (Frontmatter)**

### FASE 3: Seguridad y Producción ⏳

- [ ] **Semana 8: Seguridad de Acceso**
- [ ] **Semana 9: Motor de Búsqueda Local**
- [ ] **Semana 10: Integración y Test con Agentes**

### FASE 4: Documentación y Cierre ⏳

- [ ] **Semana 11: Automatización de Mantenimiento**
- [ ] **Semana 12: Manual de Operaciones**

---

## 🐛 Solución de Problemas

### El contenedor no inicia

```bash
# Ver logs detallados
docker-compose logs

# Ver logs en tiempo real
docker-compose logs -f

# Reconstruir la imagen
docker-compose down
docker-compose up -d --build
```

### Puerto 8080 ya en uso

```bash
# Ver qué está usando el puerto
sudo lsof -i :8080

# O cambiar el puerto en docker-compose.yml
ports:
  - "9090:80"  # Usa el puerto 9090 en lugar de 8080
```

### Error "Container name already in use"

```bash
# Listar todos los contenedores
docker ps -a

# Eliminar el contenedor existente
docker rm -f nombre-del-contenedor

# O usa docker-compose down primero
docker-compose down
docker-compose up -d
```

### Cambios en el código no se reflejan

```bash
# Reconstruir la imagen forzando
docker-compose up -d --build --force-recreate
```

---

## 📚 Recursos y Referencias

### Documentación oficial:
- [Docusaurus](https://docusaurus.io/)
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Nginx](https://nginx.org/en/docs/)

### Tecnologías utilizadas:
- **Docusaurus 3.x**: Generador de sitios estáticos
- **Node.js 16**: Runtime de JavaScript
- **React 18**: Biblioteca de UI
- **Nginx Alpine**: Servidor web ligero
- **Docker**: Containerización
- **Docker Compose**: Orquestación de contenedores

---

## 👨‍💻 Desarrollo Local (sin Docker)

Si prefieres desarrollar sin Docker:

```bash
# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm start
# Abre http://localhost:3000

# Compilar para producción
npm run build

# Previsualizar build de producción
npm run serve
```

---

## 🔐 Seguridad

**Nota**: Este proyecto incluirá en fases posteriores:
- Autenticación con Basic Auth en Nginx
- Certificados SSL/TLS con Let's Encrypt
- Restricciones por IP/VPN
- Firewall UFW configurado

---

## 📝 Notas Técnicas

### ¿Por qué Alpine Linux?

Alpine es una distribución Linux ultra-ligera:
- Imagen base: ~5 MB (vs Ubuntu: ~70 MB)
- Menor superficie de ataque (seguridad)
- Menos dependencias
- Ideal para contenedores

### ¿Por qué puerto 8080?

- Puerto 80 requiere privilegios de root en el host
- 8080 es un puerto común para desarrollo
- Fácilmente configurable en docker-compose.yml

---

## 📞 Soporte

Para problemas o dudas sobre el proyecto, contacta con:
- **Tutor del proyecto**: [nombre]
- **Repositorio**: [URL del repositorio Git]

---

## 📄 Licencia

Este proyecto es parte de un trabajo académico para el IES Cañaveral.

---

**Última actualización**: Enero 2026  
**Versión**: 1.0  
**Estado**: Fase 1 completada ✅
