---
audio: false
generated: true
lang: de
layout: post
title: Stufenänderungen im Pre-Commit Hook
translated: true
type: note
---

Um die Änderungen des `update_notes_link.py`-Skripts in den aktuellen Commit zu integrieren (anstatt einen separaten Commit zu erstellen) während eines Pre-Commit-Hooks, müssen Sie den Hook so ändern, dass er die aktualisierten Dateien staged, ohne sie separat zu committen. Auf diese Weise werden die Änderungen aus dem Python-Skript in den Commit des Benutzers aufgenommen. Im Folgenden finden Sie ein überarbeitetes Pre-Commit-Hook-Skript, das dies erreicht.

### Wichtige Änderungen
- **Kein separater Commit**: Anstatt `git commit` im Hook auszuführen, staged das Skript nur die aktualisierten Dateien (`git add`), sodass sie im Commit des Benutzers enthalten sind.
- **Commit-Nachricht des Benutzers beibehalten**: Der Hook erstellt keinen neuen Commit, sodass die ursprüngliche Commit-Nachricht des Benutzers verwendet wird.
- **Fehlerbehandlung**: Wenn das Python-Skript fehlschlägt, beendet sich der Hook mit einem Exit-Status ungleich Null, um den Commit zu verhindern.

### Pre-Commit-Hook-Skript

Hier ist das aktualisierte Pre-Commit-Hook-Skript, das Änderungen staged, ohne einen separaten Commit zu erstellen:

```x-shellscript
#!/bin/bash

# Führe das update_notes_link.py-Skript aus und erfasse seine Ausgabe
OUTPUT=$(python scripts/generate/update_notes_link.py 2>&1)
EXIT_CODE=$?

# Prüfe, ob das Python-Skript erfolgreich ausgeführt wurde
if [ $EXIT_CODE -ne 0 ]; then
    echo "Fehler: update_notes_link.py schlug fehl mit Exit-Code $EXIT_CODE"
    echo "$OUTPUT"
    exit 1
fi

# Prüfe, ob die spezifische Datei aktualisiert wurde
if echo "$OUTPUT" | grep -q "Updated original/2025-01-11-notes-en.md"; then
    echo "Notes-Links wurden aktualisiert, stufe Änderungen für den aktuellen Commit vor."

    # Stage die relevanten Dateien
    git add original/2025-01-11-notes-en.md
    git add _posts/en/*.md

    # Verifiziere, dass Dateien gestaged wurden
    if ! git diff --cached --quiet; then
        echo "Änderungen erfolgreich vorbereitet (staged)."
    else
        echo "Keine Änderungen zum Stagen vorhanden."
    fi
else
    echo "Keine Aktualisierungen für original/2025-01-11-notes-en.md, keine zusätzlichen Dateien gestaged."
fi

# Beende mit Erfolg, damit der Commit fortgesetzt werden kann
exit 0
```

### Erklärung des Skripts

- **Shebang (`#!/bin/bash`)**: Stellt sicher, dass das Skript in einer Bash-Shell läuft.
- **Python-Skript ausführen**: Führt `python scripts/generate/update_notes_link.py` aus und erfasst seine Ausgabe und Exit-Code.
- **Fehlerbehandlung**: Prüft den Exit-Code (`$EXIT_CODE`) des Python-Skripts. Wenn er ungleich Null ist, schlägt der Hook fehl, gibt den Fehler aus und stoppt den Commit.
- **Ausgabe prüfen**: Verwendet `grep`, um zu prüfen, ob die Ausgabe anzeigt, dass `original/2025-01-11-notes-en.md` aktualisiert wurde.
- **Dateien stagen**: Führt `git add` für die angegebenen Dateien (`original/2025-01-11-notes-en.md` und `_posts/en/*.md`) aus, um sie in den Commit des Benutzers aufzunehmen.
- **Kein Commit**: Überspringt `git commit`, sodass der `git commit`-Befehl des Benutzers die gestagten Änderungen mit der ursprünglichen Commit-Nachricht enthält.
- **Rückmeldung**: Gibt Meldungen aus, um den Benutzer zu informieren, ob Änderungen gestaged wurden.
- **Exit-Code**: Beendet mit `0`, um den Commit fortzusetzen, es sei denn, das Python-Skript schlägt fehl.

### Einrichten des Hooks

1. **Hook erstellen**:
   - Platzieren Sie das Skript in `.git/hooks/pre-commit` in Ihrem Repository.

2. **Ausführbar machen**:
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

3. **Hook testen**:
   - Modifizieren Sie eine Datei oder stellen Sie sicher, dass das Python-Skript `original/2025-01-11-notes-en.md` aktualisieren wird.
   - Führen Sie `git commit -m "Ihre Commit-Nachricht"` aus.
   - Verifizieren Sie, dass die aktualisierten Dateien im Commit enthalten sind, indem Sie `git diff --cached` vor dem Commit oder `git show` nach dem Commit prüfen.

### Verwendung des `pre-commit`-Framework (Optional)

Wenn Sie das `pre-commit`-Framework bevorzugen, können Sie die gleiche Logik in einer `.pre-commit-config.yaml`-Datei definieren. Dieser Ansatz ist portabler und erlaubt es Ihnen, festzulegen, welche Dateien den Hook auslösen.

1. **pre-commit installieren**:
   ```bash
   pip install pre-commit
   ```

2. **`.pre-commit-config.yaml` erstellen**:

```yaml
repos:
- repo: local
  hooks:
  - id: update-notes-links
    name: Update Notes Links
    entry: bash -c '
      OUTPUT=$(python scripts/generate/update_notes_link.py 2>&1);
      EXIT_CODE=$?;
      if [ $EXIT_CODE -ne 0 ]; then
        echo "Error: update_notes_link.py failed with exit code $EXIT_CODE";
        echo "$OUTPUT";
        exit 1;
      fi;
      if echo "$OUTPUT" | grep -q "Updated original/2025-01-11-notes-en.md"; then
        echo "Notes links updated, staging changes for the current commit.";
        git add original/2025-01-11-notes-en.md;
        git add _posts/en/*.md;
        if ! git diff --cached --quiet; then
          echo "Changes staged successfully.";
        else
          echo "No changes to stage.";
        fi;
      else
        echo "No updates to original/2025-01-11-notes-en.md, no additional files staged.";
      fi'
    language: script
    files: ^(original/2025-01-11-notes-en\.md|_posts/en/.*\.md)$
    stages: [commit]
```

3. **Hook installieren**:
   ```bash
   pre-commit install
   ```

4. **Hook testen**:
   - Committen Sie Änderungen an Dateien, die auf den `files`-Regex passen (z.B. `original/2025-01-11-notes-en.md` oder `_posts/en/*.md`).
   - Verifizieren Sie, dass der Hook läuft, Änderungen staged, falls zutreffend, und sie in Ihren Commit aufnimmt.

### Wichtige Unterschiede zum ursprünglichen GitHub Actions Workflow

- **Kein separater Commit**: Im Gegensatz zum GitHub Actions Workflow, der einen neuen Commit erstellte, staged dieser Hook Änderungen für den aktuellen Commit des Benutzers.
- **Kein Push**: Der Hook pushed keine Änderungen, da Pre-Commit-Hooks lokal ausgeführt werden, bevor der Commit finalisiert wird. Der Benutzer muss `git push` manuell ausführen.
- **Fehlerbehandlung**: Der Hook prüft den Exit-Code des Python-Skripts, um sicherzustellen, dass es nicht stillschweigend fehlschlägt.
- **Keine Git-Benutzerkonfiguration**: Das Skript lässt `git config user.name` und `user.email` weg, da die Git-Konfiguration des Benutzers für den Commit verwendet wird.

### Hinweise

- **Python-Skript**: Stellen Sie sicher, dass `scripts/generate/update_notes_link.py` lokal existiert und ausführbar ist. Wenn es auf Umgebungsvariablen oder Abhängigkeiten angewiesen ist, stellen Sie sicher, dass diese verfügbar sind.
- **Dateipfade**: Verifizieren Sie, dass die Pfade `original/2025-01-11-notes-en.md` und `_posts/en/*.md` Ihrer Repository-Struktur entsprechen.
- **Hook-Fehler**: Wenn das Python-Skript fehlschlägt, verhindert der Hook den Commit, um sicherzustellen, dass keine teilweisen Aktualisierungen gestaged werden.
- **Testen**: Testen Sie mit `git commit`, um zu bestätigen, dass Änderungen gestaged und im Commit enthalten sind, ohne einen zusätzlichen Commit zu erstellen. Verwenden Sie `git show`, um die Commit-Inhalte zu überprüfen.

### Verifikation

Zur Verifikation:
1. Modifizieren Sie eine Datei oder stellen Sie sicher, dass das Python-Skript `original/2025-01-11-notes-en.md` aktualisiert.
2. Führen Sie `git commit -m "Test-Commit"` aus.
3. Prüfen Sie `git show`, um zu bestätigen, dass die aktualisierten Dateien im Commit mit Ihrer ursprünglichen Nachricht enthalten sind.
4. Stellen Sie sicher, dass keine zusätzlichen Commits erstellt werden (z.B. kein `chore(notes): Update notes links` Commit).

Wenn Sie weitere Anpassungen benötigen, wie z.B. die Behandlung spezifischer Fehlerfälle oder das Hinzufügen weiterer Dateien zum Stagen, lassen Sie es mich wissen!