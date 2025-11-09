---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: IBM MQ WebSphere Application Server Konfiguration
translated: true
type: note
---

### Voraussetzungen
Bevor Sie IBM MQ (früher WebSphere MQ) in IBM WebSphere Application Server (WAS) konfigurieren, stellen Sie Folgendes sicher:
- IBM MQ ist auf einem dedizierten Server installiert (oder auf demselben wie WAS für den Local-Bindings-Modus).
- Ein Queue-Manager wurde in IBM MQ erstellt (z. B. mit `crtmqm QMNAME`).
- Die erforderlichen Queues wurden im Queue-Manager erstellt (z. B. mit MQ Explorer oder `runmqsc`).
- IBM MQ-Client-Bibliotheken (JAR-Dateien wie `com.ibm.mq.allclient.jar`, `com.ibm.mqjms.jar`) sind verfügbar. Wenn WAS remote von MQ ist, installieren Sie den IBM MQ-Client auf dem WAS-Rechner.
- Fügen Sie den WAS-Prozessbenutzer zur `mqm`-Gruppe für Berechtigungen hinzu.
- Für Nicht-Root-Benutzer auf Unix-ähnlichen Systemen verwenden Sie `setmqaut`, um Berechtigungen zu erteilen.

### Schritt-für-Schritt-Konfiguration
Die Konfiguration umfasst das Einrichten des JMS-Providers, der Connection Factories und der Destinations in der WAS Administrative Console. Dies geht von einer verteilten (Client-)Modus-Verbindung über TCP/IP aus; passen Sie dies für den Bindings-Modus an, falls lokal.

1. **Auf die WAS Administrative Console zugreifen**:
   - Starten Sie den WAS-Server.
   - Öffnen Sie einen Browser und navigieren Sie zu `https://localhost:9043/ibm/console` (ersetzen Sie mit Ihrem Host/Port).
   - Melden Sie sich mit Administrator-Anmeldedaten an.

2. **Den IBM MQ JMS-Provider konfigurieren**:
   - Gehen Sie zu **Ressourcen > JMS > Provider**.
   - Klicken Sie auf **Neu**.
   - Wählen Sie **WebSphere MQ Messaging Provider**.
   - Füllen Sie die Details aus:
     - **Name**: z. B. `MQProvider`.
     - **Beschreibung**: Optional.
     - **Klassenpfad**: Pfad zu den MQ-JAR-Dateien (z. B. `/opt/mqm/java/lib/*` oder kopieren nach `<WAS_HOME>/lib/ext`).
     - **Nativer Bibliothekspfad**: Erforderlich für den Bindings-Modus (Pfad zu den MQ-Bibliotheken, z. B. `/opt/mqm/lib64`).
     - **Name der externen Initial Context Factory**: `com.ibm.mq.jms.context.WMQInitialContextFactory` (für Client-Modus).
     - **URL des externen Context Providers**: z. B. `host:1414/CHANNEL` (host = MQ-Server-IP, 1414 = Standard-Port, CHANNEL = z. B. `SYSTEM.DEF.SVRCONN`).
   - Speichern Sie die Konfiguration.

3. **Eine Queue Connection Factory erstellen**:
   - Gehen Sie zu **Ressourcen > JMS > Queue Connection Factories** (Scope auf Ihren Server oder Cell setzen).
   - Klicken Sie auf **Neu**.
   - Wählen Sie den in Schritt 2 erstellten Provider.
   - Füllen Sie aus:
     - **Name**: z. B. `MQQueueCF`.
     - **JNDI-Name**: z. B. `jms/MQQueueCF`.
     - **Queue Manager**: Ihr MQ-Queue-Manager-Name (z. B. `QM1`).
     - **Host**: MQ-Server-Hostname oder IP.
     - **Port**: 1414 (Standard).
     - **Channel**: z. B. `SYSTEM.DEF.SVRCONN`.
     - **Transporttyp**: `CLIENT` (für TCP/IP) oder `BINDINGS` (lokal).
     - **Sicherheitsanmeldedaten**: Benutzer-ID und Passwort, falls erforderlich.
   - Optionale erweiterte Eigenschaften: Setzen Sie Connection-Pool-Größen (z. B. maximale Verbindungen basierend auf Ihrer Last).
   - Speichern.

4. **Queue Destinations erstellen**:
   - Gehen Sie zu **Ressourcen > JMS > Queues**.
   - Klicken Sie auf **Neu**.
   - Wählen Sie den Provider.
   - Für jede Queue:
     - **Name**: z. B. `MyQueue`.
     - **JNDI-Name**: z. B. `jms/MyQueue`.
     - **Queue-Name**: Exakter Queue-Name in MQ (z. B. `MY.LOCAL.QUEUE`).
     - **Queue Manager**: Derselbe wie oben.
     - **Zielclienttyp**: `MQ` oder `JMS`.
   - Speichern. Wiederholen Sie dies für Topics, falls Pub/Sub verwendet wird.

5. **(Optional) WebSphere MQ Server für Bindings-Modus konfigurieren**:
   - Wenn Sie Local Bindings verwenden, gehen Sie zu **Server > Servertypen > WebSphere MQ-Server**.
   - Klicken Sie auf **Neu**.
   - Setzen Sie **Name**, **Queue-Manager-Name**.
   - Geben Sie **MQ-Installationen** an (Pfad zur MQ-Installation).
   - Speichern Sie und starten Sie den Server neu.

6. **JCA Resource Adapter konfigurieren (für MDBs)**:
   - Gehen Sie zu **Ressourcen > Resource Adapters > J2C Connection Factories**.
   - Wenn Sie den eingebauten MQ-RA verwenden, stellen Sie sicher, dass er deployed ist (WAS beinhaltet `wmq.jmsra.rar`).
   - Setzen Sie Eigenschaften wie maximale Verbindungen (z. B. 10-50 basierend auf der Last).

7. **Die Konfiguration testen**:
   - Deployen Sie eine JMS-Beispielanwendung oder verwenden Sie die WAS-JMS-Beispiele.
   - Prüfen Sie die Logs auf Fehler (z. B. Verbindungsverweigerung auf Port 1414).
   - Verifizieren Sie in MQ: Verwenden Sie MQ Explorer, um Queue-Tiefen und Channels zu überwachen.

8. **Sicherheit und erweiterte Einrichtung**:
   - SSL aktivieren: Konfigurieren Sie Keystores in WAS und MQ (Channel mit `SSLCIPH`).
   - Authentifizierung einrichten: Verwenden Sie MQ-Benutzergruppen oder alternative Benutzer-IDs.
   - Für Cluster: Synchronisieren Sie Konfigurationen über Nodes hinweg.

### Tipps zur Problembehebung
- **ClassNotFoundException**: Stellen Sie sicher, dass sich die MQ-JARs im Klassenpfad befinden.
- **Verbindungsfehler**: Prüfen Sie die Firewall auf Port 1414, Channel-Status (`DISPLAY CHSTATUS(*)` in runmqsc).
- **Probleme im Bindings-Modus**: Überprüfen Sie native Bibliotheken und Benutzer in der `mqm`-Gruppe.
- Starten Sie WAS nach Änderungen neu.

Für versionsspezifische Details (z. B. WAS 9.x mit MQ 9.x) konsultieren Sie die offiziellen IBM-Dokumente.

[Using WebSphere Application Server with IBM MQ](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=together-using-websphere-application-server-mq)  
[Configuring WebSphere Application Server for use with IBM MQ](https://help.hcl-software.com/commerce/9.0.0/integration/tasks/tcvconfigure_was_for_mq.html)  
[Creating a WebSphere MQ server definition](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.multiplatform.doc/ae/tjfp0004_.html)