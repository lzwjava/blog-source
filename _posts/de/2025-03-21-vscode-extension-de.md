---
audio: false
generated: true
lang: de
layout: post
title: Fehlerbehebung bei der VSCode-Erweiterungsinstallation mit Proxyproblemen
translated: true
type: note
---

Um das Installationsprotokoll für Erweiterungen in Visual Studio Code (VSCode) zu überprüfen oder eine Erweiterung über die Befehlszeile mit `code --install-extension` zu installieren und das Protokoll einzusehen – insbesondere, wenn Sie einen Proxy-Probleme vermuten – gehen Sie wie folgt vor:

---

### Verwendung der Befehlszeile mit `code --install-extension`
Sie können Erweiterungen über die Befehlszeile installieren und erhalten dabei Einblicke in den Prozess, was bei der Diagnose von Proxy-Problemen helfen kann.

1. **Installation mit ausführlicher Ausgabe**  
   Führen Sie den folgenden Befehl aus, um eine Erweiterung zu installieren und eine detailliertere Ausgabe zu sehen:
   ```bash
   code --install-extension <extension-id> --verbose
   ```
   - Ersetzen Sie `<extension-id>` durch die ID der Erweiterung (z. B. `vscodevim.vim`).
   - Das Flag `--verbose` erhöht den Detaillierungsgrad der Ausgabe und zeigt Fortschritt und potenzielle Fehler, wie Proxy- oder Netzwerkprobleme, an.

2. **Behandlung von Proxy-Problemen**  
   Wenn Sie sich hinter einem Proxy befinden, könnte dies die Installation beeinträchtigen. Versuchen Sie folgende Ansätze:
   - **Proxy-Umgebungsvariablen setzen**:  
     Konfigurieren Sie die Proxy-Einstellungen, bevor Sie den Befehl ausführen:
     ```bash
     export HTTP_PROXY=http://ihr-proxy-server:port
     export HTTPS_PROXY=http://ihr-proxy-server:port
     code --install-extension <extension-id>
     ```
     - Unter Windows verwenden Sie `set` anstelle von `export`:
       ```cmd
       set HTTP_PROXY=http://ihr-proxy-server:port
       set HTTPS_PROXY=http://ihr-proxy-server:port
       code --install-extension <extension-id>
       ```
   - **Proxy direkt angeben**:  
     Verwenden Sie das Flag `--proxy-server`:
     ```bash
     code --install-extension <extension-id> --proxy-server=http://ihr-proxy-server:port
     ```

3. **Überprüfen der Ausgabe**  
   - Die Konsolenausgabe mit dem `--verbose`-Flag zeigt den Installationsfortschritt und eventuelle Fehler an (z. B. Verbindungstimeouts oder Proxy-Authentifizierungsfehler).
   - Hinweis: Die Befehlszeilenschnittstelle (`code`) bietet im Vergleich zur VSCode-GUI nur eingeschränkte Proxy-Unterstützung, daher sind die Protokolle möglicherweise nicht so detailliert wie erwartet.

---

### Überprüfen der Protokolle in VSCode
Für detailliertere Protokolle – insbesondere nach einem Installationsversuch – verwenden Sie die integrierten Protokollfunktionen von VSCode:

1. **Öffnen des Protokollordners**  
   - Öffnen Sie VSCode und rufen Sie die Befehlspalette auf:
     - Drücken Sie `Strg+Umschalt+P` (oder `Cmd+Umschalt+P` auf macOS).
     - Tippen Sie **Developer: Open Logs Folder** ein und wählen Sie es aus.
   - Dies öffnet einen Ordner mit verschiedenen Protokolldateien. Suchen Sie nach:
     - **`exthost.log`**: Protokolle im Zusammenhang mit Extension Host-Prozessen, einschließlich Installationsversuchen.
     - **`sharedprocess.log`**: Protokolle für gemeinsame Prozesse, die erweiterungsbezogene Ereignisse enthalten können.
   - Öffnen Sie diese Dateien in einem Texteditor und suchen Sie nach Fehlern, die die Erweiterungs-ID, Netzwerkprobleme oder Proxy-Probleme erwähnen.

2. **Anzeige des Ausgabebereichs**  
   - Gehen Sie in VSCode zu `Ansicht > Ausgabe`, um den **Ausgabe**-Bereich zu öffnen.
   - Wählen Sie im Dropdown-Menü auf der rechten Seite **Extensions** aus.
   - Dies zeigt Echtzeitprotokolle für Erweiterungsaktivitäten an, wenn die Installation über die VSCode-Oberfläche erfolgt (nicht direkt über die CLI). Wenn Sie die Installation über die VSCode-Benutzeroberfläche wiederholen, sehen Sie hier möglicherweise Proxy-bezogene Fehler.

---

### Zusätzliche Schritte zur Proxy-Fehlerbehebung
Da Sie ein Proxy-Problem vermuten, hier zusätzliche Tipps zur Sicherstellung einer korrekten Konfiguration:

- **Proxy in VSCode konfigurieren**  
  - Öffnen Sie die VSCode-Einstellungen (`Datei > Einstellungen > Einstellungen` oder `Strg+,`).
  - Suchen Sie nach `proxy` und setzen Sie:
    ```json
    "http.proxy": "http://ihr-proxy-server:port"
    ```
  - Passen Sie optional `"http.proxyStrictSSL"` an (setzen Sie es auf `false`, falls nötig) oder `"http.proxyAuthorization"` (für authentifizierte Proxys) an.
  - Diese Einstellungen gelten für Installationen innerhalb von VSCode, nicht unbedingt für die CLI.

- **Netzwerkzugriff testen**  
  - Testen Sie manuell, ob der Proxy den Zugriff auf den VSCode Marketplace erlaubt:
    - Finden Sie die VSIX-Datei-URL der Erweiterung (z. B. von der Marketplace-Website).
    - Verwenden Sie ein Tool wie `curl`:
      ```bash
      curl -x http://ihr-proxy-server:port <vsix-url>
      ```
    - Wenn dies fehlschlägt, blockiert Ihr Proxy möglicherweise die Verbindung.

---

### Empfohlener Ansatz
- **Für CLI-Installation**: Verwenden Sie `code --install-extension <extension-id> --verbose` mit Proxy-Umgebungsvariablen oder `--proxy-server`, um eine sofortige Ausgabe zu sehen. Überprüfen Sie die Fehler im Terminal.
- **Für detaillierte Protokolle**: Installieren Sie die Erweiterung über die VSCode-Benutzeroberfläche (Marketplace) und überprüfen Sie den Bereich **Ausgabe > Extensions** oder den Protokollordner (`exthost.log`).
- **Proxy-Überprüfung**: Stellen Sie sicher, dass die Proxy-Einstellungen sowohl in Ihrem System als auch in VSCode korrekt sind.

Diese Kombination ermöglicht es Ihnen, den Fortschritt zu überwachen und Proxy-Probleme effektiv zu diagnostizieren. Wenn die CLI-Ausgabe nicht ausreicht, bieten die VSCode-Protokolle einen tieferen Einblick in die Ursache des Problems.