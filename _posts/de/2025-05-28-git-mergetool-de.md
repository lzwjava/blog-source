---
audio: false
generated: true
lang: de
layout: post
title: Konfiguration von TortoiseGit als Git-Merge-Tool
translated: true
type: note
---

Um TortoiseGit als Merge-Tool für Git zu konfigurieren, müssen Sie TortoiseGitMerge (das in TortoiseGit enthaltene Merge-Tool) in Ihrer Git-Konfiguration einrichten. Nachfolgend sind die Schritte dazu aufgeführt:

### Voraussetzungen
- Stellen Sie sicher, dass TortoiseGit auf Ihrem System installiert ist. Sie können es von [tortoisegit.org](https://tortoisegit.org) herunterladen.
- Vergewissern Sie sich, dass die TortoiseGitMerge ausführbare Datei verfügbar ist (typischerweise unter `C:\Program Files\TortoiseGit\bin\TortoiseGitMerge.exe`).

### Schritte zur Konfiguration von TortoiseGitMerge als Git Mergetool

1. **Öffnen Sie eine Eingabeaufforderung oder Git Bash**
   - Sie können die Windows-Eingabeaufforderung, PowerShell oder Git Bash verwenden, um die notwendigen Git-Konfigurationsbefehle auszuführen.

2. **Setzen Sie TortoiseGitMerge als Merge-Tool**
   Führen Sie die folgenden Befehle aus, um Git für die Verwendung von TortoiseGitMerge zu konfigurieren:

   ```bash
   git config --global merge.tool tortoisegitmerge
   git config --global mergetool.tortoisemerge.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -base:\"$BASE\" -theirs:\"$REMOTE\" -mine:\"$LOCAL\" -merged:\"$MERGED\""
   ```

   **Erklärung**:
   - `merge.tool tortoisegitmerge`: Setzt den Namen des Merge-Tools auf `tortoisegitmerge` (Sie können einen beliebigen Namen wählen, aber dies ist eine Konvention).
   - `mergetool.tortoisemerge.cmd`: Spezifiziert den Befehl zum Ausführen von TortoiseGitMerge mit den entsprechenden Parametern:
     - `-base:"$BASE"`: Die gemeinsame Ursprungsdatei.
     - `-theirs:"$REMOTE"`: Die Datei aus dem Branch, der gemergt wird.
     - `-mine:"$LOCAL"`: Die Datei aus Ihrem aktuellen Branch.
     - `-merged:"$MERGED"`: Die Ausgabedatei, in der der aufgelöste Merge gespeichert wird.
   - Verwenden Sie Schrägstriche (`/`) im Pfad und setzen Sie Anführungszeichen bei Bedarf, insbesondere wenn der Pfad Leerzeichen enthält.

   **Hinweis**: Passen Sie den Pfad (`C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe`) an, wenn TortoiseGit an einem anderen Ort installiert ist (z.B. `E:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe`).

3. **Optional: Deaktivieren Sie die Mergetool-Abfrage**
   Um zu vermeiden, dass Sie jedes Mal, wenn Sie `git mergetool` ausführen, gefragt werden, können Sie die Abfrage deaktivieren:

   ```bash
   git config --global mergetool.prompt false
   ```

4. **Optional: Stellen Sie sicher, dass TortoiseGitMerge im System-PATH ist**
   Falls Git TortoiseGitMerge nicht finden kann, stellen Sie sicher, dass dessen Verzeichnis in Ihrer PATH-Umgebungsvariable des Systems enthalten ist:
   - Klicken Sie mit der rechten Maustaste auf "Dieser PC" oder "Arbeitsplatz" → Eigenschaften → Erweiterte Systemeinstellungen → Umgebungsvariablen.
   - Suchen Sie unter "Systemvariablen" die Variable `Path` und bearbeiten Sie sie, um `C:\Program Files\TortoiseGit\bin` einzuschließen.
   - Alternativ können Sie den Pfad explizit in der Git-Konfiguration setzen:

     ```bash
     git config --global mergetool.tortoisemerge.path "C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe"
     ```

5. **Testen Sie die Konfiguration**
   - Erzeugen Sie einen Merge-Konflikt in einem Git-Repository (z.B. durch das Zusammenführen zweier Branches mit konfligierenden Änderungen).
   - Führen Sie den folgenden Befehl aus, um das Merge-Tool zu starten:

     ```bash
     git mergetool
     ```

   - TortoiseGitMerge sollte sich öffnen und eine Drei-Spalten-Ansicht mit der Basis-, Theirs- und Mine-Version der konfligierenden Datei anzeigen. Der untere Bereich ist das zusammengeführte Ergebnis.

6. **Lösen Sie Konflikte in TortoiseGitMerge**
   - In der Drei-Spalten-Ansicht zeigt TortoiseGitMerge:
     - **Linker Bereich**: Die "Theirs"-Version (vom Branch, der gemergt wird).
     - **Rechter Bereich**: Die "Mine"-Version (von Ihrem aktuellen Branch).
     - **Mittlerer Bereich**: Die Basis- (gemeinsame Ursprungs-) Version.
     - **Unterer Bereich**: Das zusammengeführte Ergebnis, in dem Sie Konflikte auflösen.
   - Klicken Sie mit der rechten Maustaste auf konfligierende Abschnitte, um Optionen wie "Use text block from 'theirs'", "Use text block from 'mine'" zu wählen oder die zusammengeführte Datei manuell zu bearbeiten.
   - Sobald der Konflikt aufgelöst ist, speichern Sie die Datei (Datei → Speichern) und schließen Sie TortoiseGitMerge.
   - Git markiert die Datei als aufgelöst, wenn TortoiseGitMerge erfolgreich beendet wird (Exit-Code 0). Bestätigen Sie gegebenenfalls, dass der Konflikt als aufgelöst markiert werden soll.

7. **Committen Sie den aufgelösten Merge**
   Nach dem Auflösen der Konflikte committen Sie die Änderungen:

   ```bash
   git commit
   ```

   **Hinweis**: Wenn der Konflikt während eines Rebases oder Cherry-Picks aufgetreten ist, verwenden Sie die jeweiligen TortoiseGit-Dialoge (Rebase oder Cherry-pick), um den Prozess fortzusetzen, anstatt den standardmäßigen Commit-Dialog.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)

### Verwendung von TortoiseGitMerge über die TortoiseGit GUI
Wenn Sie es bevorzugen, die TortoiseGit GUI zum Auflösen von Konflikten zu verwenden:
1. Klicken Sie mit der rechten Maustaste auf die konfligierende Datei im Windows-Explorer.
2. Wählen Sie **TortoiseGit → Edit Conflicts**.
3. TortoiseGitMerge wird geöffnet, und Sie können Konflikte wie oben beschrieben auflösen.
4. Nach dem Speichern klicken Sie erneut mit der rechten Maustaste und wählen **TortoiseGit → Resolved**, um die Datei als aufgelöst zu markieren.
5. Committen Sie die Änderungen über den Commit-Dialog von TortoiseGit.

### Fehlerbehebung
- **Fehler: "Unsupported merge tool 'tortoisemerge'"**
  - Stellen Sie sicher, dass der Pfad zu `TortoiseGitMerge.exe` korrekt und zugänglich ist.
  - Vergewissern Sie sich, dass der Tool-Name in den Konfigurationen `merge.tool` und `mergetool.<tool>.cmd` exakt übereinstimmt.
  - Prüfen Sie, ob TortoiseGitMerge im PATH liegt oder explizit mit `mergetool.tortoisemerge.path` gesetzt ist.[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **Leerzeichen in Dateipfaden**
  - Wenn Dateipfade Leerzeichen enthalten, sollte die Befehlssyntax mit escaped Anführungszeichen (wie oben gezeigt) diese korrekt behandeln.[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **Cygwin-Benutzer**
  - Wenn Sie Cygwin verwenden, passen Sie den Pfad an, um den Mount-Point von Cygwin zu verwenden, z.B.:

    ```bash
    git config --global mergetool.tortoisemerge.cmd '"/cygdrive/c/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe" -base:"$BASE" -theirs:"$REMOTE" -mine:"$LOCAL" -merged:"$MERGED"'
    ```

    Dies berücksichtigt die Pfadstruktur `/cygdrive/c/` von Cygwin.[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)
- **TortoiseGitMerge nicht gefunden**
  - Wenn Sie zuvor TortoiseMerge von TortoiseSVN verwendet haben, stellen Sie sicher, dass Sie auf `TortoiseGitMerge.exe` verweisen, da sich der Name der ausführbaren Datei in TortoiseGit Version 1.8 geändert hat.[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/15881449/why-doesnt-tortoisemerge-work-as-my-mergetool)

### Zusätzliche Hinweise
- TortoiseGitMerge unterstützt eine Drei-Spalten-Ansicht zur Konfliktlösung, die ideal zum Zusammenführen ist. Es merged nicht-konfligierende Änderungen automatisch und hebt Konflikte zur manuellen Auflösung hervor.[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://manios.org/2018/05/30/git-merge-conflicts-using-tortoise-git-merge-windows)
- Wenn Sie TortoiseGitMerge auch als Diff-Tool verwenden möchten, konfigurieren Sie es ähnlich:

  ```bash
  git config --global diff.tool tortoisediff
  git config --global difftool.tortoisediff.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -mine:\"$REMOTE\" -base:\"$LOCAL\""
  ```

  Verwenden Sie dann `git difftool`, um Dateien zu vergleichen.[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)
- Für erweiterte Einstellungen können Sie TortoiseGit so konfigurieren, dass es auf das Schließen des Merge-Tools wartet und Dateien basierend auf dem Exit-Code automatisch als aufgelöst markiert. In TortoiseGit Einstellungen → Externe Programme → Merge Tool, wählen Sie "Block TortoiseGit while executing the external merge tool" und aktivieren Sie "Trust exit code."[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-settings.html)

### Quellen
- TortoiseGit Dokumentation:[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-merge.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)
- Stack Overflow und andere Web-Ressourcen:[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)

Wenn Sie diese Schritte befolgen, sollten Sie in der Lage sein, TortoiseGitMerge effektiv als Ihr Git Mergetool zu verwenden, entweder über die Kommandozeile oder über die TortoiseGit GUI.