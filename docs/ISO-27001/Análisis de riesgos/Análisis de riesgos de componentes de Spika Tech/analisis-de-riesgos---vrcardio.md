![](/img/analisis-de-riesgos---vrcardio/ANÁLISIS-DE-RIESGOS---VRCARDIO.pdf-0-0.png)


|Col1|PLAN DE FORMACIÓN YCONCIENCIACIÓN EN SEGURIDADINFORMACIÓN|Código: FOR-001.01|
|---|---|---|
||**ANÁLISIS DE RIESGOS**||
























|NOMBRE DE LA APLICACIÓN: VRCARDIOConcienciación|Col2|Col3|
|---|---|---|
|**1. Descripción general del proyecto**|**1. Descripción general del proyecto**|**1. Descripción general del proyecto**|
|Funcionalidad|Visualizar datos cardíacos|Visualizar datos cardíacos|
|Tecnologías utilizadas|C#, Bases de datos, API y Unity|C#, Bases de datos, API y Unity|
|Ambiente de despliegue|Hospitales|Hospitales|
|**2. Identificación de****activos críticos**|**Descripción de Activos críticos**|**Descripción de Activos críticos**|
|Datos personales deusuarios|Datos cardíacos del paciente y datos del paciente (altura,peso…). No se guardan nombres ni datos personales|Datos cardíacos del paciente y datos del paciente (altura,peso…). No se guardan nombres ni datos personales|
|Información financiera|No|No|
|Acceso a sistemasinternos|API y base de datos|API y base de datos|
|**3. Amenazas****potenciales**|**Descripción de la Amenaza**|**Descripción de la Amenaza**|
|SQL inyection|El software tiene un sistema de login donde se podría intentarhacer un SQL inyection|El software tiene un sistema de login donde se podría intentarhacer un SQL inyection|
|**4. Vulnerabilidades**|**Nivel de Riesgo**|**Nivel de Riesgo**|
|Acceso a sesiones queno pertenecen a tuusuario|Medio|Medio|
|No anonimizar algúndato|Alto|Alto|
|No cifrar los datoscardíacos|Alto|Alto|
|**5. Mitigación**|**Amenaza**|**Vulnerabilidad**|
|No tener cuentas admin|Acceso a sesiones que no tepertenecen|SQL inyection|



![](/img/analisis-de-riesgos---vrcardio/ANÁLISIS-DE-RIESGOS---VRCARDIO.pdf-0-1.png)



![](/img/analisis-de-riesgos---vrcardio/ANÁLISIS-DE-RIESGOS---VRCARDIO.pdf-0-2.png)