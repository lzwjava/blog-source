---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Grundlagen der IPv4-Routing-Tabelle
translated: true
type: note
---

### Verstehen Ihrer `ip route`-Ausgabe

Dies ist die IPv4-Routing-Tabelle Ihres Linux-Systems (vermutlich erstellt mit dem `ip`-Befehl aus iproute2). Sie zeigt, wie Ihr Rechner entscheidet, wohin Pakete basierend auf Ziel-IPs gesendet werden. Routen werden durch den längsten Präfix (spezifischste Route zuerst) abgeglichen, und die Standardroute fängt alles andere auf.

Ich werde sie Eintrag für Eintrag in einer Tabelle zur Verdeutlichung aufschlüsseln und dann zusammenfassen, was sie insgesamt bedeutet. Dies knüpft an unseren vorherigen Chat an: Es ist ein Beispiel aus der Praxis für eine einfache Routing-Tabelle mit verbundenen Routen (lokale Subnetze) und einem Standard-Gateway für das Internet.

| Ziel             | Gateway (Next Hop) | Schnittstelle | Protokoll | Scope | Quell-IP     | Metrik | Anmerkungen |
|------------------|--------------------|---------------|-----------|-------|--------------|--------|-------------|
| **0.0.0.0/0** (Standard) | 192.168.1.1       | enp4s0        | dhcp      | global| (keine)      | 100    | Aller Verkehr, der keine andere Route matcht, geht hierhin. Zeigt auf Ihren Router (vermutlich Ihr Heim-Gateway) auf der Ethernet-Schnittstelle enp4s0. Via DHCP entdeckt. |
| **169.254.0.0/16** | (direct)          | enp4s0        | kernel    | link  | (keine)      | 1000   | Link-local (APIPA) Bereich für Auto-Konfiguration, wenn DHCP fehlschlägt. Hohe Metrik bedeutet, es ist ein Fallback – wird nur verwendet, wenn keine bessere Route existiert. |
| **172.17.0.0/16** | (direct)          | docker0       | kernel    | link  | 172.17.0.1   | (keine)| Dockers Standard-Bridge-Netzwerk. "linkdown" bedeutet, die Schnittstelle ist down (keine aktiven Container?). Ihr Host agiert als Gateway für dieses Subnetz. |
| **172.18.0.0/16** | (direct)          | br-c33e38e216df | kernel  | link  | 172.18.0.1   | (keine)| Eine weitere Docker-Bridge (benutzerdefiniertes Netzwerk?). Aktiv, daher können Container auf dieser Bridge den Host via 172.18.0.1 erreichen. |
| **192.168.1.0/24** | (direct)         | enp4s0        | kernel    | link  | 192.168.1.35 | 100    | Ihr lokales LAN-Subnetz. Direkt verbunden via enp4s0 – Pakete zu anderen Geräten in 192.168.1.x bleiben lokal (z.B. zu Ihrem Router auf .1). Die IP Ihres Rechners ist 192.168.1.35. |

#### Wichtige Erkenntnisse
- **Lokale/Verbundene Routen**: Die 172.x.x.x und 192.168.1.0/24 Einträge sind "Kernel"-Routen für direkt angeschlossene Netzwerke (kein Next-Hop-Gateway nötig). Dies entspricht der einfachen Iteration, die Sie beschrieben haben – Ihr System prüft, ob die Ziel-IP in diese Bereiche fällt und sendet sie über die passende Schnittstelle (z.B. enp4s0 für das LAN).
- **Docker-Einfluss**: Sie haben Docker installiert/am Laufen, was virtuelle Bridges erstellt (docker0 und br-...). Diese erlauben es Containern, ihre eigenen isolierten Netzwerke zu haben. Das "linkdown" auf docker0 deutet darauf hin, dass derzeit keine Container die Standard-Bridge verwenden.
- **Standardroute**: Alles andere (z.B. google.com) geht via 192.168.1.1 auf enp4s0. Metrik 100 ist niedrig (bevorzugt); die Link-local-Route hat 1000, um sie zu depriorisieren.
- **Keine entfernten Routen**: Diese Tabelle ist grundlegend – keine dynamischen Routing-Protokolle (wie OSPF), die Einträge für entfernte Netzwerke hinzufügen. Wenn Sie etwas außerhalb von 192.168.1.0/24 anpingen, trifft es auf die Standardroute.

#### Schnelltests zur Überprüfung
- `ping 192.168.1.1` → Sollte die lokale Route auf enp4s0 verwenden.
- `ping 8.8.8.8` → Verwendet die Standardroute; verfolgen Sie den Pfad mit `traceroute 8.8.8.8`.
- `ip addr show enp4s0` → Bestätigt die IP Ihrer Schnittstelle.
- Falls Docker involviert ist: `docker network ls`, um die Bridges aufzulisten.

Falls dies von Ihrem Setup stammt und etwas nicht funktioniert (z.B. kein Internet?), sind häufige Lösungen: Kabel/DHCP-Erneuerung prüfen (`dhclient enp4s0`) oder Routen zurücksetzen (`ip route flush cache`). Was ist los – Fehlersuche bei der Konnektivität, oder sind Sie nur neugierig auf einen bestimmten Eintrag?