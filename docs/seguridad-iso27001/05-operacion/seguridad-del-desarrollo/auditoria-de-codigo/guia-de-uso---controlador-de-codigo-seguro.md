---
title: "Guia De Uso Controlador De Codigo Seguro"
sidebar_label: "Guia De Uso Controlador De Codigo Seguro"
responsable: "Director de Calidad"
clasificacion: "USO INTERNO"
fecha_revision: "2026-03-15"
idioma: "es"
tags:
  - auditoria
  - desarrollo-seguro
  - iso-27001
  - operacion
  - pentesting
  - procedimiento
  - seguridad
---

|USO OFICIAL INTERNO|Col2|
|---|---|
|**ACUERDO DE CONFIDENCIALIDAD **|**ACUERDO DE CONFIDENCIALIDAD **|


**Controlador de Seguridad en Desarrollo de Código Seguro**


El software **Spika Tech - Code Checker** está diseñado para ser una herramienta esencial en
la mejora de la seguridad del código antes de realizar su despliegue en el entorno de
producción. Este ejecutable automatiza un proceso de verificación exhaustiva del código
fuente en varias áreas críticas, garantizando que los desarrolladores puedan identificar y
corregir posibles vulnerabilidades, malas prácticas y el manejo inapropiado de datos
sensibles. A continuación, se presenta un resumen detallado de las funcionalidades del
software y sus beneficios:


**1** **Funciones Clave**


1. **Comprobación de dependencias vulnerables (check_dependencies.py)** : El

software escanea el código fuente en busca de bibliotecas importadas en archivos
Python. Una vez que estas dependencias son identificadas, se verifica su seguridad
mediante una herramienta de análisis de vulnerabilidades (como Safety). Esto
permite detectar vulnerabilidades conocidas en las bibliotecas utilizadas, ayudando a
evitar la inclusión de componentes inseguros en el proyecto.


2. **Búsqueda de secretos expuestos (check_password.py)** : Este módulo escanea

los archivos de código para detectar la presencia de contraseñas, claves API, tokens
de autenticación y otras credenciales sensibles que podrían haber sido
accidentalmente incluidas en el código fuente. Al encontrar tales secretos, el sistema
notifica al usuario para que estos sean gestionados adecuadamente y no sean
expuestos en el repositorio.


3. **Detección de funciones inseguras (check_sensitive_commands.py)** : Algunas

funciones, como eval(), exec(), y otras que permiten la ejecución de código arbitrario

    - comandos del sistema, son extremadamente peligrosas si se utilizan de forma
inapropiada. Este módulo examina el código para identificar el uso de dichas
funciones y notifica a los desarrolladores si se detectan.


4. **Verificación del manejo de excepciones**

**(check_try_catch_exception_control.py)** : Un manejo de excepciones incorrecto
puede llevar a la exposición de información sensible, como trazas de errores o logs
inapropiados. El software revisa el uso de bloques try-except y try-catch para
asegurarse de que las excepciones sean manejadas adecuadamente sin revelar
datos confidenciales en el proceso.


5. **Revisión de datos sensibles (check_user_data.py)** : Este módulo busca patrones

de datos sensibles en los archivos del proyecto, como claves de acceso a AWS,
tokens de GitHub y más. También verifica si los datos encontrados están cifrados
correctamente, lo cual es crucial para proteger la privacidad de los usuarios y la
seguridad de las aplicaciones.


**2** **Proceso de Generación de Reportes**


_Página_ _**1**_ _de_ _**3**_


|USO OFICIAL INTERNO|Col2|
|---|---|
|**ACUERDO DE CONFIDENCIALIDAD **|**ACUERDO DE CONFIDENCIALIDAD **|


Una característica destacada del software es la **generación automática de reportes de**
**auditoría** . El ejecutable captura los resultados de cada verificación y los organiza en un
informe PDF detallado. Esto incluye:


  - **Un resumen de las vulnerabilidades detectadas** .


  - **Identificación de secretos expuestos** .


  - **Inseguridad en las funciones utilizadas** .


  - **Malas prácticas en el manejo de excepciones** .


  - **Presencia de datos sensibles no cifrados o mal gestionados** .


Esto permite a los equipos de desarrollo realizar una auditoría completa de seguridad antes
de proceder con el despliegue del código a producción.


**3** **Beneficios del Uso de Spika Tech - Code Checker**


1. **Mejora de la seguridad** : La seguridad del código es crítica, especialmente cuando

se gestionan aplicaciones en producción. Spika Tech - Code Checker proporciona un
enfoque preventivo para identificar problemas potenciales, evitando la exposición de
datos sensibles y minimizando el riesgo de explotación de vulnerabilidades
conocidas.


2. **Automatización del proceso de revisión** : Automatizar las verificaciones de

seguridad ahorra tiempo y esfuerzo a los desarrolladores, ya que no tienen que
realizar estas tareas manualmente. Además, garantiza que ningún aspecto de
seguridad se pase por alto.


3. **Facilidad de integración** : El software está diseñado para ser fácil de integrar con

flujos de trabajo existentes en equipos de desarrollo que utilizan GitHub, lo que
permite realizar las auditorías de seguridad directamente en el código antes de
fusionarlo con ramas principales como production.


4. **Generación de informes detallados** : Los reportes generados de manera

automática ayudan a que los desarrolladores y responsables de seguridad puedan
revisar, corregir y seguir las mejores prácticas antes de que el código se implemente
en producción. Esto mejora la comunicación y asegura que todas las partes
interesadas estén al tanto de los problemas de seguridad.


**4** **Futuro: Integración con SonarQube**


A medida que Spika Tech - Code Checker evoluciona, el siguiente paso será integrar el
software con **SonarQube**, una herramienta líder en análisis de calidad de código.
SonarQube ofrece análisis estáticos más profundos, además de mejorar la capacidad de los
desarrolladores para rastrear vulnerabilidades y debilidades a lo largo del ciclo de vida del
software. Esta integración brindará una solución aún más robusta, ampliando la cobertura y
aumentando la eficiencia en la detección de problemas de seguridad.


_Página_ _**2**_ _de_ _**3**_


|USO OFICIAL INTERNO|Col2|
|---|---|
|**ACUERDO DE CONFIDENCIALIDAD **|**ACUERDO DE CONFIDENCIALIDAD **|


**5** **Conclusión**


El uso de **Spika Tech - Code Checker** es altamente recomendable para cualquier equipo
de desarrollo que busque garantizar la seguridad de su código antes de lanzarlo a
producción. Con su capacidad para detectar vulnerabilidades, secretos expuestos, malas
prácticas y datos sensibles, este software ofrece una capa adicional de protección que
ayuda a prevenir incidentes de seguridad graves. Además, la futura integración con
SonarQube potenciará aún más sus capacidades, consolidándolo como una herramienta
esencial para la seguridad del desarrollo de software.


_Página_ _**3**_ _de_ _**3**_