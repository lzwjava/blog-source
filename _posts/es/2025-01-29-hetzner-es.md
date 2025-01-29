---
audio: true
lang: es
layout: post
title: Hetzner Nube
translated: true
---

Estoy muy emocionado de probar esta plataforma en la nube recientemente.

{: .centrado }
![](assets/images/hertzner/h.jpg){: .responsivo }
*Fuente: Hetzner*{: .pie-de-foto }

Un servidor en Helsinki con una configuración de 2 VCPUs AMD, 2GB de RAM, 40GB SSD y 20TB de tráfico cuesta $4.49 USD al mes.

Una dirección IPv4 cuesta adicionalmente $0.60 USD al mes, lo que eleva el total a $5.09 USD al mes.

Ofrecen servicios en seis ubicaciones:

- Núremberg, Alemania
- Falkenstein, Alemania
- Helsinki, Finlandia
- Singapur, Singapur
- Hillsboro, OR, EE.UU.
- Ashburn, VA, EE.UU.

Es interesante que no sigan las tendencias para seleccionar ubicaciones populares. Sus ubicaciones son diferentes a las de Vultr o Digital Ocean.

Las configuraciones del firewall son fáciles de usar. Aunque esta fue mi primera vez usándolo, rápidamente configuré la configuración correcta para mi servidor proxy.

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

La velocidad del servidor de Hetzner en Helsinki es muy rápida. Usando la aplicación Speedtest de iOS, la velocidad de descarga es de 423 Mbps y la velocidad de carga es de 56.1 Mbps.

El ping en Shadowrocket es de 1175 ms, pero esto no es un problema significativo.