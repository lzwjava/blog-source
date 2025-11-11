---
audio: false
generated: true
lang: de
layout: post
title: Einrichten von BeyondCompare mit Git Difftool
translated: true
type: note
---

Um Beyond Compare als `git difftool` einzurichten, befolgen Sie diese Schritte. Diese Anweisungen setzen voraus, dass Beyond Compare installiert und Git auf Ihrem System konfiguriert ist.

### Schritte zur Konfiguration von Beyond Compare als `git difftool`

1.  **Überprüfen der Beyond Compare-Installation**
    Stellen Sie sicher, dass Beyond Compare installiert und über die Befehlszeile erreichbar ist. Sie können dies überprüfen, indem Sie ausführen:
    ```
    bcomp
    ```
    Wenn der Befehl nicht erkannt wird, stellen Sie sicher, dass die ausführbare Datei von Beyond Compare (z.B. `BCompare.exe` unter Windows oder `bcomp` unter macOS/Linux) im PATH Ihres Systems enthalten ist.

2.  **Git für die Verwendung von Beyond Compare konfigurieren**
    Führen Sie die folgenden Git-Konfigurationsbefehle in Ihrem Terminal oder Ihrer Eingabeaufforderung aus:

    ```bash
    git config --global diff.tool bc
    git config --global difftool.bc.path "Pfad/zu/bcomp"
    git config --global difftool.prompt false
    ```

    - Ersetzen Sie `"Pfad/zu/bcomp"` durch den tatsächlichen Pfad zur ausführbaren Beyond Compare-Datei:
        - **Windows**: Typischerweise `"C:\Program Files\Beyond Compare 4\BCompare.exe"`. Verwenden Sie doppelte Backslashes (`\\`) oder Forward Slashes (`/`) im Pfad.
        - **macOS**: Üblicherweise `/Applications/Beyond Compare.app/Contents/MacOS/bcomp`.
        - **Linux**: Oft `/usr/bin/bcomp` oder wo auch immer `bcomp` installiert ist.
    - Die Einstellung `difftool.prompt false` verhindert, dass Git Sie auffordert, das Difftool für jede Datei zu starten.

3.  **(Optional) Als Merge Tool konfigurieren**
    Wenn Sie Beyond Compare auch als Ihr `mergetool` verwenden möchten, fügen Sie diese Befehle hinzu:

    ```bash
    git config --global merge.tool bc
    git config --global mergetool.bc.path "Pfad/zu/bcomp"
    git config --global mergetool.prompt false
    ```

4.  **Konfiguration testen**
    Um die Einrichtung zu überprüfen, erstellen Sie oder navigieren Sie zu einem Git-Repository mit Änderungen und führen Sie aus:

    ```bash
    git difftool
    ```

    Dies sollte Beyond Compare starten, um die Unterschiede zwischen Ihren geänderten Dateien und dem letzten Commit anzuzeigen. Wenn Sie es als Mergetool verwenden, testen Sie mit:

    ```bash
    git mergetool
    ```

    (Dies gilt nur, wenn Sie Merge-Konflikte haben.)

5.  **Spezifische Hinweise für Plattformen**
    - **Windows**: Stellen Sie sicher, dass Sie den korrekten Pfad zu `BCompare.exe` verwenden. Wenn der Pfad Leerzeichen enthält, setzen Sie ihn in Anführungszeichen.
    - **macOS/Linux**: Der `bcomp`-Befehl muss oft warten, bis Beyond Compare geschlossen wurde, bevor die Kontrolle an das Terminal zurückgegeben wird. Die Dokumentation von Beyond Compare deutet darauf hin, dass dies automatisch gehandhabt wird. Wenn Git jedoch vorzeitig beendet wird, müssen Sie möglicherweise Skripte anpassen oder einen Wrapper verwenden (siehe Beyond Compare-Support für Details).
    - Wenn Sie auf Probleme stoßen, überprüfen Sie den Pfad und stellen Sie sicher, dass Beyond Compare lizenziert und funktionsfähig ist.

6.  **Beispielkonfiguration für Windows**
    Für Beyond Compare 4 unter Windows könnten die Befehle wie folgt aussehen:

    ```bash
    git config --global diff.tool bc
    git config --global difftool.bc.path "C:\\Program Files\\Beyond Compare 4\\BCompare.exe"
    git config --global difftool.prompt false
    git config --global merge.tool bc
    git config --global mergetool.bc.path "C:\\Program Files\\Beyond Compare 4\\BCompare.exe"
    git config --global mergetool.prompt false
    ```

7.  **Konfiguration überprüfen**
    Überprüfen Sie Ihre Git-Konfiguration, um sicherzustellen, dass die Einstellungen übernommen wurden:

    ```bash
    git config --global --list
    ```

    Suchen Sie nach Einträgen wie `diff.tool=bc` und `difftool.bc.path`.

### Zusätzliche Tipps

-   **Bestimmte Dateien vergleichen**: Verwenden Sie `git difftool <Datei>`, um eine bestimmte Datei zu vergleichen.
-   **Branches vergleichen**: Verwenden Sie `git difftool branch1 branch2`, um Unterschiede zwischen zwei Branches zu vergleichen.
-   **Beyond Compare-Einstellungen**: In Beyond Compare können Sie Vergleichsregeln (z.B. Ignorieren von Leerzeichen) über die Benutzeroberfläche anpassen, um eine bessere Diff-Visualisierung zu erreichen.
-   **Fehlerbehebung**: Wenn Beyond Compare nicht startet, überprüfen Sie den Pfad in der `difftool.bc.path`-Einstellung. Verwenden Sie `which bcomp` (macOS/Linux) oder `where BCompare.exe` (Windows), um die ausführbare Datei zu finden.

Diese Einrichtung sollte es Ihnen ermöglichen, Beyond Compare nahtlos mit `git difftool` und optional mit `git mergetool` zu verwenden. Wenn Sie auf spezifische Probleme stoßen, teilen Sie mir Ihr Betriebssystem und eventuelle Fehlermeldungen für eine maßgeschneiderte Beratung mit!