---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: IBM WebSphere Service Integration Bus
translated: true
type: note
---

### Service Integration Bus in IBM WebSphere Application Server

Der "Integration Bus" im Kontext von IBM WebSphere Application Server (WAS) bezieht sich typischerweise auf den **Service Integration Bus (SIB oder SIBus)**, eine eingebaute Messaging-Infrastruktur, die von WAS bereitgestellt wird. Er ermöglicht eine zuverlässige, asynchrone Kommunikation zwischen Anwendungen, insbesondere solchen, die nachrichtenbasierte Architekturen oder serviceorientierte Architekturen (SOA) verwenden.

#### Zweck
SIB fungiert als ein virtuelles Messaging-Rückgrat innerhalb einer WAS-Umgebung. Er ermöglicht es Anwendungen, die auf verschiedenen Servern oder Clustern laufen, Nachrichten auszutauschen, ohne direkte Point-to-Point-Verbindungen, was lose Kopplung, Skalierbarkeit und Fehlertoleranz fördert. Wichtige Anwendungsfälle sind:
- Unterstützung von Java Message Service (JMS) für Queuing- und Publish/Subscribe-Muster.
- Integration von Enterprise Services in SOA-Setups.
- Handhabung von Nachrichten-Routing, -Transformation und -Persistenz in verteilten Systemen.

Im Gegensatz zu eigenständigen Enterprise Service Buses (ESBs) wie dem IBM Integration Bus (früher WebSphere Message Broker) ist SIB nativ in WAS eingebettet und erfordert keine separate Installation – er wird durch Konfiguration aktiviert.

#### Wichtige Komponenten und Architektur
- **Bus-Member**: Dies sind die Anwendungsserver oder Server-Cluster in einer WAS-Zelle, die dem Bus beitreten. Jedes Member hostet einen Teil der Messaging-Infrastruktur.
- **Messaging Engines (MEs)**: Die zentralen Laufzeitkomponenten, die Nachrichten verarbeiten. Jede ME läuft innerhalb eines WAS-Prozesses (z.B. auf einem Bus-Member) und kümmert sich um das Senden, Empfangen und Speichern von Nachrichten. MEs verbinden sich dynamisch, um ein vermitteltes Netzwerk für hohe Verfügbarkeit zu bilden.
- **SIB-Service**: Ein Standarddienst auf jedem WAS-Anwendungsserver, der standardmäßig deaktiviert ist. Durch Aktivierung werden Messaging-Fähigkeiten freigeschaltet.
- **Destinations**: Queues oder Topics, auf denen Nachrichten veröffentlicht oder konsumiert werden, konfigurierbar über die WAS-Admin-Konsole.
- **Data Stores**: Für Persistenz verwenden MEs dateibasierte Stores (lokal für einzelne Server, Shared Filesystems für Cluster) oder Datenbanken, um die Nachrichtenhaltbarkeit sicherzustellen.

Die Architektur ist zellenbasiert: In einem WAS Network Deployment-Setup arbeiten mehrere Bus-Member knotenübergreifend zusammen und verwenden Protokolle wie SOAP/HTTP oder JMS für Interoperabilität.

#### Einrichtung und Verwendung
1. **Erstellung**: Über die WAS Integrated Solutions Console (Admin-Konsole), navigieren zu *Service integration > Buses > New*. Busnamen definieren, Member (Server/Cluster) hinzufügen und MEs konfigurieren (z.B. Hochverfügbarkeitsrichtlinien).
2. **Konfiguration**: Den SIB JMS-Provider aktivieren, Destinations (Queues/Topics) erstellen und sie JNDI-Namen für den App-Zugriff zuordnen.
3. **Verwendung**: Anwendungen deployen Message-Driven Beans (MDBs) oder verwenden JMS-APIs, um mit dem Bus zu interagieren. Beispielsweise legt eine Sender-App eine Nachricht auf einer Queue ab, und der Bus leitet sie zu Empfängern auf anderen Members weiter.

SIB unterstützt Standards wie JMS 1.1/2.0 und integriert sich mit externen Systemen (z.B. über WebSphere MQ Bridges). Für den Produktiveinsatz sollte eine Leistungsoptimierung in Betracht gezogen werden, z.B. die Verwendung von Shared Datastores für Failover.

**Hinweis**: Wenn Sie *IBM Integration Bus* (IIB) meinen, handelt es sich dabei um ein separates Produkt für umfassendere ESB-Anforderungen, das sich mit WAS/SIB verbinden kann, aber nicht "in" WAS selbst enthalten ist.

[Service integration buses - IBM Docs](https://www.ibm.com/docs/en/was/9.0.5?topic=integration-service-buses)  
[Service integration bus messaging provider - IBM Docs](https://www.ibm.com/docs/en/was-liberty/nd?topic=providers-service-integration-bus-messaging-provider)  
[Getting Started with Service Integration Bus](https://www.freekb.net/Article?id=1975)