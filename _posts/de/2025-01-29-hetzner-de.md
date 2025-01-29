---
audio: true
lang: de
layout: post
title: Hetzner Cloud
translated: true
---

Ich bin sehr aufgeregt, diese Cloud-Plattform kürzlich ausprobiert zu haben.

{: .zentriert }
![](assets/images/hertzner/h.jpg)
*Quelle: Hetzner*{: .bildunterschrift }

Ein Server in Helsinki mit einer Konfiguration von 2 AMD VCPUs, 2 GB RAM, 40 GB SSD und 20 TB Traffic kostet $4,49 USD pro Monat.

Eine IPv4-Adresse kostet zusätzlich $0,60 USD pro Monat, was den Gesamtbetrag auf $5,09 USD pro Monat erhöht.

Sie bieten Dienste in sechs Standorten an:

- Nürnberg, Deutschland
- Falkenstein, Deutschland
- Helsinki, Finnland
- Singapur, Singapur
- Hillsboro, OR, USA
- Ashburn, VA, USA

Es ist interessant, dass sie nicht den Trends folgen, beliebte Standorte auszuwählen. Ihre Standorte unterscheiden sich von denen von Vultr oder Digital Ocean.

Die Firewall-Einstellungen sind einfach zu bedienen. Obwohl dies mein erster Versuch war, habe ich schnell die richtige Konfiguration für meinen Proxy-Server eingerichtet.

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

Die Geschwindigkeit des Hetzner-Servers in Helsinki ist sehr hoch. Mit der Speedtest iOS-App beträgt die Download-Geschwindigkeit 423 Mbps und die Upload-Geschwindigkeit 56,1 Mbps.

Der Ping in Shadowrocket beträgt 1175 ms, was aber kein großes Problem darstellt.

Ein einfaches Python-Skript, um Server-Instanzdetails zu erhalten.

```python
from hcloud import Client
import os

# API-Token aus der Umgebungsvariablen abrufen
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Fehler: HERTZNER_API_KEY-Umgebungsvariable nicht gesetzt.")
    exit(1)

# Client-Instanz erstellen
client = Client(token=api_token)

# Alle Server auflisten
servers = client.servers.get_all()

# Serverdetails drucken
for server in servers:
    print(f"Server ID: {server.id}")
    print(f"Server Name: {server.name}")
    print(f"Server Status: {server.status}")
    print(f"Server IPv4: {server.public_net.ipv4.ip}")
    print(f"Server IPv6: {server.public_net.ipv6.ip}")
    print(f"Server Typ: {server.server_type.name}")
    print(f"Server Standort: {server.datacenter.location.name}")
    print("----------------------------------")

# Wenn Sie eine bestimmte Server-ID abrufen möchten
server_id = '59402674'
server = client.servers.get_by_id(server_id)

print(f"Spezieller Server ID: {server.id}")
print(f"Spezieller Server Name: {server.name}")
print(f"Spezieller Server Status: {server.status}")
print(f"Spezieller Server IPv4: {server.public_net.ipv4.ip}")
print(f"Spezieller Server IPv6: {server.public_net.ipv6.ip}")
print(f"Spezieller Server Typ: {server.server_type.name}")
print(f"Spezieller Server Standort: {server.datacenter.location.name}")
```