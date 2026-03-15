---
title: "Contenido"
sidebar_label: "Contenido"
responsable: "Director de Calidad"
clasificacion: "USO INTERNO"
fecha_revision: "2026-03-15"
idioma: "es"
tags:
  - calidad
  - iso-13485
  - operacion
  - procedimiento
---

PROTOCOLO DE VALIDACIÓN SOFTWARE










Función:
Elaborado por:
Revisado por:
Aprobado por:




Departamento:
Garantía de Calidad
Dirección
Garantía de Calidad


Nombre:
Esther Arnaiz
Carlos Zúñiga
Iván Pérez


Firma:





Fecha:
13/06/2024
13/06/2024
13/06/2024




# Contenido

[1. Introducción [3](#introducción)](#introducción)

[2. Alcance [3](#alcance)](#alcance)

[3. Definiciones [3](#definiciones)](#definiciones)

[4. Plan de validación [4](#plan-de-validación)](#plan-de-validación)

[4.1. Objetivos [4](#objetivos)](#objetivos)

[4.2. Métodos de validación
[4](#métodos-de-validación)](#métodos-de-validación)

[4.3. Criterios de aceptación
[4](#criterios-de-aceptación)](#criterios-de-aceptación)

[4.4. Criterios de re-validación
[4](#criterios-de-re-validación)](#criterios-de-re-validación)

[5. Procedimientos de validación
[5](#procedimientos-de-validación)](#procedimientos-de-validación)

[5.1. Cualificación de la instalación (IQ)
[5](#cualificación-de-la-instalación-iq)](#cualificación-de-la-instalación-iq)

[5.2. Cualificación de la operación (OQ)
[6](#cualificación-de-la-operación-oq)](#cualificación-de-la-operación-oq)

[5.3. Cualificación del funcionamiento (PQ)
[7](#cualificación-del-funcionamiento-pq)](#cualificación-del-funcionamiento-pq)

[6. Resultados y conclusiones
[7](#resultados-y-conclusiones)](#resultados-y-conclusiones)

[7. Histórico de versiones
[8](#histórico-de-versiones)](#histórico-de-versiones)

# Introducción

Este protocolo tiene como objetivo establecer un conjunto de directrices
y procedimientos para la validación del entorno de desarrollo utilizado
en el diseño y desarrollo del software creado por Spika Tech. Este
documento proporcionará una guía integral para asegurar que el entorno
de desarrollo cumple con los estándares de funcionalidad, confiabilidad
y seguridad necesarios para aplicaciones médicas críticas.

# Alcance

Este protocolo cubre la validación del entorno de desarrollo en términos
de funcionalidad, confiabilidad y seguridad en el contexto del
desarrollo del software médico.

Este protocolo abarca todos los aspectos de la validación de la
herramienta de desarrollo sofware empleada en Spika Tech, centrándose en
tres áreas clave: funcionalidad, confiabilidad y seguridad. Esto
incluye, pero no se limita a, la verificación de que todas las funciones
del entorno de desarrollo operan correctamente, que no se introducen
errores críticos durante el desarrollo del software, y que el entorno es
seguro frente a vulnerabilidades conocidas.

# Definiciones

Validación: Proceso de evaluar si un sistema o componente cumple
con los requisitos y funciona según lo previsto en su entorno operativo.

Cualificación de la Instalación (IQ): Verificación de que el
software y todos sus componentes se han instalado correctamente en el
entorno de destino.

Cualificación de la Operación (OQ): Confirmación de que el
software opera correctamente y que todas las funcionalidades y módulos
principales funcionan como se espera.

Cualificación del Funcionamiento (PQ): Aseguramiento de que el
software cumple con los requisitos específicos del negocio y opera según
los criterios de rendimiento y funcionalidad definidos por el usuario.

# Plan de validación

# Objetivos

El plan de validación establece los objetivos fundamentales para
garantizar que el entorno de desarrollo es adecuado para el desarrollo
del software elaborado en Spika, cumpliendo con altos estándares de
calidad y seguridad. Los objetivos específicos son:

-   Verificar la funcionalidad de la herramienta para desarrollar el
    software médico.

-   Asegurar que la herramienta no introduce errores críticos en el
    software.

-   Evaluar la seguridad y estabilidad del entorno de desarrollo

# Métodos de validación

Para cumplir con los objetivos de validación, se implementarán diversos
métodos de prueba que abarcan todos los aspectos críticos del desarrollo
del software:

-   Pruebas unitarias.

-   Pruebas de integración.

-   Pruebas de sistema.

-   Pruebas de aceptación de usuario.

# Criterios de aceptación

Los criterios de aceptación definen las condiciones que deben cumplirse
para considerar que la validación del entorno de desarrollo ha sido
exitosa:

-   Todas las pruebas deben ser exitosas sin errores críticos.

-   La seguridad del entorno debe estar garantizada sin vulnerabilidades
    conocidas.

# Criterios de re-validación

Tras la ejecución de una validación de la herramienta de desarrollo
software por parte de Spika, puede surgir la necesidad de volver a
validar dicha herramienta de desarrollo.

Será necesario realizar una re-validación completa del software cuando:

-   Se quiera comenzar a usar un software diferente al ya validado

-   Se actualice la versión del software empleado en una versión
    completa (por ejemplo, si se actualiza de una versión 2.x.x a una
    versión 3.x.x o superior)

Será necesario realizar una re-validación parcial del software cuando:

-   Se instale la misma versión de software en otro ordenar diferente al
    habitual o ya comprobado

-   Se actualice el software empleado a una versión parcial (por
    ejemplo, si se actualiza de una versión 2.3.19 a una versión 2.3.20)

En esta evaluación parcial sólo será necesario realizar las etapas de
cualificación de la operación (OQ) y cualificación del funcionamiento
(PQ), teniendo como objetivo comprobar las nuevas funcionalidades
indicadas en la nota de la actualización proporcionada por el
distribuidor del software.

# Procedimientos de validación

Este apartado describe los procedimientos necesarios para asegurar que
el software cumple con los requisitos especificados y funciona de manera
adecuada en el entorno de destino. Los procedimientos de validación se
dividen en tres etapas principales: cualificación de la instalación
(IQ), cualificación de la operación (OQ) y cualificación del
funcionamiento (PQ).

# Cualificación de la instalación (IQ)

Objetivo: Verificar que el software se ha instalado correctamente en el
entorno de destino y que todos los componentes necesarios están
presentes y en funcionamiento.

Procedimientos:

1.  Revisión de la documentación de instalación:

-   Verificar que se dispone de todos los manuales de instalación y
    guías de usuario.

-   Confirmar que se han seguido todos los pasos de instalación
    documentados.

1.  Comprobación de hardware y software:

-   Asegurar que el hardware en el que se instala el software cumple con
    las especificaciones mínimas requeridas.

-   Verificar la presencia y correcta configuración del sistema
    operativo y otros programas necesarios.

1.  Registro de la instalación:

-   Documentar el proceso de instalación, incluyendo fechas, personal
    responsable y cualquier incidencia ocurrida.

1.  Validación de integridad de archivos:

-   Verificar que todos los archivos del software están presentes

# Cualificación de la operación (OQ)

Objetivo: Confirmar que el software funciona correctamente en el entorno
de destino y que todos los módulos y funcionalidades principales operan
como se espera.

Procedimientos:

1.  Pruebas de funcionalidad básica:

-   Realizar pruebas para asegurar que las funcionalidades básicas del
    software están operativas.

-   Documentar los resultados de cada prueba, indicando si se han
    superado o no.

1.  Pruebas de integración:

-   Verificar que el software se integra correctamente con otros
    sistemas y aplicaciones que interactúan con él.

-   Probar la comunicación entre el software y bases de datos,
    servidores, u otros componentes de la infraestructura IT.

1.  Pruebas de rendimiento:

-   Ejecutar pruebas de rendimiento para asegurar que el software
    responde adecuadamente bajo condiciones normales y de alta carga.

-   Documentar tiempos de respuesta, utilización de recursos y cualquier
    problema de rendimiento observado.

1.  Verificación de seguridad:

-   Comprobar la correcta implementación de controles de acceso y
    medidas de seguridad.

# Cualificación del funcionamiento (PQ)

Objetivo: Asegurar que el software cumple con los requisitos específicos
de negocio y opera de acuerdo a los criterios de rendimiento y
funcionalidad definidos por el usuario.

Procedimientos:

1.  Pruebas de aceptación del usuario:

-   Involucrar a los usuarios finales para realizar pruebas en
    escenarios de uso real.

-   Recoger y documentar feedback de los usuarios, y realizar ajustes si
    es necesario.

1.  Pruebas de escenarios críticos:

-   Identificar y probar los escenarios críticos que son fundamentales
    para las operaciones del negocio.

-   Asegurar que el software maneja adecuadamente estos escenarios sin
    errores ni fallos.

1.  Evaluación de la documentación del usuario:

-   Verificar que la documentación del usuario está completa, es
    comprensible y proporciona toda la información necesaria para operar
    el software.

-   Asegurar que los manuales de usuario, guías de referencia y otros
    documentos están actualizados.

# Resultados y conclusiones

Este apartado presenta un resumen de los resultados obtenidos durante el
proceso de validación, así como las conclusiones derivadas de estos
resultados:

-   Resumen de resultados: detallar los hallazgos de cada fase de
    validación (IQ, OQ, PQ), incluyendo cualquier problema detectado,
    acciones correctivas tomadas y el estado final de cada prueba.

-   Conclusiones generales: evaluar si el entorno de desarrollo cumple
    con los objetivos de validación establecidos, asegurando que es
    adecuado para el desarrollo del software elaborado en Spika Tech.

-   Decisión de aceptación: indicar si el entorno de desarrollo ha sido
    aceptado para su uso en la creación del software elaborado en
    SpikaTech, justificando esta decisión con los datos recopilados
    durante el proceso de validación.

# Histórico de versiones









**VERSION**
**MOTIVO DEL CAMBIO**
**FECHA**




01
Edición inicial
Junio 2024