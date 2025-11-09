---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: JMS- und JNDI-APIs für WebSphere
translated: true
type: note
---

### Erforderliche Pakete und APIs für JMS in Java

Um den von Ihnen referenzierten JMS-Codeausschnitt (für die Suche und Verbindung zu einer JMS Connection Factory im IBM WebSphere Application Server) zu verwenden, müssen Sie die relevanten Java-Pakete importieren. Dies sind Standard-APIs aus dem Java EE/Jakarta EE-Ökosystem:

- **JNDI (Java Naming and Directory Interface)**: Für den `InitialContext`-Lookup.
  - Paket: `javax.naming` (oder `jakarta.naming` in neueren Jakarta EE-Versionen).
  - Wichtige Klasse: `InitialContext` – Dies ist der Ausgangspunkt für JNDI-Operationen. Er bietet einen Kontext zum Suchen von Ressourcen (wie JMS-Factories oder Queues) anhand ihrer JNDI-Namen (z.B. `"jms/MyConnectionFactory"`). In einem Container wie WAS verbindet er sich automatisch mit dem Naming-Dienst des Servers.

- **JMS (Java Message Service) API**: Zum Erstellen von Verbindungen, Sessions, Sendern/Empfängern und Nachrichten.
  - Paket: `javax.jms` (JMS 1.1/2.0) oder `jakarta.jms` (Jakarta JMS 3.0+ im modernen EE).
  - Wichtige Interfaces: `QueueConnectionFactory`, `QueueConnection`, `QueueSession`, `QueueSender`, `Queue`, `TextMessage`, usw.

Beispiel-Imports am Anfang Ihrer Java-Klasse:
```java
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueConnection;
import javax.jms.QueueSession;
import javax.jms.Queue;
import javax.jms.QueueSender;
import javax.jms.TextMessage;
import javax.jms.JMSException;
```

**Was ist `InitialContext`?**  
Es ist eine Klasse in der JNDI-API, die als Einstiegspunkt für einen Naming-Dienst dient. In Ihrem Code:  
```java
InitialContext ctx = new InitialContext();  // Erstellt einen Standardkontext, der an die JNDI-Umgebung des App-Servers gebunden ist
QueueConnectionFactory qcf = (QueueConnectionFactory) ctx.lookup("jms/MyConnectionFactory");  // Sucht die vorkonfigurierte Factory anhand ihres JNDI-Namens
```  
Im Konstruktor sind keine Properties für Apps erforderlich, die *innerhalb* von WAS laufen, da der Container die Umgebung injiziert (z.B. via `java.naming.factory.initial`). Wenn Sie einen eigenständigen Client *außerhalb* von WAS betreiben, würden Sie eine `Hashtable` mit Properties wie der Provider-URL übergeben.

### Maven-Abhängigkeiten (pom.xml)

Wenn Ihre Java-App **in WAS bereitgestellt und ausgeführt wird** (z.B. als Web-App, EJB oder Enterprise Bean):  
- **Keine zusätzlichen Abhängigkeiten erforderlich**. WAS stellt die JMS- und JNDI-APIs out-of-the-box als Teil seiner Java EE-Laufzeitumgebung bereit. Kompilieren Sie einfach dagegen (sie sind während Build/Deploy im Classpath).  
- In `pom.xml` können Sie sie explizit mit `<scope>provided</scope>` deklarieren, um sie nicht in Ihr WAR/EAR zu packen (hält es schlank):  
  ```xml
  <dependencies>
      <dependency>
          <groupId>javax.jms</groupId>  <!-- Oder jakarta.jms für neuere Versionen -->
          <artifactId>javax.jms-api</artifactId>
          <version>2.0.1</version>  <!-- JMS 2.0, kompatibel mit WAS 8.5+ -->
          <scope>provided</scope>
      </dependency>
      <dependency>
          <groupId>javax.naming</groupId>
          <artifactId>javax.naming-api</artifactId>
          <version>1.0</version>  <!-- JNDI 1.0, Standard -->
          <scope>provided</scope>
      </dependency>
  </dependencies>
  ```

Wenn Ihre App ein **eigenständiger Client** ist (der außerhalb von WAS läuft, z.B. ein Thin Client, der eine Verbindung zum Server herstellt):  
- Benötigen Sie die **WebSphere Application Client**-Bibliotheken für volle JMS-Unterstützung über IIOP. Laden Sie das Client-Paket "IBM WebSphere Application Server traditional" von IBM herunter und fügen Sie es dann zu Ihrem Classpath hinzu.  
- In `pom.xml` aufnehmen:  
  ```xml
  <dependency>
      <groupId>com.ibm.ws</groupId>
      <artifactId>was-jms-client</artifactId>  <!-- Ungefähr; verwenden Sie IBM's Maven-Repo, falls verfügbar -->
      <version>9.0.5</version>  <!-- Stimmen Sie Ihre WAS-Version ab -->
  </dependency>
  ```  
  Oder verwenden Sie die vollständigen Thin Client-JARs (z.B. `com.ibm.ws.orb_8.5.5.jar`, `com.ibm.ws.jndi_*.jar`). Prüfen Sie die IBM-Dokumentation für das genaue Setup.

Für die Jakarta EE-Migration (nach 2020) wechseln Sie zu `jakarta.*`-Paketen, aber WAS 9.x verwendet standardmäßig noch `javax.*` – aktivieren Sie Jakarta bei Bedarf über Feature Packs.

[IBM WebSphere JMS API-Dokumentation](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-jms-api)  
[Java EE JNDI Tutorial](https://docs.oracle.com/javase/tutorial/jndi/)