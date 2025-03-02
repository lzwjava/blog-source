---
audio: false
generated: true
lang: de
layout: post
title: Hetzner Cloud
translated: true
---

Ich bin sehr aufgeregt, diese Cloud-Plattform auszuprobieren, die kürzlich gestartet wurde.

{: .zentriert }
![](assets/images/hertzner/h.jpg)
*Quelle: Hetzner*{: .bildunterschrift }

Ein Server in Helsinki mit einer Konfiguration von 2 AMD VCPUs, 2 GB RAM, 40 GB SSD und 20 TB Traffic kostet 4,49 USD pro Monat.

Eine IPv4-Adresse kostet zusätzlich 0,60 USD pro Monat, was insgesamt 5,09 USD pro Monat ergibt.

Sie bieten Dienstleistungen in sechs Standorten an:

- Nürnberg, Deutschland
- Falkenstein, Deutschland
- Helsinki, Finnland
- Singapur, Singapur
- Hillsboro, OR, USA
- Ashburn, VA, USA

Es ist interessant, dass sie keine Trends verfolgen, um beliebte Standorte auszuwählen. Ihre Standorte unterscheiden sich von denen von Vultr oder Digital Ocean.

Die Firewall-Einstellungen sind einfach zu bedienen. Obwohl dies mein erstes Mal war, konnte ich schnell die richtige Konfiguration für meinen Proxy-Server einrichten.

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

Die Geschwindigkeit des Hetzner-Servers in Helsinki ist sehr schnell. Mit der Speedtest iOS-App beträgt die Downloadgeschwindigkeit 423 Mbps und die Uploadgeschwindigkeit 56,1 Mbps.

Der Ping in Shadowrocket beträgt 1175 ms, was aber kein großes Problem ist.

Ein einfaches Python-Skript, um Serverinstanzdetails zu erhalten.

```python
from hcloud import Client
import os

# Holen Sie sich das API-Token aus der Umgebungsvariablen
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Fehler: HERTZNER_API_KEY-Umgebungsvariable nicht gesetzt.")
    exit(1)

# Erstellen Sie eine Client-Instanz
client = Client(token=api_token)

# Liste aller Server
servers = client.servers.get_all()

# Drucken Sie die Serverdetails
for server in servers:
    print(f"Server-ID: {server.id}")
    print(f"Server-Name: {server.name}")
    print(f"Server-Status: {server.status}")
    print(f"Server IPv4: {server.public_net.ipv4.ip}")
    print(f"Server IPv6: {server.public_net.ipv6.ip}")
    print(f"Server-Typ: {server.server_type.name}")
    print(f"Server-Standort: {server.datacenter.location.name}")
    print("----------------------------------")

# Wenn Sie eine bestimmte Server-ID erhalten möchten
server_id = '59402674'
server = client.servers.get_by_id(server_id)

print(f"Server-ID: {server.id}")
print(f"Server-Name: {server.name}")
print(f"Server-Status: {server.status}")
print(f"Server IPv4: {server.public_net.ipv4.ip}")
print(f"Server IPv6: {server.public_net.ipv6.ip}")
print(f"Server-Typ: {server.server_type.name}")
print(f"Server-Standort: {server.datacenter.location.name}")

```