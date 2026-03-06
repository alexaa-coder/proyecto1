---
id: analisis-de-riesgos---vrcardio-explore
title: "Análisis De Riesgos   Vrcardio Explore"
sidebar_label: "Análisis De Riesgos   Vrcardio Explore"
---

# **ANÁLISIS DE RIESGOS**

|NOMBRE DE LA APLICACIÓN: VRCARDIO EXPLORE|Col2|Col3|
|---|---|---|
|**1. Descripción general del proyecto**|**1. Descripción general del proyecto**|**1. Descripción general del proyecto**|
|Funcionalidad|Recoger datos cardíacos|Recoger datos cardíacos|
|Tecnologías utilizadas|JavaScript, TypeScript, HTML, CSS, API, Base de datos|JavaScript, TypeScript, HTML, CSS, API, Base de datos|
|Ambiente de despliegue|Nube|Nube|
|**2. Identificación de**<br />**activos críticos**|**Descripción de Activos críticos**|**Descripción de Activos críticos**|
|Datos personales de<br />usuarios|Datos cardíacos, datos personales (nombre, apellidos, peso,<br />altura...)|Datos cardíacos, datos personales (nombre, apellidos, peso,<br />altura...)|
|Información financiera|No|No|
|Acceso a sistemas<br />internos|API|API|
|**3. Amenazas**<br />**potenciales**|**Descripción de la Amenaza**|**Descripción de la Amenaza**|
|SQL inyection|En todos los campos rellenables de login, registro y formularios<br />de pacientes y sesiones|En todos los campos rellenables de login, registro y formularios<br />de pacientes y sesiones|
|**4. Vulnerabilidades**|**Nivel de Riesgo**|**Nivel de Riesgo**|
|Acceso a sesiones que<br />no pertenecen a tu<br />usuario|Alto|Alto|
|No anonimizar datos|Alto|Alto|
|No cifrar datos|Alto|Alto|
|**5. Mitigación**|**Amenaza**|**Vulnerabilidad**|
|No compartir cuentas y<br />tener contraseñas<br />robustas|Robo de credenciales|Acceso a datos de sesiones y<br />pacientes no autorizado|