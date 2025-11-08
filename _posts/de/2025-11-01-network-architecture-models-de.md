---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Studie zu Netzwerkarchitektur und Modellen
translated: true
type: note
---

Dieses Kapitel legt den Grundstein für das Verständnis, wie Computernetzwerke aufgebaut sind und wie Daten in ihnen übertragen werden. Im Kontext des Kurses *Computer Networks Technology* (自考 code 02141 oder ähnlich) betont es theoretische Modelle wie OSI und TCP/IP, die Kernbestandteil von Prüfungsfragen zu Schichtung, Protokollen und Datenfluss sind. Konzentrieren Sie sich darauf, die Namen der Schichten, ihre Funktionen und die Zuordnungen zwischen den Modellen auswendig zu lernen. Erwarten Sie Multiple-Choice-, Kurzantwort- oder diagrammbasierte Fragen, die Vergleiche und Zuständigkeiten testen.

## 1. Einführung in geschichtete Architekturen
Netzwerke verwenden **geschichtete Architekturen**, um komplexe Kommunikation zu vereinfachen, indem sie Aufgaben in modulare Schichten unterteilen. Jede Schicht:
- Erledigt spezifische Funktionen (z.B. Fehlerprüfung, Routing).
- Interagiert nur mit benachbarten Schichten über standardisierte Schnittstellen.
- Verwendet **Encapsulation** (Hinzufügen von Headern/Trailern) beim Senden von Daten den Stack hinunter und **Decapsulation** beim Empfangen.

**Vorteile**:
- Modularität: Einfache Entwicklung, Tests und Aktualisierung einzelner Schichten.
- Interoperabilität: Geräte verschiedener Hersteller können kommunizieren.
- Skalierbarkeit: Schichten können sich unabhängig voneinander weiterentwickeln (z.B. neue Transportprotokolle).

**Zuständigkeiten** (allgemein für alle Modelle):
- **Untere Schichten**: Konzentrieren sich auf Hardware und zuverlässige Datenübertragung (physische Übertragung, Fehlererkennung).
- **Obere Schichten**: Bearbeiten anwenderorientierte Aufgaben (z.B. Dateiübertragung, Web-Browsing).
- Daten fließen **hinab** durch den Stack des Senders (Encapsulation) und **hinauf** durch den Stack des Empfängers (Decapsulation).

## 2. OSI-Referenzmodell
Das **Open Systems Interconnection (OSI)**-Modell ist ein konzeptionelles 7-Schichten-Modell, das 1984 von der ISO entwickelt wurde. Es ist theoretisch, wird nicht direkt implementiert, dient aber als Standard zum Verständnis von Protokollen. Eselsbrücke: **Please Do Not Throw Sausage Pizza Away** (Physical → Application).

| Schicht Nr. | Schicht Name      | Wichtige Funktionen und Protokolle | PDU (Protocol Data Unit) | Geräte/Beispiele |
|--------------|------------------|------------------------------------|--------------------------|------------------|
| 7           | Application     | Stellt Netzwerkdienste für Anwendungen bereit (z.B. E-Mail, Dateiübertragung). Schnittstelle zur Software. | Data | HTTP, FTP, SMTP; Webbrowser |
| 6           | Presentation    | Übersetzt Datenformate (z.B. Verschlüsselung, Kompression, ASCII zu EBCDIC). Stellt Syntax-Kompatibilität sicher. | Data | JPEG, SSL/TLS |
| 5           | Session         | Verwaltet Sitzungen/Verbindungen (z.B. Aufbau, Synchronisation, Dialogsteuerung). Verwaltet Checkpoints für Wiederherstellung. | Data | NetBIOS, RPC |
| 4           | Transport       | Ende-zu-Ende zuverlässige Zustellung (z.B. Segmentierung, Flusskontrolle, Fehlerbehebung). | Segment (TCP) / Datagram (UDP) | TCP, UDP; Ports (z.B. 80 für HTTP) |
| 3           | Network         | Logische Adressierung und Routing (z.B. Pfadbestimmung über Netzwerke hinweg). Behandelt Überlastung. | Packet | IP, ICMP, OSPF; Router |
| 2           | Data Link       | Knoten-zu-Knoten Zustellung im selben Netzwerk (z.B. Framing, Fehlererkennung via CRC, MAC-Adressierung). | Frame | Ethernet, PPP; Switches, NICs |
| 1           | Physical        | Bit-Übertragung über physikalisches Medium (z.B. Signalisierung, Verkabelung, Topologie). Behandelt Hardware-Spezifikationen. | Bit | RJ-45, Glasfaser; Hubs, Kabel |

**Wichtige Hinweise**:
- Schichten 1-2: Medienfokussiert (LAN/WAN).
- Schichten 3-4: Host-zu-Host (Internetworking).
- Schichten 5-7: Anwenderorientiert (Anwendungsunterstützung).
- Prüfungstipp: Zeichnen Sie den Stack und beschriften Sie PDUs/Header (z.B. TCP-Segment hat TCP-Header + Daten).

## 3. TCP/IP-Protokollstapel
Das **TCP/IP-Modell** (oder Internet Protocol Suite) ist ein praktisches 4-Schichten-Modell, das in den 1970er Jahren für das ARPANET (Grundlage des Internets) entwickelt wurde. Es wird weltweit implementiert und lässt sich grob auf OSI abbilden. Eselsbrücke: **LITA** (Link → Application).

| Schicht Nr. | Schicht Name      | Wichtige Funktionen und Protokolle | PDU                  | Geräte/Beispiele |
|--------------|------------------|------------------------------------|----------------------|------------------|
| 4           | Application     | Kombiniert OSI-Schichten 5-7: Anwenderdienste (z.B. Web, E-Mail). | Data/Segment | HTTP, FTP, DNS; Apps wie Browser |
| 3           | Transport       | Ende-zu-Ende (OSI-Schicht 4): Zuverlässige/unzuverlässige Zustellung. | Segment/Datagram | TCP (zuverlässig, verbindungsorientiert), UDP (Beste-Bemühung) |
| 2           | Internet        | Routing und Adressierung (OSI-Schicht 3): Logische Pfade über Netzwerke hinweg. | Packet | IP (IPv4/IPv6), ICMP; Router |
| 1           | Link (oder Network Access) | Physisch + Data Link (OSI-Schichten 1-2): Hardware-Zustellung im lokalen Netzwerk. | Frame/Bit | Ethernet, Wi-Fi; Switches, Kabel |

**Wichtige Hinweise**:
- Keine dedizierten Session/Presentation-Schichten; werden innerhalb der Application-Schicht behandelt.
- TCP/IP ist eine "Protokollfamilie" – z.B. IP ist der Kern, mit TCP/UDP darauf aufbauend.
- Prüfungstipp: Betonen Sie die reale Anwendung (z.B. TCP stellt Zuverlässigkeit über Bestätigungen sicher, während UDP leichtgewichtig für Video-Streaming ist).

## 4. Vergleich der OSI- und TCP/IP-Modelle
Verwenden Sie diese Tabelle zur schnellen Wiederholung. OSI ist theoretisch (Referenz), TCP/IP ist praktisch (Implementierung).

| Aspekt              | OSI-Modell                          | TCP/IP-Modell                       |
|---------------------|------------------------------------|------------------------------------|
| **Schichten**         | 7 (detailliert, konzeptionell)          | 4 (vereinfacht, praktisch)         |
| **Entwicklung**    | ISO (1984), Top-down-Design       | DoD/Internet (1970er), Bottom-up   |
| **Fokus**          | Allgemeine Netzwerkstandards      | Internet-spezifische Protokolle       |
| **Implementierung** | Nicht direkt implementiert; Referenz für Standards | Weit verbreitet (Grundlage des modernen Internets) |
| **Schicht-Zuordnung**  | 1: Physical → Link<br>2: Data Link → Link<br>3: Network → Internet<br>4: Transport → Transport<br>5-6-7: Session/Presentation/Application → Application | Application absorbiert OSI 5-7; Link absorbiert 1-2 |
| **Protokolle**      | Theoretisch (z.B. kein einzelnes IP)  | Spezifisch (z.B. IP, TCP, HTTP)    |
| **PDU-Fluss**       | Strikte Header pro Schicht          | Flexibel (z.B. IP-Paket enthält Transportdaten) |
| **Stärken**      | Umfassend, leicht zu lehren      | Effizient, skalierbar, herstellerneutral |
| **Schwächen**     | Übermäßig komplex, nicht praktisch     | Weniger detailliert für obere Schichten    |

**Wichtige Unterschiede**:
- **Detaillierungsgrad**: OSI trennt Session/Presentation; TCP/IP fasst sie in Application zur Vereinfachung zusammen.
- **Adressierung**: OSI verwendet Service Access Points (SAPs); TCP/IP verwendet Ports/IP-Adressen.
- **Zuverlässigkeit**: Beide haben Transport-Zuverlässigkeit, aber TCP/IPs TCP ist verbindungsorientiert wie OSIs Transport.
- Prüfungstipp: Fragen betreffen oft Zuordnungen (z.B. "Welche OSI-Schicht entspricht TCP?") oder Vorteile (z.B. TCP/IPs Anpassungsfähigkeit führte zum Wachstum des Internets).

## 5. Funktionen und Zuständigkeiten geschichteter Architekturen
**Kernprinzipien**:
- **Abstraktion**: Jede Schicht verbirgt die Details der unteren Schichten (z.B. Transport kümmert sich nicht um physische Kabel).
- **Service-Primitive**: Schichten bieten Dienste wie CONNECT, DATA, DISCONNECT für obere Schichten an.
- **Fehlerbehandlung**: Untere Schichten erkennen Fehler; obere Schichten beheben sie (z.B. Transport überträgt verlorene Pakete erneut).
- **Adressierung**: Hierarchisch – physisch (MAC), logisch (IP), Dienst (Ports).

**Beispiel für Datenübertragung**:
1. Anwendungsdaten → Transport fügt Segment-Header hinzu (Ports, Seq.-Nr.) → Network fügt Paket-Header hinzu (IP-Adressen) → Link fügt Frame-Header/Trailer hinzu (MAC) → Physical sendet Bits.
2. Umgekehrt beim Empfänger.

**Häufige Fehlerquellen**:
- Schichten nicht verwechseln: Physical ist Bits/Signale; Data Link ist Frames/fehlerfreie Frames.
- TCP/IP Link-Schicht = OSI 1+2 kombiniert.

## Lerntipps für die 自考-Prüfung
- **Auswendiglernen**: Verwenden Sie Eselsbrücken und zeichnen Sie täglich Schichtendiagramme. Konzentrieren Sie sich auf die 80% Prüfungsgewichtung zu OSI/TCP/IP-Beschreibungen.
- **Übung**:
  - Vergleichen Sie Schichten in Aufsätzen (200-300 Wörter).
  - MCQs: "Welche Schicht behandelt Routing? (A) Network".
  - Diagramme: Beschriften Sie einen PDU-Durchlauf.
- **Ressourcen**: Überprüfen Sie Lehrbuchabbildungen zur Encapsulation. Nehmen Sie sich Zeit: 30 Min. für die Vergleichstabelle.
- **Häufige Fragen**: Erklären Sie, warum OSI 7 Schichten hat vs. TCP/IPs 4; Beschreiben Sie die Aufgaben der Transport-Schicht.

Meistern Sie dieses Kapitel für einen starken Start – es wird in späteren Themen wie Protokollen (z.B. IP in Kapitel 3) referenziert. Als nächstes nehmen Sie sich die Details der Bitübertragungsschicht vor.

**Referenzen**:
- [Computer Networking: A Top-Down Approach by Kurose & Ross](https://www.pearson.com/us/higher-education/program/Kurose-Computer-Networking-A-Top-Down-Approach-8th-Edition/PGM1836378.html) (für TCP/IP-Tiefe).
- [OSI Model Explained - GeeksforGeeks](https://www.geeksforgeeks.org/open-systems-interconnection-model-osi/) (visuelle Hilfsmittel).