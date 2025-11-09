---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Diagnose von Java Hängern mit jstack
translated: true
type: note
---

### Verwendung von jstack zur Diagnose von Java-Anwendungshängern oder -Stopps

jstack ist ein Befehlszeilentool, das im JDK enthalten ist und Thread-Dumps für eine laufende Java Virtual Machine (JVM) erzeugt. Thread-Dumps erfassen den Zustand aller Threads zu einem bestimmten Zeitpunkt, was entscheidend für die Identifizierung von Ursachen für Hänger ist, wie z.B. Deadlocks, Endlosschleifen, blockierte E/A oder CPU-intensive Operationen. Es ist besonders nützlich auf Linux/Unix-Systemen oder in plattformübergreifenden Umgebungen.

#### Schritte zur Verwendung von jstack:
1. **Identifizieren der Java-Prozess-ID (PID):**
   - Führen Sie `jps` (ebenfalls Teil des JDK) aus, um alle Java-Prozesse aufzulisten:  
     ```
     jps -l
     ```
     Dies gibt etwas wie `12345 MyApp.jar` aus. Notieren Sie die PID (z.B. 12345).

   - Alternativ können Sie Betriebssystembefehle wie `ps aux | grep java` unter Linux/macOS verwenden.

2. **Erzeugen eines Thread-Dumps:**
   - Führen Sie jstack mit der PID aus, um den Dump in eine Datei zu schreiben:  
     ```
     jstack <PID> > thread-dump.txt
     ```
     - Ersetzen Sie `<PID>` durch Ihre Prozess-ID.
     - Für einen detaillierteren Dump (einschließlich Locks) verwenden Sie `jstack -l <PID> > thread-dump.txt`.
     - Wenn die JVM nicht auf Signale reagiert, verwenden Sie `jhsdb jstack --pid <PID>` (verfügbar in JDK 8+).

3. **Mehrere Dumps für die Analyse erfassen:**
   - Hänger erfordern oft einen Vergleich über die Zeit. Nehmen Sie 3-5 Dumps in Intervallen von 10-30 Sekunden:  
     ```
     jstack <PID> > dump1.txt
     sleep 10
     jstack <PID> > dump2.txt
     sleep 10
     jstack <PID> > dump3.txt
     ```
     - Automatisieren Sie dies bei Bedarf in einer Schleife (z.B. mit einem Bash-Skript).

4. **Analyse des Dumps:**
   - Öffnen Sie die Textdatei in einem Editor oder einer IDE.
   - Suchen Sie nach:
     - **Thread-Zuständen:** Konzentrieren Sie sich auf Threads in `RUNNABLE` (aktiv), `BLOCKED` (wartet auf Lock, potenzieller Deadlock), `WAITING` (Leerlauf-Warte) oder `TIMED_WAITING`.
     - **Deadlocks:** Suchen Sie nach "deadlock" oder verwenden Sie Tools wie `jstack -l`, die diese kennzeichnen.
     - **Stack Traces:** Identifizieren Sie sich wiederholende Muster oder Threads, die in bestimmten Methoden stecken bleiben (z.B. Endlosschleife in einer Schleife).
     - **Native Frames:** Wenn Threads in nativem Code stecken, kann dies auf JNI-Probleme oder Betriebssystem-bedingte Blocks hinweisen.
   - Tools für tiefergehende Analysen: VisualVM, Eclipse MAT oder Online-Parser wie fastThread.io. Laden Sie beispielsweise in VisualVM die Dump-Datei unter dem Reiter "Thread", um Locks und Zustände zu visualisieren.

Wenn die JVM nicht reagiert (z.B. keine Ausgabe von `kill -3 <PID>` unter Unix), könnte der Hänger auf Betriebssystemebene liegen – erwägen Sie dann vollständige Core Dumps via `gcore <PID>`.

### Verwendung von ProcDump zur Diagnose von Prozesshängern oder -stopps

ProcDump ist ein kostenloses Sysinternals-Tool für Windows, das Speicher- oder CPU-Dumps von Prozessen erstellt. Es eignet sich hervorragend zum Erfassen von Momentaufnahmen von Hängern in beliebigen Anwendungen (einschließlich Java), insbesondere wenn der Prozess nicht reagiert. Verwenden Sie es für vollständige Speicherauszüge, um sie mit Tools wie WinDbg oder Visual Studio zu analysieren.

#### Schritte zur Verwendung von ProcDump:
1. **Herunterladen und Einrichten:**
   - Holen Sie sich ProcDump von der Microsoft Sysinternals-Website (procdump.exe).
   - Führen Sie die Eingabeaufforderung als Administrator aus.
   - Navigieren Sie zum Ordner, der procdump.exe enthält.

2. **Identifizieren des Prozesses:**
   - Verwenden Sie den Task-Manager oder `tasklist | findstr <Prozessname>`, um die PID oder den Image-Namen (z.B. `java.exe`) zu erhalten.

3. **Erfassen eines Hänger-Dumps:**
   - Für einen sofortigen vollständigen Speicherauszug (nützlich für feststeckte Prozesse):  
     ```
     procdump -ma <Prozessname-oder-PID>
     ```
     - `-ma`: Vollständiger Speicherauszug (beinhaltet alle Threads und den Heap).
     - Beispiel: `procdump -ma java.exe` oder `procdump -ma 12345`.

   - Für automatische Hängererkennung (löst bei Nichtreagieren aus):  
     ```
     procdump -h <Prozessname-oder-PID> -o
     ```
     - `-h`: Überwacht auf Hänger (Prozess reagiert 5+ Sekunden nicht auf Fensternachrichten; für Dienste ohne Fenster verwenden Sie CPU-Schwellenwerte wie `-h 80` für 80 % CPU).
     - `-o`: Überschreibt vorhandene Dumps.
     - Für Dienste: Kombinieren Sie mit `-e` für Ausnahmen oder überwachen Sie die CPU: `procdump -c 80 -h <Dienst-exe>`.

   - Nehmen Sie mehrere Dumps: Fügen Sie `-n 3` für 3 Dumps in Intervallen hinzu (z.B. `-t 10` für 10 Sekunden Verzögerung):  
     ```
     procdump -ma -n 3 -t 10 <PID>
     ```

4. **Analyse des Dumps:**
   - Dumps werden als `.dmp`-Dateien im aktuellen Verzeichnis gespeichert.
   - Öffnen Sie sie in WinDbg (kostenlos von Microsoft) oder im Visual Studio Debugger.
   - Wichtige Befehle in WinDbg:
     - `!threads`: Listet Threads und Zustände auf (nach blockierten/wartenden suchen).
     - `~<Thread-ID>s`: Wechselt zu einem Thread und verwendet `k` für den Stack-Trace.
     - `!analyze -v`: Führt eine automatische Analyse auf Hänger/Deadlocks durch.
   - Für Java-spezifische Analysen laden Sie den Dump in Eclipse MAT oder verwenden `jhat` für einen Heap-Dump (falls mit `-mh`-Flag erfasst).

ProcDump funktioniert gut für nicht-interaktive Prozesse wie Dienste; wenn der Hänger CPU-gebunden ist, verwenden Sie `-c`, um bei hoher CPU-Auslastung auszulösen.

### Allgemeine Tipps für beide Tools
- **Sicherheit:** Dumps können groß sein (GB für vollständigen Speicher); stellen Sie ausreichend Speicherplatz sicher.
- **Tools kombinieren:** Für Java unter Windows verwenden Sie zuerst jstack (leichter), dann ProcDump für tiefergehende Einblicke auf Betriebssystemebene.
- **Prävention:** Aktivieren Sie JVM-Flags wie `-XX:+PrintGCDetails` für die Protokollierung oder verwenden Sie Agents wie JFR für Profiling.
- Wenn Dumps kein klares Problem zeigen, überprüfen Sie Systemressourcen (CPU, Speicher, E/A) mit Tools wie `top` oder der Leistungsüberwachung.

[Oracle Java Troubleshooting Guide](https://docs.oracle.com/en/java/javase/17/troubleshoot/troubleshoot-process-hangs-and-loops.html)  
[Taking a Hang Dump with ProcDump](https://www.poppastring.com/blog/taking-a-hang-dump-or-crash-dump-with-procdump)  
[Java Thread Dump Analysis](https://www.baeldung.com/java-analyze-thread-dumps)  
[ProcDump Usage for Hangs](https://learn.microsoft.com/en-us/sysinternals/downloads/procdump)