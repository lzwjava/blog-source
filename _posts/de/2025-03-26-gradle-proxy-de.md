---
audio: false
generated: true
lang: de
layout: post
title: Konfigurieren eines Proxy für Gradle in VSCode
translated: true
type: note
---

Um einen Proxy für Gradle in Visual Studio Code (VSCode) zu konfigurieren, damit es Abhängigkeiten über einen Proxy herunterladen kann, müssen Sie die Proxy-Einstellungen in der Konfiguration von Gradle vornehmen. Gradle verwendet eine Properties-Datei, um solche Einstellungen zu verwalten, und VSCode verlässt sich für Gradle-Projekte auf das Build-System von Gradle. So können Sie vorgehen:

### Schritte zum Konfigurieren des Proxys für Gradle in VSCode

1. **Die Gradle-Properties-Datei finden oder erstellen**
   - Gradle verwendet eine Datei namens `gradle.properties`, um globale Konfigurationseinstellungen zu speichern.
   - Diese Datei befindet sich typischerweise im Gradle-Benutzerheimverzeichnis:
     - Unter Windows: `C:\Users\<IhrBenutzername>\.gradle\gradle.properties`
     - Unter macOS/Linux: `~/.gradle/gradle.properties`
   - Wenn die Datei nicht existiert, erstellen Sie sie an obigem Ort.

2. **Proxy-Einstellungen zur `gradle.properties` hinzufügen**
   - Öffnen Sie die `gradle.properties`-Datei in einem Texteditor.
   - Fügen Sie die folgenden Zeilen hinzu und ersetzen Sie die Platzhalter (`<proxyHost>`, `<proxyPort>`, `<username>`, `<password>`) durch Ihre tatsächlichen Proxy-Daten:
     ```
     systemProp.http.proxyHost=<proxyHost>
     systemProp.http.proxyPort=<proxyPort>
     systemProp.http.proxyUser=<username>
     systemProp.http.proxyPassword=<password>
     systemProp.https.proxyHost=<proxyHost>
     systemProp.https.proxyPort=<proxyPort>
     systemProp.https.proxyUser=<username>
     systemProp.https.proxyPassword=<password>
     ```
   - Beispiel mit echten Werten:
     ```
     systemProp.http.proxyHost=proxy.example.com
     systemProp.http.proxyPort=8080
     systemProp.http.proxyUser=myuser
     systemProp.http.proxyPassword=mypassword
     systemProp.https.proxyHost=proxy.example.com
     systemProp.https.proxyPort=8080
     systemProp.https.proxyUser=myuser
     systemProp.https.proxyPassword=mypassword
     ```
   - Wenn Ihr Proxy keine Authentifizierung (Benutzername/Passwort) erfordert, können Sie die Zeilen `proxyUser` und `proxyPassword` weglassen.

3. **Optional: Proxy pro Projekt konfigurieren**
   - Wenn Sie möchten, dass die Proxy-Einstellungen nur für ein bestimmtes Projekt gelten (anstatt global), können Sie die `gradle.properties`-Datei mit demselben Inhalt wie oben in das Stammverzeichnis Ihres Projekts hinzufügen (z.B. `<projekt-stammverzeichnis>/gradle.properties`).

4. **Überprüfen, ob Gradle den Proxy verwendet**
   - Öffnen Sie Ihr Gradle-Projekt in VSCode.
   - Führen Sie eine Build-Aufgabe aus (z.B. `gradle build`) über das VSCode-Terminal oder die Gradle-Erweiterung.
   - Gradle sollte nun seine Downloads (wie Abhängigkeiten von der offiziellen Website) über den angegebenen Proxy routen.

5. **VSCode-spezifische Hinweise**
   - Stellen Sie sicher, dass die **Java Extension Pack** und **Gradle for Java** Erweiterungen in VSCode installiert sind, da sie die Gradle-Projektunterstützung verbessern.
   - Wenn VSCode immer noch Probleme hat, prüfen Sie, ob Ihre Java-Laufzeitumgebung (die von Gradle verwendet wird) den Proxy ebenfalls berücksichtigt. Möglicherweise müssen Sie JVM-Proxy-Argumente setzen:
     - Gehen Sie in VSCode zu `Datei > Einstellungen > Einstellungen`.
     - Suchen Sie nach `java.gradle.build.jvmArguments`.
     - Fügen Sie etwas hinzu wie:
       ```
       -Dhttp.proxyHost=<proxyHost> -Dhttp.proxyPort=<proxyPort> -Dhttps.proxyHost=<proxyHost> -Dhttps.proxyPort=<proxyPort>
       ```

6. **Die Konfiguration testen**
   - Laden Sie Ihr Projekt in VSCode neu (z.B. schließen und wieder öffnen oder verwenden Sie die "Aktualisieren"-Schaltfläche in der Gradle-Seitenleiste).
   - Führen Sie eine Gradle-Aufgabe aus (z.B. `gradle build` oder `gradle dependencies`), um zu bestätigen, dass Dateien über den Proxy heruntergeladen werden.

### Fehlerbehebung
- **Proxy-Daten prüfen**: Stellen Sie sicher, dass Ihr Proxy-Host, Port und Ihre Anmeldedaten korrekt sind.
- **Firewall oder Netzwerk**: Wenn es weiterhin fehlschlägt, blockiert Ihr Proxy oder Ihr Netzwerk möglicherweise bestimmte Gradle-URLs (z.B. `https://services.gradle.org`). Testen Sie mit einem Befehl wie `curl` oder wenden Sie sich an Ihren Netzwerkadministrator.
- **Ausführliche Ausgabe**: Führen Sie Gradle mit `--debug` oder `--info` aus (z.B. `gradle build --debug`) im VSCode-Terminal, um detaillierte Protokolle zu Netzwerkanfragen zu sehen.

Dieses Setup sollte es Gradle in VSCode ermöglichen, Abhängigkeiten erfolgreich über Ihren Proxy herunterzuladen. Lassen Sie es mich wissen, wenn Sie auf Probleme stoßen!