---
audio: false
generated: true
lang: de
layout: post
title: GNOME Terminal Benutzerdefinierter Verzeichnistitel
translated: true
type: note
---

Um den GNOME Terminal-Tabtitel so anzupassen, dass nur das aktuelle Verzeichnis angezeigt wird (z. B. `blog-server`) anstatt des Standardformats (z. B. `lzw@lzw-MS:~/Projects/blog-server`), können Sie die Prompt- oder Titelleinstellungen des Terminals ändern. So gehen Sie vor:

### Schritte, um den GNOME Terminal-Tabtitel auf die Anzeige nur des aktuellen Verzeichnisses zu setzen

1. **Bearbeiten der Bash-Konfigurationsdatei**:
   GNOME Terminal verwendet standardmäßig die Bash-Shell, und der Tabtitel wird oft vom `PS1` (Prompt) oder einem spezifischen Titelbefehl abgeleitet. Um den Titel anzupassen, können Sie die Datei `~/.bashrc` ändern.

2. **Terminaltitel ändern**:
   Fügen Sie einen Befehl hinzu, um den Terminaltitel auf das aktuelle Verzeichnis in Ihrer `~/.bashrc` zu setzen. Öffnen Sie die Datei in einem Texteditor:

   ```bash
   nano ~/.bashrc
   ```

   Fügen Sie die folgenden Zeilen am Ende der Datei hinzu:

   ```bash
   # Set terminal tab title to current directory
   case "$TERM" in
   xterm*|rxvt*)
       PS1="\[\e]0;\W\a\]$PS1"
       ;;
   *)
       ;;
   esac
   ```

   **Erklärung**:
   - `\e]0;...` setzt den Terminaltitel.
   - `\W` repräsentiert den Basisnamen des aktuellen Verzeichnisses (z. B. `blog-server` anstatt des vollständigen Pfads `~/Projects/blog-server`).
   - `\a` ist ein Bell-Zeichen, um den Titel-String zu beenden.
   - Dieser Code prüft, ob das Terminal `xterm`-kompatibel ist (was GNOME Terminal ist), bevor die Änderung angewendet wird.

3. **Änderungen übernehmen**:
   Speichern Sie die Datei und laden Sie die Bash-Konfiguration neu:

   ```bash
   source ~/.bashrc
   ```

   Alternativ können Sie das Terminal schließen und wieder öffnen, um die Änderungen zu übernehmen.

4. **Ergebnis überprüfen**:
   Navigieren Sie in ein Verzeichnis (z. B. `cd ~/Projects/blog-server`), und der Terminal-Tabtitel sollte nun nur `blog-server` anzeigen.

### Alternative: GNOME Terminal-Profileinstellungen ändern
Wenn Sie den Titel weiter anpassen möchten oder die Bearbeitung von `~/.bashrc` vermeiden möchten, können Sie die Profileinstellungen von GNOME Terminal verwenden:

1. Öffnen Sie GNOME Terminal.
2. Gehen Sie zu **Bearbeiten** > **Einstellungen** (oder **Terminal** > **Einstellungen**, abhängig von Ihrer Version).
3. Wählen Sie das von Ihnen verwendete Profil aus (z. B. "Unbenannt" oder ein benutzerdefiniertes Profil).
4. Gehen Sie zum Tab **Befehl**.
5. Setzen Sie unter **Titel und Befehl**:
   - **Initialer Titel**: Leer lassen oder auf etwas Allgemeines setzen.
   - **Wenn Befehl beendet wird**: Wählen Sie **Initialen Titel beibehalten** oder **Durch Befehlsausgabe ersetzen**.
6. Aktivieren Sie im Abschnitt **Befehl** die Option **Benutzerdefinierten Befehl anstelle meiner Shell ausführen** und setzen Sie den Befehl auf:

   ```bash
   bash --rcfile <(echo '. ~/.bashrc; PS1="\[\e]0;\W\a\]$PS1"')
   ```

   Dies stellt sicher, dass das Terminal einen benutzerdefinierten Prompt verwendet, der den Titel auf das aktuelle Verzeichnis setzt.

7. Schließen Sie den Dialog und testen Sie, indem Sie einen neuen Tab öffnen oder in ein Verzeichnis navigieren.

### Hinweise
- Wenn Sie eine andere Shell als Bash verwenden (z. B. Zsh), müssen Sie die entsprechende Konfigurationsdatei (z. B. `~/.zshrc`) ändern und die Syntax entsprechend anpassen. Für Zsh können Sie hinzufügen:

  ```zsh
  precmd() { echo -ne "\e]0;${PWD##*/}\a" }
  ```

- Wenn sich der Titel nicht wie erwartet aktualisiert, stellen Sie sicher, dass Ihr Terminal-Emulator `xterm`-kompatibel ist und dass keine anderen Skripte (z. B. benutzerdefinierte `PS1`-Einstellungen in `~/.bashrc`) den Titel überschreiben.
- Für dauerhafte Änderungen über alle Terminals hinweg stellen Sie sicher, dass die Konfiguration im Shell-Profil des Benutzers oder in den GNOME Terminal-Einstellungen vorhanden ist.

Dies sollte Ihnen einen Tabtitel geben, der nur den aktuellen Verzeichnisnamen anzeigt, wie `blog-server`. Lassen Sie mich wissen, wenn Sie weitere Erklärungen benötigen!