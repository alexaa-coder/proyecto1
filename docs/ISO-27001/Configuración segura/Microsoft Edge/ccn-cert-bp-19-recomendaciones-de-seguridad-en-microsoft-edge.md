---
id: ccn-cert_bp-19-recomendaciones-de-seguridad-en-microsoft-edge
title: "Ccn Cert Bp 19 Recomendaciones De Seguridad En Microsoft Edge"
sidebar_label: "Ccn Cert Bp 19 Recomendaciones De Seguridad En Microsoft Edge"
---

#### CCN-CERT
# **BP/26**
### **Recomendaciones** **de seguridad en** **Microsoft Edge**
INFORME DE BUENAS PRÁCTICAS JUNIO 2022
2 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
## **Índice**
**1.**
**2.**
**3.**
**4.**
**Introducción**
**Navegador web Microsoft Edge**
2.1. Versiones 2.2. Requisitos mínimos
2.3. Descarga 2.4. Instalación y configuración inicial
2.5. Directrices de configuración 2.5.1 Sincronización y ajustes básicos de idioma
2.5.2 Sección perfiles
2.5.3 Sección privacidad, búsqueda y servicios
2.5.4 Sección página de inicio, página principal
y nuevas pestañas 2.5.5 Sección cookies y permisos del sitio
2.5.6 Sección sistema y rendimiento
**Lista de comprobación**
**Decálogo de recomendaciones**
**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 3
## **1. Introducción**
**El propósito de este documento consiste en**
**establecer los procedimientos y utilidades**
**necesarias para implementar y garantizar**
**la seguridad en Microsoft Edge, frente a los**
**riesgos a los que este pueda estar expuesto.**
Para ello, se proporciona una serie de pasos e instrucciones que permitan la configuración adecuada del navegador de forma manual.
Así mismo se proporciona un archivo de configuración para aplicar medidas de seguridad y así facilitar la posibilidad de implementar
seguridad.
En el desarrollo de esta guía se ha utilizado el instalador del programa
**Microsoft Edge** Stable en su **Versión 102.0.1245.33 (Complicación**
**oficial 64 bits)** para sistemas operativos Windows. Esta configuración
también es válida para la versión Microsoft Edge Business.
Independientemente de la versión elegida, versión Stable o versión Business de Microsoft Edge, ambas corresponden con la misma
compilación, con la única diferencia de que la versión Business no necesita conexión a internet para su instalación.
4 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
## **2. Navegador web** **microsoft edge**
Microsoft Edge inicialmente fue compilado con los motores **EdgeHTML** y **Chakra** propios de Microsoft. En 2019, Microsoft Edge pasó a ser
reconstruido como un navegador basado en **Chromium**, utilizando los motores **Blink** y **V8** . Estos motores, aportan mayor seguridad y mejor
apariencia.
Microsoft Edge sustituirá al navegador Internet Explorer en los entornos Windows como navegador predeterminado a partir de la distribución
1709 de Windows 10 y en su nuevo sistema operativo Windows 11.
**Microsoft Edge**
**sustituirá al navegador**
**Internet Explorer en**
**los entornos Windows**
**como navegador**
**predeterminado.**
Microsoft Edge está disponible para su descarga de manera gratuita desde la página web de Microsoft. De igual modo este viene desplegado
por defecto en los sistemas operativos Windows 10 y Windows 11 sin necesidad de descarga.
**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 5
2. Navegador web Microsoft Edge Para descargar el instalador se necesita tener conexión a internet, al
igual que para el proceso de instalación del navegador. Si el equipo en el que se instala Microsoft Edge no tiene conexión a internet, se
necesitará realizar la descarga completa del navegador a través de la versión **“Business”** de este, por medio del enlace alternativo
proporcionado por Microsoft a tal efecto.
También se puede instalar y actualizar el navegador Microsoft Edge desde la herramienta **“Windows Update”** del sistema operativo
Windows, manualmente descargando la última versión desde la web de Microsoft o desde el propio panel de configuración de Microsoft
Edge.
En este sentido, Microsoft Edge debe tener instaladas las últimas actualizaciones de software relacionadas con la seguridad. Si no se
aplican las últimas actualizaciones de software relacionadas con la seguridad de Microsoft Edge, esto se consideraría un **fallo crítico de**
**seguridad** .
6 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge
##### **2.1 Versiones**
Microsoft Edge ofrece una cadencia de ciclo de lanzamiento principal de cuatro (4) semanas, pero la duración efectiva del soporte asistido
para una versión de canal estable es de aproximadamente doce (12)
semanas.
Las actualizaciones de seguridad y las actualizaciones de mantenimiento solo están disponibles en la versión más reciente de la
versión **“Stable”** y la última versión del canal **“Beta”** . Si usa versiones anteriores de Microsoft Edge, es probable que se pierda las últimas
actualizaciones de calidad y seguridad.
A continuación, se resumen las diferentes versiones existentes para Microsoft Edge:
**Microsoft Edge**
El canal estable está diseñado para una amplia implementación en la organización y es el canal en el que la mayoría de los usuarios deberían estar. Es la más extendida
de las versiones y es el resultado de la estabilización del conjunto de funciones disponibles, en la versión anterior del Canal Beta. Las nuevas características se envían
aproximadamente cada 4 semanas. Las actualizaciones de seguridad y calidad se envían según sea necesario.
**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 7
2. Navegador web Microsoft Edge
**Microsoft Edge BETA**
El Canal Beta está destinado a la implementación de pruebas en producción para un conjunto representativo de usuarios. Este canal brinda una gran oportunidad
para validar que las configuraciones o necesidades funcionan como se espera en un entorno. Si encuentra un problema, es posible solucionarlo antes de que se publique el
lanzamiento en el canal estable. Al igual que la versión de Microsoft Edge las nuevas características se envían aproximadamente cada 4 semanas. Las actualizaciones de
seguridad y calidad se envían según sea necesario.
**Microsoft Edge DEV**
El canal DEV está destinado para ayudar a planificar y desarrollar las actualizaciones más recientes de Microsoft Edge, pero con mayor calidad que el canal Canary. Este
canal sirve para echar un vistazo anticipado a las novedades y prepararse para la próxima versión Beta.
**Microsoft Edge Canary**
El canal Canary se actualiza a diario y es el más vanguardista de todos los canales. Si se desea acceder a las características más recientes, aparecerán aquí primero.
**Microsoft Edge Business**
Esta versión es el mismo navegador Microsoft Edge que se utiliza en la versión Stable.
La diferencia está en cómo se despliega y se administra. Los administradores de TI pueden descargar esta versión para instalar el navegador Microsoft Edge a través de
un instalador **.msi** y administrar los navegadores de su organización mediante las políticas de grupo.
8 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge Para conocer la versión de Microsoft Edge instalada en un dispositivo,
realice los siguientes pasos:
Inicie Microsoft Edge, y haga clic sobre el botón ubicado en la parte superior derecha del navegador. A continuación, haga clic sobre
**“Configuración”** en el panel que se desplegará. Posteriormente, sitúese
en la sección **“Acerca de Microsoft Edge”** . El número de la versión instalada se mostrará debajo del nombre de Microsoft Edge, tal y como
se muestra en la siguiente imagen:
##### **2.2 Requisitos mínimos**
A continuación, se detallan los requisitos mínimos necesarios del sistema para realizar la implementación del programa Microsoft Edge:
**Sistemas operativos soportados (En versiones de 32-bit y 64 bit)** .
Windows 7.
Windows 8.1.
Windows 10 Professional 1709 y versiones posteriores.
Windows 10 Home 1709 y versiones posteriores.
Windows 10 Enterprise 2015 LTSC.
Windows 10 Enterprise 2016 LTSC.
Windows 10 Enterprise 2019 LTSC.
Windows 11 Professional.
**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 9
2. Navegador web Microsoft Edge Windows 11 Enterprise.
Windows 11 Home.
Windows Server 2008 R2.
Windows Server 2012.
Windows Server 2012 R2.
Windows Server 2016 (LTSC).
Windows Server 2019 (LTSC).
Windows Server (SAC).
MacOS Sierra 10.2 o superior.
iOS 11 o superior.
Android KitKat4.4 o superior.
Linux (Ubuntu, Debian, Fedora y openSUSE).
**Requisitos hardware recomendados:**
Requisitos mínimos recomendados para el sistema operativo de 64 bits instalado.
Requisitos mínimos recomendados para el sistema operativo de 32 bits instalado.
10 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge
##### **2.3 Descarga**
En algunos casos, como por ejemplo en los sistemas operativos Windows 10 en sus versiones Pro y Home, Microsoft Edge este ya se
encuentra instalado por defecto e integrado junto al sistema operativo.
A continuación, se detalla el proceso a seguir para realizar la descarga del navegador Microsoft Edge, en equipos que no lo tengan instalado
por defecto y sea requerido su instalación:

|Paso<br />1.|Descripción<br />Para la descarga del programa desde la fuente oficial se utilizará el siguiente<br />enlace:<br />https://www.microsoft.com/es-es/edge|
|---|---|
|**2.**|Descargue la versión del navegador en función de su sistema operativo.|

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 11
2. Navegador web Microsoft Edge 12 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge
##### **2.4 Instalación y configuración inicial**
Para realizar la instalación de Microsoft Edge realice los siguientes pasos:

|Paso<br />1.|Descripción<br />Ejecute el archivo descargado haciendo doble clic sobre él, ya sea en la versión<br />que necesita conexión a internet (Utilizada durante esta guía) o la versión sin<br />conexión a internet.|
|---|---|
|**2.**|Para comenzar con la instalación de Microsoft Edge, se requiere la elevación de<br />privilegios.<br />Para ello, se debe de pulsar en la opción “Sí” en la ventana emergente (“Control<br />de cuentas de usuario”) o introducir el usuario con privilegios para instalar si así<br />lo requiere.|

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 13
2. Navegador web Microsoft Edge

|Paso<br />3.|Descripción<br />Una vez se permita la ejecución, se descargará e instalará automáticamente.|
|---|---|
|**4.**|Tras fnalizar la instalación, en el primer inicio, aparecerá una ventana de<br />bienvenida donde se han de realizar confguraciones previas de seguridad.|
|**5.**|En la primera ventana de confguración de Microsoft Edge marque la opción<br />“**Comience sin sus datos**”.|

14 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge

|Paso<br />6.|Descripción<br />En la segunda venta de configuración de Microsoft Edge maque la opción<br />“Continuar sin estos datos”.|
|---|---|
|**7.**|En la siguiente pantalla, confgure el acceso a los datos de exploración recientes.<br />Marque la opción “**No permitir**” para restringir dicho acceso y pulse sobre<br />“**Confrmar y continua**r”.|

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 15
2. Navegador web Microsoft Edge

|Paso<br />8.|Descripción<br />Por último, en la configuración de la adaptación web marque la opción “No<br />permitir” para impedir que Microsoft utilice la información de navegación. Pulse<br />sobre “Confirmar e iniciar exploración”.|
|---|---|
|**9.**|Posterior a dichas confguraciones se abrirán varias ventanas de exploración y una<br />de ellas orientada a la personalización estética del navegador. Puede ignorarlas y<br />continuar con el siguiente apartado.|

16 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge
##### **2.5 Directrices de configuración**
El navegador Microsoft Edge dispone de una interfaz gráfica para la edición de sus opciones de uso y de seguridad.
Para acceder la interfaz de configuración se debe iniciar Microsoft Edge y hacer clic sobre el botón , ubicado en la parte superior
derecha del navegador. A continuación, se debe seleccionar la sección “ **Configuración** ” donde aparecerán las opciones de configuración
editables por el usuario.
Un método alternativo para acceder a la interfaz de configuración es escribir “ **edge://settings/profiles** ” en la barra de direcciones.
**2.5.1 Sincronización y ajustes básicos de idioma**
El navegador Microsoft Edge permite la sincronización automática con servicios de Microsoft, permitiendo a los usuarios, entre otros,
sincronizar automáticamente varios elementos como favoritos, pestañas abiertas, contraseñas, extensiones, etc.
Esta información se almacena en la cuenta de Microsoft proporcionada por el usuario a tal efecto. Cabe destacar, que para evitar problemas de
privacidad y seguridad se recomienda deshabilitar dicha funcionalidad del explorador.
Una vez el navegador se encuentre instalado, siga los siguientes pasos para realizar el ajuste básico de idioma y deshabilitar el corrector
ortográfico, con la finalidad de que no se recopilen datos del usuario mediante estos métodos:
**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 17
2. Navegador web Microsoft Edge

|Paso<br />1.|Descripción<br />En la sección “Perfiles”, y siempre que sea posible, se recomienda la eliminación<br />de cualquier cuenta sincronizada para evitar la revelación y/o obtención de la<br />información recopilada.<br />Esto no es impedimento con la existencia de perfiles que permitan diferenciar el<br />uso que se realiza con el navegador.|
|---|---|
|**2.**|En el menú “**Confguración**”, dentro de la sección “**Idiomas**”, acceda al apartado<br />“**Revisar ortografía**”. Deshabilite la opción “**Habilitar corrector ortográfco**”.|

18 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge
**2.5.2 Sección perfiles**
En este apartado, se indicarán los ajustes a tener en cuenta, de manera que los datos almacenados en el navegador no estén expuestos a
posibles ataques no deseados así como evitar que directamente se puedan almacenar.
A continuación. se describe cada uno de los pasos a seguir para la adecuada configuración de este apartado:

|Paso<br />1.|Descripción<br />Debido a la forma en la que se almacenan las credenciales, es posible que un<br />atacante malicioso pueda obtener acceso a las cuentas del usuario y/o utilizar las<br />“Credenciales almacenadas” para inicios de sesión no deseados.|
|---|---|
|**2.**|Para evitar estos usos indebidos deshabilite la opción “**Preguntar si quiere guardar**<br />**sus contraseñas**”, en la sección “**Perfles**” dentro del apartado “**Contraseñas**”:|

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 19
2. Navegador web Microsoft Edge

|Paso<br />3.|Descripción<br />A continuación pulse sobre la opción “Mas opciones de configuración” y<br />deshabilite la opción “Mostrar el botón “Mostrar contraseña” en los campos de<br />contraseña”.|
|---|---|
|**4.**|La información referente a los “**Métodos de pago**” es un elemento atractivo para<br />los atacantes buscando hacer un uso fraudulento de la misma y, por ello, se<br />recomienda**no tener almacenada** esta información en el navegador Microsoft<br />Edge para evitar ser objeto de ataques maliciosos.|
|**5 .**|Deshabilite la opción “**Guardar y rellenar información de pago**”, como indica la<br />siguiente imagen, dentro de la sección “**Perfles**” en el apartado “**Información de**<br />**pago**”:|

20 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge

|Paso<br />6.|Descripción<br />Al igual que en el caso anterior, el almacenamiento de información, aun no siendo<br />crítico, puede ofrecer a un atacante información relevante sobre los movimientos,<br />acciones u otras consideraciones del usuario.|
|---|---|
|**7.**|Para evitar el uso de esta información, deshabilite las siguientes opciones:<br />**+	“Guardar y rellenar información básica”.**<br />**+	“Guardar y rellenar información personalizada”.**<br />Estas se encuentran dentro de la sección “**Perfles**”, en el apartado “**Información**<br />**personal**”:|
|**8.**|Adicional a la confguración indicada anteriormente citada, dentro de la sección<br />perfles deberán deshabilitarse las siguientes opciones dentro de cada uno de los<br />apartados indicados:<br />**+	Apartado “Microsoft Rewards”:**<br />**  • Deshabilite “Gane Microsoft Rewards en Microsoft Edge”**<br />**+	Apartado “Preferencia de perfl”:**<br />**  • Deshabilite “Permitir el inicio de sesión único para sitios profesionales o**<br />**educativos que usen este perfl”**|

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 21
2. Navegador web Microsoft Edge
**2.5.3 Sección privacidad, búsqueda y servicios**
En este apartado, se configurarán las opciones de privacidad, búsqueda y servicios para evitar la obtención de información no deseada y/o
requerida así como limitar las funcionalidades de los servicios ofrecidos a través del navegador.
A continuación se describen las configuraciones a configurar:
22 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge

|Paso<br />2.|Descripción<br />En el mismo apartado deshabilite la opción “Permitir que los sitios comprueben<br />si tiene métodos de pago guardados”.|
|---|---|
|**3.**|A continuación, en los apartados “**Datos de diagnóstico opcionales**” y<br />“**Personalizar su experiencia web**” asegúrese que sendas opciones aparecen<br />deshabilitadas tal y como se muestra en la siguiente imagen:|

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 23
2. Navegador web Microsoft Edge

|Paso<br />4.|Descripción<br />Siguiendo en la sección “Privacidad, búsqueda y servicios”, en el apartado<br />“Servicios” se deshabilitarán las siguientes opciones relacionadas con<br />funcionalidades de servicios web, ofrecidos por Microsoft Edge, tal y como<br />muestra la siguiente imagen:|
|---|---|
|**5.**|A continuación, se deberán defnir algunas confguraciones que defnan el<br />comportamiento del navegador cuando se fnaliza el uso de este de modo que**se**<br />**eliminen los fcheros generados por el navegador durante su ejecución**.<br />Esto favorece la carga de las últimas versiones de las páginas visitadas, así como<br />la confguración actualizada para el sitio web, en las siguientes ocasiones que se<br />visite el sitio, mejorando la seguridad general de la navegación.|

24 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge
**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 25
2. Navegador web Microsoft Edge

|Paso<br />7.|Descripción<br />Siguiendo en los ajustes de la sección “Privacidad, búsqueda y servicios”, habilite<br />la opción “Mejore su seguridad en la web” en el apartado “Seguridad”. Para<br />obtener esta protección, se debe hacer clic sobre el texto “Mejore su seguridad<br />en la Web” o habilitar la opción desde el botón lateral, tal y como se observa en<br />la siguiente imagen:<br />Esta protección que ofrece el navegador Microsoft Edge incluye, entre otras, las<br />siguientes características:<br />– Agrega mitigaciones de seguridad para los sitios que no visita con frecuencia.<br />– La mayoría de los sitios funcionan según lo esperado.<br />– Bloquea las amenazas de seguridad.|
|---|---|
|**8.**|Dentro del mismo apartado habilite la opción “**Bloquear aplicaciones**<br />**potencialmente no deseadas**”:|

26 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge

|Paso<br />9.|Descripción<br />La funcionalidad “Usar DNS seguro”, viene activa de forma predeterminada. Sin<br />embargo, por defecto se hace uso del DNS del proveedor del servicio actual, lo<br />que puede provocar el intento de conexiones no seguras contra un sitio web<br />debido a interrupciones del servicio.<br />Por ello, es posible establecer uno de los DNS facilitados por el navegador o<br />incluso uno personalizado si se encuentra en un entorno empresarial:|
|---|---|
|**10.**|A continuación asegúrese que las opciones “**SmartScreen de Microsoft Defender**” <br />y “**Active los servicios de seguridad del sitio para obtener mas información**<br />**sobre los sitios web que visite**” se encuentra habilitados. En caso contrario<br />habilite ambas opciones.|

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 27
2. Navegador web Microsoft Edge 28 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge
**2.5.4 Sección página de inicio, página principal y nuevas**
**pestañas**
Tal y como se verá tambien en apartados posteriores, los envíos de información en segundo plano son una parte muy importante para la
seguridad y privacidad para evitar la ejecución de código malicioso.
**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 29
2. Navegador web Microsoft Edge
**2.5.5 Sección cookies y permisos del sitio**
La configuración de las cookies y los envíos de información en segundo plano son una parte muy importante para la seguridad y privacidad.
Con una configuración segura de estos elementos se pueden prevenir brechas de seguridad y posibles robos de información sensible, ya que
un atacante podría ocultar la ejecución de código malicioso mediante el tráfico en segundo plano del navegador.
Para evitar estos riesgos, se recomienda realizar la siguiente configuración en el navegador Microsoft Edge:
**La configuración de las**
**cookies y los envíos de**
**información en segundo**
**plano son una parte**
**muy importante para la**
**seguridad y privacidad.**

|Paso<br />1.|Descripción<br />A continuación se modificarán los aspectos que impiden el almacenamiento y<br />el bloqueo de ciertas cookies para evitar el almacenamiento de información no<br />necesario, así como el bloqueo de información en segundo plano.|
|---|---|
|**2.**|En la confguración de Edge, diríjase a la sección de “**Cookies y permisos del**<br />**sitio**”, y después al apartado “**Administra y elimina cookies y datos del sitio**”.<br />Una vez allí, habilite la opción “**Bloquear las cookies de terceros**” y deshabilite la<br />opción “**Precargar páginas para una exploración y búsqueda más rápida**”, como<br />se muestra en la siguiente imagen:|

30 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge

|Paso|Descripción<br />Nota: Hay algunas páginas que necesitan cookies de terceros para su<br />correcto funcionamiento. Si se detecta que una página no funciona como se<br />espera, es posible que se necesite habilitar las cookies de terceros para su<br />correcto funcionamiento. Para ello, puede generar una excepción de cookies<br />de terceros sobre ciertas páginas para mejorar su experiencia de uso, tal y<br />como se aprecia en la siguiente imagen.|
|---|---|
|**3.**|Continuando con las confguraciones, se deberán cambiar algunos aspectos<br />para evitar ataques en ventanas minimizadas, ventanas en segundo plano, y<br />ejecuciones de código mediante JavaScript, que normalmente se utilizan para<br />realizar ataques maliciosos.|

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 31
2. Navegador web Microsoft Edge 32 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge

|Paso<br />5.|Descripción<br />Posteriormente en el mismo apartado, denominado “Cookies y permisos del<br />sitio”, se deshabilitarán los aspectos referentes a la “Sincronización en segundo<br />plano”, del tal modo que no permita que los sitios cerrados recientemente puedan<br />realizar ejecuciones de forma no deseada.<br />Deshabilite la opción “Permitir que los sitios cerrados recientemente terminen<br />de enviar y recibir datos” como aparece en la siguiente imagen:|
|---|---|
|**6.**|Para terminar las confguraciones dentro del apartado de “**Cookies y permisos**<br />**del sitio**”, se deberán cambiar algunos aspectos relativos al uso de elementos de<br />comunicación hardware del equipo. Esto permitirá establecer una confguración<br />de privacidad adecuándose a las necesidades del usuario.|
|**7.**|Se deberán establecer en estado “**Bloqueado**” los siguientes elementos:<br />**–	“Ubicación”**<br />**–	“Cámara”**<br />**–	“Micrófono”**<br />**–	“Notifcaciones”**<br />**–	“Descargas automáticas”**<br />**–	“Dispositivos USB”**<br />**–	“Puertos serie”**<br />**–	“Edición de archivos”**<br />**–	“Portapapeles”**<br />**–	“Controladores de pago”**<br />**–	“Realidad virtual”**<br />**–	“Realidad aumentada”**|

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 33
2. Navegador web Microsoft Edge 34 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
2. Navegador web Microsoft Edge
**2.5.6 Sección sistema y rendimiento**
Como ya se ha comentado en puntos anteriores, la ejecución de código en segundo plano después del cierre del navegador Microsoft Edge es
susceptible de uso para ataques maliciosos y debe ser deshabilitada, para ello, se han de realizar los siguientes pasos:
**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 35
## **3. Lista de** **comprobación**

|Criticidad<br />Alta|Descripción<br />Microsoft Edge debe tener instaladas las últimas actualizaciones de software<br />relacionadas con la seguridad, aplicándolas mediante instalación manual de<br />la última versión disponible para su descarga, la herramienta de actualización<br />automática de Microsoft Edge, o la herramienta Windows Update del sistema<br />operativo Windows.|
|---|---|
|**Alta**|En el caso de que se usen extensiones en el navegador, deberá asegurarse de que<br />estén actualizadas y provengan de fuentes confables.|
|**Media**|Cuando un usuario cambia de una página segura (habilitada para SSL) a una<br />página no segura, Microsoft Edge está confgurado para notifcar al usuario.|
|**Media**|Microsoft Edge está confgurado para bloquear ventanas emergentes.|
|**Media**|Se pueden utilizar cuentas de Microsoft y e iniciar sesión para sincronizar los<br />datos en Microsoft Edge, con una cuenta proporcionada por el usuario.|
|**Media**|Microsoft Edge está confgurado para no autocompletar búsquedas y URLs, sin<br />enviar información al buscador predeterminado.|
|**Media**|Microsoft Edge está confgurado para no guardar las contraseñas de los sitios.|
|**Media**|Microsoft Edge está confgurado para no iniciar sesión automáticamente en las<br />webs que tiene las credenciales almacenadas.|

36 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
3. Lista de comprobación

|Criticidad<br />Media|Descripción<br />Microsoft Edge está configurado para no guardar ni autocompletar métodos de<br />pago.|
|---|---|
|**Media**|Microsoft Edge está confgurado para permitir que los sitios web no comprueben<br />si hay métodos de pago guardados.|
|**Media**|Microsoft Edge está confgurado para bloquear las cookies de terceros.|
|**Media**|Microsoft Edge está confgurado para no precargar información de las páginas.|
|**Media**|Microsoft Edge está confgurado para permitir que las páginas cerradas no envíen<br />y reciban datos.|
|**Media**|Microsoft Edge está confgurado para no permitir el uso de JavaScript, excepto<br />que se añada alguna excepción.|
|**Media**|Microsoft Edge está confgurado para no ejecutar aplicaciones en segundo plano<br />al cerrar el navegador.|

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 37
## **4. Decálogo de** **recomendaciones**
##### A continuación, se indican diez recomendaciones de seguridad en el uso de Microsoft Edge.
38 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge
**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 39