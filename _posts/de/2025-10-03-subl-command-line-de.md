---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Verwenden des Subl-Befehlszeilenwerkzeugs
translated: true
type: note
---

### Verwendung des `subl`-Befehls in Sublime Text

Großartige Neuigkeiten – Ihre `subl`-CLI ist bereits installiert und funktioniert (wie durch die `--help`-Ausgabe gezeigt)! Dies ist Sublime Text Build 4200 (eine aktuelle Version), und `subl` ist die offizielle Kommandozeilenschnittstelle zum Öffnen von Dateien, Verzeichnissen und mehr. Sie ist super vielseitig für Entwickler und Power-User.

Ich werde sie mit praktischen Beispielen aufschlüsseln. Führen Sie diese in Ihrem Terminal aus einem beliebigen Verzeichnis aus. Die Kernsyntax lautet:
```
subl [Argumente] [Dateien oder Verzeichnisse]
```

#### 1. **Grundlegende Verwendung: Dateien oder Verzeichnisse öffnen**
- **Das aktuelle Verzeichnis öffnen** (lädt es als Projekt/Ordner in Sublime):
  ```
  subl .
  ```
  - Dies öffnet ein neues Fenster mit den Inhalten des aktuellen Ordners.

- **Eine bestimmte Datei öffnen**:
  ```
  subl myfile.txt
  ```
  - Öffnet `myfile.txt` im Standardfenster (oder einem neuen, wenn gewünscht).

- **Mehrere Dateien/Verzeichnisse öffnen**:
  ```
  subl file1.txt file2.js ~/Documents/myproject/
  ```
  - Öffnet alle in Sublime.

- **An einer bestimmten Zeile/Spalte öffnen** (nützlich, um zu Fehlern zu springen):
  ```
  subl myfile.py:42          # Öffnet in Zeile 42
  subl myfile.py:42:5        # Öffnet in Zeile 42, Spalte 5
  ```

#### 2. **Häufige Argumente (Aus der Hilfe)**
Hier sind die nützlichsten Flags mit Beispielen. Kombinieren Sie sie nach Bedarf (z.B. `subl -n file.txt`).

- **`-n` oder `--new-window`**: Öffnet immer in einem neuen Fenster.
  ```
  subl -n myfile.txt
  ```
  - Praktisch, wenn Sie Ihre bestehenden Sublime-Sitzungen getrennt halten möchten.

- **`-a` oder `--add`**: Fügt Dateien/Ordner zu Ihrem *aktuellen* Sublime-Fenster hinzu (falls es bereits geöffnet ist).
  ```
  subl -a newfolder/
  ```
  - Dies erstellt kein neues Fenster – ideal, um einen Arbeitsbereich aufzubauen.

- **`-w` oder `--wait`**: Wartet, bis Sie die Datei(en) in Sublime geschlossen haben, bevor der Terminalbefehl endet.
  ```
  subl -w myfile.txt
  ```
  - Nützlich in Skripten (z.B. nach dem Ausführen eines Builds, öffnen und auf Überprüfung warten). Impliziert, wenn von stdin gelesen wird.

- **`-b` oder `--background`**: Öffnet, ohne Sublime in den Vordergrund zu bringen (hält Ihren Terminalfokus).
  ```
  subl -b myfile.txt
  ```

- **`-s` oder `--stay`**: Behält den Fokus auf Sublime, nachdem Sie die Datei geschlossen haben (nur relevant mit `-w`).
  ```
  subl -w -s myfile.txt
  ```
  - Verhindert die automatische Rückkehr zum Terminal.

- **`--project <project>`**: Öffnet eine bestimmte Sublime-Projektdatei (`.sublime-project`).
  ```
  subl --project MyProject.sublime-project
  ```
  - Projekte speichern Arbeitsbereiche, Einstellungen usw. Erstellen Sie eines über Datei > Projekt speichern in Sublime.

- **`--command <command>`**: Führt einen Sublime-Befehl aus (z.B. eine Plugin-Aktion), ohne Dateien zu öffnen.
  ```
  subl --command "build"    # Löst den Build-Befehl aus, falls ein Build-System eingerichtet ist
  ```
  - Überprüfen Sie die Sublime-Konsole (Ansicht > Konsole einblenden) auf verfügbare Befehle.

- **`--launch-or-new-window`**: Öffnet nur ein neues Fenster, wenn Sublime nicht bereits läuft.
  ```
  subl --launch-or-new-window .
  ```
  - Effizient für schnelle Überprüfungen, ohne den Bildschirm zu überladen.

- **Stdin-Unterstützung** (pipede Eingabe bearbeiten):
  ```
  echo "Hello World" | subl -   # Öffnet stdin in Sublime zur Bearbeitung
  subl - > output.txt          # Stdin bearbeiten und Änderungen in output.txt speichern
  ```
  - Nach der Bearbeitung in Sublime, speichern und schließen, um fortzufahren.

- **`--safe-mode`**: Startet Sublime ohne Plugins oder benutzerdefinierte Einstellungen (zur Fehlerbehebung).
  ```
  subl --safe-mode myfile.txt
  ```

- **Andere Flags**:
  - `-h` oder `--help`: Zeigt die Hilfe, die Sie bereits gesehen haben.
  - `-v` oder `--version`: Gibt die Version aus (z.B. `subl -v`).

#### 3. **Tipps für den täglichen Gebrauch**
- **Dateien, die mit `-` beginnen**: Wenn ein Dateiname wie ein Flag aussieht (z.B. `-config`), verwenden Sie `--` zur Trennung:
  ```
  subl -- -config.json
  ```
- **Aliase für Bequemlichkeit**: Fügen Sie Ihrem Shell-Profil Verknüpfungen hinzu (`~/.zshrc` für zsh oder `~/.bash_profile` für bash):
  ```
  alias st='subl'     # Kürzerer Alias
  alias stt='subl -n' # Für neue Tabs/Fenster
  ```
  Neu laden mit `source ~/.zshrc`.
- **In Skripten/GIT**: Verwenden Sie es in Hooks oder Aliasen, z.B. `git diff | subl -` um Änderungen zu überprüfen.
- **Vs. `open`**: Jetzt, da `subl` eingerichtet ist, ist es besser als `open -a "Sublime Text"`, da es Zeilen, Projekte und mehr erweiterte Funktionen unterstützt.
- **Fehlerbehebung**:
  - Wenn `subl` nicht mehr funktioniert, führen Sie die Symlink-Installation aus meiner vorherigen Antwort erneut aus.
  - Für große Projekte verwenden Sie `-a`, um mehrere Fenster zu vermeiden.
  - Unter macOS, bei Fokusproblemen, versuchen Sie es zuerst ohne `-b`.

Dies deckt 90% dessen ab, was Sie brauchen werden! Beginnen Sie mit `subl .` in einem Projektordner und experimentieren Sie. Wenn Sie einen spezifischen Workflow oder Fehler haben, teilen Sie mehr Details für maßgeschneiderte Ratschläge.