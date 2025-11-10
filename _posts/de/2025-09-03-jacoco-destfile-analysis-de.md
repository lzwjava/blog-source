---
audio: false
generated: true
image: false
lang: de
layout: post
title: Verwendung und Analyse der JaCoCo Destfile
translated: true
type: note
---

Gute Frage – lassen Sie uns aufschlüsseln, wie JaCoCos `destfile` funktioniert, wenn Sie eine Java- oder Spring-Boot-Anwendung ausführen.

### 1. Was `destfile` ist

`destfile` ist ein Parameter des JaCoCo Java-Agents (`jacocoagent.jar`), der dem Agenten **mitteilt, wohin er seine Ausführungsdaten schreiben soll**.
Standardmäßig ist es etwas wie `jacoco.exec`, aber Sie können es explizit setzen:

```bash
-javaagent:jacocoagent.jar=destfile=/path/to/jacoco.exec
```

### 2. Was geschrieben wird

Wenn Ihre Spring-Boot-App mit dem angehängten JaCoCo-Agenten läuft, instrumentiert der Agent den Bytecode Ihrer Klassen.
Während der Ausführung zeichnet JaCoCo Abdeckungsinformationen auf, wie zum Beispiel:

* Welche Klassen und Methoden geladen wurden
* Welche Zeilen ausgeführt wurden
* Zweigabdeckung (ob sowohl `if`- als auch `else`-Pfade ausgeführt wurden, etc.)

Diese Laufzeit-Abdeckungsdaten werden im Speicher gespeichert und periodisch in die durch `destfile` definierte Datei geschrieben.

Also ja – die JVM schreibt über den JaCoCo-Agenten Funktions- und Zeilenausführungsinformationen in diese Datei.

### 3. Wie die Analyse funktioniert

Die `.exec`-Datei selbst ist **nicht menschenlesbar**. Es sind nur binäre Abdeckungsdaten.
Nachdem Ihre App beendet ist, führen Sie typischerweise einen Berichtstask aus (z.B. Maven `jacoco:report` oder Gradles `jacocoTestReport`), der:

* Die `destfile`-Daten liest
* Ihre kompilierten `.class`-Dateien und den Quellcode liest
* Einen HTML-, XML- oder CSV-Abdeckungsbericht generiert

In diesem Schritt sehen Sie dann Prozentsätze, farblich markierte Codezeilen, etc.

### 4. Laufzeit vs. Berichtszeit

* **Laufzeit:** Der Agent zeichnet die Ausführung im Speicher auf und schreibt sie in die `destfile`.
* **Berichtszeit:** Sie verwenden JaCoCo-Tools (Maven, Gradle, CLI oder Ant), um diese `.exec`-Datei zu interpretieren und lesbare Berichte zu generieren.

Die `destfile` selbst ist also **nur die rohe Ausführungsdaten** – sie wird erst analysiert, wenn Sie den Berichtsschritt ausführen.

---

👉 Kurz gesagt: Ja, wenn Ihre Spring-Boot-App mit dem JaCoCo-Agenten läuft, werden Abdeckungsinformationen über Methoden und Zeilen in der `destfile` gespeichert. Später verwenden die JaCoCo-Berichtstools diese (zusammen mit Klassen-/Quelldateien), um benutzerfreundliche Berichte zu erstellen.

Möchten Sie, dass ich Ihnen auch zeige, wie das Schritt-für-Schritt mit Spring Boot funktioniert (z.B. Maven-Konfiguration + Ausführung + Berichtsgenerierung)?