---
title: "Guía de Seguridad de las TIC CCN-STIC 885B Guía de configuración segura para SharePoint Online"
sidebar_label: "Guía de Seguridad de las TIC CCN-STIC 885B Guía de configuración segura para SharePoint Online"
responsable: "Director de Calidad"
clasificacion: "USO INTERNO"
fecha_revision: "2026-03-15"
idioma: "es"
tags:
  - formacion
  - iso-27001
  - seguridad
  - soporte
---

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-0-0.png)
# **Guía de Seguridad de las TIC** **CCN-STIC 885B** **Guía de configuración segura para SharePoint Online**

## **JUNIO 2024**



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-0-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-0-2.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


**Catálogo de Publicaciones de la Administración General del Estado**
**https://cpage.mpr.gob.es**

Edita:

CENTRO CRIPTOLOGICO NACIONAL
cn=CENTRO CRIPTOLOGICO NACIONAL,
2.5.4.97=VATES-S2800155J, ou=CENTRO
CRIPTOLOGICO NACIONAL, o=CENTRO
CRIPTOLOGICO NACIONAL, c=ES
2024.07.23 13:08:31 +02'00'

Pº de la Castellana 109, 28046 Madrid
© Centro Criptológico Nacional, 2024

NIPO: 083-24-248-9
Fecha de Edición: junio de 2024

**LIMITACIÓN DE RESPONSABILIDAD**
El presente documento se proporciona de acuerdo con los términos en él recogidos, rechazando
expresamente cualquier tipo de garantía implícita que se pueda encontrar relacionada. En ningún caso,
el Centro Criptológico Nacional puede ser considerado responsable del daño directo, indirecto, fortuito

      - extraordinario derivado de la utilización de la información y software que se indican incluso cuando se
advierta de tal posibilidad.

**AVISO LEGAL**
Quedan rigurosamente prohibidas, sin la autorización escrita del Centro Criptológico Nacional, bajo las
sanciones establecidas en las leyes, la reproducción parcial o total de este documento por cualquier
medio o procedimiento, comprendidos la reprografía y el tratamiento informático, y la distribución de
ejemplares del mismo mediante alquiler o préstamo públicos.


**Centro Criptológico Nacional** 2



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-1-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-1-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-1-2.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-1-3.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**

### **ÍNDICE**

**1.** **SHAREPOINT ONLINE ........................................................................................... 4**

1.1 DESCRIPCIÓN DEL USO DE ESTA GUÍA ..................................................................... 4
1.2 DEFINICIÓN DEL SERVICIO ........................................................................................ 4
1.3 PRERREQUISITOS PARA EL DESPLIEGUE MEDIANTE POWERSHELL ......................... 6
**2.** **DESPLIEGUE DE SHAREPOINT ONLINE ................................................................... 6**

2.1 ADMINISTRADOR – CONFIGURACIÓN INICIAL ......................................................... 6
2.2 USUARIO FINAL – PRIMEROS PASOS ........................................................................ 9

2.2.1 CREAR UN SITIO ................................................................................................. 10
**3.** **CONFIGURACIÓN DE SHAREPOINT ONLINE ......................................................... 17**

3.1 MARCO OPERACIONAL ........................................................................................... 17

3.1.1 CONTROL DE ACCESO ........................................................................................ 17
3.1.2 EXPLOTACIÓN .................................................................................................... 27
3.1.3 MONITORIZACIÓN DEL SISTEMA ....................................................................... 29
3.2 MEDIDAS DE PROTECCIÓN ..................................................................................... 29

3.2.1 PROTECCIÓN DE LAS COMUNICACIONES .......................................................... 29
3.2.2 PROTECCIÓN DE LA INFORMACIÓN .................................................................. 30
3.2.3 PROTECCIÓN DE LOS SERVICIOS ....................................................................... 37
**4.** **SCRIPTS DE CONFIGURACIÓN ............................................................................. 38**
**5.** **OTRAS CONSIDERACIONES DE SEGURIDAD ......................................................... 39**

5.1 CONTROL DE VERSIONES ....................................................................................... 39
5.2 PAPELERA DE RECICLAJE ........................................................................................ 41
5.3 DIRECTIVAS DE USO COMPARTIDO ........................................................................ 43
5.4 BLOQUEAR LA INTEGRACIÓN CON YAMMER ........................................................ 45
**6.** **GLOSARIO Y ABREVIATURAS .............................................................................. 46**
**7.** **CUADRO RESUMEN DE MEDIDAS DE SEGURIDAD ............................................... 47**


**Centro Criptológico Nacional** 3


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**

### **1. SHAREPOINT ONLINE** **1.1 DESCRIPCIÓN DEL USO DE ESTA GUÍA**


El objetivo de la presente guía es indicar los pasos a seguir para la configuración del
servicio _SharePoint Online_ cumpliendo con los requisitos necesarios del _Esquema_
_Nacional de Seguridad_ en su categoría ALTA.


Esta guía debe usarse en conjunto con “CCN-STIC-885A - Guía de configuración
segura para Office 365”, donde se describen generalidades de Microsoft 365 y
características comunes a todos los servicios, así como un _glosario_ con los términos y
abreviaturas de seguridad utilizadas en estas guías.


Para la confección de esta guía se han consultado las siguientes fuentes:


         - Documentación oficial de Microsoft.

         - CCN-STIC-823 Servicios en la Nube.

         - CCN-STIC-884A - Guía de configuración segura para Azure.

         - CCN-STIC-885A - Guía de configuración segura para Office 365.

         - ENS Real Decreto BOE-A-2022-7191.

### **1.2 DEFINICIÓN DEL SERVICIO**


_SharePoint Online_ (SPO) es un servicio basado en la nube que ayuda a las
organizaciones a compartir y administrar contenidos, conocimiento y aplicaciones para


Las principales características de _SharePoint Online_ son:

      - _Compartición sencilla y colaboración continua._


Proporcionar a los contactos un lugar donde organizarse y colaborar en el
contenido, los datos y noticias para que estén en sintonía.

      - _Informar y poner en contacto a la organización._


Compartir recursos y aplicaciones comunes y difundir mensajes con páginas
dinámicas y enriquecidas.

      - _Inteligencia._


Búsqueda empresarial potente de archivos, sitios y contactos.


**Centro Criptológico Nacional** 4



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-3-0.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


_SharePoint Online_ incluye:



















|Col1|Almacenamiento dearchivos|OneDrive proporciona espacio de almacenamientopersonal en la nube.|
|---|---|---|
||_Uso compartido__externo_|Compartir archivos y contenido de forma segura con loscontactos de dentro y fuera de la organización.|
||_Administración de__contenido_|Organizar y administrar contenido en bibliotecas y listascon metadatos, administración de registros y directivasde retención.|
||_Sitios de grupo_|Proporcionar un lugar para que el equipo se organice ycolabore en el contenido, los datos y noticias para queestén en sintonía.|
||_Sitios de__comunicación_|Difundir mensajes de un grupo y compartirlo con losmiembros de la organización con sitios de comunicaciónatractivos y dinámicos.|
||_Intranets_|Informar e involucrar a la organización con intranets ysitios para dotar de contenidos, anunciar las novedades,compartir recursos, simplificar los procesos e involucrara los contactos.|
||_Aplicaciones móviles_|Obtener acceso a las intranets, sitios de grupo ycontenido con la aplicación móvil de SharePoint paraAndroid™, iOS®, y Windows y las aplicaciones móvilesde OneDrive para Android, iOS y Windows.|
||_Automatizar el__trabajo_|Automatizar los procesos empresariales con alertas yflujos de trabajo.|
||_Detección_|Descubrir los contactos relevantes y el contenidoimportante cuando más se necesite.|
||_Búsqueda_|Personalización de la búsqueda empresarial y losresultados con características mejoradas para queaparezcan los recursos en Microsoft 365.|
||_eDiscovery_|Buscarcontenidoenformatoelectrónicoparaescenarios de retención o auditoría.|
||_Funcionalidades DLP_|Usar las funcionalidades de prevención de pérdida dedatos (DLP) avanzadas para identificar, supervisar yproteger la información sensible.|
||_Conservación local_|Usar la conservación local para prevenir la eliminación oedición de contenido mediante programación.|


**Centro Criptológico Nacional** 5


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**

### **1.3 PRERREQUISITOS PARA EL DESPLIEGUE MEDIANTE POWERSHELL**


PowerShell de Microsoft 365 permite gestionar y configurar SharePoint Online
desde la línea de comandos, con un usuario con derechos de administración. Consultar
la guía [CCN-STIC-885A - Guía de configuración segura para Office 365]

### **2. DESPLIEGUE DE SHAREPOINT ONLINE**


SharePoint Online no necesita instalación previa en el entorno on-premise del
cliente, ya que es un servicio on-line accesible desde Internet y alojado en el tenant de
Microsoft 365 de la organización. Utiliza la infraestructura de “Nube pública” referida
en la guía [823-Cloud Computing].


SharePoint Online, así como el conjunto de Microsoft 365, se encuentra englobado
en la categoría de servicio **SaaS** (Software as a Service). El CSP (Microsoft) es el
encargado de ofrecer al cliente el software como un servicio.

### **2.1 ADMINISTRADOR – CONFIGURACIÓN INICIAL**


El usuario _administrador_ podrá acceder al portal de administración de SharePoint
Online a través del portal de administración de Microsoft 365
[(https://admin.microsoft.com).](https://admin.microsoft.com/)


**Centro Criptológico Nacional** 6



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-5-0.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


En el menú [Configuración] se puede controlar qué características están disponibles
para los usuarios de la organización tanto a nivel de OneDrive, Stream y SharePoint.


**Creación de sitios**


Permite elegir la ubicación de los _sites_ de grupo
de la organización.


Configurar la zona horaria.


Activar o desactivar la creación de sitios por
parte de los usuarios.


*Recomendación: elegir la zona horaria
adecuada y dejar resto de valores por defecto.


**Centro Criptológico Nacional** 7



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-6-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-6-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-6-2.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


**Límites de almacenamiento del sitio**


_Automático_ para compartir el
almacenamiento entre todos
los sitios.


_Manual_ : establecer límites
específicos para cada sitio.


*Recomendación: dejar valor
por defecto. No afecta a la
seguridad.


**Notificaciones**


Para **permitir las notificaciones**
**en las aplicaciones móviles**
relacionadas con SharePoint.


*Recomendación: dejar valor
por defecto. No afecta a la
seguridad.


**Sincronizar**


Para **controlar la sincronización**
**de archivos en OneDrive y**
**SharePoint.**


*Recomendación: dejar valor
por defecto.


**Retención**


Para **controlar la retención**
**predeterminada en OneDrive**
**cuando se elimina una cuenta**
**de usuario.**


*Recomendación: dejar valor
por defecto.


**Centro Criptológico Nacional** 8



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-7-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-7-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-7-2.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-7-3.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**

### **2.2 USUARIO FINAL – PRIMEROS PASOS**


Pulsando en el icono de la parte superior izquierda de la pantalla y pulsando en
el icono de SharePoint se podrá acceder al portal de SharePoint.


La pantalla de inicio de SharePoint Online se encuentra dividida en dos secciones:

      - Menú lateral izquierdo. Con opciones de búsqueda, sitios que se siguen y sitios
recientes.

      - Panel principal. Para crear sitios y noticias y visualizar sitios frecuentes.


**Centro Criptológico Nacional** 9



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-8-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-8-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-8-2.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**

#### **2.2.1 CREAR UN SITIO**


Pulsando el botón “Crear sitio” del
panel principal, se despliegan dos
opciones:


      - **Sitio de comunicación** : para difundir información, compartir noticias, informes,
estados, etc. a una audiencia amplia en un formato visualmente atractivo. Sólo
genera contenido un pequeño conjunto de miembros y es un público mucho
mayor quien lo consulta.

      - **Sitio de grupo** : proporciona una ubicación concreta en la que un grupo de
personas pueden trabajar en un proyecto concreto y compartir información
desde cualquier lugar con cualquier dispositivo. Son grupos cerrados, la
información se limita sólo a los miembros del grupo o participantes específicos.

Adicionalmente, desde el _Centro de administración de SharePoint_ se muestran otras
opciones desde el botón “Examinar más sitios”, donde poder crear un sitio de grupo
sin un grupo de Microsoft 365, o bien un centro de documentos, una wiki empresarial,
un portal de publicación, centro de contenidos y más plantillas adicionales.


**Centro Criptológico Nacional** 10



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-9-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-9-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


**2.2.1.1** **CREAR UN SITIO DE GRUPO**


1. Se puede seleccionar una plantilla de las que proporciona Microsoft o una

plantilla de la propia organización.


2. Las características de la plantilla seleccionada pueden ser visualizadas y

proceder a pulsar sobre el botón ‘Usar plantilla’.


3. Agregar nombre del sitio, descripción y propietario del grupo.


**Centro Criptológico Nacional** 11



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-10-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-10-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


4. En este punto es donde se decide si el sitio va a ser público (accesible por

cualquier persona de la organización- útil para contenido genérico) o privado
(sólo los miembros pueden acceder).


5. Agregar miembros o más propietarios.


**Centro Criptológico Nacional** 12



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-11-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-11-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


6. Al pulsar el botón “Finalizar” se crea el sitio de grupo y se navega a la página del

sitio recién creado.


7. Los siguientes pasos para el usuario podrían ser:


**Centro Criptológico Nacional** 13



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-12-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-12-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


                    - Personalizar el sitio


                    - Invitar miembros


                    - Cargar archivos en el sitio


                    - Publicar noticias


                    - Agregar chat en Teams


                    - Cambiar aspecto


**2.2.1.2** **CREAR UN SITIO DE COMUNICACIÓN**


1. Se puede seleccionar una plantilla de las que proporciona Microsoft o una

plantilla de la propia organización.


**Centro Criptológico Nacional** 14



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-13-0.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


2. Las características de la plantilla seleccionada pueden ser visualizadas y

proceder a pulsar sobre el botón ‘Usar plantilla’:


3. Agregar nombre del sitio, descripción y propietario del grupo.


**Centro Criptológico Nacional** 15



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-14-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-14-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


4. Establecemos idioma y otras opciones.


5. Al pulsar “Crear sitio”, se crea el _sitio de comunicación_ .


**Centro Criptológico Nacional** 16



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-15-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-15-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**

### **3. CONFIGURACIÓN DE SHAREPOINT ONLINE**


A continuación, se abordará la configuración del servicio SharePoint Online
centrándose en el cumplimiento de los requisitos del Esquema Nacional de Seguridad
(ENS) establecidas en el BOE-A-2022-7191 Real Decreto 311/2022, de 3 de mayo que
aplican exclusivamente a este servicio:


[https://www.boe.es/diario_boe/txt.php?id=BOE-A-2022-7191](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2022-7191)

### **3.1 MARCO OPERACIONAL**

#### **3.1.1 CONTROL DE ACCESO**


El control de acceso comprende el conjunto de actividades preparatorias y
ejecutivas tendentes a permitir o denegar a una entidad, usuario o proceso, el acceso a
un recurso del sistema para la realización de una acción concreta.


**Microsoft Entra ID** es la herramienta principal para la gestión de accesos y
privilegios sobre los recursos de Azure dentro de una organización. Al ser **SharePoint**
**Online** un recurso de Azure, el proveedor de identidad será **Microsoft Entra ID** .


Si bien esta guía trata únicamente la gestión de cuentas de usuarios en nube
Microsoft Entra ID, también permite configuraciones hibridas. Se puede consultar la
documentación de identidades hibridas en el enlace:


[https://docs.microsoft.com/es-es/azure/active-directory/hybrid/index](https://docs.microsoft.com/es-es/azure/active-directory/hybrid/index)

Para cumplir con los requisitos exigidos dentro del ámbito del ENS, se recomienda
consultar la guía [CCN-STIC-884A Guía de Configuración segura para Azure].


**3.1.1.1** **IDENTIFICACIÓN**


La gestión de identidades de SharePoint Online es común a todas las aplicaciones de
la solución Microsoft 365 y se describe en la guía [CCN-STIC-885A - Guía de
configuración segura para Office 365].


**3.1.1.2** **REQUISITOS DE ACCESO**


SharePoint Online establece un conjunto de _niveles de permisos_ para proteger el
acceso a los recursos.


**El modelo de objetos en SharePoint Online**


SharePoint proporciona distintas alternativas para controlar el acceso a los objetos:

      - Los objetos pueden usar, bien los mismos permisos que el sitio web, la lista o la
carpeta primarios al heredar tanto los roles como los usuarios disponibles en el
objeto primario, o bien permisos únicos.


**Centro Criptológico Nacional** 17


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


      - SharePoint incluye los cuatro grupos siguientes de forma predeterminada, con
un nivel de permisos asociado:

              - **Administradores:** Tienen los mismos permisos de Control total que el
propietario de un sitio, y pueden realizar acciones como administrar la
búsqueda, la papelera de reciclaje y las características de la colección de
sitios. También tienen acceso a todos los elementos del sitio, incluidos
los subsitios, aún si se ha roto la herencia de permisos.

              - **Propietarios:** Tienen un control total del sitio de SharePoint. Si el sitio
tiene un grupo o equipo de Microsoft 365 asociado, los propietarios del
grupo o del equipo se incluyen automáticamente como propietarios del
sitio.

              - **Miembros** : Tienen permisos de edición para el sitio de SharePoint y
pueden agregar y quitar archivos, listas y bibliotecas. Si el sitio tiene un
grupo o equipo de Microsoft 365 asociado, los miembros del grupo o
del equipo se incluyen automáticamente como miembros del sitio

              - **Visitantes:** Tienen permisos de solo vista para el sitio de SharePoint.
Este nivel de permisos solo se usa en SharePoint y no está relacionado
con los permisos de un grupo o equipo de Microsoft 365 asociado.


Estos grupos son independientes de los grupos de Microsoft 365 y Microsoft
Entra ID (anteriormente conocido como Azure Active Directory) y constituyen la
base para asignar permisos a los recursos del sitio.


Cuando se crea un sitio web con permisos únicos (no heredados del sitio _padre_ )
con la interfaz de usuario, se navega a una página donde puede asignar
usuarios a estos grupos como parte del aprovisionamiento del sitio. Ver
apartado [2.2 Usuario final - primeros pasos] y [3.1.1.4 Proceso de gestión de
derechos de acceso].


**Agregar un nuevo propietario a un sitio de grupo desde el** _**Centro de administración**_
_**de SharePoint**_


Como administrador de SharePoint es posible asignar nuevos _propietarios (owners)_
a un sitio. Esta opción es interesante si se desea compartir tareas de administración.


1. Desde el _Centro de administración de SharePoint_, menú [Sitios\Sitios activos] y

accediendo a las propiedades del sitio seleccionado. Pulsar sobre la pestaña
“Pertenencia” y después sobre “Propietarios del sitio”:


**Centro Criptológico Nacional** 18


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


2. Pulsar sobre “Agregar propietarios de sitio”.


Para agregar un nuevo propietario basta con escribir el
nombre o la dirección de correo electrónico y pulsar
sobre el botón “Agregar”.


Para eliminar un
propietarios seleccionar al
usuario o usuarios y pulsar
sobre el botón “Quitar
como propietario del
sitio”.

Siempre debe existir al menos un propietario del sitio. Al agregar o quitar usuarios
de un sitio de grupo, se agregan o eliminan también del grupo de Microsoft 365,
Exchange Online, Teams, etc.


Para **proporcionar o restringir el acceso** de los usuarios a un sitio SharePoint
consultar el apartado [3.1.1.4 Proceso de gestión de derechos de acceso].


**Centro Criptológico Nacional** 19



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-18-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-18-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-18-2.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


**3.1.1.3** **SEGREGACIÓN DE FUNCIONES Y TAREAS**


**Rol de administrador**


Los administradores globales de Microsoft 365 pueden asignar usuarios al **rol de**
**administrador de SharePoint** para ayudarle con la administración de SharePoint
Online. Se recomienda establecer un administrador para cada servicio de la solución de
Microsoft 365. En aquellas organizaciones donde exista una delegación de tareas de
administración se requiere establecer un administrador por cada servicio delegado.


1. Abrir el C _entro de administración de Microsoft 365_, menú [Usuarios\Usuarios

activos], y pulsar sobre el nombre del usuario. En la ventana emergente, pulsar
sobre el enlace “Administrar roles”.


2. Pulsar sobre el nombre del usuario y, en el panel derecho de propiedades, pulsar el

enlace “Administrar roles”:


Puede ser interesante asociar, junto con
el rol de administrador de SharePoint, la
función de **administrador de soporte**
**técnico de servicio** . De esta forma, puede
ver información relacionada con el
servicio en el C _entro de administración de_
_Microsoft_ _365_ : crear y administrar
solicitudes de soporte técnico con
Microsoft relativas a servicios de Azure y
Microsoft 365, consultar el centro de
mensajes y el panel de servicios de Azure
Portal y el Centro de administración de
Microsoft 365.

Los usuarios a los que se ha asignado el
rol de administrador de SharePoint tienen


**Centro Criptológico Nacional** 20



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-19-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-19-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


acceso al centro de administración de SharePoint y pueden crear y administrar
colecciones de sitios, designar administradores de colecciones de sitios, administrar
perfiles de usuario, la configuración global de SharePoint y mucho más.


Más información sobre roles en la guía [CCN-STIC-885A - Guía de configuración
segura para Office 365]


**3.1.1.4** **PROCESO DE GESTIÓN DE DERECHOS DE ACCESO**


**Configurar permisos del sitio por un propietario**


Después de crear un sitio de SharePoint, **se debe** **proporcionar o restringir el**
**acceso** de los usuarios al sitio o a su contenido. Por ejemplo, puede proporcionarse
acceso solo a los miembros de un equipo, o bien a todos los usuarios, pero restringir la
edición para algunos. La manera más sencilla de trabajar con permisos es usar los
niveles de permisos y grupos predeterminados ofrecidos, que abarcan los escenarios
más comunes.


1. Desde el menú de configuración del sitio del portal de usuario de SharePoint, en la

esquina superior derecha, se accede a los permisos del sitio

[Configuración\Permisos del sitio]:


2. Desde aquí, un propietario puede invitar a nuevas personas y gestionar su nivel de

permisos: propietarios del sitio (control total del contenido del sitio), miembros del
sitio (control limitado, puede editar y ver el contenido del sitio), visitante (sin
control, puede ver el contenido del sitio).


**Centro Criptológico Nacional** 21



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-20-0.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


3. Pinchar sobre el enlace “Configuración de permisos avanzada”, para un control

más exhaustivo de los permisos a aplicar.


4. Pulsando sobre cada uno de los grupos de SharePoint se accede a una gestión

detallada, donde es posible añadir nuevos usuarios al grupo y administrar otras
opciones de configuración.


**Centro Criptológico Nacional** 22



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-21-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-21-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-21-2.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


**Niveles de permisos**


Dentro de la “Configuración de permisos avanzada”, en la pestaña “PERMISOS”,
pulsar el vínculo “Niveles de Permisos”.


Un _**nivel de permisos**_ es un conjunto de _permisos_ . En este sentido, SharePoint
cuenta con _niveles de permisos predeterminados_ que permiten proporcionar de forma
rápida y sencilla niveles de permisos comunes para un usuario o grupos de usuarios.


Se puede realizar cambios en cualquiera de los niveles de permisos
predeterminados, excepto _Control total_ y _Acceso limitado_ .


Puede resultar conveniente establecer _niveles de permisos personalizados_ para
crear nuevos roles y adaptarlos a las necesidades de cada organización. Por ejemplo,
un usuario con permisos para agregar documentos pero no eliminarlos.


1. Pulsar el enlace “Agregar un nivel de permisos”.


**Centro Criptológico Nacional** 23



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-22-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-22-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-22-2.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-22-3.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


2. Asignar nombre y descripción, y la lista de permisos adecuada.


**Configuración de solicitud de acceso**


Es recomendable indicar cómo se configura el comportamiento para solicitar acceso
a un sitio. Desde el punto de vista de la seguridad, se puede bloquear el que un usuario
comparta el sitio o contenidos con otros usuarios o enviar invitaciones al grupo
miembros del sitio. Estos detalles son importantes para evitar fuga de información sin
control. Esta configuración es independiente del “Directivas de uso compartido”,
indicado en el punto 5.3.


Dentro de la “Configuración de permisos avanzada”, en la pestaña “PERMISOS”,
pulsar el vínculo “Configuración de solicitud de acceso”.


Desde esta pantalla se elige quién puede solicitar acceso o invitar a otros a este sitio.


**Centro Criptológico Nacional** 24



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-23-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-23-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-23-2.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


**3.1.1.5** **MECANISMOS DE AUTENTICACIÓN (USUARIOS EXTERNOS)**


Los mecanismos de autenticación de SharePoint Online son comunes a todas las
aplicaciones de la solución Microsoft 365 y se describen en la guía [CCN-STIC-885A Guía de configuración segura para Office 365].


Información sobre políticas de contraseñas, autenticación MFA y otros aspectos
relacionados con la autenticación se describen en la guía [CCN-STIC-885A - Guía de
configuración segura para Office 365].


En el siguiente diagrama se describe el **proceso de autenticación de SharePoint**
**Online:**

Se explica cómo funciona el escenario con el IdP ( _Identity Provider_ ) predeterminado
de Microsoft Entra ID.


La cookie de _autenticación de Federación_
(FedAuth) es para cada sitio de alto nivel de
SharePoint Online, como el sitio raíz, _mySite_ y el
sitio de administración. La cookie de _autenticación_
_de Federación raíz_ (rtFA) se usa en todos los
SharePoint Online. Cuando un usuario visita un
nuevo sitio de alto nivel o la página de otra
empresa, la cookie rtFA se usa para autenticarlas
en modo silencioso sin que se le pregunte.
Cuando un usuario cierra sesión en SharePoint
Online, se elimina la cookie rtFA.


**Sesión y cookies persistentes**


De forma predeterminada, todas las cookies de SharePoint Online son **cookies de**
**sesión** . Estas cookies no se guardan en la caché de cookies del explorador y, en su
lugar, se eliminan siempre que se cierra el explorador.


Microsoft Entra ID muestra durante el inicio de sesión un _check:_ “mantener la sesión
iniciada” para habilitar las **cookies persistentes** . Estas cookies se guardan en la
memoria caché del explorador y se conservan, aunque el explorador se cierre o reinicie
el equipo.


Ante la pregunta: ¿Quiere
mantener la sesión iniciada?
Responder: No.


**Centro Criptológico Nacional** 25



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-24-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-24-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-24-2.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


**Se deben mantener deshabilitadas las cookies persistentes** de inicio de sesión para
evitar que se mantenga la sesión iniciada una vez se cierra el navegador y de esta
forma forzar al usuario a reautenticarse siempre que utilice el servicio. Esta opción no
es configurable a nivel de administración y por tanto es responsabilidad del usuario su
cumplimiento.


**Cierre de sesión inactiva**

Conviene advertir y después cerrar la sesión de los usuarios en dispositivos no
administrados después de un período de inactividad. Esta configuración se aplica
cuando los usuarios no seleccionan mantener la sesión iniciada.


Se accede desde el _Centro_ _de_ _administración_ _de_ _SharePoint_, menú

[Directivas\Control de acceso\Cierre de sesión inactiva].


**Aplicaciones que no usan la autenticación moderna**

Algunas aplicaciones de terceros y versiones anteriores de Office no pueden
imponer restricciones basadas en dispositivos. Conviene bloquear los accesos de estas
aplicaciones.


Se accede desde el _Centro_ _de_ _administración_ _de_ _SharePoint_, menú

[Directiva\Control de acceso\Aplicaciones que no usan la autenticación moderna].


**Centro Criptológico Nacional** 26



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-25-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-25-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


Se requiere establecer un “doble factor de autenticación” (MFA), tener una política
adecuada de gestión de credenciales y políticas de acceso condicional. Así mismo, se
requiere un registro de intentos de accesos con éxito y fallidos al sistema, descritos en
el apartado [3.1.2.3 Registro de actividad]. Adicionalmente se puede controlar el
acceso a Microsoft 365 mediante directivas de acceso condicional o reglas en AD FS,
como se describe en la guía [CCN-STIC-884A - Guía de configuración segura para
Azure].


**3.1.1.6** **MECANISMOS DE AUTENTICACIÓN (USUARIOS DE LA ORGANIZACIÓN)**


Ídem que el apartado anterior.

#### **3.1.2 EXPLOTACIÓN**


_SharePoint Online_ **siempre estará actualizado** . Es decir, el servicio es mantenido
permanentemente por Microsoft, encargándose de las actualizaciones y parches, así
como de establecer los mecanismos de detección y protección ante amenazas.


**3.1.2.1** **PROTECCIÓN FRENTE A CÓDIGO DAÑINO**


Si la organización dispone de _Microsoft Defender para Office 365_ tendrá un
explorador de detecciones en tiempo real, accesible desde el _Centro de Seguridad y_
_cumplimiento de Office 365_ . Consultar la guía [CCN-STIC-885A - Guía de configuración
segura para Office 365].


Si además se dispone de Exchange Online, se proporciona automáticamente
protección contra malware para los archivos que se cargan y guardan en bibliotecas de
documentos. Esta protección la proporciona el motor antimalware de Microsoft que
también está integrado en Exchange.


**Permitir o bloquear scripts personalizados**


Permitir que los usuarios personalicen sitios y páginas en SharePoint mediante la
inserción de una secuencia de comandos puede dar la flexibilidad necesaria para
satisfacer las distintas necesidades de la organización. Sin embargo, debe tenerse en
cuenta las implicaciones de seguridad de los scripts personalizados.


Cuando se permite a los usuarios ejecutar scripts personalizados, ya no se puede
exigir la gobernanza, el ámbito de las capacidades del código insertado. En lugar de
permitir un script personalizado, se recomienda usar _SharePoint Framework_ . Todos los
scripts que se ejecutan en una página de SharePoint (ya sea una página HTML en una
biblioteca de documentos o un JavaScript en un elemento Web de editor de scripts)
siempre se ejecutan en el contexto del usuario que visita la página y la aplicación de
SharePoint.


Una vez que permita el scripting, no se podrá identificar:


**Centro Criptológico Nacional** 27


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


      - Qué código se ha insertado.

      - Dónde se ha insertado el código.

      - Quién insertó el código.

Si se insertó un script peligroso o malintencionado, la única forma de detenerlo es
eliminar la página que lo hospeda. Esto puede provocar la pérdida de datos.


Para permitir o bloquear scripts personalizados:


1. Acceder al Centro de administración de SharePoint, menú [Configuración], y

acceder al link de la parte inferior de la página “ _página de configuración clásica_ ”.


2. En la pantalla de configuración, navegar a la sección de “Script personalizado” y

establecer los valores deseados.


**3.1.2.2** **GESTIÓN DE INCIDENTES**


Ver apartado [3.1.2.1 Protección frente a código dañino] de la guía [CCN-STIC-885A

     - Guía de configuración segura para Office 365] donde se explica cómo acceder a los
informes de “Administración de Amenazas”.


**3.1.2.3** **REGISTRO DE LA ACTIVIDAD**


Para configurar el registro de actividad del servicio de SharePoint, será necesario
hacer uso de la funcionalidad de Auditoría disponible a través del portal de Microsoft
Purview, anteriormente conocido como _Centro de Seguridad y cumplimiento de Office_


**Centro Criptológico Nacional** 28



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-27-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-27-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


_365_ . Más información en la guía [CCN-STIC-885A - Guía de configuración segura para
Office 365].


Mencionar además que existen muchas actividades relacionadas con Teams en el
registro de auditoría, accesibles desde el portal de Microsoft Purview, en el menú

[Auditar/Nueva búsqueda]:

#### **3.1.3 MONITORIZACIÓN DEL SISTEMA**


Consultar la guía [CCN-STIC-885A - Guía de configuración segura para Office 365]
para ver los distintos mecanismos de monitorización del servicio.


Conviene destacar que, a nivel de configuración de directivas de alertas, existen
muchas actividades relacionadas con los sitios y objetos almacenados en SharePoint de
manera predeterminada. Aunque dichas directivas están en desuso en función de los
comentarios de los clientes como falsos positivos. Para conservar la funcionalidad de
estas directivas de alerta, se pueden crear directivas de alerta personalizadas con la
misma o distinta configuración. Reseñamos la que aún está en vigor:

      - Volumen inusual de uso compartido de archivos externos. Genera una alerta
cuando se comparte un número inusualmente grande de archivos en
SharePoint o OneDrive con usuarios fuera de la organización. Esta directiva
tiene una configuración de gravedad media.

### **3.2 MEDIDAS DE PROTECCIÓN**

#### **3.2.1 PROTECCIÓN DE LAS COMUNICACIONES**


En cuanto a la protección de las comunicaciones, cabe reseñar que se usan los
protocolos criptográficos para conexiones TLS, integrados en Microsoft 365 de manera
automática (Todas las conexiones SSL se establecen con claves de 2048 bits). Esto es
así cuando:


**Centro Criptológico Nacional** 29



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-28-0.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


      - Los usuarios trabajan con archivos guardados en _OneDrive for Business_       SharePoint Online.

      - Los usuarios comparten archivos en reuniones en línea y conversaciones de
mensajería instantánea.


En realidad, todas las comunicaciones de Microsoft 365 están cifradas: Clientes de
correo (POP, IMAP, SMTP-TLS), Clientes Outlook (MAPI-HTTPS), Navegadores (Web
HTTPS), Dispositivos móviles (ActiveSync HTTPS), Teams y Skype (SIP-TLS). No es
necesario realizar ninguna configuración adicional, pero es importante indicar que, a
partir de junio 2020, se eliminó soporte de TLS 1.0 y 1.1. Esto tiene implicaciones
directas en los clientes.

#### **3.2.2 PROTECCIÓN DE LA INFORMACIÓN**


**3.2.2.1** **CALIFICACIÓN DE LA INFORMACIÓN**


Microsoft 365 cuenta con diversos mecanismos para calificar la información, como
se explican en el apartado [3.2.2.1 Calificación de la información] de la guía [CCN-STIC885A - Guía de configuración segura para Office 365]. A continuación se describen
varios desde el punto de vista de SharePoint Online.


3.2.2.1.1 ETIQUETAS DE RETENCIÓN

Se puede definir el tiempo que un documento debe retenerse, o el tiempo después
del cual debe borrarse. Más información sobre la **creación** de etiquetas de retención
en la guía [CCN-STIC-885A - Guía de configuración segura para Office 365].


1. Para aplicar una directiva de retención en un documento, navegar por el panel

derecho de propiedades del documento, y seleccionar la opción “Aplicar
etiqueta de retención”:


2. Se muestra un desplegable para seleccionar la etiqueta de retención a aplicar al

documento.


**Centro Criptológico Nacional** 30



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-29-0.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


Es posible seleccionar varios documentos a la
vez y aplicar “en masa” la etiqueta.


Si, por ejemplo, se ha aplicado una etiqueta de
retención de un documento que impida su
borrado durante 5 años al intentar eliminar el
documento aparecerá este mensaje.


3.2.2.1.2 SENSITIVITY LABELS

Esta característica está disponible en las aplicaciones de escritorio de Windows y
Web (Word, Excel, PowerPoint y Outlook), así como en aplicaciones de otras
plataformas (Mac, iOS y Android).


**¿Cómo se usan las sensitivity labels desde un documento?**


A fecha de edición de esta guía, ya no es necesario la instalación de ningún
complemento para usar esta característica. Dicha característica está integrada
directamente en las aplicaciones de Office (Word, Excel PowerPoint y Outlook) y el
complemento que anteriormente era necesario instalarse ha sido deprecado con fecha
de abril de 2024. Se deberá implementar una edición de suscripción de Office (ahora
denominada Microsoft 365 Apps), ya que el etiquetado integrado no está disponible
con las ediciones independientes de Office (a veces denominadas "Office Perpetual").


En las aplicaciones de Office está el icono:


1. En la pestaña Inicio, seleccionar el botón “Sensitivity”.


Importante: La _confidencialidad_ no está visible si la cuenta de Office no es una
cuenta profesional con al menos licencia de Office 365 E3/E5 asignada, si el
administrador no ha configurado _etiquetas de confidencialidad_ y ha habilitado la
característica.


2. Elegir la _sensitivity label_ que se aplicará en el documento.


**Centro Criptológico Nacional** 31



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-30-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-30-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-30-2.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-30-3.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


Para quitar una etiqueta que ya se ha aplicado al
documento, anular la selección en el menú.


**¿Qué sucede al aplicar una** _**sensitivity label**_ **a un documento?**


Al aplicar una _sensitivity label_, la información de la etiqueta se conservará con el
documento o correo electrónico, incluso a medida que se comparte entre dispositivos,
aplicaciones y servicios en la nube. Al aplicar una _sensitivity label_ también se pueden
producir cambios en el documento o correo electrónico según la configuración de la
organización, por ejemplo:

      - El cifrado con _Azure Rights Management_ se puede aplicar al correo electrónico,
invitaciones de reuniones o documentos.

      - Puede aparecer un encabezado o pie de página en el documento o correo
electrónico.

      - Puede aparecer una marca de agua en el documento


**3.2.2.2** **LIMPIEZA DE DOCUMENTOS**


Al compartir una copia electrónica de determinados documentos de Microsoft 365

     - al exponer cierta documentación en Internet, es una buena práctica revisar el
documento en busca de datos ocultos, información personal y en general cualquier
metadato que pudiera estar asociado. Es posible eliminar esta información a través del
Inspector de documentos, característica que se accede desde las propias aplicaciones
de Word, Excel, PowerPoint o Visio.


**3.2.2.3** **COPIAS DE SEGURIDAD**


No existe una solución global de respaldo de Microsoft 365. A fecha de edición de
esta guía, nos encontramos con que a finales del año 2024 Microsoft tiene previsto
sacar a disposición general un nuevo servicio llamado _Microsoft 365 Backup._ Dicho
servicio será en modalidad de pago por uso y necesitará de una suscripción de Azure y
un grupo de recursos.


**Centro Criptológico Nacional** 32



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-31-0.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


Aunque existen mecanismos relacionados que se describen en el apartado [5.
OTRAS CONSIDERACIONES DE SEGURIDAD] de la presente guía: control de versiones y
papelera de reciclaje.


Así mismo, un mecanismo basado en “políticas de retención” en ciertos casos
puede resultar suficiente para garantizar el respaldo de la información. Consultar el
apartado [3.2.2.1 Calificación de la información] para ver cómo se aplican a un
documento y cómo puede servir para protegerlo de ser eliminado.


**3.2.2.4** **DIRECTIVAS DE ADMINISTRACIÓN DE INFORMACIÓN**


Las _directivas de administración de información_ permiten controlar quién tiene
acceso a la información de la organización, qué se puede hacer con esta y cuánto
tiempo pueden conservarla. Una directiva puede ayudar a exigir el cumplimiento de
normativas gubernamentales y legales, o de procesos empresariales internos. El
administrador, puede configurar una directiva para controlar cómo realizar un
seguimiento de los documentos, quién tiene acceso a estos y cuánto tiempo pueden
conservarlos.


Se puede crear una _directiva de administración de información_ en un sitio de tres
maneras distintas:

      - Crear una _directiva de administración de información_ para usar en varios tipos
de contenido dentro de una colección de sitios.

      - Crear una _directiva de administración de información_ para un tipo de contenido
de sitio.

      - Crear una _directiva de administración de información_ para una lista o
biblioteca.


A continuación se describe cómo crear una _directiva de administración de_
_información_ para un tipo de contenido de sitio, el resto se realiza de forma análoga.
[Más información.](https://support.office.com/es-es/article/crear-y-aplicar-directivas-de-administraci%C3%B3n-de-informaci%C3%B3n-eb501fe9-2ef6-4150-945a-65a6451ee9e9)


**Crear una directiva de administración de información para un tipo de contenido de**
**sitio**


1. Acceder a la página principal del sitio, pulsar el icono “Configuración” y seleccionar

el enlace “Información del sitio”.


**Centro Criptológico Nacional** 33



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-32-0.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


2. Seleccionar “Ver todas las opciones de configuración del sitio”:


3. En “Configuración del sitio”, seleccionar “Características de colección de sitios”.


4. En la pantalla de características del sitio, navegar hasta “Directiva del sitio”, y

activarlo.


**Centro Criptológico Nacional** 34



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-33-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-33-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


5. Volver a la pantalla de “Configuración del sitio” y pulsar el nuevo enlace
“Directivas de sitio”.


6. En la pantalla de “Directivas del sitio” pulsar el botón “Crear”.


7. Establecer la política de retención adecuada.


**Centro Criptológico Nacional** 35



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-34-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-34-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-34-2.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


**3.2.2.5** **EVITAR QUE UNA BIBLIOTECA SE MUESTRA EN LOS RESULTADOS DE**

**BÚSQUEDA**


De forma predeterminada todas las bibliotecas se indizan en el buscador. Si alguna de
ellas tiene contenido sensible se puede evitar que aparezca en los resultados.


1. Abrir la configuración de la biblioteca, opción [Configuración avanzada].


2. Desactivar la búsqueda.


**3.2.2.6** **EVITAR QUE LOS ELEMENTOS SE DESCARGUEN EN CLIENTES SIN CONEXIÓN**


Si una biblioteca incluye información sensible, se puede evitar que se sincronice con
clientes sin conexión como OneDrive.


**Centro Criptológico Nacional** 36



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-35-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-35-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-35-2.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


1. Abrir la configuración de la biblioteca, opción [Configuración avanzada].


2. Bloquear que los elementos de esta biblioteca de documentos puedan descargarse

a los clientes sin conexión.

#### **3.2.3 PROTECCIÓN DE LOS SERVICIOS**


**3.2.3.1** **PROTECCIÓN FRENTE A LA DENEGACIÓN DE SERVICIO**


Microsoft 365 ofrece un sistema avanzado de **detección de amenazas** y **sistemas de**
**mitigación** para proteger la infraestructura subyacente de los ataques de _denegación_
_de servicio_ (DoS) y prevenir la interrupción de servicio a los clientes.


El sistema de defensa DDoS de Azure está diseñado no solo para resistir ataques
desde el exterior, sino también desde otros _Tenants_ de Azure. Los mecanismos de
limitación de peticiones de Exchange Online y SharePoint Online forman parte de un
enfoque de varias capas para defenderse contra ataques DoS.


Consultar la guía [CCN-STIC-884A - Guía de configuración segura para Azure] para
obtener más información sobre el _sistema de defensa DDoS de Azure._


**Centro Criptológico Nacional** 37



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-36-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-36-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**

### **4. SCRIPTS DE CONFIGURACIÓN**


Existen tareas de administración que pueden realizarse de manera más ágil a través
del módulo de PowerShell “SharePoint Online Management Shell”. Este módulo se
utiliza para administrar usuarios, sitios y colecciones de sitios. Todos los _cmdlets_ del
módulo comienzan con el prefijo SPO.


Los requerimientos mínimos de instalación en cuanto a Sistema operativo compatible:

```
      Windows 11; Windows 10; Windows 7 Service Pack 1; Windows 8; Windows Server 2008 R2 SP1; Windows
      Server 2008 Service Pack 2; Windows Server 2012; Windows Server 2016

```

Y la versión de PowerShell 3.0.


1. Comprobar si ya tenemos el módulo instalado, y si no, instalarlo.

```
        Get-Module -Name Microsoft.Online.SharePoint.PowerShell -ListAvailable | Select Name,Version

|Para instalarlo:|Col2|Col3|
|---|---|---|
|`Install-Module -Name Microsoft.Online.SharePoint.PowerShell`2. Conectarse. 2.1. Con usuario y password:`$adminUPN="`ejemplo: jdoe@contosotoycompany.onmicrosoft.com&gt;"``$orgName=""``$userCredential = Get-Credential -UserName $adminUPN -Message "Type the password."``Connect-SPOService -Url https://$orgName-admin.sharepoint.com -Credential $userCredential.`2.2. Con MFA:`$orgName="&lt;` `Nombre de la organización de Microsoft 365, ejemplo: contosotoycompany&gt;"``Connect-SPOService -Url https://$orgName-admin.sharepoint.com`|2. Conectarse. 2.1. Con usuario y password:`$adminUPN="`ejemplo: jdoe@contosotoycompany.onmicrosoft.com&gt;"``$orgName=""``$userCredential = Get-Credential -UserName $adminUPN -Message "Type the password."``Connect-SPOService -Url https://$orgName-admin.sharepoint.com -Credential $userCredential.`2.2. Con MFA:`$orgName="&lt;` `Nombre de la organización de Microsoft 365, ejemplo: contosotoycompany&gt;"``Connect-SPOService -Url https://$orgName-admin.sharepoint.com`|2. Conectarse. 2.1. Con usuario y password:`$adminUPN="`ejemplo: jdoe@contosotoycompany.onmicrosoft.com&gt;"``$orgName=""``$userCredential = Get-Credential -UserName $adminUPN -Message "Type the password."``Connect-SPOService -Url https://$orgName-admin.sharepoint.com -Credential $userCredential.`2.2. Con MFA:`$orgName="&lt;` `Nombre de la organización de Microsoft 365, ejemplo: contosotoycompany&gt;"``Connect-SPOService -Url https://$orgName-admin.sharepoint.com`|
|`Install-Module -Name Microsoft.Online.SharePoint.PowerShell`2. Conectarse. 2.1. Con usuario y password:`$adminUPN="`ejemplo: jdoe@contosotoycompany.onmicrosoft.com&gt;"``$orgName=""``$userCredential = Get-Credential -UserName $adminUPN -Message "Type the password."``Connect-SPOService -Url https://$orgName-admin.sharepoint.com -Credential $userCredential.`2.2. Con MFA:`$orgName="&lt;` `Nombre de la organización de Microsoft 365, ejemplo: contosotoycompany&gt;"``Connect-SPOService -Url https://$orgName-admin.sharepoint.com`|`$orgName="&lt;` `Nombre de la organización de Microsoft 365, ejemplo: contosotoycompany&gt;"``Connect-SPOService -Url https://$orgName-admin.sharepoint.com`||


```

A continuación se muestran algunos ejemplos de cmdlets relacionados:


_Obtener todas las colecciones de sitios_

```
          Get-SPOSite

```

_Obtener información de una colección de sitio concreta_

```
          Get-SPOSite -Identity https://contoso.sharepoint.com

```

_Obtener información_ _**detallada**_ _de un sitio de grupo_

```
          Get-SPOSite -Identity https://contoso.sharepoint.com/sites/groupname -detailed |fl

```

_Deshabilitar la compartición de un sitio para los “no propietarios”_

```
          Get-SPOSite -Identity https://contoso.sharepoint.com -DisableSharingForNonOwnersStatus

```

**Centro Criptológico Nacional** 38


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**

### **5. OTRAS CONSIDERACIONES DE SEGURIDAD** **5.1 CONTROL DE VERSIONES**


Cuando el control de versiones está habilitado en la lista o biblioteca de SharePoint,
puede almacenar, hacer un seguimiento y restaurar elementos en una lista y archivos
de una biblioteca cada vez que cambien.


El control de versiones es, sin duda, una de las herramientas más útiles en
SharePoint: permite ver qué cambios se han producido en los documentos, mostrando
el número de versión y tamaño de cada documento, quién y cuándo realizó el último
cambio y ver y/o restaurar cualquier versión anterior.


**Habilitar y configurar las versiones para una lista o biblioteca**


1. Abrir la configuración de la biblioteca y pulsar enlace “Configuración de versiones”.


2. Configurar las opciones.


**Centro Criptológico Nacional** 39



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-38-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-38-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


**Consultar el historial de versiones**


1. Se accede a través del [menú de acciones] que aparece en la propia línea del

documento a consultar.


2. Se despliega a continuación todo el historial de versiones del documento:


**Centro Criptológico Nacional** 40



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-39-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-39-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


3. En cada _item_ del historial, en el campo “modificado”, se muestra un desplegable

con las acciones a realizar sobre esa versión concreta:

### **5.2 PAPELERA DE RECICLAJE**


SharePoint Online establece dos niveles de papelera de reciclaje con dos áreas de
almacenamiento independientes, cada una con un período de retención de la
información. A diferencia de versiones anteriores no es configurable.


**Nota:** Para documentos sensibles que exijan un borrado inmediato, es responsabilidad del
usuario su eliminación definitiva de todas las áreas de la papelera de reciclaje.


1. Cuando se eliminan elementos (incluidos los de _OneDrive for Business_ ) de un sitio

de SharePoint, se envían a la _papelera de reciclaje del sitio_, también denominada
_papelera de reciclaje de_ _**primer nivel**_, donde puede restaurarlos si es necesario.


2. Cuando se eliminan elementos de una papelera de reciclaje de un sitio, se envían a

la _papelera de reciclaje de la colección de sitios_, también denominada _papelera de_
_reciclaje de_ _**segundo nivel**_ .


**Centro Criptológico Nacional** 41



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-40-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-40-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-40-2.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


Un administrador de la colección de sitios de SharePoint puede ver y restaurar los
elementos eliminados de la papelera de reciclaje de la colección de sitios a su
ubicación original. Si se elimina un elemento de la papelera de reciclaje de la colección
de sitios, o se supera el tiempo de retención, se eliminará de forma permanente.


_¿Cuánto tiempo se conservan los elementos eliminados en la Papelera de reciclaje?_


En SharePoint Online, los elementos se conservan por **93 días** desde el momento en
que se eliminan de su ubicación original. Permanecen en la _papelera de reciclaje del_
_sitio_ todo el tiempo, a menos que alguien lo elimine o vacíe esa papelera de reciclaje.


**Centro Criptológico Nacional** 42



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-41-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-41-1.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


En ese caso, los elementos van a la _papelera de reciclaje de la colección de sitios_,
donde permanecen durante el resto de 93 días, a menos que:

      - la papelera de reciclaje de la colección de sitios supera su cuota y comienza a
purgar los elementos más antiguos.

      - el administrador de la colección de sitios elimina manualmente los elementos
de la papelera de reciclaje de la colección de sitios.

El almacenamiento de la _papelera de reciclaje del sitio_ cuenta con la cuota de
almacenamiento de la colección de sitios y el umbral de vista de lista. La cantidad de
espacio asignado a la papelera de reciclaje de la colección de sitios es 200% de la cuota
de la colección de sitios. Estos valores no se pueden configurar.


3. Tercer nivel de copia de seguridad.

SharePoint Online conserva las **copias de seguridad de todo el contenido durante**
**14 días adicionales** más allá de la eliminación real. Si el contenido no se puede
restaurar a través de la papelera de reciclaje o de la restauración de archivos, un
administrador puede ponerse en contacto con el soporte técnico de Microsoft para
solicitar una restauración en cualquier momento dentro de la ventana de 14 días.

### **5.3 DIRECTIVAS DE USO COMPARTIDO**


Los administradores globales y de SharePoint en Microsoft 365 pueden cambiar su
configuración de uso compartido de nivel de organización para SharePoint y OneDrive.


Para ello acceder al C _entro de administración de SharePoint Online:_


Los niveles establecidos son los siguientes:


**Centro Criptológico Nacional** 43



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-42-0.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**






|Invitados nuevos y existentes|Los invitados deben iniciar sesión o proporcionar un código deverificación.|
|---|---|
|**Invitados existentes**|Solo los invitados que ya forman parte del directorio de suorganización.|
|**Solo los miembros de su****organización**|No se permite ningún tipo de uso compartido externo.|



1. Seleccionar el nivel menos permisivo para no permitir el uso compartido

externo, es decir, **sólo se permitirá la compartición de documentos entre**
**miembros de la organización** .

2. A continuación, se elige la opción que les aparecerá a los usuarios de forma

predeterminada.


Así, por ejemplo, con esta opción a los usuarios les aparecerá al compartir un
documento lo siguiente:


3. Elegir tipo de vínculo.


4. Seleccionar otras opciones de configuración.


**Centro Criptológico Nacional** 44



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-43-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-43-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-43-2.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


5. Elegir “permiso de vínculo predeterminado”. Valor recomendado: _Ver_ .

### **5.4 BLOQUEAR LA INTEGRACIÓN CON YAMMER**


De forma predeterminada SharePoint Online habilita la integración con Yammer.
Esto se puede restringir. Esta integración reemplaza a _Newsfeed_ y cambia la
navegación global de Microsoft 365. Además, Yammer no es un servicio disponible
actualmente en el Centro de confianza de O365. Al habilitar la integración, Yammer
podrá leer y copiar el acceso a la información de usuario y de grupo de la empresa.


Se puede activar o desactivar Yammer para conversaciones en SharePoint desde el
_Centro de administración de SharePoint Online_ .


1. Iniciar la página de _configuración clásica_ .


2. En colaboración social empresarial, seleccionar “Utilizar SharePoint Newsfeed”.


**Centro Criptológico Nacional** 45



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-44-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-44-1.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-44-2.png)
**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**

### **6. GLOSARIO Y ABREVIATURAS**



A continuación de describen una serie de términos, acrónimos y abreviaturas en
materia de seguridad utilizados en esta guía:








|Término|Definición|
|---|---|
|**IRM**|_Information Rights Management._|
|**SPO**|_SharePoint Online_|
|**Sitio de SPO**|es un sitio web que ofrece un espacio central de colaboracióny almacenamiento de documentos, información e ideas.|
|**Sitio de****comunicación**|para difundir información, compartir noticias, informes,estados, etc. a una audiencia amplia en un formatovisualmente atractivo. Sólo genera contenido un pequeñoconjunto de miembros y es un público mucho mayor quien loconsulta.|
|**Sitio de grupo**|proporciona una ubicación concreta en la que un grupo depersonaspueden trabajar en un proyecto concreto y compartirinformación desde cualquier lugar con cualquier dispositivo.Son grupos cerrados, la información se limita sólo a losmiembros del grupo o participantes específicos.|
|**Sitio de grupo****público**|sitio de SPO accesible por cualquier persona de laorganización.|
|**Sitio de grupo****privado**|sitio de SPO sólo accesible por miembros del grupo.|



**Centro Criptológico Nacional** 46


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**

### 7. CUADRO RESUMEN DE MEDIDAS DE SEGURIDAD


Se facilita a continuación un cuadro resumen de configuraciones a aplicar para la protección del servicio, donde la organización podrá
valorar qué medidas de las propuestas se cumplen.














|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
|**op**|**Marco Operacional**|**Marco Operacional**|**Marco Operacional**|
|**op.acc**|**Control de Acceso**|**Control de Acceso**|**Control de Acceso**|
|**op.acc.1**|**Identificación**|**Identificación**|**Identificación**|
|**op.acc.1**|Se ha configurado el uso de cuentas y la asignación de licencias a usuarios.Siguiendo las recomendaciones de Office 365 basada en la guía [CCN-STIC-885A -Guía de configuración segura para Office 365]|SiNo**Aplica:**  |SiNo**Cumple:**|
|**op.acc.1**|Se ha configurado el uso de cuentas y la asignación de licencias a usuarios.Siguiendo las recomendaciones de Office 365 basada en la guía [CCN-STIC-885A -Guía de configuración segura para Office 365]|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**Op.acc.2**|**_Requisitos de Acceso_ **|**_Requisitos de Acceso_ **|**_Requisitos de Acceso_ **|



**Centro Criptológico Nacional** 47


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**




















|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
||Se han comprobado los_niveles de permisos_ para los recursos de laorganización: propietarios, miembros y visitantes.|SiNo**Aplica:**  |SiNo**Cumple:**|
||Se han comprobado los_niveles de permisos_ para los recursos de laorganización: propietarios, miembros y visitantes.|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**Op.acc.3**|**Segregación de funciones y tareas**|**Segregación de funciones y tareas**|**Segregación de funciones y tareas**|
|**Op.acc.3**|Se ha asignado adecuadamente el rol de Admin a un usuario administradorde SharePoint (en caso de que se haya establecido una delegación para esteservicio).|SiNo**Aplica:**  |SiNo**Cumple:**|
|**Op.acc.3**|Se ha asignado adecuadamente el rol de Admin a un usuario administradorde SharePoint (en caso de que se haya establecido una delegación para esteservicio).|SiNo**Evidencias Recogidas:** |**Observaciones:**|



**Centro Criptológico Nacional** 48


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**




















|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
|||||
|**Op.acc.4**|**Proceso de gestión de derechos de acceso**|**Proceso de gestión de derechos de acceso**|**Proceso de gestión de derechos de acceso**|
||Se han creado “niveles de permisos” específicos para la organización.|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se han creado “niveles de permisos” específicos para la organización.|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**Op.acc.5**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|
||Se ha informado a los usuarios que mantengan deshabilitadas las_cookies_ persistentesen el inicio de sesión.|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se ha informado a los usuarios que mantengan deshabilitadas las_cookies_ persistentesen el inicio de sesión.|~~No~~**Evidencias Recogidas:**|**Observaciones:**|



**Centro Criptológico Nacional** 49


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**















|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
|||||
|**Op.acc.5**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|
||Se ha configurado la advertencia y cierre de las sesiones de los usuariosdespués de un período de inactividad.|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se ha configurado la advertencia y cierre de las sesiones de los usuariosdespués de un período de inactividad.|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**Op.acc.5**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|
||Se ha bloqueado el acceso a aplicaciones que no usan la autenticaciónmoderna.|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se ha bloqueado el acceso a aplicaciones que no usan la autenticaciónmoderna.|**Evidencias Recogidas:**|**Observaciones:**|


**Centro Criptológico Nacional** 50


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**
















|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
|||SiNo  ||
|**Op.acc.5**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|
|**Op.acc.5**|Se encuentra habilitado el “doble factor de autenticación” y se dispone deuna adecuada política de gestión de credenciales.|SiNo**Aplica:**  |SiNo**Cumple:**|
|**Op.acc.5**|Se encuentra habilitado el “doble factor de autenticación” y se dispone deuna adecuada política de gestión de credenciales.|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**Op.acc.5**|**Mecanismo de autenticación (usuarios externos)**|||
||Se han configurado directivas de acceso condicional o reglas en AD FS, comose describe en la guía [CCN-STIC-885A - Guía de configuración segura paraOffice 365].|SiNo**Aplica:**  |SiNo**Cumple:** |



**Centro Criptológico Nacional** 51


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**
















|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
|||SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**Op.acc.5**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|
||Se ha activado la_Ubicación de red_ para permitir el acceso solo desdedeterminadas direcciones IP. Y la limitación de acceso a los administradores.|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se ha activado la_Ubicación de red_ para permitir el acceso solo desdedeterminadas direcciones IP. Y la limitación de acceso a los administradores.|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**Op.acc.5**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|**Mecanismo de autenticación (usuarios externos)**|
||Se han configurado directivas de acceso condicional para el acceso remoto,como se describe en la guía [CCN-STIC-885A - Guía de configuración segurapara Office 365].|SiNo**Aplica:** |SiNo**Cumple:** |



**Centro Criptológico Nacional** 52


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**







|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
|||||
|||SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**Op.acc.6**|**Mecanismo de autenticación (usuarios de la organización)**|**Mecanismo de autenticación (usuarios de la organización)**|**Mecanismo de autenticación (usuarios de la organización)**|
||Ídem controles aplicados a Op.acc.5|SiNo**Aplica:**  |SiNo**Cumple:** |
||Ídem controles aplicados a Op.acc.5|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**op.exp**|**Explotacion**|**Explotacion**|**Explotacion**|
|**op.exp.6**|**Protección frente a código dañino**|**Protección frente a código dañino**|**Protección frente a código dañino**|
|**op.exp.6**|Se ha bloqueado que los usuarios puedan ejecutar scripts personalizados en|**Aplica:**|**Cumple:**|


**Centro Criptológico Nacional** 53


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**














|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
||sitios personales y en sitios creados por ellos mismos.|SiNo  |SiNo |
||sitios personales y en sitios creados por ellos mismos.|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**op.exp.6**|**Protección frente a código dañino**|**Protección frente a código dañino**|**Protección frente a código dañino**|
||Se recomienda la detección de amenazas en tiempo real, accesible desde el_Centro de Seguridad y cumplimiento de Office 365_. *Para dichas tareas la organización debe dispone de_Microsoft Defender__para Office 365_. |SiNo**Aplica:**  |SiNo**Cumple:** |
||Se recomienda la detección de amenazas en tiempo real, accesible desde el_Centro de Seguridad y cumplimiento de Office 365_. *Para dichas tareas la organización debe dispone de_Microsoft Defender__para Office 365_. |SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**op.exp.8**|**Registro de la actividad**|**Registro de la actividad**|**Registro de la actividad**|



**Centro Criptológico Nacional** 54


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


















|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
||Se ha activado el registro de auditoría.|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se ha activado el registro de auditoría.|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**op.mon**|**Monitorización del sistema**|**Monitorización del sistema**|**Monitorización del sistema**|
||Se han configurado alertas en el_Centro de Seguridad y cumplimiento._|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se han configurado alertas en el_Centro de Seguridad y cumplimiento._|SiNo**Evidencias Recogidas:**  |**Observaciones:**|



**Centro Criptológico Nacional** 55


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**
















|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
|**mp**|**Medidas de Protección**|**Medidas de Protección**|**Medidas de Protección**|
|**mp.info**|**Protección de la información**|**Protección de la información**|**Protección de la información**|
|**mp.info.2**|**Calificación de la información**|**Calificación de la información**|**Calificación de la información**|
||Se han aplicado políticas de retención.|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se han aplicado políticas de retención.|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**mp.info.2**|**Calificación de la información**|**Calificación de la información**|**Calificación de la información**|
||Se han aplicado políticas de DLPs cómo se describe en el apartadoCalificación de la información de la guía [CCN-STIC-884A - Guía deconfiguración segura para Azure].|SiNo**Aplica:**  |SiNo**Cumple:** |



**Centro Criptológico Nacional** 56


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**















|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
|||SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**mp.info.2**|**Calificación de la información**|**Calificación de la información**|**Calificación de la información**|
||Se han aplicado_ sensitivity labels._|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se han aplicado_ sensitivity labels._|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**mp.info.2**|**Calificación de la información**|**Calificación de la información**|**Calificación de la información**|
||Se ha aplicado un cifrado especial mediante etiquetas de sensibilidad a sitiosde SharePoint que precisan una protección especial.|SiNo**Aplica:** |SiNo**Cumple:** |


**Centro Criptológico Nacional** 57


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**















|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
||* Microsoft cifra automáticamente los datos en reposo y de maneratransparente para el usuario. Para un cifrado adicional se pueden usar las_sensitivity labels_.|||
||* Microsoft cifra automáticamente los datos en reposo y de maneratransparente para el usuario. Para un cifrado adicional se pueden usar las_sensitivity labels_.|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**mp.info.5**|**Limpieza de documentos**|**Limpieza de documentos**|**Limpieza de documentos**|
||Se ha eliminado información personal y en general cualquier metadato quepudiera estar asociado a los documentos.*Mediante la herramienta**Inspector de documentos** (característica que seaccede desde las propias aplicaciones de Word, Excel, PowerPoint o Visio) oaplicaciones de terceros. Como se describe en el apartado Limpieza dedocumentos de la guía [CCN-STIC-885A - Guía de configuración segura paraOffice 365].|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se ha eliminado información personal y en general cualquier metadato quepudiera estar asociado a los documentos.*Mediante la herramienta**Inspector de documentos** (característica que seaccede desde las propias aplicaciones de Word, Excel, PowerPoint o Visio) oaplicaciones de terceros. Como se describe en el apartado Limpieza dedocumentos de la guía [CCN-STIC-885A - Guía de configuración segura paraOffice 365].|SiNo**Evidencias Recogidas:** |**Observaciones:**|
|**mp.info.6**|**Copias de seguridad**|**Copias de seguridad**|**Copias de seguridad**|
||Se han aplicado políticas de retención para gestionar el tiempo dealmacenamiento de los documentos y correos.|SiNo**Aplica:** |SiNo**Cumple:** |


**Centro Criptológico Nacional** 58


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**















|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
|||||
|||SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**mp.info.6**|**Copias de seguridad**|**Copias de seguridad**|**Copias de seguridad**|
||Se ha comunicado a los usuarios cómo gestionar el “control de versiones” delos documentos y la papelera de reciclaje.|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se ha comunicado a los usuarios cómo gestionar el “control de versiones” delos documentos y la papelera de reciclaje.|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**mp.info**|**Evitar indización de bibliotecas con contenido sensible**|||
||Se ha configurado que las bibliotecas con contenido sensible no aparezcanen el buscador.| **Aplica:**|~~No~~**Cumple:**|


**Centro Criptológico Nacional** 59


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**














|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
|||||
|||SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**mp.info**|**Evitar indización de bibliotecas con contenido sensible**|**Evitar indización de bibliotecas con contenido sensible**|**Evitar indización de bibliotecas con contenido sensible**|
||Se ha configurado que las bibliotecas con contenido sensible no aparezcanen el buscador. Incluyendo de igual modo la descarga de elementos cuandono existe conexión.|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se ha configurado que las bibliotecas con contenido sensible no aparezcanen el buscador. Incluyendo de igual modo la descarga de elementos cuandono existe conexión.|SiNo**Evidencias Recogidas:**  |**Observaciones:**|
|**mp.s**|**Protección de los servicios**|**Protección de los servicios**|**Protección de los servicios**|
|**mp.s.4**|**Protección frente a la denegación de servicio**|**Protección frente a la denegación de servicio**|**Protección frente a la denegación de servicio**|



**Centro Criptológico Nacional** 60


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**














|Control ENS|Configuracion|Estado|Col4|
|---|---|---|---|
||Se ha tenido en cuenta la información detallada en la guía [CCN-STIC-884A -Guía de configuración segura para Azure] sobre el_sistema de defensa DDoS__de Azure_. |SiNo**Aplica:**  |SiNo**Cumple:** |
||Se ha tenido en cuenta la información detallada en la guía [CCN-STIC-884A -Guía de configuración segura para Azure] sobre el_sistema de defensa DDoS__de Azure_. |SiNo**Evidencias Recogidas:**  |**Observaciones:**|



**Centro Criptológico Nacional** 61


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**
















|Col1|OTRAS CONSIDERACIONES DE SEGURIDAD|Col3|Col4|
|---|---|---|---|
||**Uso compartido externo**|**Uso compartido externo**|**Uso compartido externo**|
||Se ha restringido el uso compartido externo.|SiNo**Aplica:** |SiNo**Cumple:** |
||Se ha restringido el uso compartido externo.|SiNo**Evidencias Recogidas:** |**Observaciones:**|
||**Integración con Yammer**|||
||Se ha bloqueado la integración con Yammer|SiNo**Aplica:**  |SiNo**Cumple:** |
||Se ha bloqueado la integración con Yammer|SiNo**Evidencias Recogidas:** |**Observaciones:**|



**Centro Criptológico Nacional** 62


**CCN-STIC-885B** **Guía de configuración segura para SharePoint Online**


**Centro Criptológico Nacional** 63



![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-62-0.png)

![](/img/ccn-stic-885b---guia-de-configuracion-segura-para-sharepoint-online/CCN-STIC-885B---Guía-de-configuración-segura-para-SharePoint-Online.pdf-62-1.png)