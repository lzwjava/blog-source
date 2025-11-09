---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Verhalten der JaCoCo-Laufzeitausführungsdatei
translated: true
type: note
---

Wenn Sie **WebSphere Liberty Profile** mit dem **JaCoCo Agent** im `exec`-Modus ausführen, ändert der JaCoCo Agent die ursprüngliche `.exec`-Datei **nicht** während der Laufzeit. Hier ist was passiert:

---

### Wie JaCoCo im `exec`-Modus funktioniert
- **Zweck**: Der JaCoCo Agent sammelt **Code-Coverage-Daten**, während Ihre Anwendung läuft.
- **Ausgabe**: Er schreibt die Coverage-Daten in die `.exec`-Datei (z.B. `jacoco.exec`).
- **Dateiverhalten**:
  - Wenn die Datei **nicht existiert**, erstellt JaCoCo sie.
  - Wenn die Datei **bereits existiert**, **hängt** JaCoCo neue Coverage-Daten an (überschreibt oder ändert vorhandene Daten nicht, es sei denn, Sie setzen die Datei explizit zurück oder führen sie zusammen).
  - Die ursprüngliche `.exec`-Datei wird **nicht so verändert**, dass ihre Struktur beschädigt oder geändert wird – sie wächst nur durch neue Daten.

---

### Wird die `.exec`-Datei verändert?
- **Ja, aber nur durch Anhängen von Daten**: Die Datei wird bei jedem Ausführen Ihrer Anwendung mit dem JaCoCo Agent mit neuen Coverage-Informationen aktualisiert.
- **Keine strukturellen Änderungen**: Das Format der `.exec`-Datei bleibt gleich; es handelt sich um eine Binärdatei, die Coverage-Daten enthält.

---

### Best Practices
- **Zusammenführen oder Zurücksetzen**: Wenn Sie neu beginnen möchten, löschen oder benennen Sie die `.exec`-Datei um, bevor Sie Ihre Anwendung erneut ausführen.
- **Mehrere Läufe zusammenführen**: Verwenden Sie das `jacoco:merge`-Goal (in Maven) oder die `org.jacoco.agent.rt.RT`-Klasse, um mehrere `.exec`-Dateien bei Bedarf zusammenzuführen.

---

### Beispiel Liberty Konfiguration
In Ihrer `server.env` oder `jvm.options` für Liberty könnte stehen:
```bash
-javaagent:/pfad/zu/jacocoagent.jar=destfile=/pfad/zu/jacoco.exec,append=true
```
- `append=true` stellt sicher, dass neue Daten an die bestehende Datei angehängt werden.

---