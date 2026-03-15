DISEÑO Y DESARROLLO

| Función: | Elaborado por: | Revisado por: | Aprobado por: |
|---------------|---------------------|---------------------------|---------------------|
| Departamento: | Garantía de Calidad | Sistemas y ciberseguridad | Garantía de Calidad |
| Nombre: | Iván Pérez | David Pozo | Fernando Pozo |
| Firma: | | | |
| Fecha: | | | |

| Valido hasta: | 02/06/2028 |
|---------------|------------|

| **HISTORIAL DEL DOCUMENTO** | | | |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------|------------------------------------|
| **VERSIÓN** | **CAUSAS DE LA MODIFICACIÓN** | **FECHA ENTRADA EN VIGOR** | **SUSTITUYE A (CÓDIGO, REVISIÓN)** |
| 01 | Edicion inicial | 22/02/2024 | N/A |
| 02 | Reescritura del procedimiento para ajustarse con la realidad del proceso de diseño de SPIKA TECH, segun AC-045/24 | 10/05/2024 | PNT-026.01 |
| 03 | Definición de copias de seguridad | 15/07/2024 | PNT-026.02 |
| 04 | Expecificación de los tipos de cambios en el diseño, cambio en los departamentos de Spika | 02/06/2025 | PNT-027.03 |

# Contenido

[1. Objetivo [4](#objetivo)](#objetivo)

[2. Alcance [4](#alcance)](#alcance)

[3. Responsabilidades y Departamentos afectados
[4](#responsabilidades-y-departamentos-afectados)](#responsabilidades-y-departamentos-afectados)

[4. Definiciones y Acrónimos
[5](#definiciones-y-acrónimos)](#definiciones-y-acrónimos)

[5. Procedimiento [6](#procedimiento)](#procedimiento)

[5.1. Reuniones de seguimiento del diseño y desarrollo del producto
[7](#reuniones-de-seguimiento-del-diseño-y-desarrollo-del-producto)](#reuniones-de-seguimiento-del-diseño-y-desarrollo-del-producto)

[5.2. Fase de investigación
[7](#fase-de-investigación)](#fase-de-investigación)

[5.3. Fase de control de diseño
[7](#fase-de-control-de-diseño)](#fase-de-control-de-diseño)

[5.4. Fase de entrada de diseño (Design Input)
[8](#fase-de-entrada-de-diseño-design-input)](#fase-de-entrada-de-diseño-design-input)

[5.4.1. Alcance de la entrada del diseño
[9](#alcance-de-la-entrada-del-diseño)](#alcance-de-la-entrada-del-diseño)

[5.4.2. Evaluación de la adecuación
[9](#evaluación-de-la-adecuación)](#evaluación-de-la-adecuación)

[5.4.3. Codificación [9](#codificación)](#codificación)

[5.5. Validación y verificación del diseño (Design output)
[9](#validación-y-verificación-del-diseño-design-output)](#validación-y-verificación-del-diseño-design-output)

[5.6. Fase de transferencia del diseño
[10](#fase-de-transferencia-del-diseño)](#fase-de-transferencia-del-diseño)

[5.7. Cambios en el diseño
[10](#cambios-en-el-diseño)](#cambios-en-el-diseño)

[5.8. Análisis de Riesgos
[12](#análisis-de-riesgos)](#análisis-de-riesgos)

[5.9. Copias de seguridad
[12](#copias-de-seguridad)](#copias-de-seguridad)

[5.9.1. Frecuencia de copias de seguridad
[12](#frecuencia-de-copias-de-seguridad)](#frecuencia-de-copias-de-seguridad)

[5.9.2. Método de copias de seguridad
[12](#método-de-copias-de-seguridad)](#método-de-copias-de-seguridad)

[5.9.3. Verificación y restauración
[12](#verificación-y-restauración)](#verificación-y-restauración)

[5.10. Etiquetado y acondicionamiento del producto
[12](#etiquetado-y-acondicionamiento-del-producto)](#etiquetado-y-acondicionamiento-del-producto)

[5.11. Fichero histórico de diseño
[13](#fichero-histórico-de-diseño)](#fichero-histórico-de-diseño)

[6. Distribución del Procedimiento
[13](#distribución-del-procedimiento)](#distribución-del-procedimiento)

[7. Anexos [13](#anexos)](#anexos)

[8. Documentación relacionada
[13](#documentación-relacionada)](#documentación-relacionada)

[9. Formación [14](#formación)](#formación)

# Objetivo

El presente procedimiento describe el proceso seguido por Spika Tech, en
adelante SPIKA, para indicar como han de gestionarse los requerimientos
de calidad relativos al Diseño y Desarrollo de productos, de modo que se
asegure el cumplimiento de los requerimientos específicos de diseño
(internos y reglamentarios), y que la transferencia al proceso
productivo real sea adecuada al uso intencionado del producto. La
documentación de todas las etapas del proceso asegurará la adecuada
trazabilidad de los datos, la definición de la responsabilidad y
disponibilidad de los recursos necesarios.

# Alcance

El presente procedimiento aplica a las etapas de diseño y desarrollo de
productos desarrollados y distribuidos por SPIKA.

Este procedimiento aplica tanto al diseño de nuevos productos como a la
modificación de los ya existentes

# Responsabilidades y Departamentos afectados

Será responsabilidad del Técnico Responsable la supervisión del sistema
de diseño y asegurar que la realización de producto es posible, y se
realiza de acuerdo al sistema de calidad implementado.

El departamento de operaciones será el responsable de liderar el proceso
de diseño y desarrollo en correcta coordinación con el resto de
departamentos o personal que aplique, y todo ello en consonancia con el
sistema de calidad instaurado.

Los departamentos afectados son los señalados en la siguiente tabla:

| Departamento | Aplica | |
|----------------------------|--------|-----|
| | Si | No |
| Dirección | ☒ | ☐ |
| Medio ambiente | ☒ | ☐ |
| Garantía de Calidad | ☒ | ☐ |
| Sistemas y Ciberseguridad | ☒ | ☐ |
| Investigación y Desarrollo | ☒ | ☐ |
| Marketing y Ventas | ☒ | ☐ |
| Gestión | ☒ | ☐ |

# 

# Definiciones y Acrónimos

- Diseño y desarrollo: Proceso que asegura la correcta
 transferencia desde los requisitos iniciales definidos de un producto
 hasta sus características finales o especificaciones.

- Entrada del diseño: requerimiento que ha de cumplir un producto
 para empezar el proceso de diseño

- Salida de diseño: resultado del proceso de diseño de un
 producto que establece las características que cumple
 (especificaciones).

- Incidencia (Jira): cabe destacar que Jira emplea el termino
 incidencia para denominar una tarea que conlleva un diseño (si
 aplica) y un desarrollo (si aplica) lo cual debe distinguirse de una
 incidencia real, de acuerdo, a las definiciones del PNT004 Gestion de
 no conformidades.

# Procedimiento

El proceso de diseño tiene diferentes fases que desembocan en la
consecución del producto final, como se muestra en el siguiente
diagrama:


style="width:4.24423in;height:3.80833in"
alt="Interfaz de usuario gráfica Descripción generada automáticamente" />

# Reuniones de seguimiento del diseño y desarrollo del producto

Durante todo el proceso de diseño y desarrollo del producto se realizan
reuniones de seguimiento en las que se revisa lo eleborado por todos los
equipos de trabajo que conforman SPIKA y se dictan las pautas para
continuar con el desarrollo del producto.

# Fase de investigación

Esta fase se considera una fase de investigación temprana que no
requiere de registro formal documental de acuerdo al sistema de calidad
de la organización. Se podrán generar registros en cuadernos de
laboratorio/similar, pero no se requiere de los elementos exigidos por
el sistema de calidad.

# Fase de control de diseño

El departamento de operaciones elaborará un informe/plan de control de
diseño, que será debidamente documentado, asegure el control apropiado
del proceso de diseño y desarrollo, y cumpliendo los objetivos de
calidad establecidos.

Todo el plan de control de diseño del producto desarrollado en SPIKA se
almacena en un tablero online de la herramienta Jira:

(&lt;https://spikatech.atlassian.net/jira/software/c/projects/VRC/boards/32?assignee=63c51264d7f68827e6b55719&assignee=63be96382a526608c54ff184&assignee=62a997d93eb34d00685f176d&assignee=632082c8ed8abffd7ffc9b4d&assignee=712020%3Acdc726be-ff96-453e-82e6-1efc1a3b1447&assignee=6310bdf3316bbc56c424972d&assignee=633a86d1f568615bdc7fbd5c&assignee=712020%3A095a3094-46f9-4e78-831d-e57b9ce328b2&assignee=712020%3Ace5b65be-8481-4065-bec3-61d9789428cd&assignee=63a03e026f068efec8f48577&assignee=70121%3A191eeba2-ab1f-4a53-be51-3b9fb48bfe89&assignee=642ae918f1f740eb291ef12a&assignee=6364da49fc0cc7a600b11a73&assignee=712020%3A974baa9e-d7d0-418e-a169-b4ac97d78cb0&assignee=70121%3Aec60de9c-c393-461d-b55d-71eb70530b50&assignee=63da2b4928cddcc70770ca2b&assignee=631713743e578bb3b5ffb524&assignee=712020%3Ac713154d-2fda-46cc-9d57-d5b0429f4b42>),
que ayuda a la organización y la gestión del desarrollo, además de la
**medición de todos los procesos** de desarrollo que se llevan a cabo
dentro de SPIKA gracias al registro de todas las tareas que se han
realizado y los informes generados automáticamente a partir de estas
tareas.

El primer paso a realizar por el departamento de desarrollo, es la
creación de una incidencia (una tarea que conlleva un diseño (si aplica)
y un desarrollo (si aplica)) dentro del producto desarrollado en SPIKA.

Dicha incidencia cumple con la resolución de una necesidad de usuario
identificada o una mejora identificada por el departamento de
desarrollo.

Estas incidencias quedan documentadas de la siguiente manera:

- Nombre de la incidencia.

- Descripción de la incidencia: descripción detallada del problema que
 se va a solucionar o función que se va a diseñar y desarrollar.

- Criterios de aceptación: esbozan los requisitos y límites esenciales
 para el desarrollo de una función. Incluyen una lista de comprobación
 específica y cuantificable que abarca aspectos funcionales y no
 funcionales, orientando el desarrollo y las pruebas. Estos criterios
 son fundamentales para alinear las expectativas del equipo y
 garantizar que una función cumpla los objetivos previstos con
 eficacia.

- Persona asignada: persona encargada del desarrollo descrito en la
 incidencia.

- Informador: persona responsable del seguimiento, verificación y
 validación del desarrollo descrito en la incidencia.

- Prioridad: orden de prioridad que se le va a dar a dicha incidencia
 dentro del proceso de desarrollo.

Requerimientos de Usuario:

El análisis de las necesidades de los potenciales usuarios del producto
será evaluado como paso previo a la iniciación del proceso de desarrollo
y diseño. Los requerimientos de usuario se registrarán en el tablero de
Jira, correspondiendo una incidencia con un posible requerimiento de
usuario.

# Fase de entrada de diseño (Design Input)

La fase de entrada de diseño se realiza para trasladar los
requerimientos de usuario (y otros como pueden ser técnicos,
funcionales, regulatorios) en una serie de requerimientos que deben ser
validados previo a implementación y progreso hacia la siguiente fase
(fase de validación y verificación (design output)).

Los requerimientos de entrada de diseño se registrarán como se ha
especificado en el punto anterior mediante la creación de incidencias en
la herramienta online Jira.

# Alcance de la entrada del diseño

El alcance del diseño se determina a través de la descripción minuciosa
de cada incidencia en la herramienta Jira, donde se ofrece una
explicación detallada del proceso que se llevará a cabo, incluyendo su
impacto previsto en el producto final. Esta descripción exhaustiva
garantiza una comprensión clara y completa de las tareas a realizar y
sus implicaciones en el resultado deseado.

# Evaluación de la adecuación 

La revisión de la idoneidad de los requisitos de entrada para el diseño
implica que el informador designado de la incidencia en la herramientra
Jira analiza minuciosamente los criterios de aceptación establecidos en
la descripción de la incidencia correspondiente. Este proceso asegura
que los requisitos del diseño se ajusten adecuadamente a las necesidades
y expectativas del proyecto, validando así su alineación con los
objetivos específicos delineados en la incidencia. Mediante esta
revisión rigurosa, se garantiza la coherencia y calidad del trabajo
realizado, y se minimiza la posibilidad de desviaciones o discrepancias
que puedan surgir durante el desarrollo del producto.

# Codificación 

Los requerimientos de entrada se codificarán como **AAA-xxx**, donde:

- “**AAA**”: se refiere a las siglas del producto que se está
 desarrollando.

- “**xxx**”: es un número correlativo que comienza en 01.

# Validación y verificación del diseño (Design output)

La fase de validación y verificación asegurará que el producto cumple
con los requerimientos de usuario y su uso intencionado. Esta fase se
asegurará que lo desarrollado funciona correctamnete, para ello, el
equipo desarrollador de la incidencia la marcará como “test” para que la
persona asignada pueda verificar su correcta implantación y
funcionalidad para poder pasar lo desarrollado al software general.

# Fase de transferencia del diseño

Durante esta fase se produce la transferencia al proceso productivo. Al
llegar hasta este punto, se da por seguro que la incidencia se ha
resuelto de forma correcta, de forma que el desarrollo se ha llevado a
cabo con éxito y el “qa” de la incidencia se ha encargado de verificar y
validar el correcto funcionamiento del nuevo desarrollo.

Dado esto, se transfiere la rama de trabajo del nuevo desarrollo a la
rama del proceso productivo mediante las herramientas de transferencia y
fusionado proporcionadas por el lugar de gestión de repositorios y
proyectos usado por SPIKA (Github).

# Cambios en el diseño

Los cambios en el diseño pueden producirse durante cualquier etapa del
desarrollo, y pueden ser de origen interno o externo;

- Cambios de origen interno: debidos a no cumplimiento de
 especificaciones, investigaciones de quejas, procesos de mejora, etc.

- Cambios de origen externo: debidos a comunicaciones de cliente,
 funcionamiento, seguimiento poscomercialización, publicaciones
 científicas, modificación de requerimientos reglamentarios, fallos en
 el funcionamiento, sugerencias de mejora, etc.

Todos los cambios asociados al proceso de control de diseño y
desarrollo, una vez todo este proceso de diseño y desarrollo se de por
finalizado y se consiga una versión definitiva del producto se
gestionarán de acuerdo al procedimiento de **PNT-005 Gestión de
controles de cambios**.

Dentro del producto, los cambios se clasifican como “Major”, “Minor” o
“Patch”, basándose en su impacto y los siguientes requisitos:

**1. Cambio Major:**

Corresponde a modificaciones significativas que afectan las
funcionalidades principales, la arquitectura, el diseño o el alcance
general del sistema/proyecto. Este tipo de cambio requiere un enfoque
exhaustivo para garantizar la calidad y el cumplimiento:

- Requisitos:

 - Comprobación de funcionalidad: Se debe verificar nuevamente que
 todas las funcionalidades del producto operen correctamente y
 conforme a los requisitos especificados.

 - Análisis de riesgos: Es imprescindible evaluar los riesgos asociados
 al cambio y actualizar los análisis existentes para mitigar posibles
 impactos.

 - Evaluación del cumplimiento reglamentario: Confirmar que el producto
 sigue cumpliendo las normativas aplicables, ya que estos cambios
 podrían afectar la conformidad.

- Impacto en la versión del producto: Incrementa el primer número de la
 versión del producto. (Ejemplo: de 1.0.0 a 2.0.0).

**2. Cambio Minor:**

Incluye modificaciones menores que afectan funcionalidades existentes,
pero sin alterar significativamente el comportamiento general del
sistema. Estos cambios tienen un impacto más limitado y requieren una
evaluación enfocada:

- Requisitos:

 - Comprobación de funcionalidad: Validar que las funcionalidades
 ajustadas o modificadas operen correctamente y que no haya
 afectaciones colaterales.

 - Análisis de riesgos: Revisar si el cambio introduce nuevos riesgos o
 afecta los existentes, y actualizar la documentación
 correspondiente.

- Impacto en la versión del producto: Incrementa el segundo número de la
 versión del producto. (Ejemplo: de 1.0.0 a 1.1.0).

**3. Cambio Patch:**

Comprende modificaciones enfocadas exclusivamente en corregir errores o
problemas específicos sin alterar la funcionalidad del sistema ni su
comportamiento general:

- Requisitos:

 - Comprobación de funcionalidad: Validar que el error corregido esté
 resuelto y que las áreas afectadas funcionen adecuadamente. No se
 requiere un análisis exhaustivo fuera del ámbito del cambio.

- Impacto en la versión del producto: Incrementa el tercer número de la
 versión del producto. (Ejemplo: de 1.0.0 a 1.0.1).

# Análisis de Riesgos

Los análisis de riesgos que pudieran generarse cuando sea necesario por
las características del producto, o del proceso productivo, tendrán en
cuenta el uso intencionado del mismo y seguirán principalmente el método
FMEA (Failure Mode and Effects Analysis), y según los principios en el
procedimiento PNT-002 Gestión de Riesgos. El análisis de riesgos
contemplará todas las etapas del proceso de diseño y desarrollo (plan,
entrada de diseño, salida de diseño, verificación, validación y
transferencia del diseño).

# Copias de seguridad

# Frecuencia de copias de seguridad

Las copias de seguridad del código fuente y de los datos almacenados en
la base de datos deben guardarse de forma segura, siguiendo un
procedimiento riguroso. Se recomienda que estas copias se realicen
diariamente a las 4:00 pm, asegurando que tanto el código como los datos
estén protegidos contra posibles pérdidas o fallos. Además, es esencial
almacenar las copias de seguridad en ubicaciones seguras y redundantes
para garantizar la recuperación de la información en caso de
emergencias.

# Método de copias de seguridad

El método de realización de estas copias de seguridad debe ser
automatizado para evitar errores humanos y asegurar que se realicen
diariamente sin falta. Las copias de seguridad se almacenan en la base
de datos alojada en el servicio de Google Firebase, garantizando tanto
la seguridad como la disponibilidad de los datos.

# Verificación y restauración

En caso de fallo o pérdida del código fuente, se accederá a la última
copia de seguridad realizada. Antes de restaurar dicha copia, es
necesario realizar un análisis exhaustivo para asegurar su correcto
funcionamiento. Este análisis garantiza que la copia a restaurar esté
libre de errores y sea completamente operativa, minimizando así el
riesgo de problemas adicionales.

# Etiquetado y acondicionamiento del producto

La información recopilada durante el proceso de diseño determinará el
etiquetado y redacción de las instrucciones de uso del producto según el
fichero histórico de diseño

# Fichero histórico de diseño

El histórico de diseño del equipo (DHF, Design History File) contendrá
los registros asociados a los requerimientos internos y externos de
diseño, verificación, validación y transferencia del diseño, actas de
reuniones del equipo de revisión, y toda la documentación técnica
aplicable.

Este histórico de diseño se podrá encontrar en el software de Jira en la
visualización de todas las incidencias asociadas a un proyecto.

# Distribución del Procedimiento

El personal perteneciente a los departamentos indicados en el Apartado 3
(Responsabilidades y Departamentos afectados), se les debe proporcionar
copia del presente procedimiento. Además, la copia controlada nº1 será
entregada al Archivo para su archivo en papel.

Copias controladas a emitir:

| **Nº Copia controlada** | **Departamentos** |
|-------------------------|-------------------|
| 1 | Archivo |

# 

# Anexos

| **NÚM. / REV.** | **TÍTULO** |
|-----------------|---------------------------|
| 1/01 | Requerimientos de usuario |

# 

# Documentación relacionada

| **Código** | **TÍTULO** |
|------------|-------------------------------------------------------|
| N/A | EN ISO 13485 (4.2.3 Archivo de producto sanitario) |
| N/A | Reglamento UE 2017/745 sobre los productos sanitarios |
| PNT-002 | Gestion de Riesgos |
| PNT-005 | Gestion de Controles de Cambios |

# 

# Formación

La presente versión requiere que los departamentos afectados indicados
en el apartado 3 reciban la formación que a continuación se indica:

| **Marcar con una X** | **Tipo formación** |
|----------------------|----------------------------------------------------------------------------------------------------------|
| ☒ | **Teórica** (lectura y comprensión del procedimiento) |
| ☐ | **Teórico – Práctica** (En caso de seleccionar esta opción, contactar con el Técnico Responsable) |