---
audio: false
generated: true
lang: de
layout: post
title: Java wie Python-Skripte ausführen
translated: true
type: note
---

Um die `MultiMark.java`-Datei direkt auszuführen, ähnlich wie ein Python-Skript, haben Sie mehrere Möglichkeiten. Da Sie sich auf einem Unix-ähnlichen System befinden (erkennbar am Pfad `~/projects` und dem `ls`-Befehl), zeige ich Ihnen Schritte, um die Ausführung des Java-Programms so nahtlos wie möglich zu gestalten. Hier sind zwei Hauptansätze:

---

### **Option 1: `MultiMark.java` direkt mit dem `java`-Befehl ausführen (Java 11+)**
Seit Java 11 können Sie eine einzelne Java-Quelldatei direkt ausführen, ohne sie explizit zu kompilieren. Das fühlt sich ähnlich an wie das Ausführen eines Python-Skripts.

1. **Stellen Sie sicher, dass Java installiert ist**
   Prüfen Sie, ob Java 11 oder höher installiert ist:
   ```bash
   java --version
   ```
   Falls Java nicht installiert ist oder eine ältere Version vorliegt, installieren Sie eine kompatible Version (z.B. OpenJDK):
   ```bash
   sudo apt update
   sudo apt install openjdk-17-jdk
   ```

2. **Die Java-Datei direkt ausführen**
   Wechseln Sie in das Verzeichnis mit `MultiMark.java`:
   ```bash
   cd ~/projects/lzwjava.github.io/scripts/benchmark
   ```
   Führen Sie die Java-Datei direkt mit folgendem Befehl aus:
   ```bash
   java MultiMark.java
   ```
   Dieser Befehl kompiliert und führt die `MultiMark.java`-Datei in einem Schritt aus. Die Ausgabe (z.B. CPU-Kerne, Thread-Anzahl und Zeiten) erscheint im Terminal.

---

### **Option 2: Ein Shell-Skript für mehr Komfort erstellen**
Um die Ausführung von `MultiMark.java` noch mehr wie ein Python-Skript zu gestalten (z.B. `./multimark`), können Sie ein Shell-Skript als Wrapper erstellen.

1. **Erstellen Sie ein Shell-Skript**
   Erstellen Sie eine Datei namens `multimark` (ohne Erweiterung) im Verzeichnis `scripts/benchmark`:
   ```bash
   nano ~/projects/lzwjava.github.io/scripts/benchmark/multimark
   ```
   Fügen Sie den folgenden Inhalt ein:
   ```bash
   #!/bin/bash
   java MultiMark.java
   ```
   Speichern Sie und beenden Sie den Editor (`Ctrl+O`, `Enter`, `Ctrl+X` in nano).

2. **Machen Sie das Skript ausführbar**
   Setzen Sie die Ausführungsberechtigungen:
   ```bash
   chmod +x multimark
   ```

3. **Führen Sie das Skript aus**
   Jetzt können Sie das Programm wie ein Python-Skript ausführen:
   ```bash
   ./multimark
   ```
   Dies führt im Hintergrund `java MultiMark.java` aus.

---

### **Option 3: Getrennt kompilieren und ausführen (Traditioneller Ansatz)**
Wenn Sie die Java-Datei explizit kompilieren möchten oder müssen (z.B. für ältere Java-Versionen oder zur Überprüfung von Kompilierungsfehlern), befolgen Sie diese Schritte:

1. **Kompilieren Sie die Java-Datei**
   Wechseln Sie in das Verzeichnis:
   ```bash
   cd ~/projects/lzwjava.github.io/scripts/benchmark
   ```
   Kompilieren Sie die Java-Quelldatei:
   ```bash
   javac MultiMark.java
   ```
   Dies erzeugt eine `MultiMark.class`-Datei.

2. **Führen Sie das kompilierte Programm aus**
   Führen Sie die kompilierte Klasse aus:
   ```bash
   java MultiMark
   ```
   Hinweis: Verwenden Sie `MultiMark` (ohne `.java`), da Sie die kompilierte Klassendatei ausführen.

---

### **Python-ähnliche Ausführung erzielen**
Um die Erfahrung so nah wie möglich an die Ausführung eines Python-Skripts heranzuführen, ist **Option 1** (direkt `java MultiMark.java`) die einfachste, da sie die manuelle Kompilierung überspringt. **Option 2** (Shell-Skript) ist ideal, wenn Sie einen einzelnen Befehl wie `./multimark` wünschen, der sich wie `./script.py` anfühlt.

### **Hinweise**
- **Java-Version**: Der Code verwendet Standard-Java-Bibliotheken (`java.util.*` und `System.nanoTime`), daher sollte er mit Java 8 oder höher funktionieren. Die Direktausführung (`java MultiMark.java`) erfordert Java 11+.
- **Performance**: Das `MultiMark.java`-Programm führt Benchmarks für Sortiervorgänge mit mehreren Threads durch. Die Ausführung direkt oder über ein Skript beeinflusst die Performance nicht, stellen Sie jedoch sicher, dass Ihr System über ausreichend Ressourcen (CPU/Speicher) für die getesteten Thread-Anzahlen (bis zu 64 Threads) verfügt.
- **Verzeichniskontext**: Da Sie `ls scripts/benchmark/` gezeigt haben, bin ich davon ausgegangen, dass sich `MultiMark.java` in diesem Verzeichnis befindet. Passen Sie die Pfade an, falls es sich woanders befindet.
- **Fehlerbehandlung**: Falls Sie Fehler erhalten (z.B. `java: command not found`), stellen Sie sicher, dass Java installiert und in Ihrem `PATH` enthalten ist. Wenn das Programm fehlschlägt (z.B. aufgrund von Speicher- oder Thread-Limits), prüfen Sie die Stack-Trace für Details.

Wenn Sie dies in einen Workflow mit Ihren Python-Skripts (`executormark.py`, `multimark.py`, `threadmark.py`) integrieren möchten, lassen Sie es mich wissen. Ich kann dann Vorschläge machen, wie Sie diese kombinieren können (z.B. Aufruf des Java-Programms von Python aus).