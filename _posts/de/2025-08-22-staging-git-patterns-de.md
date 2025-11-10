---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Staging von Dateien mit Git-Mustern
translated: true
type: note
---

### Staging von Dateien mit Mustern in Git

Der Befehl `git add` in Git akzeptiert Dateipfade und Glob-Muster (wie `*.java`), um passende Dateien zur Staging-Area hinzuzufügen. Sie können mehrere `git add`-Befehle ausführen, um verschiedene Dateigruppen zu stagen und sie dann separat zu committen. Dies ermöglicht ein selektives Staging für gruppierte Commits (z.B. einen für Java-Dateien, einen anderen für den Rest).

#### Grundlegendes Beispiel: Zuerst Java-Dateien stagen und committen
1. **Alle .java-Dateien stagen**:
   ```bash
   git add "*.java"
   ```
   - Dies staged alle unversionierten oder geänderten Dateien mit der Endung `.java` im aktuellen Verzeichnis und in Unterverzeichnissen.
   - Verwenden Sie doppelte Anführungszeichen (`"`), um Probleme mit der Shell-Erweiterung auf vielen Systemen (z.B. Bash) zu vermeiden.

2. **Die gestagten Java-Dateien committen**:
   ```bash
   git commit -m "Java-Dateien hinzufügen"
   ```
   - Dies committed nur die gestagten Dateien (die Java-Dateien).

3. **Alles andere stagen**:
   ```bash
   git add .
   ```
   - Dies staged alle verbleibenden unversionierten/geänderten Dateien (einschließlich der Inhalte des aktuellen Verzeichnisses).

4. **Die verbleibenden Dateien committen**:
   ```bash
   git commit -m "Andere Dateien hinzufügen"
   ```

- **Hinweise**:
  - Nach dem ersten Commit wird `git add .` bereits committete Dateien nicht erneut stagen; es betrifft nur ungestagte Änderungen.
  - Überprüfen Sie mit `git status` nach jedem Add-Befehl, was gestaged ist.
  - Bei verschachtelten Verzeichnissen erfasst `*.java` Dateien in jeder Tiefe.

#### Umgang mit Ausschlüssen oder weiteren Mustern
Falls Sie etwas wie das Einschließen von `*.java` bei gleichzeitigem Ausschluss anderer Dateien in einem einzigen Schritt beabsichtigen, unterstützt `git add` keine direkten Negationen wie `"!*.java"`. (Ihre Beispielsyntax `"!*.java"` ist in Git-Befehlen nicht gültig.) Verwenden Sie stattdessen mehrere `git add`-Aufrufe wie oben, oder:

- Verwenden Sie spezifische Pfade: `git add datei1.txt datei2.md` für eine manuelle Auswahl.
- Für erweiterten Ausschluss: Verwenden Sie temporär eine `.gitignore`-Datei, um Dateien zu verbergen, fügen Sie hinzu, was Sie wollen, und stellen Sie dann die `.gitignore` wieder her. Oder verwenden Sie `git add -A` (fügt alles hinzu), kombinieren Sie es aber mit selektivem Staging.
- Interaktives Hinzufügen: `git add -p` für hunk-weises Staging.
- Zur Vorschau von Änderungen: `git add --dry-run "*.java"` zeigt, was gestaged werden würde, ohne es tatsächlich durchzuführen.

#### Tipps für separate Commits
- Überprüfen Sie Änderungen immer mit `git diff --cached` vor einem Commit.
- Für größere Repositories ziehen Sie `git add --all` oder `git add -A` in Betracht, um alle Änderungen auf einmal zu stagen, und stagen Sie bei Bedarf selektiv mit `git reset HEAD <Datei>` zurück.
- Falls Muster nicht funktionieren, stellen Sie sicher, dass Anführungszeichen verwendet werden und Ihre Shell Globs unterstützt (z.B. unter Windows Git Bash verwenden). Für Groß-/Kleinschreibung beachtet Git die Einstellung Ihres Systems (siehe `core.ignorecase`).

Falls dies nicht Ihrer Absicht entspricht (z.B. wenn Sie Ausschlussmuster wie in `.gitignore` meinten), geben Sie bitte weitere Details an!