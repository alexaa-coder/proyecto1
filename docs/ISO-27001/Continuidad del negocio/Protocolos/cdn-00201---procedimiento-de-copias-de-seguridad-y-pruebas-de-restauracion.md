**pROCEDIMIENTO DE COPIAS DE SEGURIDAD Y PRUEBAS DE RESTAURACIÓN**










**HISTORIAL DEL DOCUMENTO**


**Versión**
**Resumen de modificaciones**
**Fecha de entrada**
**Sustituye a (Código, revisión)**




01
Primera versión del documento.
27/11/2025
N/A













**REGISTRO DE FIRMAS**


**Función:**
**Elaborado por:**
**Revisado por:**
**Aprobado por:**




Departamento:
Responsable del SGSI
Dirección
Jefe de seguridad
(o suplente)


Nombre:
David Pozo
Carlos Rodrigo
Carlos Zúñiga


Firma:





Fecha:
27/11/2025
27/11/2025
27/11/2025




# Contenido 

# 

[1 OBJETIVO [4](#objetivo)](#objetivo)

[2 ALCANCE [4](#alcance)](#alcance)

[3 DEFINICIONES [4](#_Toc215128681)](#_Toc215128681)

[4 Gobierno del Plan [4](#_Toc215128682)](#_Toc215128682)

[5 Análisis de Impacto en el Negocio (BIA)
[4](#_Toc215128683)](#_Toc215128683)

[5.1 Procesos críticos identificados:
[4](#_Toc215128684)](#_Toc215128684)

[5.2 Requerimientos de continuidad: [4](#_Toc215128685)](#_Toc215128685)

[6 Estrategia de Continuidad [5](#_Toc215128686)](#_Toc215128686)

[7 Procedimiento de Backup [5](#_Toc215128687)](#_Toc215128687)

[7.1 Frecuencia [5](#_Toc215128688)](#_Toc215128688)

[7.2 Ubicación de respaldos [5](#_Toc215128689)](#_Toc215128689)

[7.3 Validación de respaldos [5](#_Toc215128690)](#_Toc215128690)

[8 Procedimiento de Respuesta a Incidentes
[5](#_Toc215128691)](#_Toc215128691)

[9 Procedimiento de Recuperación TIC (DRP)
[5](#_Toc215128692)](#_Toc215128692)

[9.1 Activación del DRP [5](#_Toc215128693)](#_Toc215128693)

[9.2 Pasos de recuperación [5](#_Toc215128694)](#_Toc215128694)

[9.3 Validación [6](#_Toc215128695)](#_Toc215128695)

[10 Pruebas del Plan [6](#_Toc215128696)](#_Toc215128696)

[10.1 Frecuencia [6](#_Toc215128697)](#_Toc215128697)

[10.2 Tipos de pruebas [6](#_Toc215128698)](#_Toc215128698)

[10.3 Registro de resultados [6](#_Toc215128699)](#_Toc215128699)

[11 Mantenimiento del Plan [6](#_Toc215128700)](#_Toc215128700)

[12 Evidencias generadas [6](#_Toc215128701)](#_Toc215128701)

[13 Conclusión [6](#_Toc215128702)](#_Toc215128702)

# OBJETIVO

Establecer un procedimiento formal para la realización, almacenamiento
seguro y verificación periódica de las copias de seguridad de la
organización, garantizando el cumplimiento de los requisitos de ISO
2700.

# ALCANCE

Este procedimiento aplica a:

-   Todos los datos y sistemas críticos de la organización.

-   Información almacenada en servicios CLOUD (O365, SharePoint,
    OneDrive, Exchange Online, aplicaciones SaaS).

-   Sistemas y servidores locales.

-   Equipos y unidades de almacenamiento asignadas a usuarios.

# Responsabilidades

-   **Responsable TIC / Administrador de Sistemas:** Ejecutar y
    supervisar las copias de seguridad y pruebas de restauración.

-   **Responsable de Seguridad:** Verificar cumplimiento y registrar
    evidencias.

-   **Dirección:** Aprobar el procedimiento y asegurar recursos.

# politica general de backup

La organización debe garantizar que:

-   Toda la información crítica cuenta con respaldo.

-   Las copias se ejecutan de manera automática y periódica.

-   Los respaldos se almacenan en ubicaciones seguras y separadas del
    entorno productivo.

-   Existen mecanismos de protección contra borrado accidental,
    ransomware y corrupción.

-   Se realizan **pruebas documentadas de restauración**.

# Frecuencia de Copias de Seguridad










Tipo de Información
Frecuencia
Medio
Responsable




Datos críticos operativos
Diario
CLOUD + repositorio externo
TIC


Correo O365 (Exchange Online)
Diario
Backup CLOUD
TIC


OneDrive / SharePoint
Diario
Backup CLOUD
TIC


Sistemas locales
Semanal
Almacenamiento externo
TIC


Configuraciones de sistemas
Semanal
Repositorio seguro
TIC




# Copias de Seguridad en O365

La organización aplicará:

-   Uso de herramienta de **Backup dedicada para O365** (correo,
    OneDrive, SharePoint y Teams).

-   Conservación mínima de 30 días.

-   Retención extendida para correos críticos (6 meses o según
    política).

-   Verificación diaria del estado del backup.

# Copias de Seguridad en Sistemas Locales

Incluye:

-   Servidores de aplicaciones.

-   Servidores de archivos.

-   Bases de datos.

-   Equipos de usuarios si contienen información relevante.

Las copias se realizarán mediante herramientas corporativas aprobadas y
con las siguientes medidas:

-   Encriptación de respaldos.

-   Segregación del almacenamiento.

-   Acceso limitado únicamente al personal autorizado.

# Almacenamiento Seguro

Los respaldos deben:

-   Guardarse en un repositorio independiente del sistema productivo.

-   Tener redundancia geográfica o CLOUD.

-   Estar protegidos mediante:

    -   Cifrado.

    -   Control de acceso.

    -   Monitorización.

    -   Registro de actividad.

# Procedimiento de Restauración

## Solicitud de Restauración

El usuario o responsable solicita la recuperación a TIC, indicando:

-   Datos solicitados.

-   Fecha aproximada.

-   Sistema o ubicación.

## Proceso de Restauración

1.  Verificar que la copia de respaldo existe y está íntegra.

2.  Realizar restauración en entorno de pruebas si aplica.

3.  Validar la integridad de la información restaurada.

4.  Entregar al usuario o restaurar en producción.

5.  Registrar la restauración.

## Tiempo Objetivo

-   Restauraciones críticas: **máximo 4 horas**.

-   Restauraciones estándar: **24 a 48 horas**.

# Pruebas Periódicas de Restauración (Requisito Crítico)

Para corregir la No Conformidad, se establece:

-   **Frecuencia:** Trimestral.

-   **Alcance mínimo:**

    -   Restauración de correos O365.

    -   Restauración de archivos de OneDrive/SharePoint.

    -   Restauración de un servidor o base de datos.

-   **Registro obligatorio:**

    -   Fecha.

    -   Sistema restaurado.

    -   Responsable.

    -   Resultado.

    -   Problemas detectados.

    -   Acciones correctivas.

Los registros deben conservarse como evidencia para auditoría.

# Verificación y Auditoría Interna

El Responsable de Seguridad revisará:

-   Estado de las copias.

-   Resultados de pruebas.

-   Informes de restauraciones reales.

-   Cumplimiento de frecuencia.

# Indicadores de Cumplimiento (KPI)

-   **Éxito de backups:** ≥ 98%.

-   **Éxito de restauraciones trimestrales:** 100%.

-   **Incidentes relacionados con pérdida de datos:** 0.

# Mantenimiento del Procedimiento

Este documento deberá revisarse:

-   Cada año.

-   Tras cambios relevantes en infraestructura.

-   Tras incidentes significativos de disponibilidad.

# Conclusión

Este procedimiento garantiza:

-   Backups periódicos y verificables.

-   Almacenamiento seguro de la información.

-   Evidencias claras para auditoría.