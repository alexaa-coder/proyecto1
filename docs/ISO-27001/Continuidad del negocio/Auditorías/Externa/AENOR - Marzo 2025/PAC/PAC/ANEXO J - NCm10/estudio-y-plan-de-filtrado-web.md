---
id: estudio-y-plan-de-filtrado-web
title: "Estudio Y Plan De Filtrado Web"
sidebar_label: "Estudio Y Plan De Filtrado Web"
---

# Estudio y Plan de Filtrado Web
## TABLA DE CONTENIDO
1. Objetivo 2. Requerimientos mínimos
3. Opciones evaluadas 4. Elección y justificación
5. Plan de implantación Alta y configuración inicial
Políticas DNS básicas Políticas por categoría
Listas negras/whitelist Logs y retención
Pruebas Mantenimiento
6. Configuración mínima de políticas 7. Evidencias para auditoría
8. Lista de bloqueos Pornografía / Adult
Torrents / Piratería / P2P Gambling / Apuestas
File-sharing públicos / riesgo de fuga de datos Proxy / Anonymizer / Shorteners
### 1. Objetivo
Garantizar que el acceso a Internet se controla para bloquear sitios peligrosos o no autorizados, proteger la red y generar evidencias (logs e informes) para auditoría ISO 27001.
### 2. Requerimientos mínimos
- Bloqueo por categoría (malware, phishing, pornografía, torrents, gambling, etc.).
- Bloqueo por lista negra (dominios concretos).
- Registro de logs de consultas/denegaciones (retención mínima 90 días).
- Capacidad de excepciones (whitelist) para dominios de negocio (p. ej. Microsoft O365).
- Opciones de despliegue: DNS (fácil) y/o agente/proxy (inspección HTTPS).
### 3. Opciones evaluadas
- Cloudflare Gateway (Recomendado) — DNS + proxy, integración Zero Trust, plan gratuito/low
cost para pequeñas organizaciones; fácil onboarding y visibilidad. Ideal para &lt;10 usuarios.
- DNSFilter — DNS filtering con categorización y ML, buena para SMBs que quieren simplicidad.
- WebTitan / OpenDNS (Cisco Umbrella) — robustos, muy usados por MSPs; suelen tener mayor
coste por usuario.
- Pi-hole (DIY) — gratuito, local; requiere conocimientos para mantener listas y alta disponibilidad; no es ideal si necesitáis soporte comercial.
### 4. Elección y justificación
Cloudflare Gateway:
- Oferta adecuada para pequeñas organizaciones (fácil registro y plan gratuito/low cost para
comenzar).
- Permite aplicar políticas por usuario/dispositivo (agente) o por red (resolver DNS).
- Soporta bloqueo por categoría + listas negras personalizadas + logs, con capacidad de integración con SIEM si queréis en el futuro.
[contact@spikatech.com - www.spikatech.com](mailto:contact@spikatech.com)
SPIKA TECH, S.L., with registered office at c/ Alcalá de Guadaira, nº 6, 6ºA Derecha, 28018 MADRID, with Tax Identification Code B87386900, registered in the Mercantile Register of Madrid, in volume 33.500, Folio 200, Page M-603059, Entry. 1, hereinafter THE OWNER.
### 5. Plan de implantación
#### Alta y configuración inicial
Crear cuenta Cloudflare for Teams y definir la organización. (usuarios &lt;10). **[Cloudflare](https://www.cloudflare.com/small-business/?utm_source=chatgpt.com)**
#### Políticas DNS básicas
Configurar los resolvers DNS de la red para que apunten a Cloudflare Teams (o desplegar túnel 1.1.1.1/warp en los endpoints si hay teletrabajo).
#### Políticas por categoría
Bloquear categorías: Malware, Phishing, Adult, Gambling, Torrenting/P2P, File-sharing no corporativo, Proxy/Anonymizers.
#### Listas negras/whitelist
Importar lista negra inicial (ver sugerencias abajo) y whitelist de dominios de negocio (p. ej. *.office.com, *.microsoftonline.com, login.microsoftonline.com, outlook.office365.com, sharepoint.com).
#### Logs y retención
Activar Logpush o la consola de logs; conservar evidencias de bloqueos y gráficas trimestrales (exportar en CSV/PDF para auditoría).
#### Pruebas
Ejecutar pruebas de bloqueo (test cases) y documentar: 5 URLs bloqueadas por categoría, fecha, usuario y resultado.
#### Mantenimiento
Revisión trimestral de políticas y listas; actualización ante nuevos riesgos.
### 6. Configuración mínima de políticas
Política “Oficina – Default” (aplicada a todos):
- Denegar: Malware, Phishing, Adult, Gambling, Torrenting, File Sharing, Remote Proxy.
- Permitir: Business Apps (O365, GSuite, AWS, proveedor ERP).
- Registrar: todo tráfico permitido y denegado (logs).
[contact@spikatech.com - www.spikatech.com](mailto:contact@spikatech.com)
SPIKA TECH, S.L., with registered office at c/ Alcalá de Guadaira, nº 6, 6ºA Derecha, 28018 MADRID, with Tax Identification Code B87386900, registered in the Mercantile Register of Madrid, in volume 33.500, Folio 200, Page M-603059, Entry. 1, hereinafter THE OWNER.
### 7. Evidencias para auditoría
- Capturas de pantalla de consola con políticas activas.
- Informe de logs: CSV con registros de denegaciones y accesos durante 90 días.
- Resultados de pruebas (documento con URLs probadas y fecha).
- Registro de despliegue de agentes (listado de dispositivos).
### 8. Lista de bloqueos
#### Pornografía / Adult
- pornhub.com
- xvideos.com
- xhamster.com
#### Torrents / Piratería / P2P
- thepiratebay.org
- 1337x.to
- rutracker.org
- yts.mx
#### Gambling / Apuestas
- bet365.com
- 888casino.com
- bwin.com
#### File-sharing públicos / riesgo de fuga de datos
- mega.nz
- dropbox.com
#### Proxy / Anonymizer / Shorteners
- bitly.com
[contact@spikatech.com - www.spikatech.com](mailto:contact@spikatech.com)
SPIKA TECH, S.L., with registered office at c/ Alcalá de Guadaira, nº 6, 6ºA Derecha, 28018 MADRID, with Tax Identification Code B87386900, registered in the Mercantile Register of Madrid, in volume 33.500, Folio 200, Page M-603059, Entry. 1, hereinafter THE OWNER.
- tinyurl.com
- hide.me
- proxysite.com
[contact@spikatech.com - www.spikatech.com](mailto:contact@spikatech.com)
SPIKA TECH, S.L., with registered office at c/ Alcalá de Guadaira, nº 6, 6ºA Derecha, 28018 MADRID, with Tax Identification Code B87386900, registered in the Mercantile Register of Madrid, in volume 33.500, Folio 200, Page M-603059, Entry. 1, hereinafter THE OWNER.