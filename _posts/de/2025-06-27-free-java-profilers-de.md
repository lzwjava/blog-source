---
audio: false
generated: true
lang: de
layout: post
title: Kostenlose Alternativen zu YourKit Java Profiler
translated: true
type: note
---

Ja, es gibt kostenlose Java Profiler, die ähnliche Funktionen wie der YourKit Java Profiler bieten, auch wenn sie sich in Bezug auf Funktionsumfang, Benutzerfreundlichkeit und Analyse-Tiefe unterscheiden können. Nachfolgend sind einige der besten kostenlosen Alternativen zum YourKit Java Profiler aufgeführt, basierend auf ihren Fähigkeiten für CPU-, Speicher- und Thread-Profiling sowie ihrer Eignung für Entwicklungs- und Produktionsumgebungen:

1.  **Java VisualVM**:
    -   **Beschreibung**: Ein kostenloses, quelloffenes Profiling-Tool, das bis zum JDK 8 im Java Development Kit (JDK) enthalten war und jetzt als eigenständiger Download unter [visualvm.github.io](https://visualvm.github.io/) verfügbar ist. Es integriert mehrere JDK-Kommandozeilen-Tools (z.B. `jstat`, `jmap`, `jconsole`) in eine benutzerfreundliche GUI.
    -   **Funktionen**:
        -   Überwacht CPU-Auslastung, Speicher, Garbage Collection und Thread-Aktivität.
        -   Unterstützt lokales und entferntes Profiling.
        -   Erweiterbar über Plugins für zusätzliche Funktionalität (z.B. MBeans, Thread-Dumps).
        -   Visualisiert Heap-Dumps und Thread-Zustände für die grundlegende Erkennung von Speicherlecks und Leistungsanalyse.
    -   **Vergleich mit YourKit**: Obwohl nicht so funktionsreich wie YourKit, ist VisualVM leichtgewichtig und für grundlegende Profiling-Aufgaben ausreichend. Es fehlen fortgeschrittene Funktionen wie YourKits "What-if"-CPU-Profiling oder detaillierte Datenbankabfrage-Analyse, aber es ist ein guter Ausgangspunkt für Entwickler.
    -   **Setup unter Ubuntu**:
        ```bash
        sudo apt update
        sudo apt install visualvm
        visualvm
        ```
        Alternativ können Sie die neueste Version von der offiziellen Website herunterladen und ausführen:
        ```bash
        unzip visualvm_<version>.zip -d /opt/visualvm
        cd /opt/visualvm/visualvm_<version>/bin
        ./visualvm
        ```
    -   **Am besten geeignet für**: Anfänger, kleine Projekte oder Entwickler, die eine schnelle, kostenlose Profiling-Lösung benötigen.

2.  **Java Mission Control (JMC)**:
    -   **Beschreibung**: Ein kostenloses, quelloffenes Tool, das im JDK (seit JDK 7u40) enthalten ist und zur Leistungsüberwachung und Profiling dient. Es baut auf Java Flight Recorder (JFR) auf, der detaillierte Laufzeitdaten mit geringem Overhead erfasst.
    -   **Funktionen**:
        -   Bietet Flight Recording für eingehende Analyse von CPU, Speicher und JVM-Ereignissen.
        -   Visualisiert Methodenaufrufbäume, Speicherzuweisungen und Thread-Aktivität.
        -   Geeignet für Produktionsumgebungen aufgrund geringen Overheads.
        -   Integriert sich in IDEs wie IntelliJ IDEA und Eclipse (über Plugins).
    -   **Vergleich mit YourKit**: JMC ist fortschrittlicher als VisualVM und konkurriert eng mit YourKit im Bereich Production-Profiling. Es fehlen einige der fortgeschrittenen UI-Funktionen von YourKit (z.B. Flame Graphs, detailliertes Exception-Profiling), ist aber leistungsstark für die Analyse von JVM-Interna und die Optimierung von Langzeit-Anwendungen.
    -   **Setup unter Ubuntu**:
        -   JMC ist im OpenJDK oder Oracle JDK enthalten. Zum Starten:
            ```bash
            jmc
            ```
        -   Stellen Sie sicher, dass Ihr JDK Version 7 oder höher ist (z.B. OpenJDK 11 oder 17):
            ```bash
            sudo apt install openjdk-17-jdk
            ```
        -   Aktivieren Sie JFR für Ihre Anwendung durch Hinzufügen von JVM-Flags (z.B. `-XX:+UnlockCommercialFeatures -XX:+FlightRecorder` für ältere JDKs, in neueren Versionen nicht mehr nötig).
    -   **Am besten geeignet für**: Entwickler und Operations-Teams, die an produktionsreifen Anwendungen arbeiten und detaillierte JVM-Einblicke benötigen.

3.  **Async Profiler**:
    -   **Beschreibung**: Ein kostenloser, quelloffener (Apache-2.0-Lizenz) Profiler, der für CPU- und Speicher-Profiling mit geringem Overhead entwickelt wurde und besonders effektiv für native Methodenaufrufe und Hochleistungsanwendungen ist. Er wird häufig in Bereichen mit niedriger Latenz wie High-Frequency Trading (HFT) verwendet.
    -   **Funktionen**:
        -   Erzeugt Flame Graphs für intuitive Visualisierung von CPU-Engpässen.
        -   Unterstützt CPU-, Speicherzuweisungs- und Lock-Contention-Profiling.
        -   Arbeitet unter Linux, macOS und Windows mit minimalem Overhead.
        -   Kann sowohl lokale als auch entfernte Anwendungen profilieren.
    -   **Vergleich mit YourKit**: Async Profiler glänzt bei der Erzeugung von Flame Graphs und dem Profiling nativer Methoden, was YourKit auch unterstützt, jedoch mit einer aufpolierteren UI. Es fehlt die umfassende Datenbankabfrage-Analyse und die GUI-gesteuerte Analyse von YourKit, ist aber sehr effektiv, um Leistungsengpässe zu identifizieren.
    -   **Setup unter Ubuntu**:
        -   Laden Sie die neueste Version von [GitHub](https://github.com/async-profiler/async-profiler) herunter:
            ```bash
            wget https://github.com/async-profiler/async-profiler/releases/download/v3.0/async-profiler-3.0-linux-x64.tar.gz
            tar -xvzf async-profiler-3.0-linux-x64.tar.gz -C /opt/async-profiler
            ```
        -   Führen Sie den Profiler für eine Java-Anwendung aus (ersetzen Sie `<pid>` durch die Prozess-ID):
            ```bash
            /opt/async-profiler/profiler.sh -d 30 -f profile.svg <pid>
            ```
        -   Betrachten Sie das generierte Flame Graph (`profile.svg`) in einem Browser.
    -   **Am besten geeignet für**: Fortgeschrittene Entwickler, die an leistungskritischen Anwendungen arbeiten, insbesondere solchen, die Flame Graphs oder Profiling nativer Methoden benötigen.

4.  **Arthas**:
    -   **Beschreibung**: Ein quelloffenes (Apache-2.0-Lizenz) Diagnose-Tool von Alibaba, entwickelt für Echtzeit-Überwachung und Profiling in Produktionsumgebungen ohne Neustart der Anwendung. Verfügbar unter [arthas.aliyun.com](https://arthas.aliyun.com/).
    -   **Funktionen**:
        -   Echtzeit-Überwachung von CPU, Speicher und Thread-Auslastung.
        -   Dynamische Neudefinition von Klassen und Dekompilierung zur Fehlerbehebung.
        -   Kommandozeilen-Schnittstelle zur Diagnose von Problemen in Produktionsumgebungen.
        -   Profilt Methodenausführungszeiten und identifiziert Hotspots.
    -   **Vergleich mit YourKit**: Arthas ist weniger GUI-gesteuert als YourKit und konzentriert sich mehr auf Echtzeit-Diagnose als auf tiefgehende Nachanalyse. Es ist weniger umfassend für die Erkennung von Speicherlecks, glänzt aber in Produktionsumgebungen, in denen minimale Störung kritisch ist.
    -   **Setup unter Ubuntu**:
        -   Laden Sie Arthas herunter und installieren Sie es:
            ```bash
            wget https://arthas.aliyun.com/arthas-boot.jar
            java -jar arthas-boot.jar
            ```
        -   Folgen Sie der interaktiven Eingabeaufforderung, um sich an einen laufenden JVM-Prozess anzuhängen.
    -   **Am besten geeignet für**: Operations-Teams und Entwickler, die Echtzeit-Diagnose in der Produktion ohne aufwändige Einrichtung benötigen.

5.  **Eclipse Memory Analyzer (MAT)**:
    -   **Beschreibung**: Ein kostenloses, quelloffenes Tool, das sich auf Speicher-Profiling und Heap-Dump-Analyse spezialisiert hat, verfügbar unter [eclipse.org/mat/](https://eclipse.org/mat/).
    -   **Funktionen**:
        -   Analysiert Heap-Dumps, um Speicherlecks zu erkennen und die Speichernutzung zu optimieren.
        -   Bietet detaillierte Berichte über Objektzuweisungen und Referenzen.
        -   Leichtgewichtig und integriert sich in die Eclipse IDE.
    -   **Vergleich mit YourKit**: MAT ist auf Speicheranalyse spezialisiert und verfügt nicht über die CPU- oder Datenbank-Profiling-Fähigkeiten von YourKit. Es ist eine starke Alternative für speicherbezogene Aufgaben, aber kein vollständiger Ersatz für den umfassenden Funktionsumfang von YourKit.
    -   **Setup unter Ubuntu**:
        -   Laden Sie MAT herunter und installieren Sie es:
            ```bash
            sudo apt install eclipse-mat
            ```
        -   Alternativ laden Sie die eigenständige Version von der Eclipse-Website herunter und führen sie aus:
            ```bash
            unzip MemoryAnalyzer-<version>.zip -d /opt/mat
            /opt/mat/MemoryAnalyzer
            ```
        -   Erzeugen Sie einen Heap-Dump mit `jmap` oder YourKit und öffnen Sie ihn dann in MAT zur Analyse.
    -   **Am besten geeignet für**: Entwickler, die sich auf die Erkennung von Speicherlecks und Heap-Analyse konzentrieren.

### Wichtige Überlegungen:
-   **Funktionslücken**: Kostenlose Tools wie VisualVM, JMC und Async Profiler sind leistungsstark, aber es fehlen ihnen möglicherweise fortgeschrittene Funktionen von YourKit, wie z.B. detaillierte Datenbankabfrage-Analyse, Exception-Analyse oder die "What-if"-CPU-Profiling-Funktion. Die aufpolierte UI und Integrationen (z.B. mit Eclipse, IntelliJ) von YourKit machen es für einige Workflows auch benutzerfreundlicher.
-   **Anwendungsfall**:
    -   Für **kleine Projekte oder Anfänger** sind VisualVM oder Eclipse MAT ausreichend und einfach einzurichten.
    -   Für **Produktionsumgebungen** sind JMC oder Async Profiler aufgrund ihres geringen Overheads und ihrer Echtzeit-Fähigkeiten besser geeignet.
    -   Für **komplexe Enterprise-Anwendungen** sind YourKit oder JProfiler (eine weitere kostenpflichtige Alternative) möglicherweise aufgrund ihres umfassenden Funktionsumfangs immer noch vorzuziehen, obwohl kostenlose Tools mit zusätzlichem Aufwand ausreichen können.
-   **Kosten**: YourKit erfordert eine kommerzielle Lizenz (ab ~499$ für die persönliche Nutzung), bietet aber eine 15-tägige kostenlose Testversion und kostenlose Lizenzen für nicht-kommerzielle Open-Source-Projekte. Im Gegensatz dazu sind die oben aufgeführten Tools vollständig kostenlos.
-   **Community-Feedback**: Beiträge auf X und Reddit heben die Beliebtheit von Async Profiler aufgrund seiner Genauigkeit beim Profiling nativer Methoden und seiner Flame Graphs hervor.