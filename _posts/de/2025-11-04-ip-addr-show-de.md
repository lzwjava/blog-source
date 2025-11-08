---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Verstehen der Ausgabe von ip addr show enp4s0
translated: true
type: note
---

### Aufschlüsselung Ihrer `ip addr show enp4s0`-Ausgabe

Dieser Befehl zeigt detaillierte Informationen zu Ihrer Ethernet-Schnittstelle (enp4s0), die die LAN-Verbindung aus der zuvor besprochenen Routing-Tabelle handhabt. Sie ist aktiv und funktioniert einwandfrei – gut für die grundlegende Konnektivität. Ich werde sie Zeile für Zeile analysieren und dann zusammenfassen.

#### Wichtige Abschnitte erklärt
- **Schnittstellenstatus**:  
  `2: enp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000`  
  - Index 2 (zweite Schnittstelle, nach lo).  
  - Flags: Unterstützt Broadcast/Multicast, vollständig UP (Link erkannt und betriebsbereit).  
  - MTU: 1500 Bytes (Standard-Ethernet-Frame-Größe – keine Jumbo Frames).  
  - Queue-Discipline: fq_codel (Fair Queuing für Latenz-optimierten Verkehr, üblich auf modernem Linux).  
  - State: UP (bereit zum Senden/Empfangen).

- **Link-Layer (MAC-Adresse)**:  
  `link/ether 04:7c:16:d9:54:5b brd ff:ff:ff:ff:ff:ff`  
  - Ihre Hardware-MAC: 04:7c:16:d9:54:5b (eindeutig für diese NIC).  
  - Broadcast: ff:ff:ff:ff:ff:ff (All-Ones für Ethernet-Broadcasts).

- **IPv4-Adresse**:  
  `inet 192.168.1.35/24 brd 192.168.1.255 scope global dynamic noprefixroute enp4s0`  
  `valid_lft 4790sec preferred_lft 4790sec`  
  - IP: 192.168.1.35 mit /24 Subnetz (255.255.255.0 Maske). Entspricht dem "src 192.168.1.35" in Ihrer Routingtabelle.  
  - Broadcast: 192.168.1.255 (für subnetzweite Broadcasts).  
  - Scope: global (über diesen Host hinaus routbar).  
  - Dynamic: Zugewiesen via DHCP (von Ihrem Router bei 192.168.1.1).  
  - No prefix route: Fügt keine verbundene Route automatisch hinzu (aber der Kernel hat dies dennoch getan, wie in `ip route` zu sehen).  
  - Lease: ~79 Minuten verbleibend (4790 Sekunden) vor der Erneuerung.

- **IPv6-Adresse**:  
  `inet6 fe80::a884:a0f6:e8b4:4a7d/64 scope link noprefixroute`  
  `valid_lft forever preferred_lft forever`  
  - Link-lokale IPv6: fe80::... (automatisch aus der MAC generiert; nur für die lokale Link-Kommunikation, wie Neighbor Discovery).  
  - /64 Präfix, Scope link (nicht über diese Schnittstelle hinaus routbar).  
  - Permanent (kein Ablaufdatum).

#### Kurze Zusammenfassungstabelle

| Aspekt       | Wert/Details                  | Was es bedeutet |
|--------------|--------------------------------|---------------|
| **Status**  | UP, MTU 1500                  | Schnittstelle ist aktiv und verarbeitet Standard-Pakete. |
| **MAC**     | 04:7c:16:d9:54:5b             | Die Hardware-Adresse Ihres Geräts im Netzwerk. |
| **IPv4**    | 192.168.1.35/24 (DHCP)        | Lokale LAN-IP; Routen zu diesem Subnetz bleiben auf enp4s0. |
| **IPv6**    | fe80::a884:a0f6:e8b4:4a7d/64  | Nur lokal gültige IPv6; nützlich für IPv6 Neighbor Discovery. |
| **Lease**   | ~79 Min. verbleibend          | DHCP erneuert bald – bei Bedarf mit `dhclient -r enp4s0 && dhclient enp4s0` prüfen. |

Dieser Setup erklärt, warum Ihre Standardroute hier für den Internetzugriff zeigt und warum lokaler 192.168.1.x-Verkehr direkt ist. Wenn Sie innerhalb des LANs pingen, wird es per ARP nach der MAC-Adresse fragen und Frames über diese Schnittstelle senden.

Sieht alles gut aus, oder gibt es ein Problem (z.B. keine globale IPv6-Adresse oder Verbindungsabbrüche)? Wenn Sie `ip addr` für andere Schnittstellen oder `ping`-Ergebnisse teilen, kann ich tiefer graben. Was kommt als Nächstes – Docker-Bridges testen, oder etwas anderes?