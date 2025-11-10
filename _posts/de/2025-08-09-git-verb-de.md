---
audio: false
generated: true
image: false
lang: de
layout: post
title: Ausführliche Git-Protokollierung
translated: true
type: note
---

Um die ausführliche Protokollierung in Git zu aktivieren, können Sie je nach Befehl und dem gewünschten Detaillierungsgrad bestimmte Flags oder Umgebungsvariablen verwenden. Hier sind die wichtigsten Ansätze:

1. **Verwenden des `--verbose` oder `-v` Flags**:
   Viele Git-Befehle unterstützen das `--verbose` (oder `-v`) Flag, um eine detailliertere Ausgabe zu liefern. Zum Beispiel:
   ```bash
   git commit --verbose
   ```
   Dies zeigt den Diff der Änderungen, die committet werden, zusätzlich zur üblichen Ausgabe.

2. **Aktivieren des ausführlichen Modus für bestimmte Befehle**:
   - Für `git push`:
     ```bash
     git push --verbose
     ```
     Dies liefert Details zum Push-Vorgang, inklusive der zu pushenden Refs und der Serverkommunikation.
   - Für `git fetch`:
     ```bash
     git fetch --verbose
     ```
     Dies zeigt detaillierte Informationen darüber, was gefetcht wird.
   - Für `git clone`:
     ```bash
     git clone --verbose <repository>
     ```
     Dies zeigt den Fortschritt und zusätzliche Details während des Klonens an.

3. **Setzen der `GIT_TRACE` Umgebungsvariable**:
   Für tiefergehendes Debugging können Sie die Trace-Ausgabe von Git aktivieren, um Low-Level-Details der Git-Operationen zu sehen:
   ```bash
   GIT_TRACE=1 git <command>
   ```
   Dies gibt detaillierte Protokolle über die internen Prozesse von Git aus, wie z.B. Befehlsausführung und Systemaufrufe.

4. **Aktivieren spezifischer Trace-Level**:
   Sie können granularere Umgebungsvariablen für bestimmte Aspekte von Git verwenden:
   - `GIT_TRACE_CURL`: Aktiviert die ausführliche Protokollierung für HTTP-Operationen (nützlich für Remote-Interaktionen):
     ```bash
     GIT_TRACE_CURL=1 git <command>
     ```
   - `GIT_TRACE_PACKET`: Zeigt Paket-Level-Details für das Git-Protokoll:
     ```bash
     GIT_TRACE_PACKET=1 git <command>
     ```
   - `GIT_TRACE_PERFORMANCE`: Protokolliert Leistungsdaten:
     ```bash
     GIT_TRACE_PERFORMANCE=1 git <command>
     ```

5. **Erhöhen der Ausführlichkeit für diff-bezogene Befehle**:
   Für Befehle wie `git diff` oder `git log` können Sie Optionen verwenden, um mehr Details zu erhalten:
   - `git diff --stat` zeigt eine Zusammenfassung der Änderungen.
   - `git log --verbose` oder `git log -p` beinhaltet den vollständigen Diff für jeden Commit.

6. **Globale Konfiguration für ausführliche Ausgabe**:
   Sie können Git so konfigurieren, dass es für bestimmte Befehle immer ausführlich ist, indem Sie Aliase setzen oder Konfigurationsoptionen verwenden. Zum Beispiel:
   ```bash
   git config --global alias.logv "log --verbose"
   ```
   Wenn Sie dann `git logv` ausführen, wird immer die ausführliche Ausgabe eingeschlossen.

**Beispiel**:
Um eine detaillierte Ausgabe für einen Push-Vorgang mit vollständiger Tracing-Funktion zu sehen:
```bash
GIT_TRACE=1 git push --verbose
```

**Hinweise**:
- Die ausführliche Ausgabe kann überwältigend sein, besonders mit `GIT_TRACE`, verwenden Sie sie also nur zur Fehlersuche bei spezifischen Problemen.
- Überprüfen Sie die Manpages für spezifische Befehle (z.B. `man git-push`), um zu sehen, ob sie `--verbose` oder andere Debug-Flags unterstützen.
- Unter Windows verwenden Sie die gleiche Umgebungsvariable-Syntax in der Eingabeaufforderung (`set GIT_TRACE=1`) oder in PowerShell (`$env:GIT_TRACE=1`).

Wenn Sie eine ausführliche Protokollierung für einen bestimmten Git-Befehl oder ein bestimmtes Szenario benötigen, lassen Sie es mich wissen, und ich kann ein maßgeschneidertes Beispiel liefern!