---
id: ccn-stic-885a---guia-de-configuracion-segura-para-office-365
title: "Ccn Stic 885A   Guía De Configuración Segura Para Office 365"
sidebar_label: "Ccn Stic 885A   Guía De Configuración Segura Para Office 365"
---

# **Guía de Seguridad de las TIC** **CCN-STIC 885A** **Guía de configuración segura para Office 365**
## **MAYO 2024**
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Catálogo de Publicaciones de la Administración General del Estado**
**https://cpage.mpr.gob.es**
CRIPTOLOGICO NACIONAL, c=ES 2024.05.30 12:18:37 +02'00'
Pº de la Castellana 109, 28046 Madrid  Centro Criptológico Nacional, 2024
NIPO: 083-24-177-0 Fecha de Edición: mayo de 2024
**LIMITACIÓN DE RESPONSABILIDAD**
El presente documento se proporciona de acuerdo con los términos en él recogidos, rechazando expresamente cualquier tipo de garantía implícita que se pueda encontrar relacionada. En ningún caso,
el Centro Criptológico Nacional puede ser considerado responsable del daño directo, indirecto, fortuito
- extraordinario derivado de la utilización de la información y software que se indican incluso cuando se
advierta de tal posibilidad.
**AVISO LEGAL**
Quedan rigurosamente prohibidas, sin la autorización escrita del Centro Criptológico Nacional, bajo las sanciones establecidas en las leyes, la reproducción parcial o total de este documento por cualquier
medio o procedimiento, comprendidos la reprografía y el tratamiento informático, y la distribución de ejemplares del mismo mediante alquiler o préstamo públicos.
**Centro Criptológico Nacional** 2
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
### **ÍNDICE**
**1.** **OFFICE 365**
1.1 DESCRIPCION DEL USO DE ESTA GUÍA
1.2 DEFICIÓN DE LA SOLUCIÓN
1.3 PRERREQUISITOS PARA EL DESPLIEGUE MEDIANTE POWERSHELL
**2.** **DESPLIEGUE DE OFFICE 365**
2.1 ADMINISTRADOR – CONFIGURACION INICIAL
2.2 USUARIO FINAL – PRIMEROS PASOS
**3.** **CONFIGURACIÓN DE OFFICE 365**
3.1 MARCO OPERACIONAL
3.1.1 CONTROL DE ACCESO
3.1.1.1 IDENTIFICACIÓN
3.1.1.2 REQUISITOS DE ACCESO
3.1.1.3 SEGREGACIÓN DE FUNCIONES Y TAREAS
3.1.1.4 PROCESO DE GESTIÓN DE DERECHOS DE ACCESO
3.1.1.5 MECANISMO DE AUTENTICACIÓN (USUARIOS EXTERNOS)
3.1.1.6 MECANISMO DE AUTENTICACIÓN (USUARIOS DE LA ORGANIZACIÓN)
3.1.2 EXPLOTACIÓN
3.1.2.1 PROTECCIÓN FRENTE A CÓDIGO DAÑINO
3.1.2.2 GESTIÓN DE INCIDENTES
3.1.2.3 REGISTRO DE LA ACTIVIDAD
3.1.3 MONITORIZACIÓN DEL SISTEMA
3.2 MEDIDAS DE PROTECCIÓN
3.2.1 PROTECCIÓN DE LAS COMUNICACIONES
3.2.2 PROTECCIÓN DE LA INFORMACIÓN
3.2.2.1 CALIFICACIÓN DE LA INFORMACIÓN
3.2.2.2 LIMPIEZA DE DOCUMENTOS
3.2.2.3 COPIAS DE SEGURIDAD
3.2.3 PROTECCIÓN DE LOS SERVICIOS
3.2.3.1 PROTECCIÓN FRENTE A DENEGACIÓN DE SERVICIO
**4.** **OTRAS CONSIDERACIONES DE SEGURIDAD**
4.1 SERVICIOS Y COMPLEMENTOS
**5.** **CARACTERÍSTICAS DISPONIBLES POR LICENCIAMIENTO**
**6.** **GLOSARIO Y ABREVIATURAS**
**7.** **ANEXO A. CREAR UNA CUENTA DE USUARIO INDIVIDUAL**
**8.** **ANEXO B. CREAR VARIAS CUENTAS DE USUARIO**
**9.** **CUADRO RESUMEN DE MEDIDAS DE SEGURIDAD**
**Centro Criptológico Nacional** 3
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
### **1. OFFICE 365** **1.1 DESCRIPCION DEL USO DE ESTA GUÍA**
El objetivo de la presente guía es indicar los pasos a seguir para la configuración de Office 365 cumpliendo con los requisitos Esquema Nacional de Seguridad en su
categoría ALTA.
En esta guía se abordarán los **servicios esenciales comunes** a todos los servicios de la solución informática Office 365 y debe consultarse juntamente con el resto de las
guías específicas de cada servicio: Sharepoint Online [CCN-STIC-885B - Guía de configuración segura para Sharepoint Online], Exchange Online [CCN-STIC-885C - Guía
de configuración segura para Exchange Online] y Teams [CCN-STIC-885D - Guía de configuración segura para Microsoft Teams].
El escenario que se presenta en las guías es el de “sólo nube”, no contemplándose la hibridación de sistemas On-premises de la organización con entorno Cloud.
Para la confección de esta guía se han consultado las siguientes fuentes:
- Documentación oficial de Microsoft.
- CCN-STIC-884A - Guía de configuración segura para Azure.
- ENS Real Decreto BOE-A-2010-1330.
- ENS Real Decreto BOE-A-2022-7191.
### **1.2 DEFICIÓN DE LA SOLUCIÓN**
Office 365 es un conjunto de aplicaciones y servicios basados en la nube alojados en servidores propiedad de Microsoft y disponibles desde dispositivos con conexión a
Internet. Office 365 funciona sobre Entra ID.
Se trata de una solución de Microsoft que nos permite crear, acceder y compartir
documentos de Word, Excel, OneNote y PowerPoint desde cualquier dispositivo que
tenga acceso a internet.
Además de proporcionar herramientas adicionales de correo electrónico, mensajería
instantánea, videoconferencias, pantallas compartidas, almacenamiento en la nube,
calendarios, contactos, etc.
**Centro Criptológico Nacional** 4
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
### **1.3 PRERREQUISITOS PARA EL DESPLIEGUE MEDIANTE POWERSHELL**
PowerShell de Office 365 permite administrar la configuración de Office 365 desde la línea de comandos. Conectarse a PowerShell de Office 365 es un proceso sencillo
que consiste en instalar el software necesario y conectarse a la organización de Office 365.
Hay tres versiones del módulo de PowerShell que puede usarse para conectarse a Office 365 y administrar cuentas de usuario, grupos y licencias:
a) _Microsoft Azure Active Directory PowerShell para Graph_ (los cmdlets incluyen Azure AD en su nombre).
b) _Microsoft Azure Active Directory para Windows PowerShell_ (los cmdlets incluyen MSOL en su nombre).
c) _Microsoft Graph PowerShell_ (los cmdlets incluyen MG en su nombre).
El día 30 de marzo del 2024, los módulos _Microsoft Azure Active Directory_ _PowerShell para Graph_ y Módulo _Microsoft Azure Active Directory para Windows_
_PowerShell_ fueron deprecados y sustituidos por _Microsoft Graph PowerShell_ . Esto no significa que no se puedan utilizar, si no que al estar deprecados dejaran de recibir
actualizaciones.
Conviene destacar que existen dos caminos para la ejecución de los comandos de PowerShell descritos en esta guía: Azure Cloud Shell, incluido en el propio portal de
Entra ID; y ejecución remota de PowerShell, instalando los módulos necesarios en el equipo cliente del administrador. La seguridad para la conexión con _Microsoft Graph_,
se hace desde:
a) Autenticación inicial. Mediante un usuario, Token y Certificado digital con los derechos adecuados para la administración del servicio.
b) Cifrado continuo de la comunicación. Una vez completada la autenticación inicial, el protocolo de comunicación remota de PowerShell cifra toda la
comunicación con una clave simétrica AES256 por sesión.
**Requerimientos previos**
Usar una versión de 64 bits de Windows. Es necesario así mismo, usar la versión 7 o posterior de PowerShell. Más información sobre requerimientos previos de
[plataformas en: Install the Microsoft Graph PowerShell SDK | Microsoft Learn](https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation?view=graph-powershell-1.0)
**Instalar módulo Microsoft Graph PowerShell**
Estos pasos son necesarios una sola vez en el equipo, no cada vez que se conecta.
Sin embargo, probablemente se necesitará instalar las versiones más recientes de software periódicamente.
a) Instalar el Módulo _Microsoft Graph PowerShell_ para Windows siguiendo estos pasos:
1. Abrir un símbolo del sistema de Windows PowerShell con privilegios elevados (ejecute Windows PowerShell como administrador).
**Centro Criptológico Nacional** 5
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
2. Ejecutar el comando:
```
Install-Module Microsoft.Graph -Scope CurrentUser
```
b) Para actualizar una nueva versión del módulo ejecutar el comando anterior con el parámetro Force:
```
Update-Module Microsoft.Graph
```
**Nota:** Se recomienda realizar actualizaciones mensuales.
c) Conectarse a Microsoft Graph Para conectarse a Microsoft Graph tenemos varios métodos, por usuario y
contraseña, token, certificado, etc. El método más rápido es:
```
Connect-MgGraph -Scopes "User.ReadWrite.All"
```
La etiqueta -Scope se refiere a los permisos que tendrá el usuario cuando haga login, en este ejemplo son de lectura y escritura de usuarios. Existen más
métodos de login con este comando, para obtener más información, revisar el [enlace Connect-MgGraph.](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.authentication/connect-mggraph?view=graph-powershell-1.0)
Una vez ejecutado el comando anterior nos saldrá
esta ventana, pidiendo permisos sobre el tenant,
click en Aceptar.
**Centro Criptológico Nacional** 6
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
### **2. DESPLIEGUE DE OFFICE 365**
Esta guía hace referencia a la configuración de seguridad de Office 365. La información específica de cada servicio se encuentra en las siguientes guías:
Sharepoint Online [CCN-STIC-885B - Guía de configuración segura para Sharepoint Online], Exchange Online [CCN-STIC-885C - Guía de configuración segura para
Exchange Online] y Teams [CCN-STIC-885D - Guía de configuración segura para Microsoft Teams].
Office 365 se encuentra englobado en la categoría de servicio SaaS (Software as a Service). El CSP (Microsoft) es el encargado de ofrecer al cliente el software como un
servicio.
### **2.1 ADMINISTRADOR – CONFIGURACION INICIAL**
**a)** **Acceder al portal de Office 365 con usuario administrador.**
El usuario administrador podrá acceder al portal Office 365 a través de esta URL que el usuario final: portal.office365.com.
Al crear la suscripción de Office 365, Microsoft envía un correo con el usuario y una password temporal que deberá cambiarse en el primer login.
Además de las aplicaciones a las que tiene acceso según su licencia, cuenta con un icono de administración, para
acceder al **Centro de Administración de Microsoft 365** .
La primera vez que se accede al portal de Office 365 como administrador, puede aparecer un mensaje como el de la figura de abajo. Se muestra cuando aún no
se han asignado licencias de productos a los usuarios de la organización.
La asignación de licencias a usuarios se realiza desde el Centro de administración de Microsoft 365.
**Centro Criptológico Nacional** 7
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**b)** **Cambiar el idioma a español.**
Se accede desde el icono de Configuración de la barra superior del portal.
Click en _Idioma y zona horaria_ .
Click en Cambiar idioma para mostrar y seleccionamos el idioma.
**c)** **Acceder al Centro de Administración de Microsoft 365.**
Se accede a través del icono Admin del portal de Office 365 o bien mediante la url: admin.microsoft.com.
Si es la primera que se accede al panel aparecerá el siguiente mensaje indicando el terminar la configuración de 365. Es este ejemplo tenemos la licencia **M365**
**Empresa Estándar.**
Pulsar el botón “Ir a la configuración guiada”:
**Centro Criptológico Nacional** 8
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
_1._ _Instalar Microsoft 365_ Una vez dentro de la configuración, dará la opción de instalar las aplicaciones
del paquete office. En el caso de querer instalarlas, simplemente hacer click en el botón de descargar.
En el caso de que querer omitir este paso, hacer click en “Continuar”.
_2._ _Configuración de un dominio personalizado_ Se recomienda la personalización con un dominio propio de la organización.
**Centro Criptológico Nacional** 9
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
_3._ _Agregar nuevos usuarios_ Para la asignación de licencias a los usuarios que se especifiquen en este paso.
_4._ _Fin del proceso de instalación._ Información más detallada de cómo añadir usuarios y licencias en el apartado
[3.1.1 Control de acceso] de la presente guía.
**Centro Criptológico Nacional** 10
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
### **2.2 USUARIO FINAL – PRIMEROS PASOS**
El usuario final podrá acceder al portal Office 365 a través de la url:
portal.office365.com. Tras introducir las credenciales se muestra un panel con todas las aplicaciones a las que tiene acceso.
En algunas ocasiones, si la licencia de usuario no ha sido asignada correctamente, podría aparecer el siguiente mensaje de aviso:
Desde el propio panel de Office 365 se permite instalar la versión de escritorio de las aplicaciones.
**Nota:** Para la configuración de seguridad de la versión de escritorio de las aplicaciones
Office remitirse a la Guía CCN-STIC más actualizada (CCN-STIC-585 en el momento de edición de la presente guía).
Una vez asignadas la licencia al usuario final, y tras logarse en el portal de Office 365, se mostrará una página de inicio con los iconos de todas las aplicaciones a las que
se tiene acceso.
**Centro Criptológico Nacional** 11
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
Es aconsejable establecer el idioma y la zona horaria.
Click en Idioma y región.
Es posible instalar las versiones de escritorio de las aplicaciones o acceder on-line, pulsando los iconos correspondientes.
**Centro Criptológico Nacional** 12
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
### **3. CONFIGURACIÓN DE OFFICE 365**
A continuación, se abordará la configuración de Office 365 centrándose en el cumplimiento de los requisitos del Esquema Nacional de Seguridad.
### **3.1 MARCO OPERACIONAL**
#### **3.1.1 CONTROL DE ACCESO**
El control de acceso comprende el conjunto de actividades preparatorias y ejecutivas tendentes a permitir o denegar a una entidad, usuario o proceso, el acceso a
un recurso del sistema para la realización de una acción concreta.
**3.1.1.1** **IDENTIFICACIÓN**
Office 365 usa Microsoft Entra ID, una identidad de usuario basada en la nube y un servicio de autenticación que se incluye con la suscripción a Office 365, para
administrar las identidades y la autenticación de Office 365. Para más información consultar [CCN-STIC-884A - Guía de configuración segura para Azure].
**MODELOS DE GESTIÓN DE IDENTIDADES**
En esta sección se abordarán los distintos modelos y mecanismos para la gestión de identidades en Office 365. Principalmente nos centraremos en dos: modelo identidad
sólo nube (que será tomado como referencia en esta guía) y modelo de identidad híbrida.

|Col1|Identidad solo de nube|Identidad híbrida|
|---|---|---|
|**Definición**|La cuenta de usuario solo<br />existe en el tenant de<br />Entra<br />ID<br />para<br />su<br />suscripción a Microsoft<br />365.|La cuenta de usuario existe en AD DS y<br />una copia también se encuentra en el<br />tenant de Entra ID para su suscripción a<br />Microsoft 365. La cuenta de usuario en<br />Entra ID también puede incluir una<br />versión hash de la contraseña de la<br />cuenta de usuario.|
|**Cómo autentica**<br />**Microsoft 365 las**<br />**credenciales de**<br />**usuario**|El tenant de Entra ID para<br />su suscripción a Microsoft<br />365<br />realiza<br />la<br />autenticación<br />con<br />la<br />cuenta de identidad de<br />nube.|El tenant de Entra ID para su suscripción<br />de Microsoft 365 administra el proceso<br />de autenticación o redirige al usuario a<br />otro proveedor de identidades.|
|**Ideal para**|Organizaciones que no<br />tienen ni necesitan un AD<br />DS local.|Organizaciones que usan AD DS u otro<br />proveedor de identidades.|

**Centro Criptológico Nacional** 13
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Modelo identidad sólo nube**
Una identidad de solo nube usa cuentas de usuario que solo existen en Entra ID. La identidad de nube suele usarse en organizaciones pequeñas que no tienen servidores
locales o que no usan AD DS para administrar identidades locales.
Estos son los componentes básicos de la identidad solo de la nube.
Los usuarios locales y remotos (en línea) usan sus cuentas de usuario y contraseñas de Entra ID para acceder a los servicios en la nube de Office 365. Entra ID autentica las
credenciales de usuario en función de sus cuentas de usuario y contraseñas almacenadas.
_Administración_ Como las cuentas de usuario se almacenan solo en Entra ID, se puede administrar
las identidades de nube con herramientas como el Centro de administración de Microsoft 365 y Windows PowerShell.
**Modelo identidad híbrido**
La identidad híbrida usa cuentas que se originan en un AD DS local y tienen una copia en el tenant de Entra ID de una suscripción a Microsoft 365. Sin embargo, la
mayoría de los cambios solo fluyen en un sentido. Los cambios que realice en las cuentas de usuario de AD DS se sincronizan con su copia en Entra ID. Pero los cambios
realizados en cuentas basadas en la nube en Entra ID, como nuevas cuentas de usuario, no se sincronizan con AD DS.
Microsoft Entra Connect proporciona la sincronización de cuentas en curso. Se ejecuta en un servidor local, comprueba los cambios en AD DS y reenvía dichos
cambios a Entra ID. Microsoft Entra Connect permite filtrar las cuentas que se van a
**Centro Criptológico Nacional** 14
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
sincronizar y si se debe sincronizar una versión hash de las contraseñas de usuario, conocidas como sincronización de hash de contraseña (PHS).
Al implementar la identidad híbrida, su AD DS local es el origen de autoridad para la información de la cuenta. Esto significa que las tareas de administración se realizan
principalmente en el entorno local, que luego se sincronizan con Entra ID.
Estos son los componentes de la identidad híbrida.
El tenant de Entra ID tiene una copia de las cuentas de AD DS. En esta configuración, los usuarios locales y remotos que tienen acceso a los servicios en la nube de Microsoft
365 se autentican con Entra ID.
**GESTIÓN DE IDENTIDADES EN EL MODELO SÓLO NUBE**
Con la identidad solo de nube, todos los usuarios, grupos y contactos se almacenan en el tenant de Microsoft Entra ID de la suscripción a Office 365.
Tanto la creación de usuarios como de grupos puede realizarse desde:
- Centro de administración de Microsoft 365
- Microsoft Graph PowerShell
_Centro de Administración de Microsoft 365_ Se accede a través del icono Admin del portal de Office 365 o bien mediante la url:
admin.microsoft.com.
**Centro Criptológico Nacional** 15
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Creación de usuarios**
a) Desde el menú [Usuarios\Usuarios activos] pulsar el icono “Agregar un usuario”, y rellenar el formulario.
**Nota:** más información sobre gestión de contraseñas en el apartado [3.1.1.5
Mecanismos de autenticación].
b) Se asigna la licencia y se asocian las aplicaciones a las que tendrá acceso el usuario.
**Centro Criptológico Nacional** 16
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
c) En el caso de que el usuario requiera un rol especial, seleccionar uno desde el listado. Si el usuario no necesita ningún rol, dejar marcada la opción Usuario ( _sin_
_acceso al centro de administración_ ).
d) Añadimos información del usuario, si es necesario.
**Centro Criptológico Nacional** 17
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
e) Una vez creado el usuario aparece el siguiente mensaje.
Para comprobar que el usuario se ha creado correctamente revisar la lista de “usuarios activos”.
**Operaciones básicas sobre usuarios**
Desde el menú [Usuarios\Usuarios activos] seleccionar el usuario y se pulsar sobre el icono “Más opciones”.
**Centro Criptológico Nacional** 18
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Administrar licencias**
Desde el menú [Usuario\Usuarios activos] se despliega la lista de usuarios con las licencias asignadas. Seleccionar el usuario adecuado y pulsar sobre el nombre. En el
panel de la derecha, pestaña “Licencias y Aplicaciones” configurar las opciones pertinentes.
**Asignar usuario a grupo**
Desde el menú [Usuarios\Usuarios activos] pulsando sobre el icono “Más opciones” del usuario.
**Centro Criptológico Nacional** 19
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Editar usuario**
a) Desde el menú [Usuarios\Usuarios activos] pulsando sobre el “nombre” del usuario.
b) Para asignar roles al usuario consultar el apartado [3.1.1.3 Segregación de funciones y tareas].
**Centro Criptológico Nacional** 20
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Eliminar usuario**
Desde el menú [Usuarios\Usuarios activos] pulsando sobre el icono “Más opciones” del usuario.
Nos saldrá la siguiente ventana. Click en Eliminar usuario.
Se deberá mover los archivos que quiera conservar dentro del período de retención establecido para los archivos de OneDrive. **De forma predeterminada, el**
**período de retención es de 30 días.**
**Centro Criptológico Nacional** 21
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Crear grupo**
En la sección **grupos** del Centro de administración de Microsoft 365, puede crear y administrar estos tipos de grupos:
- Los **grupos de Office 365** se usan para la colaboración entre usuarios, tanto
dentro como fuera de la compañía.
- Los **grupos de distribución** se usan para enviar notificaciones a un grupo de
personas.
- Los **grupos de seguridad** se usan para conceder acceso a los recursos de
SharePoint.
- Los **grupos de seguridad habilitados para correo** se usan para conceder
acceso a los recursos de SharePoint y enviar notificaciones por correo electrónico a dichos usuarios.
- Los **buzones compartidos** se usan cuando varias personas necesitan tener
acceso al mismo buzón, como la información de la empresa o la dirección de correo electrónico de soporte técnico.
Es importante activar la “Auditoría de buzones compartidos” para permitir la trazabilidad en estos buzones, como se describe en la guía [CCN-STIC-885C - Guía de
configuración segura para Exchange Online].
a) Agregar grupo.
Desde el menú [Teams y grupos], pulsar la opción Grupos y equipos activos, una vez dentro pulsar el icono “Agregar un grupo de Microsoft 365”.
b) Cumplimentar información del grupo.
**Centro Criptológico Nacional** 22
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
c) Desde este apartado se agrega el propietario d) Desde este apartado se agrega los miembros del grupo
e) Configuración del grupo
**Centro Criptológico Nacional** 23
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
1) Añadimos un nombre al grupo 2) Privacidad:
- Privado: Los grupos **privados** no están disponibles para que
cualquier usuario se una a estos, y solo los propietarios del grupo pueden agregar miembros. Solo los miembros pueden acceder al
contenido del grupo.
- Público: Todos los usuarios pueden unirse a un grupo **público** sin
necesidad de la aprobación de un propietario del grupo.
Cualquier usuario puede acceder al contenido del grupo.
**Nota:** Si se requiere un mayor control sobre el acceso a la información del
grupo por parte de los usuarios, entonces se recomienda el uso del valor Privado.
3) Para asignar roles al grupo
- La opción de Privacidad debe estar en **Privado** .
- La opción de **Agregar Microsoft Teams al grupo** debe esta
desactivada.
4) Agregar Microsoft Teams al grupo
- Activar esta opción si se requiere agregar un equipo de teams al
grupo.
f) Revisar y terminar de agregar el grupo
**Centro Criptológico Nacional** 24
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
g) Revisar y finalizar
**Gestionar miembros de un grupo**
a) Desde el menú [Grupos y equipos activos] pulsando sobre el nombre del grupo, se despliega el panel del grupo con distintas pestañas. Seleccionar la
pestaña _Pertenencia_ y luego dentro _Miembros_ .
b) Buscamos los usuarios a través del nombre o del correo electrónico y hacer click en agregar.
**Centro Criptológico Nacional** 25
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Eliminar grupo**
Desde el menú [Teams y grupos/ Grupos y equipos activos], seleccionar el grupo a eliminar y desde más opciones, click en Eliminar equipo.
Click en Eliminar equipo.
**Centro Criptológico Nacional** 26
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
_Powershell de Office 365_ Para la ejecución de los siguientes scripts se requiere el módulo de Microsoft Graph
PowerShell SDK para windows PowerShell.
**Crear una cuenta de usuario individual**
Ver Anexo A en el final del documento.
**Crear varias cuentas de usuario**
Ver Anexo B en el final del documento.
**3.1.1.2** **REQUISITOS DE ACCESO**
Los mecanismos de acceso a los recursos se detallan en las guías específicas de cada servicio: Sharepoint Online [CCN-STIC-885B - Guía de configuración segura para
Sharepoint Online], Exchange Online [CCN-STIC-885C - Guía de configuración segura para Exchange Online] y Teams [CCN-STIC 885D - Guía de configuración segura para
Microsoft Teams].
**3.1.1.3** **SEGREGACIÓN DE FUNCIONES Y TAREAS**
**Roles de administración**
La suscripción de O365 incluye un conjunto de roles de administrador que se pueden asignar a los usuarios de la organización. Cada rol de administrador se asigna a
funciones empresariales comunes y proporciona a los usuarios permisos para realizar tareas específicas en los centros de administración.
Como los administradores tienen acceso a los datos y archivos sensibles, Microsoft recomienda seguir estas directrices para mantener los datos de la organización más
seguros.

|Recomendación|¿Por qué es importante?|
|---|---|
|**Tener de 2 a 4**<br />**administradores globales**|Los administradores globales tienen acceso casi ilimitado<br />a la configuración de su organización y a la mayoría de<br />sus datos. Se recomienda limitar el número de<br />administradores globales tanto como sea posible. Un<br />Administración global puede bloquear accidentalmente<br />su cuenta y requerir un restablecimiento de contraseña.<br />Otra Administración global o una Administración de<br />autenticación con privilegios pueden restablecer la<br />contraseña de un Administración global. Por lo tanto, se<br />recomienda tener al menos una Administración global<br />más o una Administración de autenticación con<br />privilegios en caso de que un Administración global<br />bloquee su cuenta.|

**Centro Criptológico Nacional** 27
**CCN-STIC 885A** **Guía de configuración segura para Office 365**

|Asignar el rol menos<br />permisivo|Asignar el rol menos permisivo significa conceder a los<br />administradores solo el acceso que necesitan para<br />realizar el trabajo. Por ejemplo, si quiere que alguien<br />restablezca las contraseñas de los empleados, no debe<br />asignar el rol de administrador global ilimitado, debe<br />asignar un rol de administrador limitado, como<br />administrador de contraseñas o administrador del<br />departamento de soporte técnico.|
|---|---|
|**Requerir la autenticación**<br />**multifactor para**<br />**administradores**|Es una buena idea requerir MFA para todos los usuarios,<br />pero definitivamente se debe exigir a los administradores<br />usar la MFA para iniciar sesión. MFA hace que los<br />usuarios usen un segundo método de identificación para<br />comprobar su identidad. Los administradores pueden<br />tener acceso a gran parte de los datos de clientes y<br />empleados. Si necesita MFA, incluso si la contraseña del<br />administrador se pone en peligro, la contraseña no sirve<br />para nada sin el segundo método de identificación.<br />Al activar la MFA, la próxima vez que el usuario inicie<br />sesión, deberá proporcionar una dirección de correo<br />electrónico y un número de teléfono alternativos para<br />recuperar la cuenta.|

**Asignar roles de administrador a un usuario**
Desde el centro de administración, ir a los detalles del usuario y
administrar funciones para asignar un rol al usuario.
**Centro Criptológico Nacional** 28
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Centro Criptológico Nacional** 29
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Roles disponibles en el centro de administración de Microsoft 365**
El centro de administración Microsoft 365 permite administrar más de 30 roles de Entra ID. Sin embargo, estos roles son un subconjunto de las funciones disponibles en
portal de Entra ID.
Usualmente es suficiente con asignar los siguientes roles a la organización:

|Rol de administrador|¿A quién se le debe asignar este rol?|
|---|---|
|**Administrador de**<br />**facturación**|Asigne el rol de administrador de facturación a los usuarios<br />que hagan compras, administren suscripciones y solicitudes<br />de servicio y supervisen el estado del servicio.<br /> <br />Los administradores de facturación también pueden:<br />- Administrar todos los aspectos de la facturación<br />- Crear y administrar vales de soporte técnico en el portal de<br />Entra ID.|
|**Administrador de**<br />**Exchange**|Asigne el rol de administrador de Exchange a los usuarios que<br />necesiten ver y administrar los buzones de correo de sus<br />usuarios, los grupos de Microsoft 365 y Exchange Online.<br /> <br />Los administradores de Exchange también pueden:<br />- Recuperar elementos eliminados en un buzón de usuario<br />- Configurar los delegados "Enviar como" y "Enviar en nombre<br />de"|
|**Administrador de**<br />**Fabric**|Asigne el rol de administrador de Fabric a los usuarios que<br />necesiten hacer lo siguiente:<br />- Administración de todas las características de administrador<br />para Microsoft Fabric y Power BI<br />- Informe sobre el uso y el rendimiento<br />- Revisión y administración de auditorías|

**Centro Criptológico Nacional** 30
**CCN-STIC 885A** **Guía de configuración segura para Office 365**

|Administrador global|Asigne el rol de administrador global a los usuarios que<br />necesiten acceso global a la mayoría de las características de<br />administración y datos en los servicios en línea de Microsoft.<br />Dar acceso global a demasiados usuarios supone un riesgo<br />para la seguridad y se recomienda tener entre dos y cuatro<br />administradores globales.<br />Solo los administradores globales pueden:<br />- Restablecer las contraseñas de todos los usuarios<br />- Agregar y administrar dominios<br />- Desbloquear a otro administrador global<br />Nota: La persona que se registró en Microsoft servicios en<br />línea se convierte automáticamente en administrador global.|
|---|---|
|**Lector global**|Asigne el rol de lector global a los usuarios que necesiten ver<br />la configuración y las funciones de administración en los<br />centros de administración que el administrador global puede<br />ver. El administrador del lector global no puede editar<br />ninguna configuración.|
|**Administrador de**<br />**grupos**|Asigne el rol de administrador de grupos a los usuarios que<br />necesiten administrar la configuración de todos los grupos en<br />los centros de administración, incluido el Centro de<br />administración de Microsoft 365 y el Centro de administración<br />de Microsoft Entra.<br /> <br />Los administradores de grupos pueden:<br />- Crear, editar, eliminar y restaurar los grupos de Microsoft<br />365<br />- Crear y actualizar las directivas de creación, expiración y<br />nomenclatura de grupos<br />- Creación, edición, eliminación y restauración Microsoft Entra<br />grupos de seguridad|

**Centro Criptológico Nacional** 31
**CCN-STIC 885A** **Guía de configuración segura para Office 365**

|Administrador del<br />departamento de<br />soporte técnico|Asigne el rol de administrador del departamento de soporte<br />técnico a los usuarios que necesiten que hacer lo siguiente:<br />- Restablecer contraseñas<br />- Forzar a los usuarios a cerrar sesión<br />- Administrar solicitudes de servicio<br />- Supervisar el estado del servicio<br />Nota: el administrador del departamento de soporte técnico<br />solo puede ayudar a usuarios que no son administradores y a<br />usuarios que tienen asignados estos roles: Lector de<br />directorios, Invitador de usuarios invitados, Administrador del<br />departamento de soporte técnico, Lector del centro de<br />mensajes y Lector de informes.|
|---|---|
|**Administrador de**<br />**licencias**|Asigne el rol de administrador de licencias a los usuarios que<br />necesiten asignar y quitar licencias a usuarios y editar su<br />ubicación de uso.<br /> <br />Los administradores de licencias también pueden:<br />- Volver a procesar asignaciones de licencia para licencias<br />basadas en grupos<br />- Asignar licencias de producto a grupos de licencias basadas<br />en grupos|
|**Lector de privacidad**<br />**del centro de**<br />**mensajes**|Asigne el rol de lector de privacidad del Centro de mensajes a<br />los usuarios que necesiten leer mensajes y actualizaciones de<br />privacidad y seguridad en el Centro de mensajes de Microsoft<br />365. Los lectores de privacidad del centro de mensajes<br />pueden<br />recibir<br />notificaciones<br />por<br />correo<br />electrónico<br />relacionadas con la privacidad de los datos, en función de sus<br />preferencias, y pueden cancelar la suscripción mediante las<br />preferencias del Centro de mensajes. Solo los administradores<br />globales y los lectores de privacidad del Centro de mensajes<br />pueden leer los mensajes de privacidad de datos. Este rol no<br />tiene permiso para ver, crear o administrar solicitudes de<br />servicio.<br /> <br />Los lectores de privacidad del centro de mensajes también<br />pueden:<br />- Supervisar todas las notificaciones en el Centro de mensajes,<br />incluidos los mensajes de privacidad de datos<br />- Ver grupos, dominios y suscripciones|

**Centro Criptológico Nacional** 32
**CCN-STIC 885A** **Guía de configuración segura para Office 365**

|Lector del Centro de<br />mensajes|Asigne el rol de Lector del Centro de mensajes a los usuarios<br />que necesiten hacer lo siguiente:<br />- Supervisar las notificaciones del Centro de mensajes<br />- Obtener resúmenes semanales por correo electrónico de las<br />publicaciones y actualizaciones del Centro de mensajes<br />- Compartir publicaciones del Centro de mensajes<br />- Tener acceso de solo lectura a Microsoft Entra servicios,<br />como usuarios y grupos|
|---|---|
|**Administrador de**<br />**migración**|Asigne el rol Administrador de migración de Microsoft 365 a<br />los usuarios que necesiten realizar las siguientes tareas:<br />- Use el Administrador de migración en el Centro de<br />administración de Microsoft 365 para administrar la migración<br />de contenido a Microsoft 365, incluidos los sitios de Teams,<br />OneDrive para la Empresa y SharePoint, desde diversos<br />orígenes, como Google Drive, Dropbox y Box.<br />- Seleccione orígenes de migración, cree inventarios de<br />migración (como listas de usuarios de Google Drive),<br />programe y ejecute migraciones y descargue informes.<br />- Cree nuevos sitios de SharePoint si los sitios de destino aún<br />no existen, cree listas de SharePoint en los sitios de<br />administración de SharePoint y cree y actualice elementos en<br />listas de SharePoint.<br />- Administrar la configuración del proyecto de migración y el<br />ciclo de vida de la migración para las tareas, así como<br />administrar asignaciones de permisos de origen a destino.<br />**Nota**: Con este rol, solo puedes migrar desde Google Drive,<br />Box, Dropbox y Egnyte. Este rol no permite migrar desde<br />orígenes de recursos compartidos de archivos desde el Centro<br />de administración de SharePoint. Use un administrador de<br />SharePoint o un administrador global para migrar desde<br />orígenes de recursos compartidos de archivos.|
|**Administrador de**<br />**aplicaciones de Office**|Asigne el rol de administrador de aplicaciones de Office a los<br />usuarios que necesiten hacer lo siguiente:<br />- Use el servicio Cloud Policy para Microsoft 365 para crear y<br />administrar directivas basadas en la nube.<br />- Crear y administrar solicitudes de servicio<br />- Administrar el contenido novedades que los usuarios ven en<br />sus aplicaciones de Microsoft 365<br />- Supervisar el estado del servicio|
|**Escritor de mensajes**<br />**de la organización**|Asigne el rol Escritor de mensajes de la organización a los<br />usuarios que necesiten escribir, publicar, administrar y revisar<br />los mensajes de la organización para los usuarios finales a<br />través de superficies de productos de Microsoft.|

**Centro Criptológico Nacional** 33
**CCN-STIC 885A** **Guía de configuración segura para Office 365**

|Aprobador de<br />mensajes de la<br />organización|Asigne el rol Aprobador de mensajes organizativos a los<br />usuarios que necesiten revisar, aprobar o rechazar nuevos<br />mensajes de la organización para su entrega en el Centro de<br />administración de Microsoft 365 antes de que se envíen a los<br />usuarios a través de superficies de productos de Microsoft.|
|---|---|
|**Administrador de**<br />**contraseñas**|Asigne el rol de administrador de contraseñas a un usuario<br />que necesite restablecer las contraseñas de los no<br />administradores y los administradores de contraseñas.|
|**Administrador de**<br />**Power Platform**|Asigne el rol de administrador de Power Platform a los<br />usuarios que necesiten hacer lo siguiente:<br />- Administrar todas las características de administración de<br />Power Apps, Power Automate, Power BI, Microsoft Fabric y<br />Prevención de pérdida de datos de Microsoft Purview<br />- Crear y administrar solicitudes de servicio<br />- Supervisar el estado del servicio|
|**Lector de informes**|Asigne el rol de lector de informes a los usuarios que<br />necesiten hacer lo siguiente:<br />- Ver datos de uso e informes de actividad en el Centro de<br />administración de Microsoft 365<br />- Obtener acceso al paquete de contenido de adopción de<br />Power BI<br />- Obtener acceso a los informes de inicio de sesión y la<br />actividad en Microsoft Entra ID<br />- Ver datos devueltos por la API de informes de Microsoft<br />Graph|
|**Administrador de**<br />**búsqueda**|Asigne el rol de administrador Búsqueda a los usuarios que<br />necesitan crear y administrar el contenido de los resultados<br />de búsqueda y definir la configuración de consulta para<br />mejorar los resultados de búsqueda dentro de la organización.<br />El administrador de Búsqueda administra la configuración de<br />búsqueda de Microsoft y puede realizar todas las tareas de<br />administración de contenido que puede realizar un editor de<br />Búsqueda.|
|**Administrador de**<br />**soporte técnico del**<br />**servicio**|Asigne el rol de administrador de soporte técnico de servicio<br />como un rol adicional a los administradores o usuarios que<br />necesiten hacer, además de su rol de administrador habitual,<br />lo siguiente:<br />- Abrir y administrar solicitudes de servicio<br />- Ver y compartir publicaciones del centro de mensajes<br />- Supervisar el estado del servicio|

**Centro Criptológico Nacional** 34
**CCN-STIC 885A** **Guía de configuración segura para Office 365**

|Administrador de<br />SharePoint|Asigne el rol de administrador de SharePoint a los usuarios<br />que necesiten acceder y administrar el centro de<br />administración de SharePoint Online.<br />Los administradores de SharePoint también pueden:<br />- Crear y eliminar sitios<br />- Administrar colecciones de sitios y la configuración global de<br />SharePoint|
|---|---|
|**Administrador de**<br />**Teams**|Asigne el rol de administrador de Teams a los usuarios que<br />necesiten acceder y administrar el Centro de administración<br />de Teams.<br /> <br />El administrador de Teams también puede:<br />- Administrar reuniones<br />- Administrar puentes de conferencia<br />- Administrar la configuración de toda la organización, incluida<br />la federación, la actualización de equipos y la configuración de<br />cliente de equipos|
|**Administrador de**<br />**usuarios**|Asigne el rol de administrador de usuarios a los usuarios que<br />necesiten hacer lo siguiente para todos los usuarios:<br />- Agregar usuarios y grupos<br />- Asignar licencias<br />- Administrar las propiedades de la mayoría de los usuarios<br />- Crear y administrar vistas de usuarios<br />- Actualizar las directivas de expiración de contraseña<br />- Administrar solicitudes de servicio<br />- Supervisar el estado del servicio<br /> <br />El administrador de usuario también puede realizar las<br />siguientes acciones para los usuarios que no sean<br />administradores y para los usuarios que tengan asignados los<br />siguientes roles: Lector de directorios, Invitador de usuarios<br />invitados, Administrador del departamento de soporte<br />técnico, Lector del centro de mensajes y Lector de informes:<br />- Administrar nombres de usuario<br />- Eliminar y restaurar usuarios<br />- Restablecer contraseñas<br />- Forzar a los usuarios a cerrar sesión<br />- Actualizar claves de dispositivo (FIDO)|
|**Administrador de**<br />**éxito de la**<br />**experiencia del**<br />**usuario**|Asigne el rol Administrador de éxito de experiencia de usuario<br />a los usuarios que necesitan acceder a Experience Insights, la<br />puntuación de adopción y el Centro de mensajes en el Centro<br />de administración de Microsoft 365. Este rol incluye los<br />permisos del rol Lector de informes de resumen de uso.|

**Centro Criptológico Nacional** 35
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
El portal de Entra ID tiene más roles que los disponibles en el Centro de administración de Microsoft 365.
Desde Entra ID es posible crear roles personalizados. Se necesita Entra ID Premium P1 o P2.
**3.1.1.4** **PROCESO DE GESTIÓN DE DERECHOS DE ACCESO**
Más información en las guías específicas de cada servicio: Sharepoint Online [CCNSTIC-885B - Guía de configuración segura para Sharepoint Online], Exchange Online [CCN-STIC-885C - Guía de configuración segura para Exchange Online] y Teams [CCNSTIC 885D - Guía de configuración segura para Microsoft Teams].
**3.1.1.5** **MECANISMO DE AUTENTICACIÓN (USUARIOS EXTERNOS)**
Desde el Centro de administración de Microsoft 365 en el menú [Configuración\ \configuración de la organización\Seguridad y Privacidad] se pueden establecer
**Directivas de expiración de contraseñas** para todos los usuarios de la organización.
Se recomienda activar la opción Establecer que las contraseñas nunca expiren (recomendado).
Desde Office 365 sólo se pueden modificar estos parámetros, cuyos valores por defecto son:
Días antes de que las contraseñas expiren: 90
**Nota** : Las notificaciones de expiración de contraseñas ya no se admiten en las
aplicaciones Centro de administración de Microsoft 365 y Microsoft 365.
Para una gestión más avanzada hay que recurrir a Entra ID. Consultar guía [CCNSTIC-884A - Guía de configuración segura para Azure].
**Powershell**
Desde PS se pueden consultar y/o modificar un parámetro relacionado con la contraseña del usuario:
- PasswordNeverExpires: si la contraseña nunca expira.
_**Listado de usuarios con información de caducidad**_
**Centro Criptológico Nacional** 36
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
_**Modificar parámetros de contraseñas**_ Se recomienda aplicar el siguiente comando:
```
Update-MgUser -UserId &lt;user ID> -PasswordPolicies DisablePasswordExpiration
```
**Nota:** Se recomienda configurar el parámetro PasswordNeverExpires en los entornos
de Producción de la empresa.
Cómo ya se ha comentado, para una configuración avanzada de la política de contraseña hay que recurrir a la guía [CCN-STIC-884A - Guía de configuración segura
para Azure].
A continuación, se desglosan las características de las cuentas de usuario de Entra ID, y los comandos para modificarlas:

|Propiedad|Requerimiento de UPN (User Principal Name)|
|---|---|
|**Caracteres permitidos**|Caracteres en mayúsculas (A - Z)<br />Caracteres en minúsculas (a - z)<br />Números (0 - 9)<br />Símbolos:<br />- @ # $ % ^ & * - _ ! + = [ ] &#123; &#125; | \ : ', . ? / ` ~ " ( ) ; &lt;><br />- espacio en blanco|
|**Caracteres no**<br />**permitidos en las**<br />**contraseñas**|Caracteres unicode<br />Espacios|
|**Longitud de la**<br />**contraseña**|Las contraseñas requieren lo siguiente<br />- Una longitud mínima de ocho caracteres<br />- 256 caracteres como máximo.|
|**Complejidad de la**<br />**contraseña**|Las contraseñas requieren tres de las cuatro categorías<br />siguientes:<br />- Caracteres en mayúsculas<br />- Caracteres en minúsculas<br />- Números<br />- Símbolos<br />**Nota**: La comprobación de complejidad de la contraseña no<br />es necesaria para los tenants de Education.|
|**Contraseña no usada**<br />**recientemente**|Cuando un usuario cambie su contraseña, la nueva<br />contraseña no debería ser la misma que la contraseña actual.|
|**La protección de**<br />**contraseñas de**<br />**Microsoft Entra no ha**<br />**prohibido la**<br />**contraseña**|La contraseña no puede estar en la lista global de<br />contraseñas prohibidas de la protección de contraseñas de<br />Microsoft Entra ni en la lista personalizable de contraseñas<br />prohibidas específicas de la organización.|

**Centro Criptológico Nacional** 37
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Activar la autenticación multifactor (MFA)**

|Elemento|Al estar habilitado|Al estar<br />deshabilitado|Método de<br />autenticación<br />secundario|
|---|---|---|---|
|**Security defaults**|No se pueden usar<br />directivas de acceso<br />condicional|Se pueden usar<br />directivas de acceso<br />condicional|Aplicación Microsoft<br />Authenticator|
|**Directivas de acceso**<br />**condicional**|Si hay alguno<br />habilitado, no puede<br />habilitar los valores<br />predeterminados de<br />seguridad.|Si se deshabilitan<br />todos, puede<br />habilitar los valores<br />predeterminados de<br />seguridad|Especificado por el<br />usuario durante el<br />registro de MFA|
|**MFA heredada por**<br />**usuario (no**<br />**recomendado)**|Invalida los valores<br />predeterminados de<br />seguridad y las<br />directivas de acceso<br />condicional que<br />requieren MFA en<br />cada inicio de sesión|Invalidado por<br />valores<br />predeterminados de<br />seguridad y<br />directivas de acceso<br />condicional|Especificado por el<br />usuario durante el<br />registro de MFA|

Como se describe en el apartado [3.1.1.3 Segregación de funciones y tareas] es importante habilitar MFA al menos para los usuarios con el rol de administración. Para
ello:
Security defaults Para activar el MFA a través de este método:
a) Iniciar sesión en el [Centro de administración Microsoft Entra](https://entra.microsoft.com/) como administrador de seguridad como mínimo.
b) Navegar a **Información general** - **Propiedades** .
c) Seleccionar **Administrar los valores predeterminados de seguridad** .
d) Cambiar los valores predeterminados de Seguridad a **Habilitado** .
e) Click en guardar.
**Centro Criptológico Nacional** 38
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
MFA heredada por usuario (no recomendado)
a) Acceder al menú [Usuarios\Usuarios Activos].
b) Pulsar el icono “Autenticación multifactor” de la barra superior.
c) Se accede a un nuevo panel de administración:
d) Marcar un usuario con el check correspondiente y habilitar o deshabilitar el MFA en el panel derecho.
Directivas de acceso condicional Las directivas de acceso condicional son un conjunto de reglas que especifican las
condiciones en las que se evalúan y permiten los inicios de sesión. Por ejemplo, puede crear una directiva de acceso condicional que indique lo siguiente:
- Si el nombre de la cuenta de usuario es miembro de un grupo de usuarios a los
que se han asignado los roles de administrador de Exchange, de usuarios, de contraseñas, de seguridad, de SharePoint o global, requerir MFA antes de
permitir el acceso.
Esta directiva le permite exigir la MFA en función de la pertenencia a grupos, en lugar de intentar configurar cuentas de usuario individuales para la MFA cuando se
asignan o se quitan estos roles de administrador.
**Centro Criptológico Nacional** 39
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
También puede usar directivas de acceso condicional para funcionalidades más avanzadas, como requerir MFA para aplicaciones específicas o que el inicio de sesión
se realice desde un dispositivo compatible, como el equipo portátil que ejecuta Windows 10.
Para más información consultar [CCN-STIC-884A - Guía de configuración segura para Azure]
_Powershell de Office 365_
**Planificación de los métodos de autenticación**
Los administradores pueden elegir los métodos de autenticación que quieren que estén disponibles para los usuarios. Es importante habilitar más de un método de
autenticación para que los usuarios tengan disponible un método alternativo en caso de que su método principal no esté disponible. Los métodos siguientes están
disponibles para que los administradores los habiliten:
a) **FIDO2 security key** : El usuario conecta la clave de seguridad FIDO2 en su equipo, Windows detecta la llave de seguridad FIDO2, entonces el usuario
realiza su gesto para desbloquear la clave privada almacenada en el enclave seguro de la llave de seguridad FIDO2.
Para más información: [Inicio de sesión sin contraseña de Microsoft Entra -](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-passwordless#passkeys-fido2)
[Microsoft Entra ID | Microsoft Learn](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-passwordless#passkeys-fido2)
b) **Notificación a través de aplicación móvil** : Se envía una notificación push a la aplicación Microsoft Authenticator del dispositivo móvil. El usuario ve la
notificación y selecciona Aprobar para completar la comprobación. Las notificaciones push a través de una aplicación móvil proporcionan la opción
menos intrusiva para los usuarios.
Para más información: [Método de autenticación de Microsoft Authenticator -](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-authenticator-app)
[Microsoft Entra ID | Microsoft Learn](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-authenticator-app)
c) **Código de verificación desde aplicación móvil** : Una aplicación móvil como la de Microsoft Authenticator genera un nuevo código de verificación de OATH cada
30 segundos. El usuario escribe el código de verificación en la interfaz de inicio
de sesión. La opción de aplicación móvil puede utilizarse independientemente de si el teléfono tiene una señal de telefonía móvil o datos.
Para más información: [Método de autenticación de Microsoft Authenticator -](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-authenticator-app)
[Microsoft Entra ID | Microsoft Learn](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-authenticator-app)
d) **SMS** : Se envía al usuario un mensaje de texto que contiene un código de verificación; después, se le pide al usuario que escriba el código de verificación
en la interfaz de inicio de sesión.
[Para más información: Métodos de autenticación de teléfono - Microsoft Entra](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-phone-options#mobile-phone-verification)
[ID | Microsoft Learn](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-phone-options#mobile-phone-verification)
**Centro Criptológico Nacional** 40
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
e) **Pase de acceso temporal (TAP):** El pase de acceso temporal (TAP) es un código de acceso de tiempo limitado que puede configurarse para usarse una o varias
veces. Los usuarios pueden iniciar sesión con un TAP para incorporar otros métodos de autenticación sin contraseña, como Microsoft Authenticator, FIDO2
y Windows Hello para empresas.
Para más información: [Configuración de un pase de acceso temporal en Id. de](https://learn.microsoft.com/es-es/entra/identity/authentication/howto-authentication-temporary-access-pass)
[Microsoft Entra para registrar métodos de autenticación sin contraseña -](https://learn.microsoft.com/es-es/entra/identity/authentication/howto-authentication-temporary-access-pass)
[Microsoft Entra ID | Microsoft Learn](https://learn.microsoft.com/es-es/entra/identity/authentication/howto-authentication-temporary-access-pass)
f) **Tokens de hardware OATH (versión preliminar):** Microsoft Entra ID admite el uso de tokens OATH-TOTP SHA-1 que actualizan los códigos cada 30 o 60
segundos. Los clientes pueden adquirir estos tokens a través de proveedores de terceros. Los tokens OATH de hardware están disponibles para usuarios con una
licencia Microsoft Entra ID P1 o P2.
Los tokens de hardware TOTP de OATH suelen incluir una clave secreta, o valor de inicialización, programada previamente en el token. Estas claves deben
introducirse en Microsoft Entra ID tal como se describe en los pasos siguientes.
Las claves secretas están limitadas a 128 caracteres, que no son compatibles con algunos tokens. La clave secreta solo puede contener los caracteres a-z o A-Z y
los dígitos 2-7, y debe estar codificada en base 32.
Para más información: [Método de autenticación de token OATH - Microsoft](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-oath-tokens#oath-hardware-tokens-preview)
[Entra ID | Microsoft Learn](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-oath-tokens#oath-hardware-tokens-preview)
**Nota:** La versión preliminar solo se admite en nubes globales de Entra ID y Entra ID
Government.
g) **Tokens de software OATH** : Los tokens de software OATH suelen ser aplicaciones, como la aplicación Microsoft Authenticator y otras aplicaciones de
autenticador. Microsoft Entra ID genera la clave secreta o valor de inicialización, que se introduce en la aplicación y se usa para generar cada OTP.
Para más información: [Método de autenticación de token OATH - Microsoft](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-oath-tokens#oath-software-tokens)
[Entra ID | Microsoft Learn](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-oath-tokens#oath-software-tokens)
h) **Llamada al teléfono** : Se realiza una llamada de voz automática al usuario. El usuario responde a la llamada y pulsa # en el teclado del teléfono para aprobar
su autenticación. La llamada a teléfono es un método alternativo excelente para los códigos de verificación o notificación de una aplicación móvil.
[Para más información: Métodos de autenticación de teléfono - Microsoft Entra](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-phone-options)
[ID | Microsoft Learn](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-authentication-phone-options)
i) **Email OTP:** La característica de código de acceso de un solo uso por correo electrónico es una manera de autenticar a los usuarios de colaboración B2B
cuando no se pueden autenticar a través de otros medios, como Microsoft Entra ID, la cuenta Microsoft (MSA) o los proveedores de identidades sociales. Cuando
un usuario invitado B2B intenta canjear la invitación o iniciar sesión en los
**Centro Criptológico Nacional** 41
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
recursos compartidos, puede solicitar un código de acceso temporal, que se envía a su dirección de correo electrónico. A continuación, escribe el código de
acceso para continuar con el inicio de sesión.
Para los usuarios internos del tenant, este método solamente se puede utilizar para la recuperación de la contraseña.
Para más información [Autenticación de código de acceso de un solo uso para](https://learn.microsoft.com/es-es/entra/external-id/one-time-passcode)
[usuarios invitados de B2B - Microsoft Entra External ID | Microsoft Learn](https://learn.microsoft.com/es-es/entra/external-id/one-time-passcode)
j) **Autenticación basada en certificados** : La autenticación basada en certificados (CBA) de Microsoft Entra habilita a los clientes para permitir o requerir que los
usuarios se autentiquen directamente con certificados X.509 en Microsoft Entra ID para aplicaciones e inicio de sesión en el explorador. Esta característica
permite a los clientes adoptar una autenticación resistente a la suplantación de identidad (phishing) y autenticarse con un certificado X.509 en su
infraestructura de clave pública (PKI).
**Para más información** [Introducción a la autenticación basada en certificados de](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-certificate-based-authentication)
[Microsoft Entra - Microsoft Entra ID | Microsoft Learn](https://learn.microsoft.com/es-es/entra/identity/authentication/concept-certificate-based-authentication)
Más información de cómo configurar los distintos métodos de autenticación en la guía [CCN-STIC-884A - Guía de configuración segura para Azure.]
**3.1.1.6** **MECANISMO DE AUTENTICACIÓN (USUARIOS DE LA ORGANIZACIÓN)**
Ver el apartado **3.1.1.5 MECANISMO DE AUTENTICACIÓN (USUARIOS EXTERNOS)**
#### **3.1.2 EXPLOTACIÓN**
Office 365, al ser un software ofrecido como servicio (SaaS), **siempre estará**
**actualizado** . Es decir, el servicio es mantenido permanentemente por **Microsoft**,
encargándose de las actualizaciones y parches, así como de establecer los mecanismos de detección y protección ante amenazas, cumpliendo con los requisitos Esquema
Nacional de Seguridad en su categoría ALTA.
En esta sección se explicará el funcionamiento y las características del Centro de Seguridad al que se accede desde el portal de Administración.
**3.1.2.1** **PROTECCIÓN FRENTE A CÓDIGO DAÑINO**
Si la organización dispone de las licencias correspondientes podrá ver el informe de “Estado de protección contra amenazas”. El informe de estado de protección contra
amenazas proporciona información sobre las amenazas detectadas antes de la entrega de correo electrónico, que abarca tecnologías de detección relevantes, tipos de
directivas y acciones de entrega.
**Centro Criptológico Nacional** 42
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
a) Desde el Centro de Seguridad de Office 365 menú [Informes\Informes de colaboración y correo electrónico].
b) Click en el botón [Ver detalle] de la tarjeta [Estado de protección contra amenazas]:
**Centro Criptológico Nacional** 43
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
Desde este informe se puede ver:
- Ver datos por Información general
- Ver datos por correos electrónicos de suplantación de identidad (phishing)
- Ver datos por correo electrónico de Malware
- Ver datos por correo electrónico de Correo no deseado
- Ver datos por contenido de software malintencionado
- Ver datos por invalidación del sistema
[Para más sobre este informe Ver informes de Defender para Office 365 - Microsoft](https://learn.microsoft.com/es-es/defender-office-365/reports-defender-for-office-365?view=o365-worldwide#threat-protection-status-report)
[Defender for Office 365 | Microsoft Learn](https://learn.microsoft.com/es-es/defender-office-365/reports-defender-for-office-365?view=o365-worldwide#threat-protection-status-report)
Más información en la guía [CCN-STIC-885C - Guía de configuración segura para Exchange Online].
**3.1.2.2** **GESTIÓN DE INCIDENTES**
Otros informes relevantes relacionados con la gestión de incidentes y accesibles desde el Centro de Seguridad son:
- Panel de alertas. [Inicio] Widget del panel principal
[https://security.microsoft.com/homepage](https://security.microsoft.com/homepage)
**Centro Criptológico Nacional** 44
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
- Panel de informes. Menú [Informes].
[https://security.microsoft.com/securityreports](https://security.microsoft.com/securityreports)
- Informes para su descarga. Menú [Informes\Informes para su descarga].
https://security.microsoft.com/ReportsForDownload
**Centro Criptológico Nacional** 45
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
- Panel de Flujo de correo. Menú [Flujo de correo\Panel].
https://security.microsoft.com/emailandcollabreport
**3.1.2.3** **REGISTRO DE LA ACTIVIDAD**
En lo relativo al registro de la actividad de usuarios y administradores se requiere la activación de la **Auditoría** de Office 365.
Cuando se activa la búsqueda de registros de auditoría en el Centro de Seguridad, la actividad de usuario y administrador de la organización se registra en el registro de
auditoría y se conserva durante 180 días.
**Activar/Desactivar registro de auditoría**
Se debe tener asignado el **rol de Audit Logs or View-Only Audit Logs** para activar o desactivar la búsqueda de registros de auditoría en su organización de Office 365. De
forma predeterminada, este rol se asigna a los grupos de roles administración de cumplimiento y administración de la organización en la página permisos del centro de
administración de Exchange. Los administradores globales de Office 365 son miembros del grupo de funciones de administración de la organización en Exchange Online.
a) Desde el Centro de Seguridad de Office 365 menú [Auditar], pulsar el botón “Grabar la actividad de usuarios y administradores”.
**Centro Criptológico Nacional** 46
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
b) Nos saldrá un pop-up solicitando confirmación, Pulsar “Sí”.
**Nota:** Pueden pasar varias horas desde que se activa el registro de auditoría
hasta que estén accesibles los datos en la búsqueda.
_Powershell de Office 365_ a) Conexión a Exchange Online mediante PowerShell.
b) Ejecutar el siguiente comando de PowerShell para activar/desactivar la búsqueda de registros de auditoría en Office 365:
1. Activar auditoría:
```
Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true
```
2. Desactivar auditoría:
```
Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $false
```
**Consultar registro de auditoría**
Permite buscar en el registro de auditoría lo que hacen los usuarios y administradores de la organización: actividades relacionadas con el correo electrónico,
grupos, documentos, permisos, servicios de directorio y mucho más.
**Nota:** Para realizar búsquedas en el registro de auditoría deben pasar al menos 24 h.
En el desplegable de Actividades se muestran todas las búsquedas posibles relacionadas con el registro de auditoría y clasificadas por temas. Ejemplo de consulta
relacionada con la descarga de ficheros:
**Centro Criptológico Nacional** 47
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Protección de los registros de actividad**
A través del uso de roles de usuarios se puede securizar quién puede consultar la información del registro de actividad. Los roles definidos para tal fin son:
- Administradores globales.
- Administradores de Exchange.
- Administradores de SharePoint
- Administradores de Teams.
- Lector de informes.
**API de Actividad de administración de Office 365**
A parte del Centro de Seguridad Office 365, existe una API de Actividad de administración de Office 365 para recuperar información sobre acciones y eventos de
usuario, administrador, sistema y directivas de los registros de actividad de Office 365 y Entra ID.
La API de Actividad de administración de Office 365 es un servicio web REST que se puede usar para desarrollar soluciones mediante cualquier lenguaje y entorno de
hospedaje que admita HTTPS y certificados X.509. La API se basa en Microsoft Entra ID y el protocolo OAuth2 para la autenticación y autorización. Para acceder a la API desde
la aplicación, primero debe registrarla en Microsoft Entra ID y configurarla con los permisos adecuados. Esto permitirá que la aplicación solicite los tokens de acceso
OAuth2 que necesita para llamar a la API. Para obtener más información, vea Get started with Office 365 Management APIs (Introducción a las API de administración de
Office 365).
Para obtener información sobre los datos que devuelve la API de Actividad de [administración de Office 365, vea: Esquema de la API de Actividad de administración](https://learn.microsoft.com/es-es/office/office-365-management-api/office-365-management-activity-api-schema)
[de Office 365 | Microsoft Learn](https://learn.microsoft.com/es-es/office/office-365-management-api/office-365-management-activity-api-schema)
**Informes de actividades en el centro de administración de Microsoft 365**
Otra manera de obtener información de cómo los usuarios de la organización usan los servicios de Office 365 es a través del Centro de administración de Microsoft 365,
menú [Informes/Uso]. Por ejemplo, se puede identificar quién está usando mucho un servicio, quién alcanza las cuotas o quién es posible que no necesite una licencia de
Office 365 en absoluto.
**Centro Criptológico Nacional** 48
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
Los informes pueden obtenerse para los últimos 7, 30, 90 o 180 días. Pulsando sobre cada widget del informe se profundiza en la información suministrada, bajando a
un nivel de más detalle.
**Nota:** los datos no estarán disponibles para todos los períodos de informes al instante
(usualmente a las 48 horas).
#### **3.1.3 MONITORIZACIÓN DEL SISTEMA**
Es posible definir **alertas** en Office 365 a través del Centro de Seguridad de Office 365.
Se pueden usar las alertas de actividad para **enviar notificaciones de correo**
**electrónico** a responsables del sistema cuando los usuarios realizan actividades
específicas en Office 365. Las alertas de actividad son similares a la búsqueda de eventos en el registro de auditoría de Office 365, excepto que se enviará un mensaje
de correo electrónico cuando se produzca un evento en el que se haya creado una alerta.
**Cómo funcionan las directivas de alerta**
A continuación, se presenta una introducción rápida sobre cómo funcionan las directivas de alertas y las alertas que se desencadenan cuando la actividad de usuario
- de administrador cumpla las condiciones de una directiva de alerta.
**Centro Criptológico Nacional** 49
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
- Un administrador de la organización crea, configura y activa una directiva de
alertas mediante la página **Directivas de alerta** del portal de purview o del portal de Microsoft Defender. También se puede crear directivas de alerta
mediante el cmdlet _New-ProtectionAlert_ en PowerShell de seguridad & Purview.
- Un usuario realiza una actividad que coincide con las condiciones de una
directiva de alerta. En el caso de ataques de malware, los mensajes de correo electrónico infectados enviados a los usuarios de su organización
desencadenan una alerta.
- Microsoft 365 genera una alerta que se muestra en la página Alertas en el
Portal de Purview o en el portal de Defender. Además, si las notificaciones por correo electrónico están habilitadas para la directiva de alertas,
Microsoft envía una notificación a una lista de destinatarios. Las alertas que un administrador u otros usuarios pueden ver que en la página Alertas están
determinadas por los roles asignados al usuario.
- Un administrador administra las alertas en el Portal de Purview. La
administración de alertas consiste en asignar un estado de alerta para ayudar a realizar un seguimiento y administrar cualquier investigación.
**Ver/editar directivas de alerta de sistema**
Con las directivas de alerta es posible realizar el seguimiento de las actividades de administradores y usuarios, amenazas de malware o incidentes de pérdida de datos en
la organización. Después de elegir la actividad sobre la que se requiere el aviso, se puede afinar la directiva agregando condiciones, decidiendo cuándo activar la alerta y
quién debería recibir las notificaciones.
**Centro Criptológico Nacional** 50
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
a) Acceder al menú [Reglas y directivas\Directivas de alerta] desde el Centro de Seguridad de Office 365.
b) Marcar las alertas sobre las cuales se quiere realizar el seguimiento de la lista de alertas predefinidas. Las alertas predefinidas se pueden activar o desactivar y
cambiar parte de su configuración.
Más información de las alertas predeterminadas en la documentación de [Microsoft. Directivas de alertas de Microsoft 365 | Microsoft Learn](https://learn.microsoft.com/es-es/purview/alert-policies)
c) Pulsar sobre una directiva concreta para acceder a sus propiedades.
Por ejemplo, la directiva “Suspicious email sending patterns detected” la cual se activa cuando se detecta que un usuario ha enviado un correo o correos con
texto con patrones sospechosos.
**Centro Criptológico Nacional** 51
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Crear directivas de alerta personalizadas**
Para crear una **directiva de alerta personalizada** pulsar el botón “Nueva directiva de alertas”, en el menú [Reglas y directivas\Directivas de alertas]. Como ejemplo se
va a crear una directiva para el borrado sospechoso de ficheros word en una ubicación concreta (sitio de Sharepoint CCN-SPO-SITIO1).
a) Asignar un nombre.
**Centro Criptológico Nacional** 52
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
b) Crear configuración de alerta.
_¿Sobre qué se quiere enviar alertas?_ Seleccionar una **actividad** :
Agregar condiciones:
Para la mayoría de las actividades, se puede definir condiciones adicionales que deben cumplirse para desencadenar una alerta. Las condiciones comunes
incluyen referencias a direcciones IP (por lo que se desencadena una alerta cuando el usuario realiza la actividad en un equipo con una dirección IP
específica o dentro de un intervalo de direcciones IP), usuarios concretos, nombres de archivos, urls de sitios o extensiones de archivos.
**Centro Criptológico Nacional** 53
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
En el ejemplo:
_¿Cómo quiere que se active la alerta?_ Puede configurar una configuración que defina la frecuencia con la que se
puede producir una actividad antes de que se desencadene una alerta.
Puede configurar una directiva para generar una alerta cada vez que una actividad coincide con las condiciones de la directiva, cuando se supera un
umbral determinado.
Puede configurar la directiva para generar una alerta cuando la aparición de la actividad que la alerta está realizando se vuelve inusual para su organización. Si
selecciona la configuración en función de una actividad inusual, Microsoft establece un valor de línea base que define la frecuencia normal de la actividad
seleccionada. El establecimiento de esta línea base tarda hasta siete días, durante los cuales no se generarán alertas. Una vez establecida la línea base, se
desencadena una alerta cuando la frecuencia de la actividad a la que realiza el seguimiento la directiva de alerta supera en gran medida el valor de línea base.
**Centro Criptológico Nacional** 54
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
c) Configurar los destinatarios
**Consultar directivas de alertas**
Desde el menú [Alertas\Directivas de alertas] pueden consultarse las directivas personalizadas, así como todas las directivas predeterminadas en el Centro de
Seguridad de Office 365.
### **3.2 MEDIDAS DE PROTECCIÓN**
#### **3.2.1 PROTECCIÓN DE LAS COMUNICACIONES**
En cuanto a la protección de las comunicaciones, cabe reseñar que se usan los protocolos criptográficos para conexiones TLS, integrados en Office 365 de manera
automática. Esto es así cuando:
- Los usuarios trabajan con archivos guardados en OneDrive For Business o
SharePoint Online.
- Los usuarios comparten archivos en reuniones en línea y conversaciones de
mensajería instantánea.
**Centro Criptológico Nacional** 55
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
- Los usuarios se comunican por correo electrónico.
Todas las comunicaciones de Office 365 están cifradas.
#### **3.2.2 PROTECCIÓN DE LA INFORMACIÓN**
**3.2.2.1** **CALIFICACIÓN DE LA INFORMACIÓN**
En este apartado se tratarán principalmente los mecanismos que ofrece Office 365 para calificar la información y aplicar políticas determinadas. En concreto:
Tipos de información confidencial.
- **Ciclo de vida del dato** (Conocido anteriormente como Políticas de
retención): La administración del ciclo de vida de datos de Microsoft Purview (anteriormente gobernanza de información de Microsoft) le
proporciona herramientas y capacidades para conservar el contenido que necesita conservar y eliminar el que no.
- **DLPs (Data Loss Prevention)** . Con estas políticas de Prevención de
Pérdida de Datos se puede identificar, supervisar y proteger información sensible en todo Office 365.
- **Sensitivity labels** . Permiten clasificar, cifrar, agregar marcadores y
controlar accesos en documentos y correos electrónicos en Office 365.
**POLÍTICAS DE RETENCIÓN**
**Definición de etiquetas de retención**
Estas etiquetas se definen en el Portal de Purview de Office 365, en el menú [Administración del ciclo de vida de datos\Microsoft 365\Etiquetas], una vez
dentro y se utilizan para aplicar políticas de retención a correos de Exchange y documentos de SharePoint y OneDrive. Se puede definir el tiempo que el correo
- el documento debe retenerse, o el tiempo después del cual debe borrarse.
Además, las retenciones se pueden aplicar a partir de la fecha de creación, de última modificación, o a partir de la fecha de aplicación de la etiqueta.
También se puede declarar un documento como Registro para impedir que sea editado o borrado.
Las etiquetas pueden aplicarse **automáticamente** según las condiciones establecidas en el Portal de Purview de Office 365, y los usuarios también
pueden aplicar estas etiquetas directamente en las aplicaciones Office, así como en SharePoint o OneDrive.
**Centro Criptológico Nacional** 56
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
Las **etiquetas de retención** tienen que ver con el cumplimiento, y se aplican a correos o documentos en una ubicación determinada.
Ejemplo: en el departamento comercial se precisa aplicar políticas de retención sobre documentos diversos:
- Presupuestos: retención de 5 años después de la fecha límite del
presupuesto.
- Contratos: retención de 10 años después de la fecha de finalización del
contrato.
- Hojas de producto: declarado como registro (no borrar).
**Consulta y modificación de etiquetas de retención**
a) Acceder a la pestaña de [Etiquetas].
b) Seleccionar una etiqueta.
c) Editar etiqueta. En el panel derecho pulsar el botón “Editar etiqueta”. Definimos la configuración de etiqueta.
**Centro Criptológico Nacional** 57
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
d) Configuramos el periodo de retención e) Configuramos la acción a ejecutar después del periodo
Una vez termine el periodo de retención establecido en la etiqueta, se debe elegir qué hacer con el elemento etiquetado:
- **Eliminar elementos automáticamente** . Se quitarán permanentemente
los elementos etiquetados desde cualquier lugar en el que se almacenen.
- **Iniciar una revisión para su eliminación** . Permite que revisores para
eliminación que se asignen decidan si los elementos se pueden eliminar o si deben realizar otras acciones.
- **Cambiar la etiqueta** . Se puede ampliar el periodo de retención aplicando
otra etiqueta.
- **Seleccionar un flujo de Power Automate** . Se puede ejecutar un flujo de
Power Automate para satisfacer una necesidad empresarial específica.
**Centro Criptológico Nacional** 58
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
- **Desactivar la configuración de retención** . Con esta opción los elementos
etiquetados no se conservarán ni eliminarán cuando se desactive su configuración de retención.
**Creación de una etiqueta de retención**
a) Acceder al menú [Etiquetas] y pulsamos el botón “Crear una etiqueta”.
b) Asignar nombre a la etiqueta.
c) Definimos la configuración de la etiqueta.
**Centro Criptológico Nacional** 59
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
d) Configurar el periodo de retención de la etiqueta.
e) Configuramos la acción a suceder después del periodo de retención f) Revisar y Crear.
**Centro Criptológico Nacional** 60
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Directivas de etiquetas (Publicar etiquetas)**
Una vez creada la etiqueta, el siguiente paso para poder utilizarla es “Publicar etiqueta”.
a) se puede hacer desde la misma pestaña de Etiquetas, haciendo click en “Publicar etiqueta” o desde la pestaña “Directiva de etiquetas”.
**Centro Criptológico Nacional** 61
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
b) Elegir las etiquetas.
c) Elegir ámbito de directiva, es decir, si se aplicara a todo el Directorio o a una unidad de Administración en concreto.
d) Elegir tipo de directiva de retención
**Centro Criptológico Nacional** 62
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
e) Elegir ubicaciones.
Hay que tener en cuenta que, en **Exchange**, las etiquetas de retención de aplicación automática (tanto para consultas como para tipos de información
sensible) **solo se aplican en los nuevos mensajes enviados** (datos en tránsito), no en todos los elementos que ya están presentes en el buzón (datos en reposo).
Además, las etiquetas de retención de aplicación automática para tipos de información sensible se aplican a todos los buzones (no se pueden seleccionar
buzones específicos).
f) Dar un nombre a la directiva.
**Centro Criptológico Nacional** 63
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
g) Revisar y Publicar.
**Nota:** Las etiquetas tardarán hasta 1 día en mostrarse a los usuarios. Las
etiquetas aparecerán en Outlook y Outlook Web App solo para los buzones que tengan al menos 10 MB de datos.
Puede consultarse la nueva directiva en la pestaña correspondiente:
**Uso de las directivas de retención**
Más información en las guías específicas de cada servicio: Sharepoint Online [CCN-STIC-885B - Guía de configuración segura para Sharepoint Online], Exchange
Online [CCN-STIC-885C - Guía de configuración segura para Exchange Online].
**DLPS (DATA LOSS PREVENTION)**
Con estas políticas de Prevención de Pérdida de Datos se puede identificar, supervisar y proteger información sensible en todo Office 365. Por ejemplo, puede
configurar directivas para asegurarse de que la información en correos electrónicos y documentos no se comparta con los contactos inadecuados.
Ejemplos de datos susceptibles de aplicación:
- Datos financieros
- Información de identificación personal
`o` Tarjetas de crédito
**Centro Criptológico Nacional** 64
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
`o` Números de Seguridad Social `o` Registros Médicos, etc.
**Elementos de una directa DLP**
- Dónde proteger el contenido: ubicaciones como Exchange Online, SharePoint
Online y sitios de OneDrive para la Empresa, así como mensajes de chat y canales de Microsoft Teams.
- Cuándo y cómo proteger el contenido aplicando reglas compuestas de:
`o` **Condiciones** que el contenido debe cumplir antes de que se aplique la regla.
Por ejemplo, una regla se puede configurar para que busque solo contenido que incluya números de seguridad social y que se haya compartido con
personas de fuera de su organización.
`o` **Acciones** que quiere que la regla realice automáticamente cuando se encuentra contenido que coincide con las condiciones. Por ejemplo, una
regla se puede configurar para bloquear el acceso a un documento y enviar una notificación por correo electrónico al usuario y al responsable de
cumplimiento.
Por ejemplo, se podría tener una directiva DLP que ayude al tratamiento de datos relativos a la salud.

|¿el qué?|Proteger los datos de salud|
|---|---|
|**¿dónde?**|En todos los sitios de SharePoint Online y OneDrive para la Empresa|
|**¿condiciones?**|Al buscar cualquier documento que contenga información sensible y<br />que se comparte con personas de fuera de la organización|
|**¿acciones?**|Bloquear el acceso al documento y enviar una notificación|

Estos requisitos se almacenan como reglas individuales y se agrupan de forma conjunta como directiva DLP para simplificar la administración y la creación de
informes.
**Casos de uso de una DLP**
Con una directiva DLP se puede:
- **Identificar información sensible en varias ubicaciones**, como Exchange Online,
SharePoint Online, OneDrive para la empresa y Microsoft Teams. Por ejemplo, identificar cualquier documento que contenga un número de tarjeta de crédito,
- bien supervisar solo los sitios de personas específicas.
- **Evitar el uso compartido accidental de información sensible** . Por ejemplo,
identificar cualquier documento o correo electrónico que contenga un registro de mantenimiento compartido con personas de fuera de la organización y, a
continuación, bloquear automáticamente el acceso a ese documento o impedir que se envíe el correo electrónico.
**Centro Criptológico Nacional** 65
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
- **Supervisar y proteger información sensible** en las versiones de escritorio de
Excel, PowerPoint y Word. Al igual que en Exchange Online, SharePoint Online y OneDrive para la empresa, estos programas de escritorio de Office incluyen las
mismas capacidades para identificar información sensible y aplicar directivas de DLP. DLP proporciona supervisión continua cuando las personas comparten
contenido en estos programas de Office.
- **Ayudar a los usuarios a aprender a cumplir** sin interrumpir el flujo de trabajo.
Puede educar a sus usuarios acerca de las directivas DLP y ayudar a que sigan manteniendo el cumplimiento normativo sin bloquear su trabajo. Por ejemplo,
si un usuario intenta compartir un documento que contiene información sensible, una directiva DLP puede enviarle una notificación por correo
electrónico y mostrarle una sugerencia de directiva en el contexto de la biblioteca de documentos que le permite invalidar la directiva si tiene una
justificación comercial. Las mismas sugerencias de directiva también aparecen en Outlook en la web, Outlook, Excel, PowerPoint y Word.
- **Ver informes de DLP** que muestran contenido que coincide con las directivas
DLP de su organización. Para evaluar si la organización está cumpliendo con una directiva DLP, puede ver cuántas coincidencias tienen la directiva y la regla
a lo largo del tiempo. Si una directiva DLP permite a los usuarios invalidar una sugerencia de directiva e informar de un falso positivo, también puede ver qué
han informado los usuarios.
**Crear una nueva política DLP**
a) Desde el Centro de Seguridad de Office 365 en el menú [Prevención de pérdida de datos\Directiva], pulsar el botón “Crear una directiva”.
b) Elegir reglamento del sector o crear una política a medida.
Seleccionar la opción Personalizado para crear una directiva personalizada:
**Centro Criptológico Nacional** 66
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
c) Asignar nombre y descripción.
d) Elegir ámbito de directiva, es decir, si se aplicara a todo el Directorio o a una unidad de Administración en concreto.
**Centro Criptológico Nacional** 67
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
e) Elegir ubicaciones.
Una directiva DLP puede buscar y proteger información sensible en todo Office 365, independientemente de si esa información se encuentra en
Exchange Online, SharePoint Online, OneDrive para la Empresa o Microsoft Teams. Puede elegir proteger el contenido en el correo electrónico de Exchange,
y los mensajes de canales y chats de Microsoft Teams, y todas las bibliotecas de SharePoint o OneDrive, o bien seleccionar ubicaciones específicas para una
directiva.
Si se elige incluir o excluir sitios de SharePoint o cuentas de OneDrive específicos, una directiva DLP no puede contener más de 100 inclusiones y
exclusiones. Aunque este límite exista, se puede superar este límite aplicando una directiva para toda la organización o una directiva que se aplique
ubicaciones completas.
f) Definir reglas.
**Centro Criptológico Nacional** 68
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
Las reglas son las que **aplican los requisitos empresariales en el contenido** de su organización. Una directiva contiene **una o más reglas**, y cada regla consta de
las condiciones y acciones. Para cada regla, cuando se cumplen las condiciones, las **acciones** **se** **realizan** **automáticamente** . Las reglas se ejecutan
**secuencialmente**, comenzando por la regla de mayor prioridad de cada directiva.
Una regla también proporciona opciones para notificar a los usuarios (con sugerencias de directiva y notificaciones por correo electrónico) y los
administradores (con informes de incidentes por correo electrónico) de que el contenido ha coincidido con la regla.
**Centro Criptológico Nacional** 69
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
f1. Condiciones Las condiciones son importantes porque determinan los tipos de
información que está buscando y cuándo se debe realizar una acción.
Las condiciones se centran en el contenido, como el tipo de información sensible que está buscando, y también en el contexto, como con quién se
comparte el documento.
Puede usar condiciones para asignar acciones diferentes a distintos niveles de riesgo. Por ejemplo, el contenido sensible compartido
internamente podría ser de menor riesgo y necesitar menos acciones que el contenido sensible compartido con personas de fuera de la organización.
**Nota:** Dependiendo de las localizaciones seleccionadas, en el apartado
“Condiciones”, veremos más o menos opciones.
**Centro Criptológico Nacional** 70
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
Una directiva DLP puede ayudar a proteger información sensible, lo que se define como un tipo de información sensible. Office 365 incluye definiciones
para muchos tipos comunes de información sensible en muchas regiones diferentes que están listas para su uso, como números de tarjeta de crédito,
números de cuentas bancarias, números de identificación nacionales y números de pasaporte.
f2. Acciones Cuando el contenido coincide con una condición en una regla, se pueden
aplicar acciones para proteger automáticamente el contenido.
**Nota:** Dependiendo de las localizaciones seleccionadas, en el apartado
“Acciones”, veremos más o menos opciones.
- Bloquear el uso compartido para los usuarios y restringir el acceso al
contenido compartido.
De forma predeterminada, los usuarios no podrán enviar a otros usuarios mensajes de correo electrónico, chats de Teams ni mensajes del
canal que incluyan el tipo de contenido que está protegiendo. Pero se puede elegir quién tiene acceso a los archivos compartidos de
**Centro Criptológico Nacional** 71
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
SharePoint y OneDrive. También decidir si se quiere permitir que los usuarios puedan ignorar las restricciones de la directiva.
Bloquear estos usuarios para que no tengan acceso al contenido de SharePoint, OneDrive y Teams:
`o` Todos. Solo el propietario del contenido, el último usuario que lo modificó y el administrador del sitio seguirán teniendo acceso
`o` Solo los usuarios fuera de la organización. Los usuarios de la organización seguirán teniendo acceso.
f3. Notificaciones de usuario e invalidaciones de usuario Se puede utilizar notificaciones de usuario e invalidaciones de usuario para
concienciarles sobre las directivas DLP y ayudarles a que sigan manteniendo el cumplimiento normativo sin bloquear su trabajo.
f4. Reemplazos de usuarios Esta opción permite a los usuarios invalidar las restricciones de la directiva
configurada en el apartado “Acciones”.
f5. Informes de incidentes Cuando una regla coincide, es posible enviar un informe de incidentes a su
responsable de cumplimento normativo (o a la persona que elija) con los detalles del evento.
**Centro Criptológico Nacional** 72
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
f6. Opciones adicionales g) Modo de directiva
**Centro Criptológico Nacional** 73
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
h) Revisar y finalizar
**PROTECCIÓN DE LA INFORMACIÓN DE MICROSOFT PURVIEW (ETIQUETAS DE SENSIBILIDAD)**
Las sensitivity labels se utilizan para clasificar mensajes de correo electrónico, documentos, sitios y mucho más. Cuando se aplique una etiqueta
(independientemente de si la aplica el usuario o se aplica automáticamente), el contenido o el sitio se protegerá en función de la configuración que se elija. Por
ejemplo, pueden crearse etiquetas que cifren archivos, que agreguen marcadores de contenido y que controlen el acceso de los usuarios a sitios específicos.
**Nota:** Las sensitivity labels son distintas de las etiquetas de retención (se usan para
conservar o eliminar el contenido en función de las directivas que se definan).
**Centro Criptológico Nacional** 74
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Crear sensitivity labels**
Abrir el Portal de Purview de Office 365, menú [Protección de la información\Etiquetas].
- En primer lugar, se debe **establecer una taxonomía** para definir los diferentes
niveles de contenido sensible. Lo mejor es usar nombres o términos comunes que tengan sentido para los usuarios. Por ejemplo, se puede empezar con las
etiquetas por defecto: Personal, Public, General, Confidential y Highly Confidential.
- Después, **definir qué puede hacer cada etiqueta** . Configurar las opciones de
protección que se quiere asociar a cada etiqueta. Por ejemplo, el contenido con un nivel de sensibilidad menor (una etiqueta "General") podría simplemente
tener un encabezado o pie de página aplicados, mientras que al contenido con un nivel de sensibilidad mayor (una etiqueta "Confidential") se le podrían aplicar
marcas de agua, encriptación para asegurarse de que solo los usuarios con privilegios pueden acceder a él.
- Y, por último, **definir quién obtiene las etiquetas** . Después de definir las
etiquetas de la organización, se publican en una directiva de etiqueta que controla qué usuarios y grupos pueden ver esas etiquetas. Una misma etiqueta
puede reutilizarse: definirla una vez y después incluirla en varias directivas de etiqueta asignadas a diferentes usuarios. Pero para que una etiqueta pueda
asignarse a un contenido, primero debe publicarse dicha etiqueta para que esté disponible en las aplicaciones de Office y otros servicios.
**Centro Criptológico Nacional** 75
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**Ejemplo de creación de sensitivity labels:**
Los archivos etiquetados estarán protegidos dondequiera que se lleven, tanto si están guardados en la nube o como si están descargados en un equipo.
a) Desde el Portal de Purview de Office 365, menú [Protección de la información\Etiquetas]. Pulsar el botón: “Crear una etiqueta”.
b) Cumplimentar el siguiente formulario con el nombre que tendrá la etiqueta, la prioridad, la descripción y el color.
**Centro Criptológico Nacional** 76
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
c) Ámbito Aquí se elige a que tipo de elementos aplicara esta etiqueta.
d) Elementos - Cifrado d1. Cifrado - Para cifrar elementos elegimos la opción “Controlar acceso”.
**Centro Criptológico Nacional** 77
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
d2. ¿Asignar permisos ahora o permitir que los usuarios decidan?
d3. Asignar permisos ahora Esta opción determina exactamente los permisos para el contenido con
esa etiqueta y los usuarios que los obtendrán.
- **En Outlook, aplique una de las siguientes restricciones:**
`o` **No reenviar** : Cuando los usuarios aplican la etiqueta a un correo electrónico en Outlook, los destinatarios podrán leer el
mensaje, pero no podrá reenviar, imprimir ni copiar el contenido. El remitente tiene permiso total para sus mensajes
y todas las respuestas.
`o` **Solo cifrar** : Cuando los usuarios aplican la etiqueta a un correo en Outlook, el correo se cifra y los destinatarios deben
autenticarse. Los destinatarios no tienen restricciones, excepto que no pueden quitar el cifrado.
- **En Word, PowerPoint y Excel, pedir a los usuarios que especifiquen**
**permisos** : Cuando los usuarios aplican la etiqueta a los archivos de
Word, PowerPoint o Excel, aparece un cuadro de diálogo en el que se
**Centro Criptológico Nacional** 78
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
les pide que elijan uno de los niveles de permisos predefinidos, especifiquen los usuarios o grupos a los que se aplican y, de forma
opcional, establezcan una fecha de expiración para el archivo etiquetado.
- **Usar el cifrado de doble clave** : Active DKE si desea utilizar dos llaves
para controlar aún más el acceso a los elementos etiquetados.
Microsoft almacena una clave en Azure y usted tiene la otra. Tenga en cuenta que, si activa esta opción, no podrá editar la etiqueta una vez
creada.
d4. Permitir a los usuarios asignar permisos al aplicar la etiqueta al contenido.
De esta forma, puede permitir a los usuarios de su organización cierta flexibilidad que pueden necesitar para colaborar y llevar a cabo su
trabajo.
1. El acceso del usuario al contenido expira Si desea limitar el tiempo que los usuarios pueden acceder al
contenido con esta etiqueta, especifique una fecha o un número de días en los que el acceso deba vencer. Más información:
- Después de este tiempo, los usuarios no podrán abrir archivos que
tengan esta etiqueta aplicada. Sin embargo, para los correos electrónicos, la expiración no siempre se aplica debido a los
mecanismos de almacenamiento en caché usados por algunos clientes de correo electrónico.
- Si especifica una fecha, es efectiva la medianoche en la zona horaria
actual.
- Si especifica un número de días, la hora comienza en el momento en
que se aplica la etiqueta al contenido.
**Centro Criptológico Nacional** 79
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
2. Permitir acceso sin conexión Si especifica que el contenido etiquetado nunca esté disponible sin
conexión o que solo esté disponible sin conexión durante un número de días, cuando se alcanza ese umbral, los usuarios deben volver a
autenticarse y su acceso se registra. Cuando esto sucede, si sus credenciales no se almacenan en caché, se pedirá a los usuarios que
inicien sesión en Microsoft 365 para poder abrir el documento o el correo electrónico.
3. Asignar permisos a usuarios y grupos específicos Aquí se asignan los permisos a usuarios específicos para que solo ellos
puedan interactuar con contenido que tenga esta etiqueta aplicada.
**Centro Criptológico Nacional** 80
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
4. Usar el cifrado de doble clave Active DKE si desea utilizar dos llaves para controlar aún más el acceso a
los elementos etiquetados. Microsoft almacena una clave en Azure y usted tiene la otra. Tenga en cuenta que, si activa esta opción, no podrá
editar la etiqueta una vez creada. Para más información ver [Aplicar](https://learn.microsoft.com/es-es/purview/encryption-sensitivity-labels#double-key-encryption)
[cifrado mediante etiquetas de confidencialidad | Microsoft Learn](https://learn.microsoft.com/es-es/purview/encryption-sensitivity-labels#double-key-encryption)
e) Elementos - Marcado de contenido Se pueden asignar encabezados, pies o marcas de agua que se agregará al
documento o correo electrónico.
f) Etiquetado automático
**Centro Criptológico Nacional** 81
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
Cuando se detecte contenido sensible en el correo electrónico o en los documentos que cumplan las condiciones que se elija, se puede aplicar
automáticamente esta etiqueta o mostrar un mensaje a los usuarios que les recomiende que la apliquen ellos mismos.
g) Parámetros de protección de los grupos y sitios.
Esta configuración se aplica a equipos, grupos y sitios que tengan esta etiqueta aplicada. Pero no se aplica directamente a los archivos almacenados
en estos contenedores.
h) Etiquetado automático para recursos de datos esquematizados
**Publicar** _**sensitivity labels**_
Una vez creada la etiqueta se publica, así estará disponible en aplicaciones de Office (Word, Excel, PowerPoint y Outlook), sitios de SharePoint y Teams, y grupos de Office
365 de usuarios específicos.
a) Pulsar el botón “Publicar etiqueta”.
**Centro Criptológico Nacional** 82
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
b) Seleccionar las etiquetas desde el asistente de publicación (panel derecho).
c) Ámbito d) Elegir usuarios o grupos
e) Configuración de la directiva Se puede tener una etiqueta de forma predeterminada, una etiqueta obligatoria
- requerir a los usuarios que justifiquen las acciones en su extremo.
**Centro Criptológico Nacional** 83
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
f) Configuración predeterminada para documentos g) Configuración predeterminada para los correos electrónicos
h) Configuración predeterminada para reuniones y eventos de calendario
**Centro Criptológico Nacional** 84
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
i) Configuración predeterminada para el contenido de Fabric y Power BI j) Nombrar la directiva.
**3.2.2.2** **LIMPIEZA DE DOCUMENTOS**
Al compartir una copia electrónica de determinados documentos de Office365 o al exponer cierta documentación en internet, es una buena práctica revisar los
documentos en busca de datos ocultos, información personal y en general cualquier metadato que pudiera estar asociado. Es posible eliminar esta información a través del
Inspector de documentos, característica que se accede desde las propias aplicaciones de Word, Excel, PowerPoint o Visio.
**3.2.2.3** **COPIAS DE SEGURIDAD**
En el Modelo de responsabilidad compartida de Office 365 de Microsoft donde se especifica qué es responsabilidad de Microsoft y qué responsabilidad del cliente en
materia de copias de seguridad.
No existe una solución global de respaldo de Office 365. Consultar las guías específicas de los servicios para información más concreta.
**Centro Criptológico Nacional** 85
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
#### **3.2.3 PROTECCIÓN DE LOS SERVICIOS**
**3.2.3.1** **PROTECCIÓN FRENTE A DENEGACIÓN DE SERVICIO**
Office 365 ofrece un sistema avanzado de detección de amenazas y sistemas de mitigación para proteger la infraestructura subyacente de los ataques de denegación
de servicio (DoS) y prevenir la interrupción de servicio a los clientes.
El sistema de defensa DDoS de Azure está diseñado no solo para resistir ataques desde el exterior, sino también desde otros tenants de Azure. Los mecanismos de
limitación de peticiones de Exchange Online y SharePoint Online forman parte de un enfoque de varias capas para defenderse contra ataques DoS.
Consultar la guía [CCN-STIC-884A - Guía de configuración segura para Azure] para obtener más información sobre el sistema de defensa DDoS de Azure.
**Centro Criptológico Nacional** 86
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
### **4. OTRAS CONSIDERACIONES DE SEGURIDAD** **4.1 SERVICIOS Y COMPLEMENTOS**
Es interesante, de cara a tener un mayor control sobre las operaciones que puedan realizar los usuarios, restringir o habilitar el uso de ciertos servicios y complementos
adicionales que puedan estar disponibles para los usuarios de Office 365. Este control se realiza desde el Centro de administración de Microsoft 365, menú
[Configuración\Configuración de la organización].
**Centro Criptológico Nacional** 87
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
### **5. CARACTERÍSTICAS DISPONIBLES POR LICENCIAMIENTO**

|Administración de cuentas de usuario Microsoft 365 E Microsoft 365 Office 365 E1 Microsoft 365 Microsoft 365 Microsoft 365 Microsoft 365<br />mpresa Básico Empresa E3 y Office 365 E5 y Office 365 F1 F3 y Office 365<br />y Estándar Premium E3 E5 Enterprise F3|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Identidad en la nube, identidad federada**<br />**o autenticación multifactor**|Sí|Sí|Sí|Sí|Sí|Sí|Sí|
|**Configuración de escritorio de Office 365**|Sí|Sí|No|Sí|Sí|No|No|
|**Eliminar cuentas y restablecer**<br />**contraseñas de usuario de Microsoft 365**<br />**o mediante Windows PowerShell**|Sí|Sí|Sí|Sí|Sí|Sí|Sí|
|**Los usuarios pueden cambiar su propia**<br />**contraseña**|Sí|Sí|Sí|Sí|Sí|Sí|Sí|
|**Administración de licencias**|Sí|Sí|Sí|Sí|Sí|Sí|Sí|
|**Informes de actividad del centro de**<br />**Administración**|**Microsoft 365**<br />**Empresa Básico**<br />**y Estándar**|**Microsoft 365**<br />**Empresa**<br />**Premium**|**Office 365 E1**|**Microsoft 365**<br />**E3 y Office 365**<br />**E3**|**Microsoft 365**<br />**E5 y Office 365**<br />**E5**|**Microsoft 365**<br />**F1**|**Microsoft 365**<br />**F3 y Office 365**<br />**Enterprise F3**|
|**Informes de actividad**|Sí|Sí|Sí|Sí|Sí|Sí|Sí|
|**API de informes de uso de Microsoft**<br />**Graph**|Sí|Sí|Sí|Sí|Sí|Sí|Sí|
|**Microsoft Graph API (BETA)**|Sí|Sí|Sí|Sí|Sí|Sí|Sí|
|**Confianza**|**Microsoft 365**<br />**Empresa Básico**<br />**y Estándar**|**Microsoft 365**<br />**Empresa**<br />**Premium**|**Office 365 E1**|**Microsoft 365**<br />**E3 y Office 365**<br />**E3**|**Microsoft 365**<br />**E5 y Office 365**<br />**E5**|**Microsoft 365**<br />**F1**|**Microsoft 365**<br />**F3 y Office 365**<br />**Enterprise F3**|
|**Office 365 Cloud App Security**|No|No|No|No|Sí|No|No|
|**Detección de Microsoft Defender for**<br />**Cloud Apps**|No|Sí|No|Sí (solo M365<br />E3)|Sí|Sí|Sí (solo M365<br />F3)|
|**Microsoft Defender for Cloud Apps**|No|No|No|No|Sí (solo M365<br />E5)|No|No|
|**Microsoft Defender para Office 365**|No|Sí|No|No|Sí|No|No|

**Centro Criptológico Nacional** 88
**CCN-STIC 885A** **Guía de configuración segura para Office 365**

|Caja de seguridad del cliente de<br />Microsoft Purview|No|No|No|No|Sí|No|No|
|---|---|---|---|---|---|---|---|
|**Clave de cliente de Microsoft Purview**|No|No|No|No|Sí|No|No|
|**Microsoft Purview eDiscovery (Premium)**|No|No|No|No|Sí|No|No|
|**Auditoría de Microsoft Purview**<br />**(estándar)**|Sí|Sí|Sí|Sí|Sí|Sí|Sí|
|**Auditoría de Microsoft Purview**<br />**(Premium)**|No|No|No|No|Sí|No|No|
|**Puntuación de seguridad de Microsoft**|Sí|Sí|Sí|Sí|Sí|Sí|Sí|
|**Office 365 Threat Intelligence**|No|No|No|No|Sí|No|No|

**Centro Criptológico Nacional** 89
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
### **6. GLOSARIO Y ABREVIATURAS**
A continuación de describen una serie de términos, acrónimos y abreviaturas en materia de seguridad utilizados en esta guía:

|Término|Definición|
|---|---|
|**AD DS**|_Active Directory Domain Services_(Servicios de dominio de<br />Directorio Activo).|
|**Microsoft Entra**<br />**ID**|_Conocido anteriormente como Azure Active Directory_.|
|**Azure RMS**|_Azure Rights Management_ (Azure RMS).|
|**Centro de**<br />**Administración**<br />**de Microsoft**<br />|Portal de Administración de Office 365.<br />Accesible desde la url: admin.microsoft.com.|
|**CSP**|_Cloud Service Provider_|
|**DDoS**|_Distributed Denial of Service_(Ataque de Denegación de Servicio<br />Distribuido), el cual se lleva a cabo generando un gran flujo de<br />información desde varios puntos de conexión hacia un mismo<br />punto de destino.|
|**ENS**|_Esquema Nacional de Seguridad._|
|**MFA**|_Multifactor Authentication_(Autenticación Multifactor). Sistema<br />de seguridad que requiere más de una forma de autenticarse, por<br />ejemplo, a través de una_app_, _sms_, etc.|
|**Microsoft**<br />**Intune**|Microsoft Intune es un servicio de administración de movilidad<br />empresarial (EMM) basado en nube que ayuda a los empleados a<br />ser productivos mientras mantiene protegidos los datos<br />corporativos. Al igual que otros servicios de Azure, Microsoft<br />Intune está disponible en el portal de Azure.**Intune** permite:<br />- <br />Administrar los dispositivos móviles y los equipos que los<br />empleados usan para tener acceso a datos de la empresa.<br />- <br />Administrar las aplicaciones móviles que usa la plantilla.<br />- <br />Proteger la información de la empresa al ayudar a controlar la<br />manera en que los empleados tienen acceso a ella y la<br />comparten.<br />- <br />Garantizar que los dispositivos y las aplicaciones sean<br />compatibles con los requisitos de seguridad de la empresa|
|**O365**|_Office 365._|
|**PowerShell**|PowerShell (originalmente llamada Windows PowerShell) es una<br />interfaz de consola (_CLI_) con posibilidad de escritura y unión de<br />comandos por medio de instrucciones (_scripts_).|
|**PS**|_PowerShell_.|
|**SaaS**|_Software as a Service_ (Software como Servicio). Modelo de<br />distribución de software donde el soporte lógico y los datos que|

**Centro Criptológico Nacional**
**CCN-STIC 885A** **Guía de configuración segura para Office 365**

|Col1|maneja se alojan en servidores de una compañía de TIC, y se<br />accede vía internet.|
|---|---|
|**Sensitivity label**|_Etiqueta de sensibilidad._Permiten clasificar, cifrar, agregar<br />marcadores y controlar accesos en documentos y correos<br />electrónicos en Office 365.|
|**Tenant**|Un_tenant_ de Office 365 es un espacio reservado en la nube de<br />Microsoft desde el que tendremos acceso a los recursos y<br />servicios que Microsoft ofrece.|
|**TLS**|TLS (Seguridad de la capa de transporte) y SSL (antecesor de TLS)<br />son protocolos criptográficos que protegen la comunicación por<br />red con certificados de seguridad que cifran una conexión entre<br />equipos.|

**Centro Criptológico Nacional**
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
### **7. ANEXO A. CREAR UNA CUENTA DE USUARIO INDIVIDUAL**
a) **Import-Module Microsoft.Graph.Users** : Con la primera línea importamos el módulos
b) **Connect-MgGraph -Scopes "User.ReadWrite.All** ": Nos conectamos a Microsoft Graph con el rol de lectura y escritura de usuarios.
c) **$params_CreateUsers:** En este array añadimos los datos del usuario.
d) **passwordProfile:**
**a.** **forceChangePasswordNextSignIn:** Al poner en true esta línea
estamos indicando que el usuario debe cambiar la contraseña en el siguiente inicio de sesión.
**b.** **Password:** Aquí se debe escribir la contraseña del usuario. Por
defecto exige que la contraseña sea fuerte.
e) **$params_AddLincese:** En este array añadimos las opciones de las licencias.
**a.** **addLicenses:**
**i.** **disabledPlans:** Si hay algún plan de la licencia que se desea
desactivar, se debera escribir el skuID de ese plan dentro de este array.
ii. **skuId:** Escribimos el skuID de la licencia a asignar.
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
**b.** **removeLicenses = @():** Si el usuario ya tuviese alguna licencia
asignada y hubiera que quitarla, se deberá escribir el skuID de esta licencia.
f) **New-MgUser -BodyParameter $params_CreateUsers:** Este comando crea el usuario.
g) **Set-MgUserLicense** **-UserId** **"AdeleV@domain.com"** **-BodyParameter**
**$params_AddLincese:** Este comando asigna la licencia al usuario creado.
h) **Disconnect-MgGraph:** Este comando termina la conexión con Microsoft Graph.
### **8. ANEXO B. CREAR VARIAS CUENTAS DE USUARIO**
a) Crear un archivo de valores separados por comas (CSV) que contenga la información necesaria de la cuenta de usuario. Por ejemplo:
b) Ejecutar desde PowerShell:
**CCN-STIC 885A** **Guía de configuración segura para Office 365**
a) **Import-Module Microsoft.Graph.Users** : Con la primera línea importamos el módulos
b) **Connect-MgGraph -Scopes "User.ReadWrite.All** ": Nos conectamos a Microsoft Graph con el rol de lectura y escritura de usuarios.
c) **$UsersList:** Aqui se añadira la ruta del CSV de los usuarios d) **$params_CreateUsers:** En este array añadimos los datos del usuario.
e) **passwordProfile:**
**a.** **forceChangePasswordNextSignIn:** Al poner en true esta línea
estamos indicando que el usuario debe cambiar la contraseña en el siguiente inicio de sesión.
**b.** **Password:** Aquí se debe escribir la contraseña del usuario. Por
defecto exige que la contraseña sea fuerte.
f) **$params_AddLincese:** En este array añadimos las opciones de las licencias.
**a.** **addLicenses:**
**i.** **disabledPlans:** Si hay algún plan de la licencia que se desea
desactivar, se debera escribir el skuID de ese plan dentro de este array.
ii. **skuId:** Escribimos el skuID de la licencia a asignar.
**b.** **removeLicenses = @():** Si el usuario ya tuviese alguna licencia
asignada y hubiera que quitarla, se deberá escribir el skuID de esta licencia.
g) **New-MgUser -BodyParameter $params_CreateUsers:** Este comando crea el usuario.
h) **Set-MgUserLicense -UserId "&lt;>" -BodyParameter $params_AddLincese:** Este comando asigna la licencia al usuario creado.
i) **Disconnect-MgGraph:** Este comando termina la conexión con Microsoft Graph.
**CCN-STIC-885A** **Guía de configuración segura para Office 365**
### 9. CUADRO RESUMEN DE MEDIDAS DE SEGURIDAD
Se facilita a continuación un cuadro resumen de configuraciones a aplicar para la protección del servicio, donde la organización podrá valorar qué medidas de las propuestas se cumplen.

|Control ENS|Configuración|Estado|Col4|
|---|---|---|---|
|Op|**Marco Operacional**|**Marco Operacional**|**Marco Operacional**|
|Op.acc|**Control de Acceso**|**Control de Acceso**|**Control de Acceso**|
|Op.acc.1|**Identificación**|**Identificación**|**Identificación**|
|Op.acc.1|Se ha configurado el uso de cuentas y la asignación de licencias a usuarios.<br />Cada usuario debe disponer de un acceso nominal y personal a Office 365<br />que permita su identificación de forma única.<br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
|Op.acc.1|Se ha configurado el uso de cuentas y la asignación de licencias a usuarios.<br />Cada usuario debe disponer de un acceso nominal y personal a Office 365<br />que permita su identificación de forma única.<br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|Op.acc.3|**Segregación de funciones y tareas**|**Segregación de funciones y tareas**|**Segregación de funciones y tareas**|
|Op.acc.3|Se ha asignado adecuadamente los roles de administración.<br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
|Op.acc.3|Se ha asignado adecuadamente los roles de administración.<br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**<br /> <br /> <br /> <br /> <br />|

**Centro Criptológico Nacional** 95
**CCN-STIC-885A** **Guía de configuración segura para Office 365**

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|Op.acc.5 <br />Op.acc.6|**Mecanismo de autenticación**<br />|**Mecanismo de autenticación**<br />|**Mecanismo de autenticación**<br />|
|Op.acc.5 <br />Op.acc.6|Se ha habilitado_Multi-Factor Authentication_ (MFA) para los usuarios de la<br />organización y externos.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
|Op.acc.5 <br />Op.acc.6|Se ha habilitado_Multi-Factor Authentication_ (MFA) para los usuarios de la<br />organización y externos.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|Op.acc.5 <br />Op.acc.6|Se ha habilitado_Multi-Factor Authentication_ (MFA) para los usuarios de la<br />organización y externos.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|op.exp|**Explotación**|**Explotación**|**Explotación**|
|op.exp.6|**Protección frente a código dañino**|**Protección frente a código dañino**|**Protección frente a código dañino**|
|op.exp.6|Se han habilitado y configurado una o varias medidas de protección del<br />correo electrónico como Antispam, Antispoofing, Antiphishing y<br />Antimalware.<br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
|op.exp.6|Se han habilitado y configurado una o varias medidas de protección del<br />correo electrónico como Antispam, Antispoofing, Antiphishing y<br />Antimalware.<br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**<br />|

**Centro Criptológico Nacional** 96
**CCN-STIC-885A** **Guía de configuración segura para Office 365**

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|op.exp.6|**Protección frente a código dañino**|||
||Se comprueba periódicamente la detección de amenazas en tiempo real,<br />accesible desde el_Centro de Seguridad de Office 365_, y se genera el informe<br />pertinente.<br />_* Si la organización dispone de las licencias correspondientes._<br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se comprueba periódicamente la detección de amenazas en tiempo real,<br />accesible desde el_Centro de Seguridad de Office 365_, y se genera el informe<br />pertinente.<br />_* Si la organización dispone de las licencias correspondientes._<br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**<br />|
|op.exp.7|**Gestión de incidentes**|**Gestión de incidentes**|**Gestión de incidentes**|
||Se ha revisado el panel de incidentes y han aplicado las medidas necesarias<br />para corregirlas.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se ha revisado el panel de incidentes y han aplicado las medidas necesarias<br />para corregirlas.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|op.exp.8|**Registro de la actividad**|**Registro de la actividad**|**Registro de la actividad**|
||Se ha comprobado que el registro de Auditoría está activado y capturando<br />eventos.<br /> <br /> <br /> <br /> <br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se ha comprobado que el registro de Auditoría está activado y capturando<br />eventos.<br /> <br /> <br /> <br /> <br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br />|**Observaciones:**|

**Centro Criptológico Nacional** 97
**CCN-STIC-885A** **Guía de configuración segura para Office 365**

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|op.exp.8|**Registro de la actividad**|**Registro de la actividad**|**Registro de la actividad**|
||Se ha securizado la consulta del registro de actividad mediante el<br />establecimiento de los roles adecuados.<br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se ha securizado la consulta del registro de actividad mediante el<br />establecimiento de los roles adecuados.<br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|op.mon|**Monitorización del sistema**|**Monitorización del sistema**|**Monitorización del sistema**|
||Se han configurado alertas en el_Centro de Seguridad de Office 365._<br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se han configurado alertas en el_Centro de Seguridad de Office 365._<br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|

**Centro Criptológico Nacional** 98
**CCN-STIC-885A** **Guía de configuración segura para Office 365**

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|mp|**Medidas de Protección**|**Medidas de Protección**|**Medidas de Protección**|
|mp.info|**Protección de la información**|**Protección de la información**|**Protección de la información**|
|mp.info.2|**Calificación de la información**|**Calificación de la información**|**Calificación de la información**|
||Se han aplicado políticas de retención.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se han aplicado políticas de retención.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|mp.info.2|**Calificación de la información**|**Calificación de la información**|**Calificación de la información**|
||Se han aplicado políticas de DLPs.<br /> <br /> <br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se han aplicado políticas de DLPs.<br /> <br /> <br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|mp.info.2|**Calificación de la información**|**Calificación de la información**|**Calificación de la información**|
||Se han aplicado_ sensitivity labels._|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|

**Centro Criptológico Nacional** 99
**CCN-STIC-885A** **Guía de configuración segura para Office 365**

|Col1|Col2|Evidencias Recogidas:<br />Si No|Observaciones:|
|---|---|---|---|
|mp.info.5|**Limpieza de documentos**|**Limpieza de documentos**|**Limpieza de documentos**|
||Se ha eliminado información personal y en general cualquier metadato que<br />pudiera estar asociado a los documentos.<br />*Mediante la herramienta**Inspector de documentos** (característica que se<br />accede desde las propias aplicaciones de Word, Excel, PowerPoint o Visio) o<br />aplicaciones de terceros.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se ha eliminado información personal y en general cualquier metadato que<br />pudiera estar asociado a los documentos.<br />*Mediante la herramienta**Inspector de documentos** (característica que se<br />accede desde las propias aplicaciones de Word, Excel, PowerPoint o Visio) o<br />aplicaciones de terceros.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|mp.info.6|**Copias de seguridad**|**Copias de seguridad**|**Copias de seguridad**|
||Se dispone de planes específicos de copias de seguridad de la información en<br />aquellos servicios en donde se admita.|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se dispone de planes específicos de copias de seguridad de la información en<br />aquellos servicios en donde se admita.|Si<br />No<br />**Evidencias Recogidas:**<br /> <br /> <br />|**Observaciones:**|
|mp.s|**Protección de los servicios**|**Protección de los servicios**|**Protección de los servicios**|
|mp.s.8|**Protección frente a denegación de servicio**|**Protección frente a denegación de servicio**|**Protección frente a denegación de servicio**|
||Se ha tenido en cuenta la información detallada en la guía [CCN-STIC-884A -<br />Guía de configuración segura para Azure] sobre el_sistema de defensa DDoS_<br />_de Azure_. <br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|

**Centro Criptológico Nacional** 100
**CCN-STIC-885A** **Guía de configuración segura para Office 365**

|Col1|Col2|Evidencias Recogidas:<br />Si No|Observaciones:|
|---|---|---|---|
||**Servicios y complementos**|**Servicios y complementos**|**Servicios y complementos**|
||Se ha controlado los servicios y complementos disponibles para los usuarios.<br />|Si<br />No<br />**Aplica:**<br /> <br /> <br />|Si<br />No<br />**Cumple:**<br /> <br />|
||Se ha controlado los servicios y complementos disponibles para los usuarios.<br />|Si<br />No<br />**Evidencias Recogidas:**<br /> <br />|**Observaciones:**|

**Centro Criptológico Nacional** 101
**CCN-STIC-885A** **Guía de configuración segura para Office 365**
**Centro Criptológico Nacional** 102