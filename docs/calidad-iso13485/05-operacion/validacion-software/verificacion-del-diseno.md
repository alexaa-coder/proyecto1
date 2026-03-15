---
title: "VERIFICACIÓN DEL DISEÑO"
sidebar_label: "VERIFICACIÓN DEL DISEÑO"
responsable: "Director de Calidad"
clasificacion: "USO INTERNO"
fecha_revision: "2026-03-15"
idioma: "es"
tags:
  - calidad
  - english
  - iso-13485
  - operacion
  - procedimiento
---

**ANEXO 2/01**

# VERIFICACIÓN DEL DISEÑO













Código
Requerimiento de usuario
Acciones Propuestas
Acción realizada
Persona que verifica y aprueba
Firma
Fecha




DOR-01
VRC-01
Crear un sistema de autentificación única de usuarios
Se ha creado un sistema de autentificación de usuarios basada en un
correo electrónico y una contraseña dentro de la aplicación
Javier Vico

07/02/2023


DOR-02
VRC-01
Crear un sistema de autentificación única de usuarios
Se ha desarrollado una API que gestiona el acceso de los usuarios
mediante el uso de un correo electrónico y la contraseña
Carlos Rodrigo

07/02/2023


DOR-03
VRC-02
Crear un espacio para el uso de la herramienta de forma
individual
Se ha creado una ramificación del código que permite ejecutar toda
la herramienta para un solo usuario en local
Javier Vico

29/03/2023


DOR-04
VRC-03
Crear un sistema que permita conectar a varios usuarios en tiempo
real dentro de la herramienta desde diferentes dispositivos
Se ha creado una ramificación del código que crea una sala a la que
se pueden conectar diferentes dispositivos que dispongan de la
herramienta de visualización y permiso por parte del creador de la sala
para poder unirse
Daniel Cámara

11/04/2023


DOR-05
VRC-04
Elaborar un protocolo de comunicación online que permita a los
usuarios comunicarse con otros usuarios de la misma sala
Se ha creado un sistema de comunicación que permite a los diferentes
usuarios de las salas online comunicarse entre ellos en tiempo real
mediante voz
Javier Vico

08/05/2023


DOR-06
VRC-05
Desarrollar un protocolo de comunicación online en tiempo real para
el paso de información entre usuarios
Se ha creado un sistema de comunicación que permite a los diferentes
usuarios de las salas online compartir información entre ellos en tiempo
real
Daniel Cámara

22/05/2023


DOR-07
VRC-06
Crear una llamada a la base de datos con los datos identificativos
de cada usuario para poder obtener una lista con todos los casos
pertenecientes al usuario correspondiente
Se ha desarrollado una interfaz en la aplicación que permite hacer
una llamada a la API para obtener un resultado de casos en forma de
lista.
Javier Vico

05/06/2023


DOR-08
VRC-06
Crear una llamada a la base de datos con los datos identificativos
de cada usuario para poder obtener una lista con todos los casos
pertenecientes al usuario correspondiente
Se ha desarrollado una API conectada con la base de datos en la que
se almacenan todos los casos para poder listarlos cuando se realiza la
petición desde la aplicación
Carlos Rodrigo

05/06/2023


DOR-09
VRC-06
Crear una llamada a la base de datos con los datos identificativos
de cada usuario para poder obtener una lista con todos los casos
pertenecientes al usuario correspondiente
Se ha diseñado un algoritmo de aprendizaje profundo que es capaz de
filtrar las señales recogidas mediante el dispositivo de adquisición de
datos para su correcta visualización.
Vicente Gallego

05/06/2023


DOR-10
VRC-07
Crear una serie de filtros para poder buscar de forma óptima entre
la lista de casos obtenida anteriormente
Se ha creado un sistema de filtros en la aplicación de visualización
en la que se incluyen diferentes parámetros que seleccionan exactamente
los casos que el usuario quiere visualizar
Daniel Cámara

26/06/2023


DOR-11
VRC-07
Crear una serie de filtros para poder buscar de forma óptima entre
la lista de casos obtenida anteriormente
Se ha desarrollado una API conectada con la base de datos en la que
se almacenan todos los casos para poder listarlos en función de los
filtros seleccionados
Carlos Rodrigo

26/06/2023


DOR-12
VRC-08
Crear acción de llamada a la base de datos que devuelva el fichero
descargable con la información que se va a visualizar
Se ha desarrollado una interfaz en la aplicación que permite la
descarga de los casos de la nube
Javier Vico

10/07/2023


DOR-13
VRC-08
Crear acción de llamada a la base de datos que devuelva el fichero
descargable con la información que se va a visualizar
Se ha desarrollado un sistema dentro de la API que permite la
descarga de los casos desde la nube, proporcionando a la aplicación un
enlace de descarga temporal
Carlos Rodrigo

10/07/2023


DOR-14
VRC-09
Desarrollar una herramienta en la que se pueda visualizar el corazón
y el torso de cada sesión grabada
Se ha desarrollado un algoritmo que resuelve el problema inverso,
para con los parámetros proporcionados, generar una reconstrucción del
corazón y torso del paciente
Vicente Gallego

30/08/2023


DOR-15
VRC-09
Desarrollar una herramienta en la que se pueda visualizar el corazón
y el torso de cada sesión grabada
Se ha desarrollado una herramienta que permite descargar los datos
de cada sesión grabada, generar un torso y un corazón a partir de los
datos grabados y visualizarlos en tres dimensiones
Daniel Cámara

30/08/2023


DOR-16
VRC-10
Desarrollar la herramienta de visualización para poder ver la
representación del voltaje en cada punto del corazón
Se ha desarrollado un algoritmo que permite identificar, a partir de
los datos adquiridos, el voltaje exacto de cada punto del corazón a lo
largo del tiempo
Vicente Gallego

26/09/2023


DOR-17
VRC-10
Desarrollar la herramienta de visualización para poder ver la
representación del voltaje en cada punto del corazón
Se ha desarrollado una herramienta que permite visualizar el voltaje
recogido en cada punto del corazón mediante la adquisición previa de
datos a lo largo del tiempo
Javier Vico

26/09/2023


DOR-18
VRC-11
Desarrollar la herramienta de visualización para poder ver la
representación de la señal en cada punto del corazón
Se ha desarrollado un algoritmo que permite identificar, a partir de
los datos adquiridos, la señal cardíaca exacta de cada punto del corazón
a lo largo del tiempo
Vicente Gallego

17/10/2023


DOR-19
VRC-11
Desarrollar la herramienta de visualización para poder ver la
representación de la señal en cada punto del corazón
Se ha desarrollado una herramienta que permite visualizar la señal
cardíaca recogida en cada punto del corazón mediante la adquisición
previa de datos
Daniel Cámara

17/10/2023


DOR-20
VRC-12
Crear un panel dentro de la pantalla de la herramienta que permita
ver diferentes señales cardíacas
Se ha creado un elemento dentro de la herramienta que permite
visualizar 10 señales cardíacas obtenidas al mismo tiempo
Javier Vico

06/11/2023


DOR-21
VRC-12
Crear un panel dentro de la pantalla de la herramienta que permita
ver diferentes señales cardíacas
Se ha desarrollado un algoritmo que permite recopilar todas las
señales cardíacas adquiridas para procesarlas y mostrarlas en la
aplicación de visualización
Vicente Gallego

06/11/2023


DOR-22
VRC-13
Crear una serie de controladores dentro de la herramienta que
permita modificar la representación de la información
Se ha creado una serie de controladores dentro de la herramienta que
permite modificar la información representada del corazón generado
Javier Vico

05/12/2023


DOR-23
VRC-14
Crear un controlador que permita modificar morfológicamente el
corazón simulando un latido real
Se ha creado un botón dentro de la herramienta que permite activar y
desactivar la deformación morfológica del corazón generado para simular
un latido real
Daniel Cámara

18/12/2023


DOR-24
VRC-15
Crear un controlador que permita cambiar entre diferentes mapas de
visualización
Se ha creado un botón con el que interactuar que permite cambiar el
corazón y el torso visualizados desde un mapa para visualizarlo de
formas diferentes
Javier Vico

10/01/2024


DOR-25
VRC-15
Crear un controlador que permita cambiar entre diferentes mapas de
visualización
Se ha desarrollado un algoritmo que permite al corazón y torsos
generados, agregarles diferentes mapas de visualización
Vicente Gallego

10/01/2024


DOR-26
VRC-16
Crear un controlador móvil que permita medir el tiempo transcurrido
en las señales cardíacas
Se ha creado un medidor dentro de la herramienta que permite medir
el tiempo transcurrido en las señales cardíacas
Javier Vico

22/01/2024


DOR-27
VRC-17
Crear dos controladores que permitan ampliar la visualización de las
señales cardíacas
Se ha creado un controlador dentro de la herramienta que permite
aumentar la amplitud de las señales cardíacas visualizadas
Daniel Cámara

29/01/2024


DOR-28
VRC-18
Crear un reproductor dentro de la herramienta que permita controlar
el tiempo
Se ha creado una serie de botones con los que interactuar que
permiten controlar el tiempo de reproducción de la animación del corazón
generado
Javier Vico

29/01/2024


DOR-29
VRC-19
Crear una animación que permita introducir el corazón generado del
paciente dentro del torso generado
Se ha creado un botón interactuable que inicia una animación en la
que el corazón generado se introduce en la posición exacta dentro del
torso para representar la ubicación del corazón de la persona
correspondiente
Javier Vico

14/02/2024


DOR-30
VRC-19
Crear una animación que permita introducir el corazón generado del
paciente dentro del torso generado
Se ha mejorado el algoritmo de generación del corazón y el torso
para la obtención exacta de la posición y rotación del corazón dentro
del torso
Vicente Gallego

14/02/2024


DOR-31
VRC-20
Desarrollar un sistema de elección de electrodos dentro del torso
para seleccionar la señal obtenida por cada electrodo específico
Se ha creado un sistema de puntos correspondientes a cada electrodo
del sistema de adquisición de datos colocados sobre el torso generado
que permite interactuar con cada punto para iluminar y seleccionar la
señal cardíaca que corresponde al electrodo de cada punto
Daniel Cámara

26/02/2024


DOR-32
VRC-20
Desarrollar un sistema de elección de electrodos dentro del torso
para seleccionar la señal obtenida por cada electrodo específico
Se ha desarrollado un algoritmo que procesa todas las señales
cardíacas obtenidas y produce una tabla en la que se ubica la posición
el electrodo que ha recogido cada señal y el índice de este
Vicente Gallego

26/02/2024


DOR-33
VRC-21
Desarrollar un sistema que permita la visualización del corazón
generado del paciente en una pantalla holográfica externa de la
herramienta
Se ha desarrollado una herramienta externa con una pantalla que
permite la visualización del corazón generado de forma holográfica en
tres dimensiones
Daniel Cámara

12/03/2024


DOR-34
VRC-22
Adaptar la cámara para que pueda verse desde unas gafas de realidad
virtual.
Se ha adaptado la cámara que se usa para la visualización de la
escena en la herramienta para que pueda ser cargada y visualizada en
unas gafas de realizad virtual
Daniel Cámara

19/03/2024


DOR-35
VRC-23
Crear un sistema de almacenamiento en la base de datos de toda la
configuración del espacio de trabajo de cada usuario
Se ha desarrollado una API que permite gestionar todas las
peticiones desde la aplicación para guardar la información
correspondiente en la base de datos
Carlos Rodrigo

27/03/2024


DOR-36
VRC-23
Crear un sistema de almacenamiento en la base de datos de toda la
configuración del espacio de trabajo de cada usuario
Se ha desarrollado una interfaz en la herramienta de visualización
para gestionar las peticiones del usuario de almacenar su espacio de
trabajo
Javier Vico

27/03/2024