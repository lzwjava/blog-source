---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Konfiguration von JMS-Ressourcen in WebSphere
translated: true
type: note
---

### Voraussetzungen
- Stellen Sie sicher, dass Sie administrativen Zugriff auf die IBM WebSphere Application Server (WAS) Integrated Solutions Console (Admin-Konsole) haben.
- Der Server sollte laufen, und Sie müssen den Geltungsbereich (z. B. Zelle, Knoten, Server) für die Ressourcen festlegen.
- Dieser Leitfaden konzentriert sich auf den Default Messaging Provider (der Service Integration Bus oder SIBus verwendet), den integrierten JMS-Provider in WAS. Bei Verwendung von WebSphere MQ ist eine zusätzliche Konfiguration für den MQ-Provider erforderlich.
- Starten Sie den Server nach größeren Änderungen neu, wenn Sie dazu aufgefordert werden.

### Schritt 1: Einen Service Integration Bus erstellen
Der Service Integration Bus dient als Messaging-Backbone für JMS-Ressourcen.

1. Melden Sie sich bei der WebSphere Integrated Solutions Console an.
2. Navigieren Sie zu **Service Integration > Buses**.
3. Klicken Sie auf **Neu**.
4. Geben Sie einen eindeutigen Busnamen ein (z. B. `MyJMSBus`).
5. Deaktivieren Sie die Option **Bus security**, sofern nicht erforderlich.
6. Klicken Sie auf **Weiter**, dann auf **Fertigstellen**, um den Bus zu erstellen.

### Schritt 2: Den Server als Bus-Member hinzufügen
Dies ermöglicht es dem Server, Messaging-Engines auf dem Bus zu hosten.

1. Wählen Sie den von Ihnen erstellten Bus aus (z. B. `MyJMSBus`).
2. Klicken Sie unter **Zusätzliche Eigenschaften** auf **Bus members**.
3. Klicken Sie auf **Hinzufügen**.
4. Führen Sie im Assistenten **Add a New Bus Member** folgende Schritte aus:
   - Wählen Sie **Messaging engine** als Bus-Member-Typ.
   - Wählen Sie Ihren Server (z. B. `server1`) aus der Liste aus.
   - Wählen Sie für den Message Store **File store** (Standard für nicht geclusterte Umgebungen) oder **Data store** für Datenbank-Persistenz und konfigurieren Sie bei Bedarf die Eigenschaften.
5. Klicken Sie auf **Weiter**, dann auf **Fertigstellen**.
6. Starten Sie den WebSphere Application Server neu, um das Bus-Member zu aktivieren.

### Schritt 3: Eine JMS Connection Factory erstellen
Eine Connection Factory wird benötigt, um JMS-Clients mit dem Provider zu verbinden.

1. Navigieren Sie zu **Ressourcen > JMS > Connection factories**.
2. Wählen Sie den entsprechenden Geltungsbereich (z. B. Server-Geltungsbereich für `server1`) und klicken Sie auf **Neu**.
3. Wählen Sie **Default messaging provider** und klicken Sie auf **OK**.
4. Geben Sie die Details ein:
   - **Name**: z. B. `MyJMSConnectionFactory`.
   - **JNDI-Name**: z. B. `jms/MyConnectionFactory`.
   - **Bus name**: Wählen Sie `MyJMSBus` aus dem Dropdown-Menü.
   - Belassen Sie die anderen Einstellungen standardmäßig (z. B. Provider endpoints auf auto-detected).
5. Klicken Sie auf **Übernehmen**, dann auf **Speichern**, um die Master-Konfiguration zu aktualisieren.

### Schritt 4: Eine JMS Queue erstellen
Dies definiert das Queue-Ziel für Point-to-Point-Messaging.

1. Navigieren Sie zu **Ressourcen > JMS > Queues**.
2. Wählen Sie den entsprechenden Geltungsbereich und klicken Sie auf **Neu**.
3. Wählen Sie **Default messaging provider** und klicken Sie auf **OK**.
4. Geben Sie die Details ein:
   - **Name**: z. B. `MyJMSQueue`.
   - **JNDI-Name**: z. B. `jms/MyQueue`.
   - **Bus name**: Wählen Sie `MyJMSBus`.
   - **Queue name**: Wählen Sie **Create Service Integration Bus Destination**, geben Sie einen eindeutigen Bezeichner ein (z. B. `MyQueueDestination`) und wählen Sie das zuvor erstellte Bus-Member aus.
   - **Base queue name**: z. B. `$MyJMSBus:MyQueueDestination` (automatisch generiert).
5. Konfigurieren Sie bei Bedarf zusätzliche Eigenschaften (z. B. delivery mode, expiry).
6. Klicken Sie auf **Übernehmen**, dann auf **Speichern**, um die Master-Konfiguration zu aktualisieren.

### Schritt 5: (Optional) Activation Specifications für Message-Driven Beans (MDBs) erstellen
Wenn Sie MDBs verwenden, um von der Queue zu konsumieren, konfigurieren Sie Activation Specs.

1. Navigieren Sie zu **Ressourcen > JMS > Activation specifications**.
2. Wählen Sie den entsprechenden Geltungsbereich und klicken Sie auf **Neu**.
3. Wählen Sie **Default messaging provider** und klicken Sie auf **OK**.
4. Geben Sie die Details ein:
   - **Name**: z. B. `MyActivationSpec`.
   - **JNDI-Name**: z. B. `jms/activation/MyActivationSpec`.
   - **Bus name**: Wählen Sie `MyJMSBus`.
   - **Destination type**: Queue.
   - **Destination**: Geben Sie den JNDI-Namen der Queue ein (z. B. `jms/MyQueue`).
5. Klicken Sie auf **Übernehmen**, dann auf **Speichern**, um die Master-Konfiguration zu aktualisieren.

### Verifikation und Test
- Synchronisieren Sie nach dem Speichern die Knoten, wenn Sie sich in einer geclusterten Umgebung befinden.
- Starten Sie den Server neu.
- Verwenden Sie eine JMS-Client-Anwendung, um das Senden/Empfangen von Nachrichten über die JNDI-Namen zu testen.
- Überwachen Sie die Vorgänge über **Service Integration > Buses > [Ihr Bus] > Bus members > [Ihr Member] > Messaging engines**.

Für erweiterte Konfigurationen (z. B. Sicherheit, Clustering) konsultieren Sie bitte die IBM-Dokumentation.

[Configuring IBM WebSphere Application Server for Decision Server](https://docs.redhat.com/en/documentation/red_hat_decision_manager/7.4/html/installing_and_configuring_decision_server_on_ibm_websphere_application_server/was-configure-proc)  
[Managing messaging with the default messaging provider](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-managing-messaging-default-messaging-provider)