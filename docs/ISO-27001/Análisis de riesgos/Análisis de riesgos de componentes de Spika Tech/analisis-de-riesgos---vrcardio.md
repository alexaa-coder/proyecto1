---
id: analisis-de-riesgos---vrcardio
title: "Análisis De Riesgos   Vrcardio"
sidebar_label: "Análisis De Riesgos   Vrcardio"
---

# **ANÁLISIS DE RIESGOS**

|NOMBRE DE LA APLICACIÓN: VRCARDIO|Col2|Col3|
|---|---|---|
|**1. Descripción general del proyecto**|**1. Descripción general del proyecto**|**1. Descripción general del proyecto**|
|Funcionalidad|Visualizar datos cardíacos|Visualizar datos cardíacos|
|Tecnologías utilizadas|C#, Bases de datos, API y Unity|C#, Bases de datos, API y Unity|
|Ambiente de despliegue|Hospitales|Hospitales|
|**2. Identificación de**<br />**activos críticos**|**Descripción de Activos críticos**|**Descripción de Activos críticos**|
|Datos personales de<br />usuarios|Datos cardíacos del paciente y datos del paciente (altura,<br />peso…). No se guardan nombres ni datos personales|Datos cardíacos del paciente y datos del paciente (altura,<br />peso…). No se guardan nombres ni datos personales|
|Información financiera|No|No|
|Acceso a sistemas<br />internos|API y base de datos|API y base de datos|
|**3. Amenazas**<br />**potenciales**|**Descripción de la Amenaza**|**Descripción de la Amenaza**|
|SQL inyection|El software tiene un sistema de login donde se podría intentar<br />hacer un SQL inyection|El software tiene un sistema de login donde se podría intentar<br />hacer un SQL inyection|
|**4. Vulnerabilidades**|**Nivel de Riesgo**|**Nivel de Riesgo**|
|Acceso a sesiones que<br />no pertenecen a tu<br />usuario|Medio|Medio|
|No anonimizar algún<br />dato|Alto|Alto|
|No cifrar los datos<br />cardíacos|Alto|Alto|
|**5. Mitigación**|**Amenaza**|**Vulnerabilidad**|
|No tener cuentas admin|Acceso a sesiones que no te<br />pertenecen|SQL inyection|