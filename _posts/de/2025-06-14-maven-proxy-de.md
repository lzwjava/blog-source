---
audio: false
generated: true
lang: de
layout: post
title: Maven-Proxy-Einstellungen
translated: true
type: note
---

Basierend auf der Ausgabe Ihres `checkproxy`-Befehls sind sowohl Ihre HTTP- als auch HTTPS-Proxys auf `http://127.0.0.1:7890` eingestellt. Unten finden Sie den aktualisierten Konfigurationsausschnitt für die Maven-`settings.xml`, um Maven für die Verwendung dieser Proxy-Einstellungen zu konfigurieren.

### Aktualisierter `settings.xml` Proxy-Konfigurationsausschnitt

Fügen Sie den Abschnitt `<proxies>` in Ihrer Maven-`settings.xml`-Datei (befindet sich unter `~/.m2/settings.xml` oder `/usr/share/maven/conf/settings.xml`) hinzu oder aktualisieren Sie ihn wie folgt:

```xml
<settings>
  <proxies>
    <proxy>
      <id>http-proxy</id>
      <active>true</active>
      <protocol>http</protocol>
      <host>127.0.0.1</host>
      <port>7890</port>
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
    <proxy>
      <id>https-proxy</id>
      <active>true</active>
      <protocol>https</protocol>
      <host>127.0.0.1</host>
      <port>7890</port>
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
  </proxies>
</settings>
```

### Erklärung des Ausschnitts
- **`<id>`**: Eindeutige Bezeichner (`http-proxy` und `https-proxy`) für jede Proxy-Konfiguration.
- **`<active>true</active>`**: Aktiviert den Proxy.
- **`<protocol>`**: Auf `http` für den HTTP-Proxy und `https` für den HTTPS-Proxy gesetzt, entsprechend Ihrer `checkproxy`-Ausgabe.
- **`<host>127.0.0.1</host>`**: Die IP-Adresse des Proxy-Servers, wie in Ihren Proxy-Einstellungen angezeigt.
- **`<port>7890</port>`**: Die Portnummer für beide Proxys, wie angegeben.
- **`<nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>`**: Schließt `localhost` und `127.0.0.1` von der Proxy-Nutzung aus, was Standard ist, um Probleme mit lokalen Diensten zu vermeiden.
- **Kein `<username>` oder `<password>`**: Da Ihre Proxy-Ausgabe keine Authentifizierung anzeigt, werden diese Felder weggelassen. Falls Authentifizierung erforderlich ist, fügen Sie sie mit Ihren Anmeldedaten hinzu.

### Schritte zur Anwendung
1. **Öffnen Sie `settings.xml`**:
   - Falls `~/.m2/settings.xml` existiert, bearbeiten Sie diese Datei (z.B. `nano ~/.m2/settings.xml`).
   - Falls sie nicht existiert, erstellen Sie sie oder bearbeiten Sie die globale Datei unter `/usr/share/maven/conf/settings.xml` (erfordert `sudo`).

2. **Fügen Sie den Abschnitt `<proxies>` ein oder aktualisieren Sie ihn**:
   - Falls `<proxies>` bereits existiert, ersetzen oder führen Sie die `<proxy>`-Einträge mit dem obigen Ausschnitt zusammen.
   - Falls `<settings>` leer oder minimal ist, können Sie den gesamten Ausschnitt als Inhalt der Datei verwenden.

3. **Speichern und schließen** Sie die Datei.

### Überprüfen der Konfiguration
Führen Sie einen Maven-Befehl aus, der Internetzugriff erfordert, um zu bestätigen, dass der Proxy verwendet wird:
```bash
cd ~/Projects/blog-server
mvn -X clean checkstyle:check
```

Suchen Sie in der Debug-Ausgabe (`-X`) nach Zeilen, die anzeigen, dass Maven den Proxy verwendet (z.B. Verbindungen zu `127.0.0.1:7890`). Wenn der Befehl Abhängigkeiten herunterlädt oder ohne Netzwerkfehler abgeschlossen wird, funktioniert der Proxy.

### Problembehandlung
- **Proxy funktioniert nicht**:
  - Stellen Sie sicher, dass der Proxy-Server unter `127.0.0.1:7890` läuft (testen Sie z.B. mit `curl -x http://127.0.0.1:7890 https://repo.maven.apache.org`).
  - Überprüfen Sie die `settings.xml`-Datei auf Tippfehler.
- **Einstellungsdatei wird ignoriert**:
  - Bestätigen Sie, dass Maven `~/.m2/settings.xml` liest, indem Sie in der Debug-Ausgabe nach dem Dateipfad suchen.
  - Falls Sie die globale Datei verwenden, stellen Sie sicher, dass Sie `/usr/share/maven/conf/settings.xml` korrekt bearbeitet haben.
- **Authentifizierung erforderlich**:
  - Falls Ihr Proxy einen Benutzernamen und ein Passwort erfordert, fügen Sie jedem `<proxy>`-Block Folgendes hinzu:
    ```xml
    <username>IhrBenutzername</username>
    <password>IhrPasswort</password>
    ```

### Hinweis zum vorherigen Kontext
Ihr `checkstyle:check`-Problem im `blog-server`-Projekt (bezogen auf `checks.xml` und `SuppressWithNearbyTextFilter`) sollte separat gelöst werden, indem Sie die `pom.xml` wie zuvor vorgeschlagen aktualisieren (Verwendung von `maven-checkstyle-plugin:3.3.1` mit Checkstyle `10.17.0` und `<configLocation>${project.basedir}/checks.xml</configLocation>`). Die oben genannten Proxy-Einstellungen stellen sicher, dass Maven alle erforderlichen Artefakte für diese Korrektur herunterladen kann.

Lassen Sie mich wissen, wenn Sie auf Probleme stoßen oder Hilfe mit der aktualisierten `pom.xml` oder weiterer Proxy-Problembehandlung benötigen!