---
title: "BP/19"
sidebar_label: "BP/19"
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

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-0-1.png)
#### CCN-CERT
# **BP/19**

### **Recomendaciones de** **seguridad en** **Google Chrome**

INFORME DE BUENAS PRÁCTICAS


MAYO **2021**



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-0-0.png)
![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-1-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-1-1.png)



2 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome


## **Índice**



**1.**

**2.**

**3.**


**4.**

**5.**

**Anexo A.**



**Sobre CCN-CERT, CERT Gubernamental Nacional**

**Introducción**

**Navegador web Google Chrome**

3.1 Versiones

3.2 Requisitos mínimos

3.3 Descarga

3.4 Instalación

3.5 Aplicación de configuraciones de seguridad

3.6 Directrices de configuración

3.6.1 Sección Google y tú

3.6.2 Sección autocompletar

3.6.3 Sección privacidad y seguridad

3.6.4 Sección sistema


**Lista de comprobación**

**Decálogo de recomendaciones**

**Archivo de configuración de seguridad**



4

5

6

7

9

10

13

14

16

16

18

21

27


28

29

31



**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 3


## **1. Sobre CCN-CERT,** **CERT Gubernamental** **Nacional**



**El CCN-CERT es**

**la Capacidad de**

**Respuesta a incidentes**

**de Seguridad de la**

**Información del Centro**

**Criptológico Nacional,**

**CCN.**



El **CCN-CERT** es la Capacidad de Respuesta a incidentes de Seguridad

de la Información del Centro Criptológico Nacional, CCN, adscrito al

Centro Nacional de Inteligencia, CNI. Este servicio se creó en el año

2006 como **CERT Gubernamental Nacional español** y sus funciones

quedan recogidas en la Ley 11/2002 reguladora del CNI, el RD 421/2004

de regulación del CCN y en el RD 3/2010, de 8 de enero, regulador del

Esquema Nacional de Seguridad (ENS), modificado por el RD 951/2015

de 23 de octubre.


Su misión, por tanto, es **contribuir a la mejora de la ciberseguridad**

**española**, siendo el centro de alerta y respuesta nacional que coopere

y ayude a responder de forma rápida y eficiente a los ciberataques y a

afrontar de forma activa las ciberamenazas, incluyendo la coordinación

a nivel público estatal de las distintas Capacidades de Respuesta a

Incidentes o Centros de Operaciones de Ciberseguridad existentes.


Todo ello, con el fin último de **conseguir un ciberespacio más seguro**

**y confiable**, preservando la información clasificada (tal y como recoge

el art. 4. F de la Ley 11/2002) y la información sensible, defendiendo

el Patrimonio Tecnológico español, formando al personal experto,

aplicando políticas y procedimientos de seguridad y empleando y

desarrollando las tecnologías más adecuadas a este fin.


De acuerdo a esta normativa y la Ley 40/2015 de Régimen Jurídico

del Sector Público es competencia del CCN-CERT la gestión de

ciberincidentes que afecten a cualquier organismo o empresa pública.

En el caso de operadores críticos del sector público la gestión de

ciberincidentes se realizará por el CCN-CERT en coordinación con el

CNPIC.



4 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome


## **2. Introducción**

**El propósito de este documento consiste en**

**establecer los procedimientos y utilidades**

**necesarias para implementar y garantizar la**

**seguridad en** _**Google Chrome**_ **.**


Para ello, se proporciona un archivo de configuración para aplicar

medidas de seguridad y así facilitar la posibilidad de implementar

seguridad.


Este documento establece un procedimiento para **mejorar la seguridad**

y **proteger el navegador** _Google Chrome_ para mitigar las posibles

vulnerabilidades y los riesgos frente a los que pudiera estar expuesto.


En el desarrollo de esta guía se ha utilizado el instalador del programa

_Google Chrome_ en su **versión 89.0.4389** para sistemas operativos

Windows.


**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 5


## **3. Navegador web** **Google Chrome**

_**Google Chrome**_ **está disponible para su descarga**

**de manera gratuita desde la página web de**

**Google.**


El instalador se descarga y necesita tener conexión a internet para el

proceso de instalación del navegador. Si el equipo en el que se instala

_Google Chrome_ no tiene conexión a internet se necesitará realizar la

descarga completa en el enlace alternativo proporcionado por _Google_

a tal efecto.


En este sentido, _Google Chrome_ debe tener instaladas las últimas

actualizaciones de _software_ relacionadas con la seguridad. Para ello, se

aconseja determinar el método de actualización (por ejemplo, conexión

a un servidor _WSUS_, procedimiento local, actualización automática,

etc.) ya que, si no se aplican las últimas actualizaciones de _software_

relacionadas con la seguridad de Chrome, esto se consideraría un **fallo**

**crítico de seguridad** .


6 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome


3. Navegador web Google Chrome

##### **3.1 Versiones**


**El navegador** _**Google Chrome**_ **dispone de varias**

**versiones. La elección de la versión a instalar**

**dependerá del uso que se vaya a dar.**


**Chrome (Estable)**

Es la **versión oficial**, aquella que utilizarán la mayoría de los usuarios.

Esta versión siempre será la más estable dado que antes de su

publicación es sometida a una completa batería de pruebas. Esta

versión recibe actualizaciones menores cada tres (3) semanas y

actualizaciones mayores cada seis (6) semanas.


**Chrome Beta**

Esta versión se caracteriza por ser una **versión previa a la estable**,

donde se depuran los fallos antes de la publicación de la versión final.

Dicha versión recibe actualizaciones menores todas las semanas y

actualizaciones mayores cada seis (6) semanas.


**Chrome Dev**

**Versión anterior a la beta y menos conocida** ya que se utiliza

principalmente por los **desarrolladores de Google** para las pruebas de

las actualizaciones mayores. En esta versión se finalizan las mejoras

              - nuevas funciones más importantes que estarán disponibles en la

siguiente versión. Esta versión contiene errores, fallos y/o problemas

de compatibilidad, lo que la convierte en una versión inestable. Esta

versión recibe actualizaciones una o dos veces por semana debido a

que muchas de sus funcionalidades están aún en fase de desarrollo.


**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 7



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-6-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-6-1.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-6-2.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-6-3.png)
3. Navegador web Google Chrome


**Chrome Canary**

Esta versión **cuenta con los últimos cambios**, las nuevas

funcionalidades, nuevas herramientas y más opciones, pero **otorgando**

**cierta inestabilidad** al navegador.


Esto lleva a una versión **destinada a identificar los problemas de**

**las nuevas características**, lo que la convierte en una versión muy

inestable. Esta versión se genera automáticamente en los servidores

de Google con los cambios realizados en el código del navegador a

diario. No se recomienda su uso, pero se puede descargar.


**Chrome Empresarial**

Esta versión es el mismo navegador Chrome que se utiliza en la versión

estable. La diferencia está en cómo se despliega y se administra. Los

**administradores de TI pueden descargar esta versión** para instalar

el navegador Chrome a través de un instalador MSI **y administrar los**

**navegadores Chrome de su organización** mediante las políticas de

grupo (actualmente existen más de 200 directivas de configuración).


Para conocer la versión de _Google Chrome_ instalada en un dispositivo

siga los siguientes pasos:


Haga clic sobre el botón  , ubicado en la parte superior derecha

del navegador. A continuación, seleccione la opción “ **Configuración** ” y

posteriormente, en la nueva ventana abierta en el navegador, en el panel

izquierdo pulse sobre la opción “ **Información de Chrome** ”. El número de

la versión instalada se mostrará debajo del nombre de _Google Chrome_,

tal y como se muestra en la siguiente imagen:


**Descripción**


Figura 1


8 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-7-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-7-1.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-7-2.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-7-3.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-7-5.png)
3. Navegador web Google Chrome

##### **3.2 Requisitos mínimos**


A continuación, se detallan los **requisitos mínimos necesarios** del

sistema para realizar la implementación del programa _Google Chrome_

en Windows.


**Sistemas Operativos soportados** (en versiones de 32-bit y 64-bit):


**Windows 7**


**Windows 8 y Windows 8.1**


**Windows 10**


**Windows Server 2008 R2**


**Windows Server 2012 R2**


**Windows Server 2016**


**Hardware recomendado:**


**Pentium 4 o un procesador más moderno que admita**

**SSE2.**


**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 9


3. Navegador web Google Chrome

##### **3.3 Descarga**


A continuación, se detalla el **proceso a seguir** para realizar la **descarga**

del navegador _Google Chrome._






|Paso1.|DescripciónPara la descarga del programa desde la fuente oficial se utilizará el siguienteenlace:https://www.google.com/chrome/browser/desktop/index.html|
|---|---|
|**2.**|La web de descarga detecta automáticamente el sistema operativo instalado enel equipo y la arquitectura de dicho sistema operativo (32 o 64 bits) adecuandolas opciones de instalación tal y como se muestra en la siguiente imagen:Figura 2|



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-9-0.png)

10 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome


3. Navegador web Google Chrome

|Paso3.|DescripciónDesmarque la opción “Ayúdanos a mejorar Google Chrome enviando estadísticasde uso e informes de errores de forma automática”. Posteriormente, pulse sobre elbotón “Descargar Chrome”.Figura 3|
|---|---|
|**4.**|Una vez acabada la descarga aparecerá la siguiente imagen en su navegador:Figura 4|



**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 11



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-10-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-10-1.png)
3. Navegador web Google Chrome



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-11-1.png)







![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-11-0.png)

**Nota: Existe una versión para equipos que no disponen de conexión**

**a internet. Se puede acceder a su descarga desde el enlace oficial:**


**[Enlace: https://www.google.com/intl/es/chrome/browser/](https://www.google.com/intl/es/chrome/browser/desktop/index.html?standalone=1)**

**[desktop/index.html?standalone=1](https://www.google.com/intl/es/chrome/browser/desktop/index.html?standalone=1)**


El proceso de descarga es el mismo que el de la descarga normal, salvo

que en este caso **el archivo a descargar es de mayor tamaño** y llevará

**más tiempo su descarga** .


12 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome


3. Navegador web Google Chrome

##### **3.4 Instalación**





![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-12-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-12-1.png)


|Paso1.|DescripciónEjecute el archivo descargado haciendo doble clic sobre él, ya sea la versión quenecesita conexión a internet o la versión sin conexión a internet.Figura 6|
|---|---|
|**2.**|Para comenzar con la instalación_Google Chrome_ necesita de su autorización.Para ello, pulse “_Sí_” en la siguiente ventana emergente.Figura 7|
|**3.**|Una vez permita la ejecución del programa se instalará automáticamente.**Nota: La instalación de****_Google Chrome_ no permite la personalización de la ruta****de instalación.**|



**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 13


3. Navegador web Google Chrome

##### **3.5 Aplicación de** **configuraciones de** **seguridad**


El archivo “ _master_preferences_ ” ubicado en “ **C:\ProgramFiles\Google\**

**Chrome\Application** ” sirve para personalizar la instalación de _Chrome_

en entorno empresarial. Si se instala una versión _Chrome_ empresarial,

además de poder personalizar la instalación mediante el archivo

“ _master_preferences_ ”, se pueden utilizar plantillas administrativas a

través de la edición de directivas de grupo (GPO) en un controlador de

dominio Windows Server.


_Google Chrome_ dispone de un fichero de configuración llamado

“ _Preferences_ ” donde se almacenan las opciones seleccionadas por el

usuario en este navegador. Para el uso y aplicación de este fichero es

necesario que el navegador esté cerrado. Este fichero se encuentra

ubicado en la ruta:


**C:\Users\\AppData\Local\Google\**

**Chrome\User Data\Default**


Figura 8


14 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-13-0.png)
|GU|Col2|Col3|
|---|---|---|
|Navegador web Googl|||


Para hacer uso del archivo suministrado junto a esta guía, deberá

reemplazar el fichero creado durante la instalación de _Google Chrome_ .

Para esto se deberá copiar el fichero “ **Preferences** ” ubicado en la

carpeta “Scripts” y sustituirlo en la ruta citada anteriormente.


Este fichero cambiará las opciones marcadas y desmarcadas con los

valores de las configuraciones recomendadas en el apartado “ **3.6.**

**DIRECTRICES DE CONFIGURACIÓN** ” de esta guía. Las configuraciones

de personalización de rutas, páginas web y otro tipo de opciones

no se verán afectadas. Si se desea personalizar alguna de estas

**configuraciones personalizadas** (como la URL de inicio, por ejemplo)

se deberán configurar manualmente en el navegador _Google Chrome_ .


**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 15


3. Navegador web Google Chrome

##### **3.6 Directrices de** **configuración**


El navegador _Google Chrome_ dispone de una interfaz gráfica para la

edición de las **opciones del navegador** . Para acceder a esta interfaz se

debe hacer clic sobre el botón     , ubicado en la parte superior derecha

del navegador, y a continuación, seleccionar la opción “ _Configuración_ ”

donde aparecerán las opciones de configuración editables por el

usuario.


Un método alternativo para acceder a la interfaz de configuración es

escribir **chrome://settings/** en la barra de direcciones y pulsar la tecla

“ _Enter_ ”.


**3.6.1 Sección Google y tú**


El navegador _Google Chrome_ permite la **sincronización automática**

**con servicios de Google**, permitiendo a los usuarios, entre otros,

sincronizar automáticamente varios elementos como **marcadores**,

**pestañas abiertas**, **contraseñas**, **complementos**, etc. Esta información

se almacena en la cuenta de Google proporcionada por el usuario a tal

efecto.


**Para evitar problemas de privacidad y seguridad se**

**recomienda deshabilitar esta funcionalidad del navegador.**


16 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome


3. Navegador web Google Chrome


**Se recomienda seguir los siguientes pasos:**


Localice la sección de “ _Google y tú_ ” y haga clic en la parte de **Sincronización**

**y servicios de Google**, tal y como aparece en la siguiente imagen:


Figura 9


En este apartado desmarque las opciones _“Permitir el inicio de sesión en_

_Chrome”_, _“Autocompletar búsquedas y URLs”_, _“Ayudar a mejorar las_

_funciones y el rendimiento de Chrome”_, _“Mejorar las búsquedas y la_

_navegación”_, _“Revisión ortográfica mejorada”_ tal y como se muestra en la

siguiente imagen:


Figura 10


Estos cambios requieren el **reinicio del navegador**, tal y como muestra el

aviso en la parte inferior de la pantalla.


Figura 11


**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 17



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-16-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-16-1.png)
3. Navegador web Google Chrome


**3.6.2 Sección autocompletar**


Debido a la forma en la que se almacenan las credenciales, **es posible**

**que un atacante malicioso pueda obtener acceso a las cuentas** del

usuario y/o utilizar las credenciales almacenadas para inicios de sesión

no deseados.


Para evitar estos usos indebidos **se recomienda deshabilitar las**

**siguientes opciones** :


En el panel izquierdo de la página localice la sección de _“Autocompletar”_ y

haga clic en la parte de contraseñas, tal y como muestra la imagen:


Figura 12


En este apartado **desmarque las opciones** “ _Preguntar si quiero guardar_

_contraseñas_ ” e “ _Iniciar sesión automáticamente_ ”, como se muestra a

continuación:


Figura 13


18 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-17-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-17-2.png)
3. Navegador web Google Chrome


La información referente a los **métodos de pago** es un elemento

atractivo para los atacantes buscando hacer un **uso fraudulento**

**de la misma** y, por ello, **se recomienda no tener almacenada esta**

**información** en el navegador Google Chrome para evitar ser objeto de

ataques maliciosos.


Se recomienda realizar los siguientes pasos:


Dentro de la sección “ _Autocompletar_ ”, haga clic en el apartado _“Métodos de_

_pago”_, como se muestra en la imagen.


Figura 14


En este apartado **desmarque las opciones** “ _Guardar y autocompletar_

_métodos de pago_ ” y “ _Permitir a los sitios comprobar si tienes métodos de_

_pago guardados_ ” siguiendo de referencia la siguiente imagen.


Figura 15


**La información**

**referente a los**

**medios de pago es**

**un elemento atractivo**

**para los atacantes**

**y se recomienda no**

**tener almacenada**

**esta información en**

**el navegador Google**

**Chrome.**


**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 19



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-18-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-18-2.png)
3. Navegador web Google Chrome


Al igual que en el caso anterior el **almacenamiento de información**, aun

no siendo crítico, puede ofrecer a un atacante información relevante

sobre los **movimientos, acciones u otras consideraciones** del usuario.


Para evitar el uso de esta información, se recomienda **inhabilitar** la

siguiente opción:


Dentro de la sección _“Autocompletar”_ haga clic en el apartado _“Direcciones_

_y más”_ .


Figura 16


En este apartado **desmarque la opción** _“Guardar y autocompletar_

_direcciones”_, como se muestra a continuación:


Figura 17


20 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-19-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-19-2.png)
3. Navegador web Google Chrome


**3.6.3 Sección privacidad y seguridad**


La configuración de las cookies [1] y los envíos de **información en segundo**

**plano** son una parte muy importante para la seguridad y privacidad.

Con una configuración segura de estos elementos se pueden prevenir

brechas de seguridad y posibles robos de información sensible, ya que

un atacante podría ocultar la ejecución de código malicioso mediante

el tráfico en segundo plano del navegador.


Para evitar estos riesgos, se recomienda la siguiente configuración

para el navegador _Google Chrome_ :


En la sección de “ _Privacidad y seguridad_ ”, en el panel izquierdo de la página,

haga clic en el apartado “ _Cookies y otros datos de sitios_ ”, tal y como se

muestra a continuación:


Figura 18


Se deben definir algunas configuraciones para que cuando se termine de

navegar, y se proceda al cierre del navegador, **se eliminen los ficheros**

**generados por el navegador durante su ejecución** . Esto favorece la carga,

en siguientes ocasiones cuando se visite el sitio, de las últimas versiones

de las páginas visitadas, así como la configuración actualizada para el

sitio web mejorando así la seguridad general de la navegación.


**1.** Archivo generado por un servidor web y que guarda datos de la navegación para hacer que la experiencia del usuario sea más
sencilla con información sobre sus preferencias y pautas de navegación.


**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 21



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-20-0.png)
3. Navegador web Google Chrome


Para poder proceder a estas configuraciones acceda al apartado “ _Cookies_

_y otros datos de sitios_ ” en la sección izquierda del navegador. Una vez allí,

**marque las siguientes opciones** tal y como aparece en la imagen:


Figura 19


**Nota: Hay algunas páginas que necesitan cookies de terceros para su**

**correcto funcionamiento. Si se detecta que una página no funciona**

**como se espera, es posible que se necesite habilitar las cookies de**

**terceros para su correcto funcionamiento. Para ello, puede generar una**

**excepción de cookies de terceros sobre ciertas páginas para mejorar su**

**experiencia de uso, tal y como se aprecia en la siguiente imagen.**


Figura 20


22 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-21-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-21-1.png)
3. Navegador web Google Chrome


Dentro de la sección “ _Privacidad y seguridad_ ”, concretamente en el

apartado “ _Seguridad_ ” se recomienda activar la pestaña llamada “ _Protección_

_mejorada_ ”. Esta protección que ofrece el navegador _Google Chrome_

incluye, entre otras, las siguientes características:


Figura 21


Para obtener esta protección **deberá activar la opción** “ _Protección_

_mejorada_ ” tal y como se muestra en la siguiente imagen.


Figura 22


**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 23



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-22-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-22-1.png)
3. Navegador web Google Chrome


Por último, la funcionalidad _“Usar DNS seguro”_, viene activa de forma

predeterminada. Sin embargo por defecto se hace uso del DNS de proveedor

de servicio actual, lo que puede provocar el intento de conexiones no

seguras contra un sitio web debido a interrupciones del servicio.


Por ello es posible establecer uno de los DNS facilitados por Google e

incluso uno personalizado si se encuentra en un entorno empresarial.


Figura 23


Continuando con las configuraciones dentro del apartado de _“Privacidad_

_y seguridad”_, se deberán cambiar algunos aspectos para evitar ataques

en ventanas minimizadas, ventanas en segundo plano, y ejecuciones de

código mediante _JavaScript_, que normalmente se utilizan para realizar

ataques maliciosos.


Para limitar lo indicado anteriormente, acceda al apartado “ _Configuración_

_de sitios_ ” tal y como se muestra a continuación:


Figura 24


24 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-23-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-23-1.png)
3. Navegador web Google Chrome


En este apartado modifique los aspectos referentes a _“Sincronización_

_en segundo plano”_ del tal modo que no permitan que los sitios cerrados

recientemente terminen de enviar y recibir datos, como aparece en la

siguiente imagen:


Figura 25


**Nota: En la mayoría de los casos, JavaScript deberá mantenerse**

**habilitado para disponer de una funcionalidad completa en las páginas**

**web que se visitan. Sin embargo, en algunos entornos empresariales**

**en donde se requieran niveles de seguridad mejorados, se recomienda**

**revisar esta configuración y bloquear el uso de JavaScript para evitar**

**ataques de ejecución de código, añadiendo las excepciones en aquellos**

**sitios que sean necesarios para la organización.**


Figura 26


**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 25



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-24-0.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-24-1.png)
3. Navegador web Google Chrome


Para terminar las con iguraciones dentro del apartado de _“Privacidad_

_y seguridad”_, se deberán cambiar algunos aspectos relativos al uso de

elementos de comunicación hardware del equipo.


Esto permitirá establecer una configuración de privacidad adecuándose a

las necesidades del usuario. Por defecto se bloquearán las configuraciones

de _“Ubicación”_, _“Cámara”_, _“Micrófono”_ y _“Notificaciones”_ . Así mismo

se limitarán todos los elementos incluidos en el apartado _“Permisos_

_Adicionales”_ .


Esta configuración podrá ser modificada añadiendo excepciones a los

sitios web que requieran el uso de estos elementos.


Figura 27


**Nota: Adicional a esta configuración dentro del apartado general,**

**“Buscador”, es recomendable revisar regularmente la configuración**

**establecida, eliminando si existiese algún buscador desconocido. En**

**todo caso, es recomendable eliminar aquellos buscadores que no vayan**

**a ser utilizados.**


26 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-25-1.png)
3. Navegador web Google Chrome


**3.6.4 Sección sistema**


Como ya se ha comentado en puntos anteriores, la **ejecución de**

**código en segundo plano** después del cierre del navegador _Google_

_Chrome_, es susceptible de uso para ataques maliciosos y deben ser

deshabilitados.


En la sección de “ _Sistema_ ”, dentro de la pestaña “ _Configuración avanzada_ ”

en el panel izquierdo de la página de “ _Configuración_ ”, deshabilite la opción

“ _Seguir ejecutando las aplicaciones en segundo plano al cerrar Google_

_Chrome_ ”, como se muestra en la siguiente imagen.


Figura 28


**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 27



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-26-0.png)
## **4. Lista de** **comprobación**






































|CriticidadAlta|DescripciónGoogle Chrome debe tener instaladas las últimas actualizaciones de softwarerelacionadas con la seguridad.|
|---|---|
|**Alta**|En el caso de uso de extensiones dentro del navegador deberá comprobar queestén actualizadas la última versión y que provienen de fuentes confables.|
|**Media**|Las preferencias de seguridad requeridas por_Google Chrome_ no pueden sercambiadas por el usuario.|
|**Media**|_Google Chrome_ está confgurado para actualizarse de forma automática.|
|**Media**|_Google Chrome_ está confgurado para proporcionar advertencias cuando unusuario cambia de una página segura (habilitada para SSL) a una página nosegura.|
|**Media**|_Google Chrome_está confgurado para bloquear ventanas emergentes.|
|**Media**|_Google Chrome_está confgurado para no utilizar cuentas de Google y no poderiniciar sesión en los servicios de Google con una cuenta proporcionada por elusuario.|
|**Media**|_Google Chrome_ está confgurado para no autocompletar búsquedas y URLs, sinenviar información al buscador predeterminado.|
|**Media**|_Google Chrome_ está confgurado para no guardar las contraseñas de los sitios.|
|**Media**|_Google Chrome_ está confgurado para no iniciar sesión automáticamente en laswebs que tiene las credenciales almacenadas.|
|**Media**|_Google Chrome_ está confgurado para no guardar ni autocompletar métodos depago.|
|**Media**|_Google Chrome_ está confgurado para permitir que los sitios web no compruebensi hay métodos de pago guardados.|
|**Media**|_Google Chrome_ está confgurado para bloquear las cookies de terceros.|
|**Media**|_Google Chrome_ está confgurado para no precargar información de las páginas,incluso sin haberlas visitado. Esta precarga puede incluir cookies si estánpermitidas.|
|**Media**|_Google Chrome_ está confgurado para permitir que las páginas cerradas no envíeny reciban datos.|
|**Media**|_Google Chrome_ está confgurado para permitir el uso de JavaScript.|
|**Media**|_Google Chrome_ está confgurado para no ejecutar aplicaciones en segundo planoal cerrar_Google Chrome_.|



28 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome


## **5. Decálogo de** **recomendaciones**

##### A continuación, se indican diez (10) recomendaciones de seguridad en el uso de Google Chrome .

**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 29


![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-29-0.png)





Figura 29. Decálogo de recomendaciones

30 **CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome


## **Anexo A.** **Archivo de** **configuración** **de seguridad**

Para facilitar la aplicación del refuerzo de estas medidas de seguridad

sobre _Google Chrome_, se incluye adjunto al documento un archivo

“ _Preferences_ ” para la configuración inicial del navegador. Todas estas

configuraciones son modificables por el usuario y se almacenaran en

la carpeta por defecto del navegador.


Acuda al apartado “ **3.5. APLICACIÓN DE CONFIGURACIONES**

**DE SEGURIDAD** ” para conocer cómo implantar este archivo de

configuración dentro de _Google Chrome_ .


**CCN-CERT BP/19:** Recomendaciones de seguridad en Google Chrome 31


![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-31-5.png)



![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-31-3.png)

![](/img/ccn-cert-bp-19-recomendaciones-de-seguridad-en-google-chrome/CCN-CERT_BP-19-Recomendaciones-de-seguridad-en-Google-Chrome.pdf-31-4.png)