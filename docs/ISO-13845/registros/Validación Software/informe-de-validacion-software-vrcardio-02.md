INFORME DE VALIDACIÓN SOFTWARE










Función:
Elaborado por:
Revisado por:
Aprobado por:




Departamento:
Desarrollo
Desarrollo
Garantía de Calidad


Nombre:
Daniel Cámara
Javier Vico
Iván Pérez


Firma:





Fecha:
09/08/2024
09/08/2024
09/08/2024




# Contenido

[1. Introducción [4](#introducción)](#introducción)

[2. Alcance [4](#alcance)](#alcance)

[3. Definiciones [4](#definiciones)](#definiciones)

[4. Plan de validación [4](#plan-de-validación)](#plan-de-validación)

[4.1. Objetivos [4](#objetivos)](#objetivos)

[4.2. Métodos de validación
[5](#métodos-de-validación)](#métodos-de-validación)

[4.3. Criterios de aceptación
[5](#criterios-de-aceptación)](#criterios-de-aceptación)

[4.4. Versión del software validado
[5](#versión-del-software-validado)](#versión-del-software-validado)

[5. Procedimientos de validación
[6](#procedimientos-de-validación)](#procedimientos-de-validación)

[5.1. Cualificación de la instalación (IQ)
[6](#cualificación-de-la-instalación-iq)](#cualificación-de-la-instalación-iq)

[5.1.1. Revisión de la documentación de instalación
[6](#revisión-de-la-documentación-de-instalación)](#revisión-de-la-documentación-de-instalación)

[5.1.2. Comprobación de hardware y software
[6](#comprobación-de-hardware-y-software)](#comprobación-de-hardware-y-software)

[5.1.3. Registro de la instalación
[7](#registro-de-la-instalación)](#registro-de-la-instalación)

[5.1.4. Validación de integridad de archivos
[7](#validación-de-integridad-de-archivos)](#validación-de-integridad-de-archivos)

[5.2. Cualificación de la operación (OQ)
[8](#cualificación-de-la-operación-oq)](#cualificación-de-la-operación-oq)

[5.2.1. Pruebas de funcionalidad básica
[8](#pruebas-de-funcionalidad-básica)](#pruebas-de-funcionalidad-básica)

[5.2.2. Pruebas de integración
[9](#pruebas-de-integración)](#pruebas-de-integración)

[5.2.3. Pruebas de rendimiento
[11](#pruebas-de-rendimiento)](#pruebas-de-rendimiento)

[5.2.4. Verificación de seguridad
[14](#verificación-de-seguridad)](#verificación-de-seguridad)

[5.3. Cualificación del funcionamiento (PQ)
[15](#cualificación-del-funcionamiento-pq)](#cualificación-del-funcionamiento-pq)

[5.3.1. Pruebas de aceptación de usuario
[15](#pruebas-de-aceptación-de-usuario)](#pruebas-de-aceptación-de-usuario)

[5.3.2. Pruebas de escenarios críticos
[16](#pruebas-de-escenarios-críticos)](#pruebas-de-escenarios-críticos)

[5.3.3. Evaluación de la documentación del usuario
[18](#evaluación-de-la-documentación-del-usuario)](#evaluación-de-la-documentación-del-usuario)

[6. Resultados y conclusiones
[18](#resultados-y-conclusiones)](#resultados-y-conclusiones)

[7. Historico de versiones
[19](#historico-de-versiones)](#historico-de-versiones)

[8. Conformidad del responsable de la validación
[19](#conformidad-del-responsable-de-la-validación)](#conformidad-del-responsable-de-la-validación)

# Introducción

Este informe presenta los resultados de la validación del software
VRCardio VHET360, en adelante VRCardio, desarrollado por Spika Tech, en
adelante SPIKA, específicamente diseñado para la visualización y
análisis de señales cardíacas. La validación comprueba que VRCardio
cumpla con los estándares de funcionalidad, confiabilidad y seguridad
necesarios.

# Alcance

La validación abarca todos los aspectos del entorno VRCardio,
centrándose en tres áreas clave: funcionalidad, confiabilidad y
seguridad. Incluye la verificación de todas las funciones del entorno,
la detección de errores críticos y la evaluación de la seguridad contra
vulnerabilidades conocidas.

# Definiciones

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

Los objetivos principales de la validación del software VRCardio son:

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

# Versión del software validado 

Con la realización de este informe de validación software se realiza
para la versión siguiente de VRCardio: 1.0.0.

# Procedimientos de validación

# Cualificación de la instalación (IQ)

# Revisión de la documentación de instalación

Se ha recopilado toda la información disponible para la descarga del
software y primeros pasos para la creación de un proyecto:

-   Enlace de descarga: Aún no existe ningún enlace de descarga, hasta
    que la aplicación sea lanzada de forma pública

-   Instalación: Descomprimir archivo .zip y abrir el archivo
    VRCardio-VHET360-Visualization.exe

-   Requisitos mínimos:

    -   Sistema opeativo: Windows 10 64-bit

    -   Procesador: 8-Core Intel Core i5 o equivalente

    -   RAM: 8 GB o más

    -   Para uso sin VR: NVIDIA GeForce GTX 1050 ti o equivalente

    -   Para uso con VR: NVIDIA GeForce RTX 2070 o equivalente

    -   Espacio de disco: Mínimo 2 GB de espacio libre

Tras ello se ha procedido a la descarga del software y a su posterior
instalación de forma exitosa.

# Comprobación de hardware y software

Para la versión de VRCardio (1.0.0) los requisitos mínimos indicados
para su correcto funcionamiento son:

-   Windows 10 o superior

-   Arquitectura de x64

-   DX10, DX11 o DX12

Los ordenadores en los que se ha instalado y probado este software
cuentan con las siguientes características:

-   Windows 10 o Windows 11

-   Arquitectura de x64

-   DX12

# Registro de la instalación









Proceso
Personal
Incidencias




Acceso a la descarga interna
Descarga e instalación del software
Inicio de sesión con cuenta de desarrollo privada
Acceso al software desarrollado
David Pozo
Ninguna


Acceso a la descarga interna
Descarga e instalación del software
Inicio de sesión con cuenta de desarrollo privada
Acceso al software desarrollado
Daniel Cámara
Ninguna


Acceso a la descarga interna
Descarga e instalación del software
Inicio de sesión con cuenta de desarrollo privada
Acceso al software desarrollado
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




Abrir la aplicación.
La aplicación se abre sin errores.
La aplicación ha iniciado su carga y posterior apertura.


Iniciar sesión.
El usuario incia sesión sin problema.
El usuario accede a su cuenta correctamente.


Cerrar sesión.
El usuario sale de su cuenta.
El usuario cierra sesión correctamente y vuelve a la pantalla de
iniciar sesión.


Acceder a una sala offline.
El usuario crea una sala offline y accede a ella correctamente.
El usuario puede interactuar con los paneles de la sala sin
problema.


Cargar un caso
El usuario accede al listado de casos, carga uno de ellos y aparece
en pantalla
El usuario puede visualizar e interactuar el caso sin problema.


Ver y manejar señales cardíacas.
El usuario accede a las señales y puede visualizarlas sin
problema
Las señales se han representado correctamente en la gráfica.


Manejar el tiempo
El usuario ha podido manejar el tiempo de la sesión mediante los
controladores.
El tiempo ha respondido correctamente a las accines del
usuario.


Usar gafas de VR
El usuario ha entrado correctamente a una sala usando gafas VR
El usuario visualiza la escena correctamente usando gafas VR


Usar pantalla holográfica
El usuario ha entrado correctamente a una sala usando una pantalla
holográfica
El usuario visualiza la escena correctamente usando una pantalla
holográfica


Acceder a una sala online
El usuario accede a una sala online mediante el código
El usuario puede visualizar la escena online junto al puntero del
resto de usuarios.


Modificar posición de paneles
El usario ha podipo mover y rotar los paneles de la sala sin
problema.
Los paneles han sido modificados en posición y rotación.


Ocultar y mostrar paneles
El usuario ha ocultado varios paneles sin problema
Los paneles han aparecido y desaparecido a gusto del usuario.




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

Aplicación sometida a carga de archivos pesados
Recuperación completa a un estado normal en segundos.



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
Tiempo de carga inicial: 6 segundos


Prueba de tiempo de ejecución de scripts
Los scripts se ejecutan dentro del tiempo esperado.
Registros de tiempos de ejecución de scripts:

Tiempo de ejecución promedio: 50 ms
Tiempo de ejecución máximo: 200 ms



Pruebas de uso de recursos en segundo plano
La aplicación maneja bien los recursos en segundo plano.
Resultados de uso de recursos:

Uso de CPU en segundo plano: 30%
Uso de memoria en segundo plano: 35%





# Verificación de seguridad









Prueba realizada
Resultado
Confirmación




Prueba de acceso no autorizado
El sistema bloquea accesos no autorizados.
Registros de intentos de acceso y bloqueos:

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


Prueba de integridad de datos
La integridad de los datos está garantizada.
Todos los datos permanecieron íntegros durante la prueba.




# Cualificación del funcionamiento (PQ)

# Pruebas de aceptación de usuario









Prueba realizada
Resultado
Confirmación




Instalación y ejecución del software
Los usuarios descargan, instalan y ejecutan la aplicación sin
problema
Retroalimentación sobre la facilidad de configuración y
funcionalidad de los parámetros:

Usuario A: "Fue muy sencillo el proceso."
Usuario B: "Pude instalar la aplicación sin problema."
Usuario C: "Descargar e instalar la app es sencillo."



Uso de los paneles de visualización
Los usuarios utilizan los paneles de visualización de datos para
analizar patrones.
Comentarios sobre la efectividad y facilidad de uso de los
paneles de visualización:

Usuario A: " los paneles son útiles y fácile de usar."
Usuario B: "Es muy cómodo usar los paneles para cambiar la
visualización."
Usuario C: "Me ha gustado la experiencia al manejar los
paneles."



Los usuarios evalúan la navegación y usabilidad del software
Los usuarios evalúan la navegación y usabilidad del software de
VRCardio.
Feedback sobre la interfaz de usuario y facilidad de uso:

Usuario A: "Ha sido intuitivo y cómoda."
Usuario B: "La aplicación tiene buena usabilidad."
Usuario C: "Fácil de usar y fácil de manejar."





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
Tiempo de recuperación: 1 minutos.
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


Guía de buenas prácticas
Se verifica que la guía de buenas prácticas está completa y es
comprensible.
La guía es comprensible y cubre todas las mejores prácticas
recomendadas.


Tutoriales en video
Se asegura que los tutoriales en video son claros y educativos.
Los tutoriales son claros y bien estructurados.




# Resultados y conclusiones

Después de realizar exhaustivas pruebas de instalación (IQ), operación
(OQ) y funcionamiento (PQ), se concluye que VRCardio cumple con los
estándares requeridos para su uso con finalidad médica. Los resultados
obtenidos en cada fase de la validación indican lo siguiente:

-   Instalación Exitosa: La instalación de VRCardio se llevó a cabo sin
    incidentes, cumpliendo con los requisitos de hardware y software
    establecidos. Todos los archivos se instalaron correctamente y su
    integridad fue verificada.

-   Operación Satisfactoria: Las pruebas de funcionalidad básica,
    integración, rendimiento y seguridad muestran que VRCardio opera
    correctamente bajo diversas condiciones. No se encontraron errores
    significativos y todas las funcionalidades principales respondieron
    según lo esperado.

-   Funcionamiento Adecuado: Las pruebas de aceptación de usuario y
    escenarios críticos validan que el entorno es adecuado para el
    desarrollo de aplicaciones de visualización y análisis de señales
    cardíacas. Los usuarios encontraron el software intuitivo y eficaz
    para sus propósitos.

En base a los datos recopilados, se aprueba el uso de VRCardio,
garantizando que cumple con los criterios de funcionalidad,
confiabilidad y seguridad necesarios.

# Historico de versiones









**VERSION**
**MOTIVO DEL CAMBIO**
**FECHA**




01
Edicion inicial
Julio 2024




# Conformidad del responsable de la validación

Estado:

☐ Conforme

☐ No conforme

Nombre:

Fecha:

Firma: