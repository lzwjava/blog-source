---
audio: true
generated: false
lang: de
layout: post
title: Fehlerbehebung bei der Bereitstellung im WebSphere Liberty Profile
translated: true
---

Wenn Sie versuchen, auf Ihre Spring Boot-Anwendung unter `http://localhost:9080/myapp/` zuzugreifen und dabei einen "context root not found"-Fehler auf WebSphere Liberty Profile (WLP) erhalten, bedeutet dies, dass WLP Ihre Anwendung nicht unter dem erwarteten Kontextpfad (`/myapp`) erfolgreich bereitgestellt hat. Dieses Problem tritt in der Regel aufgrund von Problemen mit der Bereitstellungs-Konfiguration, der Server-Einrichtung oder der WAR-Datei selbst auf. Im Folgenden finden Sie eine umfassende Anleitung zur Fehlerbehebung und Behebung dieses Problems.

---

### Verständnis des Problems
Der "context root not found"-Fehler bedeutet, dass WLP eine unter `/myapp` bereitgestellte Anwendung nicht finden kann. Normalerweise wird, wenn Sie eine WAR-Datei namens `myapp.war` in das `dropins`-Verzeichnis von WLP legen, diese automatisch mit dem Kontextpfad `/myapp` bereitgestellt, sodass sie unter `http://localhost:9080/myapp/` zugänglich ist. Da dies nicht der Fall ist, müssen wir untersuchen, warum die Bereitstellung fehlgeschlagen ist.

---

### Schritte zur Fehlerbehebung

#### 1. **Überprüfen Sie die Serverprotokolle auf Bereitstellungsnachrichten**
Der erste Schritt besteht darin zu bestätigen, ob WLP Ihre Anwendung bereitgestellt hat.

- **Protokolle finden:**
  - Wenn Ihr Server `myServer` heißt, überprüfen Sie die Protokolle unter:
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/messages.log
    ```
    oder
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/console.log
    ```
  - Wenn Sie den Standardserver verwenden, ersetzen Sie `myServer` durch `defaultServer`.

- **Bereitstellungsbestätigung suchen:**
  - Sie sollten eine Nachricht wie diese sehen:
    ```
    [AUDIT   ] CWWKT0016I: Webanwendung verfügbar (default_host): http://localhost:9080/myapp/
    ```
    Dies zeigt an, dass die Anwendung bereitgestellt und verfügbar ist.
  - Zusätzlich sollten Sie nach folgendem suchen:
    ```
    CWWKZ0001I: Anwendung myapp gestartet in X.XXX Sekunden.
    ```
    Dies bestätigt, dass die Anwendung erfolgreich gestartet wurde.

- **Was zu tun ist:**
  - Wenn diese Nachrichten fehlen, wurde die Anwendung nicht bereitgestellt. Suchen Sie nach `ERROR`- oder `WARNING`-Nachrichten in den Protokollen, die angeben könnten, warum (z. B. fehlende Funktionen, Dateiberechtigungen oder Startfehler).
  - Wenn Sie Spring Boot-Startprotokolle sehen (z. B. das Spring Boot-Banner), wird die Anwendung geladen, und das Problem könnte mit dem Kontextpfad oder der URL-Zuordnung zusammenhängen.

#### 2. **Überprüfen Sie den Speicherort und die Berechtigungen der WAR-Datei**
Stellen Sie sicher, dass die WAR-Datei korrekt im `dropins`-Verzeichnis platziert ist und für WLP zugänglich ist.

- **Pfad überprüfen:**
  - Für einen Server namens `myServer` sollte sich die WAR-Datei unter:
    ```
    /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
    befinden.
  - Wenn `defaultServer` verwendet wird, passen Sie entsprechend an:
    ```
    /opt/ibm/wlp/usr/servers/defaultServer/dropins/myapp.war
    ```

- **Berechtigungen überprüfen:**
  - Stellen Sie sicher, dass der WLP-Prozess Leseberechtigungen für die Datei hat. Auf einem Unix-ähnlichen System führen Sie aus:
    ```bash
    ls -l /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
    Die Datei sollte vom Benutzer, der WLP ausführt, lesbar sein (z. B. `rw-r--r--`).

- **Was zu tun ist:**
  - Wenn die Datei fehlt oder falsch platziert ist, kopieren Sie sie in das richtige `dropins`-Verzeichnis:
    ```bash
    cp target/myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
    ```
  - Bei Bedarf Berechtigungen korrigieren:
    ```bash
    chmod 644 /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```

#### 3. **Überprüfen Sie die Überwachung von `dropins` in `server.xml`**
Das `dropins`-Verzeichnis von WLP ist standardmäßig aktiviert, aber benutzerdefinierte Konfigurationen könnten es deaktivieren.

- **`server.xml` überprüfen:**
  - Öffnen Sie die Serverkonfigurationsdatei:
    ```
    /opt/ibm/wlp/usr/servers/myServer/server.xml
    ```
  - Suchen Sie nach dem `applicationMonitor`-Element:
    ```xml
    <applicationMonitor updateTrigger="polled" pollingRate="5s" dropins="dropins" />
    ```
    Dies bestätigt, dass WLP das `dropins`-Verzeichnis alle 5 Sekunden auf neue Anwendungen überprüft.

- **Was zu tun ist:**
  - Wenn es fehlt, fügen Sie die obige Zeile innerhalb der `<server>`-Tags hinzu oder stellen Sie sicher, dass keine überschreibende Konfiguration `dropins` deaktiviert.
  - Starten Sie den Server nach Änderungen neu:
    ```bash
    /opt/ibm/wlp/bin/server stop myServer
    /opt/ibm/wlp/bin/server start myServer
    ```

#### 4. **Stellen Sie sicher, dass die erforderlichen Funktionen aktiviert sind**
WLP benötigt spezifische Funktionen, um eine Spring Boot WAR-Datei bereitzustellen, wie z. B. Servlet-Unterstützung.

- **`server.xml` überprüfen:**
  - Stellen Sie sicher, dass der `featureManager`-Bereich enthält:
    ```xml
    <featureManager>
        <feature>javaee-8.0</feature>
    </featureManager>
    ```
    Die Funktion `javaee-8.0` enthält Servlet 4.0, das mit Spring Boot kompatibel ist. Alternativ sollte mindestens `servlet-4.0` vorhanden sein.

- **Was zu tun ist:**
  - Wenn es fehlt, fügen Sie die Funktion hinzu und starten Sie den Server neu.

#### 5. **Überprüfen Sie die Struktur der WAR-Datei**
Eine beschädigte oder falsch strukturierte WAR-Datei könnte die Bereitstellung verhindern.

- **WAR-Datei inspizieren:**
  - Entpacken Sie die WAR-Datei, um deren Inhalte zu überprüfen:
    ```bash
    unzip -l myapp.war
    ```
  - Suchen Sie nach:
    - `WEB-INF/classes/com/example/demo/HelloController.class` (Ihre Controller-Klasse).
    - `WEB-INF/lib/` mit Spring Boot-Abhängigkeiten (z. B. `spring-web-x.x.x.jar`).

- **Was zu tun ist:**
  - Wenn die Struktur falsch ist, erstellen Sie die WAR-Datei neu:
    ```bash
    mvn clean package
    ```
    Stellen Sie sicher, dass Ihr `pom.xml` `<packaging>war</packaging>` setzt und `spring-boot-starter-tomcat` als `<scope>provided</scope>` markiert.

#### 6. **Alternative Bereitstellung über das `apps`-Verzeichnis**
Wenn `dropins` fehlschlägt, versuchen Sie, die Anwendung explizit über das `apps`-Verzeichnis bereitzustellen.

- **Schritte:**
  - Verschieben Sie die WAR-Datei:
    ```bash
    mv /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war /opt/ibm/wlp/usr/servers/myServer/apps/
    ```
  - Bearbeiten Sie `server.xml`, um hinzuzufügen:
    ```xml
    <application id="myapp" name="myapp" type="war" location="${server.config.dir}/apps/myapp.war">
        <context-root>/myapp</context-root>
    </application>
    ```
  - Starten Sie den Server neu:
    ```bash
    /opt/ibm/wlp/bin/server restart myServer
    ```

- **Erneut testen:**
  - Greifen Sie auf `http://localhost:9080/myapp/` zu. Wenn es funktioniert, lag das Problem bei `dropins`.

#### 7. **Überprüfen Sie den Serverstatus**
Stellen Sie sicher, dass der Server korrekt läuft.

- **Status überprüfen:**
  ```bash
  /opt/ibm/wlp/bin/server status myServer
  ```
  - Wenn gestoppt, starten Sie ihn:
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **WLP selbst testen:**
  - Besuchen Sie `http://localhost:9080/`. Wenn WLP läuft, sehen Sie eine Willkommensseite (es sei denn, sie wurde überschrieben). Wenn dies fehlschlägt, gibt es ein breiteres Serverproblem.

---

### Lösung
Um den "context root not found"-Fehler zu beheben:

1. **Hier beginnen:**
   - Überprüfen Sie die Serverprotokolle (`messages.log` oder `console.log`) auf Bereitstellungsnachrichten oder Fehler.
   - Stellen Sie sicher, dass `myapp.war` sich im `dropins`-Verzeichnis mit den richtigen Berechtigungen befindet.

2. **Nächste Schritte:**
   - Überprüfen Sie, dass `server.xml` die Funktion `javaee-8.0` aktiviert und `dropins` überwacht.
   - Wenn nicht aufgelöst, stellen Sie über das `apps`-Verzeichnis mit einer expliziten `<application>`-Konfiguration in `server.xml` bereit.

3. **Endgültige Überprüfung:**
   - Nach dem Vornehmen von Änderungen starten Sie WLP neu und greifen auf `http://localhost:9080/myapp/` zu. Sie sollten "Hello World!" sehen, wenn die Bereitstellung erfolgreich war.

Durch das Befolgen dieser Schritte identifizieren Sie, ob das Problem mit der Serverkonfiguration, der Platzierung der WAR-Datei oder der WAR-Datei selbst zusammenhängt, und beheben es entsprechend.