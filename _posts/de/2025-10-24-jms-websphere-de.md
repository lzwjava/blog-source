---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: JMS in WebSphere Application Server
translated: true
type: note
---

### Funktionsweise von JMS in IBM WebSphere Application Server (WAS)

JMS (Java Message Service) ist eine standardisierte API zum Senden und Empfangen von Nachrichten zwischen Java-Anwendungen auf entkoppelte, asynchrone Weise. In WAS wird JMS durch den **Default Messaging Provider** implementiert, der den **Service Integration Bus (SIBus)** als zugrunde liegende Messaging-Engine verwendet. SIBus ist ein integrierter, skalierbarer Bus, der Nachrichtenrouting, -warteschlangen und -zustellung ohne externe Software verwaltet.

#### Wichtige Komponenten und Ablauf
1.  **Service Integration Bus (SIBus)**: Dies ist die Kerninfrastruktur. Er ist wie ein virtuelles Netzwerk, in dem Messaging-Engines (eine pro Server oder Cluster) Nachrichten verarbeiten. Sie erstellen einen Bus, fügen Server als Mitglieder hinzu und definieren Destinations (Queues oder Topics) darauf.

2.  **Connection Factory**: Dient als Einstiegspunkt. Ihre Java-Anwendung sucht diese über JNDI (z.B. `jms/MyConnectionFactory`), um eine JMS-Verbindung zum SIBus herzustellen.

3.  **Destinations (Queues/Topics)**: Queues sind für Point-to-Point-Messaging (ein Sender, ein Empfänger). Einmal erstellt und an den Bus gebunden, speichern sie Nachrichten persistent (unter Verwendung von File Stores oder Datenbanken, konfigurierbar).

4.  **Wie Nachrichten fließen**:
    - **Senden**: Die App erstellt eine JMS-Session über die Connection Factory, erhält eine Queue-Referenz über JNDI und sendet eine Nachricht (z.B. `TextMessage`). Der SIBus leitet sie zur Ziel-Messaging-Engine weiter, die sie in die Queue stellt.
    - **Empfangen**: Ein Consumer (z.B. eine andere App oder Message-Driven Bean) verbindet sich auf ähnliche Weise und fragt Nachrichten ab oder lauscht auf diese. SIBus liefert sie zuverlässig aus und kümmert sich um Wiederholungen, Bestätigungen und Transaktionen.
    - SIBus unterstützt Clustering für Hochverfügbarkeit, Lastverteilung und Foreign Bus Links zur Integration mit anderen Systemen.

WAS verwaltet den Lebenszyklus: Starten/Stoppen von Engines, Überwachen von Queues und Sicherstellen der Dauerhaftigkeit basierend auf Ihrer Konfiguration (z.B. persistente vs. nicht-persistente Nachrichten).

#### Ermöglicht das Erstellen einer JMS-Queue Java-Apps das Senden/Empfangen von Nachrichten?
Ja, genau. Nach dem Setup (wie zuvor skizziert: Bus, Mitglied, Connection Factory, Queue) kann Ihre Java-Anwendung:
- Standard-JMS-APIs (`javax.jms.*`) zum Senden/Empfangen verwenden.
- Ressourcen über JNDI im App-Server-Kontext nachschlagen.
- Beispielausschnitt für das Senden:
  ```java
  InitialContext ctx = new InitialContext();
  QueueConnectionFactory qcf = (QueueConnectionFactory) ctx.lookup("jms/MyConnectionFactory");
  Queue queue = (Queue) ctx.lookup("jms/MyQueue");
  QueueConnection conn = qcf.createQueueConnection();
  QueueSession session = conn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
  QueueSender sender = session.createSender(queue);
  TextMessage msg = session.createTextMessage("Hello JMS!");
  sender.send(msg);
  // Ressourcen schließen...
  ```
Das Empfangen funktioniert ähnlich mit `QueueReceiver` oder MDBs. Kein benutzerdefinierter Code für den Bus ist nötig – alles ist abstrahiert.

#### Verwaltet WAS die Queue ordnungsgemäß?
Absolut. SIBus kümmert sich um:
- **Persistenz**: Nachrichten überstehen Neustarts (File-/DB-Store).
- **Zuverlässigkeit**: Garantierte Zustellung, Dead-Letter-Queues für Fehler.
- **Skalierbarkeit**: Bewältigt hohen Durchsatz, Clustering.
- **Monitoring**: Statistiken in der Admin-Konsole einsehen (z.B. Nachrichtenanzahl, Backlogs).
Bei Problemen (z.B. volle Queue) sind Logs und Warnungen verfügbar. Es ist produktionsreif für den Enterprise-Einsatz.

#### Benötigen wir zusätzliche Plugins wie Kafka?
Nein, nichts wie Kafka wird benötigt – SIBus ist vollständig in WAS integriert (keine separate Installation oder Lizenz außerhalb von WAS selbst). Kafka ist eine andere, verteilte Streaming-Plattform; SIBus ist JMS-spezifisch und einfacher für WAS-Apps. Wenn Sie Kafka-ähnliche Funktionen benötigen (z.B. Streams), könnten Sie diese über Foreign Bus Links integrieren, aber für standardmäßiges JMS-Queuing sollten Sie beim Default Provider bleiben.

Für vertiefende Informationen lesen Sie die IBM-Docs zu [Managing messaging with the default messaging provider](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-managing-messaging-default-messaging-provider) und [How JMS applications connect to a messaging engine on a bus](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=messaging-how-jms-applications-connect-engine-bus).