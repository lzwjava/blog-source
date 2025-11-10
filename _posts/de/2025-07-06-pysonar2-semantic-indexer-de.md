---
audio: false
generated: true
lang: de
layout: post
title: 'PySonar2: Semantischer Python-Indexierer'
translated: true
type: note
---

PySonar2 ist ein semantischer Indexierer für Python, entwickelt von yinwang0, der interprozedurale Typinferenz nutzt, um große Python-Codebasen zu analysieren. Es ist für die Stapelverarbeitung konzipiert und eignet sich daher eher für die Erstellung von Indizes für Code-Browser und Suchmaschinen als für Echtzeit-Integrated Development Environments (IDEs). Sein Hauptaugenmerk liegt auf Genauigkeit durch Typinferenz, die beschreiben soll, wie der Code tatsächlich verwendet wird.

**Wichtige Merkmale und Eigenschaften:**

*   **Semantische Indizierung:** Die Kernfunktion von PySonar2 ist der Aufbau eines semantischen Indexes von Python-Code, der erweiterte Code-Navigations- und Suchfunktionen ermöglicht.
*   **Interprozedurale Typinferenz:** Es setzt anspruchsvolle interprozedurale Typinferenz ein, um den Fluss und die Verwendung von Typen über eine gesamte Codebase hinweg zu verstehen, was zu seiner Genauigkeit beiträgt.
*   **Stapelverarbeitung:** Optimiert für die Verarbeitung großer Projekte auf Stapelbasis, im Gegensatz zu Echtzeit-Analyse-Tools.
*   **Bibliothek für Entwicklertools:** PySonar2 ist als grundlegende Bibliothek für andere Entwicklertools gedacht, nicht als eigenständige Endbenutzeranwendung.
*   **Apache-2.0-Lizenz:** Das Projekt ist quelloffen unter der Apache-2.0-Lizenz, die freie Nutzung, Modifikation und Verteilung erlaubt.

**Verbreitung und Nutzung:**

PySonar2 hat in der Industrie bedeutende Verbreitung gefunden und dient notably als Indexierungs-Engine für:

*   Googles internen Code Search
*   sourcegraph.com
*   insight.io

**Technische Details:**

*   **Sprachen:** Das Repository ist überwiegend in Java (94,4 %) geschrieben, wobei Python (5,1 %) für das Analyseziel verwendet wird.
*   **Build-System:** Es verwendet Maven für den Build. Um das Projekt zu bauen, führen Sie `mvn package -DskipTests` aus.
*   **Demo:** Eine Demo ist verfügbar, um einen einfachen Code-Browser für die Python 2.7-Standardbibliothek mit einem Java-Befehl zu erstellen.
*   **Systemanforderungen:** Erfordert Python 2.7.x oder 3.x, Java 8+ und Maven. Eine korrekte Konfiguration der Umgebungsvariablen `PATH` und `PYTHONPATH` ist entscheidend.
*   **Tests:** Unittests können mit `mvn test` ausgeführt werden. Neue Tests beinhalten das Erstellen von Python-Code in Verzeichnissen, die auf ".test" enden, innerhalb des `tests`-Verzeichnisses.

**Repository-Status:**

Das Repository hat beträchtliche Aufmerksamkeit erhalten, belegt durch:

*   **1,4k Sterne**
*   **506 Forks**

Aktuelle Commits deuten auf eine laufende Wartung hin, einschließlich Updates der README und der Version sowie Behebungen von Code Smells.

**Beiträge:**

Beiträge sind willkommen, allerdings wird bei signifikanten Änderungen eine Diskussion mit dem Maintainer empfohlen, aufgrund der komplexen zugrundeliegenden Theorie des Projekts.

Weitere Details finden Sie im [PySonar2 GitHub Repository](https://github.com/yinwang0/pysonar2).