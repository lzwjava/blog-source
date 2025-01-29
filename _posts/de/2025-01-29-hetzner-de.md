---
audio: true
lang: de
layout: post
title: Hetzner Cloud
translated: true
---

Ich freue mich sehr, diese Cloud-Plattform auszuprobieren.

{: .centered }
![](assets/images/hertzner/h.jpg){: .responsive }
*Quelle: Hetzner*{: .caption }

Ein Server in Helsinki mit einer Konfiguration von 2 AMD VCPUs, 2 GB RAM, 40 GB SSD und 20 TB Traffic kostet 4,49 USD pro Monat.

Eine IPv4-Adresse kostet zusätzlich 0,60 USD pro Monat, was den Gesamtpreis auf 5,09 USD pro Monat erhöht.

Sie bieten Dienste in sechs Standorten an:

- Nürnberg, Deutschland
- Falkenstein, Deutschland
- Helsinki, Finnland
- Singapur, Singapur
- Hillsboro, OR, USA
- Ashburn, VA, USA

Es ist interessant, dass sie sich nicht an die Trends halten, um beliebte Standorte auszuwählen. Ihre Standorte unterscheiden sich von denen von Vultr oder Digital Ocean.

Die Firewall-Einstellungen sind einfach zu bedienen. Obwohl dies das erste Mal war, dass ich sie verwendet habe, konnte ich schnell die richtige Konfiguration für meinen Proxy-Server einrichten.

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

Die Geschwindigkeit des Hetzner-Servers in Helsinki ist sehr schnell. Mit der Speedtest iOS-App beträgt die Download-Geschwindigkeit 423 Mbps und die Upload-Geschwindigkeit 56,1 Mbps.

Der Ping in Shadowrocket beträgt 1175 ms, was jedoch kein erhebliches Problem darstellt.