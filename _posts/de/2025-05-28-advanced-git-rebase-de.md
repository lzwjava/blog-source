---
audio: false
generated: true
lang: de
layout: post
title: 'Fortgeschrittenes Git: Rebase, Merge, Konfliktlösung, Squash'
translated: true
type: note
---

Diese Anleitung behandelt die fortgeschrittene Verwendung von `git rebase` und `git merge`, das Auflösen von Konflikten, die Verwendung der `ours`- und `theirs`-Strategien sowie das Squashen von Commits. Ich werde präzise Erklärungen und praktische Beispiele für jedes Thema liefern, wobei der Fokus auf fortgeschrittenen Workflows liegt, die Vertrautheit mit grundlegenden Git-Befehlen voraussetzen.

## 1. Git Merge: Fortgeschrittene Verwendung
`git merge` kombiniert mehrere Entwicklungsstränge zu einer einzigen, vereinheitlichten Historie. Die fortgeschrittene Verwendung umfasst das Handhaben komplexer Merges, die Verwendung von Merge-Strategien und die Verwaltung von Merge-Commits.

### Wichtige Merge-Strategien
- **Recursive (Standard)**: Verarbeitet mehrere gemeinsame Vorgänger und ist für die meisten Merges geeignet.
  - Beispiel: `git merge --strategy=recursive branch-name`
- **Ours**: Behält die Änderungen des aktuellen Branches bei und verwirft die Änderungen des gemergten Branches.
  - Beispiel: `git merge --strategy=ours feature-branch`
- **Theirs**: Keine echte Strategie, kann aber emuliert werden (siehe unten bei der Konfliktlösung).
- **Octopus**: Mergt mehrere Branches gleichzeitig (verwendet für >2 Branches).
  - Beispiel: `git merge branch1 branch2 branch3`

### Fortgeschrittene Merge-Optionen
- `--no-ff`: Erzwingt einen Merge-Commit, selbst wenn ein Fast-Forward möglich ist, und bewahrt so die Branch-Historie.
  - Beispiel: `git merge --no-ff feature-branch`
- `--squash`: Kombiniert alle Commits des gemergten Branches zu einem einzelnen Commit im aktuellen Branch.
  - Beispiel: `git merge --squash feature-branch && git commit`
- `--allow-unrelated-histories**: Mergt Branches ohne gemeinsame Historie.
  - Beispiel: `git merge --allow-unrelated-histories external-repo-branch`

### Beispiel: Merge ohne Fast-Forward
```bash
git checkout main
git merge --no-ff feature-branch
# Erstellt einen Merge-Commit und bewahrt die feature-branch-Historie
```

## 2. Git Rebase: Fortgeschrittene Verwendung
`git rebase` schreibt die Historie um, indem Commits verschoben oder modifiziert werden, um eine lineare Historie zu erstellen. Es ist mächtig zum Bereinigen von Branches, verändert aber die Historie. Daher ist Vorsicht bei gemeinsamen Branches geboten.

### Arten von Rebase
- **Standard Rebase**: Spielt die Commits des aktuellen Branches auf den Basis-Branch neu ab.
  - Beispiel: `git rebase main` (während man auf `feature-branch` ist)
- **Interaktiver Rebase**: Ermöglicht das Bearbeiten, Squashen oder Neusortieren von Commits.
  - Beispiel: `git rebase -i main`

### Befehle für den interaktiven Rebase
Führe `git rebase -i <base>` aus (z.B. `git rebase -i HEAD~3` für die letzten 3 Commits). Dies öffnet einen Editor mit Befehlen wie:
- `pick`: Behält den Commit unverändert bei.
- `reword`: Bearbeitet die Commit-Nachricht.
- `edit`: Unterbricht den Rebase, um den Commit zu ändern.
- `squash`: Kombiniert mit dem vorherigen Commit.
- `fixup`: Wie squash, verwirft aber die Commit-Nachricht.
- `drop`: Entfernt den Commit.

### Beispiel: Interaktiver Rebase
Um die letzten 3 Commits zu squashen:
```bash
git rebase -i HEAD~3
# Im Editor "pick" zu "squash" oder "fixup" für die zu kombinierenden Commits ändern
# Speichern und schließen, um abzuschließen
```

### Rebase auf eine andere Basis
Um einen Branch auf eine neue Basis zu verschieben (z.B. `feature-branch` von `old-base` auf `main`):
```bash
git rebase --onto main old-base feature-branch
```

### Rebase mit Merge-Commits
Standardmäßig glättet Rebase Merge-Commits. Um sie zu bewahren:
```bash
git rebase -i --preserve-merges main
```

### Rebase abbrechen
Wenn etwas schiefgeht:
```bash
git rebase --abort
```

## 3. Auflösen von Merge-/Rebase-Konflikten
Konflikte treten auf, wenn Git Änderungen nicht automatisch in Einklang bringen kann. Sowohl `merge` als auch `rebase` können zu Konflikten führen, die ähnlich gelöst werden.

### Schritte zur Konfliktlösung
1. **Konflikte identifizieren**: Git hält an und listet die Dateien mit Konflikten auf.
   - Für Merge: `git status` zeigt Dateien mit Konflikten an.
   - Für Rebase: Konflikte werden Commit-für-Commit während `git rebase -i` aufgelöst.
2. **Konfliktdateien bearbeiten**: Dateien öffnen und nach Konfliktmarkierungen suchen:
   ```text
   <<<<<<< HEAD
   Ihre Änderungen
   =======
   Eingehende Änderungen
   >>>>>>> branch-name
   ```
   Manuell bearbeiten, um die gewünschten Änderungen zu behalten, dann Markierungen entfernen.
3. **Als gelöst markieren**:
   - Für Merge: `git add <datei>`
   - Für Rebase: `git add <datei>`, dann `git rebase --continue`
4. **Prozess abschließen**:
   - Merge: `git commit` (Git kann automatisch eine Commit-Nachricht generieren).
   - Rebase: `git rebase --continue` bis alle Commits angewendet sind.

### Beispiel: Einen Merge-Konflikt auflösen
```bash
git checkout main
git merge feature-branch
# Konflikt tritt auf
git status  # Listet konfliktbehaftete Dateien auf
# Dateien bearbeiten, um Konflikte zu lösen
git add resolved-file.txt
git commit  # Merge finalisieren
```

### Beispiel: Einen Rebase-Konflikt auflösen
```bash
git checkout feature-branch
git rebase main
# Konflikt tritt auf
# Konfliktdateien bearbeiten
git add resolved-file.txt
git rebase --continue
# Wiederholen, bis der Rebase abgeschlossen ist
```

## 4. Verwendung von Ours und Theirs bei der Konfliktlösung
Während Konflikten möchten Sie möglicherweise die Änderungen einer Seite bevorzugen (`ours` oder `theirs`). Die Bedeutung von `ours` und `theirs` hängt vom Vorgang ab.

### Merge: Ours vs. Theirs
- `ours`: Änderungen vom aktuellen Branch (z.B. `main`).
- `theirs`: Änderungen vom Branch, der gemergt wird (z.B. `feature-branch`).
- Verwenden Sie die `--strategy-option` (`-X`):
  - `ours` behalten: `git merge -X ours feature-branch`
  - `theirs` behalten: `git merge -X theirs feature-branch`

### Rebase: Ours vs. Theirs
- `ours`: Änderungen vom Basis-Branch (z.B. `main`).
- `theirs`: Änderungen vom Branch, der rebased wird (z.B. `feature-branch`).
- Verwendung während der Rebase-Konfliktlösung:
  ```bash
  git checkout --ours file.txt  # Version des Basis-Branches behalten
  git checkout --theirs file.txt  # Version des rebased Branches behalten
  git add file.txt
  git rebase --continue
  ```

### Beispiel: Merge mit Theirs
Um `feature-branch` in `main` zu mergen und die Änderungen von `feature-branch` zu bevorzugen:
```bash
git checkout main
git merge -X theirs feature-branch
```

### Beispiel: Rebase mit Ours
Während des Rebase von `feature-branch` auf `main`, einen Konflikt durch Behalten der Version von `main` lösen:
```bash
git checkout feature-branch
git rebase main
# Konflikt tritt auf
git checkout --ours file.txt
git add file.txt
git rebase --continue
```

## 5. Squashen von Commits
Squashing kombiniert mehrere Commits zu einem, was eine sauberere Historie erzeugt. Dies wird typischerweise mit interaktivem Rebase durchgeführt.

### Schritte zum Squashen von Commits
1. Starten Sie einen interaktiven Rebase für die gewünschten Commits:
   ```bash
   git rebase -i HEAD~n  # n = Anzahl der zu squashenden Commits
   ```
2. Im Editor `pick` zu `squash` (oder `fixup`) für die Commits ändern, die in den vorherigen Commit kombiniert werden sollen.
3. Speichern und schließen. Git fordert möglicherweise zur Bearbeitung der Commit-Nachricht für den kombinierten Commit auf.
4. Die aktualisierte Historie pushen (Force-Push, falls bereits geteilt):
   ```bash
   git push --force-with-lease
   ```

### Beispiel: 3 Commits squashen
```bash
git rebase -i HEAD~3
# Editor zeigt:
# pick abc123 Commit 1
# pick def456 Commit 2
# pick ghi789 Commit 3
# Ändern zu:
# pick abc123 Commit 1
# squash def456 Commit 2
# squash ghi789 Commit 3
# Speichern und schließen
# Kombinierte Commit-Nachricht bearbeiten, wenn aufgefordert
git push --force-with-lease
```

### Squashen während eines Merges
Um alle Commits eines Branches während eines Merges zu squashen:
```bash
git checkout main
git merge --squash feature-branch
git commit  # Einen einzelnen Commit erstellen
```

## Best Practices und Tipps
- **Backup vor Rebase**: Rebase schreibt die Historie um. Erstellen Sie einen Backup-Branch:
  ```bash
  git branch backup-branch
  ```
- **Rebase gemeinsamer Branches vermeiden**: Das Umschreiben der Historie auf öffentlichen Branches kann Probleme für Mitwirkende verursachen. Verwenden Sie stattdessen `merge`.
- **`--force-with-lease` für Sicherheit verwenden**: Verhindert das Überschreiben von Änderungen anderer, wenn eine umgeschriebene Historie gepusht wird.
- **Nach Konfliktlösung testen**: Stellen Sie sicher, dass Ihr Projekt nach dem Lösen von Konflikten baut und Tests bestehen.
- **Tools für Konflikte verwenden**: GUI-Tools wie VS Code, SourceTree oder `git mergetool` können die Konfliktlösung vereinfachen.
- **Mit dem Team kommunizieren**: Wenn Sie in einem Team arbeiten, koordinieren Sie Rebases, um Konflikte zu vermeiden.

## Häufige Fallstricke
- **Verlust von Arbeit während Rebase**: Immer ein Backup erstellen oder `git reflog` verwenden, um verlorene Commits wiederherzustellen.
- **Falsche Verwendung von Ours/Theirs**: Überprüfen Sie doppelt, welcher Branch `ours` vs. `theirs` im Merge- vs. Rebase-Kontext ist.
- **Force-Push ohne Absprache**: Force-Pushing gemeinsamer Branches kann Teammitglieder stören. Verwenden Sie `--force-with-lease` und kommunizieren Sie.

## Wiederherstellung nach Fehlern
- **Historie anzeigen**: Verwenden Sie `git reflog`, um vorherige Zustände zu sehen und verlorene Commits wiederherzustellen:
  ```bash
  git reflog
  git checkout <commit-hash>
  ```
- **Auf Zustand vor Merge zurücksetzen**:
  ```bash
  git reset --hard HEAD^  # Letzten Merge-Commit rückgängig machen
  ```
- **Merge abbrechen**: Wenn ein Merge schiefläuft:
  ```bash
  git merge --abort
  ```

Diese Anleitung bietet eine solide Grundlage für fortgeschrittene Git-Workflows. Für spezifische Szenarien oder Fehler lassen Sie es mich wissen, dann kann ich tiefer graben oder nach Echtzeit-Lösungen suchen!