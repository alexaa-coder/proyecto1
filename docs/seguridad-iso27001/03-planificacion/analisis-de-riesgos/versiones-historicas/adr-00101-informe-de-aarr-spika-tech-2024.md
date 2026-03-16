---
title: "INFORME DE ANÁLISIS Y GESTIÓN DE RIESGOS"
sidebar_label: "INFORME DE ANÁLISIS Y GESTIÓN DE RIESGOS"
responsable: "Responsable del SGSI"
clasificacion: "USO INTERNO RESTRINGIDO"
fecha_revision: "2026-03-15"
idioma: "es"
tags:
  - aarr
  - historico
  - iso-27001
  - objetivos
  - planificacion
  - riesgos
  - seguridad
---

|Col1|INFORME DE ANÁLISIS YGESTIÓN DE RIESGOS|Código: ADR-001.01|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-0-0.png)

![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-0-1.png)
# **INFORME DE ANÁLISIS Y GESTIÓN DE** **RIESGOS**


|Col1|INFORME DE ANÁLISIS YGESTIÓN DE RIESGOS|Código: ADR-001.01|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-1-0.png)






|HISTORIAL DEL DOCUMENTO|Col2|Col3|Col4|
|---|---|---|---|
|**Versión**|**Resumen de modificaciones**|**Fecha de****entrada**|**Sustituye a****(Código,****revisión)**|
|01|Primera versión del documento.|11/03/2025|N/A|


















|REGISTRO DE FIRMAS|Col2|Col3|Col4|
|---|---|---|---|
|**Función:**|**Elaborado por:**|**Revisado por:**|**Aprobado por:**|
|Departamento:|Responsable del SGSI|Dirección|Jefe de seguridad(o suplente)|
|Nombre:|David Pozo|Carlos Rodrigo|Carlos Zúñiga|
|Firma:|`Firmado por POZO``SANCHEZ DAVID -``***6992** el día``11/03/2025`  |~~`F`~~`*``Z``*``1`~~`c`~~`Firmado por``RODRIGO RIVERO,``CARLOS``(AUTENTICACIÓN)`~~`l día`~~|~~`irmado por`~~`**8264** CARLOS``UÑIGA (R:``***8690*) el día``1/03/2025 con un`~~`ertificado emitido`~~|**
|Fecha:|11/03/2025|11/03/2025 |11/03/2025|


|Col1|INFORME DE ANÁLISIS YGESTIÓN DE RIESGOS|Código: ADR-001.01|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-2-0.png)
## **CONTENIDO**

1 INTRODUCCIÓN ................................................................................................................................ 4

2 ALCANCE ............................................................................................................................................. 5

3 NORMATIVA APLICABLE ................................................................................................................ 5

4 DATOS DE PARTIDA ........................................................................................................................ 5

4.1 INVENTARIO DE ACTIVOS ..................................................................................................... 5

4.2 LISTADO DE AMENAZAS ........................................................................................................ 6

4.3 NIVEL DE MADUREZ ................................................................................................................ 7

5 RESULTADOS ................................................................................................................................. 11

5.1 AMENAZAS CON NIVEL DE IMPACTO Y PROBABILIDAD ELEVADA ...................... 11

5.2 AMENANZAS CON PROBABILIDAD BAJA Y NIVEL DE IMPACTO ELEVADO ....... 12

5.3 AMENANZAS CON PROBABILIDAD BAJA Y NIVEL DE IMPACTO BAJO ............... 12

5.4 ACTIVOS CON NIVEL DE RIESGO MAJOR (9-12) ......................................................... 13

5.5 ACTIVOS CON NIVEL DE RIESGO CRITICAL (12-16) .................................................... 15

6 PLAN DE TRATAMIENTO DE RIESGOS .................................................................................. 17


|Col1|INFORME DE ANÁLISIS YGESTIÓN DE RIESGOS|Código: ADR-001.01|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-3-0.png)
## **1 INTRODUCCIÓN**

Se ha realizado un análisis formal de riesgos del Sistema de Información de SPIKA TECH


conforme a los requisitos de la norma **ISO/IEC 27001** :2022, específicamente en lo relacionado


con la **evaluación y tratamiento de riesgos** (Cláusula 6.1.2 y Anexo A). Este análisis sigue


las mejores prácticas reconocidas en el ámbito de la seguridad de la información.


La metodología utilizada para el análisis y la gestión de riesgos ha sido **MAGERIT**


**(Metodología de Análisis y Gestión de Riesgos de los Sistemas de Información) v3.0**,


que es plenamente compatible con los principios de la ISO/IEC 27001.


Los niveles de riesgos tomados en consideración para la realización del análisis de riesgos


son los siguientes:


  - **Riesgo CRITICAL (de 12 a 16)** : Los activos con esta combinación de impacto y


probabilidad son altamente críticos y deben ser tratados con urgencia para reducir el


impacto potencial de las amenazas. Este nivel se genera cuando el **Impacto** es **"A"**


(severamente alto) y la **probabilidad** es alta.


  - **Riesgo MAJOR (de 9 a 12)** : Estos activos presentan un riesgo importante, que puede


tener un impacto negativo significativo en la seguridad o la operación, aunque no tan


grave como los riesgos críticos. Generalmente, estos niveles ocurren cuando el


**Impacto** es **"M"** (alto) con una probabilidad también considerable.


  - **Riesgo MINOR (de 4 a 8)** : Estos riesgos son manejables y no presentan una amenaza


inmediata a las operaciones. A menudo, el **Impacto** en estos casos es **"B"** (medio) o


el **Impacto** es **"M"** pero con una baja probabilidad de ocurrencia.


  - **Riesgo LIMITED (de 1 a 3)** : Los riesgos limitados son aquellos con **Impacto** bajo y


**probabilidad** baja. Estos no suelen afectar significativamente las operaciones del


sistema, pero aun así deben ser monitoreados.


|Col1|INFORME DE ANÁLISIS YGESTIÓN DE RIESGOS|Código: ADR-001.01|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-4-0.png)

Impact

|4|Col2|12|Col4|
|---|---|---|---|
|**3 **|**6 **|**9 **|**12**|
|**2 **|**4 **|**6 **|**8 **|
|**1 **|**2 **|**3 **|**4 **|



1 2 3 4


MB B M A Probability

## **2 ALCANCE**


El presente análisis afecta a todos los activos que quedan bajo el alcance del Sistema de


Información de SPIKA TECH.

## **3 NORMATIVA APLICABLE**


Es aplicable toda la normativa establecida en el documento de **RGS_1 NORMATIVA**


**APLICABLE**, que se actualizara de forma periódica Las Políticas, Normas y Procedimientos


dentro del alcance.

## **4 DATOS DE PARTIDA**


**4.1** **INVENTARIO DE ACTIVOS**


Se ha realizado un inventario pormenorizado de los activos, y posteriormente, estos han sido


clasificados y agrupados bajo una categoría específica denominada 'asset type'.


|Col1|INFORME DE ANÁLISIS YGESTIÓN DE RIESGOS|Código: ADR-001.01|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-5-0.png)

![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-5-1.png)

**4.2** **LISTADO DE AMENAZAS**


|Col1|INFORME DE ANÁLISIS YGESTIÓN DE RIESGOS|Código: ADR-001.01|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-6-0.png)













|ID|Threats[Desastre] Fuego, agua o desastres naturales[Actividad malintencionada / abuso] Fuga de información[Actividad malintencionada / abuso] Introducción de falsa información[Actividad malintencionada / abuso] Alteración de la información[Actividad malintencionada / abuso] Destrucción de información[Actividad malintencionada / abuso] Interceptación de información (escucha)[Malfuncionamiento] Corte del suministro eléctrico[Desastre] Condiciones inadecuadas de temperatura o humedad[Malfuncionamiento] Fallo de servicios de comunicaciones|
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
|TH13|[Daños accidentales] Errores del administrador[Daños accidentales] Errores de configuración[Daños accidentales] Degradación de los soportes de almacenamiento de lainformación|
|TH14|TH14|
|TH15|TH15|
|TH16|[Actividad malintencionada / abuso] Instalación de software dañino[Daños accidentales] Errores de mantenimiento / actualización de programas(software)[Indisponibilidad del recurso] Caída del sistema por sobrecarga[Daños accidentales] Pérdida de equipos[Indisponibilidad del recurso] Indisponibilidad del personal|
|TH17|TH17|
|TH18|TH18|
|TH19|TH19|
|TH20|TH20|
|TH21|[Actividad malintencionada / abuso] Abuso de privilegios de acceso|
|TH22|[Actividad malintencionada / abuso] Acceso no autorizado[Actividad malintencionada / abuso] Denegación de servicio[Actividad malintencionada / abuso] Extorsión|
|TH23|TH23|
|TH24|TH24|
|TH25|[Actividad malintencionada / abuso] Ingeniería social|


**4.3** **NIVEL DE MADUREZ**


Se han implementado los controles establecidos por la norma ISO 27001, asegurando su


cumplimiento en todos los aspectos relevantes. Además, se ha llevado a cabo una evaluación


del nivel de madurez para cada uno de estos controles, con el fin de medir su efectividad y


determinar las áreas de mejora necesarias para optimizar el sistema de gestión de la


seguridad de la información.


Para ello, se ha tenido en cuenta la siguiente tabla de equivalencias:


|Col1|INFORME DE ANÁLISIS YGESTIÓN DE RIESGOS|Código: ADR-001.01|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-7-0.png)

![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-7-1.png)








|Eficacia de la Salvaguarda|Col2|Descripción|
|---|---|---|
|**Valor****cualitativo**|**Valor****cuantitativo**|**Valor****cuantitativo**|
|**L0 -****Inexistente**|**0**|Esta medida no existe o no se está siendo aplicada en este momento.|
|**L1 -****Inicial/ad-****hoc**|**10%**|En el nivel L1 de madurez, el proceso existe, pero no se gestiona. Cuando laorganización no proporciona un entorno estable.El éxito o fracaso del proceso depende de la competencia y buena voluntadde las personas y es difícil prever la reacción ante una situación de emergencia.En este caso, las organizaciones exceden con frecuencia presupuestos ytiempos de respuesta. El éxito del nivel L1 depende de tener personal de altacalidad.|
|**L2 -****Reproducibl****e, pero****intuitivo**|**50%**|En el nivel L2 de madurez, la eficacia del proceso depende de la buena suertey de la buena voluntad de las personas.Existe un mínimo de planificación que proporciona una pauta a seguircuando se repiten las mismas circunstancias.Es impredecible el resultado si se dan circunstancias nuevas.Todavía hay un riesgo significativo de exceder las estimaciones de coste yriesgo.|


|5. Terminar la configumóvil). Haz click en|Col2|Col3|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-8-0.png)








|Col1|Col2|Col3|
|---|---|---|
|**L4 -****Gestionado****y Medible**|**90%**|Cuando se dispone de un sistema de medidas y métricas para conocer eldesempeño (eficacia y eficiencia) de los procesos.La Dirección es capaz de establecer objetivos cualitativos a alcanzar ydispone de medios para valorar si se han alcanzado los objetivos y en quémedida. En el nivel L4 de madurez, el funcionamiento de los procesos está bajocontrol con técnicas estadísticas y cuantitativas.La confianza es cuantitativa, mientras que en el nivel L3, la confianza erasolamente cualitativa.|
|**L5 -****Optimizado**|**100%**|**Optimizado.** El nivel L5 de madurez se centra en la mejora continua de los procesos conmejoras tecnológicas incrementales e innovadoras.Se establecen objetivos cuantitativos de mejora. Y se revisancontinuamente para reflejar los cambios en los objetivos de negocio,utilizándose como indicadores en la gestión de la mejora de los procesos.En este nivel la organización es capaz de mejorar el desempeño de lossistemas a base de una mejora continua de los procesos basada en losresultados de las medidas e indicadores.|




|Col1|Col2|Col3|
|---|---|---|
|C001|Políticas de seguridad de la información|3|
|C002|Roles y segregación de responsabilidades|3,5|
|C003|Contacto con las autoridades y grupos de interés|2|
|C004|Inteligencia de amenazas|2|


|CCN-STIC-885B Guía de configur|ación segura para SharePoint Online|Col3|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-9-0.png)








|Col1|Col2|Col3|
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
|C023|Requerimientos contractuales legales y regulatorios - Identificar y documentar los requisitospertinentes|4|
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


![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-10-0.png)

|CCN-STIC-885B Guía de configurControl ENS|Col2|Col3|Col4|ación segura para SharePoint Online|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||USO OFICIAL||||||
|||||INTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|Fecha de vigor: 11/03/2025|Fecha de vigor: 11/03/2025|||
|||||||||||
||||abilidades técnicas3  guración3  mación3 3  xfiltración de datos2 3  las instalaciones de procesamiento de la información2 2  onitorización2,5 e reloj3  as privilegiados3  ftware en sistemas operativos - Procedimientos para la instalación de SW3   ed2,5 edes2,53  |abilidades técnicas3  guración3  mación3 3  xfiltración de datos2 3  las instalaciones de procesamiento de la información2 2  onitorización2,5 e reloj3  as privilegiados3  ftware en sistemas operativos - Procedimientos para la instalación de SW3   ed2,5 edes2,53  |abilidades técnicas3  guración3  mación3 3  xfiltración de datos2 3  las instalaciones de procesamiento de la información2 2  onitorización2,5 e reloj3  as privilegiados3  ftware en sistemas operativos - Procedimientos para la instalación de SW3   ed2,5 edes2,53  |abilidades técnicas3  guración3  mación3 3  xfiltración de datos2 3  las instalaciones de procesamiento de la información2 2  onitorización2,5 e reloj3  as privilegiados3  ftware en sistemas operativos - Procedimientos para la instalación de SW3   ed2,5 edes2,53  |abilidades técnicas3  guración3  mación3 3  xfiltración de datos2 3  las instalaciones de procesamiento de la información2 2  onitorización2,5 e reloj3  as privilegiados3  ftware en sistemas operativos - Procedimientos para la instalación de SW3   ed2,5 edes2,53  |||
|C|057|Gestión de vuler|abilidades técnicas|abilidades técnicas|abilidades técnicas|3|3|3|3|
|C|058|Gestión de confi|guración|guración|guración|3|3|3|3|
|C|059|Borrado de infor|mación|mación|mación|3|3|3|3|
|C|060|Data masking||||3|3|3|3|
|C|061|Prevención de e|xfiltración de datos|xfiltración de datos|xfiltración de datos|2|2|2|2|
|C|062|Backups||||3|3|3|3|
|C|063|Redundancia de|las instalaciones de procesamiento de la información|las instalaciones de procesamiento de la información|las instalaciones de procesamiento de la información|2|2|2|2|
|C|063|Redundancia de|las instalaciones de procesamiento de la información|las instalaciones de procesamiento de la información|las instalaciones de procesamiento de la información|2|2|||
|C|064|Logging||||2|2|2|2|
|C|065|Actividades de m|onitorización|onitorización|onitorización|2,5|2,5|2,5|2,5|
|C|066|Sincronización d|e reloj|e reloj|e reloj|3|3|3|3|
|C|067|Uso de program|as privilegiados|as privilegiados|as privilegiados|3|3|3|3|
|C|068|Instalación de so|ftware en sistemas operativos - Procedimientos para la instalación de SW|ftware en sistemas operativos - Procedimientos para la instalación de SW|ftware en sistemas operativos - Procedimientos para la instalación de SW|3|3|3|3|
|C|069|Seguridad en la r|ed|ed|ed|2,5|2,5|2,5|2,5|
|C|070|Segregación de r|edes|edes|edes|2,5|2,5|2,5|2,5|
|C|071|Web filtering||||3|3|3|3|
|C||||||||||
|C|072|Uso de la criptog|rafía|rafía|rafía|2,5||||
|C|073|Ciclo de vida del|desarrollo seguro|desarrollo seguro|desarrollo seguro|3,5|3,5|3,5|3,5|
|C|074|Requerimientos||||||||
|C|074|Requerimientos|de seguridad en las aplicaciones|de seguridad en las aplicaciones|de seguridad en las aplicaciones|3,5|3,5|||
|C|075|Arquitectura de|sistemas seguros y principios de ingeniería|sistemas seguros y principios de ingeniería|sistemas seguros y principios de ingeniería|3|3|3|3|
|C|076|Secure coding||||3|3|3|3|
|C|077|Pruebas de segu|ridad en desarrollo y aceptación|ridad en desarrollo y aceptación|ridad en desarrollo y aceptación|3|3|3|3|
|C|078|Desarrollo exter|nalizado|nalizado|nalizado|3|3|3|3|
|C|079|Separación de d|esarrollo, test y producción|esarrollo, test y producción|esarrollo, test y producción|3|3|3|3|
|C|080|Gestión del cam|bio|bio|bio|3|3|3|3|
|C|081|Test information||||3|3|3|3|
|C|081|Test information||||3|3|||
|C|082|Protección de lo|s sistemas de información durante las auditorías|s sistemas de información durante las auditorías|s sistemas de información durante las auditorías|3|3|3|3|
|C|**RESULTAD**|**RESULTAD**|**RESULTAD**|**RESULTAD**|**RESULTAD**|**RESULTAD**|**RESULTAD**|**RESULTAD**|**RESULTAD**|


**5.1** **AMENAZAS CON NIVEL DE IMPACTO Y PROBABILIDAD ELEVADA**


Las **amenazas** del sistema de información de SPIKA TECH identificadas con Probabilidad **alta**

(3,0 – 4,0) e impacto **alto** (3,0-4,0), son las que siguen:



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-10-1.png)
|Col1|INFORME DE ANÁLISIS YGESTIÓN DE RIESGOS|Código: ADR-001.01|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-11-0.png)

**5.2** **AMENANZAS CON PROBABILIDAD BAJA Y NIVEL DE IMPACTO ELEVADO**


Las **amenazas** del sistema de información de SPIKA TECH identificadas con Probabilidad **baja**

(1,0 – 2,0) e impacto **alto** (3,0-4,0), son las que siguen:


**5.3** **AMENANZAS CON PROBABILIDAD BAJA Y NIVEL DE IMPACTO BAJO**


Las **amenazas** del sistema de información de SPIKA TECH identificadas con Probabilidad **baja**

(1,0 – 2,0) e impacto **bajo** (1,0-2,0), son las que siguen:



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-11-1.png)

![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-11-2.png)
|Col1|INFORME DE ANÁLISIS YGESTIÓN DE RIESGOS|Código: ADR-001.01|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-12-0.png)








![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-13-1.png)







![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-13-0.png)






|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|AS13Laptop|AS13Laptop|AS13Laptop|TH19[Daños accidentales] Pérdida de equipos|TH19[Daños accidentales] Pérdida de equipos|TH19[Daños accidentales] Pérdida de equipos|2,04,0|2,04,0|2,04,0|8,0 MAJOR|8,0 MAJOR|
||AS13|Laptop||TH23|[Actividad malintencionada / abuso] Denegación de servic|io|3,0|3,0|9,0|MAJOR|
||AS15|DNS||TH22|[Actividad malintencionada / abuso] Acceso no autorizado||2,5|2,5|6,3|MAJOR|
||AS16|Aplicaci|ones de escritorio|TH22|[Actividad malintencionada / abuso] Acceso no autorizado||2,5|2,5|6,3|MAJOR|
||AS17|VR-CAR|DIO|TH10|[Indisponibilidad del recurso] Interrupción de servicios y sesenciales|uministros|3,0|3,0|9,0|MAJOR|
||AS17|VR-CAR|DIO|TH14|[Daños accidentales] Errores de configuración||2,0|3,0|6,0|MAJOR|
||AS17|VR-CAR|DIO|TH17|[Daños accidentales] Errores de mantenimiento / actualiz(software)|ación de programas|2,0|3,0|6,0|MAJOR|
||AS17|VR-CAR|DIO|TH23|[Actividad malintencionada / abuso] Denegación de servic|io|3,0|3,0|9,0|MAJOR|
||AS18|Visual C|ardio|TH10|[Indisponibilidad del recurso] Interrupción de servicios y sesenciales|uministros|3,0|3,0|9,0|MAJOR|
||AS18|Visual C|ardio|TH14|[Daños accidentales] Errores de configuración||2,0|3,0|6,0|MAJOR|
||AS18|Visual C|ardio|TH17|[Daños accidentales] Errores de mantenimiento / actualiz(software)|ación de programas|2,0|3,0|6,0|MAJOR|
||AS18|Visual C|ardio|TH23|[Actividad malintencionada / abuso] Denegación de servic|io|3,0|3,0|9,0|MAJOR|
||AS19|Magalla|nes|TH10|[Indisponibilidad del recurso] Interrupción de servicios y sesenciales|uministros|3,0|3,0|9,0|MAJOR|
||AS19|Magalla|nes|TH14|[Daños accidentales] Errores de configuración||2,0|3,0|6,0|MAJOR|
||AS19|Magalla|nes|TH17|[Daños accidentales] Errores de mantenimiento / actualiz(software)|ación de programas|2,0|3,0|6,0|MAJOR|
||AS19|Magalla|nes|TH23|[Actividad malintencionada / abuso] Denegación de servic|io|3,0|3,0|9,0|MAJOR|
||AS20|Platafor|ma comercial|TH10|[Indisponibilidad del recurso] Interrupción de servicios y sesenciales|uministros|3,0|3,0|9,0|MAJOR|
||AS20|Platafor|ma comercial|TH14|[Daños accidentales] Errores de configuración||2,0|3,0|6,0|MAJOR|
||AS20|Platafor|ma comercial|TH17|[Daños accidentales] Errores de mantenimiento / actualiz(software)|ación de programas|2,0|3,0|6,0|MAJOR|
||AS20|Platafor|ma comercial|TH23|[Actividad malintencionada / abuso] Denegación de servic|io|3,0|3,0|9,0|MAJOR|
||AS21|SFTP||TH22|[Actividad malintencionada / abuso] Acceso no autorizado||2,5|2,5|6,3|MAJOR|
||AS22|Sedes||TH22|[Actividad malintencionada / abuso] Acceso no autorizado||2,5|2,5|6,3|MAJOR|
||AS24|Datos|e negocio|TH03|[Actividad malintencionada / abuso] Introducción de falsa|información|2,0|3,0|6,0|MAJOR|
||||||||||||
||AS24|Datos d|e negocio|TH15|[Daños accidentales] Degradación de los soportes de almainformación|cenamiento de la|2,0|4,0|8,0|MAJOR|
||AS26|Datos d|e carácter personal|TH03|[Actividad malintencionada / abuso] Introducción de falsa|información|2,0|3,0|6,0|MAJOR|
||AS26|Datos d|e carácter personal|TH15|[Daños accidentales] Degradación de los soportes de almainformación|cenamiento de la|2,0|4,0|8,0|MAJOR|
||||||||||||


|Col1|INFORME DE ANÁLISIS YGESTIÓN DE RIESGOS|Código: ADR-001.01|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-14-0.png)


|Col1|AS27|Copias de seguridad|TH03|[Actividad malintencionada / abuso] Introducción de falsa información|2,0|3,0|6,0|MAJOR|
|---|---|---|---|---|---|---|---|---|
||AS27|Copias de seguridad|TH15|[Daños accidentales] Degradación de los soportes de almacenamiento de lainformación|2,0|4,0|8,0|MAJOR|
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


|Puede acceder a las copiasseguridad de Norton Pass|ProtegerImportar los datos de Nor|los datos confidenciales 88ton Password Manager|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-15-0.png)


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|AS20|Plataforma comercial|TH22|[Actividad malintencionada / abuso] Acceso n|o autorizado|4,0|4,0|16,0|CRITICAL|
|AS23|Salas técnicas|TH21|[Actividad malintencionada / abuso] Abuso de|privilegios de acceso|3,0|4,0|12,0|CRITICAL|
|AS23|Salas técnicas|TH22|[Actividad malintencionada / abuso] Acceso n|o autorizado|4,0|4,0|16,0|CRITICAL|
|AS24|Datos de negocio|TH02|[Actividad malintencionada / abuso] Fuga de i|nformación|3,0|4,0|12,0|CRITICAL|
|AS24|Datos de negocio|TH04|[Actividad malintencionada / abuso] Alteració|n de la información|4,0|4,0|16,0|CRITICAL|
|AS24|Datos de negocio|TH05|[Actividad malintencionada / abuso Destrucci|ón de información|4,0|4,0|16,0|CRITICAL|
|AS24|Datos de negocio|TH06|[Actividad malintencionada / abuso] Intercept|ación de información (escucha)|3,0|4,0|12,0|CRITICAL|
|AS26|Datos de carácter personal|TH02|[Actividad malintencionada / abuso] Fuga de i|nformación|3,0|4,0|12,0|CRITICAL|
|AS26|Datos de carácter personal|TH04|[Actividad malintencionada / abuso] Alteració|n de la información|4,0|4,0|16,0|CRITICAL|
|AS26|Datos de carácter personal|TH05|[Actividad malintencionada / abuso Destrucci|ón de información|4,0|4,0|16,0|CRITICAL|
|AS26|Datos de carácter personal|TH06|[Actividad malintencionada / abuso] Intercept|ación de información (escucha)|3,0|4,0|12,0|CRITICAL|
|AS27|Copias de seguridad|TH02|[Actividad malintencionada / abuso] Fuga de i|nformación|3,0|4,0|12,0|CRITICAL|
|AS27|Copias de seguridad|TH04|[Actividad malintencionada / abuso] Alteració|n de la información|4,0|4,0|16,0|CRITICAL|
|AS27|Copias de seguridad|TH05|[Actividad malintencionada / abuso Destrucci|ón de información|4,0|4,0|16,0|CRITICAL|
|AS27|Copias de seguridad|TH06|[Actividad malintencionada / abuso] Intercept|ación de información (escucha)|3,0|4,0|12,0|CRITICAL|


|Col1|INFORME DE ANÁLISIS YGESTIÓN DE RIESGOS|Código: ADR-001.01|
|---|---|---|
||USO OFICIALINTERNO RESTRINGIDO|Fecha de vigor: 11/03/2025|



![](/img/adr-00101-informe-de-aarr-spika-tech-2024/ADR-001.01_Informe-de-AARR_SPIKA-TECH_2024.pdf-16-0.png)
## **6 PLAN DE TRATAMIENTO DE RIESGOS**

Se procederá a la elaboración de un plan de tratamiento de riesgos, centrado en abordar


prioritariamente aquellos riesgos clasificados como 'Major' o 'Critical'. Este enfoque permitirá


dirigir los recursos y esfuerzos hacia la mitigación de los riesgos más significativos,


asegurando que se implementen medidas efectivas para reducir su impacto y probabilidad. El


plan estará alineado con los objetivos estratégicos de la organización, garantizando una


gestión proactiva y eficiente de los riesgos más críticos.