INFORME DE VALIDACIÓN SOFTWARE










Función:
Elaborado por:
Revisado por:
Aprobado por:




Departamento:
Desarrollo
Dirección
Garantía de Calidad


Nombre:
Javier Vico
Carlos Zúñiga
Iván Pérez


Firma:





Fecha:
13/06/2024
13/06/2024
13/06/2024




# Contenido

[1. Introducción [3](#introducción)](#introducción)

[2. Alcance [3](#alcance)](#alcance)

[3. Definicones [3](#definiciones)](#definiciones)

[4. Procedimientos de validación
[4](#procedimientos-de-validación)](#procedimientos-de-validación)

[4.1. Cualificación de la instalación (IQ)
[4](#cualificación-de-la-instalación-iq)](#cualificación-de-la-instalación-iq)

[4.1.1. Revisión de la documentación de instalación
[4](#revisión-de-la-documentación-de-instalación)](#revisión-de-la-documentación-de-instalación)

[4.1.2. Comprobación de hardware y software
[5](#comprobación-de-hardware-y-software)](#comprobación-de-hardware-y-software)

[4.1.3. Registro de la instalación
[5](#registro-de-la-instalación)](#registro-de-la-instalación)

[4.1.4. Validación de integridad de archivos
[6](#validación-de-integridad-de-archivos)](#validación-de-integridad-de-archivos)

[4.2. Cualificación de la operación (OQ)
[6](#cualificación-de-la-operación-oq)](#cualificación-de-la-operación-oq)

[4.2.1. Pruebas de funcionalidad básica
[6](#pruebas-de-funcionalidad-básica)](#pruebas-de-funcionalidad-básica)

[4.2.2. Pruebas de integración
[9](#pruebas-de-integración)](#pruebas-de-integración)

[4.2.3. Pruebas de rendimiento
[11](#pruebas-de-rendimiento)](#pruebas-de-rendimiento)

[4.2.4. Verificación de seguridad
[13](#verificación-de-seguridad)](#verificación-de-seguridad)

[4.3. Cualificación del funcionamiento (PQ)
[15](#cualificación-del-funcionamiento-pq)](#cualificación-del-funcionamiento-pq)

[4.3.1. Pruebas de aceptación de usuario
[15](#pruebas-de-aceptación-de-usuario)](#pruebas-de-aceptación-de-usuario)

[4.3.2. Pruebas de escenarios críticos
[17](#pruebas-de-escenarios-críticos)](#pruebas-de-escenarios-críticos)

[4.3.3. Evaluación de la documentación del usuario
[19](#evaluación-de-la-documentación-del-usuario)](#evaluación-de-la-documentación-del-usuario)

[5. Resultados y conclusiones
[20](#resultados-y-conclusiones)](#resultados-y-conclusiones)

[6. Historico de versiones
[20](#historico-de-versiones)](#historico-de-versiones)

# Introducción

Este informe presenta los resultados de la validación de la herramienta
de desarrollo Unity utilizado por Spika Tech, en adelante SPIKA, para el
desarrollo de software médico, específicamente diseñado para la
visualización y análisis de señales cardíacas. La validación comrpueba
que Unity cumpla con los estándares de funcionalidad, confiabilidad y
seguridad necesarios para el sofware desarrollado por SPIKA.

# Alcance

La validación abarca todos los aspectos del entorno Unity, centrándose
en tres áreas clave: funcionalidad, confiabilidad y seguridad. Incluye
la verificación de todas las funciones del entorno, la detección de
errores críticos y la evaluación de la seguridad contra vulnerabilidades
conocidas.

# Definiciones

Unity: Plataforma de desarrollo utilizada para la creación del
software.

Validación: Proceso de evaluar si un sistema o componente cumple
con los requisitos y funciona según lo previsto en su entorno operativo.

Cualificación de la Instalación (IQ): Verificación de que el
software y todos sus componentes se han instalado correctamente en el
entorno de destino.

Cualificación de la Operación (OQ): Confirmación de que el
software opera correctamente y que todas las funcionalidades y módulos
principales funcionan como se espera.

Cualificación del Funcionamiento (PQ): Aseguramiento de que el
software cumple con los requisitos específicos del negocio y opera según
los criterios de rendimiento y funcionalidad definidos por el usuario.

# Plan de validación

# Objetivos

Los objetivos principales de la validación del software Unity son:

-   Asegurar que el software cumple con los requisitos de funcionalidad
    y rendimiento establecidos.

-   Verificar la confiabilidad y estabilidad del software en diferentes
    condiciones de operación.

-   Evaluar la seguridad del software contra vulnerabilidades conocidas
    y potenciales.

# Métodos de validación

Los métodos utilizados para la validación incluyen:

-   Pruebas de instalación y configuración.

-   Pruebas de funcionalidad básica y avanzada.

-   Pruebas de integración y comunicación con otros sistemas.

-   Pruebas de rendimiento bajo diferentes cargas.

-   Pruebas de seguridad y resistencia a ataques.

# Criterios de aceptación

El software se considerará aceptado si cumple con los siguientes
criterios:

-   Instalación y configuración correctas sin errores.

-   Funcionamiento correcto de todas las funcionalidades principales.

-   Integración exitosa con sistemas externos y hardware.

-   Rendimiento adecuado bajo diferentes condiciones de carga.

-   Cumplimiento con los estándares de seguridad establecidos.

# 

# Procedimientos de validación

# Cualificación de la instalación (IQ)

# Revisión de la documentación de instalación

Se ha recopilado toda la información disponible para la descarga del
software y primeros pasos para la creación de un proyecto:

-   Enlace de descarga:
    







Proceso
Personal
Incidencias




Acceso a la página de descarga
Descarga e instalación del software
Inicio de sesión con cuenta de desarrollo privada
Acceso al proyecto creado
David Pozo
Ninguna


Acceso a la página de descarga
Descarga e instalación del software
Inicio de sesión con cuenta de desarrollo privada
Acceso al proyecto creado
Daniel Cámara
Ninguna


Acceso a la página de descarga
Descarga e instalación del software
Inicio de sesión con cuenta de desarrollo privada
Acceso al proyecto creado
Javier Vico
Ninguna




# 

# Validación de integridad de archivos

Tras cada descarga e instalación del software, se ha accedido a la
carpeta de ruta local para comprobar que todos los archivos existen y
tienen una fecha de modificación acorde a la fecha de la instalación, lo
que corrobora que ningún fichero o archivo ha sufrido modificaciones de
ningún tipo tras la instalación.

# Cualificación de la operación (OQ)

# Pruebas de funcionalidad básica









Prueba realizada
Resultado
Confirmación




Abrir poyecto existente
El proyecto se abre sin errores
El proyecto a iniciado su carga y posterior apertura


Crear un nuevo proyecto
El nuevo proyecto se crea sin problemas
El proyecto se abre adecuadamente


Agregar un objeto 3D a la escena
El objeto aparece en la escena
El objeto "Cube" fue añadido a la escena y se posicionó delante de
la cámara.


Aplicar un material a un objeto
El material se aplica correctamente
El material "Madera" se aplicó al objeto "Cube", cambiando su
apariencia visual.


Ejecutar la simulación de la escena
La simulación corre sin errores
La escena corrió con una simulación de física básica sin
errores.


Configurar una luz en la escena
La luz se configura y afecta a la escena
Se añadió una luz direccional que ilumina el objeto "Cube", creando
sombras adecuadas.


Aplicar un script a un objeto
El script se ejecuta correctamente.
Se añadió un script para rotar el "Cube". El cubo rota continuamente
en la escena.


Exportar el proyecto
El proyecto se exporta sin errores.
Se genera la build correctamente.


Guardar cambios en el proyecto
Los cambios se guardan sin problemas.
Desaparece el asterisco de que hay cambios sin guardar.


Configuración de parámetros de renderizado
Los parámetros se configuran y aplican correctamente.
Parámetros de renderizado configurados para alta calidad con sombras
y reflejos activados.


Uso de herramientas de navegación
Las herramientas funcionan correctamente.
Herramientas de zoom, pan y órbita utilizadas sin problemas. La
cámara se movió fluidamente por la escena.


Implementación de UI básica
La interfaz de usuario se implementa y funciona.
Se creó una interfaz básica con botones y menús funcionales.


Añadir efectos de partículas
Los efectos se visualizan correctamente.
Efecto de partículas de "Chispas" añadido a la escena,
visualizándose correctamente.


Configuración de animaciones
Las animaciones se configuran y reproducen adecuadamente.
Animación de movimiento configurada para el objeto "Cube".
La animación se reproduce suavemente.


Uso de prefabs
Los prefabs se instancian correctamente.
Prefab de "Árbol" instanciado en la escena, con todas sus
propiedades intactas.


Configiuración de audio
El audio se configura y reproduce sin problemas.
Archivo de audio "Ambiente" añadido a la escena.
Reproducción verificada sin interrupciones.


Implementación de controles de usuario
Los controles responden como se espera.
Se implementaron controles de teclado para mover el objeto "Cube".
Los controles responden adecuadamente a las entradas del usuario.




# Pruebas de integración









Prueba realizada
Resultado
Confirmación




Integración con base de datos
Los datos se almacenan y recuperan correctamente.
Resultados de las consultas y actualizaciones:

Consulta de prueba realizada en 10 ms, recuperación de datos
precisa.
Actualización de registro completada en 20 ms, confirmación de
actualización exitosa.



Comunicación con servidores remotos
La comunicación es estable y sin errores.
Registros de las comunicaciones:

Petición HTTP enviada
Respuesta recibida en 200 ms, sin errores de conexión.



Sincronización de datos entre dispositivos
Los datos se sincronizan adecuadamente.
Confirmación de datos sincronizados correctamente entre dispositivo
A y B.


Autenticación de usuarios
Los usuarios se autentican correctamente.
Autenticación completada en 50 ms, sin errores.


Interacción con una API
Las API responde correctamente.
Respuesta recibida en 300 ms con datos correctos de pacientes


Uso de servicios en la nube
Los servicios en la nube funcionan sin problemas.
Archivo subido y accesible en 5 segundos, sin errores.


Interacción con hardware externo
El hardware responde adecuadamente.
Lecturas de datos recibidas en 100 ms, sin errores de
comunicación.


Sincronización de datos en tiempo real
La sincronización es rápida y sin errores.
Confirmación de sincronización en tiempo real exitosa.


Gestión de sesiones de usuario
Las sesiones se gestionan correctamente.
Registros de inicio y cierre de sesión:

Inicio de sesión de usuario a las 12:00 PM.
Cierre de sesión realizado a las 12:30 PM.
Sesión gestionada sin problemas.



Integración con servicios de almacenamiento
Los datos se almacenan y recuperan sin problemas.
Datos almacenados en la base de datos.
Recuperación de datos completada en 2 segundos, sin errores.


Monitoreo de aplicaciones
El monitoreo se realiza sin interrupciones.
Confirmación de datos de monitoreo recibidos continuamente sin
interrupciones.




# Pruebas de rendimiento









Prueba realizada
Resultado
Confirmación




Carga máxima de usuarios silmutáneos
La aplicación soporta la carga máxima sin degradación.
Registros de tiempos de respuesta y utilización de recursos:

Número de usuarios simultáneos: 50
Tiempo de respuesta promedio: 200 ms
Utilización de CPU: 70%
Utilización de memoria: 65%



Prueba de estrés
El sistema se recupera adecuadamente tras el estrés.
Resultados de pruebas de estrés:

Aplicación sometida a 1000 solicitudes por minuto durante 10
minutos.
Recuperación completa en 5 minutos con todos los servicios
funcionando normalmente.



Prueba de latencia
La latencia se mantiene dentro de límites aceptables.
Resultados de pruebas de latencia:

Latencia promedio: 150 ms
Latencia máxima: 300 ms
Pruebas realizadas bajo diferentes condiciones de red.



Prueba de concurrencia
El sistema maneja múltiples solicitudes concurrentes.
Resultados de pruebas de concurrencia:

1,000 solicitudes concurrentes.
Todas las solicitudes procesadas correctamente sin
errores.



Prueba de uso de memoria
La aplicación maneja adecuadamente el uso de memoria.
Uso de memoria durante la prueba de carga: 65%
Sin fugas de memoria detectadas.


Pruebas de uso de cpu
La aplicación maneja adecuadamente el uso de CPU.
Uso de CPU durante la prueba de carga: 75%


Pruebas de ancho de banda
La aplicación funciona bien con diferentes anchos de banda.
Ancho de banda utilizado: 10 Mbps, 50 Mbps, 100 Mbps.
Rendimiento estable


Prueba de respuesta en diferentes redes
La aplicación responde adecuadamente en diferentes redes.
Resultados de pruebas en varias redes:

Redes probadas: 3G, 4G, 5G, Wi-Fi.
Tiempo de respuesta promedio en 3G: 500 ms
Tiempo de respuesta promedio en 4G: 300 ms
Tiempo de respuesta promedio en 5G y Wi-Fi: 100 ms



Pruebas de tiempo de carga
Los tiempos de carga son aceptables.
Tiempo de carga inicial: 3 segundos


Prueba de tiempo de ejecución de scripts
Los scripts se ejecutan dentro del tiempo esperado.
Registros de tiempos de ejecución de scripts:

Tiempo de ejecución promedio: 50 ms
Tiempo de ejecución máximo: 200 ms



Pruebas de uso de recursos en segundo plano
La aplicación maneja bien los recursos en segundo plano.
Resultados de uso de recursos:

Uso de CPU en segundo plano: 15%
Uso de memoria en segundo plano: 20%





# Verificación de seguridad









Prueba realizada
Resultado
Confirmación




Prueba de acceso no autorizado
El sistema bloquea accesos no autorizados.
Registros de intentos de acceso y bloqueos:

Intentos de acceso no autorizado: 5
Todos los intentos fueron bloqueados correctamente



Pruebas de inyección SQL
El sistema es inmune a inyecciones SQL.
No se logró realizar ninguna inyección SQL.


Pruebas de Cross-Site Scripting (XSS)
No se encuentran vulnerabilidades XSS.
No se encontraron vulnerabilidades XSS.


Pruebas de control de acceso
Los controles de acceso funcionan correctamente.
Usuarios con diferentes roles probados.
Todos los accesos fueron controlados adecuadamente según los
permisos.


Pruebas de seguridad en la comunicación
La comunicación está segura.
Resultados de pruebas de seguridad en la comunicación:

Verificación de SSL/TLS realizada.
Confirmación de comunicación segura sin
vulnerabilidades.



Prueba de integridad de datos
La integridad de los datos está garantizada.
Todos los datos permanecieron íntegros durante la prueba.


Prueba de seguridad de archivos
Los archivos están protegidos contra accesos no autorizados.
Resultados de pruebas de seguridad de archivos:

Accesos a archivos restringidos verificados.
Todos los accesos no autorizados fueron bloqueados.



Prueba de protección contra malware
El sistema está protegido contra malware.
Resultados de pruebas de malware:

Escaneo de malware realizado.
Sistema libre de malware.



Prueba de seguridad en redes
La red es segura.
Red sin vulnerabilidades y con tráfico seguro.


Pruebas de seguridad de configuración
La configuración es segura.
Todas las configuraciones críticas protegidas adecuadamente.




# Cualificación del funcionamiento (PQ)

# Pruebas de aceptación de usuario









Prueba realizada
Resultado
Confirmación




Configuración de parámetros personalizados
Los usuarios configuran parámetros específicos para adaptarse a
diferentes escenarios.
Retroalimentación sobre la facilidad de configuración y
funcionalidad de los parámetros:

Usuario A: "Configurar los parámetros fue sencillo y se adaptaron
bien a mis necesidades."
Usuario B: "La personalización es efectiva, aunque algunas
opciones podrían ser más visibles."
Usuario C: "La funcionalidad es excelente, permite ajustar a
diferentes escenarios fácilmente."



Uso de herramientas de visualización
Los usuarios utilizan herramientas de visualización de datos para
analizar patrones.
Comentarios sobre la efectividad y facilidad de uso de las
herramientas de visualización:

Usuario A: "Las herramientas de visualización son muy efectivas y
fáciles de usar."
Usuario B: "Visualizar los datos fue sencillo, aunque podría
mejorar la interacción."
Usuario C: "Excelente visualización, me ayudó a identificar
patrones clave rápidamente."



Los usuarios evalúan la navegación y usabilidad del software
Los usuarios evalúan la navegación y usabilidad del software de
Unity.
Feedback sobre la interfaz de usuario y facilidad de uso:

Usuario A: "La navegación es intuitiva y la usabilidad es
alta."
Usuario B: "Interfaz amigable, aunque algunos botones podrían
estar mejor ubicados."
Usuario C: "Muy fácil de usar, la interfaz es clara y bien
organizada."





# Pruebas de escenarios críticos









Prueba realizada
Resultado
Confirmación




Recuperación de datos tras un fallo
Se simula un fallo del sistema y se verifica la recuperación de
datos.
Tiempo de recuperación y precisión de los datos recuperados:

Simulación de fallo realizada.
Recuperación de datos completada.
Tiempo de recuperación: 5 minutos.
Todos los datos fueron recuperados con precisión y sin
pérdida.



Análisis en tiempo real
Se evalua el análisis de datos en tiempo real durante operaciones
críticas
Desempeño y precisión del análisis en tiempo real:

Desempeño registrado: Tiempo de respuesta promedio de 50
ms.
Precisión del análisis: 99.5%



Escenarios de alta demanda
Se simulan escenarios de alta demanda y evaluar el rendimiento del
software.
Desempeño del software bajo alta demanda:

Prueba realizada con alta carga de procesamiento
El software manejó la carga sin caídas de rendimiento
significativas.
Tiempo de respuesta promedio: 200 ms.



Gestión de grandes volúmenes de datos
Se evalua la capacidad del software para gestionar y analizar
grandes volúmenes de datos.
Desempeño y precisión en el análisis de grandes volúmenes de
datos:

Prueba realizada con 10 GB de datos.
Desempeño registrado: Procesamiento completado en 30
minutos.
Precisión del análisis: 98.7%





# Evaluación de la documentación del usuario









Prueba realizada
Resultado
Confirmación




Revisión manual de usuario
Verificación de que el manual de usuario cubre todas las
funcionalidades del software.
Todas las funcionalidades principales están cubiertas.


Guía de configuración
Se asegura que la guía de configuración es clara y completa.
La guía cubre todos los pasos necesarios para la configuración
inicial.


Actualización de versiones
Se verifica que la documentación está actualizada con la última
versión del software.
La documentación está completamente actualizada y refleja la última
versión del software.


Guía de solución de problemas
Se evalua la guía de solución de problemas para asegurarse de que
cubre posibles incidencias.
La guía cubre una amplia gama de problemas comunes y sus
soluciones.


Guía de buenas prácticas
Se verifica que la guía de buenas prácticas está completa y es
comprensible.
La guía es comprensible y cubre todas las mejores prácticas
recomendadas.


Tutoriales en video
Se asegura que los tutoriales en video son claros y educativos.
Los tutoriales son claros y bien estructurados.


Documentación de API
Se revisa que la documentación de las API para asegurarse de que es
completa y precisa.
La documentación es completa y precisa, cubriendo todos los
endpoints y ejemplos de uso.




# Resultados y conclusiones

Después de realizar exhaustivas pruebas de instalación (IQ), operación
(OQ) y funcionamiento (PQ), se concluye que el entorno de desarrollo
Unity cumple con los estándares requeridos para el diseño y desarrollo
de software en Spika Tech. Los resultados obtenidos en cada fase de la
validación indican lo siguiente:

-   Instalación Exitosa: La instalación del software Unity se llevó a
    cabo sin incidentes, cumpliendo con los requisitos de hardware y
    software establecidos. Todos los archivos se instalaron
    correctamente y su integridad fue verificada.

-   Operación Satisfactoria: Las pruebas de funcionalidad básica,
    integración, rendimiento y seguridad muestran que Unity opera
    correctamente bajo diversas condiciones. No se encontraron errores
    significativos y todas las funcionalidades principales respondieron
    según lo esperado.

-   Funcionamiento Adecuado: Las pruebas de aceptación de usuario y
    escenarios críticos validan que el entorno es adecuado para el
    desarrollo de aplicaciones de visualización y análisis de señales
    cardíacas. Los usuarios encontraron el software intuitivo y eficaz
    para sus propósitos.

En base a los datos recopilados, se aprueba el uso de Unity para el
diseño y desarrollo de software en Spika Tech, garantizando que cumple
con los criterios de funcionalidad, confiabilidad y seguridad
necesarios.

# Historico de versiones









**VERSION**
**MOTIVO DEL CAMBIO**
**FECHA**




01
Edicion inicial
Junio 2024