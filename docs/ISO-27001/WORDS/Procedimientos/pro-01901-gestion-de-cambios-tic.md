**ProCEDIMIENTO DE GESTIÓN DE CAMBIOS TIC**










**HISTORIAL DEL DOCUMENTO**


**Versión**
**Resumen de modificaciones**
**Fecha de entrada**
**Sustituye a (Código, revisión)**




01
Primera versión del documento.
26/02/2025
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
26/02/2025
26/02/2025
26/02/2025




# Contenido 

# 

[1 OBJETIVO [4](#objetivo)](#objetivo)

[2 ALCANCE [4](#alcance)](#alcance)

[3 NORMATIVA APLICABLE [4](#normativa-aplicable)](#normativa-aplicable)

[4 ROLES [4](#roles)](#roles)

[5 DESARROLLO [5](#desarrollo)](#desarrollo)

[5.1 OBJETIVOS [5](#objetivos)](#objetivos)

[5.2 PRINCIPIOS [5](#principios)](#principios)

[6 PROCEDIMIENTO DE PETICIONES DE GESTIÓN DE CAMBIO
[6](#procedimiento-de-peticiones-de-gestión-de-cambio)](#procedimiento-de-peticiones-de-gestión-de-cambio)

[6.1 SOLICITUD DE CAMBIO
[6](#solicitud-de-cambio)](#solicitud-de-cambio)

[6.2 CALENDARIO DE CAMBIOS
[7](#calendario-de-cambios)](#calendario-de-cambios)

[6.3 CAMBIOS DE EMERGENCIA
[7](#cambios-de-emergencia)](#cambios-de-emergencia)

[6.4 GESTIÓN DE LOS CAMBIOS
[7](#gestión-de-los-cambios)](#gestión-de-los-cambios)

[7 REFERENCIAS [8](#referencias)](#referencias)

# OBJETIVO

El objeto del presente documento es describir el proceso de gestión de
cambios vigente SPIKA TECH identificando sus principales
características, responsabilidades y señalando las actividades que deben
realizarse, para garantizar el éxito del cambio.

# ALCANCE 

Este procedimiento se aplica en todos los sistemas de información que
dan soporte a los servicios especificados que se incluyen en cada ámbito
de actuación de SPIKA TECH.

# NORMATIVA APLICABLE

Es aplicable toda la normativa establecida en el documento de **RGS\_1
NORMATIVA APLICABLE**, que se actualizara de forma periódica Las
Políticas, Normas y Procedimientos dentro del alcance.

# ROLES

-   **Propietario/Responsable del Proceso / Proyecto:** Lidera el
    proceso / proyecto en la organización, integrando al personal de los
    distintos departamentos involucrados, y adaptando la respuesta de
    dicho proceso a las directrices que se establezcan desde la
    Dirección, al objeto de la Gestión de Servicios de TI.

-   **Gestor del cambio**: Es el rol, interno o externo, que se señala
    como el encargado de la ejecución operativa del proceso, bajo las
    directrices del propietario del proceso / proyecto, y que garantiza
    su correcta realización basándose en la planificación y los
    principios establecidos.

-   **Responsable de seguridad**: Rol que será responsable de aprobar
    aquellos cambios que supongan un riesgo crítico o muy alto para la
    prestación normal de los servicios. En algunos supuestos podrá
    delegar las funciones encomendadas, siempre y cuando no se
    contravengan las atribuciones expresas e indelegables.

# DESARROLLO

## OBJETIVOS

El objetivo de la Gestión de Cambios es tratar eficiente y rápidamente
todos los cambios, con el fin de minimizar las incidencias derivadas de
cambios y el impacto sobre la calidad del servicio, consiguiendo, por
tanto, mejorar el funcionamiento diario de la organización, asegurando
que todos los cambios son gestionados de una manera controlada. En
concreto se definen los siguientes objetivos del proceso:

-   Asegurar que se utilizan métodos adecuados para manejar eficiente y
    rápidamente todos los cambios.

-   Lograr una gestión adecuada del cambio a través de la planificación
    y el calendario de colisiones.

-   Integrar la comunicación con otros procesos que requieren de la
    información o soporte de gestión de cambios.

-   Mantener permanentemente actualizado y accesible a los implicados en
    el servicio el listado de cambios abiertos o en curso.

-   Disponer de mecanismos y procedimientos para gestionar de manera
    adecuada los cambios urgentes y de emergencia.

-   Priorizar la implantación de los cambios de acuerdo con los
    compromisos de servicio.

-   Colaborar en la identificación de cambios proactivos que ayuden a la
    mejora del servicio.

-   Mejorar la utilización de los recursos, incrementando de este modo
    la eficiencia.

## PRINCIPIOS

-   El área de ciberseguridad evalúa el riesgo de aquellas peticiones de
    cambio que supongan un trabajo programado.

-   Los criterios para definir un cambio de emergencia se basan en la
    criticidad y el impacto.

-   Se evaluará todas las peticiones de cambio sustanciales o mayores.

-   Son revisadas las implementaciones de todos los cambios.

-   Las fechas de implementación son conocidas y difundidas a los
    afectados.

-   Se determinan los criterios de impacto de un cambio que genere
    diseño o modificación de un nuevo servicio.

# PROCEDIMIENTO DE PETICIONES DE GESTIÓN DE CAMBIO

## SOLICITUD DE CAMBIO

La petición de cambio puede venir dada por distintos medios:

-   Por el solicitante (persona, área, organismo o unidad que crea la
    petición de cambio).

-   Por correo electrónico.

-   Por problema técnico.

-   Por cambio en la gestión de la configuración

Debe incluir la información y documentación que se estime necesaria para
poder evaluar el cambio, así como una fecha propuesta para la
implementación del cambio. La prioridad de un cambio se determina en
función de su categoría e impacto en el Sistema, teniendo en cuenta
siempre que la solicitud de cambio va a atender a factores de: categoría
de servicio implicado y categorías:

-   **Muy bajo y Bajo**: son aquellos que no impactan de forma inmediata
    a las actividades del servicio, es decir, se puede seguir prestando
    el servicio en condiciones normales de actividad.

-   **Medio**: son aquellos que impactan parcialmente en las actividades
    del servicio.

-   **Alto:** Tiene impacto crítico en los procesos de operación
    realizados desde el servicio y no paralizan toda actividad de este.

-   **Muy alto:** Tiene impacto crítico en los procesos de operación
    realizados desde el servicio y paralizan toda actividad de este.

Todos los cambios que suponga un nivel de riesgo, medio, alto y muy alto
se **desarrollarán con anterioridad en un entorno de pre-producción**,
que tendrá una configuración idéntica al entorno de producción final.
Todo ello se realizará con la finalidad de testear las actualizaciones o
cambios necesarios y asegurar que los mismos no corromperán la
aplicación en los servidores en producción cuando sean desplegados.  

Para realizar la solicitud de cualquier cambio se atenderá a la NORMA DE
REGISTROS DE AUTORIZACIONES.

## CALENDARIO DE CAMBIOS

En el caso de que fuese necesario un cambio de nivel medio, alto o muy
alto, se notificará con suficiente antelación a aquellos usuarios de
SPIKA TECH que hagan uso del servicio afectado. De esta forma, se podrán
determinar los periodos de tiempo críticos para los servicios prestados,
así como el riesgo existente entre los cambios planificados.

## CAMBIOS DE EMERGENCIA

Los cambios con categoría, criticidad y prioridad muy alta se consideran
cambios de emergencia y requieren el análisis y aprobación/rechazo del
Responsable de Seguridad. Una vez aprobados por este, se procederá a la
Implementación del Cambio realizándose posteriormente la documentación
del cambio.

## GESTIÓN DE LOS CAMBIOS

Los cambios solicitados serán gestionados por la persona responsable de
realizarlos siguiendo el siguiente procedimiento:

-   **Solicitado.** Una vez registrada la petición de cambio por la
    persona responsable, el estado del cambio pasará al estado de
    solicitado.

-   **Análisis riesgo**. Antes de realizar el cambio en el entorno de
    pre-producción, se analizarán los riesgos que pudieran derivarse.

-   **Pendiente de aprobación.** Se encuentran en estado “Pendiente de
    aprobación” las peticiones pendientes de validación por parte del
    responsable de realización del cambio. Se debe analizar el posible
    impacto, los recursos necesarios para su implementación y los costes
    asociados.

-   **Rechazado.** Si como resultado del análisis se determina que no es
    procedente/viable la solicitud de gestión de cambio pasará a
    denegarse.

-   **Aprobado.** La solicitud de cambio se encuentra en estado
    “Aprobado”, una vez considerado su impacto y viabilidad, están
    pendientes de planificación para abordar el cambio.

-   **En progreso.** Se encuentran en estado “En Progreso” las
    solicitudes de cambio en producción. La ejecución se realiza a
    través de las peticiones planificadas.

-   **Cancelado**. Solicitudes de cambio con resultado negativo durante
    el proceso de ejecución.

-   **Pendiente PIR.** **Es la Revisión Post Implementación.** Antes de
    dar por finalizada la se debe analizar el resultado de la
    implementación antes de pasar de forma definitiva al entorno de
    producción.

-   **Exitoso.** El cambio se encuentra en este estado cuando la
    ejecución de las peticiones planificadas es correcta.

-   **Fallido.** La ejecución incorrecta de las peticiones planificadas
    que provocan que el cambio sea “Fallido”. Este estado implica la
    ejecución del procedimiento de “marcha atrás” (conjunto de pasos que
    permiten regresar a la configuración anterior a los pasos
    realizados).

# REFERENCIAS

-   ISO 27001:2022:



-   8.32 Gestión de cambios.