---
id: cdn-002-01---procedimiento-de-copias-de-seguridad-y-pruebas-de-restauracion
title: "Cdn 002.01   Procedimiento De Copias De Seguridad Y Pruebas De Restauración"
sidebar_label: "Cdn 002.01   Procedimiento De Copias De Seguridad Y Pruebas De Restauración"
---

pROCEDIMIENTO DE COPIAS DE SEGURIDAD Y PRUEBAS DE RESTAURACIÓN Contenido
## OBJETIVO
Establecer un procedimiento formal para la realización, almacenamiento seguro y verificación periódica de las copias de seguridad de la organización, garantizando el cumplimiento de los requisitos de ISO 2700.
## ALCANCE
Este procedimiento aplica a:
Todos los datos y sistemas críticos de la organización.
Información almacenada en servicios CLOUD (O365, SharePoint, OneDrive, Exchange Online, aplicaciones SaaS).
Sistemas y servidores locales.
Equipos y unidades de almacenamiento asignadas a usuarios.
## Responsabilidades
Responsable TIC / Administrador de Sistemas: Ejecutar y supervisar las copias de seguridad y pruebas de restauración.
Responsable de Seguridad: Verificar cumplimiento y registrar evidencias.
Dirección: Aprobar el procedimiento y asegurar recursos.
## politica general de backup
La organización debe garantizar que:
Toda la información crítica cuenta con respaldo.
Las copias se ejecutan de manera automática y periódica.
Los respaldos se almacenan en ubicaciones seguras y separadas del entorno productivo.
Existen mecanismos de protección contra borrado accidental, ransomware y corrupción.
Se realizan pruebas documentadas de restauración.
## Frecuencia de Copias de Seguridad
## Copias de Seguridad en O365
La organización aplicará:
Uso de herramienta de Backup dedicada para O365 (correo, OneDrive, SharePoint y Teams).
Conservación mínima de 30 días.
Retención extendida para correos críticos (6 meses o según política).
Verificación diaria del estado del backup.
## Copias de Seguridad en Sistemas Locales
Incluye:
Servidores de aplicaciones.
Servidores de archivos.
Bases de datos.
Equipos de usuarios si contienen información relevante.
Las copias se realizarán mediante herramientas corporativas aprobadas y con las siguientes medidas:
Encriptación de respaldos.
Segregación del almacenamiento.
Acceso limitado únicamente al personal autorizado.
## Almacenamiento Seguro
Los respaldos deben:
Guardarse en un repositorio independiente del sistema productivo.
Tener redundancia geográfica o CLOUD.
Estar protegidos mediante:
Cifrado.
Control de acceso.
Monitorización.
Registro de actividad.
## Procedimiento de Restauración
## Solicitud de Restauración
El usuario o responsable solicita la recuperación a TIC, indicando:
Datos solicitados.
Fecha aproximada.
Sistema o ubicación.
## Proceso de Restauración
Verificar que la copia de respaldo existe y está íntegra.
Realizar restauración en entorno de pruebas si aplica.
Validar la integridad de la información restaurada.
Entregar al usuario o restaurar en producción.
Registrar la restauración.
## Tiempo Objetivo
Restauraciones críticas: máximo 4 horas.
Restauraciones estándar: 24 a 48 horas.
## Pruebas Periódicas de Restauración (Requisito Crítico)
Para corregir la No Conformidad, se establece:
Frecuencia: Trimestral.
Alcance mínimo:
Restauración de correos O365.
Restauración de archivos de OneDrive/SharePoint.
Restauración de un servidor o base de datos.
Registro obligatorio:
Fecha.
Sistema restaurado.
Responsable.
Resultado.
Problemas detectados.
Acciones correctivas.
Los registros deben conservarse como evidencia para auditoría.
## Verificación y Auditoría Interna
El Responsable de Seguridad revisará:
Estado de las copias.
Resultados de pruebas.
Informes de restauraciones reales.
Cumplimiento de frecuencia.
## Indicadores de Cumplimiento (KPI)
Éxito de backups: ≥ 98%.
Éxito de restauraciones trimestrales: 100%.
Incidentes relacionados con pérdida de datos: 0.
## Mantenimiento del Procedimiento
Este documento deberá revisarse:
Cada año.
Tras cambios relevantes en infraestructura.
Tras incidentes significativos de disponibilidad.
## Conclusión
Este procedimiento garantiza:
Backups periódicos y verificables.
Almacenamiento seguro de la información.
Evidencias claras para auditoría.

| HISTORIAL DEL DOCUMENTO | HISTORIAL DEL DOCUMENTO | HISTORIAL DEL DOCUMENTO | HISTORIAL DEL DOCUMENTO |
| Versión | Resumen de modificaciones | Fecha de entrada | Sustituye a (Código, revisión) |
| 01 | Primera versión del documento. | 27/11/2025 | N/A |

| REGISTRO DE FIRMAS | REGISTRO DE FIRMAS | REGISTRO DE FIRMAS | REGISTRO DE FIRMAS |
| Función: | Elaborado por: | Revisado por: | Aprobado por: |
| Departamento: | Responsable del SGSI | Dirección | Jefe de seguridad

(o suplente) |

| Nombre: | David Pozo | Carlos Rodrigo | Carlos Zúñiga |
| Firma: |  |  |  |
| Fecha: | 27/11/2025 | 27/11/2025 | 27/11/2025 |

| Tipo de Información | Frecuencia | Medio | Responsable |
| Datos críticos operativos | Diario | CLOUD + repositorio externo | TIC |
| Correo O365 (Exchange Online) | Diario | Backup CLOUD | TIC |
| OneDrive / SharePoint | Diario | Backup CLOUD | TIC |
| Sistemas locales | Semanal | Almacenamiento externo | TIC |
| Configuraciones de sistemas | Semanal | Repositorio seguro | TIC |