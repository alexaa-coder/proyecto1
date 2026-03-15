---
title: "Contenido"
sidebar_label: "Contenido"
responsable: "Director de Calidad"
clasificacion: "USO INTERNO"
fecha_revision: "2026-03-15"
idioma: "es"
tags:
  - calidad
  - english
  - iso-13485
  - operacion
  - pnt
  - procedimiento
---

GESTIÓN DE CONTROL DE CAMBIOS










Función:
Elaborado por:
Revisado por:
Aprobado por:




Departamento:
Garantía de Calidad
Sistemas y ciberseguridad
Garantía de Calidad


Nombre:
Iván Pérez
David Pozo
Fernando Pozo


Firma:





Fecha:














Valido hasta:
30/11/2028















**HISTORIAL DEL DOCUMENTO**




**VERSIÓN**
**CAUSAS DE LA MODIFICACIÓN**
**FECHA entrada en Vigor**
**SUSTITUYE A (Código, Revisión)**


01
Edición inicial
14/02/2024
N/A


02
Cambio en los departamentos de Spika. Adaptación a formato
digital
02/06/2025
PNT-005.01


03
Modificación del apartado 5.5
30/11/2025
PNT-005.02




# Contenido

[1. Objetivo [4](#_Toc197611356)](#_Toc197611356)

[2. Alcance [4](#alcance)](#alcance)

[3. Responsabilidades y Departamentos afectados
[4](#responsabilidades-y-departamentos-afectados)](#responsabilidades-y-departamentos-afectados)

[4. Definiciones y Acrónimos
[5](#definiciones-y-acrónimos)](#definiciones-y-acrónimos)

[5. Procedimiento [6](#procedimiento)](#procedimiento)

[5.1. Introducción [6](#introducción)](#introducción)

[5.2. Clasificación de los cambios
[6](#clasificación-de-los-cambios)](#clasificación-de-los-cambios)

[5.3. Codificación controles de cambio
[6](#codificación-controles-de-cambio)](#codificación-controles-de-cambio)

[5.4. Fase I: propuesta y descripción del cambio
[7](#fase-i-propuesta-y-descripción-del-cambio)](#fase-i-propuesta-y-descripción-del-cambio)

[5.5. Fase II: evaluación y aprobación
[7](#fase-ii-evaluación-y-aprobación)](#fase-ii-evaluación-y-aprobación)

[5.6. Fase III: clasificación y aprobación del cambio
[8](#fase-iii-clasificación-y-aprobación-del-cambio)](#fase-iii-clasificación-y-aprobación-del-cambio)

[5.7. Modificaciones a la propuesta inicial
[9](#modificaciones-a-la-propuesta-inicial)](#modificaciones-a-la-propuesta-inicial)

[5.8. Listado de controles de cambios
[9](#listado-de-controles-de-cambios)](#listado-de-controles-de-cambios)

[6. Distribución del Procedimiento
[9](#distribución-del-procedimiento)](#distribución-del-procedimiento)

[7. Documentación relacionada
[10](#documentación-relacionada)](#documentación-relacionada)

[8. Formación [10](#section)](#section)



# Objetivo

El objetivo del presente procedimiento es definir la estrategia y
requerimientos de Spika Tech, en adelante SPIKA, para la gestión de los
cambios, con el fin de evitar que los cambios se hagan sin control y
evaluación pudiendo afectar negativamente a la seguridad y calidad de
los productos fabricados por SPIKA.

Una buena gestión de control de cambios asegura que se tomen las
precauciones necesarias por todos los departamentos que intervienen en
los procesos para que estos cambios se evalúen, documenten, aprueben y
se implementen de manera adecuada.

# Alcance

Este procedimiento aplica a todos los cambios planificados o no
planificados que puedan afectar al producto desarrollado, utilizado o
mantenido por la organización, incluyendo:

-   Código fuente, algoritmos y lógica funcional.

-   Arquitectura, módulos y componentes del sistema.

-   Documentación del software (requisitos, especificaciones,
    validaciones...).

-   Sistemas de soporte (infraestructura TI, bases de datos, APIs...).

-   Herramientas de desarrollo o testeo que impacten en la calidad del
    producto.

-   Elementos del sistema de gestión de calidad que afecten al ciclo de
    vida del software (p.ej., procedimientos, plantillas,
    configuraciones clave).

#  Responsabilidades y Departamentos afectados

Todo el personal de SPIKA debe gestionar los cambios de su área, y es
responsable de cumplir las pautas de este procedimiento.

El Técnico Responsable asegurará el cumplimiento de este procedimiento.

Los departamentos afectados son los señalados en la siguiente tabla:









Departamento
Aplica


Si
No




Dirección
☒
☐


Medio ambiente
☒
☐


Garantía de Calidad
☒
☐


Sistemas y Ciberseguridad
☒
☐


Investigación y Desarrollo
☒
☐


Marketing y Ventas
☒
☐


Gestión
☒
☐




# Definiciones y Acrónimos

-   Cambio: Toda inclusión, modificación, sustitución o
    eliminación, temporal o permanente, planificada sobre un estándar
    establecido. Abarca procesos, especificaciones, código fuente,
    componentes de software, servicios o documentación relacionada con
    el sistema de gestión de calidad del software..

-   Cambio temporal: Aquel que, tras un periodo de tiempo
    definido, revierte al estado anterior. Se utiliza cuando el cambio
    está justificado para una situación puntual. Debe dejarse constancia
    de su duración, seguimiento y mecanismos de reversión.

-   Control de Cambios: Proceso formal en el que personal
    cualificado revisa, evalúa, aprueba y documenta los cambios que
    pueden impactar en la seguridad, desempeño, cumplimiento normativo o
    trazabilidad del producto software o del sistema de calidad. Su
    objetivo es asegurar que el sistema mantiene su conformidad y
    validez tras la implementación del cambio.

-   CC: Control de Cambios

# Procedimiento

# Introducción

Una correcta gestión del proceso de control de cambios se considera un
pilar fundamental del Sistema de Gestión de Calidad. Este procedimiento
asegura que cualquier modificación planificada en el producto,
infraestructura tecnológica, procesos asociados o documentación
relevante sea evaluada, aprobada y documentada de forma estructurada,
garantizando el cumplimiento normativo, la seguridad y la eficacia del
sistema.

El presente procedimiento establece las fases necesarias para la gestión
de un cambio, desde su origen hasta su completa implementación. Se
divide en **tres etapas principales**, cada una con actividades y
responsabilidades definidas:

-   Fase I Propuesta y descripción del cambio

-   Fase II Evaluación y aprobación

-   Fase III Implementación y cierre

# Clasificación de los cambios

-   **Cambio Major**: Corresponde a modificaciones significativas
    que afectan las funcionalidades principales, la arquitectura, el
    diseño o el alcance general del sistema/proyecto. Este tipo de
    cambio requiere un enfoque exhaustivo para garantizar la calidad y
    el cumplimiento

-   **Cambio Minor**: Incluye modificaciones menores que afectan
    funcionalidades existentes, pero sin alterar significativamente el
    comportamiento general del sistema. Estos cambios tienen un impacto
    más limitado y requieren una evaluación enfocada.

-   **Cambio Patch**: Comprende modificaciones enfocadas
    exclusivamente en corregir errores o problemas específicos sin
    alterar la funcionalidad del sistema ni su comportamiento general

# Codificación controles de cambio

Cada control de cambios será identificado con un nº único asignado
automáticamente por el software Jira, de la siguiente manera:

**CC – XX**

Donde:

CC son las siglas de Control de Cambios

XX nº correlativo de 2 dígitos

# Fase I: propuesta y descripción del cambio

Una vez identificada la necesidad de un cambio, el solicitante del
cambio debe iniciar la solicitud directamente en Jira. El solicitante es
responsable de detallar la razón de la modificación, así como las
repercusiones de su implementación.

En Jira, el solicitante completará los campos necesarios para describir
el cambio, su justificación y la descripción del impacto esperado. Una
vez completada esta información, el cambio será registrado y listo para
su evaluación inicial.

# Fase II: evaluación y aprobación

Dependiendo del tipo de cambio hay que llevar a cabo la suiguiente
evaluación:

-   Cambio Major:

    -   Comprobación de funcionalidad: Se debe verificar nuevamente que
        todas las funcionalidades del producto operen correctamente y
        conforme a los requisitos especificados.

    

    -   Análisis de riesgos: Es imprescindible evaluar los riesgos
        asociados al cambio y actualizar los análisis existentes para
        mitigar posibles impactos.

    -   Evaluación del cumplimiento reglamentario: Confirmar que el
        producto sigue cumpliendo las normativas aplicables, ya que
        estos cambios podrían afectar la conformidad.



-   Cambio Minor:

    -   Comprobación de funcionalidad: Validar que las funcionalidades
        ajustadas o modificadas operen correctamente y que no haya
        afectaciones colaterales.

    -   Análisis de riesgos: Revisar si el cambio introduce nuevos
        riesgos o afecta los existentes, y actualizar la documentación
        correspondiente.

-   Cambio Patch:

    -   Comprobación de funcionalidad: Validar que el error corregido
        esté resuelto y que las áreas afectadas funcionen adecuadamente.
        No se requiere un análisis exhaustivo fuera del ámbito del
        cambio.

Se debe realizar un análisis de impacto UDI para cada modificación:

-   Se documentará si la liberación genera un nuevo **UDI-PI** (cambio
    de versión).

-   Se determinará si el cambio afecta al **Basic UDI-DI** (por ejemplo,
    cambio en el uso previsto o familia de productos)."

**Evaluación de Impacto Regulatorio (MDR):** Durante la evaluación, se
deben cumplimentar los campos específicos en la solicitud de cambio para
registrar el análisis de:

-   **Gestión de Riesgos:** Revisar si el cambio afecta al análisis de
    riesgos existente.

-   **Identificadores UDI:** Determinar si el cambio requiere un nuevo
    UDI-DI o UDI-PI.

-   **Documentación Técnica:** Identificar qué secciones del expediente
    técnico requieren actualización.

-   **Notificación al Organismo Notificado:** Revisar si el cambio
    afecta a la información ya evaluada por el Organismo Notificado y
    requiere notificación previa según el MDR.

# Fase III: clasificación y aprobación del cambio

En esta fase, una vez aprobado el cambio, se procede a su implementación
con el objetivo de liberar una nueva versión del producto afectado.
Todas las tareas necesarias para ejecutar el cambio deberán estar
correctamente planificadas, asignadas y monitorizadas en Jira.

Durante esta etapa, el equipo técnico será responsable de coordinar la
ejecución del plan, incluyendo actividades como el desarrollo, pruebas,
validaciones internas, generación de documentación actualizada y
comunicación a los usuarios o clientes si aplica.

Una vez implementado el cambio, se deberá registrar en Jira el número de
versión correspondiente, junto con una breve descripción de los cambios
incluidos. También se deberá documentar si la implementación ha sido
satisfactoria, identificando cualquier desviación o incidencia que haya
surgido durante el proceso.

La versión será considerada como finalizada y cerrada en Jira cuando:

-   Todas las tareas estén completadas y verificadas.

-   Se haya documentado correctamente el resultado del cambio.

-   Se haya actualizado la versión del producto y esté disponible para
    los usuarios o producción.

# Modificaciones a la propuesta inicial

Si por algún motivo la propuesta inicial del cambio cambia ese cambio
será anulado y deberá abrirse uno nuevo.

# Listado de controles de cambios

Todos los controles de cambios serán registrados y gestionados a través
del tablero de Jira, desde donde podrá consultarse en todo momento el
historial completo de cambios. En el apartado de **Incidencias** del
proyecto, se mostrará automáticamente el listado con todos los controles
de cambios generados, junto con sus identificadores únicos, estados,
responsables, fechas clave, tipo de cambio y cualquier información
relevante asociada. Este registro digital sustituye al listado manual y
asegura la trazabilidad, consulta y supervisión.

# Distribución del Procedimiento

El personal perteneciente a los departamentos indicados en el Apartado 3
(Responsabilidades y Departamentos afectados), se les debe proporcionar
copia del presente procedimiento. Además, la copia controlada nº1 será
entregada al Archivo para su archivo en papel.

Copias controladas a emitir:








**Nº Copia controlada**
**Departamentos**




1
Archivo




# Documentación relacionada








**Código**
**TÍTULO**




MQ-01
Manual de Calidad




# 

# Formación

La presente versión requiere que los departamentos afectados indicados
en el apartado 3 reciban la formación que a continuación se indica:








**Marcar con una X**
**Tipo formación**




☒
**Teórica** (lectura y comprensión del
procedimiento)


☐
**Teórico – Práctica** (En caso de seleccionar esta
opción, contactar con el Técnico Responsable)