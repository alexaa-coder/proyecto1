---
title: "Analisis De Riesgos Vrcardio Explore"
sidebar_label: "Analisis De Riesgos Vrcardio Explore"
responsable: "Responsable del SGSI"
clasificacion: "USO INTERNO RESTRINGIDO"
fecha_revision: "2026-03-15"
idioma: "es"
tags:
  - aarr
  - english
  - iso-27001
  - objetivos
  - planificacion
  - riesgos
  - seguridad
---

![](/img/analisis-de-riesgos---vrcardio-explore/ANÁLISIS-DE-RIESGOS---VRCARDIO-Explore.pdf-0-0.png)


|Col1|PLAN DE FORMACIÓN YCONCIENCIACIÓN EN SEGURIDADINFORMACIÓN|Código: FOR-001.01|
|---|---|---|
||**ANÁLISIS DE RIESGOS**||
























|Col1|Col2|Col3|
|---|---|---|
|**1. Descripción general del proyecto**|**1. Descripción general del proyecto**|**1. Descripción general del proyecto**|
|Funcionalidad|Recoger datos cardíacos|Recoger datos cardíacos|
|Tecnologías utilizadas|JavaScript, TypeScript, HTML, CSS, API, Base de datos|JavaScript, TypeScript, HTML, CSS, API, Base de datos|
|Ambiente de despliegue|Nube|Nube|
|**2. Identificación de****activos críticos**|**Descripción de Activos críticos**|**Descripción de Activos críticos**|
|Datos personales deusuarios|Datos cardíacos, datos personales (nombre, apellidos, peso,altura...)|Datos cardíacos, datos personales (nombre, apellidos, peso,altura...)|
|Información financiera|No|No|
|Acceso a sistemasinternos|API|API|
|**3. Amenazas****potenciales**|**Descripción de la Amenaza**|**Descripción de la Amenaza**|
|SQL inyection|En todos los campos rellenables de login, registro y formulariosde pacientes y sesiones|En todos los campos rellenables de login, registro y formulariosde pacientes y sesiones|
|**4. Vulnerabilidades**|**Nivel de Riesgo**|**Nivel de Riesgo**|
|Acceso a sesiones queno pertenecen a tuusuario|Alto|Alto|
|No anonimizar datos|Alto|Alto|
|No cifrar datos|Alto|Alto|
|**5. Mitigación**|**Amenaza**|**Vulnerabilidad**|
|No compartir cuentas ytener contraseñasrobustas|Robo de credenciales|Acceso a datos de sesiones ypacientes no autorizado|



![](/img/analisis-de-riesgos---vrcardio-explore/ANÁLISIS-DE-RIESGOS---VRCARDIO-Explore.pdf-0-1.png)



![](/img/analisis-de-riesgos---vrcardio-explore/ANÁLISIS-DE-RIESGOS---VRCARDIO-Explore.pdf-0-2.png)