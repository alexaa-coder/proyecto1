---
id: ccn-stic-885d-guia-de-configuracion-segura-para-microsoft-teams
title: "Ccn Stic 885D Guía De Configuración Segura Para Microsoft Teams"
sidebar_label: "Ccn Stic 885D Guía De Configuración Segura Para Microsoft Teams"
---

# **Guía de Seguridad de las TIC** **CCN-STIC 885D**
## **ABRIL 2024**
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
**Catálogo de Publicaciones de la Administración General del Estado**
**https://cpage.mpr.gob.es**
Edita:
CENTRO CRIPTOLOGICO NACIONAL cn=CENTRO CRIPTOLOGICO NACIONAL,
2.5.4.97=VATES-S2800155J, ou=CENTRO CRIPTOLOGICO NACIONAL, o=CENTRO
CRIPTOLOGICO NACIONAL, c=ES 2024.04.29 18:32:23 +02'00'
Pº de la Castellana 109, 28046 Madrid  Centro Criptológico Nacional, 2024
NIPO: 083-24-157-7 Fecha de Edición: abril de 2024
**LIMITACIÓN DE RESPONSABILIDAD**
El presente documento se proporciona de acuerdo con los términos en él recogidos, rechazando expresamente cualquier tipo de garantía implícita que se pueda encontrar relacionada. En ningún caso, el
Centro Criptológico Nacional puede ser considerado responsable del daño directo, indirecto, fortuito o extraordinario derivado de la utilización de la información y software que se indican incluso cuando se
advierta de tal posibilidad.
**AVISO LEGAL**
Quedan rigurosamente prohibidas, sin la autorización escrita del Centro Criptológico Nacional, bajo las sanciones establecidas en las leyes, la reproducción parcial o total de este documento por cualquier medio
- procedimiento, comprendidos la reprografía y el tratamiento informático, y la distribución de
ejemplares del mismo mediante alquiler o préstamo públicos.
**Centro Criptológico Nacional** 2
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
### **ÍNDICE**
**1.** **MICROSOFT TEAMS**
1.1 DESCRIPCIÓN DEL USO DE ESTA GUÍA
1.2 DEFINICIÓN DEL SERVICIO
1.3 PRERREQUISITOS PARA EL DESPLIEGUE MEDIANTE POWERSHELL
**2.** **DESPLIEGUE DE MICROSOFT TEAMS**
2.1 _ADMINISTRADOR – CONFIGURACIÓN INICIAL_
2.1.1 CONFIGURACIÓN DE TODA LA ORGANIZACIÓN
2.1.1.1 NOTIFICACIONES Y FUENTES
2.1.1.2 ETIQUETADO
2.1.1.3 INTEGRACIÓN DE CORREO ELECTRÓNICO
2.1.1.4 ARCHIVOS
2.1.1.5 ORGANIZACIÓN
2.1.1.6 DISPOSITIVOS
2.1.1.7 BUSCAR POR NOMBRE
2.1.1.8 SEGURIDAD Y COMUNICACIONES
2.1.1.9 CANALES COMPARTIDOS
2.2 _USUARIO FINAL - PRIMEROS PASOS_
2.2.1 CREACIÓN DE UN EQUIPO
2.2.1.1 CREAR UN EQUIPO DESDE CERO
2.2.1.2 CREAR UN EQUIPO DESDE GRUPO EXISTENTE DE MICROSOFT 365
2.2.2 ADMINISTRAR EQUIPO DE TEAMS
**3.** **CONFIGURACIÓN DE MICROSOFT TEAMS**
3.1 MARCO OPERACIONAL
3.1.1 CONTROL DE ACCESO
3.1.1.1 IDENTIFICACIÓN
3.1.1.2 REQUISITOS DE ACCESO
3.1.1.3 SEGREGACIÓN DE FUNCIONES Y TAREAS
3.1.1.4 PROCESO DE GESTIÓN DE DERECHOS DE ACCESO
3.1.1.5 MECANISMOS DE AUTENTICACIÓN (USUARIOS EXTERNOS)
3.1.1.6 MECANISMOS DE AUTENTICACIÓN (USUARIOS DE LA ORGANIZACIÓN)
3.1.2 EXPLOTACIÓN
**Centro Criptológico Nacional** 3
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
3.1.2.1 PROTECCIÓN FRENTE A CÓDIGO DAÑINO
3.1.2.2 GESTIÓN DE INCIDENTES
3.1.2.3 REGISTRO DE ACTIVIDAD
3.1.3 MONITORIZACIÓN DEL SISTEMA
3.2 MEDIDAS DE PROTECCIÓN
3.2.1 PROTECCIÓN DE LAS COMUNICACIONES
3.2.2 PROTECCIÓN DE LA INFORMACIÓN
3.2.2.1 CALIFICACIÓN DE LA INFORMACIÓN
3.2.2.2 LIMPIEZA DE DOCUMENTOS
3.2.2.3 COPIAS DE SEGURIDAD
3.2.3 PROTECCIÓN DE LOS SERVICIOS
3.2.3.1 PROTECCIÓN FRENTE A LA DENEGACIÓN DE SERVICIO
**4.** **OTRAS CONSIDERACIONES DE SEGURIDAD**
4.1 DIRECTIVA DE EQUIPOS
4.2 DIRECTIVAS DE MENSAJERÍA
4.3 DIRECTIVAS DE PERMISOS DE APLICACIONES
4.4 DIRECTIVAS DE CONFIGURACIÓN DE LA APLICACIÓN
4.5 DIRECTIVAS DE VOZ
4.6 DIRECTIVAS DE REUNIÓN
4.7 DIRECTIVAS DE DISPOSITIVOS
**5.** **CUADRO RESUMEN DE MEDIDAS DE SEGURIDAD**
**Centro Criptológico Nacional** 4
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
### **1. MICROSOFT TEAMS** **1.1 Descripción del uso de esta guía**
El objetivo de la presente guía es indicar los pasos a seguir para la configuración del servicio _Microsoft Teams_ cumpliendo con los requisitos necesarios del _Esquema_
_Nacional de Seguridad_ en su categoría ALTA.
Esta guía debe usarse en conjunto con [CCN-STIC-885A - Guía de configuración segura para Office 365], donde se describen generalidades de Office 365 y características
comunes a todos los servicios, así como un _glosario_ con los términos y abreviaturas de seguridad utilizadas en estas guías.
Para la confección de esta guía se han consultado las siguientes fuentes:
- Documentación oficial de Microsoft.
- CCN-STIC-823 Servicios en la Nube.
- CCN-STIC-884A - Guía de configuración segura para Azure.
- CCN-STIC-885A - Guía de configuración segura para Office 365.
- ENS Real Decreto BOE-A-2010-1330.
### **1.2 Definición del servicio**
Microsoft Teams es el centro de trabajo en equipo en Microsoft 365 diseñado para mejorar la comunicación y colaboración de los equipos de trabajo de las empresas,
reforzando las funciones colaborativas de la plataforma en la nube, Office 365 (conjunto Microsoft Teams ofrece la posibilidad de utilizar las aplicaciones de Office 365,
personalizando el entorno según las necesidades de tu equipo. Con Teams los usuarios de un equipo pueden:
- Realizar chats de grupo o privados para mantener conversaciones de grupo con
pocos miembros.
- Ver el contenido y el historial de chat en cualquier momento.
- Iniciar reuniones de vídeo o voz gracias a la integración de _Skype empresarial_ .
- Obtener acceso instantáneo a todo el contenido, las herramientas de
colaboración, los usuarios y las conversaciones a través de pestañas.
- Agregar acceso rápido a los documentos, a los sitios web y a las aplicaciones que
se usen con frecuencia.
- Acceso a notas y documentos gracias a la integración con _OneNote_ y _SharePoint_ .
**Centro Criptológico Nacional** 5
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
- Trabajar con documentos de Office Online directamente desde Teams.
- Planificar tareas gracias a la integración con _Planner_ .
- Agregar informes de _Power BI_ .
- Disfrutar de un espacio común de trabajo con interfaz web y para dispositivos
móviles.
- Al estar basado en grupos permite al usuario moverse de una plataforma de
colaboración a otra fácilmente.
- Agregar conectores que permiten integrar aplicaciones como Yammer y servicios
de terceros, como por ejemplo: RSS, Canal de noticias de Bing o Twitter.
- Crear una integración personalizada con interfaces de programación de
aplicaciones y otras herramientas de desarrollo.
### **1.3 Prerrequisitos para el despliegue mediante PowerShell**
PowerShell de Office 365 permite gestionar y configurar _Microsoft Teams_ desde la línea de comandos, con un usuario con derechos de administración. Consultar la guía [CCNSTIC-885A - Guía de configuración segura para Office 365].
Los comandos para administrar Teams se encuentran en dos módulos diferentes:
- **Módulo PowerShell de Microsoft Teams** : contiene los cmdlets necesarios para
crear y manejar equipos.
Para instalarlo, abrir una versión de PS en modo administrador:
 `Install-Module -Name MicrosoftTeams`  `Install-Module -name MicrosoftTeams -AllowClobber`
- **Módulo PowerShell de Skype for Business** : contiene los cmdlets para manejar
políticas, configuraciones y otras herramientas de Teams.
1. Localizar el módulo en el “Centro de Descargas” de Microsoft:
[https://www.microsoft.com/en-us/download/details.aspx?id=39366](https://www.microsoft.com/en-us/download/details.aspx?id=39366)
2. Descargar el archivo “SkypeOnlinePowerShell.exe” y ejecutar.
Para conectarse al módulo de Microsoft Teams:
**Centro Criptológico Nacional** 6
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
 `Connect-MicrosoftTeams` Para consultar los _Teams_ (equipos) creados:
 `Get-Team`
### **2. DESPLIEGUE DE MICROSOFT TEAMS** **2.1 Administrador – configuración inicial**
Al pulsar en el icono de Teams se accede al _Centro de administración de Microsoft_ _Teams_ .
**Centro Criptológico Nacional** 7
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
En el menú [Usuarios] se controla la configuración de usuario de toda la organización. A continuación se describen las más relevantes desde el punto de vista de la seguridad.
**Acceso externo**
Acceso externo permite que los usuarios de Teams y Skype Empresarial buscar, llamar, chatear y configurar reuniones con usuarios externos. La configuración de la
organización dicta cómo los usuarios de nuestra organización pueden comunicarse con los usuarios de Teams de otras organizaciones, los usuarios de Teams no administrados
y otros grupos de usuarios externos. Para que el acceso externo funcione, las organizaciones externas también deben permitir nuestro dominio en su configuración
de acceso externo. Menú [Usuarios\Acceso externo].
**Centro Criptológico Nacional** 8
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
El acceso externo se utiliza cuando:
- Existen usuarios en diferentes dominios de la organización.
- Se necesita que personas de la organización usen Teams para ponerse en
contacto con personas de empresas específicas de fuera de la organización.
De forma predeterminada, la organización puede comunicarse con todos los dominios externos. Podremos elegir entre permitir solo dominios externos específicos, bloquear
todos los dominios externos o bloquear sólo dominios externos específicos.
1. En la pantalla anterior, seleccionando “ _Permitir sólo dominio externos específicos_ ” y pulsando “ _Agregar dominios externos_ ” podremos agregar dominios permitidos.
2. Añadir dominios a la lista de permitidos.
2.1. Escribir el nombre del dominio.
2.2. Pulsar “Listo”.
Así se van añadiendo los dominios individualmente.
Es importante restringir los dominios externos, desde el punto de vista de la
seguridad, para evitar que usuarios de otras organizaciones puedan ponerse en contacto
con miembros de nuestra organización.
Con esta configuración, también se controlará el acceso de los usuarios a otras organizaciones. La capacidad de comunicarse con usuarios de otras organizaciones es
un elemento fundamental en Teams, por lo tanto, se recomienda mantener una lista de dominios autorizados o bloqueados, y mantener adecuadamente dicha lista a lo largo
del tiempo.
En esta pantalla también podremos ajustar la comunicación entre cuentas de la organización respecto a cuentas no administradas por una organización y usuarios de
Skype. Como recomendación, conviene deshabilitar dicho tipo de cuentas no administradas.
**Centro Criptológico Nacional** 9
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
**Acceso de invitado**
Con el acceso de invitados se permite que personas que no pertenecen a la organización se les conceda acceso a _equipos, recursos, chats, aplicaciones_ y _canales_ en uno o más
espacios empresariales a personas que no pertenezcan a la organización, sin perder por ello el control sobre los datos corporativos. Todo contacto que tenga una cuenta de
correo electrónico (como Outlook o Gmail u otros) puede participar como invitado en Teams con acceso total a los chats, las reuniones y los archivos del equipo.
Al invitar a un invitado a Teams, se crea una cuenta de invitado para él en Microsoft Entra ID y está cubierto por la misma protección de cumplimiento y auditoría que otros
usuarios de la organización.
**Nota** : Si solo deseamos buscar, llamar, chatear y configurar reuniones con personas de otras
organizaciones, bastará con hacer uso del _acceso externo_ descrito en el apartado anterior.
Dichas configuraciones, se acceden a través del menú [Usuarios\Acceso de invitado].
El acceso de invitado **se encuentra activado de forma predeterminada**, y se recomienda desactivarlo salvo que sea necesario.
Todos los _invitados_ de Teams están protegidos con el mismo cumplimiento de normativas y auditorías que el resto de Office 365, y se pueden administrar de forma
segura dentro de Azure AD.
_Diferencias entre el acceso de invitado y acceso externo_
- Acceso de invitado concede permiso de acceso a una persona. Acceso externo
concede permiso de acceso a un dominio completo.
- El acceso de invitados, una vez otorgado por el propietario de un equipo, permite
que un invitado tenga acceso a recursos, como archivos y debates de canales, para un equipo específico y conversar con otros usuarios del equipo al que han sido
invitados.
- Con el acceso externo (chat federado), los participantes del chat externo no tienen
acceso a los equipos de la organización o a los recursos del equipo. Solo pueden participar en un chat federado (one-on-one).
**Centro Criptológico Nacional** 10
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
- Los administradores del tenant pueden elegir entre las dos opciones de
comunicación dependiendo del nivel de colaboración que sea deseable con la parte externa. Los administradores pueden elegir entre dos enfoques o ambos, según las
necesidades de la organización.
En la siguiente tabla se muestra una comparativa de las características de ambos:

|Los usuarios pueden|Usuarios de<br />acceso<br />externo|Usuarios de<br />acceso de<br />invitado|
|---|---|---|
|Chatear con alguien de otra organización|Sí|Sí|
|Llamar a alguien de otra organización|Sí|Sí|
|Ver si alguien de otra organización está disponible para<br />realizar llamadas o chats|Sí|Sí1|
|Buscar personas de otras organización|Sí2|No|
|Compartir archivos|No|Sí|
|Ver el mensaje de fuera de oficina de una persona de otra<br />organización|No|Sí|
|Bloquear a alguien de otra organización|Sí|Sí|
|Usar @mentions|Sí3|Sí|
|Acceder a los recursos de Teams|No|Sí|
|Agregarse a un chat grupal <br />|Sí|Sí|
|Invitarse a una reunión|Sí|Sí|
|Realizar llamadas privadas|Sí|Sí5|
|Ver el número de teléfono de los participantes de la<br />reunión por acceso telefónico|No4|Sí|
|Usar vídeo IP|Sí|Sí5|
|Uso compartido de la pantalla|Sí3|Sí5|
|Usar reunirse ahora|No|Sí5|
|Editar los mensajes enviados|Sí3|Sí5|
|Eliminar mensajes enviados|Sí3|Sí5|
|Usar Giphy en las conversaciones|Sí3|Sí5|

**Centro Criptológico Nacional** 11
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**

|Usar adhesivos y memes en una conversación|Sí3|Sí5|
|---|---|---|
|Se muestra la presencia|Sí|Sí|

1 Si el usuario se ha agregado como invitado y ha iniciado sesión con la cuenta de
invitado.
2 solo por correo electrónico o dirección de protocolo de inicio de sesión (SIP).
3 compatible con chat individual entre dos usuarios de Teams solo de dos organizaciones
diferentes.
4 por defecto, los participantes externos no pueden ver los números de teléfono de los
participantes mediante teléfono.
5 está permitido de forma predeterminada, el administrador de Teams puede
desactivarlo.
#### **2.1.1 Configuración de toda la organización**
En el menú [Equipos\Configuración de Teams] se puede controlar qué características están disponibles para los usuarios de la organización, incluyendo notificaciones y
fuentes, integración de email, opciones de almacenamiento en la nube, y dispositivos.
**2.1.1.1** **Notificaciones y fuentes**
La fuente de actividades de Microsoft Teams permite a los usuarios evaluar los elementos que requieren atención mediante la notificación de cambios.
**Centro Criptológico Nacional** 12
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
**2.1.1.2** **Etiquetado**
Las etiquetas de Microsoft Teams permiten a los usuarios conectarse rápida y fácilmente con un subconjunto de personas de un equipo. Como recomendación, dejar a los
propietarios del equipo que puedan administrar etiquetas.
**2.1.1.3** **Integración de correo electrónico**
Activar esta característica para que los usuarios puedan enviar un correo electrónico a un canal en Microsoft Teams mediante la dirección de correo electrónico del canal.
**2.1.1.4** **Archivos**
Aquí se pueden activar o desactivar las opciones de uso compartido de archivos y de almacenamiento de archivos en la nube.
**Centro Criptológico Nacional** 13
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
Los usuarios pueden cargar y compartir archivos de los servicios de almacenamiento en nube en los canales y chats de Teams. Las opciones de almacenamiento en nube en
Microsoft Teams actualmente incluyen Citrix files, Dropbox, Box, Google Drive y Egnyte.
Activar el conmutador de los proveedores de almacenamiento en la nube que quiera usar la organización.
**Nota** : Como recomendación conviene habilitar únicamente aquellos servicios de
almacenamiento en nube que hayan sido aprobados y estén controlados por la organización. De lo contrario, existe el riesgo de almacenar información sensible en proveedores externos no
controlados por las directivas de la organización.
**2.1.1.5** **Organización**
Permite que los usuarios vean a otros usuarios en la jerarquía de la organización. La pestaña Organización muestra el organigrama de la empresa, de modo que, en una
conversación uno a uno, se puede ver a quién informa y quién le informa. También buscar otras personas mientras está allí para ver dónde aparecen en el gráfico.
**2.1.1.6** **Dispositivos**
Este apartado controla el comportamiento de la cuenta de recursos para los dispositivos de tipo “Surface Hub” que asisten a las reuniones de Microsoft Teams.
En el caso de que no se disponga de tales dispositivos, la recomendación es dejarlo desactivado.
**Centro Criptológico Nacional** 14
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
**2.1.1.7** **Buscar por nombre**
En este apartado se configura si se quiere limitar la búsqueda de los usuarios en Microsoft Teams a un subconjunto de los usuarios de toda la organización. Es decir, esto
nos permite crear límites virtuales para controlar la forma en que los usuarios pueden encontrar a otros usuarios de la organización y comunicarse con ellos. Para ello,
Microsoft Teams puede usar la directiva de libretas de direcciones (ABP) de Exchange o barreras de información.
La recomendación en este sentido es desactivarlo si no se cuenta con Address Book Policies o barreras de información.
**2.1.1.8** **Seguridad y comunicaciones**
Esta configuración está orientada principalmente a entornos educacionales para evitar un comportamiento de mensajería inadecuado. Con el chat supervisado permite a los
formadores designados iniciar chats con los alumnos e impide que los alumnos inicien nuevos chats a menos que esté presente un formador adecuado. Cuando se habilita la
supervisión del chat, los supervisores no pueden abandonar chats y otros participantes no pueden eliminarlos, lo que garantiza que los chats con alumnos se supervisen
correctamente.
**Centro Criptológico Nacional** 15
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
**2.1.1.9** **Canales compartidos**
Los canales compartidos en Microsoft Teams crean espacios de colaboración donde puede invitar a personas que no forman parte del equipo. Solo los usuarios que sean
propietarios o miembros del canal compartido pueden acceder al canal. Aunque los invitados (personas con cuentas en Microsoft Entra de invitado de la organización) no
se pueden agregar a un canal compartido, puede invitar a personas de fuera de su organización a participar en un canal compartido mediante Microsoft Entra conexión
directa B2B.
La recomendación en este sentido es dejar dicha característica deshabilitada.
### **2.2 Usuario final - primeros pasos**
Pulsar en el icono de Teams para acceder al portal de _Microsoft Teams_ (https://teams.microsoft.com).
**Centro Criptológico Nacional** 16
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
Las distintas opciones que se presentan en el menú de usuario son:
**Actividad** : comentarios y repuestas que ha hecho cada miembro del equipo
sobre algún tema. Para mostrar solamente las del propio usuario se debe seleccionar la opción “Mi actividad”.
**Chat** : para establecer nuevas conversaciones con cualquier miembro de la
organización o bien reanudar conversaciones.
**Equipos** : lista de canales, que son secciones que pueden crearse dentro de
un _equipo_ . Se pueden organizar los canales por temas, proyectos, etc.
**Llamadas** : muestra opciones de marcación rápida, lista de contactos e
historial de llamadas y correo de voz.
**OneDrive** : Acceso desde Teams al OneDrive del usuario.
**Calendario** : todas las reuniones y compromisos planificadas del usuario. Al
dar clic podrán ver su agenda completa.
**Aplicaciones** : acceso a las distintas aplicaciones integradas en Teams.
#### **2.2.1 Creación de un equipo**
Los equipos son recopilaciones de personas, contenido y herramientas alrededor de varios proyectos y tareas dentro de una organización.
- Los equipos pueden crearse para ser:
`o` Privados, solo para los usuarios invitados.
`o` Públicos, de modo que todos los integrantes de la organización se pueden unir.
**Centro Criptológico Nacional** 17
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
`o` De toda la organización, si la organización es nueva en Teams y no tiene más de 5.000 usuarios, se creará automáticamente un equipo de toda la
organización. Proporcionan a todos los miembros de la organización de tamaño pequeño a mediano una forma de formar parte de un único
equipo y de colaboración. Los equipos de toda la organización incluyen automáticamente todos los usuarios de la organización y mantienen la
pertenencia actualizada a medida que los usuarios se unen y abandonan la organización.
Además puede crearse un equipo desde cero, partiendo de un grupo existente en Microsoft 365 o desde plantilla. Para ello desde la aplicación (ya sea en su versión Web
- de escritorio) pulsaremos sobre el menú lateral de usuario “Equipos”, después sobre
el signo ‘ **+** ’ y en el menú desplegable seleccionaremos “Crear equipo”.
Podremos elegir si se crea el equipo _desde plantilla (ya sea desde cero u otras plantillas_ _predefinidas), desde otro equipo o desde un grupo existente de Microsoft 365_ .
**2.2.1.1** **Crear un equipo desde cero**
Cuando se crea un equipo, esto es lo que se crea:
- Un nuevo grupo de Microsoft 365.
- Un sitio de SharePoint Online y la biblioteca de documentos para almacenar los
archivos del equipo.
- Un buzón y un calendario compartidos de Exchange Online.
- Un bloc de notas de OneNote.
**Centro Criptológico Nacional** 18
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
- Vínculos con otras aplicaciones de Office 365, como Planner y Power BI.
Así pues, los pasos para generar un equipo desde cero son los siguientes:
1. Seleccionaremos la opción “ _Desde plantilla_ ” y elegiremos la plantilla con nombre “ _Desde cero_ ”.
2. Elegir si es Público, Privado o Toda la organización.
A continuación se describen las acciones para la creación de un ‘ _equipo privado’_, es decir, las personas del equipo necesitarán permiso para unirse.
3. Asignar un _nombre_ al equipo, y pulsar el botón “Crear”.
creará el equipo en Teams y se pasará al siguiente paso.
**Centro Criptológico Nacional** 19
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
4. Agregar _miembros_ al equipo.
5. Revisar configuración del equipo y realizar más operaciones si procede.
En el ejemplo, se ha creado el _equipo_ “CCN-Team1” y un _canal_ asociado “ _General_ ” (por defecto).
Pulsando en el menú “ _Mas opciones_ ” representado por el símbolo de los tres puntos ( **…** ) del equipo se desplieguen múltiples opciones:
Más adelante se describe la opción “ _Administrar equipo_ ” que es la opción más interesante desde el punto de vista de la seguridad.
**2.2.1.2** **Crear un equipo desde grupo existente de Microsoft 365**
Cuando se crea un equipo desde un grupo existente, la pertenencia del grupo, el sitio, el buzón y el bloc de notas se muestran en Teams.
1. Desde el menú lateral izquierdo de Teams seleccionamos “Equipos”, botón “ **+** ” y “Crear equipo”.
2. Pulsar el botón “ _Desde grupo_ ”.
**Centro Criptológico Nacional** 20
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
3. Elegir el grupo de Microsoft 365 a utilizar.
En este ejemplo elegir el grupo creado desde SharePoint “CCN-O365-Grupos1”.
Consultar información sobre la creación de grupos de SharePoint en la guía [CCNSTIC-885B - Guía de configuración segura para SharePoint Online].
4. Revisar configuración del equipo y realizar más operaciones si procede.
#### **2.2.2 Administrar equipo de Teams**
1. Seleccionar el equipo en el desplegable de equipos y pulsar el botón “Más opciones”, representado por los tres puntos ( **…** ).
**Centro Criptológico Nacional** 21
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
2. Seleccionar el ítem “Administrar equipo”.
Se muestra una pantalla con varias pestañas:
En la pestaña [Miembros] aparecen todos los miembros del equipo y su rol correspondiente. El propietario del equipo puede cambiar el **rol** de cada miembro
desde el desplegable de la columna _rol_ .
**Centro Criptológico Nacional** 22
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
En la pestaña [Configuración] aparecen distintas opciones, las más destacadas desde el punto de vista de la seguridad son:
- _Permisos de miembros_ : permitir la creación de canales, agregar aplicaciones
y más.
- _Permisos de invitados_ : permitir a invitados acciones sobre canales.
- _Código de equipo_ : código para compartir y que sea posible unirse al equipo
directamente (no se recibir solicitud para unirse).
Los permisos sobre miembros e invitados son:
Para ver como se administran permisos sobre el equipo y canales asociados consultar el apartado [3.1.1.2 Requisitos de acceso].
**Centro Criptológico Nacional** 23
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
### **3. CONFIGURACIÓN DE MICROSOFT TEAMS**
A continuación, se abordará la configuración del servicio _Microsoft Teams_ centrándose en el cumplimiento de los requisitos del Esquema Nacional de Seguridad que aplican
exclusivamente a este servicio.
### **3.1 Marco Operacional**
#### **3.1.1 Control de acceso**
**3.1.1.1** **Identificación**
La gestión de identidades de _Microsoft Teams_ es común a todas las aplicaciones de la solución Office 365 y se describe en la guía [CCN-STIC-885A - Guía de configuración
segura para Office 365].
**3.1.1.2** **Requisitos de acceso**
En este apartado se abordan los niveles de permisos existentes sobre un equipo y un canal, y cómo se conceden los derechos de acceso a los distintos miembros.
**Propietarios y miembros**
En Microsoft Teams hay dos _niveles de permisos de usuario_ : **propietario** y **miembro** . De forma predeterminada, a un usuario que crea un equipo nuevo se le concede el estado
de propietario. Además, los propietarios y miembros pueden tener capacidades de moderador para un canal (siempre que se haya configurado la moderación). Si se crea
un equipo a partir de un grupo existente de Microsoft 365, se heredan los permisos.
En la tabla siguiente se muestra la diferencia entre un propietario y un miembro a nivel de **Equipo** :

|Col1|Propietario de<br />equipo|Integrante de<br />grupo|
|---|---|---|
|Crear o eliminar un equipo|Sí|No|
|Editar nombre o descripción del equipo|Sí|No|
|Agregar miembros a un equipo privado|Sí|No|
|Agregar miembros al equipo público|Sí|Sí|
|Solicitud para agregar nuevo miembro|N/D|Sí|
|Promover o disminuir nivel del estado de<br />usuario|Sí|No|
|Abandonar equipo|Sí|Sí|

**Centro Criptológico Nacional** 24
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
En la tabla siguiente se muestra la diferencia entre un propietario y un miembro a nivel

|de Canales:|Col2|Col3|
|---|---|---|
||**Propietario de**<br />**equipo**|**Integrante de**<br />**grupo**|
|**Tareas de canal estándar**|||
|Crear o eliminar canal|Sí|Sí, si el propietario<br />del equipo lo ha<br />habilitado|
|**Editar nombre o descripción del canal**|Sí|Sí, si el propietario<br />del equipo lo ha<br />habilitado|
|**Tareas del canal privado**|||
|Crear un canal|Sí|Sí, si el propietario<br />del equipo lo ha<br />habilitado|
|Eliminar canal|Sí|No|
|Editar nombre o descripción del canal|No|N/D|
|Editar nombre o descripción del equipo|Sí|No|
|**Tareas de canal compartido**|||
|Crear un canal|Sí|No|
|Eliminar canal|Sí|No|
|Editar nombre o descripción del canal|No|No|

Los propietarios pueden convertir en propietarios a otros miembros del equipo. Un equipo puede tener hasta 100 propietarios. Se recomienda tener al menos dos
propietarios para evitar tener grupos huérfanos si un propietario abandona el equipo.
**Centro Criptológico Nacional** 25
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
**3.1.1.3** **Segregación de funciones y tareas**
Microsoft Teams dispone de varios **roles de administración** enfocados a administrar distintas partes y elementos del servicio:
- _Administrador de Teams_, se encarga de administrar el servicio de Microsoft
Teams, así como administrar y crear Grupos de Microsoft 365.
- _Administrador de comunicaciones de Teams_, se encarga de administrar las
características relativas a llamadas y reuniones dentro del servicio de Microsoft Teams.
- _Ingeniero de soporte en comunicaciones de Teams_, se encarga de hacer el
_troubleshooting_ de problemas de comunicaciones en Teams haciendo uso de herramientas avanzadas.
- _Especialista de soporte técnico de comunicaciones de Teams_, se encarga de hacer
el _troubleshooting_ de problemas de comunicaciones en Teams haciendo uso de herramientas básicas.
- _Administrador de dispositivos de Teams,_ se encarga de administrar dispositivos
configurados para su uso con el servicio de Teams.
El rol genérico de _Administrador de Teams_ puede asignarse desde el _Centro de_ _administración de Microsoft 365_ . Para asignar los roles específicos descritos
anteriormente se debe utilizar Azure AD. Consultar la guía [CCN-STIC-884A - Guía de configuración segura para Azure].
**3.1.1.4** **Proceso de gestión de derechos de acceso**
En este apartado se describe cómo un propietario puede asignar permisos al resto de miembros sobre el propio equipo o los canales asociados.
**Administrar equipo de Teams por un propietario**
1. Seleccionar el equipo en el desplegable de equipos y pulsar el botón “Más opciones”.
**Centro Criptológico Nacional** 26
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
2. Seleccionar el ítem “ _Administrar equipo_ ”.
Se muestra una pantalla con varias pestañas:
En la pestaña [Miembros] aparecen todos los miembros del equipo y su rol correspondiente. El propietario del equipo puede cambiar el **rol** de cada miembro
desde el desplegable de la columna _rol_ .
**Centro Criptológico Nacional** 27
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
En la pestaña [Configuración] aparecen distintas opciones, las más destacadas desde el punto de vista de la seguridad son:
- _Permisos de miembros_ : permitir la creación de canales, agregar aplicaciones
y más.
- _Permisos de invitados_ : permitir a invitados acciones sobre canales.
- _Código de equipo_ : código para compartir y que sea posible unirse al equipo
directamente (no se recibir solicitud para unirse).
Los permisos sobre miembros e invitados son:
**Asignar permisos en la configuración de un canal por un propietario**
Además de otras funciones, los propietarios y miembros de los equipos pueden tener capacidades de **moderador para un canal** (siempre que la moderación esté activada
para un equipo). Los moderadores pueden iniciar publicaciones nuevas en un canal y controlar si los miembros del equipo pueden responder a los mensajes de canal
existentes. También pueden controlar si los bots y los conectores pueden enviar mensajes de canal.
Para administrar la moderación de canales (por un propietario de un equipo):
1. En Teams, seleccionar canal de un equipo y pulsar el icono de “Más opciones”.
2. En el desplegable pulsar “Administrar canal”.
3. Gestionar los permisos.
**Centro Criptológico Nacional** 28
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
**3.1.1.5** **Mecanismos de autenticación (usuarios externos)**
Información sobre políticas de contraseñas, autenticación MFA y otros aspectos relacionados con la autenticación se muestra en la guía [CCN-STIC-885A - Guía de
configuración segura para Office 365].
Microsoft Teams usa la autenticación moderna para que la experiencia de inicio de sesión sea sencilla y segura. La autenticación moderna es un proceso que permite a los
equipos saber que los usuarios ya han escrito sus credenciales (como el correo electrónico y la contraseña del trabajo) en otro lugar y no es necesario que las vuelvan
a escribir para iniciar la aplicación.
Se requiere establecer un “doble factor de autenticación” (MFA), tener una política adecuada de gestión de credenciales y políticas de acceso condicional. Así mismo, se
requiere un registro de intentos de accesos con éxito y fallidos al sistema, descritos en el apartado [3.1.2.2 Registro de actividad]. Adicionalmente se puede controlar el acceso
a Office 365 mediante directivas de acceso condicional o reglas en ADFS, como se describe en la guía [CCN-STIC-884A - Guía de configuración segura para Azure].
**3.1.1.6** **Mecanismos de autenticación (usuarios de la organización)**
Información sobre políticas de contraseñas, autenticación MFA y otros aspectos relacionados con la autenticación se muestra en la guía [CCN-STIC-885A - Guía de
configuración segura para Office 365].
Microsoft Teams usa la autenticación moderna para que la experiencia de inicio de sesión sea sencilla y segura. La autenticación moderna es un proceso que permite a los
equipos saber que los usuarios ya han escrito sus credenciales (como el correo electrónico y la contraseña del trabajo) en otro lugar y no es necesario que las vuelvan
a escribir para iniciar la aplicación.
Se requiere establecer un “doble factor de autenticación” (MFA), tener una política adecuada de gestión de credenciales y políticas de acceso condicional. Así mismo, se
requiere un registro de intentos de accesos con éxito y fallidos al sistema, descritos en el apartado [3.1.2.2 Registro de actividad]. Adicionalmente se puede controlar el acceso
a Office 365 mediante directivas de acceso condicional o reglas en ADFS, como se describe en la guía [CCN-STIC-884A - Guía de configuración segura para Azure].
#### **3.1.2 Explotación**
_Microsoft Teams_ **siempre estará actualizado** . Es decir, el servicio es mantenido permanentemente por Microsoft, encargándose de las actualizaciones y parches, así
como de establecer los mecanismos de detección y protección ante amenazas, cumpliendo con el _Esquema Nacional de Seguridad_ en su categoría Alta.
**3.1.2.1** **Protección frente a código dañino**
Si la organización dispone de _Microsoft Defender para Office 365_ tendrá un explorador de detecciones en tiempo real, accesible desde el _Centro de Seguridad y cumplimiento_
**Centro Criptológico Nacional** 29
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
_de Office 365_ . Consultar la guía [CCN-STIC-885A - Guía de configuración segura para Office 365].
Destacar que cuando un archivo en _SharePoint Online_, _OneDrive For Business_ _Microsoft Teams_ se identifica como malintencionado, Microsoft Defender bloquea el archivo.
La imagen siguiente muestra un ejemplo de un archivo malintencionado
detectado en una biblioteca. Puede verse que el archivo está allí, pero está
bloqueado y muestra un icono de advertencia junto a él.
La opción más segura es **eliminar el archivo** .
**3.1.2.2** **Gestión de incidentes**
Ver apartado [3.1.2.1 Protección frente a código dañino] de la guía [CCN-STIC-885A Guía de configuración segura para Office 365] donde se explica cómo acceder a los informes de “Administración de Amenazas”.
**3.1.2.3** **Registro de actividad**
Para configurar el registro de actividad del servicio de Teams, será necesario hacer uso de la funcionalidad de Auditoría disponible a través del _Centro de Seguridad y_
_cumplimiento de Office 365_ . Más información en la guía [CCN-STIC-885A - Guía de configuración segura para Office 365].
Mencionar además que existen muchas actividades relacionadas con Teams en el registro de auditoría, accesibles desde el _Centro de Seguridad y cumplimiento, conocido_
_en la actualidad como Microsoft Purview en el_ menú [Auditar/Nueva búsqueda]:
Como ejemplo de tales consultas:
**Centro Criptológico Nacional** 30
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
#### **3.1.3 Monitorización del sistema**
Consultar la guía [CCN-STIC-885A - Guía de configuración segura para Office 365] para ver los distintos mecanismos de monitorización del servicio, y el apartado [Registro de
actividad] de la presente guía.
### **3.2 Medidas de protección**
#### **3.2.1 Protección de las comunicaciones**
En cuanto a la protección de las comunicaciones, cabe reseñar que se usan los protocolos criptográficos para conexiones TLS, integrados en Office 365 de manera
automática. Esto es así cuando:
- Los usuarios trabajan con archivos guardados en _OneDrive For Business_
SharePoint Online.
- Los usuarios comparten archivos en reuniones en línea y conversaciones de
mensajería instantánea.
En realidad, todas las comunicaciones de Office 365 están cifradas: Clientes de correo (POP, IMAP, SMTP-TLS), Clientes Outlook (MAPI-HTTPS), Navegadores (Web HTTPS),
Dispositivos móviles (ActiveSync HTTPS), Teams y Skype (SIP-TLS). No es necesario realizar ninguna configuración adicional, pero es importante indicar que, a partir de
junio 2020, se eliminará soporte de TLS 1.0 y 1.1. Esto tiene implicaciones directas en los clientes .
**Centro Criptológico Nacional** 31
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
#### **3.2.2 Protección de la información**
**3.2.2.1** **Calificación de la información**
Office 365 cuenta con diversos mecanismos para calificar la información, como se explican en el apartado [Calificación de la información] de la guía [CCN-STIC-885A - Guía
de configuración segura para Office 365].
Respecto a las etiquetas de retención para Teams, desde el _Portal de Purview,_ es posible establecer como ubicaciones en políticas de retención, tanto los “Mensajes de canal de
Teams”, en los “Chats de Teams e interacciones con Copilot” y en “Mensajes del canal privado de Teams”. Es decir, que se puede actuar proactivamente en decidir si conservar
y/o eliminar contenido en función de la duración del tiempo, tanto en las conversaciones, chats como en los mensajes de canal.
**3.2.2.2** **Limpieza de documentos**
Al compartir una copia electrónica de determinados documentos de Office365 o al exponer cierta documentación en internet, es una buena práctica revisar el documento
en busca de datos ocultos, información personal y en general cualquier metadato que pudiera estar asociado. Es posible eliminar esta información a través del _**Inspector de**_
_**documentos,**_ característica que se accede desde las propias aplicaciones de Word, Excel, PowerPoint o Visio.
**3.2.2.3** **Copias de Seguridad**
No existe una solución global de respaldo de Office 365.
Aunque un mecanismo basado en “políticas de retención” en ciertos casos puede resultar suficiente para garantizar el respaldo de la información. Consultar el apartado
[3.2.3.1 Calificación de la información] para ver cómo se aplican a un documento y cómo puede servir para protegerlo de ser eliminado.
Una opción interesante relacionada con los mecanismos de respaldo es el “ **Archivado** ”.
Con el tiempo, es posible que un equipo creado en Microsoft Teams se quede fuera de uso o que se desee archivar o eliminar un equipo al final de un proyecto.
**Archivar un** _**equipo**_ **en Microsoft Teams**
Cuando archiva un _equipo_, se detiene toda la actividad de ese equipo. El archivado de un equipo también archiva los canales privados y sus colecciones de sitios asociadas. Sin
embargo, aún se puede agregar o quitar miembros y actualizar roles, y aún se puede ver toda la actividad del equipo en los canales, los archivos y los chats estándar y privados.
**Centro Criptológico Nacional** 32
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
1. En el centro de administración de Microsoft Teams, seleccionar [Equipos\Administrar equipos].
2. Seleccionar un equipo haciendo clic en el nombre del equipo.
3. Seleccione _**Archivar**_ .
Y aparecerá el siguiente mensaje:
Al pulsar “Archivar” el estado asociado al equipo pasará de “Activo” a “Archivado”.
En cualquier momento se puede deshacer la operación con la opción “Desarchivar”:
**Eliminar un** _**equipo**_ **en Microsoft Teams**
Si el equipo no se va a necesitar en el futuro, puede eliminarse en lugar de archivarlo.
1. En el centro de administración de Microsoft Teams, seleccionar [Equipos\Administrar equipos].
**Centro Criptológico Nacional** 33
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
2. Seleccionar un _equipo_ haciendo clic en el nombre del equipo.
3. Seleccione “Eliminar”. Aparecerá un mensaje de confirmación.
**Restauración de un equipo en Microsoft Teams**
La operación de **restauración** de un equipo se realiza de la siguiente manera:
1. En el centro de administración de Microsoft Teams, seleccionar [Equipos\Administrar equipos].
2. Seleccionaremos “Acciones” y pulsaremos sobre “Ver equipos eliminados”.
3. Nos mostrará una ventana con los equipos eliminados. Seleccionaremos el equipo a restaurar y pulsaremos sobre el botón “Restaurar”.
De forma predeterminada, un equipo de Teams eliminado se conserva durante 30 días.
**Centro Criptológico Nacional** 34
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
#### **3.2.3 Protección de los servicios**
**3.2.3.1** **Protección frente a la denegación de servicio**
Office 365 ofrece un sistema avanzado de **detección de amenazas** y **sistemas de**
**mitigación** para proteger la infraestructura subyacente de los ataques de _denegación de_
_servicio_ (DoS) y prevenir la interrupción de servicio a los clientes.
El sistema de defensa DDoS de Azure está diseñado no solo para resistir ataques desde el exterior, sino también desde otros _Tenants_ de Azure. Los mecanismos de limitación
de peticiones de Exchange Online y SharePoint Online forman parte de un enfoque de varias capas para defenderse contra ataques DoS.
Consultar la guía [CCN-STIC-884A - Guía de configuración segura para Azure] para obtener más información sobre el _sistema de defensa DDoS de Azure_ .
**Centro Criptológico Nacional** 35
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
### **4. OTRAS CONSIDERACIONES DE SEGURIDAD**
Desde el _Centro de administración de Microsoft Teams_ pueden configurarse directivas de equipos, mensajería, reuniones, aplicaciones y voz y controlar a qué usuarios de la
organización deben aplicarse. A continuación se muestran aquellas características que tienen cierta relevancia en la seguridad.
### **4.1 Directiva de equipos**
Las directivas de equipos y canales se usan para controlar la configuración o características que están disponibles para los usuarios cuando usan los equipos y
canales. Se puede usar la directiva global (predeterminada para toda la organización) y personalizarla, o bien se puede crear una o varias directivas personalizadas para los
miembros de un equipo o canal de la organización.
- Descubrir equipos privados: Activar esta opción para permitir que los usuarios
busquen equipos privados. Cuando encuentren un equipo privado, podrán solicitar unirse.
- Crear canales privados: Cuando está activado, los propietarios y miembros del
equipo pueden crear canales privados. (Los propietarios de equipos pueden controlar si los miembros pueden crear canales privados en cada equipo).
- Crear canales compartidos: Cuando está activado, los propietarios de equipos
pueden crear canales compartidos. Las aplicaciones de Teams que están disponibles para la organización también están disponibles en canales
compartidos.
- Invitar a usuarios externos a canales compartidos: Cuando está activada, los
propietarios y los miembros de canales compartidos pueden invitar a participantes externos de organizaciones donde se haya configurado una
confianza entre organizaciones.
**Centro Criptológico Nacional** 36
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
- Unirse a canales compartidos externos: Cuando está activada, los usuarios
pueden participar en canales compartidos creados por otras organizaciones donde se ha configurado una confianza entre organizaciones. Las directivas de
Teams para la otra organización se aplican a estos canales.
### **4.2 Directivas de mensajería**
Las directivas de mensajería se usan para controlar qué características de mensajería por chat y canales están disponibles para los usuarios de Teams. Se puede usar la
directiva global (predeterminada para toda la organización), o bien se puede crear una
- varias directivas de mensajería personalizadas para los contactos de la organización.
De forma predeterminada, se crea una directiva denominada **global** (opción predeterminada para toda la organización). A todos los usuarios de la organización se
les asignará esta directiva de mensajería de forma predeterminada, a menos que creemos y asignemos una directiva personalizada. Se pueden realizar cambios en esta
Directiva o crear una o más directivas personalizadas y asignarles usuarios.
Por ejemplo, supongamos que se desea asegurarse de que los mensajes enviados no se eliminen ni modifiquen por parte de los usuarios. Se debería crear una nueva directiva
personalizada denominada "R _etener mensajes enviados_ " y con la configuración siguiente:
- Los propietarios pueden eliminar los mensajes enviados.
- Los usuarios NO pueden eliminar mensajes enviados
- Los usuarios NO pueden editar mensajes enviados
1. Acceder al _Centro_ _de_ _administración_ _de_ _Microsoft_ _Teams._ Menú [Mensajería\Directivas de mensajería].
2. Pulsar el botón “Agregar”.
**Centro Criptológico Nacional** 37
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
3. Configurar la opciones y “Guardar”.
### **4.3 Directivas de permisos de aplicaciones**
Las directivas de permisos de aplicaciones controlan qué aplicaciones estarán disponibles para los usuarios de Teams en la organización. Se puede usar la directiva
global (predeterminada para toda la organización) y personalizarla, o bien se puede crear una o varias directivas para satisfacer las necesidades de su organización.
Se accede desde el _Centro de administración de Microsoft Teams._ Menú [Aplicaciones de Teams\Administrar aplicaciones]. Una vez allí, pulsaremos sobre el botón “Acciones”
y seleccionaremos “Configuración de la aplicación para toda la organización”.
Permite configurar qué aplicaciones de Microsoft, de terceros y personalizadas pueden instalar los usuarios. Se recomienda habilitar únicamente aquellas aplicaciones que
hayan sido probadas y autorizadas por la organización, y mantener un control sobre las aplicaciones que se publican en la tienda.
**Centro Criptológico Nacional** 38
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
### **4.4 Directivas de configuración de la aplicación**
Las directivas de configuración de aplicaciones controlan la forma en que las aplicaciones están disponibles para el usuario con la aplicación de Teams.
Las aplicaciones se anclan a la barra de la aplicación. Esta es la barra en el lateral del cliente de escritorio de Teams y en la parte inferior de los clientes móviles de Teams (iOS
y Android).
Puede usarse la directiva global (predeterminada para toda la organización) y personalizarla, o bien pueden crearse directivas personalizadas y asignarlas a un
conjunto de usuarios.
Se accede desde el _Centro de administración de Microsoft Teams._ Menú [Aplicaciones de Teams\Directivas de configuración].
**Centro Criptológico Nacional** 39
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
Se recomienda NO permitir la “Carga de aplicaciones personalizadas”.
### **4.5 Directivas de voz**
En Microsoft Teams, las directivas de llamadas controlan qué características de llamadas y desvío de llamadas están disponibles para los usuarios. Las políticas de llamadas
determinan si un usuario puede hacer llamadas privadas, usar el desvío de llamadas o llamar de forma simultánea a otros usuarios o números de teléfono externos, enrutar
llamadas al buzón de voz, enviar llamadas a grupos de llamadas, usar la delegación para llamadas entrantes y salientes, etc.
**Nota** : Microsoft Teams permite conectar el servicio Online con una centralita telefónica local o
de nube, a través del enrutamiento directo. Se requiere un controlador de borde de sesión (SBC)
compatible. Desde el punto de vista de la seguridad, si la organización tiene previsto integrar este servicio, se deberá garantizar que la comunicación SIP esté cifrada con TLS 1.2.
### **4.6 Directivas de reunión**
Las _directivas de reunión_ se usan para controlar qué características están disponibles para los usuarios cuando se unen a reuniones de Microsoft Teams y también administrar
las experiencias de unirse a la reunión y de la sala de espera.
Se accede desde el _Centro de administración de Microsoft Teams._ Menú [Reuniones\ Directivas de reunión].
**Centro Criptológico Nacional** 40
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
Puede usarse la directiva global (predeterminada para toda la organización) y personalizarla, o bien pueden crearse una o varias directivas de reunión personalizadas
para las personas que organicen reuniones en la organización.
Con estas directivas puede establecerse, por ejemplo, el bloqueo para usuarios anónimos, permitir o bloquear grabación, permitir el uso compartido, etc.
### **4.7 Directivas de dispositivos**
Teams permite conectar dispositivos que estén certificados (teléfonos, pantallas, Surface Hub, Dispositivos SIP, paneles, etc.) directamente con el servicio. Cada vez es
más habitual ver dispositivos de conferencia y teléfonos utilizándose con Teams.
Se pueden controlar los teléfonos IP y dispositivos periféricos, como auriculares y cámaras web que se han certificado para su uso con Teams. Pueden crearse y cargar
perfiles de configuración para cada tipo de dispositivo que disponga la organización, de forma que puedan realizarse cambios en su configuración.
Se accede desde el Centro de administración de Microsoft Teams. Menú [Dispositivos de Teams].
**Centro Criptológico Nacional** 41
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
**Perfiles de configuración**
Desde la pestaña “Perfiles de configuración” es posible controlar opciones de seguridad del dispositivo (teléfonos, paneles y pantallas) como bloqueo, PIN, protector de pantalla,
logs, etc.
**Centro Criptológico Nacional** 42
**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**
### 5. CUADRO RESUMEN DE MEDIDAS DE SEGURIDAD
Se facilita a continuación un cuadro resumen de configuraciones a aplicar para la protección del servicio, donde la organización podrá valorar qué medidas de las propuestas se cumplen.

|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
|op|**Marco Operacional**|**Marco Operacional**|**Marco Operacional**|
|op.acc|**Control de Acceso**|**Control de Acceso**|**Control de Acceso**|
|op.acc.1|**Identificación**|**Identificación**|**Identificación**|
|op.acc.1|Se ha configurado el uso de cuentas y la asignación de licencias a usuarios.<br />Siguiendo las recomendaciones de Office 365 basada en la guía [CCN-STIC-885A -<br />Guía de configuración segura para Office 365]<br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
|op.acc.1|Se ha configurado el uso de cuentas y la asignación de licencias a usuarios.<br />Siguiendo las recomendaciones de Office 365 basada en la guía [CCN-STIC-885A -<br />Guía de configuración segura para Office 365]<br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|Op.acc.2|**_Requisitos de Acceso_ **|**_Requisitos de Acceso_ **|**_Requisitos de Acceso_ **|

**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**

|Col1|Se han comprobado los niveles de permisos de los recursos: propietarios y<br />miembro.|Aplica:<br />Si No|Cumple:<br />Si No|
|---|---|---|---|
||Se han comprobado los_niveles de permisos_ de los recursos: propietarios y<br />miembro.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|Op.acc.3|**Segregación de funciones y tareas**|**Segregación de funciones y tareas**|**Segregación de funciones y tareas**|
|Op.acc.3|Se ha asignado adecuadamente los roles de administrador (en caso de que<br />se haya establecido una delegación para este servicio).<br />Siguiendo las recomendaciones del apartado Segregación de funciones y<br />tareas en la guía [CCN-STIC-885A - Guía de configuración segura para Office<br />365]<br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
|Op.acc.3|Se ha asignado adecuadamente los roles de administrador (en caso de que<br />se haya establecido una delegación para este servicio).<br />Siguiendo las recomendaciones del apartado Segregación de funciones y<br />tareas en la guía [CCN-STIC-885A - Guía de configuración segura para Office<br />365]<br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|

**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**

|Op.acc.4|Proceso de gestión de derechos de acceso|Col3|Col4|
|---|---|---|---|
||Se han revisado los permisos específicos en cada uno de los usuarios de los<br />equipos creados.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se han revisado los permisos específicos en cada uno de los usuarios de los<br />equipos creados.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|Op.acc.5|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|
|Op.acc.5|Se ha habilitado_Multi-Factor Authentication_ (MFA) para los usuarios<br />externos.<br />_Siguiendo recomendaciones del apartado Mecanismos de autenticación en la_<br />_guía [CCN-STIC-885A - Guía de configuración segura para Office 365]_<br /> <br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
|Op.acc.5|Se ha habilitado_Multi-Factor Authentication_ (MFA) para los usuarios<br />externos.<br />_Siguiendo recomendaciones del apartado Mecanismos de autenticación en la_<br />_guía [CCN-STIC-885A - Guía de configuración segura para Office 365]_<br /> <br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|

**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**

|Op.acc.5|Mecanismo de autenticación (usuarios externos)|Col3|Col4|
|---|---|---|---|
|Op.acc.5|Se dispone de un registro de intentos de accesos con éxito y fallidos al<br />sistema.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
|Op.acc.5|Se dispone de un registro de intentos de accesos con éxito y fallidos al<br />sistema.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|Op.acc.6|**Mecanismo de autenticación (usuarios de la organización)**|||
||Se encuentra habilitado el “doble factor de autenticación” y/o directivas de<br />acceso condicional, como se describe en la guía [CCN-STIC-885A - Guía de<br />configuración segura para Office 365].|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se encuentra habilitado el “doble factor de autenticación” y/o directivas de<br />acceso condicional, como se describe en la guía [CCN-STIC-885A - Guía de<br />configuración segura para Office 365].|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|

**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**

|Op.acc.6|Mecanismo de autenticación (usuarios de la organización)|Col3|Col4|
|---|---|---|---|
||Se dispone de un registro de intentos de accesos con éxito y fallidos al<br />sistema.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se dispone de un registro de intentos de accesos con éxito y fallidos al<br />sistema.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|op.exp|**Explotacion**|**Explotacion**|**Explotacion**|
|op.exp.6|**Protección frente a código dañino**|**Protección frente a código dañino**|**Protección frente a código dañino**|
||Se comprueba periódicamente la detección de amenazas en tiempo real,<br />accesible desde el_Centro de Seguridad y cumplimiento de Office 365_, y se<br />genera el informe pertinente.<br />* Si la organización dispone de_Microsoft Defender para Office 365_. <br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se comprueba periódicamente la detección de amenazas en tiempo real,<br />accesible desde el_Centro de Seguridad y cumplimiento de Office 365_, y se<br />genera el informe pertinente.<br />* Si la organización dispone de_Microsoft Defender para Office 365_. <br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br />|**Observaciones:**|

**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|op.exp.7|**Gestión de incidentes**|**Gestión de incidentes**|**Gestión de incidentes**|
||Se comprueba periódicamente la detección de amenazas en tiempo real,<br />accesible desde el Centro de Seguridad y cumplimiento de Office 365, y se<br />genera el informe pertinente.<br />* Si la organización dispone de Microsoft Defender para Office 365.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se comprueba periódicamente la detección de amenazas en tiempo real,<br />accesible desde el Centro de Seguridad y cumplimiento de Office 365, y se<br />genera el informe pertinente.<br />* Si la organización dispone de Microsoft Defender para Office 365.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|op.exp.8|**Registro de la actividad**|**Registro de la actividad**|**Registro de la actividad**|
||Se ha activado el registro de auditoría.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se ha activado el registro de auditoría.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br />|**Observaciones:**|

**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|op.mon|**Monitorización del sistema**|**Monitorización del sistema**|**Monitorización del sistema**|
||Se han configurado alertas en el_Centro de Seguridad y cumplimiento de_<br />_Office 365._<br />_Siguiendo las recomendaciones del apartado Monitorización del sistema en_<br />_la guía [CCN-STIC-885A - Guía de configuración segura para Office 365]_<br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se han configurado alertas en el_Centro de Seguridad y cumplimiento de_<br />_Office 365._<br />_Siguiendo las recomendaciones del apartado Monitorización del sistema en_<br />_la guía [CCN-STIC-885A - Guía de configuración segura para Office 365]_<br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|mp|**Medidas de Protección**|**Medidas de Protección**|**Medidas de Protección**|
|mp.info|**Protección de la información**|**Protección de la información**|**Protección de la información**|
|mp.info.2|**Calificación de la información**|**Calificación de la información**|**Calificación de la información**|
||Se han aplicado políticas de retención.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se han aplicado políticas de retención.|**Evidencias Recogidas:**|**Observaciones:**|

**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**

|Col1|Col2|Si No|Col4|
|---|---|---|---|
|mp.info.2|**Calificación de la información**|**Calificación de la información**|**Calificación de la información**|
||Se han aplicado políticas de DLPs.<br />_Siguiendo las recomendaciones del apartado DLPs (Data Loss Prevention) en_<br />_la guía [CCN-STIC-885A - Guía de configuración segura para Office 365]_<br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se han aplicado políticas de DLPs.<br />_Siguiendo las recomendaciones del apartado DLPs (Data Loss Prevention) en_<br />_la guía [CCN-STIC-885A - Guía de configuración segura para Office 365]_<br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|mp.info.2|**Calificación de la información**|**Calificación de la información**|**Calificación de la información**|
||Se han aplicado_ sensitivity labels._<br />_Siguiendo las recomendaciones del apartado Calificación de la información_<br />_en la guía [CCN-STIC-885A - Guía de configuración segura para Office 365]_<br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se han aplicado_ sensitivity labels._<br />_Siguiendo las recomendaciones del apartado Calificación de la información_<br />_en la guía [CCN-STIC-885A - Guía de configuración segura para Office 365]_<br />|**Evidencias Recogidas:**|**Observaciones:**|

**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**

|Col1|Col2|Si No|Col4|
|---|---|---|---|
|mp.info.9|**Copias de seguridad**|**Copias de seguridad**|**Copias de seguridad**|
||Se ha comprobado el archivado/eliminación de_equipos_ en Microsoft Teams.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se ha comprobado el archivado/eliminación de_equipos_ en Microsoft Teams.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|mp.s|**Protección de los servicios**|**Protección de los servicios**|**Protección de los servicios**|
|mp.s.8|**Protección frente a la denegación de servicio**|**Protección frente a la denegación de servicio**|**Protección frente a la denegación de servicio**|
||Se ha tenido en cuenta la información detallada en la guía [CCN-STIC-884A -<br />Guía de configuración segura para Azure] sobre el_sistema de defensa DDoS_<br />_de Azure_. <br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|

**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**

|Col1|Col2|Evidencias Recogidas:<br />Si No|Observaciones:|
|---|---|---|---|
||**OTRAS CONSIDERACIONES DE SEGURIDAD**|**OTRAS CONSIDERACIONES DE SEGURIDAD**|**OTRAS CONSIDERACIONES DE SEGURIDAD**|
||**Directivas de equipos**|**Directivas de equipos**|**Directivas de equipos**|
||Se han revisado las directivas de equipos|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se han revisado las directivas de equipos|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
||**Directivas de mensajería**|**Directivas de mensajería**|**Directivas de mensajería**|
||Se han revisado las directivas de mensajería.|**Aplica:**|**Cumple:**|

**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**

|Col1|Col2|Si No|Si No|
|---|---|---|---|
|||Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
||**Directivas de permisos de aplicaciones**|**Directivas de permisos de aplicaciones**|**Directivas de permisos de aplicaciones**|
||Se han revisado las directivas de configuracion y permisos de aplicaciones.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se han revisado las directivas de configuracion y permisos de aplicaciones.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|||||
||**Directivas de reunión**|**Directivas de reunión**|**Directivas de reunión**|

**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**

|Col1|Se han revisado las directivas de reunión.|Aplica:<br />Si No|Cumple:<br />Si No|
|---|---|---|---|
||Se han revisado las directivas de reunión.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
||**Directivas de dispositivos**|**Directivas de dispositivos**|**Directivas de dispositivos**|
||Se han revisado las directivas de dispositivos.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se han revisado las directivas de dispositivos.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|

**CCN-STIC 885D** **Guía de configuración segura para Microsoft Teams**