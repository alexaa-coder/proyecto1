style="width:4.70833in;height:1.85417in" alt="Spika Tech" /&gt;

**PROCEDIMIENTO DE CONTROL DE ACCESO DE USUARIOS**










**HISTORIAL DEL DOCUMENTO**


**Versión**
**Resumen de modificaciones**
**Fecha de entrada**
**Sustituye a (Código, revisión)**




01
Primera versión del documento.
26/02/2025
N/A













**REGISTRO DE FIRMAS**


**Función:**
**Elaborado por:**
**Revisado por:**
**Aprobado por:**




Departamento:
Responsable del SGSI
Dirección
Jefe de seguridad
(o suplente)


Nombre:
David Pozo
Carlos Rodrigo
Carlos Zúñiga


Firma:





Fecha:
26/02/2025
26/02/2025
26/02/2025




# CONTENIDO

[1 Objetivo [4](#objetivo)](#objetivo)

[2 Alcance [4](#alcance)](#alcance)

[3 POLÍTICAS GENERALES: IDENTIFICACIÓN
[4](#_Toc191457499)](#_Toc191457499)

[3.1 DIRECTRICES DEL SISTEMA
[5](#directrices-del-sistema)](#directrices-del-sistema)

[4 Política de acceso a los servicios de red
[7](#política-de-acceso-a-los-servicios-de-red)](#política-de-acceso-a-los-servicios-de-red)

[5 Gestión de acceso a Usuarios en los Sistemas de Información
[8](#gestión-de-acceso-a-usuarios-en-los-sistemas-de-información)](#gestión-de-acceso-a-usuarios-en-los-sistemas-de-información)

[5.1 REGISTRO Y ALTA DE USUARIO
[9](#registro-y-alta-de-usuario)](#registro-y-alta-de-usuario)

[5.2 PROVISIÓN DE ACCESO DE LOS USUARIOS
[11](#provisión-de-acceso-de-los-usuarios)](#provisión-de-acceso-de-los-usuarios)

[5.3 GESTIÓN DE PRIVILEGIOS DE ACCESO
[11](#gestión-de-privilegios-de-acceso)](#gestión-de-privilegios-de-acceso)

[5.4 GESTIÓN DE LA INFORMACIÓN SECRETA DE AUTENTIFICACIÓN DE LOS
USUARIOS
[12](#gestión-de-la-información-secreta-de-autentificación-de-los-usuarios)](#gestión-de-la-información-secreta-de-autentificación-de-los-usuarios)

[5.5 REVISIÓN DE LOS DERECHOS DE ACCESO DE USUARIO
[12](#revisión-de-los-derechos-de-acceso-de-usuario)](#revisión-de-los-derechos-de-acceso-de-usuario)

[5.6 Retirada de los derechos de acceso/BAJA
[13](#retirada-de-los-derechos-de-accesobaja)](#retirada-de-los-derechos-de-accesobaja)

[6 Control de acceso a sistemas y aplicaciones
[14](#control-de-acceso-a-sistemas-y-aplicaciones)](#control-de-acceso-a-sistemas-y-aplicaciones)

[6.1 PROCEDIMIENTOS SEGUROS DE INICIO DE SESIÓN
[14](#procedimientos-seguros-de-inicio-de-sesión)](#procedimientos-seguros-de-inicio-de-sesión)

[6.2 SISTEMA DE GESTIÓN DE CONTRASEÑAS
[15](#sistema-de-gestión-de-contraseñas)](#sistema-de-gestión-de-contraseñas)

[6.3 USO DE LAS UTILIDADES CON PRIVILEGIOS DEL SISTEMA
[16](#uso-de-las-utilidades-con-privilegios-del-sistema)](#uso-de-las-utilidades-con-privilegios-del-sistema)

[7 Referencias [16](#referencias)](#referencias)

#  Objetivo

Este procedimiento establece los requisitos y características mínimas
que deberán disponer los controles de acceso a los sistemas de
información/aplicaciones administradoras que presten soporte directo a
los servicios proporcionados por SPIKA TECH.

#  Alcance 

Este procedimiento será de aplicación para todas las personas empleadas
del SPIKA TECH en el cumplimiento de las funciones que tengan asignadas
como parte de su desempeño profesional, así como a la totalidad de los
recursos corporativos que permiten el acceso a los sistemas recogidos en
el alcance y que sean utilizados para llevar a cabo dichas funciones.

# POLÍTICAS GENERALES: IDENTIFICACIÓN

-   Previamente a la atribución de la clave de acceso, los usuarios
    deberán ser registrados mediante un procedimiento en el que se
    verifique la identidad del usuario de forma inequívoca y
    personalizada.

-   Los usuarios se identificarán y autenticarán en el acceso a los
    sistemas de información, recursos, áreas de procesamiento de datos y
    redes de comunicaciones de SPIKA TECH, utilizando una clave de
    acceso de modo que se puedan reconocer (identificación) y comprobar
    (autenticación) la identidad del usuario que accede de forma
    inequívoca y personalizada, tal y como está autorizado.

-   Cada usuario tendrá su propia clave de acceso única e intransferible
    en el SPIKA TECH. Se impedirá que existan dos identificadores
    iguales.

-   No está permitida la compartición o utilización de usuarios
    genéricos ni de claves atendiendo a la **Normativa de Utilización de**
    los Recursos y Sistemas de Información** de SPIKA TECH.**

-   Periódicamente, se revisan los últimos accesos de los usuarios para
    verificar que los siguen utilizando. se procede a su eliminación.
    Todas las claves de acceso que no hayan sido utilizadas durante un
    serán deshabilitadas, a no ser que se sospeche de su actividad o se
    sepa a ciencia cierta que ya no se procederá a su uso, en cuyo caso
    podrá ser antes.

-   Las cuentas de empleados internos que hayan sido dados de baja, así
    como las de usuarios externos que no continúen prestando sus
    servicios en el SPIKA TECH serán desactivadas si bien, se
    preservarán la trazabilidad de los accesos y acciones durante un
    periodo de tiempo estipulado.

-   La baja implica automáticamente que serán eliminados los derechos de
    acceso asociados a estos usuarios en todos los sistemas de
    información, recursos, áreas de procesamiento de datos y redes de
    comunicaciones del SPIKA TECH a los cuales tengan acceso, así como a
    la cuenta de correo electrónico.

-   Serán concedidas las claves de acceso según el rol definido por cada
    responsable de área y el perfil que deba tener el usuario, siempre
    teniendo en cuenta el documento de **Procedimiento de roles y**
    segregación de funciones,** así como aquellos roles y**
    responsabilidades que por sus particularidades, están recogidos en
    los diferentes procedimientos, normativas y políticas aplicables al
    SPIKA TECH.

-   Cuando un usuario tenga diferentes roles en el sistema (trabajador,
    administrador del sistema) se le proporcionarán identificadores
    individuales para cada rol. El uso de identificadores de grupos o
    genéricos, deberá ser debidamente autorizado y convenientemente
    justificado.

## DIRECTRICES DEL SISTEMA

-   Todo nuevo sistema de información desarrollado internamente o
    adquirido como producto de mercado, deberá respetar los criterios de
    seguridad de acceso especificados en este documento.

-   Las claves de acceso en los recursos de sistemas y redes deben tener
    identificadores únicos, es decir, no pueden existir dos o más claves
    iguales en el mismo sistema. Todo sistema del SPIKA TECH debe:

    -   Generar una contraseña aleatoria, dentro de los parámetros de
        configuración seguros.

    -   Garantizar el cambio de contraseña por el propietario de la
        clave en la primera autenticación realizada con éxito.

    -   Permitir que el usuario modifique la propia contraseña en
        cualquier momento.



-   Se recomienda que, en sistemas accesibles a través de Internet, la
    autenticación sólo deberá ser posible mediante el uso de claves de
    acceso que posibiliten una autenticación fuerte, es decir, se debe
    utilizar más de un factor para realizar la autenticación, como, por
    ejemplo, usuario y contraseña en conjunto como generador automático
    de claves (ej.: aplicación para autenticación en dos pasos).

-   Los recursos de sistemas y red deben impedir conexiones simultáneas
    de una misma clave a partir de equipos distintos.

-   Las contraseñas deben ser almacenadas cifradas o por medio de
    funciones de resumen (hash) con acceso restricto en los sistemas de
    red.

-   Debe ser configurado un mecanismo de autenticación del usuario para
    bloquear el acceso después de un número definido de intentos de
    acceso no autorizado de acuerdo a la Política de Contraseñas
    establecida.

-   Los equipos deben ser configurados de modo que no se realice su
    inicio o ejecución a través de medios removibles.

-   Debe ser habilitada la contraseña de protección de la configuración
    de los equipos.

-   Los equipos solamente deben tener conexiones e interfaces necesarias
    para su finalidad.

-   No estando permitido a los usuarios compartir carpetas de red con el
    objetivo de transferir archivos si éstas no tienen un control de
    acceso y privilegios.

-   Los recursos de acceso compartidos deberán tener permisiones
    restrictivas, concedidas por el principio del mínimo privilegio, de
    modo que permita el acceso solamente a usuarios autorizados, según
    los procedimientos internos.

-   Los equipos deben tener un método de protección de pantalla después
    de un periodo de inactividad de 5 minutos.

-   El acceso a los equipos con fines de mantenimiento relacionados con
    peticiones del usuario (ej. instalación de una aplicación), debe ser
    autorizado por sus respectivos usuarios. Antes de autorizar la
    intervención de manutención, deben cerrar todas las aplicaciones.

-   El acceso remoto a la red o redes del SPIKA TECH debe realizarse
    solamente por usuarios autorizados y mediante equipos que atiendan
    los estándares normativos de seguridad física y lógica definidos por
    SPIKA TECH.

-   Todos los usuarios, antes de autorizar la intervención de
    mantenimiento, deben cerrar todas las aplicaciones.

-   El acceso remoto a la red o redes del SPIKA TECH debe realizarse
    solamente por usuarios autorizados y mediante equipos que atiendan
    los estándares normativos de seguridad física y lógica definidos de
    la organización.

-   Controles de autenticación tales como tokens, no deben ser
    transportados junto con los ordenadores portátiles y los
    dispositivos móviles.

# Política de acceso a los servicios de red 

El Control de Acceso a la Red tendrá como objetivo asegurar que todos
los dispositivos que se conectan a las redes corporativas de una
organización cumplen con las Políticas de seguridad establecidas para
evitar amenazas como la entrada de virus, salida de información, etc.

Este control estará basado en estos cinco principios:

-   **Detección:** Detección del intento de conexión física o
    inalámbrica a los recursos de red reconociendo si el mismo es un
    dispositivo autorizado o no.

-   **Cumplimiento:** Verificación de que el dispositivo cumple con los
    requisitos de seguridad establecidos como por ejemplo dispositivo
    autorizado, ubicación, usuario, antivirus actualizado.

&gt; Cuando un dispositivo no cumpla los requerimientos se podrá rechazar
&gt; la conexión o aplicar las mejores prácticas que el área dedicada a
&gt; esta labor estipule como por ejemplo mandarlo a un portal cautivo
&gt; “Cuarentena”.

-   **Subsanación:** Modificación lógica de dichos requisitos en el
    dispositivo que intenta conectarse a la red corporativa.

-   **Aceptación:** Entrada del dispositivo a los recursos de red en
    función del perfil del usuario y los permisos correspondientes a su
    perfil que residen en un servicio de directorio.

-   **Persistencia:** Vigilancia durante toda la conexión para evitar la
    vulneración de las políticas asignadas.

Por la red del SPIKA TECH entendemos cualquier punto de conexión desde
donde se puedan acceder a los recursos propios del SPIKA TECH como
servidores, ficheros, impresoras, conexiones a Internet, Intranet o
cualquier otro servicio que se dé a los usuarios.

A la red del SPIKA TECH se puede acceder desde un escritorio remoto, el
portátil facilitado por el mismo, o a través de un escritorio virtual,
en algunos de estos supuestos será necesario, además, la configuración
de una VPN o de un acceso remoto seguro.

Sea cual sea el acceso siempre se validarán los permisos, a través de la
cuenta de usuario y contraseña.

El acceso a la red del SPIKA TECH queda limitado para fines
estrictamente de trabajo que el usuario desempeña en el SPIKA TECH de
acuerdo con la **Norma** **general de utilización de los recursos y**
sistemas de información**. Las acciones realizadas tras la introducción**
de la contraseña se consideran responsabilidad del usuario.

El área de ciberseguridad se encarga de poner todas las medidas posibles
para registrar los accesos, dar o quitar permisos, detectar intrusiones
y usos indebidos en la red del SPIKA TECH.

Todos los dispositivos (switches, etc.) de red local deben utilizar
mecanismos de autenticación y control de acceso de manera que nadie
pueda conectar su dispositivo en la red local sin previa autorización.

Se establecen perfiles de acceso con niveles de acceso distintos según
la función del usuario.

La red interna debe ser segregada en segmentos lógicos según los niveles
de riesgo.

# Gestión de acceso a Usuarios en los Sistemas de Información

Con la finalidad de evitar accesos no autorizados a los Sistemas de
Información, se establecerán los procedimientos formales para controlar
la asignación de los derechos de acceso a los sistemas y servicios.

Estos procedimientos deben cubrir todas las etapas del ciclo de vida del
acceso de los usuarios, desde el registro inicial de los nuevos, hasta
la baja del registro de los usuarios que ya no requieran dicho acceso a
los sistemas o servicios. Se prestará especial atención al control de la
asignación de derechos de acceso privilegiados que permitan a ciertos
usuarios evitar los controles del sistema, en este sentido:

-   Se prevendrá el acceso no autorizado a las plataformas de los
    servicios de información, mediante mecanismos de identificación y
    autenticación apropiados e implantando mecanismos de seguridad a
    nivel de sistema operativo para restringir el acceso a los recursos.

-   Se evitará el acceso no autorizado a la información contenida en los
    sistemas. Las aplicaciones deben proporcionar acceso a la
    información solo a su propietario, personas autorizadas nominalmente
    o usuarios designados formalmente. Se deben usar las prestaciones de
    seguridad lógica dentro de los sistemas de aplicación para
    restringir el acceso.

-   Los accesos a la información y los procesos de negocio deben ser
    monitorizados, a fin de comprobar la eficacia de los controles
    adoptados y detectar las desviaciones respecto de la política de
    control de accesos.

-   El proceso de gestión de derechos de acceso ya sea en el alta o en
    la modificación de acceso, se otorgarán en función de las
    competencias de los usuarios y en base a los principios de:

    -   Mínimo privilegio: los privilegios de cada entidad, usuario o
        proceso se reducirán al mínimo imprescindible para cumplir sus
        obligaciones.

    -   Necesidad de conocer y responsabilidad de compartir: solo se
        concederá el acceso a aquella información que es necesario
        conocer para desempeñar la actividad encomendada.

    -   Capacidad de otorgar: el acceso solo lo puede otorgar la persona
        designado para ello.

## REGISTRO Y ALTA DE USUARIO

-   Para solicitar el alta a cualquier tipo de servicio, aplicación o
    material, será necesario que el usuario haga una petición al
    responsable de IT para que el mismo valoré la petición, y en caso de
    aceptarla, darle los credenciales y permisos correspondientes

-   Los usuarios de los sistemas de información pertenecerán a un tipo
    de usuario determinado de acuerdo con el rol o funciones que tenga
    SPIKA TECH, debiendo recogerse al menos los siguientes datos:

    -   Nombre, apellidos, NIF, empresa (si son externos), categoría
        profesional, área o departamento y tiempo estimado (sin son
        externos).

    -   El procedimiento de generación de identificadores de usuario
        garantizará la no duplicidad de los mismos. Tal procedimiento
        garantizará, además, que se cumpla con las reglas de
        identificación y nomenclatura, así como demás estándares
        aplicables, y en particular se realizarán las siguientes las
        siguientes acciones:



-   En algunos supuestos, se solicitará además del usuario y contraseña,
    un doble factor de autenticación. Estos supuestos engloban el acceso
    a aplicaciones clientes pesadas y web desde dispositivos personales
    (BYOD), y aquellas a las que se accedan desde el equipo corporativo,
    pero fuera de las instalaciones del SPIKA TECH.

-   El sistema habitual consiste en el establecimiento de una
    contraseña, siendo en este caso obligatorio establecer unos
    criterios mínimos de calidad respecto a la misma, así como, unas
    normas de actuación para protegerla de posibles robos o actos
    malintencionados.

-   Cualquier modificación sobre las credenciales o permisos del usuario
    tendrá que ser tramitada a través de una solicitud al área de
    ciberseguridad. Asimismo, cualquier modificación sobre las
    credenciales tendrá que ser aprobada por el responsable del usuario.
    Por otra parte, el área de ciberseguridad validará la adecuación de
    la modificación para que respete las políticas del SPIKA TECH.

-   Con el fin de tener controlados, en todo momento, a los usuarios que
    se conectan a los Sistemas de Información, se hace indispensable la
    regulación una correcta gestión de las bajas de usuarios a los
    sistemas de información. Las causas que pueden implicar una baja un
    de usuario son:

    -   Se detecte inactividad en un máximo de 180 días, ya sea de forma
        automatizada mediante los propios sistemas de información o como
        resultado de una revisión periódica de los usuarios.

    -   La persona deje de trabajar en el SPIKA TECH.

    -   Una revisión sobre accesos detecte credenciales obsoletas. Al
        finalizar desde el Sistema General de Recursos Humanos se
        enviará como mínimo mensualmente, un listado de las personas que
        han causado baja.

## PROVISIÓN DE ACCESO DE LOS USUARIOS

-   Se aplica el principio del menor privilegio para los permisos. Los
    privilegios de acceso a muy alto nivel, (Ej. asistencia técnica de
    alto nivel, utilidades del sistema y administración de la seguridad)
    capaces de anular los controles del sistema y las aplicaciones:

    -   Son controlados y limitados al mínimo nivel requerido para hacer
        el trabajo.

    -   Sólo deben usarse en un entorno distinto del empleado para el
        trabajo diario.

    -   Las contraseñas son cambiadas en función de la política de
        contraseñas definida en el SPIKA TECH para cada sistema de
        información.

    -   Los accesos y permisos por defectos podrán variar entre usuarios
        internos y externos del SPIKA TECH.



-   Los derechos de acceso son revisados periódicamente por el área de
    ciberseguridad y el Responsable del SGSI.

## GESTIÓN DE PRIVILEGIOS DE ACCESO

-   Se deberán limitar los privilegios administrativos a muy pocos
    usuarios, a aquellos que deban administrar el sistema operativo y
    que estén autorizados por el SPIKA TECH y por razones de servicio
    para modificar la configuración del sistema operativo, estos
    privilegios se revisarán periódicamente.

-   Se deberán utilizar las cuentas administrativas sólo para
    actividades de administración del sistema, no se utilizarán para
    leer los correos, ni para componer documentos, ni para navegar por
    internet, por ejemplo.

-   Se deberán revisar la fecha de expiración de las cuentas.

-   Se deberán revisar las cuentas que estén desactivadas y aquellas que
    no estén asociadas con el servicio.

-   Los accesos con privilegios especiales deberán ser controlados
    mediante un proceso de autorización formal definido atendiendo a las
    necesidades de la subdirección correspondiente, y manteniendo las
    siguientes premisas:

    -   Identificar los derechos de acceso especiales con
        Sistema/Proceso.

    -   Identificar las necesidades Rol/Responsabilidad.

    -   Proceso de autorización complementado antes de dar acceso
        privilegiado.



-   Existir premisas de finalización de uso de acceso privilegiado.

-   Estos accesos con privilegios deberán ser revisados regularmente por
    los administradores de los Sistemas/Redes, así como por los
    Responsables de la Información. Cualquier uso indebido del usuario
    deberá estar contemplado en los procedimientos disciplinarios y
    mecanismos correspondientes.

-   El área de ciberseguridad realizará auditorías semestrales de los
    permisos de acceso otorgados a los usuarios del SPIKA TECH.

-   El área de ciberseguridad será responsable de registrar, mantener y
    custodiar los permisos otorgados a los usuarios.

## GESTIÓN DE LA INFORMACIÓN SECRETA DE AUTENTIFICACIÓN DE LOS USUARIOS

-   Cuando se requiera a los usuarios mantener sus propias contraseñas,
    se les debe proporcionar inicialmente una contraseña segura y
    temporal la cual se vean obligados a cambiar inmediatamente.

-   Establecer requisitos para verificar la identidad de un usuario
    previamente a proporcionarle una contraseña ya sea nueva, de
    sustitución o temporal.

-   Las contraseñas temporales deben proporcionarse a los usuarios de
    una manera segura, debe evitarse el uso de terceros.

-   Las contraseñas temporales deben ser únicas e individuales y no
    adivinables.

-   Las contraseñas nunca deben ser almacenadas en los ordenadores de
    forma no protegida.

-   Las contraseñas por defecto facilitadas por un proveedor, deberán
    ser modificadas en el proceso de instalación de los sistemas o del
    software.

## REVISIÓN DE LOS DERECHOS DE ACCESO DE USUARIO

-   Los derechos de acceso de usuario son revisados a intervalos
    regulares y después de cualquier cambio o baja temporal/definitiva.

-   Las autorizaciones para derechos de acceso con privilegios
    especiales son revisadas con una frecuencia mayor.

-   Las asignaciones de privilegios deben comprobarse a intervalos
    regulares para asegurar que no se han obtenido privilegios no
    autorizados.

-   Los cambios en las cuentas de privilegios deberían ser registrados
    para su revisión periódica, cuando exista:

    -   Necesidad de nuevos permisos.

    -   Cancelación de antiguos permisos.

    -   Segregación de funciones.

    -   Devolución de activos y modificación o cancelación de permisos
        de accesos físicos.

    -   Modificación de contraseñas de acceso.

    -   Notificación al personal implicado de su baja o cambio.

    -   Necesidad de retención de registros.

## Retirada de los derechos de acceso/BAJA

-   En este sentido, todos los accesos (tanto físicos como lógicos) en
    los casos de finalizar la relación con SPIKA TECH, son
    deshabilitados temporalmente, en primer lugar, y posteriormente,
    eliminados de forma definitiva. Una vez conocida la baja, se procede
    a la deshabilitación temporal de usuario y su cuenta, y
    transcurridos 6 meses , se procede a la
    eliminación definitiva de las cuentas afectadas. Este periodo de
    tiempo constituye el periodo de retención establecido como necesario
    para poder atender a las necesidades de trazabilidad de los
    registros asociados a dichas cuentas.

-   En el caso de que las funciones del usuario cambien sustancialmente
    también deben de ser revisados y modificados los derechos de acceso.

-   En una de las aplicaciones corporativas se incluye un “desh” delante
    del email del usuario para evitar la recepción de correos, de forma
    paralela, se tramita la inhabilitación del propio usuario.

**Baja de sistemas y retirada de equipo:**

-   El Responsable de la Solicitud remitirá al área de ciberseguridad la
    Solicitud de Alta/Baja de Recursos IT, informando de la baja del
    empleado y solicitando la baja del empleado público en los sistemas,
    la retirada del equipo que en su caso tenga asignado, y señalando la
    fecha de baja.

-   El área de ciberseguridad ejecutará las acciones pertinentes para
    dar de baja al usuario de los sistemas en la fecha de baja señalada.

-   El área de ciberseguridad se pondrá en contacto con Responsable de
    la Solicitud que el usuario va a causar baja y le reclamará la
    devolución del equipo facilitado por el SPIKA TECH.

-   Una vez completada la solicitud, el área de ciberseguridad informará
    mediante correo electrónico la finalización del trabajo solicitado.

**Baja de telefonía móvil (fija y portátil):**

-   El Responsable de Asignación de Recursos IT remitirá informando de
    la baja del usuario y solicitando la retirada del equipo de
    telefonía móvil y fijo, así como la tarjeta de conexión de datos de
    movilidad que tuviere asignado, y señalando la fecha de baja.

-   En el caso de tener asignado material, el área de ciberseguridad, se
    pondrá en contacto con el usuario que causa baja y retirará el
    material que el empleado tuviera asignado, o le indicará al mismo
    que acuda para su devolución.

-   El área de ciberseguridad dará de baja al usuario en las
    aplicaciones y sistemas de información del SPIKA TECH.

-   Una vez confirmado que se ha dado de baja al usuario en los
    sistemas, que se le ha retirado el equipo, el teléfono y la tarjeta
    de acceso, el área de ciberseguridad enviará la confirmación de la
    baja completa al Responsable de la Solicitud.

# Control de acceso a sistemas y aplicaciones

## PROCEDIMIENTOS SEGUROS DE INICIO DE SESIÓN

-   Las advertencias en la pantalla de inicio de sesión deben indicar
    que el uso de la información y los sistemas está restringido a
    personas autorizadas y son sólo para uso de SPIKA TECH.

-   El control de acceso a los archivos de registro (sistema,
    aplicación, seguridad) garantiza la integridad de los archivos.

-   Todas las actividades están monitorizadas y quedan registros de los
    accesos.

-   Los operadores de ordenadores no deben tener acceso a la
    documentación sobre programación.

-   Se deben utilizar los métodos apropiados de autenticación para el
    control de acceso a los usuarios en remoto.

-   Tras el inicio de sesión, los usuarios deben desconectarse
    automáticamente tras un período de inactividad y se requerirá una
    contraseña para iniciar la sesión.

-   No debe darse ninguna explicación de desconexión al usuario como
    resultado de intentos de conexión fallidos o intentos de
    transacciones no autorizadas.

-   Se deben usar restricciones en los tiempos de conexión para
    proporcionar una seguridad adicional a las aplicaciones de alto
    riesgo.

## SISTEMA DE GESTIÓN DE CONTRASEÑAS

La Gestión de Contraseñas de los sistemas de información recogidos en el
apartado de Alcance del presente procedimiento:

-   Fuerza el uso de los identificadores de usuario individuales y de
    las contraseñas para mantener la responsabilidad.

-   Permite a los usuarios el seleccionar y cambiar sus propias
    contraseñas e incluir un procedimiento de confirmación que tenga en
    cuenta los errores de entrada.

-   Fuerza la elección de contraseñas de calidad.

-   Fuerza el cambio de contraseñas.

-   Fuerza a los usuarios el cambio de las contraseñas temporales
    después de la primera entrada.

-   Mantiene un registro de las contraseñas de usuarios anteriores y
    prevenir su reutilización.

-   No muestra las contraseñas en la pantalla cuando se están
    introduciendo.

-   Almacena los ficheros de contraseñas por separado de los datos de la
    aplicación del sistema.

-   Almacena y transmite las contraseñas de forma protegida (por
    ejemplo: cifradas o codificadas).

## USO DE LAS UTILIDADES CON PRIVILEGIOS DEL SISTEMA

SPIKA TECH considera las siguientes directrices para el uso del sistema:

-   El uso de procedimientos de identificación, autenticación y
    autorización para los recursos del sistema.

-   La segregación de los recursos del sistema para las aplicaciones de
    software.

-   La limitación del uso de los recursos del sistema al mínimo número
    viable de usuarios de confianza autorizados.

-   La autorización para el uso ad–hoc de los recursos del sistema.

-   La limitación de la disponibilidad de los recursos del sistema.

-   El registro de todos los usos de los recursos del sistema.

-   Definir y documentar los niveles de autorización para los recursos
    del sistema.

-   Retirar o deshabilitar todos los recursos y software de los sistemas
    basados en software innecesario.

-   No dejar disponibles los recursos del sistema a los usuarios que
    tienen acceso a las aplicaciones de los sistemas donde se requiere
    segregación de tareas.

# Referencias

-   ISO/ IEC 27001:2022:



-   5.16 Gestión de identidad

-   5.15 Control de acceso

-   5.3 Segregación de tareas

-   5.18 Derechos de acceso

-   8.2 Gestión de privilegios de acceso

-   8.5 Autenticación segura


style="width:6.28333in;height:2.475in" /&gt;