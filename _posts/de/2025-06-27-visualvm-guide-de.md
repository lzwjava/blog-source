---
audio: false
generated: true
lang: de
layout: post
title: 'Umfassender Leitfaden zu VisualVM: Java-Profiling und -Überwachung'
translated: true
type: note
---

# Umfassender Leitfaden zu VisualVM

VisualVM ist ein leistungsstarkes, quelloffenes Java-Profiling- und Monitoring-Tool, das eine grafische Oberfläche zur Analyse der Leistung von Java-Anwendungen bereitstellt. Es ist im Java Development Kit (JDK) enthalten und besonders nützlich zur Diagnose von Leistungsproblemen, Speicherlecks und thread-bezogenen Problemen. Dieser Leitfaden behandelt die Funktionen, das Setup, die Verwendung und Best Practices von VisualVM für Entwickler und Systemadministratoren.

## Inhaltsverzeichnis
1. [Was ist VisualVM?](#was-ist-visualvm)
2. [Hauptfunktionen von VisualVM](#hauptfunktionen-von-visualvm)
3. [Systemanforderungen](#systemanforderungen)
4. [Installation von VisualVM](#installation-von-visualvm)
5. [Starten von VisualVM](#starten-von-visualvm)
6. [Verbinden mit Java-Anwendungen](#verbinden-mit-java-anwendungen)
7. [Verwendung von VisualVM für Monitoring und Profiling](#verwendung-von-visualvm-für-monitoring-und-profiling)
   - [Übersichts-Tab](#übersichts-tab)
   - [Monitor-Tab](#monitor-tab)
   - [Threads-Tab](#threads-tab)
   - [Sampler](#sampler)
   - [Profiler](#profiler)
   - [Heap-Dump-Analyse](#heap-dump-analyse)
   - [Thread-Dump-Analyse](#thread-dump-analyse)
   - [MBeans](#mbeans)
8. [Remote-Monitoring](#remote-monitoring)
9. [Erweiterung von VisualVM mit Plugins](#erweiterung-von-visualvm-mit-plugins)
10. [Best Practices](#best-practices)
11. [Behebung häufiger Probleme](#behebung-häufiger-probleme)
12. [Zusätzliche Ressourcen](#zusätzliche-ressourcen)

## Was ist VisualVM?

VisualVM ist ein Java-basiertes Tool, das mehrere JDK-Dienstprogramme (wie `jstack`, `jmap` und `jconsole`) in einer einzigen, benutzerfreundlichen Oberfläche integriert. Es ermöglicht Entwicklern, Java-Anwendungen in Echtzeit zu überwachen, CPU- und Speichernutzung zu profilieren, Heap-Dumps zu analysieren und Threads zu verwalten. VisualVM ist besonders wertvoll, um Leistungsengpässe, Speicherlecks und Threading-Probleme in lokalen und entfernten Java-Anwendungen zu identifizieren.

Ursprünglich von Sun Microsystems entwickelt, ist VisualVM jetzt Teil des Oracle JDK und wird aktiv als Open-Source-Projekt gepflegt. Es unterstützt Java-Anwendungen, die auf JDK 6 und höher laufen.

## Hauptfunktionen von VisualVM

- **Echtzeit-Monitoring**: Verfolgt CPU-Auslastung, Speicherverbrauch, Thread-Aktivität und Garbage Collection.
- **Profiling**: Bietet CPU- und Memory-Profiling zur Identifizierung von Leistungsengpässen und Speicherbelegungsmustern.
- **Heap-Dump-Analyse**: Ermöglicht die Untersuchung des Speicherinhalts zur Diagnose von Speicherlecks.
- **Thread-Dump-Analyse**: Hilft bei der Analyse von Thread-Zuständen und der Erkennung von Deadlocks.
- **MBean-Management**: Bietet Zugriff auf Java Management Extensions (JMX) zur Überwachung und Verwaltung von Anwendungen.
- **Remote-Monitoring**: Unterstützt die Überwachung von Java-Anwendungen, die auf entfernten Rechnern laufen.
- **Erweiterbarkeit**: Unterstützt Plugins zur Erweiterung der Funktionalität, wie z.B. Integration mit bestimmten Frameworks oder zusätzlichen Profiling-Tools.
- **Einfach und leichtgewichtig**: Minimales Setup mit einer intuitiven grafischen Oberfläche.

## Systemanforderungen

Um VisualVM zu verwenden, stellen Sie Folgendes sicher:
- **Betriebssystem**: Windows, macOS, Linux oder jedes andere Betriebssystem, das eine JVM unterstützt.
- **Java-Version**: JDK 6 oder höher (VisualVM ist ab JDK 8 im Lieferumfang enthalten).
- **Speicher**: Mindestens 512 MB freier RAM für leichtgewichtiges Monitoring; 1 GB oder mehr für die Heap-Dump-Analyse.
- **Festplattenspeicher**: Etwa 50 MB für die VisualVM-Installation.
- **Berechtigungen**: Administratorrechte können für bestimmte Funktionen erforderlich sein (z.B. Zugriff auf Systemprozesse).

## Installation von VisualVM

VisualVM ist ab Oracle JDK 8 im Lieferumfang enthalten und befindet sich im `bin`-Verzeichnis der JDK-Installation (`jvisualvm`-Executable). Alternativ können Sie es als eigenständige Anwendung herunterladen:

1. **Aus dem JDK**:
   - Wenn Sie JDK 8 oder höher installiert haben, ist VisualVM bereits im `JAVA_HOME/bin`-Verzeichnis als `jvisualvm` verfügbar.
   - Führen Sie die `jvisualvm`-Executable aus, um das Tool zu starten.

2. **Eigenständiger Download**:
   - Besuchen Sie die [VisualVM-Website](https://visualvm.github.io/), um die neueste eigenständige Version herunterzuladen.
   - Entpacken Sie die ZIP-Datei in ein Verzeichnis Ihrer Wahl.
   - Führen Sie die `visualvm`-Executable aus (z.B. `visualvm.exe` unter Windows).

3. **Installation überprüfen**:
   - Stellen Sie sicher, dass die Umgebungsvariable `JRE_HOME` oder `JAVA_HOME` auf ein kompatibles JDK/JRE verweist.
   - Testen Sie durch Starten von VisualVM.

## Starten von VisualVM

So starten Sie VisualVM:
- **Unter Windows**: Doppelklicken Sie auf `jvisualvm.exe` im `bin`-Ordner des JDK oder im eigenständigen Installationsverzeichnis.
- **Unter macOS/Linux**: Führen Sie `./jvisualvm` im Terminal im `bin`-Verzeichnis aus.
- Die VisualVM-Oberfläche öffnet sich und zeigt eine Liste lokaler Java-Anwendungen im linken Bereich an.

## Verbinden mit Java-Anwendungen

VisualVM kann sowohl lokale als auch entfernte Java-Anwendungen überwachen.

### Lokale Anwendungen
- Beim Start erkennt VisualVM automatisch laufende Java-Anwendungen auf dem lokalen Rechner.
- Doppelklicken Sie auf eine Anwendung im linken Bereich, um ihr Monitoring-Dashboard zu öffnen.
- Wenn eine Anwendung nicht aufgeführt wird, stellen Sie sicher, dass sie unter einer kompatiblen JVM läuft.

### Entfernte Anwendungen
So überwachen Sie eine entfernte Java-Anwendung:
1. Aktivieren Sie JMX in der entfernten Anwendung durch Hinzufügen von JVM-Argumenten (z.B. `-Dcom.sun.management.jmxremote`).
2. Gehen Sie in VisualVM zu **Datei > JMX-Verbindung hinzufügen**.
3. Geben Sie die IP-Adresse und den Port des entfernten Hosts ein (z.B. `hostname:port`).
4. Geben Sie Anmeldedaten an, falls eine Authentifizierung aktiviert ist.
5. Verbinden Sie sich und überwachen Sie die Anwendung.

**Hinweis**: Für sichere Verbindungen konfigurieren Sie SSL und Authentifizierung nach Bedarf (siehe [Remote-Monitoring](#remote-monitoring)).

## Verwendung von VisualVM für Monitoring und Profiling

VisualVM bietet mehrere Tabs und Tools zur Analyse von Java-Anwendungen. Im Folgenden finden Sie eine detaillierte Aufschlüsselung jeder Funktion.

### Übersichts-Tab
- Zeigt allgemeine Informationen über die Anwendung an, einschließlich:
  - JVM-Argumente
  - Systemeigenschaften
  - Anwendungsklassenpfad
  - PID (Prozess-ID)
- Nützlich zur Überprüfung der Konfiguration der Anwendung.

### Monitor-Tab
- Bietet Echtzeit-Diagramme für:
  - **CPU-Auslastung**: Verfolgt Anwendungs- und System-CPU-Auslastung.
  - **Heap-Speicher**: Überwacht die Heap-Nutzung (Eden, Old Gen, PermGen/Metaspace) und die Garbage Collection-Aktivität.
  - **Klassen**: Zeigt die Anzahl der geladenen Klassen.
  - **Threads**: Zeigt die Anzahl der lebenden und Daemon-Threads.
- Ermöglicht das manuelle Auslösen von Garbage Collection oder Heap-Dumps.

### Threads-Tab
- Visualisiert Thread-Zustände (Running, Sleeping, Waiting, etc.) über die Zeit.
- Bietet Thread-Dump-Funktionalität, um den aktuellen Zustand aller Threads zu erfassen.
- Nützlich zur Identifizierung von Deadlocks, blockierten Threads oder übermäßiger Thread-Nutzung.

### Sampler
- Bietet leichtgewichtiges CPU- und Memory-Sampling für die Leistungsanalyse.
- **CPU-Sampling**:
  - Erfasst die Ausführungszeit auf Methodenebene.
  - Identifiziert "heiße" Methoden, die die meiste CPU-Zeit verbrauchen.
- **Memory-Sampling**:
  - Verfolgt Objektallokationen und Speichernutzung.
  - Hilft bei der Identifizierung von Objekten, die übermäßig viel Speicher verbrauchen.
- Sampling hat einen geringeren Overhead als Profiling, liefert aber weniger detaillierte Daten.

### Profiler
- Bietet detailliertes CPU- und Memory-Profiling.
- **CPU-Profiling**:
  - Misst die Ausführungszeit von Methoden.
  - Identifiziert Leistungsengpässe auf Methodenebene.
- **Memory-Profiling**:
  - Verfolgt Objektallokationen und Referenzen.
  - Hilft bei der Erkennung von Speicherlecks durch Identifizierung von Objekten, die unerwartet bestehen bleiben.
- **Hinweis**: Profiling hat einen höheren Overhead als Sampling und kann die Anwendung verlangsamen.

### Heap-Dump-Analyse
- Ein Heap-Dump ist eine Momentaufnahme des Speichers der Anwendung.
- So generieren Sie einen Heap-Dump:
  1. Gehen Sie zum **Monitor**-Tab.
  2. Klicken Sie auf **Heap Dump**.
  3. Speichern Sie den Dump in einer `.hprof`-Datei oder analysieren Sie ihn direkt in VisualVM.
- Funktionen:
  - Anzeigen von Klasseninstanzen, -größen und -referenzen.
  - Identifizieren von Objekten mit hohem Speicherverbrauch.
  - Erkennen von Speicherlecks durch Analyse von Objekt-Retention-Pfaden.
- Verwenden Sie die **OQL (Object Query Language)**-Konsole für erweiterte Heap-Abfragen.

### Thread-Dump-Analyse
- Erfasst den Zustand aller Threads zu einem bestimmten Zeitpunkt.
- So generieren Sie einen Thread-Dump:
  1. Gehen Sie zum **Threads**-Tab.
  2. Klicken Sie auf **Thread Dump**.
  3. Analysieren Sie den Dump in VisualVM oder exportieren Sie ihn für externe Tools.
- Nützlich zur Diagnose von:
  - Deadlocks
  - Blockierten Threads
  - Thread-Contention-Problemen

### MBeans
- Bietet Zugriff auf JMX MBeans zur Verwaltung und Überwachung der Anwendung.
- Funktionen:
  - Anzeigen und Ändern von MBean-Attributen.
  - Aufrufen von MBean-Operationen.
  - Überwachen von MBean-Benachrichtigungen.
- Nützlich für Anwendungen mit benutzerdefinierter JMX-Instrumentierung.

## Remote-Monitoring

So überwachen Sie entfernte Java-Anwendungen:
1. **Konfigurieren Sie die entfernte JVM**:
   - Fügen Sie der entfernten Anwendung die folgenden JVM-Argumente hinzu:
     ```bash
     -Dcom.sun.management.jmxremote
     -Dcom.sun.management.jmxremote.port=<port>
     -Dcom.sun.management.jmxremote.ssl=false
     -Dcom.sun.management.jmxremote.authenticate=false
     ```
   - Für sichere Verbindungen aktivieren Sie SSL und Authentifizierung:
     ```bash
     -Dcom.sun.management.jmxremote.ssl=true
     -Dcom.sun.management.jmxremote.authenticate=true
     -Dcom.sun.management.jmxremote.password.file=<password_file>
     ```
2. **Richten Sie VisualVM ein**:
   - Fügen Sie in VisualVM eine JMX-Verbindung unter Verwendung der IP und des Ports des entfernten Hosts hinzu.
   - Geben Sie bei Bedarf Anmeldedaten an.
3. **Firewall-Konfiguration**:
   - Stellen Sie sicher, dass der JMX-Port auf dem entfernten Host geöffnet ist.
   - Verwenden Sie bei Bedarf SSH-Tunneling für sicheren Remote-Zugriff:
     ```bash
     ssh -L <local_port>:<remote_host>:<remote_port> user@remote_host
     ```

## Erweiterung von VisualVM mit Plugins

VisualVM unterstützt Plugins zur Erweiterung seiner Funktionalität:
1. **Plugins installieren**:
   - Gehen Sie zu **Tools > Plugins**.
   - Durchsuchen Sie das Plugin-Center nach verfügbaren Plugins (z.B. Visual GC, BTrace, JConsole-Plugins).
   - Installieren Sie sie und starten Sie VisualVM neu.
2. **Beliebte Plugins**:
   - **Visual GC**: Visualisiert die Garbage Collection-Aktivität.
   - **BTrace**: Bietet dynamisches Tracing für Java-Anwendungen.
   - **JConsole Plugins**: Fügt JConsole-kompatible Funktionen hinzu.
3. **Benutzerdefinierte Plugins**:
   - Laden Sie Plugins von der VisualVM-Website oder von Drittanbietern herunter.
   - Platzieren Sie die Plugin-Dateien im `plugins`-Verzeichnis und starten Sie VisualVM neu.

## Best Practices

- **Beginnen Sie mit Sampling**: Verwenden Sie Sampling vor dem Profiling, um die Leistungsauswirkungen zu minimieren.
- **Beschränken Sie den Profiling-Bereich**: Profilen Sie bestimmte Pakete oder Klassen, um den Overhead zu reduzieren.
- **Regelmäßige Heap-Dumps**: Planen Sie periodische Heap-Dumps für langlebige Anwendungen, um Speichertrends zu verfolgen.
- **Überwachen Sie die Garbage Collection**: Verwenden Sie das Visual GC-Plugin zur Analyse der GC-Leistung.
- **Sichere Remote-Verbindungen**: Verwenden Sie immer SSL und Authentifizierung für Remote-Monitoring.
- **Speichern Sie Snapshots**: Speichern Sie Heap- und Thread-Dumps für spätere Analysen oder die Zusammenarbeit.
- **Verwenden Sie OQL für erweiterte Analysen**: Lernen Sie OQL für effiziente Heap-Dump-Abfragen.
- **Überwachen Sie die Ressourcennutzung**: Stellen Sie sicher, dass VisualVM über ausreichend Speicher für große Heap-Dumps verfügt.

## Behebung häufiger Probleme

- **Anwendung wird nicht erkannt**:
  - Stellen Sie sicher, dass die Anwendung auf einer kompatiblen JVM läuft.
  - Prüfen Sie, ob die JVM für JMX-Verbindungen konfiguriert ist.
- **Hoher Overhead während des Profilings**:
  - Wechseln Sie zu Sampling für geringeren Overhead.
  - Profilen Sie bestimmte Klassen oder Methoden.
- **Verbindungsprobleme beim Remote-Monitoring**:
  - Überprüfen Sie den JMX-Port und die Firewall-Einstellungen.
  - Testen Sie die Konnektivität mit `telnet <host> <port>`.
- **OutOfMemoryError in VisualVM**:
  - Erhöhen Sie die Heap-Größe von VisualVM durch Bearbeiten der `visualvm.conf`-Datei:
    ```bash
    -J-Xmx<memory_size>m
    ```
- **Heap-Dump-Analyse ist langsam**:
  - Verwenden Sie einen Rechner mit mehr RAM.
  - Filtern Sie Klassen, um den Analyseumfang zu reduzieren.

## Zusätzliche Ressourcen

- **Offizielle Website**: [visualvm.github.io](https://visualvm.github.io/)
- **Dokumentation**: [VisualVM-Dokumentation](https://visualvm.github.io/documentation.html)
- **Tutorials**:
  - Oracles [VisualVM-Leitfaden](https://www.oracle.com/java/technologies/visualvm.html)
  - [Java-Leistungsoptimierung mit VisualVM](https://www.baeldung.com/java-visualvm)
- **Community**:
  - [VisualVM GitHub Issues](https://github.com/visualvm/visualvm.github.io/issues)
  - [Stack Overflow VisualVM Tag](https://stackoverflow.com/questions/tagged/visualvm)