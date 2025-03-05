---
audio: false
generated: true
lang: de
layout: post
title: Projektdateien, erstellt mit Eclipse IDE
translated: true
---

### Warum gibt es .project-Dateien und wofür sind `filteredResources`, `filter` und `matcher`?

`.project`-Dateien dienen dazu, projektspezifische Einstellungen und Konfigurationen für Entwicklungsumgebungen zu speichern. Im Kontext Ihrer Frage werden sie verwendet, um zu verwalten, wie Ressourcen (Dateien und Ordner) innerhalb eines Projekts angezeigt oder verarbeitet werden. Elemente wie `filteredResources`, `filter` und `matcher` sind Teil dieser Konfiguration und spielen eine Rolle bei der **Ressourcenfilterung** – einem Feature, das Entwicklern ermöglicht, bestimmte Dateien oder Ordner aus der Ansicht auszublenden, wie z.B. Build-Ausgaben, temporäre Dateien oder andere irrelevante Ressourcen. Dies hält den Arbeitsbereich organisiert und konzentriert sich auf die Dateien, die für die aktuelle Aufgabe wichtig sind.

- **`filteredResources`**: Dieser Abschnitt in der `.project`-Datei definiert, welche Ressourcen (Dateien oder Verzeichnisse) aus der Projektansicht ausgefiltert werden.
- **`filter`**: Dies gibt die Regeln oder Bedingungen für die Filterung an, wie z.B. Dateinamen, Muster oder Typen.
- **`matcher`**: Dies arbeitet mit dem `filter`, um zu definieren, wie die Filterkriterien angewendet werden, wie z.B. Muster oder Ausschlüsse.

Zum Beispiel könnte ein Entwickler diese Einstellungen verwenden, um temporäre Dateien (z.B. `.class`-Dateien oder Protokolle), die von einem Projekt erzeugt werden, aus dem Projekt-Explorer auszuschließen, was die Navigation durch die Codebasis erleichtert.

### Welche IDE erstellt diese Dateien?

Die **Eclipse IDE** ist das Hauptwerkzeug, das `.project`-Dateien erstellt und verwendet, einschließlich der Elemente `filteredResources`, `filter` und `matcher`. Eclipse verwendet die `.project`-Datei, um Metadaten über ein Projekt zu speichern, wie z.B. seine Art (z.B. Java-Projekt), Build-Befehle und Ressourcenfilter. Wenn Sie Ressourcenfilter in Eclipse konfigurieren (z.B. über die Projekt-Explorer-Ansicht), werden diese Einstellungen in der `.project`-Datei gespeichert, sodass sie über Sitzungen hinweg bestehen bleiben und angewendet werden, wenn das Projekt geöffnet wird.

Obwohl Eclipse die Haupt-IDE ist, die mit diesem Dateiformat verbunden ist, können auch andere Tools wie **Maven** oder **Gradle** `.project`-Dateien erstellen. Diese Build-Tools erstellen sie oft, um die Kompatibilität mit Eclipse sicherzustellen und so das nahtlose Importieren von Projekten zu ermöglichen. Die spezifische Verwendung von `filteredResources`, `filter` und `matcher` ist jedoch an das Ressourcenverwaltungssystem von Eclipse gebunden.

### Zusammenfassung

- **Zweck**: `.project`-Dateien dienen dazu, Projekteinstellungen zu verwalten, und `filteredResources`, `filter` und `matcher` werden von Eclipse verwendet, um unerwünschte Ressourcen aus der Projektansicht auszublenden.
- **IDE**: Eclipse erstellt diese Dateien nativ, obwohl Tools wie Maven oder Gradle sie auch für die Kompatibilität mit Eclipse erstellen können.

Diese Einrichtung ist besonders nützlich für Entwickler, die an komplexen Projekten arbeiten, bei denen Unordnung durch irrelevante Dateien den Arbeitsablauf sonst verlangsamen könnte.