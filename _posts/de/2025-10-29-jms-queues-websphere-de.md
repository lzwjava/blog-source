---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: JMS-Warteschlangen im WebSphere Application Server
translated: true
type: note
---

### Java Message Service (JMS) – Überblick
Java Message Service (JMS) ist eine standardisierte API zum Senden von Nachrichten zwischen Java-Anwendungen, die asynchrone Kommunikation ermöglicht. Sie unterstützt zwei Hauptnachrichtenmuster: Point-to-Point (unter Verwendung von Queues) und Publish-Subscribe (unter Verwendung von Topics). In IBM WebSphere Application Server (WAS) ist JMS integriert, um Messaging innerhalb von Enterprise-Anwendungen zu handhaben, oft unter Verwendung des eingebauten Standard-Messaging-Providers oder externer Provider wie IBM MQ.

### Queues in JMS
In JMS ist eine **Queue** eine Art Destination, die für **Point-to-Point-Messaging** verwendet wird. Hier eine Aufschlüsselung:
- **Zweck**: Nachrichten, die an eine Queue gesendet werden, werden an genau einen Consumer (Empfänger) ausgeliefert. Dies ist ideal für Szenarien, in denen eine Nachricht von einer einzelnen Anwendung oder Komponente verarbeitet werden muss, wie z.B. bei der Aufgabenverteilung oder Request-Response-Mustern.
- **Wesentliche Merkmale**:
  - **FIFO (First-In-First-Out)**: Nachrichten werden typischerweise in der Reihenfolge ihres Eingangs verarbeitet, obwohl JMS eine Priorisierung ermöglicht.
  - **Persistenz**: Nachrichten können persistent (dauerhaft gespeichert) oder nicht-persistent sein, was Zuverlässigkeit im Fehlerfall gewährleistet.
  - **Consumer**: Mehrere Consumer können an eine Queue angehängt werden, aber jede Nachricht wird nur von einem Consumer verarbeitet. Wenn kein Consumer verfügbar ist, sammeln sich die Nachrichten in der Queue, bis sie verarbeitet werden.
- **Beteiligte Komponenten**:
  - **Queue Sender/Producer**: Sendet Nachrichten an die Queue.
  - **Queue Receiver/Consumer**: Fragt Nachrichten auf der Queue ab oder lauscht auf diese.
  - **Connection Factory**: Wird verwendet, um Verbindungen zum JMS-Provider herzustellen.

### Queues in IBM WebSphere Application Server
In IBM WAS werden JMS-Queues als Ressourcen innerhalb der Messaging-Infrastruktur des Servers konfiguriert. WAS unterstützt:
- **Default Messaging Provider**: Eingebauter JMS-Engine für leichtgewichtiges Messaging.
- **Integration mit IBM MQ**: Für robusteres, skalierbares Queuing.

#### Konfigurationsgrundlagen
Um Queues in WAS zu verwenden:
1. **Erstellen eines JMS-Bus**: Eine logische Gruppierung von Servern für das Nachrichten-Routing.
2. **Hinzufügen von Bus-Mitgliedern**: Einbinden von Application Servern in den Bus.
3. **Erstellen von Queue-Destinations**: Definieren der Queue (z.B. Name, JNDI-Bindung) und Verknüpfen mit dem Bus.
4. **Einrichten von Connection Factories**: Für Producer/Consumer, um eine Verbindung herzustellen.
5. **Activation Specs**: Für Message-driven Beans (MDBs), um automatisch Nachrichten von Queues zu konsumieren.

Queues können über die WAS-Admin-Konsole auf Tiefe, Alter und Durchsatz überwacht werden. Beispielsweise könnten Sie eine Queue namens `MyApp.Queue` mit einem JNDI-Namen wie `jms/queue/MyQueue` zur Suche im Code erstellen.

#### Beispiel-Anwendungsfall
In einer Banking-App könnte eine Queue Transaktionsanfragen handhaben: Ein Frontend sendet eine Nachricht an die Queue, und ein Backend-MDB verarbeitet sie nacheinander, um Duplikate zu vermeiden.

Detaillierte Einrichtungsinformationen finden Sie in der IBM-Dokumentation.

### Referenzen
- [Configuring Java Message Service for WebSphere Application Server](https://www.ibm.com/docs/en/mfci/7.6.2?topic=clusters-configuring-jms-websphere-application-server)
- [Queue Collection in WebSphere Application Server](https://www.ibm.com/docs/en/was/8.5.5?topic=s-queue-collection)