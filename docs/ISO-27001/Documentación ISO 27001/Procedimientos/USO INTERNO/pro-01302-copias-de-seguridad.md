---
id: pro-013-02_copias-de-seguridad
title: "Pro 013.02 Copias De Seguridad"
sidebar_label: "Pro 013.02 Copias De Seguridad"
---

|Col1|PROCEDIMIENTO DE<br />COPIAS DE SEGURIDAD<br />Y RESPALDO|Código: PRO-013.02|
|---|---|---|
||<br />USO OFICIAL INTERNO<br />|<br />Fecha de vigor: 19/03/2025<br />|

# **PROCEDIMIENTO DE COPIAS DE** **SEGURIDAD Y RESPALDO**

|Col1|PROCEDIMIENTO DE<br />COPIAS DE SEGURIDAD<br />Y RESPALDO|Código: PRO-013.02|
|---|---|---|
||<br />USO OFICIAL INTERNO<br />|<br />Fecha de vigor: 19/03/2025<br />|

|HISTORIAL DEL DOCUMENTO|Col2|Col3|Col4|
|---|---|---|---|
|**Versión**|**Resumen de modificaciones**|**Fecha de**<br />**entrada**|**Sustituye a**<br />**(Código,**<br />**revisión)**|
|01|Primera versión del documento.|26/02/2025|N/A|
|02|Cambio de nombre del anexo II|19/03/2025|01|

|REGISTRO DE FIRMAS|Col2|Col3|Col4|
|---|---|---|---|
|**Función:**|**Elaborado por:**|**Revisado por:**|**Aprobado por:**|
|Departam<br />ento:|Responsable del SGSI|Dirección|Jefe de seguridad<br />(o suplente)|
|Nombre:|David Pozo|Carlos Rodrigo|Carlos Zúñiga|
|Firma:|<br />[FIRMA DIGITAL]<br />`SANCHEZ DAVID -`<br />` el día`<br />`19/03/2025`<br /> <br /> <br /><br /> <br />|<br />`Firmado por`<br />`RODRIGO RIVERO,`<br />`CARLOS`<br />`(AUTENTICACIÓN) el`<br />`día 19/03/2025 con`|<br />`Firmado por`<br />` CARLOS`<br />`ZUÑIGA (R:`<br />`****8690*) el día`<br />~~`19/03/2025 con un`~~|
|Fecha:|19/03/2025|19/03/2025|19/03/2025<br />|

|Col1|PROCEDIMIENTO DE<br />COPIAS DE SEGURIDAD<br />Y RESPALDO|Código: PRO-013.02|
|---|---|---|
||<br />USO OFICIAL INTERNO<br />|<br />Fecha de vigor: 19/03/2025<br />|

## **CONTENIDO**
1 OBJETIVO Y ÁMBITO DE APLICACIÓN
2 RESPONSABILIDADES
3 COPIAS DE RESPALDO
3.1 Tipos de copias de respaldo
3.2 Copias de respaldo de información de usuarios
3.3 Retención de Información
3.4 Prueba de copias de seguridad
3.5 Automatización del sistema de Backup
3.6 Almacenamiento y traslado de soportes
3.7 Período de retención de las Copias de respaldo
3.8 Control de acceso
4 GENERACIÓN DE COPIAS DE RESPALDO
4.1 Procedimiento de generación de copias de respaldo
4.1.1 Datos a guardar
4.1.2 Política de copias de seguridad
4.1.3 Procedimiento de verificación de copias de respaldo
5 PROCESO DE RECUPERACIÓN DE ACTIVOS A PARTIR DE COPIAS DE RESPALDO
5.1 Solicitud de Recuperación de Activos
5.2 Recuperación de Activos
6 COMPROBACIÓN PERIÓDICA DE LOS PROCEDIMIENTOS DE RESTAURACIÓN
6.1.1 Procedimiento de Comprobación
7 REFERENCIAS
8 ANEXO I: PLAZOS LEGALES DE RETENCIÓN
9 ANEXO II: PLAZOS ESTABLECIDOS DE RETENCIÓN

|Col1|PROCEDIMIENTO DE<br />COPIAS DE SEGURIDAD<br />Y RESPALDO|Código: PRO-013.02|
|---|---|---|
||<br />USO OFICIAL INTERNO<br />|<br />Fecha de vigor: 19/03/2025<br />|

## **1 OBJETIVO Y ÁMBITO DE APLICACIÓN**
Para garantizar la seguridad de los datos, además de procurar la confidencialidad de los mismos es preciso certificar su integridad y disponibilidad. Con el objetivo de asegurar estas
dos características fundamentales de la protección de la información, es preciso establecer procedimientos de respaldo y recuperación de los datos, para su puesta en funcionamiento
ante un eventual fallo del sistema.
El objeto del presente documento es la definición del Procedimiento aplicable a la Generación de Copias de Respaldo y Recuperación de la Información manejada por SPIKA TECH.
Este procedimiento se aplica en todos los sistemas de información que dan soporte a los servicios internos corporativos de SPIKA TECH, así como los servicios de infraestructura,
comunicaciones y puestos de trabajo que los soportan, debiendo ser conocida y cumplida por todo el personal involucrado en la operación y mantenimiento de estos.
## **2 RESPONSABILIDADES**
El área de IT, se responsabilizará de:
- Comprobar la correcta realización de las copias de seguridad de los Sistemas de
información.
- Las copias de seguridad y, en su caso, los soportes informáticos con datos de carácter
personal, se almacenarán en lugares debidamente protegidos.
- Las copias de respaldo y procedimientos de recuperación de datos críticos se
almacenarán en una ubicación diferente a la de los locales donde se encuentran las instalaciones.
## **3 COPIAS DE RESPALDO**
Toda la información de SPIKA TECH del ámbito de alcance de la norma ISO 27001 será periódicamente respaldada en soportes de backup. Las copias de respaldo deben abarcar
toda la información necesaria para recuperar el servicio en caso de corrupción o pérdida de la información. Tal información puede incluir datos, programas y ficheros de configuración.

|Col1|PROCEDIMIENTO DE<br />COPIAS DE SEGURIDAD<br />Y RESPALDO|Código: PRO-013.02|
|---|---|---|
||<br />USO OFICIAL INTERNO<br />|<br />Fecha de vigor: 19/03/2025<br />|

Para toda aquella información clasificada como “crítica y esencial” se definirán los estándares de respaldo, que incluirán, al menos la siguiente información:
- Periodicidad de las copias de respaldo.
- Periodos de retención de las copias.
- Ubicación de los soportes de respaldo, si fuera de aplicación.
- Procedimientos de recuperación de la información
- Procedimientos de inventario.
**3.1 Tipos de copias de respaldo**
**Completa**
Se efectúa una copia de seguridad completa de todos los ficheros y bases de datos. Puede consumir bastante tiempo si el volumen de datos a salvaguardar es elevado. La ventaja
derivada de este tipo de copia es que se tiene la seguridad de tener una imagen completa de los datos en el momento de la salvaguarda.
**Incremental**
Se copian los datos modificados desde la anterior copia incremental. Siempre se debe partir de una salvaguarda completa inicial. Si se realiza con frecuencia, el proceso no consumirá un
tiempo excesivo, debido al bajo volumen de datos a copiar. Por el contrario, la restauración es lenta, toda vez que requiere restaurar una copia completa y todas las copias incrementales
realizadas hasta el momento al que se quiera restaurar el sistema.
**3.2 Copias de respaldo de información de usuarios**
En ningún caso se deberán almacenar copias de respaldo en el domicilio del usuario o en dependencias de terceros ajenos a SPIKA TECH si no existe un acuerdo previamente suscrito
con el tercero en el que se prevea tal posibilidad y se expliciten las cautelas debidas respecto de la custodia de la información almacenada.
**3.3 Retención de Información**
Los documentos originales y los ficheros en formato electrónico deben ser retenidos durante el tiempo que en cada caso el ordenamiento jurídico prescriba.

|Col1|PROCEDIMIENTO DE<br />COPIAS DE SEGURIDAD<br />Y RESPALDO|Código: PRO-013.02|
|---|---|---|
||<br />USO OFICIAL INTERNO<br />|<br />Fecha de vigor: 19/03/2025<br />|

Cuando la información de SPIKA TECH deje de ser necesaria, deberá ser destruida o eliminada de manera segura. Para dar soporte a este requisito, los responsables funcionales
de los sistemas de información de SPIKA TECH deberán revisar, de forma periódica, el valor y la utilidad de la información almacenada.
Todos los datos almacenados en soportes de información que se desechen serán eliminados según un procedimiento definido a tal efecto, que asegure los objetivos de seguridad para la
información de los citados soportes. En este sentido, se deberá tener especial cuidado con respecto a la información almacenada en servidores o estaciones de trabajo, el software
licenciado o desarrollado a medida y los elementos que recibirán mantenimiento dentro de SPIKA TECH por usuarios que no tengan permiso permanente de acceso a los mismos.
**3.4 Prueba de copias de seguridad**
La información del ámbito de aplicación de la ISO 27001 almacenada en un medio informático durante un período prolongado de tiempo, deberá ser verificada al menos una vez al año, para
asegurar que la información es recuperable.
La realización de las pruebas de restauración de las copias de respaldo confirmará el funcionamiento correcto del proceso de recuperación de copias de datos, y garantizará la
integridad de los datos que contienen.
Se establecerán pruebas respecto a la restauración de las copias de respaldo, de forma rotativa y con una periodicidad previamente establecida. Las pruebas y los resultados deberán
estar convenientemente documentados y, como consecuencia de las mismas, se subsanarán las incidencias que se hayan puesto de manifiesto durante su desarrollo.
Además, cuando se traten ficheros que contengan datos de carácter personal, el Responsable del Fichero deberá verificar la correcta definición, funcionamiento y aplicación de los
procedimientos de realización de copias de respaldo y recuperación.
**3.5 Automatización del sistema de Backup**
Siempre que sea posible, los backups se deben automatizar. La automatización de los procedimientos de backup reducirán la posibilidad de omitir ciclos de respaldo o que éstos
sean erróneos. La programación periódica de las copias de respaldo se debe efectuar a través de un sistema de administración de soportes.

|Col1|PROCEDIMIENTO DE<br />COPIAS DE SEGURIDAD<br />Y RESPALDO|Código: PRO-013.02|
|---|---|---|
||<br />USO OFICIAL INTERNO<br />|<br />Fecha de vigor: 19/03/2025<br />|

**3.6 Almacenamiento y traslado de soportes**
El traslado de los soportes se encuentra regulado en el **Procedimiento de entrada y salida**
**de soportes de información** .
**3.7 Período de retención de las Copias de respaldo**
El establecimiento de un período de existencia de las copias de respaldo, de acuerdo con el ordenamiento jurídico vigente en cada momento, facilitará la salvaguarda de estas, el
cumplimiento legal y el uso eficiente del espacio físico disponible para el almacenamiento. Se deberá establecer el período de existencia para las copias de seguridad y los procedimientos
a seguir para proceder a su eliminación.
**3.8 Control de acceso**
Solo podrán acceder a las copias de seguridad aquellas personas habilitadas y con acceso para ello.
## **4 GENERACIÓN DE COPIAS DE RESPALDO**
**4.1 Procedimiento de generación de copias de respaldo**
SPIKA TECH dispone de un listado de información sobre los que ejecutar las copias de respaldo.
**4.1.1 Datos a guardar**
El área de IT mantendrá un inventario de los activos sobre los que se realiza copia de seguridad en el Registro de Activos sujetos a Copia de Respaldo. A modo de resumen, se
copian las máquinas virtuales que dan servicio a las aplicaciones de negocio, volúmenes de ficheros, bases de datos, aplicaciones en nube (OneDrive Y Outlook) y los servidores que
mantienen la infraestructura de SPIKA TECH.
**4.1.2 Política de copias de seguridad**
Actualmente se dispone de tres tipos de políticas de tiempo. Se distinguen, por otro lado, según el tipo de información y su grado de criticidad:

|Col1|PROCEDIMIENTO DE<br />COPIAS DE SEGURIDAD<br />Y RESPALDO|Código: PRO-013.02|
|---|---|---|
||<br />USO OFICIAL INTERNO<br />|<br />Fecha de vigor: 19/03/2025<br />|

- Backup diario: copia incremental o completa de datos críticos de la compañía.
- Backup mensual: copia completa de todos los datos críticos o de riesgo de SPIKA
TECH.
- Back up bianual: copia completa de todos los datos relevantes de SPIKA TECH.
**4.1.3 Procedimiento de verificación de copias de respaldo**
La herramienta de generación de copias de respaldo (en caso de que aplique) de SPIKA TECH contará con un sistema automático de verificación de copias, en caso de que el proceso
esté automatizado. Este sistema, que se mantendrá permanentemente activado, verificará las copias de respaldo una vez generadas y almacenará el resultado de la operación en el registro
del sistema.
Se comprueba mensual el registro del sistema, al objeto de garantizar la correcta ejecución de las operaciones de copia de respaldo. En caso de detectar un fallo en el proceso de
generación, se investiga, resuelve la incidencia y relanza la tarea de copia.
Además, en caso de detección de error en el proceso de copia de seguridad, el sistema envía una alerta al usuario que le avisa de la incidencia.
## **5 PROCESO DE RECUPERACIÓN DE ACTIVOS A PARTIR DE COPIAS** **DE RESPALDO**
**5.1 Solicitud de Recuperación de Activos**
Bajo petición del usuario y responsable del activo se podrá realizar una petición de recuperaciones de activos a partir de copias de respaldo.
**5.2 Recuperación de Activos**
Se accede a la herramienta donde residen las copias de respaldo respecto del activo a recuperar y lo restaura en el servidor correspondiente. Una vez restaurada la información,
informa al responsable del activo sobre la ubicación de la información.

|Col1|PROCEDIMIENTO DE<br />COPIAS DE SEGURIDAD<br />Y RESPALDO|Código: PRO-013.02|
|---|---|---|
||<br />USO OFICIAL INTERNO<br />|<br />Fecha de vigor: 19/03/2025<br />|

## **6 COMPROBACIÓN PERIÓDICA DE LOS PROCEDIMIENTOS DE** **RESTAURACIÓN**
Para garantizar la eficacia de los procedimientos de restauración de SPIKA TECH y la capacidad para recuperar los activos desde las copias de respaldo, se establece el
procedimiento de comprobación periódica que se detalla a continuación.
**6.1.1 Procedimiento de Comprobación**
Con el fin de verificar la validez de las copias para asegurar la continuidad del negocio, mensualmente se hacen pruebas de recuperación de la información clasificada como crítica
para SPIKA TECH.
Los registros de recuperación son generados por la herramienta de gestión de copias de seguridad implementada por SPIKA TECH. Este registro almacena el log de la herramienta
de generación de copias con el resultado de la operación de restauración.
## **7 REFERENCIAS**
- ISO/ IEC 27001:2022:
`o` 8.13 Copias de seguridad de la información.
`o` 8.14 Redundancia de los recursos de tratamiento de la información.
`o` 7.14 Eliminación o reutilización segura o de equipos.
`o` 7.10 Soportes de almacenamiento.
`o` 5.37 Documentación de procedimientos operacionales.
`o` 5.29 Seguridad de la información durante la interrupción.
`o` 5.30 Preparación para las TIC para continuidad de negocio.
`o` 5.31 Identificación de requisitos legales, reglamentarios y contractuales.

|Col1|PROCEDIMIENTO DE<br />COPIAS DE SEGURIDAD<br />Y RESPALDO|Código: PRO-013.02|
|---|---|---|
||<br />USO OFICIAL INTERNO<br />|<br />Fecha de vigor: 19/03/2025<br />|

## **8 ANEXO I: PLAZOS LEGALES DE RETENCIÓN**
Los periodos de retención de las copias de seguridad deben cumplir tanto con las necesidades operativas de la organización como con los requisitos legales de conservación de datos que
varían según el tipo de información. En función de las normativas aplicables (como la normativa de protección de datos, legislación fiscal, normativa laboral, entre otras), los plazos
pueden variar considerablemente.
A continuación, se detallan algunos de los plazos legales de conservación de datos más relevantes y su impacto en las copias de seguridad:

|Tipo de información|Precepto legal|Plazo de conservación|
|---|---|---|
|Documentación<br />fiscal<br />y <br />contable|Art. 66 Ley 58/2003 (Ley<br />General Tributaria)|Al menos 4 años (ampliable a 5 -<br />6 años para cubrir posibles<br />retrasos<br />en<br />auditorías<br />o <br />inspecciones fiscales).|
|Documentación<br />de<br />la<br />Seguridad Social|Art. 4 RD Legislativo<br />5/2000|4 años.|
|Documentación en materia de<br />prevención<br />de<br />riesgos<br />laborales|Art. 4 RD Legislativo<br />5/2000|5 años.|
|Documentación mercantil y<br />societaria|Art.<br />30.1<br />Código<br />de<br />Comercio|Al menos 6 años a partir del<br />último<br />asiento<br />realizado<br />(ampliable hasta 10 años para<br />fines históricos o para cumplir<br />con otras normativas).|
|Prevención de blanqueo de<br />capitales y financiación del<br />terrorismo|Art. 25 de la Ley 10/2010|10 años.|
|Documentación<br />relacionada<br />con contratos|Art. 63 Ley 9/2017 (Ley de<br />Contratos<br />del<br />Sector<br />Público)|Al menos 5 años a partir de su<br />fecha<br />de<br />finalización<br />o <br />resolución.|

|Col1|PROCEDIMIENTO DE<br />COPIAS DE SEGURIDAD<br />Y RESPALDO|Código: PRO-013.02|
|---|---|---|
||<br />USO OFICIAL INTERNO<br />|<br />Fecha de vigor: 19/03/2025<br />|

|Videovigilancia|Art. 22 LOPDGDD|Plazo máximo de 1 mes y<br />después supresión física.|
|---|---|---|
|Denuncias internas|Art. 24 LOPDGDD|Plazo máximo de 3 meses y<br />después supresión física.|

|Col1|PROCEDIMIENTO DE<br />COPIAS DE SEGURIDAD<br />Y RESPALDO|Código: PRO-013.02|
|---|---|---|
||<br />USO OFICIAL INTERNO<br />|<br />Fecha de vigor: 19/03/2025<br />|

## **9 ANEXO II: PLAZOS ESTABLECIDOS DE RETENCIÓN**
Los periodos de retención de copias de seguridad se justifican en función de la criticidad del activo, su impacto en la operativa de la organización y los tiempos aceptables de recuperación
y pérdida de datos que se puedan tolerar sin afectar significativamente a la organización. Los periodos de retención de los activos de tipo base de datos pueden ser modificados en función
de los plazos legales de conservación que requiera el tipo de información almacenada, según se detalla en el Anexo I:

|Nivel|Tipo de<br />copia|Periodicidad|Retención|Soporte<br />(almacenamiento)|
|---|---|---|---|---|
|**Bajo**|Completa|1 año|2 años|Físico y digital|
|**Bajo**|Completa|6 meses|1 año|Físico|
|**Bajo**|Completa|1 mes|6 meses|Físico|

|Nivel|Tipo de<br />copia|Periodicidad|Retención|Soporte<br />(almacenamiento)|
|---|---|---|---|---|
|**Medio**|Completa|3 meses|3 años|Físico y digital|
|**Medio**|Completa|1 mes|2 años|Físico y digital|
|**Medio**|Completa|1 semana|1 año|Físico|

|Nivel|Tipo de<br />copia|Periodicidad|Retención|Soporte<br />(almacenamiento)|
|---|---|---|---|---|
|**Alto**|Completa|1 mes|8 años|Físico y digital|
|**Alto**|Completa|1 semana|6 años|Físico y digital|
|**Alto**|Completa|1 día|4 años|Físico y digital|