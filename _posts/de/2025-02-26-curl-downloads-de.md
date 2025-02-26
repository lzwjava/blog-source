---
audio: false
lang: de
layout: post
title: Fehlerbehebung bei curl-Downloads
translated: true
---

Wenn Sie versuchen, eine Eclipse ZIP-Datei von eclipse.org mit `curl -O` herunterzuladen, könnten Sie auf ein Problem stoßen, bei dem eine HTML-Datei anstelle der gewünschten ZIP-Datei heruntergeladen wird, begleitet von einem "301 Moved Permanently" Fehler. Dies geschieht, weil die von Ihnen verwendete URL zu einer anderen Stelle weitergeleitet wird und `curl` diese Weiterleitung nicht automatisch verfolgt, um zur eigentlichen Datei zu gelangen. Hier ist, wie Sie das Problem beheben können:

### Verständnis des Problems

- **301 Moved Permanently**: Dieser HTTP-Statuscode bedeutet, dass die Ressource (die ZIP-Datei) dauerhaft zu einer neuen URL verschoben wurde. Server verwenden oft Weiterleitungen für Download-Links, um auf Spiegel-Sites oder aktualisierte Standorte zu verweisen.
- **Verhalten von `curl -O`**: Die Option `-O` weist `curl` an, den heruntergeladenen Inhalt in einer Datei zu speichern, die nach der entfernten Datei benannt ist. Ohne explizite Behandlung von Weiterleitungen speichert `curl` jedoch möglicherweise den Inhalt der Zwischenantwort der Weiterleitung (oft eine HTML-Seite) anstelle der Verfolgung zur ZIP-Datei.

### Lösung

Um sicherzustellen, dass `curl` der Weiterleitung folgt und die Eclipse ZIP-Datei herunterlädt, verwenden Sie die Option `-L` zusammen mit `-O`. Die `-L`-Flagge weist `curl` an, jeder Weiterleitung zu folgen, bis sie das endgültige Ziel erreicht.

#### Befehl

```bash
curl -L -O <URL>
```

- **`-L`**: Folgt Weiterleitungen, wie die 301-Weiterleitung, zur neuen Stelle.
- **`-O`**: Speichert die Datei mit dem ursprünglichen Namen aus der endgültigen URL.
- **`<URL>`**: Ersetzen Sie dies durch die spezifische Eclipse-Download-URL, z.B. `https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip`.

### Schritt-für-Schritt-Anweisungen

1. **Finden Sie die richtige URL**:
   - Besuchen Sie die Eclipse-Website (z.B. `https://www.eclipse.org/downloads/`).
   - Wählen Sie das gewünschte Paket (z.B. Eclipse IDE für Java-Entwickler).
   - Klicken Sie mit der rechten Maustaste auf den Download-Link oder die Schaltfläche und kopieren Sie die URL. Alternativ können Sie die Entwicklertools Ihres Browsers (F12, Netzwerk-Tab) verwenden, um die genaue URL zu erfassen, wenn Sie auf Download klicken.

2. **Führen Sie den Befehl aus**:
   - Öffnen Sie Ihr Terminal.
   - Führen Sie den `curl`-Befehl mit den Optionen `-L` und `-O` aus, wobei Sie die kopierte URL verwenden:
     ```bash
     curl -L -O https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
     ```
   - Dies sollte die ZIP-Datei (z.B. `eclipse-java-2023-03-R-win32-x86_64.zip`) in Ihr aktuelles Verzeichnis herunterladen.

### Fehlerbehebung

Wenn Sie weiterhin Probleme haben, versuchen Sie diese zusätzlichen Schritte:

- **Überprüfen Sie Weiterleitungen mit detaillierter Ausgabe**:
  - Verwenden Sie die `-v`-Option, um detaillierte Informationen über die Anfrage und Weiterleitungen zu sehen:
    ```bash
    curl -v -L -O <URL>
    ```
  - Sehen Sie sich den `Location`-Header in der 301-Antwort an, um zu sehen, wohin es weitergeleitet wird. Wenn es auf eine HTML-Seite anstelle einer ZIP-Datei verweist, ist die URL möglicherweise kein direkter Download-Link.

- **Überprüfen Sie die URL**:
  - Eclipse verwendet oft ein `download.php`-Skript, das möglicherweise zu einem Spiegel weiterleitet. Stellen Sie sicher, dass Ihre URL entweder der direkte Link zur ZIP-Datei oder ein weiterleitender Link ist, der zur Datei aufgelöst wird. Zum Beispiel könnte ein direkter Spiegel-Link so aussehen:
    ```bash
    curl -L -O https://mirror.its.dal.ca/eclipse/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
    ```

- **Setzen Sie einen User-Agent-Header**:
  - Einige Server verhalten sich je nach Client unterschiedlich. Wenn der Server HTML zurückgibt, weil er `curl` erkennt, ahmen Sie einen Browser nach, indem Sie einen User-Agent hinzufügen:
    ```bash
    curl -L -O -A "Mozilla/5.0" <URL>
    ```

### Warum das funktioniert

Die Eclipse-Website kann Download-Anfragen zu einem Spiegel oder einer aktualisierten URL weiterleiten. Ohne `-L` speichert `curl -O` die Weiterleitungsantwort (eine HTML-Seite) anstelle der Verfolgung zur eigentlichen ZIP-Datei. Durch Hinzufügen von `-L` stellt `curl` sicher, dass es der 301-Weiterleitung zur eigentlichen ZIP-Datei folgt, wodurch das Problem behoben wird.

Durch die Befolgung dieser Schritte sollten Sie die Eclipse ZIP-Datei von eclipse.org erfolgreich mit `curl` herunterladen können.