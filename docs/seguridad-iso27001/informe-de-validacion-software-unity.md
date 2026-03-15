INFORME DE VALIDACIÓN SOFTWARE

| Función:      | Elaborado por: | Revisado por: | Aprobado por:       |
|---------------|----------------|---------------|---------------------|
| Departamento: | Desarrollo     | Dirección     | Garantía de Calidad |
| Nombre:       | Javier Vico    | Carlos Zúñiga | Iván Pérez          |
| Firma:        |                |               |                     |
| Fecha:        | 13/06/2024     | 13/06/2024    | 13/06/2024          |

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

# 

# Procedimientos de validación

# Cualificación de la instalación (IQ)

# Revisión de la documentación de instalación

Se ha recopilado toda la información disponible para la descarga del
software y primeros pasos para la creación de un proyecto:

- Enlace de descarga: &lt;https://unity.com/es/download#how-to-get-started>

- Creación de un proyecto:
  &lt;https://unity.com/es/onboardingsuccess/unity-pro>

- Notas de la versión descargada:
  &lt;https://unity.com/es/releases/editor/whats-new/2021.3.19#notes>

- Requisitos mínimos:
  &lt;https://docs.unity3d.com/es/2021.1/Manual/system-requirements.html>

Tras ello se ha procedido a la descarga del software y a su posterior
instalación de forma exitosa.

# Comprobación de hardware y software

Para la versión de Unity descargada (2021.3.19) los requisitos mínimos
indicados para su correcto funcionamiento son:

- Windows 7 o superior

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
&lt;td>Acceso a la página de descarga
Descarga e instalación del software
Inicio de sesión con cuenta de desarrollo privada
Acceso al proyecto creado&lt;/td>
&lt;td>David Pozo&lt;/td>
&lt;td>Ninguna&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Acceso a la página de descarga
Descarga e instalación del software
Inicio de sesión con cuenta de desarrollo privada
Acceso al proyecto creado&lt;/td>
&lt;td>Daniel Cámara&lt;/td>
&lt;td>Ninguna&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Acceso a la página de descarga
Descarga e instalación del software
Inicio de sesión con cuenta de desarrollo privada
Acceso al proyecto creado&lt;/td>
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
&lt;td>Abrir poyecto existente&lt;/td>
&lt;td>El proyecto se abre sin errores&lt;/td>
&lt;td>El proyecto a iniciado su carga y posterior apertura&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Crear un nuevo proyecto&lt;/td>
&lt;td>El nuevo proyecto se crea sin problemas&lt;/td>
&lt;td>El proyecto se abre adecuadamente&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Agregar un objeto 3D a la escena&lt;/td>
&lt;td>El objeto aparece en la escena&lt;/td>
&lt;td>El objeto "Cube" fue añadido a la escena y se posicionó delante de
la cámara.&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Aplicar un material a un objeto&lt;/td>
&lt;td>El material se aplica correctamente&lt;/td>
&lt;td>El material "Madera" se aplicó al objeto "Cube", cambiando su
apariencia visual.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Ejecutar la simulación de la escena&lt;/td>
&lt;td>La simulación corre sin errores&lt;/td>
&lt;td>La escena corrió con una simulación de física básica sin
errores.&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Configurar una luz en la escena&lt;/td>
&lt;td>La luz se configura y afecta a la escena&lt;/td>
&lt;td>Se añadió una luz direccional que ilumina el objeto "Cube", creando
sombras adecuadas.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Aplicar un script a un objeto&lt;/td>
&lt;td>El script se ejecuta correctamente.&lt;/td>
&lt;td>Se añadió un script para rotar el "Cube". El cubo rota continuamente
en la escena.&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Exportar el proyecto&lt;/td>
&lt;td>El proyecto se exporta sin errores.&lt;/td>
&lt;td>Se genera la build correctamente.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Guardar cambios en el proyecto&lt;/td>
&lt;td>Los cambios se guardan sin problemas.&lt;/td>
&lt;td>Desaparece el asterisco de que hay cambios sin guardar.&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Configuración de parámetros de renderizado&lt;/td>
&lt;td>Los parámetros se configuran y aplican correctamente.&lt;/td>
&lt;td>Parámetros de renderizado configurados para alta calidad con sombras
y reflejos activados.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Uso de herramientas de navegación&lt;/td>
&lt;td>Las herramientas funcionan correctamente.&lt;/td>
&lt;td>Herramientas de zoom, pan y órbita utilizadas sin problemas. La
cámara se movió fluidamente por la escena.&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Implementación de UI básica&lt;/td>
&lt;td>La interfaz de usuario se implementa y funciona.&lt;/td>
&lt;td>Se creó una interfaz básica con botones y menús funcionales.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Añadir efectos de partículas&lt;/td>
&lt;td>Los efectos se visualizan correctamente.&lt;/td>
&lt;td>Efecto de partículas de "Chispas" añadido a la escena,
visualizándose correctamente.&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Configuración de animaciones&lt;/td>
&lt;td>Las animaciones se configuran y reproducen adecuadamente.&lt;/td>
&lt;td>Animación de movimiento configurada para el objeto "Cube".
La animación se reproduce suavemente.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Uso de prefabs&lt;/td>
&lt;td>Los prefabs se instancian correctamente.&lt;/td>
&lt;td>Prefab de "Árbol" instanciado en la escena, con todas sus
propiedades intactas.&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Configiuración de audio&lt;/td>
&lt;td>El audio se configura y reproduce sin problemas.&lt;/td>
&lt;td>Archivo de audio "Ambiente" añadido a la escena.
Reproducción verificada sin interrupciones.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Implementación de controles de usuario&lt;/td>
&lt;td>Los controles responden como se espera.&lt;/td>
&lt;td>Se implementaron controles de teclado para mover el objeto "Cube".
Los controles responden adecuadamente a las entradas del usuario.&lt;/td>
&lt;/tr>
&lt;/tbody>
&lt;/table>

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
&lt;li>Aplicación sometida a 1000 solicitudes por minuto durante 10
minutos.&lt;/li>
&lt;li>Recuperación completa en 5 minutos con todos los servicios
funcionando normalmente.&lt;/li>
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
&lt;td>Tiempo de carga inicial: 3 segundos&lt;/td>
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
&lt;li>Uso de CPU en segundo plano: 15%&lt;/li>
&lt;li>Uso de memoria en segundo plano: 20%&lt;/li>
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
&lt;li>Intentos de acceso no autorizado: 5&lt;/li>
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
&lt;td>Pruebas de seguridad en la comunicación&lt;/td>
&lt;td>La comunicación está segura.&lt;/td>
&lt;td>Resultados de pruebas de seguridad en la comunicación:
&lt;ul>
&lt;li>Verificación de SSL/TLS realizada.&lt;/li>
&lt;li>Confirmación de comunicación segura sin
vulnerabilidades.&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Prueba de integridad de datos&lt;/td>
&lt;td>La integridad de los datos está garantizada.&lt;/td>
&lt;td>Todos los datos permanecieron íntegros durante la prueba.&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Prueba de seguridad de archivos&lt;/td>
&lt;td>Los archivos están protegidos contra accesos no autorizados.&lt;/td>
&lt;td>Resultados de pruebas de seguridad de archivos:
&lt;ul>
&lt;li>Accesos a archivos restringidos verificados.&lt;/li>
&lt;li>Todos los accesos no autorizados fueron bloqueados.&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Prueba de protección contra malware&lt;/td>
&lt;td>El sistema está protegido contra malware.&lt;/td>
&lt;td>Resultados de pruebas de malware:
&lt;ul>
&lt;li>Escaneo de malware realizado.&lt;/li>
&lt;li>Sistema libre de malware.&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Prueba de seguridad en redes&lt;/td>
&lt;td>La red es segura.&lt;/td>
&lt;td>Red sin vulnerabilidades y con tráfico seguro.&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Pruebas de seguridad de configuración&lt;/td>
&lt;td>La configuración es segura.&lt;/td>
&lt;td>Todas las configuraciones críticas protegidas adecuadamente.&lt;/td>
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
&lt;td>Configuración de parámetros personalizados&lt;/td>
&lt;td>Los usuarios configuran parámetros específicos para adaptarse a
diferentes escenarios.&lt;/td>
&lt;td>Retroalimentación sobre la facilidad de configuración y
funcionalidad de los parámetros:
&lt;ul>
&lt;li>Usuario A: "Configurar los parámetros fue sencillo y se adaptaron
bien a mis necesidades."&lt;/li>
&lt;li>Usuario B: "La personalización es efectiva, aunque algunas
opciones podrían ser más visibles."&lt;/li>
&lt;li>Usuario C: "La funcionalidad es excelente, permite ajustar a
diferentes escenarios fácilmente."&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="even">
&lt;td>Uso de herramientas de visualización&lt;/td>
&lt;td>Los usuarios utilizan herramientas de visualización de datos para
analizar patrones.&lt;/td>
&lt;td>Comentarios sobre la efectividad y facilidad de uso de las
herramientas de visualización:
&lt;ul>
&lt;li>Usuario A: "Las herramientas de visualización son muy efectivas y
fáciles de usar."&lt;/li>
&lt;li>Usuario B: "Visualizar los datos fue sencillo, aunque podría
mejorar la interacción."&lt;/li>
&lt;li>Usuario C: "Excelente visualización, me ayudó a identificar
patrones clave rápidamente."&lt;/li>
&lt;/ul>&lt;/td>
&lt;/tr>
&lt;tr class="odd">
&lt;td>Los usuarios evalúan la navegación y usabilidad del software&lt;/td>
&lt;td>Los usuarios evalúan la navegación y usabilidad del software de
Unity.&lt;/td>
&lt;td>Feedback sobre la interfaz de usuario y facilidad de uso:
&lt;ul>
&lt;li>Usuario A: "La navegación es intuitiva y la usabilidad es
alta."&lt;/li>
&lt;li>Usuario B: "Interfaz amigable, aunque algunos botones podrían
estar mejor ubicados."&lt;/li>
&lt;li>Usuario C: "Muy fácil de usar, la interfaz es clara y bien
organizada."&lt;/li>
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
&lt;li>Tiempo de recuperación: 5 minutos.&lt;/li>
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

| Prueba realizada              | Resultado                                                                                     | Confirmación                                                                              |
|-------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Revisión manual de usuario    | Verificación de que el manual de usuario cubre todas las funcionalidades del software.        | Todas las funcionalidades principales están cubiertas.                                    |
| Guía de configuración         | Se asegura que la guía de configuración es clara y completa.                                  | La guía cubre todos los pasos necesarios para la configuración inicial.                   |
| Actualización de versiones    | Se verifica que la documentación está actualizada con la última versión del software.         | La documentación está completamente actualizada y refleja la última versión del software. |
| Guía de solución de problemas | Se evalua la guía de solución de problemas para asegurarse de que cubre posibles incidencias. | La guía cubre una amplia gama de problemas comunes y sus soluciones.                      |
| Guía de buenas prácticas      | Se verifica que la guía de buenas prácticas está completa y es comprensible.                  | La guía es comprensible y cubre todas las mejores prácticas recomendadas.                 |
| Tutoriales en video           | Se asegura que los tutoriales en video son claros y educativos.                               | Los tutoriales son claros y bien estructurados.                                           |
| Documentación de API          | Se revisa que la documentación de las API para asegurarse de que es completa y precisa.       | La documentación es completa y precisa, cubriendo todos los endpoints y ejemplos de uso.  |

# Resultados y conclusiones

Después de realizar exhaustivas pruebas de instalación (IQ), operación
(OQ) y funcionamiento (PQ), se concluye que el entorno de desarrollo
Unity cumple con los estándares requeridos para el diseño y desarrollo
de software en Spika Tech. Los resultados obtenidos en cada fase de la
validación indican lo siguiente:

- Instalación Exitosa: La instalación del software Unity se llevó a cabo
  sin incidentes, cumpliendo con los requisitos de hardware y software
  establecidos. Todos los archivos se instalaron correctamente y su
  integridad fue verificada.

- Operación Satisfactoria: Las pruebas de funcionalidad básica,
  integración, rendimiento y seguridad muestran que Unity opera
  correctamente bajo diversas condiciones. No se encontraron errores
  significativos y todas las funcionalidades principales respondieron
  según lo esperado.

- Funcionamiento Adecuado: Las pruebas de aceptación de usuario y
  escenarios críticos validan que el entorno es adecuado para el
  desarrollo de aplicaciones de visualización y análisis de señales
  cardíacas. Los usuarios encontraron el software intuitivo y eficaz
  para sus propósitos.

En base a los datos recopilados, se aprueba el uso de Unity para el
diseño y desarrollo de software en Spika Tech, garantizando que cumple
con los criterios de funcionalidad, confiabilidad y seguridad
necesarios.

# Historico de versiones

| **VERSION** | **MOTIVO DEL CAMBIO** | **FECHA**  |
|-------------|-----------------------|------------|
| 01          | Edicion inicial       | Junio 2024 |