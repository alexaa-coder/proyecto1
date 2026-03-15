---
title: "**BP/26**"
sidebar_label: "**BP/26**"
responsable: "Responsable de RRHH"
clasificacion: "USO INTERNO"
fecha_revision: "2026-03-15"
idioma: "es"
tags:
  - confidencialidad
  - english
  - formacion
  - iso-27001
  - nda
  - seguridad
  - soporte
---

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-0-1.png)
#### CCN-CERT
# **BP/26**

### **Recomendaciones** **de seguridad en** **Microsoft Edge**

INFORME DE BUENAS PRÁCTICAS


JUNIO 2022



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-0-0.png)
![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-1-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-1-1.png)



2 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge


## **Índice**



**1.**

**2.**


**3.**

**4.**



**Introducción**

**Navegador web Microsoft Edge**

2.1. Versiones

2.2. Requisitos mínimos

2.3. Descarga

2.4. Instalación y configuración inicial

2.5. Directrices de configuración

2.5.1 Sincronización y ajustes básicos de idioma

2.5.2 Sección perfiles

2.5.3 Sección privacidad, búsqueda y servicios

2.5.4 Sección página de inicio, página principal

y nuevas pestañas

2.5.5 Sección cookies y permisos del sitio

2.5.6 Sección sistema y rendimiento


**Lista de comprobación**

**Decálogo de recomendaciones**



4

5

7

9

11

13

17

17

19

22


29

30

35


36

38



**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 3


## **1. Introducción**

**El propósito de este documento consiste en**

**establecer los procedimientos y utilidades**

**necesarias para implementar y garantizar**

**la seguridad en Microsoft Edge, frente a los**

**riesgos a los que este pueda estar expuesto.**


Para ello, se proporciona una serie de pasos e instrucciones que

permitan la configuración adecuada del navegador de forma manual.

Así mismo se proporciona un archivo de configuración para aplicar

medidas de seguridad y así facilitar la posibilidad de implementar

seguridad.


En el desarrollo de esta guía se ha utilizado el instalador del programa

**Microsoft Edge** Stable en su **Versión 102.0.1245.33 (Complicación**

**oficial 64 bits)** para sistemas operativos Windows. Esta configuración

también es válida para la versión Microsoft Edge Business.


Independientemente de la versión elegida, versión Stable o versión

Business de Microsoft Edge, ambas corresponden con la misma

compilación, con la única diferencia de que la versión Business no

necesita conexión a internet para su instalación.


4 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-3-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-3-1.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-3-2.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-3-3.png)
## **2. Navegador web** **microsoft edge**



Microsoft Edge inicialmente fue compilado con los motores **EdgeHTML**

y **Chakra** propios de Microsoft. En 2019, Microsoft Edge pasó a ser

reconstruido como un navegador basado en **Chromium**, utilizando los

motores **Blink** y **V8** . Estos motores, aportan mayor seguridad y mejor

apariencia.


Microsoft Edge sustituirá al navegador Internet Explorer en los entornos

Windows como navegador predeterminado a partir de la distribución

1709 de Windows 10 y en su nuevo sistema operativo Windows 11.



**Microsoft Edge**

**sustituirá al navegador**

**Internet Explorer en**

**los entornos Windows**

**como navegador**

**predeterminado.**



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-4-0.png)





Microsoft Edge está disponible para su descarga de manera gratuita

desde la página web de Microsoft. De igual modo este viene desplegado

por defecto en los sistemas operativos Windows 10 y Windows 11 sin

necesidad de descarga.


**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 5


2. Navegador web Microsoft Edge


Para descargar el instalador se necesita tener conexión a internet, al

igual que para el proceso de instalación del navegador. Si el equipo

en el que se instala Microsoft Edge no tiene conexión a internet, se

necesitará realizar la descarga completa del navegador a través

de la versión **“Business”** de este, por medio del enlace alternativo

proporcionado por Microsoft a tal efecto.



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-5-0.png)



También se puede instalar y actualizar el navegador Microsoft Edge

desde la herramienta **“Windows Update”** del sistema operativo

Windows, manualmente descargando la última versión desde la web

de Microsoft o desde el propio panel de configuración de Microsoft

Edge.


En este sentido, Microsoft Edge debe tener instaladas las últimas

actualizaciones de software relacionadas con la seguridad. Si no se

aplican las últimas actualizaciones de software relacionadas con la

seguridad de Microsoft Edge, esto se consideraría un **fallo crítico de**

**seguridad** .


6 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-5-1.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-5-2.png)
2. Navegador web Microsoft Edge

##### **2.1 Versiones**


Microsoft Edge ofrece una cadencia de ciclo de lanzamiento principal

de cuatro (4) semanas, pero la duración efectiva del soporte asistido

para una versión de canal estable es de aproximadamente doce (12)

semanas.



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-6-0.png)



Las actualizaciones de seguridad y las actualizaciones de

mantenimiento solo están disponibles en la versión más reciente de la

versión **“Stable”** y la última versión del canal **“Beta”** . Si usa versiones

anteriores de Microsoft Edge, es probable que se pierda las últimas

actualizaciones de calidad y seguridad.


A continuación, se resumen las diferentes versiones existentes para

Microsoft Edge:


**Microsoft Edge**


El canal estable está diseñado para una amplia implementación en la organización y

es el canal en el que la mayoría de los usuarios deberían estar. Es la más extendida

de las versiones y es el resultado de la estabilización del conjunto de funciones

disponibles, en la versión anterior del Canal Beta. Las nuevas características se envían

aproximadamente cada 4 semanas. Las actualizaciones de seguridad y calidad se

envían según sea necesario.


**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 7



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-6-1.png)
2. Navegador web Microsoft Edge

|Control ENS|ConfiguracionSe han comprobado los niveles de permisos para los recursos de laorganización: propietarios, miembros y visitantes.|EstadoAplica:Si No|Cumple:Si No|
|---|---|---|---|
||**Microsoft Edge BETA**El Canal Beta está destinado a la implementación de pruebas en producción paraun conjunto representativo de usuarios. Este canal brinda una gran oportunidadpara validar que las confguraciones o necesidades funcionan como se espera en unentorno. Si encuentra un problema, es posible solucionarlo antes de que se publique ellanzamiento en el canal estable. Al igual que la versión de Microsoft Edge las nuevascaracterísticas se envían aproximadamente cada 4 semanas. Las actualizaciones deseguridad y calidad se envían según sea necesario.|||
||**Microsoft Edge DEV**|**Microsoft Edge DEV**|**Microsoft Edge DEV**|
||El canal DEV está destinado para ayudar a planifcar y desarrollar las actualizacionesmás recientes de Microsoft Edge, pero con mayor calidad que el canal Canary. Estecanal sirve para echar un vistazo anticipado a las novedades y prepararse para lapróxima versión Beta.**Microsoft Edge Canary**El canal Canary se actualiza a diario y es el más vanguardista de todos los canales. Sise desea acceder a las características más recientes, aparecerán aquí primero.|||
||El canal DEV está destinado para ayudar a planifcar y desarrollar las actualizacionesmás recientes de Microsoft Edge, pero con mayor calidad que el canal Canary. Estecanal sirve para echar un vistazo anticipado a las novedades y prepararse para lapróxima versión Beta.**Microsoft Edge Canary**El canal Canary se actualiza a diario y es el más vanguardista de todos los canales. Sise desea acceder a las características más recientes, aparecerán aquí primero.|||



**Microsoft Edge Business**


Esta versión es el mismo navegador Microsoft Edge que se utiliza en la versión Stable.

La diferencia está en cómo se despliega y se administra. Los administradores de TI

pueden descargar esta versión para instalar el navegador Microsoft Edge a través de

un instalador **.msi** y administrar los navegadores de su organización mediante las

políticas de grupo.


8 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-7-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-7-1.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-7-2.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-7-3.png)
2. Navegador web Microsoft Edge


Para conocer la versión de Microsoft Edge instalada en un dispositivo,

realice los siguientes pasos:


Inicie Microsoft Edge, y haga clic sobre el botón   ubicado en la

parte superior derecha del navegador. A continuación, haga clic sobre

**“Configuración”** en el panel que se desplegará. Posteriormente, sitúese

en la sección **“Acerca de Microsoft Edge”** . El número de la versión

instalada se mostrará debajo del nombre de Microsoft Edge, tal y como

se muestra en la siguiente imagen:

##### **2.2 Requisitos mínimos**


A continuación, se detallan los requisitos mínimos necesarios del

sistema para realizar la implementación del programa Microsoft Edge:


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



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-8-0.png)
2. Navegador web Microsoft Edge


Windows 11 Enterprise.

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



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-9-1.png)



**Requisitos hardware recomendados:**


Requisitos mínimos recomendados para el sistema operativo de 64

bits instalado.

Requisitos mínimos recomendados para el sistema operativo de 32

bits instalado.


10 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge


2. Navegador web Microsoft Edge

##### **2.3 Descarga**


En algunos casos, como por ejemplo en los sistemas operativos

Windows 10 en sus versiones Pro y Home, Microsoft Edge este ya se

encuentra instalado por defecto e integrado junto al sistema operativo.


A continuación, se detalla el proceso a seguir para realizar la descarga

del navegador Microsoft Edge, en equipos que no lo tengan instalado

por defecto y sea requerido su instalación:





![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-10-0.png)


|Paso1.|DescripciónPara la descarga del programa desde la fuente oficial se utilizará el siguienteenlace:https://www.microsoft.com/es-es/edge|
|---|---|
|**2.**|Descargue la versión del navegador en función de su sistema operativo.|



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-10-1.png)

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 11


2. Navegador web Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-11-1.png)



12 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-11-0.png)
2. Navegador web Microsoft Edge

##### **2.4 Instalación y configuración inicial**


Para realizar la instalación de Microsoft Edge realice los siguientes pasos:

|Paso1.|DescripciónEjecute el archivo descargado haciendo doble clic sobre él, ya sea en la versiónque necesita conexión a internet (Utilizada durante esta guía) o la versión sinconexión a internet.|
|---|---|
|**2.**|Para comenzar con la instalación de Microsoft Edge, se requiere la elevación deprivilegios.Para ello, se debe de pulsar en la opción “Sí” en la ventana emergente (“Controlde cuentas de usuario”) o introducir el usuario con privilegios para instalar si asílo requiere.|



**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 13



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-12-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-12-1.png)
2. Navegador web Microsoft Edge





![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-13-0.png)


|Paso3.|DescripciónUna vez se permita la ejecución, se descargará e instalará automáticamente.|
|---|---|
|**4.**|Tras fnalizar la instalación, en el primer inicio, aparecerá una ventana debienvenida donde se han de realizar confguraciones previas de seguridad.|
|**5.**|En la primera ventana de confguración de Microsoft Edge marque la opción“**Comience sin sus datos**”.|



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-13-1.png)

14 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge


2. Navegador web Microsoft Edge

|Paso6.|DescripciónEn la segunda venta de configuración de Microsoft Edge maque la opción“Continuar sin estos datos”.|
|---|---|
|**7.**|En la siguiente pantalla, confgure el acceso a los datos de exploración recientes.Marque la opción “**No permitir**” para restringir dicho acceso y pulse sobre“**Confrmar y continua**r”.|



**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 15



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-14-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-14-1.png)
2. Navegador web Microsoft Edge





![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-15-0.png)


|Paso8.|DescripciónPor último, en la configuración de la adaptación web marque la opción “Nopermitir” para impedir que Microsoft utilice la información de navegación. Pulsesobre “Confirmar e iniciar exploración”.|
|---|---|
|**9.**|Posterior a dichas confguraciones se abrirán varias ventanas de exploración y unade ellas orientada a la personalización estética del navegador. Puede ignorarlas ycontinuar con el siguiente apartado.|



16 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge


2. Navegador web Microsoft Edge

##### **2.5 Directrices de configuración**


El navegador Microsoft Edge dispone de una interfaz gráfica para la

edición de sus opciones de uso y de seguridad.


Para acceder la interfaz de configuración se debe iniciar Microsoft

Edge y hacer clic sobre el botón , ubicado en la parte superior

derecha del navegador. A continuación, se debe seleccionar la sección

“ **Configuración** ” donde aparecerán las opciones de configuración

editables por el usuario.


Un método alternativo para acceder a la interfaz de configuración es

escribir “ **edge://settings/profiles** ” en la barra de direcciones.


**2.5.1 Sincronización y ajustes básicos de idioma**


El navegador Microsoft Edge permite la sincronización automática

con servicios de Microsoft, permitiendo a los usuarios, entre otros,

sincronizar automáticamente varios elementos como favoritos,

pestañas abiertas, contraseñas, extensiones, etc.


Esta información se almacena en la cuenta de Microsoft proporcionada

por el usuario a tal efecto. Cabe destacar, que para evitar problemas de

privacidad y seguridad se recomienda deshabilitar dicha funcionalidad

del explorador.


Una vez el navegador se encuentre instalado, siga los siguientes pasos

para realizar el ajuste básico de idioma y deshabilitar el corrector

ortográfico, con la finalidad de que no se recopilen datos del usuario

mediante estos métodos:


**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 17



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-16-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-16-1.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-16-2.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-16-3.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-16-4.png)
2. Navegador web Microsoft Edge

|Paso1.|DescripciónEn la sección “Perfiles”, y siempre que sea posible, se recomienda la eliminaciónde cualquier cuenta sincronizada para evitar la revelación y/o obtención de lainformación recopilada.Esto no es impedimento con la existencia de perfiles que permitan diferenciar eluso que se realiza con el navegador.|
|---|---|
|**2.**|En el menú “**Confguración**”, dentro de la sección “**Idiomas**”, acceda al apartado“**Revisar ortografía**”. Deshabilite la opción “**Habilitar corrector ortográfco**”.|



18 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-17-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-17-1.png)
2. Navegador web Microsoft Edge


**2.5.2 Sección perfiles**


En este apartado, se indicarán los ajustes a tener en cuenta, de manera

que los datos almacenados en el navegador no estén expuestos a

posibles ataques no deseados así como evitar que directamente se

puedan almacenar.


A continuación. se describe cada uno de los pasos a seguir para la

adecuada configuración de este apartado:





![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-18-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-18-1.png)


|Paso1.|DescripciónDebido a la forma en la que se almacenan las credenciales, es posible que unatacante malicioso pueda obtener acceso a las cuentas del usuario y/o utilizar las“Credenciales almacenadas” para inicios de sesión no deseados.|
|---|---|
|**2.**|Para evitar estos usos indebidos deshabilite la opción “**Preguntar si quiere guardar****sus contraseñas**”, en la sección “**Perfles**” dentro del apartado “**Contraseñas**”:|



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-18-2.png)

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 19


2. Navegador web Microsoft Edge





![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-19-0.png)


|Paso3.|DescripciónA continuación pulse sobre la opción “Mas opciones de configuración” ydeshabilite la opción “Mostrar el botón “Mostrar contraseña” en los campos decontraseña”.|
|---|---|
|**4.**|La información referente a los “**Métodos de pago**” es un elemento atractivo paralos atacantes buscando hacer un uso fraudulento de la misma y, por ello, serecomienda**no tener almacenada** esta información en el navegador MicrosoftEdge para evitar ser objeto de ataques maliciosos.|
|**5 .**|Deshabilite la opción “**Guardar y rellenar información de pago**”, como indica lasiguiente imagen, dentro de la sección “**Perfles**” en el apartado “**Información de****pago**”:|



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-19-1.png)

20 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge


2. Navegador web Microsoft Edge






|Paso6.|DescripciónAl igual que en el caso anterior, el almacenamiento de información, aun no siendocrítico, puede ofrecer a un atacante información relevante sobre los movimientos,acciones u otras consideraciones del usuario.|
|---|---|
|**7.**|Para evitar el uso de esta información, deshabilite las siguientes opciones:**+	“Guardar y rellenar información básica”.****+	“Guardar y rellenar información personalizada”.**Estas se encuentran dentro de la sección “**Perfles**”, en el apartado “**Información****personal**”:|
|**8.**|Adicional a la confguración indicada anteriormente citada, dentro de la secciónperfles deberán deshabilitarse las siguientes opciones dentro de cada uno de losapartados indicados:**+	Apartado “Microsoft Rewards”:****  • Deshabilite “Gane Microsoft Rewards en Microsoft Edge”****+	Apartado “Preferencia de perfl”:****  • Deshabilite “Permitir el inicio de sesión único para sitios profesionales o****educativos que usen este perfl”**|



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-20-0.png)

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 21


2. Navegador web Microsoft Edge


**2.5.3 Sección privacidad, búsqueda y servicios**


En este apartado, se configurarán las opciones de privacidad, búsqueda

y servicios para evitar la obtención de información no deseada y/o

requerida así como limitar las funcionalidades de los servicios ofrecidos

a través del navegador.


A continuación se describen las configuraciones a configurar:



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-21-3.png)



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-21-0.png)



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-21-1.png)

22 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-21-2.png)
2. Navegador web Microsoft Edge

|Paso2.|DescripciónEn el mismo apartado deshabilite la opción “Permitir que los sitios compruebensi tiene métodos de pago guardados”.|
|---|---|
|**3.**|A continuación, en los apartados “**Datos de diagnóstico opcionales**” y“**Personalizar su experiencia web**” asegúrese que sendas opciones aparecendeshabilitadas tal y como se muestra en la siguiente imagen:|



**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 23



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-22-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-22-1.png)
2. Navegador web Microsoft Edge





![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-23-0.png)


|Paso4.|DescripciónSiguiendo en la sección “Privacidad, búsqueda y servicios”, en el apartado“Servicios” se deshabilitarán las siguientes opciones relacionadas confuncionalidades de servicios web, ofrecidos por Microsoft Edge, tal y comomuestra la siguiente imagen:|
|---|---|
|**5.**|A continuación, se deberán defnir algunas confguraciones que defnan elcomportamiento del navegador cuando se fnaliza el uso de este de modo que**se****eliminen los fcheros generados por el navegador durante su ejecución**.Esto favorece la carga de las últimas versiones de las páginas visitadas, así comola confguración actualizada para el sitio web, en las siguientes ocasiones que sevisite el sitio, mejorando la seguridad general de la navegación.|



24 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge


2. Navegador web Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-24-2.png)







![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-24-0.png)



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-24-1.png)

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 25


2. Navegador web Microsoft Edge

|Paso7.|DescripciónSiguiendo en los ajustes de la sección “Privacidad, búsqueda y servicios”, habilitela opción “Mejore su seguridad en la web” en el apartado “Seguridad”. Paraobtener esta protección, se debe hacer clic sobre el texto “Mejore su seguridaden la Web” o habilitar la opción desde el botón lateral, tal y como se observa enla siguiente imagen:Esta protección que ofrece el navegador Microsoft Edge incluye, entre otras, lassiguientes características:– Agrega mitigaciones de seguridad para los sitios que no visita con frecuencia.– La mayoría de los sitios funcionan según lo esperado.– Bloquea las amenazas de seguridad.|
|---|---|
|**8.**|Dentro del mismo apartado habilite la opción “**Bloquear aplicaciones****potencialmente no deseadas**”:|



26 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-25-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-25-1.png)
2. Navegador web Microsoft Edge





![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-26-0.png)


|Paso9.|DescripciónLa funcionalidad “Usar DNS seguro”, viene activa de forma predeterminada. Sinembargo, por defecto se hace uso del DNS del proveedor del servicio actual, loque puede provocar el intento de conexiones no seguras contra un sitio webdebido a interrupciones del servicio.Por ello, es posible establecer uno de los DNS facilitados por el navegador oincluso uno personalizado si se encuentra en un entorno empresarial:|
|---|---|
|**10.**|A continuación asegúrese que las opciones “**SmartScreen de Microsoft Defender**” y “**Active los servicios de seguridad del sitio para obtener mas información****sobre los sitios web que visite**” se encuentra habilitados. En caso contrariohabilite ambas opciones.|



**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 27


2. Navegador web Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-27-2.png)



28 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-27-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-27-1.png)
2. Navegador web Microsoft Edge


**2.5.4 Sección página de inicio, página principal y nuevas**
**pestañas**


Tal y como se verá tambien en apartados posteriores, los envíos de

información en segundo plano son una parte muy importante para la

seguridad y privacidad para evitar la ejecución de código malicioso.



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-28-2.png)



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-28-0.png)

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 29



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-28-1.png)
2. Navegador web Microsoft Edge


**2.5.5 Sección cookies y permisos del sitio**



La configuración de las cookies y los envíos de información en segundo

plano son una parte muy importante para la seguridad y privacidad.

Con una configuración segura de estos elementos se pueden prevenir

brechas de seguridad y posibles robos de información sensible, ya que

un atacante podría ocultar la ejecución de código malicioso mediante

el tráfico en segundo plano del navegador.


Para evitar estos riesgos, se recomienda realizar la siguiente

configuración en el navegador Microsoft Edge:



**La configuración de las**

**cookies y los envíos de**

**información en segundo**

**plano son una parte**

**muy importante para la**

**seguridad y privacidad.**






|Paso1.|DescripciónA continuación se modificarán los aspectos que impiden el almacenamiento yel bloqueo de ciertas cookies para evitar el almacenamiento de información nonecesario, así como el bloqueo de información en segundo plano.|
|---|---|
|**2.**|En la confguración de Edge, diríjase a la sección de “**Cookies y permisos del****sitio**”, y después al apartado “**Administra y elimina cookies y datos del sitio**”.Una vez allí, habilite la opción “**Bloquear las cookies de terceros**” y deshabilite laopción “**Precargar páginas para una exploración y búsqueda más rápida**”, comose muestra en la siguiente imagen:|



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-29-0.png)

30 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge


2. Navegador web Microsoft Edge





![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-30-0.png)


|Paso|DescripciónNota: Hay algunas páginas que necesitan cookies de terceros para sucorrecto funcionamiento. Si se detecta que una página no funciona como seespera, es posible que se necesite habilitar las cookies de terceros para sucorrecto funcionamiento. Para ello, puede generar una excepción de cookiesde terceros sobre ciertas páginas para mejorar su experiencia de uso, tal ycomo se aprecia en la siguiente imagen.|
|---|---|
|**3.**|Continuando con las confguraciones, se deberán cambiar algunos aspectospara evitar ataques en ventanas minimizadas, ventanas en segundo plano, yejecuciones de código mediante JavaScript, que normalmente se utilizan pararealizar ataques maliciosos.|



**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 31


2. Navegador web Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-31-2.png)







![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-31-0.png)



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-31-1.png)

32 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge


2. Navegador web Microsoft Edge





![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-32-0.png)


|Paso5.|DescripciónPosteriormente en el mismo apartado, denominado “Cookies y permisos delsitio”, se deshabilitarán los aspectos referentes a la “Sincronización en segundoplano”, del tal modo que no permita que los sitios cerrados recientemente puedanrealizar ejecuciones de forma no deseada.Deshabilite la opción “Permitir que los sitios cerrados recientemente terminende enviar y recibir datos” como aparece en la siguiente imagen:|
|---|---|
|**6.**|Para terminar las confguraciones dentro del apartado de “**Cookies y permisos****del sitio**”, se deberán cambiar algunos aspectos relativos al uso de elementos decomunicación hardware del equipo. Esto permitirá establecer una confguraciónde privacidad adecuándose a las necesidades del usuario.|
|**7.**|Se deberán establecer en estado “**Bloqueado**” los siguientes elementos:**–	“Ubicación”****–	“Cámara”****–	“Micrófono”****–	“Notifcaciones”****–	“Descargas automáticas”****–	“Dispositivos USB”****–	“Puertos serie”****–	“Edición de archivos”****–	“Portapapeles”****–	“Controladores de pago”****–	“Realidad virtual”****–	“Realidad aumentada”**|



**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 33


2. Navegador web Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-33-1.png)



34 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-33-0.png)
2. Navegador web Microsoft Edge


**2.5.6 Sección sistema y rendimiento**


Como ya se ha comentado en puntos anteriores, la ejecución de código

en segundo plano después del cierre del navegador Microsoft Edge es

susceptible de uso para ataques maliciosos y debe ser deshabilitada,

para ello, se han de realizar los siguientes pasos:



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-34-2.png)



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-34-0.png)

**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 35



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-34-1.png)
## **3. Lista de** **comprobación**


















|CriticidadAlta|DescripciónMicrosoft Edge debe tener instaladas las últimas actualizaciones de softwarerelacionadas con la seguridad, aplicándolas mediante instalación manual dela última versión disponible para su descarga, la herramienta de actualizaciónautomática de Microsoft Edge, o la herramienta Windows Update del sistemaoperativo Windows.|
|---|---|
|**Alta**|En el caso de que se usen extensiones en el navegador, deberá asegurarse de queestén actualizadas y provengan de fuentes confables.|
|**Media**|Cuando un usuario cambia de una página segura (habilitada para SSL) a unapágina no segura, Microsoft Edge está confgurado para notifcar al usuario.|
|**Media**|Microsoft Edge está confgurado para bloquear ventanas emergentes.|
|**Media**|Se pueden utilizar cuentas de Microsoft y e iniciar sesión para sincronizar losdatos en Microsoft Edge, con una cuenta proporcionada por el usuario.|
|**Media**|Microsoft Edge está confgurado para no autocompletar búsquedas y URLs, sinenviar información al buscador predeterminado.|
|**Media**|Microsoft Edge está confgurado para no guardar las contraseñas de los sitios.|
|**Media**|Microsoft Edge está confgurado para no iniciar sesión automáticamente en laswebs que tiene las credenciales almacenadas.|



36 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge


3. Lista de comprobación












|CriticidadMedia|DescripciónMicrosoft Edge está configurado para no guardar ni autocompletar métodos depago.|
|---|---|
|**Media**|Microsoft Edge está confgurado para permitir que los sitios web no compruebensi hay métodos de pago guardados.|
|**Media**|Microsoft Edge está confgurado para bloquear las cookies de terceros.|
|**Media**|Microsoft Edge está confgurado para no precargar información de las páginas.|
|**Media**|Microsoft Edge está confgurado para permitir que las páginas cerradas no envíeny reciban datos.|
|**Media**|Microsoft Edge está confgurado para no permitir el uso de JavaScript, exceptoque se añada alguna excepción.|
|**Media**|Microsoft Edge está confgurado para no ejecutar aplicaciones en segundo planoal cerrar el navegador.|



**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 37


## **4. Decálogo de** **recomendaciones**

##### A continuación, se indican diez recomendaciones de seguridad en el uso de Microsoft Edge.

38 **CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge


![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-38-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-38-1.png)





**CCN-CERT BP/26:** Recomendaciones de seguridad en Microsoft Edge 39


![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-39-6.png)



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-39-3.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-39-4.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-microsoft-edge/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Microsoft-Edge.pdf-39-5.png)