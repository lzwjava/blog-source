---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Git Clean Befehl Erklärt
translated: true
type: note
---

### Was der Befehl bewirkt
Der Befehl `git clean -f -d` (angenommen, "clean clean" ist ein Tippfehler und Sie meinten `git clean`) entfernt unversionierte Dateien und Verzeichnisse aus Ihrem Git-Arbeitsverzeichnis. Die Flags bedeuten im Einzelnen:
- `-f` (force): Erforderlich, um Dateien tatsächlich zu löschen, da Git sie standardmäßig nicht entfernt, um versehentlichen Datenverlust zu vermeiden.
- `-d` (directories): Erweitert die Bereinigung, um auch unversionierte Verzeichnisse einzubeziehen, nicht nur Dateien.

Sie haben `-fd -f` geschrieben, was `-f -d -f` kombiniert. Da `-f` zweimal vorkommt, ist es redundant, aber harmlos – Flags können ohne Probleme wiederholt werden. Falls Sie etwas anderes gemeint haben, klären Sie es bitte!

### So funktioniert es
Git clean arbeitet auf dem Working Tree (Ihren lokalen Dateien), nicht auf dem Repository selbst. Hier ist eine schrittweise Aufschlüsselung seines Verhaltens:

1.  **Scannt das Arbeitsverzeichnis**: Es identifiziert "unversionierte" Elemente – Dateien/Verzeichnisse, die sich nicht im Git-Index befinden oder von irgendwelchen Commits getrackt werden. Beispiele: Temporäre Dateien wie `*.log`, Build-Artefakte oder leere Verzeichnisse von entfernten Branches.

2.  **Wendet Optionen an**:
    - Ohne `-f` zeigt es nur an, was gelöscht werden würde (Dry-Run-Modus). Mit `-f` führt es die Löschung durch.
    - Ohne `-d` überspringt es Verzeichnisse. Mit `-d` entfernt es leere oder rekursiv leere Verzeichnisse, die unversionierte Dateien enthalten.
    - Es respektiert standardmäßig die `.gitignore`-Datei: Ignorierte Dateien bleiben unberührt, es sei denn, Sie fügen `-x` (eXclude from ignore rules) oder `-X` (nur ignorierte Dateien bereinigen) hinzu.

3.  **Sicherheitsmaßnahmen**: Git warnt, wenn `-f` nicht verwendet wird. Es werden keine Dateien in ignorierten Verzeichnissen entfernt, es sei denn, es wird explizit angewiesen. Führen Sie zuerst `git clean --dry-run -f -d` aus, um eine Vorschau der Änderungen zu sehen.

4.  **Beispiel zur Verwendung**:
    - Zur interaktiven Bereinigung: `git clean -i` (fragt bei jedem Element nach).
    - Typischer Workflow: Nach `git reset` verwenden Sie dies, um exakt Ihrem letzten Commit zu entsprechen.

### Einschränkungen und Nachweis
-   **Risiko**: Das Löschen von Dateien ist ohne Backups oder `git reflog` unwiderruflich. Committen Sie immer zuerst wichtige Arbeit.
-   **Beleg aus der Git-Dokumentation**: Die offizielle Git-Dokumentation (z.B. `man git-clean` oder docs unter git-scm.com) bestätigt dies: `-f` erzwingt die Entfernung, `-d` schließt Verzeichnisse ein. Es verwendet Dateisystemoperationen wie `unlink` und `rmdir`, aber nur auf unversionierten Elementen, um die Beschädigung getrackter Daten zu vermeiden.
-   **Test-Tipp**: Erstellen Sie in einem Mock-Repo eine unversionierte Datei und ein Verzeichnis, führen Sie dann den Befehl aus – beobachten Sie die Ausgabe und die Änderungen im Dateisystem.

Falls dies nicht Ihrer Absicht entspricht, geben Sie bitte mehr Kontext an!