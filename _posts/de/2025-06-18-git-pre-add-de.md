---
audio: false
generated: true
lang: de
layout: post
title: Erstellen von Git Pre-Add Hook Alternativen
translated: true
type: note
---

Git verfügt nicht über einen integrierten `pre-add`-Hook, aber es gibt mehrere Möglichkeiten, ähnliche Funktionalität zu erreichen. Hier sind einige Ansätze:

### 1. **Git Aliases (Empfohlener Ansatz)**
Sie können einen Git-Alias erstellen, der Ihre Prüfungen ausführt, bevor `git add` aufgerufen wird:

```bash
git config --global alias.safe-add '!your-pre-add-script.sh && git add'
```

Verwenden Sie dann `git safe-add` anstelle von `git add`.

### 2. **Wrapper Script**
Erstellen Sie ein Skript namens `git-pre-add` in Ihrem PATH, das:
1. Ihre Pre-Add-Prüfungen ausführt
2. `git add` aufruft, wenn die Prüfungen bestanden werden

```bash
#!/bin/bash
# Ihre Pre-Add-Validierungslogik hier
if [ some_condition ]; then
  git add "$@"
else
  echo "Pre-add checks failed"
  exit 1
fi
```

### 3. **Verwendung vorhandener Hooks**
Sie könnten vorhandene Hooks auf kreative Weise nutzen:
- **pre-commit**: Dieser Hook läuft zwar nach `add`, aber vor `commit`. Hier könnten Sie die staged-Dateien prüfen.
- **prepare-commit-msg**: Ähnlich wie pre-commit, aber früher im Prozess.

### 4. **Filesystem Monitoring**
Für fortgeschrittene Anforderungen könnten Sie verwenden:
- **inotifywait** (Linux), um Ihr Arbeitsverzeichnis zu überwachen
- **fswatch** (Mac) für ähnliche Funktionalität

### Beispielskript für eine Pre-Add-Prüfung
Hier ist ein einfaches Beispiel, das das Hinzufügen von Dateien mit nachgestellten Leerzeichen verhindert:

```bash
#!/bin/bash
# .git/hooks/pre-commit (funktioniert aber mit staged-Dateien)

# Auf Leerzeichenfehler prüfen
if git diff --cached --check; then
  exit 0
else
  echo "Found whitespace errors in staged files"
  exit 1
fi
```

Denken Sie daran, alle Hook-Skripte ausführbar zu machen (`chmod +x script.sh`).