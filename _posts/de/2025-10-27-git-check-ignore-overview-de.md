---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht des Git Check-Ignore Befehls
translated: true
type: note
---

### Was ist `git check-ignore`?

Der Befehl `git check-ignore` ist ein Git-Tool, mit dem überprüft wird, ob eine bestimmte Datei oder ein bestimmter Pfad von den Ignore-Mechanismen von Git ignoriert wird, wie z.B. `.gitignore`-Dateien, `.git/info/exclude` oder globale Ignore-Dateien (über `core.excludesFile`). Es ist besonders nützlich zum Debuggen, warum eine Datei nicht vom Repository verfolgt oder hinzugefügt wird.

Wenn der Pfad ignoriert wird, gibt der Befehl den Pfad aus (und optional das passende Pattern). Wenn er nicht ignoriert wird, gibt es keine Ausgabe (Exit-Code 0). Dies macht es script-freundlich für die Automatisierung.

### Grundlegende Verwendung

Führen Sie ihn mit einem oder mehreren zu überprüfenden Pfaden aus:

```
git check-ignore <Pfadname>...
```

- **Beispiel**: Überprüfen, ob eine einzelne Datei ignoriert wird:
  ```
  git check-ignore pfad/zu/meinedatei.txt
  ```
  - Ausgabe: Wenn ignoriert, wird `pfad/zu/meinedatei.txt` ausgegeben. Wenn nicht, wird nichts ausgegeben.

- **Beispiel**: Mehrere Dateien überprüfen:
  ```
  git check-ignore datei1.txt datei2.txt verzeichnis/datei3.txt
  ```
  - Gibt nur die ignorierten Pfade aus, einen pro Zeile.

### Wichtige Optionen

| Option | Beschreibung | Beispiel |
|--------|-------------|---------|
| `-v`, `--verbose` | Zeigt das Ignore-Pattern an, das übereingestimmt hat (z.B. die Zeile aus `.gitignore`). | `git check-ignore -v pfad/zu/meinedatei.txt`<br>Ausgabe: `pfad/zu/meinedatei.txt: .gitignore:1:*.txt` (Pfad + Datei:Zeile:Pattern) |
| `-q`, `--quiet` | Unterdrückt die Ausgabe, verwendet aber weiterhin den Exit-Code (0 wenn nicht ignoriert, 1 wenn ignoriert). Nützlich in Scripts. | `git check-ignore -q pfad/zu/meinedatei.txt`<br>(Keine Ausgabe; prüfe `$?` für Exit-Code) |
| `--stdin` | Liest Pfade von der Standardeingabe statt von der Kommandozeile. | `echo "datei1.txt\ndatei2.txt" \| git check-ignore --stdin` |
| `--non-matching` | Kehrt die Ausgabe um: Zeigt Pfade an, die *nicht* ignoriert werden. | `git check-ignore --non-matching -v datei1.txt datei2.txt` |

### Häufige Anwendungsfälle

1. **Debuggen von `.gitignore`-Regeln**:
   - Wenn `git status` eine Datei nicht anzeigt, die Sie erwarten, führen Sie `git check-ignore -v <Datei>` aus, um genau zu sehen, welche Regel sie ignoriert.
   - Beispielausgabe: `src/logs/app.log: .gitignore:5:logs/*` (zeigt an, dass Zeile 5 in `.gitignore` übereinstimmt).

2. **In Scripts**:
   - Überprüfen, ob eine Datei hinzugefügt werden sollte:
     ```
     if git check-ignore -q meinedatei.txt; then
         echo "Datei wird ignoriert, überspringe..."
     else
         git add meinedatei.txt
     fi
     ```

3. **Stapelverarbeitung (Batch Checking)**:
   - Liste aller ignorierten Dateien in einem Verzeichnis:
     ```
     find . -type f -print0 | xargs -0 git check-ignore
     ```

### Tipps
- Es respektiert den Git-Ignore-Stack: lokale `.gitignore`, globale Excludes, etc.
- Funktioniert mit unverfolgten Dateien oder solchen, die bereits im Repo sind (prüft aber gegen Ignore-Regeln).
- Für weitere Details siehe die offizielle Dokumentation.

[Git check-ignore Dokumentation](https://git-scm.com/docs/git-check-ignore)  
[Stack Overflow: Git command to show which specific files are ignored](https://stackoverflow.com/questions/466764/git-command-to-show-which-specific-files-ignored-by-gitignore)  
[Using git check-ignore to debug your .gitignore](https://alexwlchan.net/til/2020/using-git-check-ignore-to-debug-your-gitignore/)