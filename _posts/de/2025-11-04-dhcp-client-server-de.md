---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: DHCP-Client- und Serverrollen
translated: true
type: note
---

Nein, das ist ein häufiges Missverständnis, aber DHCP muss nicht dasselbe auf dem Client und dem Router "ausführen" – es handelt sich um ein Client-Server-Protokoll mit unterschiedlichen Rollen für jede Seite. Lassen Sie es mich einfach erklären.

### Kurzer DHCP-Überblick
DHCP (Dynamic Host Configuration Protocol) automatisiert die Vergabe von IP-Adressen und anderen Netzwerkeinstellungen (wie Subnetzmaske, Gateway, DNS) an Geräte in einem Netzwerk. Es eliminiert die manuelle Konfiguration.

### Rollen in einem typischen Setup
- **Router (oder DHCP-Server)**: Führt die **DHCP-Server**-Software aus. Dies ist der "Chef", der IP-Adressen aus einem von ihm verwalteten Pool vergibt. Die meisten Heim-/SOHO-Router (z.B. von TP-Link, Netgear) haben dies eingebaut und standardmäßig aktiviert.
- **Client (z.B. Ihr Laptop, Smartphone, PC)**: Führt einen **DHCP-Client** aus (eingebaut in das Betriebssystem, wie `dhclient` unter Linux oder die automatische IP-Einrichtung von Windows). Dieser fordert eine IP vom Server an, vergibt aber selbst keine IPs an andere.

Beide Seiten sind für den Handshake essenziell, aber sie führen nicht identische "DHCP"-Prozesse aus – einer bedient, einer fragt an.

### So funktioniert es (Grundablauf)
1.  **Client sendet "DISCOVER" als Broadcast**: Ein neues Gerät verbindet sich mit dem Netzwerk und ruft: "Hey, hat jemand eine IP für mich?"
2.  **Server (Router) sendet "OFFER"**: "Klar, hier ist eine verfügbare IP und die Einstellungen."
3.  **Client sendet "REQUEST"**: "Ich nehme diese, bitte."
4.  **Server sendet Bestätigung "ACK"**: "Erledigt – verwende sie."

Wenn der DHCP-Server des Routers ausgeschaltet ist, benötigen Clients möglicherweise statische IPs oder einen anderen Server (z.B. in einem Pi-hole oder Enterprise-Setup).

### Häufige Szenarien

| Setup | DHCP-Server-Standort | Client-Verhalten |
|-------|----------------------|-----------------|
| **Heimnetzwerk** | Router (aktiviert) | Konfiguriert alles automatisch |
| **Kein Router-DHCP** | Manuelle/statische IPs oder externer Server | Client wechselt zu APIPA (169.254.x.x), falls keine Antwort |
| **Enterprise** | Dedizierter DHCP-Server (nicht der Router) | Gleicher Client-Anfrageprozess |

Wenn Sie ein bestimmtes Problem beheben (z.B. "Mein Gerät bekommt keine IP"), teilen Sie mehr Details mit – ich kann beim Debugging helfen! Für vertiefende Lektüre sehen Sie sich das offizielle RFC an: [RFC 2131: Dynamic Host Configuration Protocol](https://datatracker.ietf.org/doc/html/rfc2131).