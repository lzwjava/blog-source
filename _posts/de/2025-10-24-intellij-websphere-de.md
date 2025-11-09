---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: IntelliJ IDEA für WebSphere-Entwicklung
translated: true
type: note
---

### Verwendung von IntelliJ IDEA für IBM WebSphere Application Server (WAS) Entwicklung

IntelliJ IDEA ist eine solide Wahl für die Entwicklung von Java EE-Anwendungen, die für den IBM WebSphere Application Server (WAS) bestimmt sind. Es unterstützt Java EE-Standards, an die sich WAS hält, und bietet hervorragende Werkzeuge zum Erstellen, Bereitstellen und Debuggen von Enterprise-Apps. Während Eclipse über eine natürlichere WAS-Integration via IBM-Tools verfügt, funktioniert IntelliJ mit etwas Einrichtung gut. Im Folgenden werden die Grundlagen, Remote-Debugging (ja, Sie können sich an die WAS-JVM anhängen) und zusätzliche Tipps behandelt.

#### 1. Ersteinrichtung für die WAS-Entwicklung in IntelliJ
- **Erforderliche Plugins installieren**:
  - Gehen Sie zu **Datei > Einstellungen > Plugins** und suchen Sie im JetBrains Marketplace nach "WebSphere Server". Installieren Sie es für ein besseres lokales Servermanagement (z.B. Starten/Stoppen von WAS aus IntelliJ). Dieses Plugin ist nicht im Lieferumfang enthalten, daher ist es optional, aber für die lokale Entwicklung empfohlen.
  - Stellen Sie sicher, dass die Java EE und Jakarta EE Plugins aktiviert sind (sie sind normalerweise vorinstalliert).

- **Ein Projekt erstellen**:
  - Starten Sie ein neues **Java Enterprise**-Projekt (oder importieren Sie ein bestehendes).
  - Wählen Sie den **Web Application**-Archetyp und konfigurieren Sie ihn für Java EE (z.B. Version 8 oder 9, abhängig von Ihrer WAS-Version wie 9.x).
  - Fügen Sie bei Bedarf Abhängigkeiten für WAS-spezifische Bibliotheken hinzu (z.B. via Maven/Gradle: `com.ibm.websphere.appserver.api:jsp-2.3` für JSP-Unterstützung).

- **Lokalen WAS-Server konfigurieren (Optional für lokale Ausführungen)**:
  - Gehen Sie zu **Ausführen > Konfigurationen bearbeiten > + > WebSphere Server > Lokal**.
  - Zeigen Sie auf Ihr lokales WAS-Installationsverzeichnis (z.B. `/opt/IBM/WebSphere/AppServer`).
  - Legen Sie den Servernamen, die JRE (verwenden Sie IBMs JDK, falls mit WAS gebündelt) und Bereitstellungsoptionen fest (z.B. explodiertes WAR für Hot-Reload).
  - Für die Bereitstellung: Fügen Sie im Tab **Bereitstellung** Ihr Artefakt (z.B. WAR-Datei) hinzu und legen Sie den Kontextpfad fest.

Dieses Setup ermöglicht es Ihnen, direkt aus IntelliJ für lokale Tests auszuführen/bereitzustellen.

#### 2. Remote-Debugging: Anhängen von IntelliJ an die WAS-JVM
Ja, Sie können den IntelliJ-Debugger absolut an eine entfernte WAS-JVM anhängen. Dies ist Standard-Java-Remote-Debugging via JDWP (Java Debug Wire Protocol). Es funktioniert sowohl für lokale als auch für entfernte WAS-Instanzen – behandeln Sie den Server einfach als "Remote JVM".

**Schritt 1: Debugging auf dem WAS-Server aktivieren**
- **Via Admin Console (Empfohlen für Produktions-ähnliche Setups)**:
  - Melden Sie sich bei der WAS Admin Console an (z.B. `https://your-host:9043/ibm/console`).
  - Navigieren Sie zu **Server > Servertypen > WebSphere Application Servers > [Ihr Server] > Debugging Service**.
  - Aktivieren Sie **Enable service at server startup**.
  - Legen Sie den **JVM debug port** fest (Standard ist 7777; wählen Sie einen unbenutzten Port wie 8000, um Konflikte zu vermeiden).
  - Speichern Sie und starten Sie den Server neu.

- **Via server.xml (Für Standalone- oder Schnellbearbeitungen)**:
  - Bearbeiten Sie `$WAS_HOME/profiles/[Profil]/config/cells/[Zelle]/nodes/[Knoten]/servers/[Server]/server.xml`.
  - Fügen Sie im Abschnitt `<jvmEntries>` unter `<processDefinitions>` hinzu oder aktualisieren Sie:
    ```
    <jvmEntries xmi:id="..." debugMode="true">
      <debugArgs>-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:8000</debugArgs>
    </jvmEntries>
    ```
    - `suspend=n` startet den Server normal (verwenden Sie `suspend=y`, um beim Start anzuhalten).
    - Ersetzen Sie `8000` durch Ihren Port.
  - Speichern Sie und starten Sie dann den Server neu: `./startServer.sh [ServerName]` (oder via Konsole).

- Überprüfen: Prüfen Sie die Server-Logs auf "JDWP: transport=dt_socket, address=*:8000" oder ähnliches.

**Schritt 2: Remote-Debugging in IntelliJ konfigurieren**
- Gehen Sie zu **Ausführen > Konfigurationen bearbeiten > + > Remote JVM Debug**.
- Geben Sie einen Namen ein (z.B. "WAS Remote Debug").
- Setzen Sie den **Debugger mode** auf "Attach to remote JVM".
- **Host**: Ihre WAS-Server-IP/ Hostname (z.B. `localhost` für lokal, `192.168.1.100` für remote).
- **Port**: Der JVM-Debug-Port (z.B. 8000).
- Optional: Legen Sie **Use module classpath** fest, wenn Ihr Projekt spezifische Bibliotheken hat.
- Übernehmen und schließen.

**Schritt 3: Anhängen und Debuggen**
- Setzen Sie Breakpoints in Ihrem Code (z.B. in einem Servlet oder EJB).
- Stellen Sie Ihre App auf WAS bereit (manuell via Admin Console oder wsadmin-Skripte).
- Führen Sie die Debug-Konfiguration aus (**Ausführen > Debuggen 'WAS Remote Debug'**).
- Rufen Sie Ihre App auf (z.B. via HTTP-Request). IntelliJ wird sich anheften und die Ausführung an den Breakpoints anhalten.
- Häufige Probleme: Die Firewall blockiert den Port, nicht übereinstimmende JDK-Versionen (verwenden Sie WAS's IBM JDK in IntelliJ) oder der Server wurde nach Konfigurationsänderungen nicht neu gestartet.

Dies funktioniert für WAS 7+ (einschließlich Liberty Profile). Für entfernte Server stellen Sie sicher, dass der Netzwerkzugriff auf den Debug-Port besteht.

#### 3. Weitere Tipps für eine effiziente WAS-Entwicklung
- **Hot Deployment/Hotswap**: Für schnellere Iterationen stellen Sie als "explodiertes" WAR (entpackt) bereit. WAS unterstützt Hot-Reload für JSPs und einige Klassen, aber für vollständigen Hotswap (Code-Änderungen ohne Neustart) verwenden Sie das JRebel-Plugin (kostenpflichtig) oder DCEVM + HotSwapAgent (kostenlos, aber Kompatibilität mit WAS's IBM JDK testen).

- **Build-Tools**: Verwenden Sie Maven oder Gradle für Abhängigkeiten. Fügen Sie WAS-Laufzeitbibliotheken als provided Scope hinzu, um Classpath-Bloat zu vermeiden:
  ```
  <dependency>
    <groupId>com.ibm.websphere.appserver.runtime</groupId>
    <artifactId>shared</artifactId>
    <version>9.0.5</version>
    <scope>provided</scope>
  </dependency>
  ```
  Führen Sie `mvn clean package` aus und stellen Sie das WAR via Admin Console bereit.

- **Logging und Profiling**: Integrieren Sie SLF4J/Logback für App-Logs. Für die Performance verwenden Sie VisualVM oder YourKit (remote anhängen wie beim Debugging). WAS's PMI (Performance Monitoring Infrastructure) ist großartig – aktivieren Sie es in der Admin Console für Metriken.

- **Testing**: Verwenden Sie Arquillian für Integrationstests gegen einen entfernten WAS. Oder embedden Sie Open Liberty (WAS-kompatibel) für lokale Unit-Tests ohne vollen WAS.

- **Versionsspezifische Hinweise**: Für WAS 9.x+ nutzen Sie die Jakarta EE-Migrationstools in IntelliJ. Wenn Sie WAS Liberty (Microprofile-fokussiert) verwenden, fügt das Liberty Tools Plugin einen Dev-Modus mit Auto-Reload hinzu.

- **Häufige Fallstricke**:
  - Classpath-Probleme: Stellen Sie sicher, dass IntelliJ's Projekt-SDK mit WAS's JDK übereinstimmt.
  - Sicherheit: Remote-Debugging exponiert den Port – verwenden Sie es nur in Dev/vertrauenswürdigen Netzwerken.
  - Plugin-Einschränkungen: Das WebSphere-Plugin ist grundlegend; für erweiterte Funktionen ziehen Sie IBMs Rational Application Developer in Betracht (bleiben Sie aber bei IntelliJ für dessen UX).

Dies sollte Ihnen den Einstieg ermöglichen. Wenn Sie eine spezifische WAS-Version verwenden, teilen Sie Details für eine maßgeschneidertere Beratung mit.

#### Referenzen
- [Run/Debug Configuration: WebSphere Server | IntelliJ IDEA](https://www.jetbrains.com/help/idea/run-debug-configuration-websphere-server.html)
- [WebSphere remote server debug configuration in IntelliJ Idea](https://stackoverflow.com/questions/33013860/websphere-remote-server-debug-configuration-in-intellij-idea)
- [Debug code running on IBM Websphere using Eclipse / Intellij IDEA](https://davanum.wordpress.com/2009/11/20/debug-code-running-on-ibm-websphere-using-eclipse-intellij-idea/)
- [Debugging applications - IBM](https://www.ibm.com/docs/en/was/9.0.5?topic=applications-debugging)
- [Remote Debugging with IntelliJ IDEA | Baeldung](https://www.baeldung.com/intellij-remote-debugging)