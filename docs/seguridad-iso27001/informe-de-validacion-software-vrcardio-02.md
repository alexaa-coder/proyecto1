INFORME DE VALIDACIÓN SOFTWARE

| Función:      | Elaborado por: | Revisado por: | Aprobado por:       |
|---------------|----------------|---------------|---------------------|
| Departamento: | Desarrollo     | Desarrollo    | Garantía de Calidad |
| Nombre:       | Daniel Cámara  | Javier Vico   | Iván Pérez          |
| Firma:        |                |               |                     |
| Fecha:        | 09/08/2024     | 09/08/2024    | 09/08/2024          |

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

- Asegurar que el software cumple con los requisitos de funcionalidad y
  rendimiento establecidos.

- Verificar la confiabilidad y estabilidad del software en diferentes
  condiciones de operación.

- Evaluar la seguridad del software contra vulnerabilidades conocidas y
  potenciales.

# Métodos de validación

Los métodos utilizados para la validación incluyen:

- Pruebas de instalación y configuración.

- Pruebas de funcionalidad básica y avanzada.

- Pruebas de integración y comunicación con otros sistemas.

- Pruebas de rendimiento bajo diferentes cargas.

- Pruebas de seguridad y resistencia a ataques.

# Criterios de aceptación

El software se considerará aceptado si cumple con los siguientes
criterios:

- Instalación y configuración correctas sin errores.

- Funcionamiento correcto de todas las funcionalidades principales.

- Integración exitosa con sistemas externos y hardware.

- Rendimiento adecuado bajo diferentes condiciones de carga.

- Cumplimiento con los estándares de seguridad establecidos.

# Versión del software validado 

Con la realización de este informe de validación software se realiza
para la versión siguiente de VRCardio: 1.0.0.

# Procedimientos de validación

# Cualificación de la instalación (IQ)

# Revisión de la documentación de instalación

Se ha recopilado toda la información disponible para la descarga del
software y primeros pasos para la creación de un proyecto:

- Enlace de descarga: Aún no existe ningún enlace de descarga, hasta que
  la aplicación sea lanzada de forma pública

- Instalación: Descomprimir archivo .zip y abrir el archivo
  VRCardio-VHET360-Visualization.exe

- Requisitos mínimos:

  - Sistema opeativo: Windows 10 64-bit

  - Procesador: 8-Core Intel Core i5 o equivalente

  - RAM: 8 GB o más

  - Para uso sin VR: NVIDIA GeForce GTX 1050 ti o equivalente

  - Para uso con VR: NVIDIA GeForce RTX 2070 o equivalente

  - Espacio de disco: Mínimo 2 GB de espacio libre

Tras ello se ha procedido a la descarga del software y a su posterior
instalación de forma exitosa.

# Comprobación de hardware y software

Para la versión de VRCardio (1.0.0) los requisitos mínimos indicados
para su correcto funcionamiento son:

- Windows 10 o superior

- Arquitectura de x64

- DX10, DX11 o DX12

Los ordenadores en los que se ha instalado y probado este software
cuentan con las siguientes características:

- Windows 10 o Windows 11

- Arquitectura de x64

- DX12

# Registro de la instalación

&lt;table>
&lt;colgroup>
&lt;col style="width: 53%" />
&lt;col style="width: 22%" />
&lt;col style="width: 24%" />
&lt;/colgroup>
&lt;thead>
&lt;tr class="header">
&lt;th>Proceso&lt;/th>
&lt;th>Personal&lt;/th>
&lt;th>Incidencias&lt;/th>
&lt;/tr>
&lt;/thead>
&lt;tbody>
&lt;tr class="odd">
&lt;td>Acceso a la descarga interna
Descarga e instalación del software
Inicio de sesión con cuenta de desarrollo privada
Acceso al software desarrollado&lt;/td>
&lt;td>David Pozo&lt;/td>
&lt;td>Ninguna&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Acceso a la descarga interna
Descarga e instalación del software
Inicio de sesión con cuenta de desarrollo privada
Acceso al software desarrollado&lt;/td>
&lt;td>Daniel Cámara&lt;/td>
&lt;td>Ninguna&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Acceso a la descarga interna
Descarga e instalación del software
Inicio de sesión con cuenta de desarrollo privada
Acceso al software desarrollado&lt;/td>
&lt;td>Javier Vico&lt;/td>
&lt;td>Ninguna&lt;/td>
&lt;/tr>
&lt;/tbody>
&lt;/table>

# 

# Validación de integridad de archivos

Tras cada descarga e instalación del software, se ha accedido a la
carpeta de ruta local para comprobar que todos los archivos existen y
tienen una fecha de modificación acorde a la fecha de la instalación, lo
que corrobora que ningún fichero o archivo ha sufrido modificaciones de
ningún tipo tras la instalación.

# Cualificación de la operación (OQ)

# Pruebas de funcionalidad básica

| Prueba realizada                 | Resultado                                                                       | Confirmación                                                                         |
|----------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Abrir la aplicación.             | La aplicación se abre sin errores.                                              | La aplicación ha iniciado su carga y posterior apertura.                             |
| Iniciar sesión.                  | El usuario incia sesión sin problema.                                           | El usuario accede a su cuenta correctamente.                                         |
| Cerrar sesión.                   | El usuario sale de su cuenta.                                                   | El usuario cierra sesión correctamente y vuelve a la pantalla de iniciar sesión.     |
| Acceder a una sala offline.      | El usuario crea una sala offline y accede a ella correctamente.                 | El usuario puede interactuar con los paneles de la sala sin problema.                |
| Cargar un caso                   | El usuario accede al listado de casos, carga uno de ellos y aparece en pantalla | El usuario puede visualizar e interactuar el caso sin problema.                      |
| Ver y manejar señales cardíacas. | El usuario accede a las señales y puede visualizarlas sin problema              | Las señales se han representado correctamente en la gráfica.                         |
| Manejar el tiempo                | El usuario ha podido manejar el tiempo de la sesión mediante los controladores. | El tiempo ha respondido correctamente a las accines del usuario.                     |
| Usar gafas de VR                 | El usuario ha entrado correctamente a una sala usando gafas VR                  | El usuario visualiza la escena correctamente usando gafas VR                         |
| Usar pantalla holográfica        | El usuario ha entrado correctamente a una sala usando una pantalla holográfica  | El usuario visualiza la escena correctamente usando una pantalla holográfica         |
| Acceder a una sala online        | El usuario accede a una sala online mediante el código                          | El usuario puede visualizar la escena online junto al puntero del resto de usuarios. |
| Modificar posición de paneles    | El usario ha podipo mover y rotar los paneles de la sala sin problema.          | Los paneles han sido modificados en posición y rotación.                             |
| Ocultar y mostrar paneles        | El usuario ha ocultado varios paneles sin problema                              | Los paneles han aparecido y desaparecido a gusto del usuario.                        |

# Pruebas de integración

&lt;table>
&lt;colgroup>
&lt;col style="width: 33%" />
&lt;col style="width: 33%" />
&lt;col style="width: 33%" />
&lt;/colgroup>
&lt;thead>
&lt;tr class="header">
&lt;th>Prueba realizada&lt;/th>
&lt;th>Resultado&lt;/th>
&lt;th>Confirmación&lt;/th>
&lt;/tr>
&lt;/thead>
&lt;tbody>
&lt;tr class="odd">
&lt;td>Integración con base de datos&lt;/td>
&lt;td>Los datos se almacenan y recuperan correctamente.&lt;/td>
&lt;td>Resultados de las consultas y actualizaciones:
&lt;ul>
&lt;li>Consulta de prueba realizada en 10 ms, recuperación de datos
precisa.&lt;/li>
&lt;li>Actualización de registro completada en 20 ms, confirmación de
actualización exitosa.&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Comunicación con servidores remotos&lt;/td>
&lt;td>La comunicación es estable y sin errores.&lt;/td>
&lt;td>Registros de las comunicaciones:
&lt;ul>
&lt;li>Petición HTTP enviada&lt;/li>
&lt;li>Respuesta recibida en 200 ms, sin errores de conexión.&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Sincronización de datos entre dispositivos&lt;/td>
&lt;td>Los datos se sincronizan adecuadamente.&lt;/td>
&lt;td>Confirmación de datos sincronizados correctamente entre dispositivo
A y B.&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Autenticación de usuarios&lt;/td>
&lt;td>Los usuarios se autentican correctamente.&lt;/td>
&lt;td>Autenticación completada en 50 ms, sin errores.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Interacción con una API&lt;/td>
&lt;td>Las API responde correctamente.&lt;/td>
&lt;td>Respuesta recibida en 300 ms con datos correctos de pacientes&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Uso de servicios en la nube&lt;/td>
&lt;td>Los servicios en la nube funcionan sin problemas.&lt;/td>
&lt;td>Archivo subido y accesible en 5 segundos, sin errores.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Interacción con hardware externo&lt;/td>
&lt;td>El hardware responde adecuadamente.&lt;/td>
&lt;td>Lecturas de datos recibidas en 100 ms, sin errores de
comunicación.&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Sincronización de datos en tiempo real&lt;/td>
&lt;td>La sincronización es rápida y sin errores.&lt;/td>
&lt;td>Confirmación de sincronización en tiempo real exitosa.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Gestión de sesiones de usuario&lt;/td>
&lt;td>Las sesiones se gestionan correctamente.&lt;/td>
&lt;td>Registros de inicio y cierre de sesión:
&lt;ul>
&lt;li>Inicio de sesión de usuario a las 12:00 PM.&lt;/li>
&lt;li>Cierre de sesión realizado a las 12:30 PM.&lt;/li>
&lt;li>Sesión gestionada sin problemas.&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Integración con servicios de almacenamiento&lt;/td>
&lt;td>Los datos se almacenan y recuperan sin problemas.&lt;/td>
&lt;td>Datos almacenados en la base de datos.
Recuperación de datos completada en 2 segundos, sin errores.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Monitoreo de aplicaciones&lt;/td>
&lt;td>El monitoreo se realiza sin interrupciones.&lt;/td>
&lt;td>Confirmación de datos de monitoreo recibidos continuamente sin
interrupciones.&lt;/td>
&lt;/tr>
&lt;/tbody>
&lt;/table>

# Pruebas de rendimiento

&lt;table>
&lt;colgroup>
&lt;col style="width: 33%" />
&lt;col style="width: 33%" />
&lt;col style="width: 33%" />
&lt;/colgroup>
&lt;thead>
&lt;tr class="header">
&lt;th>Prueba realizada&lt;/th>
&lt;th>Resultado&lt;/th>
&lt;th>Confirmación&lt;/th>
&lt;/tr>
&lt;/thead>
&lt;tbody>
&lt;tr class="odd">
&lt;td>Carga máxima de usuarios silmutáneos&lt;/td>
&lt;td>La aplicación soporta la carga máxima sin degradación.&lt;/td>
&lt;td>Registros de tiempos de respuesta y utilización de recursos:
&lt;ul>
&lt;li>Número de usuarios simultáneos: 50&lt;/li>
&lt;li>Tiempo de respuesta promedio: 200 ms&lt;/li>
&lt;li>Utilización de CPU: 70%&lt;/li>
&lt;li>Utilización de memoria: 65%&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Prueba de estrés&lt;/td>
&lt;td>El sistema se recupera adecuadamente tras el estrés.&lt;/td>
&lt;td>Resultados de pruebas de estrés:
&lt;ul>
&lt;li>Aplicación sometida a carga de archivos pesados&lt;/li>
&lt;li>Recuperación completa a un estado normal en segundos.&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Prueba de latencia&lt;/td>
&lt;td>La latencia se mantiene dentro de límites aceptables.&lt;/td>
&lt;td>Resultados de pruebas de latencia:
&lt;ul>
&lt;li>Latencia promedio: 150 ms&lt;/li>
&lt;li>Latencia máxima: 300 ms&lt;/li>
&lt;li>Pruebas realizadas bajo diferentes condiciones de red.&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Prueba de concurrencia&lt;/td>
&lt;td>El sistema maneja múltiples solicitudes concurrentes.&lt;/td>
&lt;td>Resultados de pruebas de concurrencia:
&lt;ul>
&lt;li>1,000 solicitudes concurrentes.&lt;/li>
&lt;li>Todas las solicitudes procesadas correctamente sin
errores.&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Prueba de uso de memoria&lt;/td>
&lt;td>La aplicación maneja adecuadamente el uso de memoria.&lt;/td>
&lt;td>Uso de memoria durante la prueba de carga: 65%
Sin fugas de memoria detectadas.&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Pruebas de uso de cpu&lt;/td>
&lt;td>La aplicación maneja adecuadamente el uso de CPU.&lt;/td>
&lt;td>Uso de CPU durante la prueba de carga: 75%&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Pruebas de ancho de banda&lt;/td>
&lt;td>La aplicación funciona bien con diferentes anchos de banda.&lt;/td>
&lt;td>Ancho de banda utilizado: 10 Mbps, 50 Mbps, 100 Mbps.
Rendimiento estable&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Prueba de respuesta en diferentes redes&lt;/td>
&lt;td>La aplicación responde adecuadamente en diferentes redes.&lt;/td>
&lt;td>Resultados de pruebas en varias redes:
&lt;ul>
&lt;li>Redes probadas: 3G, 4G, 5G, Wi-Fi.&lt;/li>
&lt;li>Tiempo de respuesta promedio en 3G: 500 ms&lt;/li>
&lt;li>Tiempo de respuesta promedio en 4G: 300 ms&lt;/li>
&lt;li>Tiempo de respuesta promedio en 5G y Wi-Fi: 100 ms&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Pruebas de tiempo de carga&lt;/td>
&lt;td>Los tiempos de carga son aceptables.&lt;/td>
&lt;td>Tiempo de carga inicial: 6 segundos&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Prueba de tiempo de ejecución de scripts&lt;/td>
&lt;td>Los scripts se ejecutan dentro del tiempo esperado.&lt;/td>
&lt;td>Registros de tiempos de ejecución de scripts:
&lt;ul>
&lt;li>Tiempo de ejecución promedio: 50 ms&lt;/li>
&lt;li>Tiempo de ejecución máximo: 200 ms&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Pruebas de uso de recursos en segundo plano&lt;/td>
&lt;td>La aplicación maneja bien los recursos en segundo plano.&lt;/td>
&lt;td>Resultados de uso de recursos:
&lt;ul>
&lt;li>Uso de CPU en segundo plano: 30%&lt;/li>
&lt;li>Uso de memoria en segundo plano: 35%&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;/tbody>
&lt;/table>

# Verificación de seguridad

&lt;table>
&lt;colgroup>
&lt;col style="width: 33%" />
&lt;col style="width: 33%" />
&lt;col style="width: 33%" />
&lt;/colgroup>
&lt;thead>
&lt;tr class="header">
&lt;th>Prueba realizada&lt;/th>
&lt;th>Resultado&lt;/th>
&lt;th>Confirmación&lt;/th>
&lt;/tr>
&lt;/thead>
&lt;tbody>
&lt;tr class="odd">
&lt;td>Prueba de acceso no autorizado&lt;/td>
&lt;td>El sistema bloquea accesos no autorizados.&lt;/td>
&lt;td>Registros de intentos de acceso y bloqueos:
&lt;ul>
&lt;li>Todos los intentos fueron bloqueados correctamente&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Pruebas de inyección SQL&lt;/td>
&lt;td>El sistema es inmune a inyecciones SQL.&lt;/td>
&lt;td>No se logró realizar ninguna inyección SQL.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Pruebas de Cross-Site Scripting (XSS)&lt;/td>
&lt;td>No se encuentran vulnerabilidades XSS.&lt;/td>
&lt;td>No se encontraron vulnerabilidades XSS.&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Pruebas de control de acceso&lt;/td>
&lt;td>Los controles de acceso funcionan correctamente.&lt;/td>
&lt;td>Usuarios con diferentes roles probados.
Todos los accesos fueron controlados adecuadamente según los
permisos.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Prueba de integridad de datos&lt;/td>
&lt;td>La integridad de los datos está garantizada.&lt;/td>
&lt;td>Todos los datos permanecieron íntegros durante la prueba.&lt;/td>
&lt;/tr>
&lt;/tbody>
&lt;/table>

# Cualificación del funcionamiento (PQ)

# Pruebas de aceptación de usuario

&lt;table>
&lt;colgroup>
&lt;col style="width: 33%" />
&lt;col style="width: 33%" />
&lt;col style="width: 33%" />
&lt;/colgroup>
&lt;thead>
&lt;tr class="header">
&lt;th>Prueba realizada&lt;/th>
&lt;th>Resultado&lt;/th>
&lt;th>Confirmación&lt;/th>
&lt;/tr>
&lt;/thead>
&lt;tbody>
&lt;tr class="odd">
&lt;td>Instalación y ejecución del software&lt;/td>
&lt;td>Los usuarios descargan, instalan y ejecutan la aplicación sin
problema&lt;/td>
&lt;td>Retroalimentación sobre la facilidad de configuración y
funcionalidad de los parámetros:
&lt;ul>
&lt;li>Usuario A: "Fue muy sencillo el proceso."&lt;/li>
&lt;li>Usuario B: "Pude instalar la aplicación sin problema."&lt;/li>
&lt;li>Usuario C: "Descargar e instalar la app es sencillo."&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Uso de los paneles de visualización&lt;/td>
&lt;td>Los usuarios utilizan los paneles de visualización de datos para
analizar patrones.&lt;/td>
&lt;td>Comentarios sobre la efectividad y facilidad de uso de los
paneles de visualización:
&lt;ul>
&lt;li>Usuario A: " los paneles son útiles y fácile de usar."&lt;/li>
&lt;li>Usuario B: "Es muy cómodo usar los paneles para cambiar la
visualización."&lt;/li>
&lt;li>Usuario C: "Me ha gustado la experiencia al manejar los
paneles."&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Los usuarios evalúan la navegación y usabilidad del software&lt;/td>
&lt;td>Los usuarios evalúan la navegación y usabilidad del software de
VRCardio.&lt;/td>
&lt;td>Feedback sobre la interfaz de usuario y facilidad de uso:
&lt;ul>
&lt;li>Usuario A: "Ha sido intuitivo y cómoda."&lt;/li>
&lt;li>Usuario B: "La aplicación tiene buena usabilidad."&lt;/li>
&lt;li>Usuario C: "Fácil de usar y fácil de manejar."&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;/tbody>
&lt;/table>

# Pruebas de escenarios críticos

&lt;table>
&lt;colgroup>
&lt;col style="width: 33%" />
&lt;col style="width: 33%" />
&lt;col style="width: 33%" />
&lt;/colgroup>
&lt;thead>
&lt;tr class="header">
&lt;th>Prueba realizada&lt;/th>
&lt;th>Resultado&lt;/th>
&lt;th>Confirmación&lt;/th>
&lt;/tr>
&lt;/thead>
&lt;tbody>
&lt;tr class="odd">
&lt;td>Recuperación de datos tras un fallo&lt;/td>
&lt;td>Se simula un fallo del sistema y se verifica la recuperación de
datos.&lt;/td>
&lt;td>Tiempo de recuperación y precisión de los datos recuperados:
&lt;ul>
&lt;li>Simulación de fallo realizada.&lt;/li>
&lt;li>Recuperación de datos completada.&lt;/li>
&lt;li>Tiempo de recuperación: 1 minutos.&lt;/li>
&lt;li>Todos los datos fueron recuperados con precisión y sin
pérdida.&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Análisis en tiempo real&lt;/td>
&lt;td>Se evalua el análisis de datos en tiempo real durante operaciones
críticas&lt;/td>
&lt;td>Desempeño y precisión del análisis en tiempo real:
&lt;ul>
&lt;li>Desempeño registrado: Tiempo de respuesta promedio de 50
ms.&lt;/li>
&lt;li>Precisión del análisis: 99.5%&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Escenarios de alta demanda&lt;/td>
&lt;td>Se simulan escenarios de alta demanda y evaluar el rendimiento del
software.&lt;/td>
&lt;td>Desempeño del software bajo alta demanda:
&lt;ul>
&lt;li>Prueba realizada con alta carga de procesamiento&lt;/li>
&lt;li>El software manejó la carga sin caídas de rendimiento
significativas.&lt;/li>
&lt;li>Tiempo de respuesta promedio: 200 ms.&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Gestión de grandes volúmenes de datos&lt;/td>
&lt;td>Se evalua la capacidad del software para gestionar y analizar
grandes volúmenes de datos.&lt;/td>
&lt;td>Desempeño y precisión en el análisis de grandes volúmenes de
datos:
&lt;ul>
&lt;li>Prueba realizada con 10 GB de datos.&lt;/li>
&lt;li>Desempeño registrado: Procesamiento completado en 30
minutos.&lt;/li>
&lt;li>Precisión del análisis: 98.7%&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;/tbody>
&lt;/table>

# Evaluación de la documentación del usuario

| Prueba realizada           | Resultado                                                                              | Confirmación                                                              |
|----------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Revisión manual de usuario | Verificación de que el manual de usuario cubre todas las funcionalidades del software. | Todas las funcionalidades principales están cubiertas.                    |
| Guía de configuración      | Se asegura que la guía de configuración es clara y completa.                           | La guía cubre todos los pasos necesarios para la configuración inicial.   |
| Guía de buenas prácticas   | Se verifica que la guía de buenas prácticas está completa y es comprensible.           | La guía es comprensible y cubre todas las mejores prácticas recomendadas. |
| Tutoriales en video        | Se asegura que los tutoriales en video son claros y educativos.                        | Los tutoriales son claros y bien estructurados.                           |

# Resultados y conclusiones

Después de realizar exhaustivas pruebas de instalación (IQ), operación
(OQ) y funcionamiento (PQ), se concluye que VRCardio cumple con los
estándares requeridos para su uso con finalidad médica. Los resultados
obtenidos en cada fase de la validación indican lo siguiente:

- Instalación Exitosa: La instalación de VRCardio se llevó a cabo sin
  incidentes, cumpliendo con los requisitos de hardware y software
  establecidos. Todos los archivos se instalaron correctamente y su
  integridad fue verificada.

- Operación Satisfactoria: Las pruebas de funcionalidad básica,
  integración, rendimiento y seguridad muestran que VRCardio opera
  correctamente bajo diversas condiciones. No se encontraron errores
  significativos y todas las funcionalidades principales respondieron
  según lo esperado.

- Funcionamiento Adecuado: Las pruebas de aceptación de usuario y
  escenarios críticos validan que el entorno es adecuado para el
  desarrollo de aplicaciones de visualización y análisis de señales
  cardíacas. Los usuarios encontraron el software intuitivo y eficaz
  para sus propósitos.

En base a los datos recopilados, se aprueba el uso de VRCardio,
garantizando que cumple con los criterios de funcionalidad,
confiabilidad y seguridad necesarios.

# Historico de versiones

| **VERSION** | **MOTIVO DEL CAMBIO** | **FECHA**  |
|-------------|-----------------------|------------|
| 01          | Edicion inicial       | Julio 2024 |

# Conformidad del responsable de la validación

Estado:

☐ Conforme

☐ No conforme

Nombre:

Fecha:

Firma: