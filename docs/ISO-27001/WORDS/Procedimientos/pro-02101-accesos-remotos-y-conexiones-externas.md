---
id: pro-021-01_accesos-remotos-y-conexiones-externas
title: "Pro 021.01 Accesos Remotos Y Conexiones Externas"
sidebar_label: "Pro 021.01 Accesos Remotos Y Conexiones Externas"
---

PROCEDIMIENTO DE CONTROL DE ACCESOS REMOTOS Y EXTERNOS
## OBJETIVO
Este procedimiento establece los requisitos y características mínimas que deberán disponer los controles de acceso remotos para los sistemas de información/aplicaciones de SPIKA TECH.
## ALCANCE
Este procedimiento será de aplicación para los proveedores y por las personas empleadas de SPIKA TECH en el cumplimiento de las funciones que tengan asignadas como parte de su desempeño profesional, así como a la totalidad de los recursos corporativos que permiten el acceso a los sistemas recogidos en el alcance y que sean utilizados para llevar a cabo dichas funciones.
## ROLES Y RESPONSABILIDADES
Responsable de Seguridad / SGSI Autorizar conexiones sobre servicios nuevos y la tipología de conexión.
Responsable de la solicitud (Responsable de Servicio o equivalente, o superior jerárquico)
Autorizar conexiones de acceso remoto con las características requeridas.
Solicitar Altas, Bajas o Modificaciones de las conexiones de acceso remoto.
Usuario Destinatario final de la conexión remota.
Área de Ciberseguridad / Informática:
Asignación de los servicios especificados en el formulario de solicitud de conexión remota incluyendo al usuario en los grupos pertinentes.
Gestionar las solicitudes de acceso remoto: altas, bajas o modificación de características.
Proteger las autorizaciones de acceso remoto.
Evalúa las solicitudes de acceso remoto con necesidades de conexión fuera de los perfiles establecidos en la política corporativa de acceso remoto cuando se tengan dudas sobre su idoneidad.
Participan en aquellas solicitudes complejas o que tienen algún tipo de incidencia.
## GESTIÓN DE LAS CONEXIONES REMOTAS
## ALTA
Para solicitar el alta a cualquier tipo de conexión, será necesario que el Responsable de la Solicitud, pida la correspondiente conexión a través de solicitud mediante correo electrónico (incidencias@spikatech.com) y registre la solicitud de servicio correspondiente.
Esta solicitud será emitida por el responsable de la persona que necesita acceso de acuerdo a las necesidades que considere para el desarrollo de las funciones que son de su competencia.
Es responsabilidad del área de ciberseguridad mapear los servicios especificados en el formulario de solicitud de conexión remota a las direcciones IP y puertos correspondientes.
## PERIODO DE VALIDEZ
Los accesos remotos de tipo no tendrán una caducidad preestablecida, sino que estarán ligados a la continuidad o no del usuario en su prestación del servicio o con el desarrollo de sus funciones, es decir, si cambian las características del puesto, la modificación de los accesos cambiará, o si cesa en el mismo se deshabilitará y suprimirá.
## MODIFICACIONES EN EL ACCESO REMOTO
Cuando los usuarios requieran cambios en las características de su conexión remota, dicho cambio será tratado como una nueva solicitud corporativa de acceso remoto. Para ello se utilizará el formulario de solicitud, cumplimentado de la misma forma que si se tratara de un registro, indicando que se trata de una modificación de una conexión existente y las características que se desea modificar.
## BLOQUEO
Las conexiones están monitorizadas por lo que cualquier anomalía o incidencia queda registrada, en las diferentes herramientas existentes.
Cualquier incumplimiento de las normas contenidas en la política de acceso remoto o en la normativa vigente de SPIKA TECH, dará lugar al bloqueo de la conexión, notificándoselo al usuario de dicha conexión.
## BAJA
Un acceso remoto corporativo será eliminado en los siguientes casos:
Caducidad del plazo de vigencia de las mismas, sin solicitud de renovación.
Presentación por parte del responsable de la autorización del formulario de solicitud con cancelación del acceso del usuario indicado, por ejemplo, en el caso de cese de la relación laboral.
## TIPOS DE CONEXIONES EXTERNAS
Los accesos externos desde al SPIKA TECH pueden ser realizarse de las siguientes formas y con las siguientes medidas de seguridad:
## EQUIPO CORPORATIVO
Todos los equipos corporativos contienen una configuración que incluye al menos:
Medidas específicas de seguridad.
Herramientas corporativas instaladas por defecto.
Escritorios virtuales.
Disco cifrado.
Actualizaciones y políticas de seguridad centralizadas.
Control de instalación de aplicaciones.
Doble factor de autenticación de usuarios.
## USUARIO NO REALIZA CONEXIÓN A SPIKA TECH
El usuario puede trabajar desde el portátil corporativo a distancia. Las aplicaciones que vienen instaladas por defecto no requieren de doble factor de autenticación, sin embargo, aquellas aplicaciones a las que se accede desde internet requerirán doble factor para cada una de ellas.
## ACCESO MEDIANTE NAVEGADOR WEB DESDE EQUIPO PERSONAL
Acceso a través de cualquier navegador web a las aplicaciones disponible en internet. Se necesitará el doble factor de autenticación para cada aplicación a la que se vaya a conectar.
En este caso, se aísla la plataforma de acceso de la red corporativa impidiendo que las vulnerabilidades presentes en el cliente pongan en riesgo a los sistemas corporativos.
## CONEXIÓN VPN
La conexión a la VPN es obligatoria VPN para aquellas conexiones a aplicaciones desde las que se requiera acceso a través de internet. Se solicitará doble factor de autenticación cuando se conecta la VPN.
Cuando se vaya a hacer uso de una conexión VPN, se tendrán en cuenta las siguientes medidas de seguridad complementarias:
Restringir las direcciones IP desde donde se van a originar las conexiones.
Disponer de un mecanismo de doble factor de autenticación.
Es importante tener en cuenta que la gran mayoría de los usuarios contarán con conexiones a Internet con direccionamiento IP dinámico, por lo tanto, es probable un aumento de la gestión administrativa diaria para poder autorizar de nuevo cada una de las nuevas direcciones IP que presentan los usuarios.
Almacenar los registros de auditoría asociados a las conexiones almacenando los siguientes datos:
Dirección IP origen y destino de las conexiones.
Hora inicio y de fin de la conexión.
Usuario.
Comandos ejecutados.
Ficheros ejecutados o accedidos.
Utilizar la última versión del cliente VPN.
## ACCESO EXTERNO A LAS REDES CORPORATIVAS
Sólo los usuarios autorizados podrán utilizar el servicio VPN, quienes serán además los responsables del correcto uso del servicio de acceso remoto.
Será responsabilidad del usuario con privilegios VPN, asegurarse de que ninguna otra persona utilice su cuenta de acceso, entendiendo que es de uso exclusivo para quienes se les ha asignado dichos privilegios.
Se controlará el uso del sistema VPN, utilizando una contraseña de autenticación fuerte, que será mantenida siempre en secreto.
Cuando se esté conectado activamente a la red de SPIKA TECH vía VPN, se permitirá el tráfico de acuerdo con el perfil del usuario hacia y desde el ordenador o través del túnel VPN, el resto del tráfico pasará por la conexión respectiva.
Sólo se permitirá una conexión, no estará permitida la multiplicación paralela de túneles.
Las puertas de enlace VPN serán configuradas y administradas por el área de ciberseguridad:
Todos los ordenadores y dispositivos conectados a las redes internas de SPIKA TECH mediante VPN o cualquier otra tecnología, deberán utilizar el antivirus al máximo nivel de actualización.
Los usuarios de VPN serán automáticamente desconectados de la sesión una vez hayan transcurrido 8 horas de inactividad. El usuario deberá logarse nuevamente para volver a conectarse a la red de SPIKA TECH. No se deberán utilizar tácticas artificiales como “ping” para mantener la sesión abierta.
Los usuarios de equipos informáticos que no sean de SPIKA TECH que se conecten vía VPN, deberán cumplir todas las directrices establecidas en la normativa de SPIKA TECH y además firmar un acuerdo de confidencialidad de la información, así como cumplir con la cláusula de seguridad del contrato establecido con SPIKA TECH.
Mediante el uso de la tecnología VPN los usuarios deberán conocer qué equipo, ya sea corporativo o personal, es una extensión de las redes de SPIKA TECH, y, como tales, estarán sujetos a las mismas normas y reglamentos que se aplican a los equipos de las propias instalaciones de SPIKA TECH.
## ACCESO REMOTO
## PERSONAL DE SPIKA TECH
El acceso remoto a los recursos de sistemas y red será autorizado, siempre que esté justificado normalmente y aprobado por el gestor inmediato de acuerdo con los siguientes requisitos:
Debe ser segregado por niveles de acceso según el perfil del usuario.
El acceso a debe hacerse solamente con equipos que estén preferiblemente plataformados, salvo que sean personales del usuario y se sigan las directrices sobre el uso de dispositivos personales (BYOD)
En todas las conexiones se usará un segundo factor de autenticación, que será individual y personal.
Las configuraciones de acceso remoto deben hacerse de forma que no permitan acceso ilimitado al SPIKA TECH y a sus aplicaciones.
## PROVEEDORES
No deben liberarse accesos remotos cliente a sitio para subcontratados. Las excepciones deben ser analizadas por el Responsable de Seguridad. El acceso remoto a los recursos de sistemas y red (sitio a sitio) será autorizado solamente para los siguientes casos, siempre que sea justificado formalmente y aprobado por el gestor inmediato según los siguientes requisitos:
Debe ser segregado por niveles de acceso según el perfil del usuario.
Debe hacerse solamente por medio de equipos que estén en conformidad con las directrices de seguridad de SPIKA TECH.
Debe utilizarse un segundo factor de autenticación (p.ej.: token), que será individual y personal.
Las configuraciones de acceso remoto deben hacerse de forma que no permitan acceso incondicional.
SPIKA TECH podrá, a su criterio, solicitar un estudio de la infraestructura de la empresa de la Subcontratada, así como solicitar modificaciones para la adecuación a los niveles de Seguridad establecidos por sus directrices y solamente después de las adecuaciones, conceder el acceso remoto.
## REFERENCIAS
ISO/ IEC 27001:2022:
5.18 Derechos de acceso
8.5 Autenticación segura
Medidas de seguridad para acceso remoto (CCN).

| HISTORIAL DEL DOCUMENTO | HISTORIAL DEL DOCUMENTO | HISTORIAL DEL DOCUMENTO | HISTORIAL DEL DOCUMENTO |
| Versión | Resumen de modificaciones | Fecha de entrada | Sustituye a (Código, revisión) |
| 01 | Primera versión del documento. | 26/02/2025 | N/A |

| REGISTRO DE FIRMAS | REGISTRO DE FIRMAS | REGISTRO DE FIRMAS | REGISTRO DE FIRMAS |
| Función: | Elaborado por: | Revisado por: | Aprobado por: |
| Departamento: | Responsable del SGSI | Dirección | Jefe de seguridad

(o suplente) |

| Nombre: | David Pozo | Carlos Rodrigo | Carlos Zúñiga |
| Firma: |  |  |  |
| Fecha: | 26/02/2025 | 26/02/2025 | 26/02/2025 |