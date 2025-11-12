---
audio: false
generated: true
lang: de
layout: post
title: Fehlerbehebung bei curl-Downloads
translated: true
type: note
---

Wenn Sie versuchen, eine Eclipse-ZIP-Datei von eclipse.org mit `curl -O` herunterzuladen, kann es vorkommen, dass stattdessen eine HTML-Datei mit einem "301 Moved Permanently"-Fehler heruntergeladen wird. Dies passiert, weil die verwendete URL auf einen anderen Ort weiterleitet und `curl` dieser Weiterleitung nicht automatisch zur eigentlichen Datei folgt. So beheben Sie das Problem:

### Problemverständnis

- **301 Moved Permanently**: Dieser HTTP-Statuscode bedeutet, dass die Ressource (die ZIP-Datei) dauerhaft auf eine neue URL umgezogen ist. Server verwenden oft Weiterleitungen für Download-Links, um auf Mirror-Sites oder aktualisierte Orte zu verweisen.
- **`curl -O`-Verhalten**: Die `-O`-Option weist `curl` an, den heruntergeladenen Inhalt unter dem Namen der Remote-Datei zu speichern. Ohne explizite Behandlung von Weiterleitungen speichert `curl` jedoch möglicherweise den Inhalt der Zwischenantwort (oft eine HTML-Seite) anstatt der Weiterleitung zur ZIP-Datei zu folgen.

### Lösung

Um sicherzustellen, dass `curl` der Weiterleitung folgt und die Eclipse-ZIP-Datei herunterlädt, verwenden Sie die `-L`-Option zusammen mit `-O`. Das `-L`-Flag weist `curl` an, allen Weiterleitungen bis zum endgültigen Ziel zu folgen.

#### Befehl

```bash
curl -L -O <URL>
```

- **`-L`**: Folgt Weiterleitungen, wie der 301-Weiterleitung, zum neuen Ort.
- **`-O`**: Speichert die Datei mit dem ursprünglichen Namen aus der finalen URL.
- **`<URL>`**: Ersetzen Sie dies durch die spezifische Eclipse-Download-URL, z.B. `https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip`.

### Schritt-für-Schritt-Anleitung

1. **Korrekte URL finden**:
   - Besuchen Sie die Eclipse-Website (z.B. `https://www.eclipse.org/downloads/`).
   - Wählen Sie das gewünschte Paket aus (z.B. Eclipse IDE for Java Developers).
   - Klicken Sie mit der rechten Maustaste auf den Download-Link oder die Schaltfläche und kopieren Sie die URL. Alternativ können Sie die Entwicklertools Ihres Browsers verwenden (F12, Netzwerk-Tab), um die exakte URL beim Klick auf den Download zu erfassen.

2. **Befehl ausführen**:
   - Öffnen Sie Ihr Terminal.
   - Führen Sie den `curl`-Befehl mit den Optionen `-L` und `-O` unter Verwendung der kopierten URL aus:
     ```bash
     curl -L -O https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
     ```
   - Dies sollte die ZIP-Datei (z.B. `eclipse-java-2023-03-R-win32-x86_64.zip`) in Ihr aktuelles Verzeichnis herunterladen.

### Fehlerbehebung

Wenn weiterhin Probleme auftreten, versuchen Sie diese zusätzlichen Schritte:

- **Weiterleitungen mit ausführlicher Ausgabe prüfen**:
  - Verwenden Sie die `-v`-Option, um detaillierte Informationen zur Anfrage und zu Weiterleitungen zu sehen:
    ```bash
    curl -v -L -O <URL>
    ```
  - Suchen Sie nach dem `Location`-Header in der 301-Antwort, um zu sehen, wohin weitergeleitet wird. Wenn dies auf eine HTML-Seite statt auf eine ZIP-Datei verweist, ist die URL möglicherweise nicht der direkte Download-Link.

- **URL überprüfen**:
  - Eclipse verwendet oft ein `download.php`-Skript, das auf einen Mirror weiterleiten kann. Stellen Sie sicher, dass Ihre URL entweder der direkte Link zur ZIP-Datei ist oder ein Weiterleitungslink, der zur Datei führt. Ein direkter Mirror-Link könnte beispielsweise so aussehen:
    ```bash
    curl -L -O https://mirror.its.dal.ca/eclipse/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
    ```

- **User-Agent-Header setzen**:
  - Einige Server verhalten sich je nach Client unterschiedlich. Wenn der Server HTML zurückgibt, weil er `curl` erkennt, können Sie einen Browser nachahmen, indem Sie einen User-Agent hinzufügen:
    ```bash
    curl -L -O -A "Mozilla/5.0" <URL>
    ```

### Warum das funktioniert

Die Eclipse-Website leitet Download-Anfragen möglicherweise an einen Mirror oder eine aktualisierte URL weiter. Ohne `-L` speichert `curl -O` die Weiterleitungsantwort (eine HTML-Seite) anstatt ihr zu folgen. Durch das Hinzufügen von `-L` stellt man sicher, dass `curl` der 301-Weiterleitung zur eigentlichen ZIP-Datei folgt und das Problem löst.

Wenn Sie diese Schritte befolgen, sollten Sie die Eclipse-ZIP-Datei erfolgreich von eclipse.org mit `curl` herunterladen können.