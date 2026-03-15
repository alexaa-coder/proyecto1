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

CICLO DE VIDA DE DESARROLLO DE SISTEMAS INFORMATIZADOS (SDLC)










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
02/06/2028















**HISTORIAL DEL DOCUMENTO**




**VERSIÓN**
**CAUSAS DE LA MODIFICACIÓN**
**FECHA entrada en Vigor**
**SUSTITUYE A (CÓDIGO, REVISIÓN)**


01
Edicion inicial
22/02/2024
N/A


02
Cambio en los departamentos de Spika
02/06/2025
PNT-027.01




# Contenido

[1. Objetivo [4](#objetivo)](#objetivo)

[2. Alcance [4](#alcance)](#alcance)

[3. Responsabilidades y Departamentos afectados
[4](#responsabilidades-y-departamentos-afectados)](#responsabilidades-y-departamentos-afectados)

[4. Definiciones y Acrónimos
[5](#definiciones-y-acrónimos)](#definiciones-y-acrónimos)

[5. Procedimiento [5](#procedimiento)](#procedimiento)

[5.1. Generalidades [5](#generalidades)](#generalidades)

[5.2. Clasificación del software
[7](#clasificación-del-software)](#clasificación-del-software)

[5.3. Planificación [10](#planificación)](#planificación)

[5.3.1. Análisis de los requisitos del software.
[10](#análisis-de-los-requisitos-del-software.)](#análisis-de-los-requisitos-del-software.)

[5.4. Diseño [11](#diseño)](#diseño)

[5.5. Construcción y codificación
[12](#construcción-y-codificación)](#construcción-y-codificación)

[5.6. Pruebas [12](#pruebas)](#pruebas)

[5.7. Operación y Mantenimiento
[12](#operación-y-mantenimiento)](#operación-y-mantenimiento)

[5.7.1. Plan de mantenimiento
[13](#plan-de-mantenimiento)](#plan-de-mantenimiento)

[6. Distribución del Procedimiento
[13](#distribución-del-procedimiento)](#distribución-del-procedimiento)

[7. Anexos [14](#anexos)](#anexos)

[8. Documentación relacionada
[14](#documentación-relacionada)](#documentación-relacionada)

[9. Formación [14](#formación)](#formación)

[Clasificación de software
[15](#clasificación-de-software)](#clasificación-de-software)

# Objetivo

El objetivo del presente procedimiento es describir el proceso del Ciclo
de Vida de Desarrollo de Sistemas Informatizados, en adelante, SDLC, *en
inglés*, Software Development Lyfe Cycle, incluyendo el ciclo de vida de
validación de software, en Spika Tech, adelante SPIKA..

# Alcance

Este proceso SDLC se aplica al software desarrollad en Spika con el fin
de cumplir con las reglamentaciones aplicables a los productos
sanitarios, así como con los requisitos de los clientes, con la
finalidad, de que el usuario obtenga los requisitos planteados. De esta
manera dar conformidad al sistema de calidad de Spika.

#  Responsabilidades y Departamentos afectados

El departamento de investigación y desarrollo es el encargado de
gestionar y documentar el ciclo de vida de los sistemas desarrollado por
Spika.

El Técnico Responsable es el encargado de supervisar la gestión de los
documentos generados, así como custodiarlos y mantener las copias. Será
también el encargado de supervisar el cumplimiento de este
procedimiento.

Los departamentos afectados son:









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

-   Elemento software: cualquier parte identificable de un
    programa de ordenador, por ejemplo, código fuente, código objeto,
    código de control, datos de control, o un conjunto de estos
    elementos.

-   Liberación (reléase): versión particular de un elemento de
    configuración que es puesto a disposición para un propósito
    específico.

-   SDLC: Software Development Lyfe Cycle.

# Procedimiento

# Generalidades

Con este procedimiento se va a proporcionar controles sobre el ciclo de
vida del sistema y documentación del software, se pretenden controlar
los siguientes puntos:

-   Configuración

-   Controles de cambios

-   Control de las versiones

-   Retención de los registros

-   Gestión de la información

-   Gestión de las incidencias

-   Revisión periódica

-   Aprobación/liberación

En el siguiente esquema resume las fases del ciclo de vida:


style="width:6.69236in;height:3.70278in" /&gt;

La documentación que se genera deberá ser aprobado por un equipo que
incluya representante con conocimiento de la normativa regulatoria y un
representante de calidad, los cuales, deben revisar y aprobar las etapas
clave del proyecto.

La documentación que se utilizará para implementar el proceso SDLC podrá
ser la siguiente, siempre en función de la criticidad del producto:

-   **Plan de validación (PV):** incorporará los resultados de la
    evaluación de riesgos y las fases de la validación y su estrategia,
    hitos, roles y responsabilidades, asi como la clasificación de
    seguridad. En el plan se debe definir el modelo de ciclo de vida ode
    desarrollo de software que se va a seguir.

-   **Requerimientos de Usuario (URS):** describe los requisitos que el
    usuario necesita para resolver un problema o alcanzar los objetivos.

-   **Documentación de Diseño (DQ)**: el contenido del documento
    describe elementos tales como estructuras lógicas, de control, de
    los datos, mensajes de error, configuraciones del sistema,
    seguridades, etc…

-   **Cualificación de la Instalación (IQ):** Documenta las
    instrucciones de instalación, configuración y cualificación del
    hardware y software incluyendo software intermedio para demostrar
    que todos estos elementos pueden realizar las funciones requeridas
    por el software de aplicación.

-   **Entorno de pruebas:** este entorno separado del entorno de
    producción garantiza la independencia y estabilidad de los datos, en
    previsión de errores.

-   **Documentación de pruebas de validación:** se engloban de la
    siguiente manera, teniendo especial cuidado entre fases y respetando
    el orden de ejecución. Con las pruebas de validación bajo un
    protocolo debidamente aprobado antes de su ejecución por el equipo
    evaluador, se documentarán las actividades para demostrar los
    procesos, métodos y datos utilizados en la evaluación estructural y
    funcional del sistema.

El orden de ejecución será:

&gt; **à Cualificación de la Instalación (IQ)**
&gt;
&gt; **à Cualificación de la operación (OQ)**
&gt;
&gt; **à Cualificación del funcionamiento (PQ)**

-   **Instalación e implantación del sistema:** proporciona los detalles
    técnicos y las instrucciones de cómo se pone operativo el sistema.

-   **Instrucciones de uso**: Describe información con instrucciones
    para su uso y operación.

# Clasificación del software

En la fase de clasificación se debe identificar en función de la
seguridad del software conforme al riesgo de daño al paciente. Se
identificará si el software es de Clase de Seguridad A, B o C, de la
siguiente manera:








**CLASIFICACION**
**EFECTOS DEL DAÑO**




A
No puede contribuir a una situacion peligrosa


Puede contribuir a una situación peligrosa que no resulte en un
riesgo inaceptable tras considerar las medidas externas de control de
riesgos aplicadas.


B
Puede contribuir a una situacion peligrosa que resulte en un riesgo
inaceptable tras considerar las medidas externas de control de riesgos
aplicadas y el posible daño resultante es una lesión NO-SERIA.


C
Puedes contribuir a una situacion peligrosa que resulte en un riesgo
inaceptable tras considerar las medidas externas de control de los
riesgos y el posible daño resultante es una lesion SERIA.




A continuación, se muestra un diagrama de decisión para la clasificación
del software y durante la toma de requisitos y desarrollo de un software
se debe documentar la clasificación del mismo siguiendo el esquema y
argumentación incluidas en el **Anexo 1**, de no existir dicha
clasificación se tomará por defecto el Software como clase C, una vez
exista documentación suficiente podrá darse la clase que corresponde.

# Planificación 

En la fase de planificación se identifica el uso del sistema y la
documentación requerida para el SDLC. En este momento un estudio de
gestión de riesgos se puede utilizar para determinar el alcance y
extensión de las pruebas y documentación asociada. El alcance y
profundidad de las pruebas y fases podrán ser condensadas u omitidas
debidamente justificadas.

En esta fase se desarrollan los URS. Además, se deben tratar los
siguientes puntos:

-   Los procesos a usar en el desarrollo del sistema, procesos
    existentes o nuevos.

-   Los entregables, incluyendo la documentación a generar, actividades
    y tareas

-   Trazabilidad entre los requisitos del sistema, requisitos del
    software, ensayos del sistema del software y medidas de control del
    riesgo

-   Gestión de la configuración y cambio del software

-   Resolución de problemas del software para manejar problemas
    detectados en los productos y actividades de cada etapa del ciclo de
    vida.

# Análisis de los requisitos del software.

Para cada sistema software el fabricante debe definir y documentar los
requisitos del sistema, se deberán incluir los siguientes puntos:








REQUISITOS
DESCRIPCION/EJEMPLO




Requisitos funcionales y de capacidad
Funciones (propósito), características físicas (lenguaje de código,
plataforma, sistema operativo), entorno informático (hardware, tamaño de
memoria), necesidad de compatibilidad con mejoras.


Entradas y salidas
Caracterísitcas de los datos, rangos, límites y valores por
defecto.


Interfaces entre el sistema y otros sistemas
Si aplica


Alarmas
Advertencias y mensajes del operador conducidos por el software


Requisitos de seguridad
Autentificación, autorización, auditoria, integridad de la
comunicacion


Requisitos de ingeniería de aptitud al uso que son sensible a
errores y formación humana
Soporte para operaciones manuales, interacciones hombre-máquina,
coacción del personal y destacar áreas de atención de las personas


Requisitos de la definicion de datos y base de datos
Forma, adecuación y función


Requisitos de instalación y aceptación del software
N/A


Requisitos relativos a los métodos de funcionamiento y
mantenimiento
N/A


Documentación del usuario a ser desarrollada
Manual


Requisitos de mantenimiento del usuario
N/A


Requisitos reglamentarios
N/A




# Diseño

La fase de diseño incluye las especificaciones de diseño de software que
describen cómo el software debe funcionar, es decir, se deben convertir
los requisitos del software en arquitectura documentada que describa la
estructura del software e identifique sus elementos. La forma en que se
implantará, y como se puede mitigar los riesgos derivados, trazando los
requisitos de usuario con las funcionalidades del diseño elaboradas.

Se identificarán especificaciones de diseño relacionadas con:

-   Arquitectura del sistema: requisitos de hardware, software,
    comunicaciones, seguridad, etc…

-   Base de datos: representación lógica y física de las definiciones de
    datos, componentes críticos, seguridad y tamaño de las bases de
    datos.

-   Interfaces: incluyendo interfaces de uso, navegación y diseño de los
    informes.

# Construcción y codificación

En esta fase se implementa el diseño del sistema en código fuente y los
ajustes de configuración para su uso por el cliente final. Es deseable
que en esta fase se desarrollen los protocolos de ensayo y pruebas a
realizar para la verificación correcta del funcionamiento.

# Pruebas

En la fase de pruebas se verifica que el sistema funciona de acuerdo a
las especificaciones aprobadas, bajo un entorno de test. El fabricante
debe establecer y realizar un conjunto de ensayos con criterio de
pasa/falla de modo que se cubran todos los requisitos del software.

Las pruebas incluyen ejercicios en el software bajo condiciones
conocidas y resultados documentos. Todas las incidencias detectadas se
deben registrar, revisar y tratarse antes de la puesta en servicio del
producto. En este momento se harán uso del protocolo de cualificación de
diseño, de instalación, de operación y de funcionamiento.

Las pruebas se documentan con buen nivel de detalle evidenciando el
máximo valor de los datos posible a modo de pantallazos, por ejemplo, y
siempre identificando quien, y cuando se han realizado, así como un
listado de anomalías encontradas.

Si se realizarán cambios después de los ensayos, con el fin de corregir
errores/anomalías, se deben repetir ensayos, realizar ensayos
modificados o adicionales, según proceda, de la misma manera verificar
que no se han incluido efectos secundarios indeseables por un cambio y
cuando aplique revisar las actividades de gestión de riesgos
correspondiente.

# Operación y Mantenimiento

Durante la fase de operación y mantenimiento el software está en el
entorno de producción y todos los cambios a realizar deben gestionarse
bajo un sistema reglado de control de cambios, ver **PNT-005 Gestión de**
Control de Cambios.

Durante esta fase se producirá la **“liberación del software”**, donde
el fabricante debe asegurarse que se ha culminado la verificación del
mismo y que los resultados se han evaluado antes de la liberación. Debe
estar claramente indicada la versión del software que se está liberando.

El fabricante debe establecer procedimiento para asegurar que el
producto o software liberado puede ser suministrado en el punto del uso
sin deformación o cambios no autorizados. Estos procedimientos deben
tratar la producción y manejo de medio que contengan software incluyendo
cuando aplique los siguientes puntos:

-   Replicación

-   Etiquetado

-   Almacenamiento

-   Suministro

# Plan de mantenimiento

Se debe establecer un plan de mantenimiento del software para realizar
actividades y tareas del proceso de mantenimiento, en este plan se debe
tratar lo siguiente:

-   Procedimientos para: Recepción, documentación, evaluación,
    resolución y seguimiento.

-   Criterio para determinar si los retornos (véase reclamaciones) se
    consideran un problema, ver **PNT-007 Gestión de reclamaciones**

-   Uso del proceso de gestión de riesgos

-   Uso del proceso de resolución de problemas, véase **PNT-004 Gestión
    de no conformidades

-   Uso del proceso de gestión de la configuración

-   Procedimientos para mejoras, corrección de problemas, arreglos y
    obsolescencia.

De los retornos de información que ocurren después de la liberación.

En esta fase es esencial el plan de back-up o disaster recovery así como
el sistema de incidentes y seguimiento periódico.

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




# Anexos








**NÚM. / REV.**
**TÍTULO**




1/01
Clasificacion de software




# Documentación relacionada








**Código**
**TÍTULO**




N/A
ISO 13485


N/A
Reglamento 2017/745


N/A
UNE-EN 62304


SGC-004
Gestion de no conformidades


SGC-007
Gestion de reclamaciones




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




# 

**Anexo 1\_VERSION\_02**

# Clasificación de software











**CLASIFICACION DE SOFTWARE**




**EVALUACION DE LA SEGURIDAD**


**Descripcion**



**Uso previsto**



**Pregunta**
**Respuesta**
**Justificación**


**Si**
**No**


1. ¿El software puede producir un situacion peligrosa a causa de un
fallo del sistema?
☐
☐



2.El fallo del software resulta un riesgo inaceptable? (ver nota
1)
☐
☐



3.¿El fallo del software provoca una lesión NO SERIA? (ver nota
2)
☐
☐



4.¿El fallo del software provoca una lesion SERIA?
☐
☐





*NOTA 1: 2. Si responde que sí, continúe a punto 3.*

*NOTA 2: 3. Si response que sí, ha terminado el cuestionario, si
responde que no continúe a la pregunta 4.




**ANEXO 1/02**















**RESULTADO FINAL**
**A**
☐
**B**
☐
**C**
☐




**Jusificación:**



**Revisado por:**
Firma:
Fecha:


**Aprobado por:**
Firma:
Fecha: