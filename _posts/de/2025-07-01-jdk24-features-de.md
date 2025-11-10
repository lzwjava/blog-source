---
audio: false
generated: true
lang: de
layout: post
title: 'JDK 24: Wichtige Funktionen und Aktualisierungen'
translated: true
type: note
---

### Einführung in JDK 24

Das Java Development Kit (JDK) 24 ist ein Feature-Release der Java SE (Standard Edition) Platform, das am 18. März 2025 offiziell als Referenzimplementierung der Version 24 veröffentlicht wurde, spezifiziert durch JSR 399 im Java Community Process. Es setzt den Sechs-Monats-Release-Zyklus von Oracle fort und liefert eine robuste Reihe von Verbesserungen, um die Entwicklerproduktivität, Leistung und Sicherheit zu steigern. JDK 24 enthält 24 JDK Enhancement Proposals (JEPs), die höchste Anzahl an Features seit Beginn des zeitbasierten Release-Zeitplans im Jahr 2018, was es zu einem bedeutenden Meilenstein in der Evolution von Java macht. Es dient als Schrittmacher für JDK 25, dem nächsten Long-Term Support (LTS)-Release, das für September 2025 geplant ist.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://openjdk.org/projects/jdk/24/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### Long-Term Support (LTS) Status

JDK 24 ist **kein** Long-Term Support (LTS)-Release. Es ist ein Release mit Kurzzeit-Support und erhält nur sechs Monate Premier-Support von Oracle, bis September 2025, wenn es von JDK 25 abgelöst wird. Im Gegensatz dazu erhalten LTS-Releases wie JDK 21 (September 2023) und das kommende JDK 25 (September 2025) mindestens fünf Jahre Premier-Support, was sie für unternehmerische Stabilität präferiert macht. Oracles LTS-Zyklus findet alle zwei Jahre statt, wobei JDK 21 das letzte LTS war und JDK 25 das nächste sein wird.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)

### Veröffentlichung und Stabilität

JDK 24 ist ein **stabiles, produktionsreifes Release**, das am 18. März 2025 die Allgemeine Verfügbarkeit (GA) erreicht hat. Produktionsreife Binärdateien sind von Oracle unter den Oracle No-Fee Terms and Conditions (NFTC) und der GNU General Public License (GPLv2) für OpenJDK verfügbar, wobei Binärdateien anderer Anbieter kurz darauf folgen. Das Release enthält über 3.000 Bugfixes und kleinere Verbesserungen jenseits der 24 JEPs, was Stabilität für den allgemeinen Einsatz gewährleistet. Da es sich jedoch um ein Nicht-LTS-Release handelt, ist es primär für Entwickler gedacht, die neue Features testen möchten, und nicht für Unternehmen, die langfristige Stabilität benötigen.[](https://openjdk.org/projects/jdk/24/)[](https://www.theregister.com/2025/03/18/oracle_jdk_24/)[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)

### Neue Features in JDK 24

JDK 24 führt 24 JEPs ein, kategorisiert in Core Library-Erweiterungen, Sprachverbesserungen, Sicherheitsfeatures, HotSpot JVM-Optimierungen und Java-Tools. Davon sind 14 permanente Features, sieben sind Preview-Features, zwei sind experimentell und eines ist ein Inkubator-Modul. Nachfolgend sind einige der bemerkenswertesten Features aufgeführt, mit Fokus auf solche, die für Entwickler und Deployments relevant sind:

1.  **Stream Gatherers (JEP 485)** - Permanent
    - Erweitert die Stream API durch die Einführung der `Gatherer`-Schnittstelle, die es Entwicklern ermöglicht, benutzerdefinierte Intermediate Operations für Stream-Pipelines zu definieren. Dies ermöglicht flexiblere Datentransformationen und ergänzt die bestehende `Collector`-Schnittstelle für Terminal Operations.
    - Beispiel: Gruppieren von Wörtern nach Länge mit `StreamGatherers.groupBy`.
    - Vorteil: Vereinfacht komplexe Stream-Verarbeitung für Entwickler.[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

2.  **Ahead-of-Time Class Loading & Linking (JEP 483)** - Experimentell
    - Teil von Project Leyden, dieses Feature reduziert die Startzeiten von Java-Anwendungen, indem Klassen während einer Vorbereitungsphase in einen Cache vorab geladen und verlinkt werden. Der Cache wird zur Laufzeit wiederverwendet und umgeht so aufwändige Class-Loading-Schritte.
    - Vorteil: Verbessert die Leistung für Cloud- und Microservices-Anwendungen.[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

3.  **Compact Object Headers (JEP 450)** - Experimentell
    - Teil von Project Lilliput, dies reduziert die Größe von Java-Object Headern auf 64-Bit-Architekturen von 96–128 Bit auf 64 Bit, was die Heap-Nutzung verringert und die Speichereffizienz verbessert.
    - Vorteil: Reduziert den Memory Footprint und verbessert die Datenlokalität für eine bessere Leistung.[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)[](https://www.happycoders.eu/java/java-24-features/)

4.  **Generational Shenandoah Garbage Collector (JEP 404)** - Permanent
    - Stellt den Generational Mode des Shenandoah GC von einem experimentellen in ein Produkt-Feature um, verbessert den Durchsatz, die Resilienz bei Lastspitzen und die Speichernutzung, indem Objekte in Young und Old Generationen unterteilt werden.
    - Vorteil: Steigert die Leistung für anspruchsvolle Workloads.[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.infoworld.com/article/3846172/jdk-25-the-new-features-in-java-25.html)

5.  **Module Import Declarations (JEP 494)** - Zweite Preview
    - Vereinfacht die modulare Programmierung, indem der direkte Import aller von einem Modul exportierten Pakete erlaubt wird, ohne dass eine `module-info.java`-Datei erforderlich ist (z.B. `import module java.sql;`).
    - Vorteil: Reduziert den Overhead für schlanke Anwendungen und Scripting, hilft Anfängern und beim Rapid Prototyping.[](https://codefarm0.medium.com/java-24-features-a-deep-dive-into-whats-coming-81e77382b39c)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

6.  **Flexible Constructor Bodies (JEP 492)** - Dritte Preview
    - Erlaubt Anweisungen in Konstruktoren vor `super()`- oder `this()`-Aufrufen, ermöglicht eine natürlichere Platzierung der Feldinitialisierungslogik ohne Hilfsmethoden.
    - Vorteil: Verbessert die Code-Zuverlässigkeit und Lesbarkeit, insbesondere bei der Subklassierung.[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

7.  **Key Derivation Function (KDF) API (JEP 487)** - Preview
    - Führt eine API für kryptographische Key Derivation Functions wie HMAC-based Extract-and-Expand und Argon2 ein, unterstützt sicheres Passwort-Hashing und die Interaktion mit kryptographischer Hardware.
    - Vorteil: Erhöht die Sicherheit für Anwendungen, die erweiterte Kryptographie benötigen.[](https://www.jrebel.com/blog/whats-new-java-24)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

8.  **Permanently Disable the Security Manager (JEP 486)** - Permanent
    - Entfernt den Security Manager, der in JDK 17 als deprecated markiert wurde, da er nicht mehr das primäre Mittel zum Absichern von Java-Anwendungen ist (ersetzt durch Container-basierte Sandboxing).
    - Hinweis: Anwendungen, die auf den Security Manager angewiesen sind, benötigen möglicherweise architektonische Änderungen.[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

9.  **Late Barrier Expansion for G1 Garbage Collector (JEP 464)** - Permanent
    - Vereinfacht die Barrier-Implementierung des G1 GC, indem die Expansion später in der Compilation-Pipeline verschoben wird, was die Kompilierzeit reduziert und die Wartbarkeit verbessert.
    - Vorteil: Verbessert die Leistung für Anwendungen, die den G1 GC verwenden.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

10. **Quantum-Resistant Cryptography (JEP 452, 453)** - Preview
    - Führt Module-Lattice-Based Key Encapsulation Mechanism (ML-KEM) und Digital Signature Algorithm (ML-DSA) ein, um vor Quantencomputing-Angriffen zu schützen.
    - Vorteil: Macht Java-Anwendungen zukunftssicher für Post-Quantum-Security.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

11. **Scoped Values (JEP 480)** - Vierte Preview
    - Ermöglicht das sicherere Teilen unveränderlicher Daten innerhalb und über Threads hinweg im Vergleich zu Thread-Local Variables und verbessert die Nebenläufigkeitsbehandlung.
    - Vorteil: Vereinfacht das Nachvollziehen von nebenläufigem Code.[](https://www.jrebel.com/blog/whats-new-java-24)

12. **Deprecate 32-bit x86 Port (JEP 501)** - Permanent
    - Markiert den 32-Bit-x86-Port als deprecated für die Entfernung in JDK 25, mit dem architektur-agnostischen Zero-Port als Alternative für 32-Bit-Systeme.
    - Vorteil: Reduziert Wartungsaufwand, Fokus auf moderne Architekturen.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

13. **Vector API (JEP 489)** - Neunter Inkubator
    - Verfeinert weiterhin die Vector API für SIMD-Programmierung, mit Verbesserungen an Cross-Lane- und arithmetischen Operationen.
    - Vorteil: Verbessert die Leistung für rechenintensive Anwendungen.[](https://www.infoq.com/news/2025/02/java-24-so-far/)

14. **Linking Run-Time Images without JMODs (JEP 493)** - Permanent
    - Ermöglicht dem `jlink`-Tool die Erstellung benutzerdefinierter Laufzeitimages ohne JMOD-Dateien, reduziert die JDK-Größe um ~25 %.
    - Vorteil: Erhöht die Deployment-Effizienz für benutzerdefinierte Java-Laufzeitumgebungen.[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### Zusätzliche Hinweise

-   **Preview- und Experimentelle Features**: Viele Features (z.B. Scoped Values, KDF API) befinden sich im Preview- oder experimentellen Stadium, was Entwicklern erlaubt, sie zu testen und Feedback zu geben, bevor sie in JDK 25 oder später permanent werden. Diese können sich vor der Finalisierung noch ändern.[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.infoq.com/news/2025/02/java-24-so-far/)
-   **Projekt-Integration**: JDK 24 führt Elemente von OpenJDK-Projekten wie Leyden (Startoptimierung), Lilliput (Speichereffizienz) und Panama (Native Interoperabilität) ein und legt den Grundstein für zukünftige Verbesserungen.[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)
-   **Sicherheit und Deprecation**: Features wie die Entfernung des Security Managers und die Deprecation des 32-Bit-x86-Ports spiegeln Oracles Fokus auf die Modernisierung von Java wider, indem veraltete Komponenten ausgemustert werden.[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### Fazit

JDK 24 ist ein stabiles, funktionsreiches Release, das die Leistung, Entwicklerproduktivität und Sicherheit von Java vorantreibt. Obwohl es kein LTS-Release ist, bieten seine 24 JEPs bedeutende Verbesserungen, von denen viele im kommenden LTS-Release JDK 25 finalisiert werden. Entwickler können Features wie Stream Gatherers und Module Import Declarations für sofortige Produktivitätsgewinne nutzen, während experimentelle Features wie Compact Object Headers und Ahead-of-Time Class Loading die fortlaufende Optimierung von Java für moderne Workloads signalisieren. Für den Unternehmenseinsatz wird aufgrund des erweiterten Supports die Nutzung von LTS-Releases wie JDK 21 oder das Abwarten von JDK 25 empfohlen.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

Für weitere Details, besuchen Sie:
-   [Oracle JDK 24 Release Notes](https://www.oracle.com)[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)
-   [OpenJDK JDK 24](https://openjdk.org)[](https://openjdk.org/projects/jdk/24/)
-   [JavaOne 2025 Conference](https://www.oracle.com/javaone) für Feature-Highlights[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)