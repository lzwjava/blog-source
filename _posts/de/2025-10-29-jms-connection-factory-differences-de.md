---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Unterschiede bei JMS-Verbindungsfabriken
translated: true
type: note
---

In IBM WebSphere Application Server (WAS) sind sowohl Connection Factories als auch Queue Connection Factories JMS-Ressourcen (Java Message Service), die verwendet werden, um Verbindungen zu einem JMS-Provider für Messaging herzustellen. Sie unterscheiden sich jedoch in Bezug auf ihren Geltungsbereich, ihre API-Kompatibilität und ihre Verwendung basierend auf den JMS-Domain-Modellen (Point-to-Point vs. Publish/Subscribe). Hier eine Aufschlüsselung:

### Hauptunterschiede

| Aspekt                  | Connection Factory                                                                 | Queue Connection Factory                                                                 |
|-------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Hauptzweck**          | Erstellt JMS-Verbindungen zu Destinations für **sowohl** Point-to-Point (Queues) als auch Publish/Subscribe (Topics) Messaging. Unterstützt die vereinheitlichte "Classic" API, die in JMS 1.1 eingeführt wurde. | Erstellt JMS-Verbindungen **ausschließlich** für Point-to-Point Messaging mit Queues. Basiert auf der Legacy-Domain-spezifischen API aus JMS 1.0. |
| **API-Hierarchie**      | Basis-Interface (`javax.jms.ConnectionFactory`). Kann dynamisch `Queue`- oder `Topic`-Destinations und Sessions in derselben Verbindung/Session erstellen. | Unterklasse von `ConnectionFactory` (`javax.jms.QueueConnectionFactory`). Erstellt nur `QueueConnection`- und `QueueSession`-Objekte; kann keine Topics verarbeiten. |
| **Flexibilität**        | Flexibler für moderne Anwendungen. Ermöglicht das Mischen von Queue- und Topic-Operationen in derselben Transaktion/Arbeitseinheit (JMS 1.1+). Ideal für Code, der zwischen Messaging-Stilen wechseln muss, ohne neu konfiguriert zu werden. | Weniger flexibel; beschränkt auf Queues. Nützlich für Legacy-JMS-1.0-Code oder strikte Trennung der Belange, bei der nur Point-to-Point benötigt wird. |
| **Konfiguration in WAS**| Konfiguriert unter **Ressourcen > JMS > Connection Factories** in der Admin-Konsole. Einem JMS-Provider zugeordnet (z.B. Default Messaging, WebSphere MQ). | Konfiguriert unter **Ressourcen > JMS > Queue Connection Factories**. An Queue-spezifische Provider wie IBM MQ oder Default Messaging gebunden, nur für Point-to-Point. |
| **Wann zu verwenden**   | Bevorzugt für neue Entwicklungen oder Apps, die JMS 1.1+ verwenden. Verwenden, wenn Ihre App möglicherweise mit sowohl Queues als auch Topics interagiert. | Verwenden für Abwärtskompatibilität mit JMS-1.0-Domain-spezifischem Code oder wenn explizit auf Queues beschränkt (z.B. in WebSphere MQ-Setups für Leistungs-/Sicherheitsisolation). |
| **Leistung/Sicherheit** | Allgemein gleichwertig, kann aber zusätzliche Einrichtung für domänenübergreifende Nutzung erfordern. | Kann für reinen Queue-Betrieb optimiert werden (z.B. Bindings Transport in MQ für höheren Durchsatz, ~30% Verbesserung). |

### Beispielverwendung im Code
- **Mit Connection Factory** (vereinheitlicht, flexibel):
  ```java
  ConnectionFactory factory = (ConnectionFactory) context.lookup("jms/ConnectionFactory");
  Connection conn = factory.createConnection();
  Session session = conn.createSession(false, Session.AUTO_ACKNOWLEDGE);
  // Kann beides erstellen:
  Queue queue = session.createQueue("myQueue");
  Topic topic = session.createTopic("myTopic");
  ```

- **Mit Queue Connection Factory** (nur Queues):
  ```java
  QueueConnectionFactory qFactory = (QueueConnectionFactory) context.lookup("jms/QueueConnectionFactory");
  QueueConnection qConn = qFactory.createQueueConnection();
  QueueSession qSession = qConn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
  Queue queue = qSession.createQueue("myQueue");
  // Kann hier keine Topics erstellen.
  ```

Zusammenfassend sollte man eine allgemeine Connection Factory für die Vielseitigkeit in zeitgenössischen JMS-Apps auf WAS wählen, während Queue Connection Factories ein spezialisiertes Überbleibsel für Queue-zentrierte oder Legacy-Szenarien sind.

[Connection Factory Collection - IBM](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=settings-connection-factory-collection)  
[Queue Connection Factory Collection - IBM](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=settings-queue-connection-factory-collection)  
[JMS QueueConnectionFactory vs ConnectionFactory - Stack Overflow](https://stackoverflow.com/questions/30121654/jms-queueconnectionfactory-vs-connectionfactory)  
[Queue Connection Factory VS Connection Factory - MQSeries.net](https://mqseries.net/phpBB/viewtopic.php?p=102901)