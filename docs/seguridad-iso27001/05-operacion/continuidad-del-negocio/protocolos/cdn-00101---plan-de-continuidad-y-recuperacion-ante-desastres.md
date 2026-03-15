---
title: "Contenido"
sidebar_label: "Contenido"
responsable: "Responsable del SGSI"
clasificacion: "USO INTERNO"
fecha_revision: "2026-03-15"
idioma: "es"
tags:
  - cdn
  - continuidad
  - iso-27001
  - operacion
  - procedimiento
  - seguridad
---

style="width:4.70833in;height:1.85426in" alt="Spika Tech" /&gt;

**PLAN DE CONTINUIDAD Y RECUPERACIÓN ANTE DESASTRES**










**HISTORIAL DEL DOCUMENTO**


**Versión**
**Resumen de modificaciones**
**Fecha de entrada**
**Sustituye a (Código, revisión)**




01
Primera versión del documento.
26/11/2025
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
26/11/2025
26/11/2025
26/11/2025




# Contenido 

# 

[1 OBJETIVO [4](#objetivo)](#objetivo)

[2 ALCANCE [4](#alcance)](#alcance)

[3 DEFINICIONES [4](#definiciones)](#definiciones)

[4 Gobierno del Plan [4](#gobierno-del-plan)](#gobierno-del-plan)

[5 Análisis de Impacto en el Negocio (BIA)
[4](#análisis-de-impacto-en-el-negocio-bia)](#análisis-de-impacto-en-el-negocio-bia)

[5.1 Procesos críticos identificados:
[4](#procesos-críticos-identificados)](#procesos-críticos-identificados)

[5.2 Requerimientos de continuidad:
[4](#requerimientos-de-continuidad)](#requerimientos-de-continuidad)

[6 Estrategia de Continuidad
[5](#estrategia-de-continuidad)](#estrategia-de-continuidad)

[7 Procedimiento de Backup
[5](#procedimiento-de-backup)](#procedimiento-de-backup)

[7.1 Frecuencia [5](#frecuencia)](#frecuencia)

[7.2 Ubicación de respaldos
[5](#ubicación-de-respaldos)](#ubicación-de-respaldos)

[7.3 Validación de respaldos
[5](#validación-de-respaldos)](#validación-de-respaldos)

[8 Procedimiento de Respuesta a Incidentes
[5](#procedimiento-de-respuesta-a-incidentes)](#procedimiento-de-respuesta-a-incidentes)

[9 Procedimiento de Recuperación TIC (DRP)
[5](#procedimiento-de-recuperación-tic-drp)](#procedimiento-de-recuperación-tic-drp)

[9.1 Activación del DRP [5](#activación-del-drp)](#activación-del-drp)

[9.2 Pasos de recuperación
[5](#pasos-de-recuperación)](#pasos-de-recuperación)

[9.3 Validación [6](#validación)](#validación)

[10 Pruebas del Plan [6](#pruebas-del-plan)](#pruebas-del-plan)

[10.1 Frecuencia [6](#frecuencia-1)](#frecuencia-1)

[10.2 Tipos de pruebas [6](#tipos-de-pruebas)](#tipos-de-pruebas)

[10.3 Registro de resultados
[6](#registro-de-resultados)](#registro-de-resultados)

[11 Mantenimiento del Plan
[6](#mantenimiento-del-plan)](#mantenimiento-del-plan)

[12 Evidencias generadas
[6](#evidencias-generadas)](#evidencias-generadas)

[13 Conclusión [6](#conclusión)](#conclusión)

# OBJETIVO

Establecer los procesos, responsabilidades y recursos necesarios para
garantizar la continuidad de las operaciones críticas de la organización
y la protección de la información durante interrupciones operativas,
cumpliendo con los requisitos de ISO 27001 y corrigiendo la No
Conformidad detectada.

# ALCANCE

Este plan aplica a:

-   Sistemas TIC críticos.

-   Datos y activos de información esenciales para la operación.

-   Proveedores que soportan actividades críticas, incluyendo servicios
    CLOUD.

# DEFINICIONES

-   **BCP (Business Continuity Plan):** Conjunto de procedimientos para
    mantener la operación durante y después de una interrupción.

-   **DRP (Disaster Recovery Plan):** Conjunto de procesos para
    recuperar sistemas TIC tras un desastre.

-   **RTO:** Tiempo objetivo de recuperación.

-   **RPO:** Punto objetivo de recuperación.

# Gobierno del Plan

-   **Responsable del plan:** Responsable TIC / Seguridad.
-   **Comité de Continuidad:** Dirección, TIC, Seguridad, Operaciones.
-   **Frecuencia de revisión:** Anual o tras cambios significativos.

# Análisis de Impacto en el Negocio (BIA)

## Procesos críticos identificados:

-   Operación de sistemas internos.
-   Acceso a datos operativos.
-   Comunicación con clientes.
-   Procesos financieros.

## Requerimientos de continuidad:










Proceso
RTO
RPO
Nivel de Impacto




Acceso a sistemas críticos
4 h
1 h
Alto


Acceso a datos
8 h
4 h
Alto


Comunicaciones
2 h
0 h
Alto




# Estrategia de Continuidad

Para garantizar la protección de la información: - Copias de seguridad
automáticas diarias. - Redundancia en servicios CLOUD y validación del
proveedor. - Replicación de datos (cuando aplique). - Documentación de
procedimientos alternativos manuales.

# Procedimiento de Backup

## Frecuencia

-   **Diaria:** Datos críticos.
-   **Semanal:** Sistema completo.

## Ubicación de respaldos

-   Almacenamiento seguro externo al entorno productivo.
-   Control de acceso restringido.

## Validación de respaldos

-   Pruebas trimestrales de restauración.

# Procedimiento de Respuesta a Incidentes

1.  Identificación del incidente.
2.  Activación del equipo de continuidad.
3.  Notificación a la dirección.
4.  Inicio del modo de operación alternativo.
5.  Registro en el sistema de incidentes.

# Procedimiento de Recuperación TIC (DRP)

## Activación del DRP

-   El Responsable TIC activa el DRP cuando la interrupción supera los
    límites establecidos.

## Pasos de recuperación

1.  Evaluar el estado de infraestructura.
2.  Restaurar servicios críticos en orden de prioridad.
3.  Recuperar datos desde la copia de seguridad validada.
4.  Validar integridad y disponibilidad de la información.

## Validación

-   Checklist de funcionamiento.
-   Firma del responsable.

# Pruebas del Plan

## Frecuencia

-   **Anual:** Prueba integral de continuidad.
-   **Trimestral:** Prueba de recuperación de backups.

## Tipos de pruebas

-   Pruebas de escritorio.
-   Pruebas técnicas de restauración.
-   Simulaciones completas.

## Registro de resultados

Cada prueba incluirá: - Objetivo. - Alcance. - Fecha. - Participantes. Resultados. - Acciones de mejora.

# Mantenimiento del Plan

-   Actualización tras cambios en infraestructura o procesos.
-   Revisión anual por Seguridad.

# Evidencias generadas

Para cumplir la NC, se guardarán: - Informes de pruebas de
continuidad. - Registros de restauración de backups. - Controles de
estado del proveedor CLOUD. - Versiones revisadas del plan.

# Conclusión

Este plan establece los mecanismos formales para garantizar: Protección de la información crítica. - Continuidad del negocio. Recuperación eficaz ante incidentes. - Validación periódica mediante
pruebas.

Con su aprobación y aplicación, se da cumplimiento a los requisitos que
motivaron la No Conformidad detectada.