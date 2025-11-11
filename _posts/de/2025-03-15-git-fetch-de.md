---
audio: false
generated: true
lang: de
layout: post
title: Grundlagen von Git Fetch
translated: true
type: note
---

Lassen Sie mich den Git-Befehl `/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=5 origin` Schritt für Schritt erklären. Dieser Befehl wird verwendet, um Updates von einem entfernten Git-Repository abzurufen, mit spezifischen Optionen, um zu steuern, welche und wie viele Daten abgerufen werden. Hier ist eine Aufschlüsselung:

### Befehlsaufschlüsselung

1.  **`/usr/bin/git`**
    Dies ist einfach der Pfad zur Git-Executable auf dem System. Er weist das System an, das Git-Programm mit den nachfolgenden Optionen und dem Befehl auszuführen.

2.  **`-c protocol.version=2`**
    Dies setzt eine Konfigurationsoption für diesen spezifischen Git-Befehl und zwingt Git, die Protokollversion 2 für die Kommunikation mit dem entfernten Repository zu verwenden. Protokollversion 2 ist eine neuere Version des Git-Kommunikationsprotokolls, die im Vergleich zur älteren Version 1 verbesserte Leistung oder Funktionen bieten kann.

3.  **`fetch`**
    Der `fetch`-Befehl ruft Updates (wie neue Commits und Branches) von einem entfernten Repository ab. Im Gegensatz zu `pull` führt er diese Änderungen nicht in Ihre lokalen Branches zusammen – er aktualisiert nur Ihre *Remote-Tracking-Branches* (z.B. `origin/main`), damit Sie sehen können, was im Remote-Repository neu ist.

4.  **`--no-tags`**
    Normalerweise ruft `fetch` auch Tags ab (Labels, die bestimmte Commits markieren, wie z.B. Versionsnummern für Releases). Diese Option weist Git an, *keine* Tags vom entfernten Repository abzurufen, wodurch Ihr lokales Repository von diesen Markierungen frei bleibt.

5.  **`--prune`**
    Diese Option räumt Ihre lokalen Remote-Tracking-Branches auf. Wenn ein Branch im entfernten Repository gelöscht wurde, entfernt `--prune` den entsprechenden Remote-Tracking-Branch (z.B. `origin/old-branch`) aus Ihrem lokalen Repository, um die Übersicht zu behalten.

6.  **`--no-recurse-submodules`**
    Submodule sind separate Repositorys, die in Ihrem Haupt-Repository verschachtelt sind. Standardmäßig könnte `fetch` auch Updates für diese Submodule abrufen. Diese Option verhindert das, sodass nur die Daten des Haupt-Repositorys abgerufen werden und alle Submodule ignoriert werden.

7.  **`--depth=5`**
    Diese Option erzeugt einen *flachen Fetch* (shallow fetch), der den Verlauf auf die letzten 5 Commits pro Branch beschränkt. Anstatt den gesamten Commit-Verlauf herunterzuladen, erhalten Sie eine gekürzte Version, die Zeit und Speicherplatz spart – nützlich, wenn Sie den vollständigen Verlauf nicht benötigen.

8.  **`origin`**
    Dies ist der Name des entfernten Repositorys, von dem Sie abrufen. `origin` ist der Standardname, den Git dem Haupt-Remote-Repository gibt, wenn Sie ein Projekt klonen. Dieser Befehl ruft also Updates von dieser Quelle ab.

### Was macht dieser Befehl insgesamt?

Dieser Git-Befehl ruft Updates vom `origin`-Remote-Repository mit mehreren Einschränkungen ab:

-   Er verwendet Protokollversion 2 für die Kommunikation.
-   Er ruft nur die letzten 5 Commits pro Branch ab (`--depth=5`).
-   Er überspringt das Abrufen von Tags (`--no-tags`).
-   Er löscht alle lokalen Remote-Tracking-Branches, die es im Remote-Repository nicht mehr gibt (`--prune`).
-   Er ignoriert Submodules (`--no-recurse-submodules`).

Kurz gesagt, es ist eine leichtgewichtige Methode, um Ihre lokale Sicht auf das Remote-Repository zu aktualisieren, die sich auf recente Änderungen konzentriert und zusätzliche Daten wie Tags, Submodule oder den vollständigen Verlauf vermeidet. Dies könnte verwendet werden, um Bandbreite zu sparen, den Prozess zu beschleunigen oder Ihr lokales Repository minimal zu halten.

### Beispielszenario
Stellen Sie sich vor, Sie arbeiten an einem Projekt mit einem großen Repository und benötigen nur die neuesten Änderungen vom `main`-Branch, um etwas schnell zu überprüfen. Die Ausführung dieses Befehls würde:
-   `origin/main` mit den letzten 5 Commits aktualisieren.
-   Alle veralteten Branches entfernen (z.B. wenn `origin/feature-x` remote gelöscht wurde).
-   Tags und Submodules überspringen, um den Fetch schnell und fokussiert zu halten.

Das war's! Dieser Befehl dreht sich ganz um Effizienz und Kontrolle bei der Synchronisation mit einem entfernten Repository.