---
audio: false
generated: true
lang: de
layout: post
title: Beheben Sie Java Classpath-Fehler
translated: true
type: note
---

Der Fehler, den Sie erhalten haben (`Could not find or load main class scripts.benchmark.MultiMark`), tritt auf, weil Sie versucht haben, das Java-Programm aus dem Projekt-Stammverzeichnis (`~/projects/lzwjava.github.io`) mit dem vollständig qualifizierten Klassennamen (`scripts.benchmark.MultiMark`) auszuführen. Die Java-Laufzeitumgebung erwartet jedoch, dass die Klasse aus dem Verzeichnis ausgeführt wird, in dem die Paketstruktur beginnt, oder Sie müssen den Classpath korrekt angeben. Als Sie in das Verzeichnis `scripts/benchmark` gewechselt sind und `java MultiMark` ausgeführt haben, hat es funktioniert, weil sich die Klasse relativ zum Befehl im korrekten Verzeichnis befand.

Um `MultiMark.java` oder `MultiMark.class` aus dem Projekt-Stammverzeichnis (`~/projects/lzwjava.github.io`) auszuführen, ohne das Verzeichnis zu wechseln, können Sie die Option `-cp` (Classpath) mit dem `java`-Befehl verwenden, um Java mitzuteilen, wo die kompilierte Klassendatei zu finden ist. Hier sind zwei Möglichkeiten, dies zu erreichen, während Sie im Stammverzeichnis bleiben:

---

### **Option 1: Die kompilierte Klasse mit Classpath ausführen**
Falls `MultiMark.class` bereits in `scripts/benchmark/` existiert (wie in Ihrer `ls`-Ausgabe gezeigt), können Sie sie aus dem Stammverzeichnis ausführen, indem Sie den Classpath angeben.

1. **Im Stammverzeichnis bleiben**
   Stellen Sie sicher, dass Sie sich in `~/projects/lzwjava.github.io` befinden.

2. **Das Programm ausführen**
   Verwenden Sie die `-cp`-Option, um auf das Verzeichnis mit der Klassendatei zu verweisen:
   ```bash
   java -cp scripts/benchmark MultiMark
   ```
   - `-cp scripts/benchmark` weist Java an, im Verzeichnis `scripts/benchmark` nach Klassen zu suchen.
   - `MultiMark` ist der Klassenname (ohne `.class` oder Paketpräfix, da `MultiMark.java` keine `package`-Anweisung hat).

   Dies sollte eine Ausgabe wie folgt produzieren:
   ```
   CPU cores: 32
   ...
   ```

3. **Hinweis**: Falls `MultiMark.class` veraltet oder nicht vorhanden ist, kompilieren Sie die Quelldatei zuerst aus dem Stammverzeichnis:
   ```bash
   javac scripts/benchmark/MultiMark.java
   ```
   Führen Sie dann den obigen Befehl aus.

---

### **Option 2: Die Quelldatei direkt mit Classpath ausführen (Java 11+)**
Wenn Sie die Quelldatei lieber direkt ausführen möchten (ähnlich wie `python script.py`), können Sie den `java`-Befehl mit dem Pfad zur Quelldatei verwenden und dabei den Classpath angeben.

1. **Im Stammverzeichnis bleiben**
   Stellen Sie sicher, dass Sie sich in `~/projects/lzwjava.github.io` befinden.

2. **Die Quelldatei ausführen**
   Verwenden Sie:
   ```bash
   java -cp scripts/benchmark scripts/benchmark/MultiMark.java
   ```
   - `-cp scripts/benchmark` setzt den Classpath auf das Verzeichnis, das die Quelle enthält.
   - `scripts/benchmark/MultiMark.java` spezifiziert die zu kompilierende und auszuführende Quelldatei.

   Dies kompiliert und führt `MultiMark.java` in einem Schritt aus und erzeugt die gleiche Ausgabe wie zuvor.

---

### **Option 3: Ein Shell-Skript im Stammverzeichnis erstellen**
Um es noch bequemer zu machen (wie das Ausführen von `./multimark` aus dem Stammverzeichnis), können Sie ein Shell-Skript im Stammverzeichnis (`~/projects/lzwjava.github.io`) erstellen.

1. **Ein Shell-Skript erstellen**
   Erstellen Sie eine Datei namens `multimark` im Stammverzeichnis:
   ```bash
   nano multimark
   ```
   Fügen Sie Folgendes hinzu:
   ```bash
   #!/bin/bash
   java -cp scripts/benchmark MultiMark
   ```
   Speichern Sie und beenden Sie.

2. **Ausführbar machen**
   ```bash
   chmod +x multimark
   ```

3. **Das Skript ausführen**
   Aus dem Stammverzeichnis:
   ```bash
   ./multimark
   ```
   Dies führt das Java-Programm aus, ohne dass Sie das Verzeichnis wechseln müssen.

4. **Optional: Kompilierung im Skript**
   Wenn Sie möchten, dass das Skript die Kompilierung übernimmt (z.B. falls sich die Quelldatei ändert), modifizieren Sie das Skript:
   ```bash
   #!/bin/bash
   javac scripts/benchmark/MultiMark.java
   java -cp scripts/benchmark MultiMark
   ```

---

### **Wichtige Hinweise**
- **Classpath (`-cp`)**: Die `-cp`-Option teilt Java mit, wo es Klassen oder Quelldateien finden soll. Da `MultiMark.java` keine `package`-Anweisung hat, ist der Klassenname einfach `MultiMark`, nicht `scripts.benchmark.MultiMark`. Wenn sie eine Zeile `package scripts.benchmark;` hätte, müssten Sie `java -cp . scripts.benchmark.MultiMark` aus dem Stammverzeichnis verwenden.
- **Java-Version**: Die Ausführung von Quelldateien (`java scripts/benchmark/MultiMark.java`) erfordert Java 11 oder höher. Ihr System scheint Java installiert zu haben, da es aus dem `scripts/benchmark`-Verzeichnis funktioniert hat.
- **Verzeichnis**: Diese Lösungen lassen Sie im Stammverzeichnis (`~/projects/lzwjava.github.io`) bleiben, entsprechend Ihrer Präferenz.
- **Automatisierung**: Das Shell-Skript (Option 3) kommt einer Python-ähnlichen Erfahrung am nächsten, da Sie `./multimark` wie ein Python-Skript ausführen können. Sie könnten es auch zu Ihrem `PATH` hinzufügen für globalen Zugriff, aber das ist optional.
- **Fehlerbehandlung**: Wenn Sie Fehler wie `NoClassDefFoundError` erhalten, stellen Sie sicher, dass `MultiMark.class` in `scripts/benchmark/` existiert, oder kompilieren Sie neu. Falls Java nicht gefunden wird, überprüfen Sie die Installation (`java --version`).

Wenn Sie dies in Ihre Python-Skripte integrieren möchten oder einen spezifischen Workflow benötigen (z.B. das gemeinsame Ausführen von `multimark.py` und `MultiMark.java`), lassen Sie es mich wissen!