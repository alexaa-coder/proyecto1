---
id: adr-001-02_informe-de-análisis-de-riesgos-2024
title: "Adr 001.02 Informe De Análisis De Riesgos 2024"
sidebar_label: "Adr 001.02 Informe De Análisis De Riesgos 2024"
---

|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-0-0.png)

</div>


![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-0-1.png)
# **INFORME DE ANÁLISIS Y GESTIÓN DE** **RIESGOS**


|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-1-0.png)

</div>



|HISTORIAL DEL DOCUMENTO|Col2|Col3|Col4|
|---|---|---|---|
|**Versión**|**Resumen de modificaciones**|**Fecha de**<br />**entrada**|**Sustituye a**<br />**(Código,**<br />**revisión)**|
|01|Primera versión del documento.|11/03/2025|N/A|
|02|Añadida la fórmula que se usa para calcular el<br />nivel de riesgo.|10/04/2025|01|




|REGISTRO DE FIRMAS|Col2|Col3|Col4|
|---|---|---|---|
|**Función:**|**Elaborado por:**|**Revisado por:**|**Aprobado por:**|
|Departam<br />ento:|Responsable del SGSI|Dirección|Jefe de seguridad<br />(o suplente)|
|Nombre:|David Pozo|Carlos Rodrigo|Carlos Zúñiga|
|Firma:|<br />[DIGITAL SIGNATURE]<br />`SANCHEZ DAVID -`<br />` el día`<br />`10/04/2025`<br /> <br /> <br /><br /> <br />|<br /> <br /> <br /> <br /> <br /> <br />`Firmado por`<br />`RODRIGO RIVERO,`<br />`CARLOS`<br />`(AUTENTICACIÓN) el`<br />~~`ía 10/04/2025 con`~~|<br />`Firmado por`<br />` CARLOS`<br />`ZUÑIGA (R:`<br />`****8690*) el día`<br />~~`10/04/2025 con un`~~|
|Fecha:|10/04/2025<br />|10/04/2025<br /> <br />|10/04/2025<br />|




|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-2-0.png)
## **CONTENIDO**

1 INTRODUCCIÓN

2 ALCANCE

3 NORMATIVA APLICABLE

4 DATOS DE PARTIDA

4.1 INVENTARIO DE ACTIVOS

4.2 LISTADO DE AMENAZAS

4.3 NIVEL DE MADUREZ

5 RESULTADOS

5.1 AMENAZAS CON NIVEL DE IMPACTO Y PROBABILIDAD ELEVADA

5.2 AMENANZAS CON PROBABILIDAD BAJA Y NIVEL DE IMPACTO ELEVADO

5.3 AMENANZAS CON PROBABILIDAD BAJA Y NIVEL DE IMPACTO BAJO

5.4 ACTIVOS CON NIVEL DE RIESGO MAJOR (9-12)

5.5 ACTIVOS CON NIVEL DE RIESGO CRITICAL (12-16)

6 PLAN DE TRATAMIENTO DE RIESGOS


|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-3-0.png)
## **1 INTRODUCCIÓN**

<div style={{textAlign: "justify"}}>

Se ha realizado un análisis formal de riesgos del Sistema de Información de SPIKA TECH

</div>


<div style={{textAlign: "justify"}}>

conforme a los requisitos de la norma **ISO/IEC 27001** :2022, específicamente en lo relacionado

</div>


<div style={{textAlign: "justify"}}>

con la **evaluación y tratamiento de riesgos** (Cláusula 6.1.2 y Anexo A). Este análisis sigue

</div>


<div style={{textAlign: "justify"}}>

las mejores prácticas reconocidas en el ámbito de la seguridad de la información.

</div>


<div style={{textAlign: "justify"}}>

La metodología utilizada para el análisis y la gestión de riesgos ha sido **MAGERIT**

</div>


**(Metodología de Análisis y Gestión de Riesgos de los Sistemas de Información) v3.0**,

<div style={{textAlign: "justify"}}>

que es plenamente compatible con los principios de la ISO/IEC 27001.

</div>


<div style={{textAlign: "justify"}}>

Los niveles de riesgos tomados en consideración para la realización del análisis de riesgos se

</div>


<div style={{textAlign: "justify"}}>

calculan multiplicando la probabilidad de que suceda el riesgo por el impacto que tendría en

</div>


<div style={{textAlign: "justify"}}>

el caso de que suceda. Primero se establecen valores del 1 al 4 para la probabilidad y el

</div>


impacto, para posteriormente multiplicar esos valores.

<div style={{textAlign: "justify"}}>

Con estos valores, los niveles de riesgo son los siguientes:

</div>


 - **Riesgo CRITICAL (de 12 a 16)** : Los activos con esta combinación de impacto y

<div style={{textAlign: "justify"}}>

probabilidad son altamente críticos y deben ser tratados con urgencia para reducir el

</div>


<div style={{textAlign: "justify"}}>

impacto potencial de las amenazas. Este nivel se genera cuando el **Impacto** es **"A"**

</div>


(severamente alto) y la **probabilidad** es alta.

 - **Riesgo MAJOR (de 9 a 12)** : Estos activos presentan un riesgo importante, que puede

<div style={{textAlign: "justify"}}>

tener un impacto negativo significativo en la seguridad o la operación, aunque no tan

</div>


<div style={{textAlign: "justify"}}>

grave como los riesgos críticos. Generalmente, estos niveles ocurren cuando el

</div>


**Impacto** es **"M"** (alto) con una probabilidad también considerable.

 - **Riesgo MINOR (de 4 a 8)** : Estos riesgos son manejables y no presentan una amenaza

<div style={{textAlign: "justify"}}>

inmediata a las operaciones. A menudo, el **Impacto** en estos casos es **"B"** (medio) o

</div>


<div style={{textAlign: "justify"}}>

el **Impacto** es **"M"** pero con una baja probabilidad de ocurrencia.

</div>


 - **Riesgo LIMITED (de 1 a 3)** : Los riesgos limitados son aquellos con **Impacto** bajo y

**probabilidad** baja. Estos no suelen afectar significativamente las operaciones del

sistema, pero aun así deben ser monitoreados.


|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-4-0.png)

</div>


Impact


|4|Col2|12|Col4|
|---|---|---|---|
|**3 **|**6 **|**9 **||
|**2 **|**4 **|**6 **|**8 **|
|**1 **|**2 **|**3 **|**4 **|



1 2 3 4

MB B M A Probability

## **2 ALCANCE**

<div style={{textAlign: "justify"}}>

El presente análisis afecta a todos los activos que quedan bajo el alcance del Sistema de

</div>


Información de SPIKA TECH.

## **3 NORMATIVA APLICABLE**

<div style={{textAlign: "justify"}}>

Es aplicable toda la normativa establecida en el documento de **RGS_1 NORMATIVA**

</div>


**APLICABLE**, que se actualizara de forma periódica Las Políticas, Normas y Procedimientos

dentro del alcance.

## **4 DATOS DE PARTIDA**

**4.1** **INVENTARIO DE ACTIVOS**

<div style={{textAlign: "justify"}}>

Se ha realizado un inventario pormenorizado de los activos, y posteriormente, estos han sido

</div>


<div style={{textAlign: "justify"}}>

clasificados y agrupados bajo una categoría específica denominada 'asset type'.

</div>



|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-5-0.png)

</div>


<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-5-1.png)

</div>


**4.2** **LISTADO DE AMENAZAS**


|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-6-0.png)

</div>



|ID|Threats<br />[Desastre] Fuego, agua o desastres naturales<br />[Actividad malintencionada / abuso] Fuga de información<br />[Actividad malintencionada / abuso] Introducción de falsa información<br />[Actividad malintencionada / abuso] Alteración de la información<br />[Actividad malintencionada / abuso] Destrucción de información<br />[Actividad malintencionada / abuso] Interceptación de información (escucha)<br />[Malfuncionamiento] Corte del suministro eléctrico<br />[Desastre] Condiciones inadecuadas de temperatura o humedad<br />[Malfuncionamiento] Fallo de servicios de comunicaciones|
|---|---|
|TH01|TH01|
|TH02|TH02|
|TH03|TH03|
|TH04|TH04|
|TH05|TH05|
|TH06|TH06|
|TH07|TH07|
|TH08|TH08|
|TH09|TH09|
|TH10|[Indisponibilidad del recurso] Interrupción de servicios y suministros esenciales|
|TH11|[Desastre] Desastres industriales|
|TH12|[Daños accidentales] Errores de los usuarios|
|TH13|[Daños accidentales] Errores del administrador<br />[Daños accidentales] Errores de configuración<br />[Daños accidentales] Degradación de los soportes de almacenamiento de la<br />información|
|TH14|TH14|
|TH15|TH15|
|TH16|[Actividad malintencionada / abuso] Instalación de software dañino<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />[Indisponibilidad del recurso] Caída del sistema por sobrecarga<br />[Daños accidentales] Pérdida de equipos<br />[Indisponibilidad del recurso] Indisponibilidad del personal|
|TH17|TH17|
|TH18|TH18|
|TH19|TH19|
|TH20|TH20|
|TH21|[Actividad malintencionada / abuso] Abuso de privilegios de acceso|
|TH22|[Actividad malintencionada / abuso] Acceso no autorizado<br />[Actividad malintencionada / abuso] Denegación de servicio<br />[Actividad malintencionada / abuso] Extorsión|
|TH23|TH23|
|TH24|TH24|
|TH25|[Actividad malintencionada / abuso] Ingeniería social|



**4.3** **NIVEL DE MADUREZ**

<div style={{textAlign: "justify"}}>

Se han implementado los controles establecidos por la norma ISO 27001, asegurando su

</div>


<div style={{textAlign: "justify"}}>

cumplimiento en todos los aspectos relevantes. Además, se ha llevado a cabo una evaluación

</div>


<div style={{textAlign: "justify"}}>

del nivel de madurez para cada uno de estos controles, con el fin de medir su efectividad y

</div>


<div style={{textAlign: "justify"}}>

determinar las áreas de mejora necesarias para optimizar el sistema de gestión de la

</div>


seguridad de la información.

<div style={{textAlign: "justify"}}>

Para ello, se ha tenido en cuenta la siguiente tabla de equivalencias:

</div>



|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-7-0.png)

</div>


<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-7-1.png)

</div>



|Eficacia de la Salvaguarda|Col2|Descripción|
|---|---|---|
|**Valor**<br />**cualitativo**|**Valor**<br />**cuantitativo**|**Valor**<br />**cuantitativo**|
|**L0 -**<br />**Inexistente**||<br />Esta medida no existe o no se está siendo aplicada en este momento.|
|**L1 -**<br />**Inicial/ad-**<br />**hoc**|**10%**|<br />En el nivel L1 de madurez, el proceso existe, pero no se gestiona. Cuando la<br />organización no proporciona un entorno estable.<br />El éxito o fracaso del proceso depende de la competencia y buena voluntad<br />de las personas y es difícil prever la reacción ante una situación de emergencia.<br />En este caso, las organizaciones exceden con frecuencia presupuestos y<br />tiempos de respuesta. El éxito del nivel L1 depende de tener personal de alta<br />calidad.|
|**L2 -**<br />**Reproducibl**<br />**e, pero**<br />**intuitivo**|**50%**|<br />En el nivel L2 de madurez, la eficacia del proceso depende de la buena suerte<br />y de la buena voluntad de las personas.<br />Existe un mínimo de planificación que proporciona una pauta a seguir<br />cuando se repiten las mismas circunstancias.<br />Es impredecible el resultado si se dan circunstancias nuevas.<br />Todavía hay un riesgo significativo de exceder las estimaciones de coste y<br />riesgo.|




|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-8-0.png)

</div>



|L3 -<br />Proceso<br />definido|80%|Se dispone un catálogo de procesos que se mantiene actualizado. Estos<br />procesos garantizan la consistencia de las actuaciones entre las diferentes<br />partes de la organización, que adaptan sus procesos particulares al proceso<br />general. Hay normativa establecida y procedimientos para garantizar la<br />reacción profesional ante los incidentes.<br />Se ejerce un mantenimiento regular. Las oportunidades de sobrevivir son<br />altas, aunque siempre queda el factor de lo desconocido (o no planificado). El<br />éxito es algo más que buena suerte: se merece.<br />Una diferencia importante entre el nivel 2 y el nivel 3 es la coordinación entre<br />departamentos y proyectos, coordinación que no existe en el nivel 2, y que se<br />gestiona en el nivel 3.|
|---|---|---|
|**L4 -**<br />**Gestionado**<br />**y Medible**|**90%**|<br />Cuando se dispone de un sistema de medidas y métricas para conocer el<br />desempeño (eficacia y eficiencia) de los procesos.<br />La Dirección es capaz de establecer objetivos cualitativos a alcanzar y<br />dispone de medios para valorar si se han alcanzado los objetivos y en qué<br />medida. En el nivel L4 de madurez, el funcionamiento de los procesos está bajo<br />control con técnicas estadísticas y cuantitativas.<br />La confianza es cuantitativa, mientras que en el nivel L3, la confianza era<br />solamente cualitativa.|
|**L5 -**<br />**Optimizado**|**100%**|**Optimizado.** <br />El nivel L5 de madurez se centra en la mejora continua de los procesos con<br />mejoras tecnológicas incrementales e innovadoras.<br />Se establecen objetivos cuantitativos de mejora. Y se revisan<br />continuamente para reflejar los cambios en los objetivos de negocio,<br />utilizándose como indicadores en la gestión de la mejora de los procesos.<br />En este nivel la organización es capaz de mejorar el desempeño de los<br />sistemas a base de una mejora continua de los procesos basada en los<br />resultados de las medidas e indicadores.|




|ID|Controls|Assessment Maturity<br />2024|
|---|---|---|
|C001|Políticas de seguridad de la información|3|
|C002|Roles y segregación de responsabilidades|3,5|
|C003|Contacto con las autoridades y grupos de interés|2|
|C004|Inteligencia de amenazas|2|




|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-9-0.png)

</div>



|C005|Seguridad de la información en la gestión de proyectos|3|
|---|---|---|
|C006|Inventario de información y otros activos|4|
|C007|Uso aceptable de la información y otros activos|3,5|
|C008|Devolución de activos|3|
|C009|Clasificación y etiquetado de la información|3|
|C010|Transferencia de información|3,5|
|C011|Gestión de identidades y control de acceso|3|
|C012|Información de autenticación|3|
|C013|Derechos de acceso|3|
|C014|Gestión de la seguridad de la información en relaciones con terceros|3|
|C015|Monitorización, revisión y gestión del cambio de servicios de terceros|3|
|C016|Seguridad de la información para el uso de servicios en cloud|3|
|C017|Planificación y respuesta para la gestión de incidentes|3|
|C018|Evaluación y decisión de eventos de seguridad|3|
|C019|Aprendizaje de los incidentes de seguridad|3|
|C020|Recogida de evidencias|3|
|C021|Seguridad de la información durante una interrupción|3|
|C022|Preparación de IT para la continuidad del negocio|3|
|C023|Requerimientos contractuales legales y regulatorios - Identificar y documentar los requisitos<br />pertinentes|4|
|C024|Derechos de propiedad intelectual|3,5|
|C025|Protección de registros|3|
|C026|Privacidad y protección de la información personal|3,5|
|C027|Revisión independiente de la seguridad de la información|3|
|C028|Cumplimiento de políticas, normas, procesos operativos y estándares de seguridad|3|
|C029|Screening|3|
|C030|Términos y condiciones|3|
|C031|Concienciación y training sobre seguridad de la información|3,5|
|C032|Proceso disciplinario|2|
|C033|Responsabilidades a la finalización de la relación laboral|3|
|C034|Confidencialidad o NDAs|4|
|C035|Teletrabajo|2,5|
|C036|Reporting de eventos de seguridad - Notifiación por los canales adecuados|3,5|
|C037|Perímetros físicos de seguridad|2,5|
|C038|Entrada física|2,5|
|C039|Seguridad en oficinas e instalaciones.|2,5|
|C040|Monitoreo de seguridad física|2|
|C041|Protección ante amenazas físicas y medioambientales|3|
|C042|Mesas y escritorios limpios|3|
|C043|Protección del equipamiento|3|
|C044|Seguridad de los activos off-premises|3|
|C045|Dispositivos de almacenamiento|3,5|
|C046|Servicios de apoyo|3|
|C047|Seguridad en el cableado|3|
|C048|Mantenimiento de equipos|3|
|C050|Endpoints para usuarios|3|
|C051|Derechos de acceso privilegiados|3|
|C052|Restricción de acceso a la información|2,5|
|C053|Acceso al código fuente|3|
|C054|Autenticación segura|3|
|C055|Gestión de capacidades|3|
|C056|Protección contra el malware|2,5|




|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-10-0.png)

</div>



|C057|Gestión de vulerabilidades técnicas|3|
|---|---|---|
|C058|Gestión de configuración|3|
|C059|Borrado de información|3|
|C060|Data masking|3|
|C061|Prevención de exfiltración de datos|2|
|C062|Backups|3|
|C063|Redundancia de las instalaciones de procesamiento de la información|2|
|C064|Logging|2|
|C065|Actividades de monitorización|2,5|
|C066|Sincronización de reloj|3|
|C067|Uso de programas privilegiados|3|
|C068|Instalación de software en sistemas operativos - Procedimientos para la instalación de SW|3|
|C069|Seguridad en la red|2,5|
|C070|Segregación de redes|2,5|
|C071|Web filtering|3|
|C072|Uso de la criptografía|2,5|
|C073|Ciclo de vida del desarrollo seguro|3,5|
|C074|Requerimientos de seguridad en las aplicaciones|3,5|
|C075|Arquitectura de sistemas seguros y principios de ingeniería|3|
|C076|Secure coding|3|
|C077|Pruebas de seguridad en desarrollo y aceptación|3|
|C078|Desarrollo externalizado|3|
|C079|Separación de desarrollo, test y producción|3|
|C080|Gestión del cambio|3|
|C081|Test information|3|
|C082|Protección de los sistemas de información durante las auditorías|3|



## **5 RESULTADOS**

**5.1** **AMENAZAS CON NIVEL DE IMPACTO Y PROBABILIDAD ELEVADA**

<div style={{textAlign: "justify"}}>

Las **amenazas** del sistema de información de SPIKA TECH identificadas con Probabilidad **alta**

</div>


<div style={{textAlign: "justify"}}>

(3,0 – 4,0) e impacto **alto** (3,0-4,0), son las que siguen:

</div>


<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-10-1.png)

</div>



|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-11-0.png)

</div>


**5.2** **AMENANZAS CON PROBABILIDAD BAJA Y NIVEL DE IMPACTO ELEVADO**

<div style={{textAlign: "justify"}}>

Las **amenazas** del sistema de información de SPIKA TECH identificadas con Probabilidad **baja**

</div>


<div style={{textAlign: "justify"}}>

(1,0 – 2,0) e impacto **alto** (3,0-4,0), son las que siguen:

</div>


**5.3** **AMENANZAS CON PROBABILIDAD BAJA Y NIVEL DE IMPACTO BAJO**

<div style={{textAlign: "justify"}}>

Las **amenazas** del sistema de información de SPIKA TECH identificadas con Probabilidad **baja**

</div>


<div style={{textAlign: "justify"}}>

(1,0 – 2,0) e impacto **bajo** (1,0-2,0), son las que siguen:

</div>


<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-11-1.png)

</div>


<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-11-2.png)

</div>



|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-12-0.png)

</div>



|5.4 ACTIVOS CON NIVEL DE RIESGO MAJOR (9-12)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|Inherent Risk|Inherent Risk|Inherent Risk|Inherent Risk|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|Asset ID|Asset|Threat ID|Threat|PROB|IMP|RISK|LEVEL|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS01|Personal Directivo|TH24|[Actividad malintencionada / abuso] Extorsión|2,0|3,0|6,0|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS02|Usuario Final|TH24|[Actividad malintencionada / abuso] Extorsión|2,0|3,0|6,0|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS03|Usuarios administradores|TH24|[Actividad malintencionada / abuso] Extorsión|2,0|3,0|6,0|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS04|Usuarios Cloud|TH25|[Actividad malintencionada / abuso] Ingeniería social|2,5|2,5|6,3|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS05|Proveedores Desarrollo|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|2,5|2,5|6,3|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS06|Proveedores Infraestructura y Comunicaciones|TH17|[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|2,0|3,0|6,0|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS06|Proveedores Infraestructura y Comunicaciones|TH23|[Actividad malintencionada / abuso] Denegación de servicio|3,0|3,0|9,0|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS08|Proxy CloudFare (VRcardio)|TH17|[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|2,0|3,0|6,0|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS08|Proxy CloudFare (VRcardio)|TH24|[Actividad malintencionada / abuso] Extorsión|2,0|3,0|6,0|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS08|Proxy CloudFare (VRcardio)|TH17|[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|2,0|3,0|6,0|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS08|Proxy CloudFare (VRcardio)|TH24|[Actividad malintencionada / abuso] Extorsión|2,0|3,0|6,0|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS09|WAF|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|2,5|2,5|6,3|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS10|Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|2,5|2,5|6,3|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS11|Maquina de Salto|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|2,5|2,5|6,3|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS12|Desktop|TH10|[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales|3,0|3,0|9,0|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS12|Desktop|TH14|[Daños accidentales] Errores de configuración|2,0|3,0|6,0|MAJOR|
|Asset ID<br />Asset<br />Threat ID<br />Threat<br />AS01<br />Personal Directivo<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS02<br />Usuario Final<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS03<br />Usuarios administradores<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS04<br />Usuarios Cloud<br />TH25<br />[Actividad malintencionada / abuso] Ingeniería social<br />AS05<br />Proveedores Desarrollo<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS06<br />Proveedores Infraestructura y Comunicaciones<br />TH23<br />[Actividad malintencionada / abuso] Denegación de servicio<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)<br />AS08<br />Proxy CloudFare (VRcardio)<br />TH24<br />[Actividad malintencionada / abuso] Extorsión<br />AS09<br />WAF<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS10<br />Elementos de soporte de red (switch, modens, hubs,<br />router, WAP)<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS11<br />Maquina de Salto<br />TH22<br />[Actividad malintencionada / abuso] Acceso no autorizado<br />AS12<br />Desktop<br />TH10<br />[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales<br />AS12<br />Desktop<br />TH14<br />[Daños accidentales] Errores de configuración<br />AS12<br />Desktop<br />TH17<br />[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|AS12|Desktop|TH17|[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|2,0|3,0|6,0|MAJOR|
||AS12|Desktop|TH19|[Daños accidentales] Pérdida de equipos|2,0|4,0|8,0|MAJOR|
||AS12|Desktop|TH23|[Actividad malintencionada / abuso] Denegación de servicio|3,0|3,0|9,0|MAJOR|
||AS13|Laptop|TH10|[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales|3,0|3,0|9,0|MAJOR|
||AS13|Laptop|TH14|[Daños accidentales] Errores de configuración|2,0|3,0|6,0|MAJOR|
||AS13|Laptop|TH17|[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|2,0|3,0|6,0|MAJOR|




|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-13-0.png)

</div>



|Col1|AS13|Laptop|TH19|[Daños accidentales] Pérdida de equipos|2,0|4,0|8,0|MAJOR|
|---|---|---|---|---|---|---|---|---|
||AS13|Laptop|TH23|[Actividad malintencionada / abuso] Denegación de servicio|3,0|3,0|9,0|MAJOR|
||AS15|DNS|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|2,5|2,5|6,3|MAJOR|
||AS16|Aplicaciones de escritorio|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|2,5|2,5|6,3|MAJOR|
||AS17|VR-CARDIO|TH10|[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales|3,0|3,0|9,0|MAJOR|
||AS17|VR-CARDIO|TH14|[Daños accidentales] Errores de configuración|2,0|3,0|6,0|MAJOR|
||AS17|VR-CARDIO|TH17|[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|2,0|3,0|6,0|MAJOR|
||AS17|VR-CARDIO|TH23|[Actividad malintencionada / abuso] Denegación de servicio|3,0|3,0|9,0|MAJOR|
||AS18|Visual Cardio|TH10|[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales|3,0|3,0|9,0|MAJOR|
||AS18|Visual Cardio|TH14|[Daños accidentales] Errores de configuración|2,0|3,0|6,0|MAJOR|
||AS18|Visual Cardio|TH17|[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|2,0|3,0|6,0|MAJOR|
||AS18|Visual Cardio|TH23|[Actividad malintencionada / abuso] Denegación de servicio|3,0|3,0|9,0|MAJOR|
||AS19|Magallanes|TH10|[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales|3,0|3,0|9,0|MAJOR|
||AS19|Magallanes|TH14|[Daños accidentales] Errores de configuración|2,0|3,0|6,0|MAJOR|
||AS19|Magallanes|TH17|[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|2,0|3,0|6,0|MAJOR|
||AS19|Magallanes|TH23|[Actividad malintencionada / abuso] Denegación de servicio|3,0|3,0|9,0|MAJOR|
||AS20|Plataforma comercial|TH10|[Indisponibilidad del recurso] Interrupción de servicios y suministros<br />esenciales|3,0|3,0|9,0|MAJOR|
||AS20|Plataforma comercial|TH14|[Daños accidentales] Errores de configuración|2,0|3,0|6,0|MAJOR|
||AS20|Plataforma comercial|TH17|[Daños accidentales] Errores de mantenimiento / actualización de programas<br />(software)|2,0|3,0|6,0|MAJOR|
||AS20|Plataforma comercial|TH23|[Actividad malintencionada / abuso] Denegación de servicio|3,0|3,0|9,0|MAJOR|
||AS21|SFTP|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|2,5|2,5|6,3|MAJOR|
||AS22|Sedes|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|2,5|2,5|6,3|MAJOR|
||AS24|Datos de negocio|TH03|[Actividad malintencionada / abuso] Introducción de falsa información|2,0|3,0|6,0|MAJOR|
||AS24|Datos de negocio|TH15|[Daños accidentales] Degradación de los soportes de almacenamiento de la<br />información|2,0|4,0|8,0|MAJOR|
||AS26|Datos de carácter personal|TH03|[Actividad malintencionada / abuso] Introducción de falsa información|2,0|3,0|6,0|MAJOR|
||AS26|Datos de carácter personal|TH15|[Daños accidentales] Degradación de los soportes de almacenamiento de la<br />información|2,0|4,0|8,0|MAJOR|




|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-14-0.png)

</div>



|Col1|AS27|Copias de seguridad|TH03|[Actividad malintencionada / abuso] Introducción de falsa información|2,0|3,0|6,0|MAJOR|
|---|---|---|---|---|---|---|---|---|
||AS27|Copias de seguridad|TH15|[Daños accidentales] Degradación de los soportes de almacenamiento de la<br />información|2,0|4,0|8,0|MAJOR|
||AS28|Registros de actividad (logs)|TH04|[Actividad malintencionada / abuso] Alteración de la información|2,5|2,5|6,3|MAJOR|
||AS28|Registros de actividad (logs)|TH05|[Actividad malintencionada / abuso Destrucción de información|2,5|2,5|6,3|MAJOR|




|5.5 ACTIVOS CON NIVEL DE RIESGO CRITICAL (12-16)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||Inherent Risk|Inherent Risk|Inherent Risk|Inherent Risk|
|Asset ID|Asset|Threat ID|Threat|PROB|IMP|RISK|LEVEL|
|AS01|Personal Directivo|TH25|[Actividad malintencionada / abuso] Ingeniería social|4,0|4,0|16,0|CRITICAL|
|AS02|Usuario Final|TH25|[Actividad malintencionada / abuso] Ingeniería social|4,0|4,0|16,0|CRITICAL|
|AS03|Usuarios administradores|TH25|[Actividad malintencionada / abuso] Ingeniería social|4,0|4,0|16,0|CRITICAL|
|AS06|Proveedores Infraestructura y Comunicaciones|TH02|[Actividad malintencionada / abuso] Fuga de información|3,0|4,0|12,0|CRITICAL|
|AS06|Proveedores Infraestructura y Comunicaciones|TH16|[Actividad malintencionada / abuso] Instalación de software dañino|4,0|3,0|12,0|CRITICAL|
|AS06|Proveedores Infraestructura y Comunicaciones|TH21|[Actividad malintencionada / abuso] Abuso de privilegios de acceso|3,0|4,0|12,0|CRITICAL|
|AS06|Proveedores Infraestructura y Comunicaciones|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|4,0|4,0|16,0|CRITICAL|
|AS08|Proxy CloudFare (VRcardio)|TH25|[Actividad malintencionada / abuso] Ingeniería social|4,0|4,0|16,0|CRITICAL|
|AS08|Proxy CloudFare (VRcardio)|TH25|[Actividad malintencionada / abuso] Ingeniería social|4,0|4,0|16,0|CRITICAL|
|AS12|Desktop|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|4,0|4,0|16,0|CRITICAL|
|AS13|Laptop|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|4,0|4,0|16,0|CRITICAL|
|AS17|VR-CARDIO|TH16|[Actividad malintencionada / abuso] Instalación de software dañino|4,0|3,0|12,0|CRITICAL|
|AS17|VR-CARDIO|TH21|[Actividad malintencionada / abuso] Abuso de privilegios de acceso|3,0|4,0|12,0|CRITICAL|
|AS17|VR-CARDIO|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|4,0|4,0|16,0|CRITICAL|
|AS18|Visual Cardio|TH16|[Actividad malintencionada / abuso] Instalación de software dañino|4,0|3,0|12,0|CRITICAL|
|AS18|Visual Cardio|TH21|[Actividad malintencionada / abuso] Abuso de privilegios de acceso|3,0|4,0|12,0|CRITICAL|
|AS18|Visual Cardio|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|4,0|4,0|16,0|CRITICAL|
|AS19|Magallanes|TH16|[Actividad malintencionada / abuso] Instalación de software dañino|4,0|3,0|12,0|CRITICAL|
|AS19|Magallanes|TH21|[Actividad malintencionada / abuso] Abuso de privilegios de acceso|3,0|4,0|12,0|CRITICAL|
|AS19|Magallanes|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|4,0|4,0|16,0|CRITICAL|
|AS20|Plataforma comercial|TH16|[Actividad malintencionada / abuso] Instalación de software dañino|4,0|3,0|12,0|CRITICAL|




|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



<div style={{textAlign: "justify"}}>

![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-15-0.png)

</div>



|AS20|Plataforma comercial|TH21|[Actividad malintencionada / abuso] Abuso de privilegios de acceso|3,0|4,0|12,0|CRITICAL|
|---|---|---|---|---|---|---|---|
|AS20|Plataforma comercial|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|4,0|4,0|16,0|CRITICAL|
|AS23|Salas técnicas|TH21|[Actividad malintencionada / abuso] Abuso de privilegios de acceso|3,0|4,0|12,0|CRITICAL|
|AS23|Salas técnicas|TH22|[Actividad malintencionada / abuso] Acceso no autorizado|4,0|4,0|16,0|CRITICAL|
|AS24|Datos de negocio|TH02|[Actividad malintencionada / abuso] Fuga de información|3,0|4,0|12,0|CRITICAL|
|AS24|Datos de negocio|TH04|[Actividad malintencionada / abuso] Alteración de la información|4,0|4,0|16,0|CRITICAL|
|AS24|Datos de negocio|TH05|[Actividad malintencionada / abuso Destrucción de información|4,0|4,0|16,0|CRITICAL|
|AS24|Datos de negocio|TH06|[Actividad malintencionada / abuso] Interceptación de información (escucha)|3,0|4,0|12,0|CRITICAL|
|AS26|Datos de carácter personal|TH02|[Actividad malintencionada / abuso] Fuga de información|3,0|4,0|12,0|CRITICAL|
|AS26|Datos de carácter personal|TH04|[Actividad malintencionada / abuso] Alteración de la información|4,0|4,0|16,0|CRITICAL|
|AS26|Datos de carácter personal|TH05|[Actividad malintencionada / abuso Destrucción de información|4,0|4,0|16,0|CRITICAL|
|AS26|Datos de carácter personal|TH06|[Actividad malintencionada / abuso] Interceptación de información (escucha)|3,0|4,0|12,0|CRITICAL|
|AS27|Copias de seguridad|TH02|[Actividad malintencionada / abuso] Fuga de información|3,0|4,0|12,0|CRITICAL|
|AS27|Copias de seguridad|TH04|[Actividad malintencionada / abuso] Alteración de la información|4,0|4,0|16,0|CRITICAL|
|AS27|Copias de seguridad|TH05|[Actividad malintencionada / abuso Destrucción de información|4,0|4,0|16,0|CRITICAL|
|AS27|Copias de seguridad|TH06|[Actividad malintencionada / abuso] Interceptación de información (escucha)|3,0|4,0|12,0|CRITICAL|




|Col1|INFORME DE ANÁLISIS Y<br />GESTIÓN DE RIESGOS|Código: ADR-001.02|
|---|---|---|
||USO OFICIAL<br />INTERNO RESTRINGIDO|<br />Fecha de vigor: 10/04/2025<br />|



![](/img/adr-001-02_informe-de-análisis-de-riesgos-2024/ADR-001.02_INFORME-DE-ANÁLISIS-DE-RIESGOS-2024.pdf-16-0.png)
## **6 PLAN DE TRATAMIENTO DE RIESGOS**

<div style={{textAlign: "justify"}}>

Se procederá a la elaboración de un plan de tratamiento de riesgos, centrado en abordar

</div>


<div style={{textAlign: "justify"}}>

prioritariamente aquellos riesgos clasificados como 'Major' o 'Critical'. Este enfoque permitirá

</div>


<div style={{textAlign: "justify"}}>

dirigir los recursos y esfuerzos hacia la mitigación de los riesgos más significativos,

</div>


<div style={{textAlign: "justify"}}>

asegurando que se implementen medidas efectivas para reducir su impacto y probabilidad. El

</div>


<div style={{textAlign: "justify"}}>

plan estará alineado con los objetivos estratégicos de la organización, garantizando una

</div>


gestión proactiva y eficiente de los riesgos más críticos.