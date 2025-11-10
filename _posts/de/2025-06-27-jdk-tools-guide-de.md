---
audio: false
generated: true
lang: de
layout: post
title: Übersicht der OpenJDK 21-Tools
translated: true
type: note
---

Das Verzeichnis `/usr/lib/jvm/java-21-openjdk-amd64/bin/` enthält Tools, die vom OpenJDK 21 Java Development Kit (JDK) bereitgestellt werden. Diese Tools werden für verschiedene Aufgaben im Zusammenhang mit Java-Entwicklung, Debugging, Monitoring und Packaging verwendet. Nachfolgend finden Sie eine kurze Erklärung jedes Tools und seiner gängigen Verwendung. Für detaillierte Informationen können Sie `tool_name --help` oder `man tool_name` im Terminal für die meisten dieser Tools ausführen.

---

### 1. **jar** - Erstellen und Verwalten von Java ARchive (JAR)-Dateien
- **Zweck**: Verpacken von Java-Klassen und Ressourcen in eine JAR-Datei oder Extrahieren von Inhalten aus einer JAR-Datei.
- **Gängige Verwendung**:
  ```bash
  jar cf myapp.jar *.class  # Erstellt eine JAR-Datei
  jar xf myapp.jar          # Extrahiert den Inhalt einer JAR-Datei
  jar tf myapp.jar          # Listet den Inhalt einer JAR-Datei auf
  ```
- **Beispiel**: `jar cvfm myapp.jar manifest.txt *.class` (erstellt eine JAR-Datei mit einer Manifest-Datei).

---

### 2. **java** - Starten einer Java-Anwendung
- **Zweck**: Ausführen eines Java-Programms durch Ausführen einer Klassen-Datei oder JAR-Datei.
- **Gängige Verwendung**:
  ```bash
  java MyClass              # Führt eine Klassen-Datei aus
  java -jar myapp.jar       # Führt eine JAR-Datei aus
  java -cp . MyClass        # Führt mit einem spezifischen Classpath aus
  ```
- **Beispiel**: `java -Xmx512m -jar myapp.jar` (führt eine JAR-Datei mit 512 MB maximalem Heap-Speicher aus).

---

### 3. **javadoc** - Generieren von API-Dokumentation
- **Zweck**: Erstellen von HTML-Dokumentation aus Java-Quellcode-Kommentaren.
- **Gängige Verwendung**:
  ```bash
  javadoc -d docs MyClass.java  # Generiert Dokumentation im Ordner 'docs'
  ```
- **Beispiel**: `javadoc -d docs -sourcepath src -subpackages com.example` (generiert Dokumentation für ein Paket).

---

### 4. **jcmd** - Senden von Diagnosebefehlen an eine laufende JVM
- **Zweck**: Interaktion mit einem laufenden Java-Prozess für Diagnosezwecke (z.B. Thread-Dumps, Heap-Informationen).
- **Gängige Verwendung**:
  ```bash
  jcmd <pid> help           # Listet verfügbare Befehle für einen JVM-Prozess auf
  jcmd <pid> Thread.print   # Druckt einen Thread-Dump
  ```
- **Beispiel**: `jcmd 1234 GC.run` (löst Garbage Collection für Prozess-ID 1234 aus).

---

### 5. **jdb** - Java Debugger
- **Zweck**: Interaktives Debuggen von Java-Anwendungen.
- **Gängige Verwendung**:
  ```bash
  jdb MyClass               # Startet das Debuggen einer Klasse
  java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 MyClass  # Führt mit Debug-Agent aus
  jdb -attach localhost:5005  # Verbindet mit einer laufenden JVM
  ```
- **Beispiel**: `jdb -sourcepath src MyClass` (debuggt mit Quellcode).

---

### 6. **jdeps** - Analysieren von Klassen- und JAR-Abhängigkeiten
- **Zweck**: Identifizieren von Abhängigkeiten einer Java-Anwendung oder -Bibliothek.
- **Gängige Verwendung**:
  ```bash
  jdeps myapp.jar           # Analysiert Abhängigkeiten in einer JAR-Datei
  jdeps -s MyClass.class    # Zusammenfassung der Abhängigkeiten
  ```
- **Beispiel**: `jdeps -v myapp.jar` (detaillierte Abhängigkeitsanalyse).

---

### 7. **jhsdb** - Java HotSpot Debugger
- **Zweck**: Erweitertes Debuggen und Analysieren von JVM-Prozessen (z.B. Core Dumps).
- **Gängige Verwendung**:
  ```bash
  jhsdb jmap --heap --pid <pid>  # Analysiert den Heap eines laufenden Prozesses
  jhsdb hsdb                     # Startet den HotSpot Debugger GUI
  ```
- **Beispiel**: `jhsdb jmap --heap --pid 1234` (erstellt Heap-Informationen für Prozess 1234).

---

### 8. **jinfo** - Anzeigen oder Ändern der JVM-Konfiguration
- **Zweck**: Überprüfen oder Ändern von JVM-Optionen für einen laufenden Prozess.
- **Gängige Verwendung**:
  ```bash
  jinfo <pid>               # Zeigt JVM-Flags und Eigenschaften an
  jinfo -flag +PrintGC <pid>  # Aktiviert ein JVM-Flag
  ```
- **Beispiel**: `jinfo -sysprops 1234` (zeigt Systemeigenschaften für Prozess 1234 an).

---

### 9. **jmap** - Erstellen von JVM-Speicher- oder Heap-Informationen
- **Zweck**: Erstellen von Heap-Dumps oder Speicherstatistiken.
- **Gängige Verwendung**:
  ```bash
  jmap -heap <pid>          # Druckt Heap-Zusammenfassung
  jmap -dump:file=dump.hprof <pid>  # Erstellt einen Heap-Dump
  ```
- **Beispiel**: `jmap -dump:live,format=b,file=dump.hprof 1234` (erstellt einen Dump von live-Objekten).

---

### 10. **jpackage** - Packen von Java-Anwendungen
- **Zweck**: Erstellen von nativen Installationsprogrammen oder ausführbaren Dateien für Java-Anwendungen (z.B. .deb, .rpm, .exe).
- **Gängige Verwendung**:
  ```bash
  jpackage --input target --name MyApp --main-jar myapp.jar --main-class MyClass
  ```
- **Beispiel**: `jpackage --type deb --input target --name MyApp --main-jar myapp.jar` (erstellt ein Debian-Paket).

---

### 11. **jps** - Auflisten laufender JVM-Prozesse
- **Zweck**: Anzeigen von Java-Prozessen mit ihren Prozess-IDs (PIDs).
- **Gängige Verwendung**:
  ```bash
  jps                       # Listet alle Java-Prozesse auf
  jps -l                    # Schließt vollständige Klassennamen ein
  ```
- **Beispiel**: `jps -m` (zeigt Hauptklasse und Argumente an).

---

### 12. **jrunscript** - Ausführen von Skripten in Java
- **Zweck**: Ausführen von Skripten (z.B. JavaScript) unter Verwendung der Java Scripting Engine.
- **Gängige Verwendung**:
  ```bash
  jrunscript -e "print('Hello')"  # Führt einen einzelnen Skriptbefehl aus
  jrunscript script.js            # Führt eine Skriptdatei aus
  ```
- **Beispiel**: `jrunscript -l js -e "print(2+2)"` (führt JavaScript-Code aus).

---

### 13. **jshell** - Interaktive Java REPL
- **Zweck**: Interaktives Ausführen von Java-Code-Schnipseln zum Testen oder Lernen.
- **Gängige Verwendung**:
  ```bash
  jshell                    # Startet die interaktive Shell
  jshell script.jsh         # Führt ein JShell-Skript aus
  ```
- **Beispiel**: `jshell -q` (startet JShell im Quiet-Modus).

---

### 14. **jstack** - Erzeugen von Thread-Dumps
- **Zweck**: Erfassen der Stack-Traces von Threads in einer laufenden JVM.
- **Gängige Verwendung**:
  ```bash
  jstack <pid>              # Druckt Thread-Dump
  jstack -l <pid>           # Schließt Sperr-Informationen ein
  ```
- **Beispiel**: `jstack 1234 > threads.txt` (speichert Thread-Dump in einer Datei).

---

### 15. **jstat** - Überwachen von JVM-Statistiken
- **Zweck**: Anzeigen von Leistungsstatistiken (z.B. Garbage Collection, Speichernutzung).
- **Gängige Verwendung**:
  ```bash
  jstat -gc <pid>           # Zeigt Garbage Collection-Statistiken
  jstat -class <pid> 1000   # Zeigt Klassenladestatistiken jede 1 Sekunde
  ```
- **Beispiel**: `jstat -gcutil 1234 1000 5` (zeigt GC-Statistiken 5 Mal, jede 1 Sekunde).

---

### 16. **jstatd** - JVM-Monitoring-Daemon
- **Zweck**: Ausführen eines Remote-Monitoring-Servers, um Tools wie `jstat` die Remote-Verbindung zu ermöglichen.
- **Gängige Verwendung**:
  ```bash
  jstatd -J-Djava.security.policy=jstatd.policy
  ```
- **Beispiel**: `jstatd -p 1099` (startet Daemon auf Port 1099).

---

### 17. **keytool** - Verwalten kryptografischer Schlüssel und Zertifikate
- **Zweck**: Erstellen und Verwalten von Keystores für sichere Java-Anwendungen.
- **Gängige Verwendung**:
  ```bash
  keytool -genkeypair -alias mykey -keystore keystore.jks  # Erzeugt ein Schlüsselpaar
  keytool -list -keystore keystore.jks                     # Listet Keystore-Inhalte auf
  ```
- **Beispiel**: `keytool -importcert -file cert.pem -keystore keystore.jks` (importiert ein Zertifikat).

---

### 18. **rmiregistry** - Starten der RMI-Registry
- **Zweck**: Ausführen einer Registry für Java Remote Method Invocation (RMI)-Objekte.
- **Gängige Verwendung**:
  ```bash
  rmiregistry               # Startet RMI-Registry auf Standardport (1099)
  rmiregistry 1234          # Startet auf einem spezifischen Port
  ```
- **Beispiel**: `rmiregistry -J-Djava.rmi.server.codebase=file:./classes/` (startet mit einer Codebase).

---

### 19. **serialver** - Generieren von serialVersionUID für Klassen
- **Zweck**: Berechnen der `serialVersionUID` für Java-Klassen, die `Serializable` implementieren.
- **Gängige Verwendung**:
  ```bash
  serialver MyClass         # Druckt serialVersionUID für eine Klasse
  ```
- **Beispiel**: `serialver -classpath . com.example.MyClass` (berechnet für eine spezifische Klasse).

---

### 20. **javac** - Java-Compiler
- **Zweck**: Kompilieren von Java-Quelldateien in Bytecode.
- **Gängige Verwendung**:
  ```bash
  javac MyClass.java        # Kompiliert eine einzelne Datei
  javac -d bin *.java       # Kompiliert in ein spezifisches Verzeichnis
  ```
- **Beispiel**: `javac -cp lib/* -sourcepath src -d bin src/MyClass.java` (kompiliert mit Abhängigkeiten).

---

### 21. **javap** - Disassemblieren von Klassen-Dateien
- **Zweck**: Anzeigen des Bytecode oder der Methodensignaturen einer kompilierten Klasse.
- **Gängige Verwendung**:
  ```bash
  javap -c MyClass          # Disassembliert Bytecode
  javap -s MyClass          # Zeigt Methodensignaturen
  ```
- **Beispiel**: `javap -c -private MyClass` (zeigt private Methoden und Bytecode).

---

### 22. **jconsole** - Grafisches JVM-Monitoring-Tool
- **Zweck**: Überwachen der JVM-Leistung (Speicher, Threads, CPU) über eine GUI.
- **Gängige Verwendung**:
  ```bash
  jconsole                  # Startet JConsole und verbindet mit einer lokalen JVM
  jconsole <pid>            # Verbindet mit einem spezifischen Prozess
  ```
- **Beispiel**: `jconsole localhost:1234` (verbindet mit einer entfernten JVM).

---

### 23. **jdeprscan** - Scannen nach veralteten APIs
- **Zweck**: Identifizieren der Verwendung veralteter APIs in einer JAR- oder Klassen-Datei.
- **Gängige Verwendung**:
  ```bash
  jdeprscan myapp.jar       # Scannt eine JAR-Datei nach veralteten APIs
  ```
- **Beispiel**: `jdeprscan --release 11 myapp.jar` (prüft gegen Java 11 APIs).

---

### 24. **jfr** - Java Flight Recorder
- **Zweck**: Verwalten und Analysieren von Java Flight Recorder Profiling-Daten.
- **Gängige Verwendung**:
  ```bash
  jfr print recording.jfr   # Druckt den Inhalt einer JFR-Datei
  jfr summary recording.jfr # Fasst eine JFR-Datei zusammen
  ```
- **Beispiel**: `jfr print --events GC recording.jfr` (zeigt GC-Ereignisse).

---

### 25. **jimage** - Inspizieren oder Extrahieren von JIMAGE-Dateien
- **Zweck**: Arbeiten mit JIMAGE-Dateien (verwendet in JDK-Modulen).
- **Gängige Verwendung**:
  ```bash
  jimage extract image.jimage  # Extrahiert den Inhalt einer JIMAGE-Datei
  ```
- **Beispiel**: `jimage list image.jimage` (listet den Inhalt einer JIMAGE-Datei auf).

---

### 26. **jlink** - Erstellen benutzerdefinierter Java-Laufzeitimages
- **Zweck**: Erstellen einer minimalen JRE mit nur den erforderlichen Modulen.
- **Gängige Verwendung**:
  ```bash
  jlink --module-path mods --add-modules java.base --output myjre
  ```
- **Beispiel**: `jlink --add-modules java.base,java.sql --output custom-jre` (erstellt JRE mit spezifischen Modulen).

---

### 27. **jmod** - Verwalten von JMOD-Dateien
- **Zweck**: Erstellen oder Verwalten von JMOD-Dateien (verwendet für JDK-Module).
- **Gängige Verwendung**:
  ```bash
  jmod create --class-path classes mymod.jmod  # Erstellt eine JMOD-Datei
  jmod list mymod.jmod                        # Listet den Inhalt auf
  ```
- **Beispiel**: `jmod extract mymod.jmod` (extrahiert JMOD-Inhalt).

---

### 28. **jwebserver** - Einfacher HTTP-Server
- **Zweck**: Ausführen eines einfachen Webservers zum Bereitstellen statischer Dateien.
- **Gängige Verwendung**:
  ```bash
  jwebserver -d /path/to/dir  # Startet Server für ein Verzeichnis
  jwebserver -p 8080          # Startet auf einem spezifischen Port
  ```
- **Beispiel**: `jwebserver -d ./html -p 8000` (bedient Dateien aus ./html auf Port 8000).

---

### Tipps für weiterführendes Lernen
- **Dokumentation**: Führen Sie `tool_name --help` aus oder überprüfen Sie die JDK-Dokumentation von Oracle (z.B. https://docs.oracle.com/en/java/javase/21/docs/specs/man/).
- **Man Pages**: Verwenden Sie `man tool_name` für Tools mit Manual Pages.
- **Praxis**: Experimentieren Sie in einem Testprojekt, um das Tool-Verhalten zu verstehen.
- **Monitoring-Tools**: Verwenden Sie für `jcmd`, `jmap`, `jstack` usw. `jps`, um die PID Ihres Java-Prozesses zu finden.
- **Debugging**: Kombinieren Sie `jdb`, `jhsdb` oder `jconsole` für erweitertes Debugging.

Wenn Sie an einem Trading-Projekt arbeiten (wie durch Ihr Verzeichnis nahegelegt), sind Tools wie `javac`, `java`, `jar` und `jpackage` wahrscheinlich am relevantesten für das Kompilieren, Ausführen und Packen Ihrer Anwendung. Für die Leistungsoptimierung verwenden Sie `jstat`, `jmap` oder `jfr`. Lassen Sie mich wissen, wenn Sie einen tieferen Einblick in ein bestimmtes Tool oder Hilfe bei Ihrem Trading-Projekt benötigen!