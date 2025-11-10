---
audio: false
generated: true
lang: de
layout: post
title: 'Beherrschung des YourKit Java Profilers: Ein umfassender Leitfaden'
translated: true
type: note
---

# Umfassender Leitfaden für YourKit Java Profiler

YourKit Java Profiler ist ein leistungsstarkes und funktionsreiches Tool, das entwickelt wurde, um Entwicklern und Performance-Ingenieuren bei der Analyse und Optimierung der Leistung von Java-Anwendungen zu helfen. Es bietet tiefgehende Einblicke in die CPU-Auslastung, Speicherbelegung, Thread-Aktivität und mehr, was es zu einem unverzichtbaren Werkzeug für die Diagnose von Performance-Engpässen und Speicherlecks in Java-Anwendungen macht. Dieser Leitfaden bietet einen umfassenden Überblick über den YourKit Java Profiler, einschließlich seiner Funktionen, Einrichtung, Verwendung und Best Practices.

## Inhaltsverzeichnis
1. [Einführung in den YourKit Java Profiler](#einführung-in-den-yourkit-java-profiler)
2. [Hauptfunktionen](#hauptfunktionen)
3. [Systemanforderungen und Installation](#systemanforderungen-und-installation)
4. [Einrichten des YourKit Java Profilers](#einrichten-des-yourkit-java-profilers)
5. [Verwendung des YourKit Java Profilers](#verwendung-des-yourkit-java-profilers)
6. [Best Practices für effektives Profiling](#best-practices-für-effektives-profiling)
7. [Anwendungsfälle](#anwendungsfälle)
8. [Integration mit Entwicklungstools](#integration-mit-entwicklungstools)
9. [Lizenzierung und Support](#lizenzierung-und-support)
10. [Behebung häufiger Probleme](#behebung-häufiger-probleme)
11. [Fazit](#fazit)

## Einführung in den YourKit Java Profiler
YourKit Java Profiler ist ein Profiling-Tool auf professionellem Niveau, entwickelt von YourKit LLC, zur Überwachung und Optimierung der Leistung von Java-Anwendungen, die auf Java EE- und Java SE-Plattformen laufen. Es wird häufig von Entwicklern verwendet, um Performance-Engpässe, Speicherlecks, Thread-Synchronisationsprobleme und ineffizienten Code zu identifizieren. Der Profiler unterstützt sowohl lokales als auch Remote-Profiling, was ihn für Entwicklungs-, Test- und Produktionsumgebungen geeignet macht. Mit seinem Overhead-armen Design, der benutzerfreundlichen Oberfläche und den fortschrittlichen Analysetools ist YourKit die erste Wahl für Java-Entwickler, die die Anwendungsleistung verbessern möchten.

## Hauptfunktionen
YourKit Java Profiler bietet einen umfassenden Funktionsumfang zur Diagnose und Optimierung von Java-Anwendungen. Im Folgenden sind die Hauptfunktionen aufgeführt:

### CPU-Profiling
- **Aufrufbäume und Hot Spots**: Visualisieren Sie Methodenausführungszeiten und identifizieren Sie CPU-intensive Methoden mithilfe von Aufrufbäumen oder Hot-Spot-Listen.
- **Flame Graphs**: Bieten eine visuelle Darstellung des Call Stacks, um Performance-Engpässe schnell zu lokalisieren.
- **Smart What-If Analysis**: Bewerten Sie potenzielle Leistungsverbesserungen ohne Neu-Profiling der Anwendung.
- **Sampling und Tracing**: Wählen Sie zwischen Sampling (geringer Overhead) oder Tracing (detailliert), um Leistung und Genauigkeit abzuwägen.

### Memory-Profiling
- **Object Heap Analysis**: Durchlaufen Sie den Objektgraphen, inspizieren Sie Objekteigenschaften und identifizieren Sie Speicherlecks.
- **Memory Retention Paths**: Verstehen Sie, warum Objekte im Speicher verbleiben, und optimieren Sie Objekt-Lebenszyklen.
- **Snapshot Comparison**: Vergleichen Sie Speicher-Snapshots, um Änderungen der Speichernutzung über die Zeit zu verfolgen.
- **Deobfuscation Support**: Stellen Sie ursprüngliche Klassen-, Methoden- und Feldnamen für Anwendungen wieder her, die mit Tools wie ProGuard oder Zelix KlassMaster obfuskiert wurden.

### Thread-Profiling
- **Thread Activity Visualization**: Überwachen Sie Thread-Zustände, erkennen Sie blockierte Threads und analysieren Sie Synchronisationsprobleme.
- **Deadlock Detection**: Identifizieren Sie automatisch Deadlocks und erhalten Sie Details zu beteiligten Threads und Monitoren.
- **Frozen Threads View**: Identifizieren Sie Threads, die aufgrund langer Wartezeiten oder potenzieller Deadlocks inaktiv sind.

### Exception-Profiling
- **Exception Analysis**: Erkennen und analysieren Sie während der Ausführung geworfene Exceptions, einschließlich versteckter Performance-Probleme durch übermäßiges Exception-Throwing.
- **Exception Flame Graph**: Visualisieren Sie Exception-Vorkommen, um problematische Bereiche zu identifizieren.

### Datenbank- und I/O-Profiling
- **SQL und NoSQL Support**: Profilen Sie Abfragen für Datenbanken wie MongoDB, Cassandra und HBase, um langsame Abfragen zu identifizieren.
- **HTTP Request Analysis**: Kombinieren Sie Thread-Zustände mit HTTP-Anfragen, um die Leistung der Anfrageverarbeitung zu verstehen.
- **I/O Operations**: Erkennen Sie ineffiziente I/O-Operationen und optimieren Sie die Ressourcennutzung.

### Performance Inspections
- **40+ Built-in Inspections**: Identifizieren Sie automatisch häufige Probleme wie geleakte Webapps, duplizierte Objekte, nicht geschlossene SQL-Statements und ineffiziente Collections.
- **Custom Inspections**: Erstellen Sie benutzerdefinierte Probes, um anwendungsspezifische Performancedaten zu sammeln.

### Telemetrie und Performance-Charts
- **Real-Time Monitoring**: Verfolgen Sie CPU, Speicher, Garbage Collection (GC) und andere Metriken in Echtzeit.
- **Customizable Interface**: Passen Sie die Benutzeroberfläche an, um sich auf relevante Performancedaten zu konzentrieren.

### Integration und Automatisierung
- **IDE Plugins**: Nahtlose Integration mit Eclipse, IntelliJ IDEA und NetBeans für Profiling mit einem Klick.
- **Command-Line Tools**: Automatisieren Sie Profiling-Aufgaben und integrieren Sie sie in CI/CD-Pipelines (z.B. Jenkins, TeamCity).
- **API Support**: Verwenden Sie die erweiterbare API, um Profiling-Modi programmgesteuert zu verwalten und Snapshots zu erfassen.

### Remote-Profiling
- **SSH Tunneling**: Profilen Sie Remote-Anwendungen sicher mit minimalem Setup.
- **Cloud und Container Support**: Profilen Sie Anwendungen in Cloud-, Container- und geclusterten Umgebungen wie Docker.

## Systemanforderungen und Installation
### Systemanforderungen
- **Unterstützte Plattformen**: Windows, macOS, Linux, Solaris, FreeBSD (arm32, arm64, ppc64le, x64, x86).
- **Java-Versionen**: Unterstützt Java 8 bis Java 24.
- **JDK-Anforderung**: JDK 1.5 oder neuer, um den Profiler auszuführen.
- **Hardware**: Mindestens 2 GB RAM (4 GB oder mehr für große Anwendungen empfohlen).

### Installation
1. **Download**: Laden Sie die neueste Version des YourKit Java Profilers von der offiziellen Website (https://www.yourkit.com/java/profiler/download/) herunter. Eine 15-tägige kostenlose Testversion ist verfügbar.
2. **Installieren**:
   - **Windows**: Führen Sie das Installationsprogramm aus und folgen Sie den Anweisungen.
   - **Linux/Solaris**: Führen Sie das Skript `yjp.sh` aus dem Installationsverzeichnis aus (`<YourKit Home>/bin/yjp.sh`).
   - **macOS**: Entpacken Sie die heruntergeladene Anwendung und klicken Sie auf das Symbol.
3. **Installation überprüfen**: Stellen Sie sicher, dass der Profiler korrekt installiert ist, indem Sie `java -agentpath:<vollständiger Agent-Bibliothekspfad> -version` ausführen. Dies prüft, ob der Profiler-Agent korrekt geladen wird.

## Einrichten des YourKit Java Profilers
### Profiling aktivieren
Um eine Java-Anwendung zu profilieren, müssen Sie den YourKit Profiler-Agenten an die JVM anhängen. Dies kann manuell oder über eine IDE-Integration erfolgen.

#### Manuelles Setup
1. **Agent-Bibliothek lokalisieren**:
   - Die Agent-Bibliothek befindet sich unter `<YourKit Home>/bin/<platform>/libyjpagent.so` (Linux) oder `libyjpagent.dll` (Windows).
2. **JVM konfigurieren**:
   - Fügen Sie den Agenten zum JVM-Startbefehl hinzu:
     ```bash
     java -agentpath:<vollständiger Agent-Bibliothekspfad> YourMainClass
     ```
   - Beispiel für Linux:
     ```bash
     java -agentpath:/home/user/yjp-2025.3/bin/linux-x86-64/libyjpagent.so YourMainClass
     ```
   - Optionale Parameter:
     - `onexit=memory,dir=<Pfad>`: Erfasst einen Speicher-Snapshot beim Beenden.
     - `usedmem=70`: Löst einen Snapshot aus, wenn die Speichernutzung 70 % erreicht.
3. **Agent-Laden überprüfen**:
   - Überprüfen Sie die Konsolenausgabe auf Meldungen wie `[YourKit Java Profiler 2025.3] Profiler agent is listening on port 10001`.

#### IDE-Integration
1. Installieren Sie das YourKit-Plugin für Ihre IDE (Eclipse, IntelliJ IDEA oder NetBeans) über den jeweiligen Plugin-Marktplatz.
2. Konfigurieren Sie das Plugin so, dass es auf das YourKit-Installationsverzeichnis verweist.
3. Verwenden Sie die Profiling-Option der IDE, um Ihre Anwendung mit angehängtem YourKit zu starten.

#### Remote-Profiling
1. **SSH-Zugang sicherstellen**: Sie benötigen SSH-Zugang zum Remote-Server.
2. **Agent kopieren**:
   - Kopieren Sie die entsprechende Agent-Bibliothek auf den Remote-Server.
   - Beispiel für Docker:
     ```bash
     docker cp libyjpagent.so <Container-ID>:/Pfad/zum/Agent
     ```
3. **Anwendung starten**:
   - Fügen Sie den Agenten zum JVM-Startbefehl auf dem Remote-Server hinzu.
4. **Profiler-UI verbinden**:
   - Öffnen Sie die YourKit Profiler-UI und wählen Sie "Profile remote Java server or application".
   - Geben Sie den Remote-Host und Port ein (Standard: 10001) oder verwenden Sie SSH-Tunneling.
   - Testen Sie die Verbindung und verbinden Sie sich mit der Anwendung.

## Verwendung des YourKit Java Profilers
### Starten einer Profiling-Sitzung
1. **Profiler-UI starten**:
   - Unter Windows: Starten Sie über das Startmenü.
   - Unter Linux/Solaris: Führen Sie `<YourKit Home>/bin/yjp.sh` aus.
   - Unter macOS: Klicken Sie auf das YourKit Java Profiler-Symbol.
2. **Mit der Anwendung verbinden**:
   - Lokale Anwendungen erscheinen in der Liste "Monitor Applications".
   - Für Remote-Anwendungen konfigurieren Sie die Verbindung wie oben beschrieben.
3. **Profiling-Modus auswählen**:
   - Wählen Sie CPU-, Memory- oder Exception-Profiling aus der Symbolleiste.
   - Verwenden Sie Sampling für Overhead-armes CPU-Profiling oder Tracing für detaillierte Analysen.

### CPU-Leistung analysieren
1. **CPU-Profiling starten**:
   - Wählen Sie den gewünschten Profiling-Modus (Sampling oder Tracing) aus der Symbolleiste.
   - Die Ergebnisse werden in Ansichten wie Call Tree, Flame Graph oder Method List angezeigt.
2. **Ergebnisse interpretieren**:
   - **Call Tree**: Zeigt Methodenaufrufketten und Ausführungszeiten an.
   - **Flame Graph**: Hebt CPU-intensive Methoden visuell hervor.
   - **Hot Spots**: Listet Methoden auf, die die meiste CPU-Zeit verbrauchen.
3. **Trigger verwenden**: Starten Sie das Profiling automatisch basierend auf hoher CPU-Auslastung oder bestimmten Methodenaufrufen.

### Speichernutzung analysieren
1. **Memory-Profiling starten**:
   - Aktivieren Sie Memory-Profiling, um Objektallokationen und Garbage Collection zu verfolgen.
2. **Object Heap inspizieren**:
   - Durchlaufen Sie den Objektgraphen, um zurückgehaltene Objekte zu identifizieren.
   - Verwenden Sie Retention Paths, um Speicherlecks zu finden.
3. **Snapshots vergleichen**:
   - Erfassen Sie Snapshots zu verschiedenen Zeitpunkten und vergleichen Sie sie, um Speicherwachstum zu identifizieren.

### Thread- und Deadlock-Analyse
1. **Threads überwachen**:
   - Zeigen Sie Thread-Zustände an und identifizieren Sie blockierte oder eingefrorene Threads.
   - Überprüfen Sie den Tab "Deadlocks" zur automatischen Deadlock-Erkennung.
2. **Monitore analysieren**:
   - Verwenden Sie den Monitors-Tab, um Warte- und Blockierungsereignisse zu inspizieren.
   - Visualisieren Sie Contention mit dem Monitor Flame Graph.

### Exception- und Datenbank-Profiling
1. **Exception-Profiling**:
   - Aktivieren Sie Exception-Profiling, um geworfene Exceptions zu verfolgen.
   - Verwenden Sie den Exception Tree oder Flame Graph, um Exception-Muster zu analysieren.
2. **Datenbank-Profiling**:
   - Überwachen Sie SQL/NoSQL-Abfragen, um langsame oder ineffiziente Abfragen zu identifizieren.
   - Kombinieren Sie dies mit Thread-Zuständen, um Datenbankaufrufe mit der Anwendungsleistung zu korrelieren.

### Erfassen und Analysieren von Snapshots
1. **Snapshots erfassen**:
   - Verwenden Sie die UI oder das Kommandozeilen-Tool:
     ```bash
     java -jar <YourKit Home>/lib/yjp-controller-api-redist.jar localhost 10001 capture-performance-snapshot
     ```
   - Snapshots werden standardmäßig in `<user home>/Snapshots` gespeichert.
2. **Snapshots analysieren**:
   - Öffnen Sie Snapshots in der YourKit-UI zur Offline-Analyse.
   - Exportieren Sie Berichte in Formaten wie HTML, CSV oder XML zur Weitergabe.

## Best Practices für effektives Profiling
1. **Overhead minimieren**:
   - Verwenden Sie Sampling für CPU-Profiling in der Produktion, um den Overhead zu reduzieren.
   - Vermeiden Sie das Aktivieren unnötiger Funktionen wie J2EE-Profiling unter hoher Last.
2. **Ausreichende Profiling-Dauer**:
   - Erfassen Sie Daten lange genug, um intermittierende Probleme zu identifizieren, vermeiden Sie aber übermäßige Datensammlung.
3. **Fokus auf Schlüsselmetriken**:
   - Priorisieren Sie CPU-intensive Methoden, Speicherlecks und Thread-Contention.
4. **Snapshots zum Vergleich verwenden**:
   - Erfassen und vergleichen Sie regelmäßig Snapshots, um Leistungsänderungen zu verfolgen.
5. **Automatisierung nutzen**:
   - Integrieren Sie Kommandozeilen-Tools in CI/CD-Pipelines für kontinuierliche Leistungsüberwachung.
6. **Zuerst in Staging testen**:
   - Üben Sie Profiling in einer Staging-Umgebung, bevor Sie es in der Produktion verwenden, um seine Auswirkungen zu verstehen.

## Anwendungsfälle
- **Performance-Optimierung**: Identifizieren und optimieren Sie CPU-intensive Methoden oder langsame Datenbankabfragen.
- **Speicherleck-Erkennung**: Finden Sie unnötig im Speicher gehaltene Objekte und optimieren Sie die Garbage Collection.
- **Thread-Synchronisation**: Lösen Sie Deadlocks und Contention-Probleme in Multithread-Anwendungen.
- **Produktionsüberwachung**: Verwenden Sie Overhead-armes Profiling, um Anwendungen in der Produktion zu überwachen, ohne signifikante Leistungseinbußen.
- **CI/CD-Integration**: Automatisieren Sie Performance-Tests in Build-Pipelines, um Regressionen frühzeitig zu erkennen.

## Integration mit Entwicklungstools
- **IDE-Plugins**: YourKit integriert sich mit Eclipse, IntelliJ IDEA und NetBeans, ermöglicht Profiling mit einem Klick und die Navigation von Profiling-Ergebnissen zum Quellcode.
- **CI/CD-Tools**: Unterstützt Jenkins, Bamboo, TeamCity, Gradle, Maven, Ant und JUnit für automatisiertes Profiling.
- **Docker**: Verwenden Sie optimierte Agent-Binaries für das Profiling von Anwendungen in Docker-Containern.
- **Cloud-Umgebungen**: Profilen Sie Anwendungen in AWS, Azure oder anderen Cloud-Plattformen mithilfe von SSH- oder AWS-CLI-Integration.

## Lizenzierung und Support
- **Lizenzoptionen**:
  - Kommerzielle Lizenzen für Einzelpersonen oder Teams.
  - Kostenlose 15-tägige Testversion verfügbar.
  - Kostenlose Lizenzen für nicht-kommerzielle Open-Source-Projekte.
  - Vergünstigte Lizenzen für Bildungs- und wissenschaftliche Einrichtungen.
- **Support**:
  - Umfangreiche Online-Dokumentation: `<YourKit Home>/docs/help/index.html`.
  - Community-Support über Foren und E-Mail.
  - Kostenloser Support für Open-Source-Projekte.

## Behebung häufiger Probleme
1. **Agent lässt sich nicht laden**:
   - Überprüfen Sie den Agent-Pfad und die Kompatibilität (z.B. 64-Bit-Agent für 64-Bit-JVM).
   - Überprüfen Sie die Konsole auf Fehlermeldungen und konsultieren Sie den Troubleshooting-Leitfaden.
2. **Hoher Profiling-Overhead**:
   - Wechseln Sie in den Sampling-Modus für CPU-Profiling.
   - Deaktivieren Sie unnötige Funktionen wie J2EE-Profiling.
3. **Verbindungsprobleme beim Remote-Profiling**:
   - Stellen Sie SSH-Zugang und korrekte Port-Konfiguration sicher (Standard: 10001).
   - Überprüfen Sie die Firewall-Einstellungen, um die Profiler-Kommunikation zu ermöglichen.
4. **Probleme bei der Snapshot-Analyse**:
   - Stellen Sie ausreichend Speicherplatz für Snapshots sicher.
   - Verwenden Sie die YourKit-UI zum Öffnen von Snapshots anstelle von Drittanbieter-Tools.

## Fazit
YourKit Java Profiler ist ein vielseitiges und leistungsstarkes Tool zur Diagnose und Optimierung der Leistung von Java-Anwendungen. Sein umfassender Funktionsumfang, das Overhead-arme Design und die Unterstützung verschiedener Umgebungen machen es gleichermaßen für Entwickler und Performance-Ingenieure geeignet. Indem Sie die Einrichtungs- und Verwendungsrichtlinien in diesem Leitfaden befolgen, können Sie YourKit effektiv nutzen, um Performance-Engpässe, Speicherlecks und Threading-Probleme zu identifizieren und zu beheben und letztendlich die Reaktionsfähigkeit und Skalierbarkeit Ihrer Java-Anwendungen zu verbessern.

Weitere detaillierte Informationen finden Sie in der offiziellen YourKit-Dokumentation unter https://www.yourkit.com/docs/java/ oder nutzen Sie die 15-tägige kostenlose Testversion, um praktische Erfahrungen zu sammeln.

---
**Quellen**:
- YourKit Offizielle Website: https://www.yourkit.com[](https://www.yourkit.com/java/profiler/)[](https://www.yourkit.com/java/profiler/features/)[](https://www.yourkit.com/)
- DevOpsSchool: https://www.devopsschool.com[](https://www.devopsschool.com/blog/what-is-yourkit-java-profiler-and-use-cases-of-yourkit-java-profiler/)
- Baeldung: https://www.baeldung.com[](https://www.baeldung.com/java-profilers)
- Jahia: https://www.jahia.com[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)[](https://www.jahia.com/fr/blog/analyzingsystemperformancewit)
- YourKit Dokumentation: https://www.yourkit.com/docs/java/[](https://www.yourkit.com/docs/java-profiler/latest/help/enabling-profiling-manually.jsp)[](https://www.yourkit.com/docs/java-profiler/latest/help/cpu_profiling.jsp)[](https://www.yourkit.com/docs/java-profiler/latest/help/connect-to-profiled-application.jsp)
- MuleSoft Dokumentation: https://docs.mulesoft.com[](https://docs.mulesoft.com/mule-runtime/latest/profiling-mule)