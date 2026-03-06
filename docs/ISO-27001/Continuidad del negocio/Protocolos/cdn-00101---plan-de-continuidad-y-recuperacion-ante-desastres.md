---
id: cdn-001-01---plan-de-continuidad-y-recuperacion-ante-desastres
title: "Cdn 001.01   Plan De Continuidad Y Recuperación Ante Desastres"
sidebar_label: "Cdn 001.01   Plan De Continuidad Y Recuperación Ante Desastres"
---

PLAN DE CONTINUIDAD Y RECUPERACIÓN ANTE DESASTRES Contenido
## OBJETIVO
Establecer los procesos, responsabilidades y recursos necesarios para garantizar la continuidad de las operaciones críticas de la organización y la protección de la información durante interrupciones operativas, cumpliendo con los requisitos de ISO 27001 y corrigiendo la No Conformidad detectada.
## ALCANCE
Este plan aplica a:
Sistemas TIC críticos.
Datos y activos de información esenciales para la operación.
Proveedores que soportan actividades críticas, incluyendo servicios CLOUD.
## DEFINICIONES
BCP (Business Continuity Plan): Conjunto de procedimientos para mantener la operación durante y después de una interrupción.
DRP (Disaster Recovery Plan): Conjunto de procesos para recuperar sistemas TIC tras un desastre.
RTO: Tiempo objetivo de recuperación.
RPO: Punto objetivo de recuperación.
## Gobierno del Plan
Responsable del plan: Responsable TIC / Seguridad.
Comité de Continuidad: Dirección, TIC, Seguridad, Operaciones.
Frecuencia de revisión: Anual o tras cambios significativos.
## Análisis de Impacto en el Negocio (BIA)
## Procesos críticos identificados:
Operación de sistemas internos.
Acceso a datos operativos.
Comunicación con clientes.
Procesos financieros.
## Requerimientos de continuidad:
## Estrategia de Continuidad
Para garantizar la protección de la información: - Copias de seguridad automáticas diarias. - Redundancia en servicios CLOUD y validación del proveedor. - Replicación de datos (cuando aplique). - Documentación de procedimientos alternativos manuales.
## Procedimiento de Backup
## Frecuencia
Diaria: Datos críticos.
Semanal: Sistema completo.
## Ubicación de respaldos
Almacenamiento seguro externo al entorno productivo.
Control de acceso restringido.
## Validación de respaldos
Pruebas trimestrales de restauración.
## Procedimiento de Respuesta a Incidentes
Identificación del incidente.
Activación del equipo de continuidad.
Notificación a la dirección.
Inicio del modo de operación alternativo.
Registro en el sistema de incidentes.
## Procedimiento de Recuperación TIC (DRP)
## Activación del DRP
El Responsable TIC activa el DRP cuando la interrupción supera los límites establecidos.
## Pasos de recuperación
Evaluar el estado de infraestructura.
Restaurar servicios críticos en orden de prioridad.
Recuperar datos desde la copia de seguridad validada.
Validar integridad y disponibilidad de la información.
## Validación
Checklist de funcionamiento.
Firma del responsable.
## Pruebas del Plan
## Frecuencia
Anual: Prueba integral de continuidad.
Trimestral: Prueba de recuperación de backups.
## Tipos de pruebas
Pruebas de escritorio.
Pruebas técnicas de restauración.
Simulaciones completas.
## Registro de resultados
Cada prueba incluirá: - Objetivo. - Alcance. - Fecha. - Participantes. - Resultados. - Acciones de mejora.
## Mantenimiento del Plan
Actualización tras cambios en infraestructura o procesos.
Revisión anual por Seguridad.
## Evidencias generadas
Para cumplir la NC, se guardarán: - Informes de pruebas de continuidad. - Registros de restauración de backups. - Controles de estado del proveedor CLOUD. - Versiones revisadas del plan.
## Conclusión
Este plan establece los mecanismos formales para garantizar: - Protección de la información crítica. - Continuidad del negocio. - Recuperación eficaz ante incidentes. - Validación periódica mediante pruebas.
Con su aprobación y aplicación, se da cumplimiento a los requisitos que motivaron la No Conformidad detectada.

| HISTORIAL DEL DOCUMENTO | HISTORIAL DEL DOCUMENTO | HISTORIAL DEL DOCUMENTO | HISTORIAL DEL DOCUMENTO |
| Versión | Resumen de modificaciones | Fecha de entrada | Sustituye a (Código, revisión) |
| 01 | Primera versión del documento. | 26/11/2025 | N/A |

| REGISTRO DE FIRMAS | REGISTRO DE FIRMAS | REGISTRO DE FIRMAS | REGISTRO DE FIRMAS |
| Función: | Elaborado por: | Revisado por: | Aprobado por: |
| Departamento: | Responsable del SGSI | Dirección | Jefe de seguridad

(o suplente) |

| Nombre: | David Pozo | Carlos Rodrigo | Carlos Zúñiga |
| Firma: |  |  |  |
| Fecha: | 26/11/2025 | 26/11/2025 | 26/11/2025 |

| Proceso | RTO | RPO | Nivel de Impacto |
| Acceso a sistemas críticos | 4 h | 1 h | Alto |
| Acceso a datos | 8 h | 4 h | Alto |
| Comunicaciones | 2 h | 0 h | Alto |