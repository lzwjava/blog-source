---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Konfiguration von IBM MQ in WebSphere
translated: true
type: note
---

### Konfiguration von Message Queues in IBM WebSphere Application Server (mit IBM MQ als Provider)

IBM WebSphere Application Server (WAS) unterstützt Message Queuing über Java Message Service (JMS)-Integration mit IBM MQ (früher WebSphere MQ). Die Konfiguration erfolgt typischerweise über die **WebSphere Integrated Solutions Console** (die Administrationsoberfläche), erreichbar unter `https://your-server:9043/ibm/console` (standardmäßiger sicherer Port; bei Bedarf anpassen). Diese Anleitung konzentriert sich auf das traditionelle WAS mit Vollprofil (z.B. Version 9.0+), die Schritte sind jedoch für WebSphere Liberty mit geringen Anpassungen ähnlich.

#### Voraussetzungen
- IBM MQ muss installiert, gestartet und erreichbar sein (z.B. Queue Manager gestartet).
- Der WAS-Server ist gestartet und Sie haben Administratorzugriff auf die Konsole.
- Laden Sie die IBM MQ JMS Client-Bibliotheken (z.B. `com.ibm.mq.allclient.jar`) herunter und installieren Sie sie in den Shared Libraries von WAS (unter **Umgebung > Gemeinsam genutzte Bibliotheken**), falls noch nicht geschehen.
- Stellen Sie sicher, dass der WebSphere MQ Messaging-Provider konfiguriert ist (unter **Ressourcen > JMS > JMS-Provider**). Falls nicht, erstellen Sie einen mit Details wie Host, Port (Standard 1414) und Queue-Manager-Namen.

Nach der Konfiguration speichern Sie die Änderungen (**Speichern**-Button oben) und starten den Anwendungsserver neu, damit diese wirksam werden.

#### Schritt 1: Eine JMS Queue Connection Factory erstellen
Die Connection Factory stellt Verbindungen zum IBM MQ Queue Manager her.

1. Melden Sie sich bei der WAS-Administrationskonsole an.
2. Erweitern Sie im Navigationsbereich **Ressourcen > JMS > Warteschlangenverbindungsfactorys**.
3. Wählen Sie den entsprechenden **Bereich** (Scope) (z.B. Zelle, Knoten, Server) aus dem Dropdown-Menü und klicken Sie auf **Übernehmen**.
4. Klicken Sie auf **Neu**.
5. Wählen Sie **WebSphere MQ Messaging-Provider** und klicken Sie auf **OK**.
6. Auf dem nächsten Bildschirm:
   - **Name**: Geben Sie einen beschreibenden Namen ein (z.B. `MyMQQueueConnectionFactory`).
   - **JNDI-Name**: Geben Sie eine JNDI-Bindung ein (z.B. `jms/MyQueueConnectionFactory`).
   - Klicken Sie auf **Weiter**.
7. Geben Sie die Verbindungsdetails ein:
   - **Queue-Manager**: Name Ihres IBM MQ Queue Managers (z.B. `QM1`).
   - **Hostname**: Hostname oder IP-Adresse des IBM MQ-Servers.
   - **Port**: Listener-Port (Standard: 1414).
   - **Transporttyp**: CHANNEL (für Client-Modus) oder BINDINGS (für eingebetteten Modus).
   - **Kanal**: Name des Standardkanals (z.B. `SYSTEM.DEF.SVRCONN`).
   - **Benutzer-ID** und **Passwort**: Anmeldedaten für die MQ-Authentifizierung (falls erforderlich).
   - Klicken Sie auf **Weiter**.
8. Überprüfen Sie die Zusammenfassung und klicken Sie auf **Fertig stellen**.
9. Wählen Sie die neue Factory aus, gehen Sie zu **Zusätzliche Eigenschaften > Verbindungspool** (optional) und passen Sie Einstellungen wie **Maximale Verbindungen** an (z.B. basierend auf der erwarteten Last).
10. Klicken Sie auf **Verbindung testen**, um diese zu überprüfen.

#### Schritt 2: Ein JMS Queue Destination erstellen
Dies definiert den eigentlichen Queue-Endpunkt zum Senden/Empfangen von Nachrichten.

1. Erweitern Sie im Navigationsbereich **Ressourcen > JMS > Warteschlangen**.
2. Wählen Sie den entsprechenden **Bereich** (Scope) (übereinstimmend mit der Connection Factory) und klicken Sie auf **Übernehmen**.
3. Klicken Sie auf **Neu**.
4. Wählen Sie **WebSphere MQ Messaging-Provider** und klicken Sie auf **OK**.
5. Geben Sie die Eigenschaften an:
   - **Name**: Beschreibender Name (z.B. `MyRequestQueue`).
   - **JNDI-Name**: JNDI-Bindung (z.B. `jms/MyRequestQueue`).
   - **Basis-Warteschlangenname**: Exakter Queue-Name in IBM MQ (z.B. `REQUEST.QUEUE`; muss in MQ existieren oder erstellt werden).
   - **Zielclient**: JMS (für JMS-Apps) oder MQ (für native MQ-Apps).
   - **Ziel-Zielmodus**: Einmalig (Standard für Zuverlässigkeit).
   - Klicken Sie auf **OK**.
6. (Optional) Konfigurieren Sie unter **Zusätzliche Eigenschaften** Einstellungen für Persistenz, Ablauf oder Priorität.
7. Speichern Sie die Konfiguration.

#### Schritt 3: (Optional) Eine Activation Specification für Message-Driven Beans (MDBs) erstellen
Falls MDBs verwendet werden, um Nachrichten asynchron zu konsumieren:

1. Erweitern Sie im Navigationsbereich **Ressourcen > JMS > Aktivierungsspezifikationen**.
2. Wählen Sie den **Bereich** (Scope) und klicken Sie auf **Neu**.
3. Wählen Sie **WebSphere MQ Messaging-Provider** und klicken Sie auf **OK**.
4. Geben Sie ein:
   - **Name**: z.B. `MyQueueActivationSpec`.
   - **JNDI-Name**: z.B. `jms/MyQueueActivation`.
   - **Zieltyp**: Warteschlange (Queue).
   - **Ziel-JNDI-Name**: Die JNDI Ihrer Warteschlange (z.B. `jms/MyRequestQueue`).
   - **Verbindungsfactory-JNDI-Name**: Die JNDI Ihrer Connection Factory (z.B. `jms/MyQueueConnectionFactory`).
   - Nachrichten-Selektor (optional): JMS-Selektor zum Filtern von Nachrichten.
5. Erstellen Sie unter **Zusätzliche Eigenschaften > Message Listener Service > Listener-Ports** bei Bedarf einen Port:
   - **Name**: z.B. `MyListenerPort`.
   - **Verbindungsfactory-JNDI**: Wie oben.
   - **Ziel-JNDI**: Wie oben.
   - **Komponente**: Der Bereitstellungsdeskriptor Ihrer MDB.
6. Klicken Sie auf **OK** und speichern Sie.

#### Schritt 4: Überprüfen und Testen
- **In der Konsole testen**: Verwenden Sie **Verbindung testen** bei Factorys und Spezifikationen.
- **Eine App bereitstellen**: Erstellen Sie eine einfache JMS-Client- oder MDB-App, stellen Sie sie bereit und senden/testen Sie Nachrichten über IBM MQ-Tools (z.B. MQ Explorer).
- **Monitoring**: Unter **Überwachung und Optimierung > Performance Viewer** oder **Fehlerbehebung > Protokolle** können Sie nach JMS-bezogenen Fehlern suchen.
- Häufige Probleme:
  - Verbindungsfehler: Überprüfen Sie die Firewall, den MQ-Kanalstatus (`DISPLAY CHANNEL`) und die Anmeldedaten.
  - JNDI-Lookup-Fehler: Stellen Sie sicher, dass die Bindungen korrekt sind und die App den richtigen Bereich verwendet.
  - Persistenz: Stimmen Sie die Dauerhaftigkeitseinstellungen zwischen WAS und MQ ab.

Für Befehlszeilenalternativen (wsadmin-Scripting) siehe IBM-Dokumentation. Passen Sie die Einstellungen basierend auf Ihrer Version an (z.B. unterstützt WAS 9.0.5+ JMS 2.0).

#### Referenzen
- [Konfigurieren von JMS-Ressourcen in WebSphere Application Server](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=resources-configuring-jms-in-websphere-application-server)
- [Einstellungen für WebSphere MQ Messaging-Provider Warteschlange](https://www.ibm.com/docs/en/was/8.5.5?topic=settings-websphere-mq-messaging-provider-queue)
- [Erstellen einer WebSphere MQ Messaging-Provider Warteschlangenverbindungsfactory](https://help.hcl-software.com/commerce/7.0.0/com.ibm.commerce.integration.doc/tasks/tcvjmsqueuefactory.html)
- [Konfigurieren eines JMS-Warteschlangen-Ziels für WebSphere MQ](http://www.setgetweb.com/p/i5/portal/WAS60/Configure_JMS_queue_destinationfor_WebSphere_MQ.html)