---
audio: false
generated: true
lang: de
layout: post
title: 'PowerShell: Befehle im aktuellen Terminal ausführen'
translated: true
type: note
---

Um Befehle wie `mvn` oder WebSphere-Server-Befehle direkt im aktuellen PowerShell-Terminal auszuführen, ohne eine neue Eingabeaufforderung zu öffnen, können Sie den Call-Operator (`&`) verwenden oder den Befehl direkt aufrufen. Dieser Ansatz stellt sicher, dass der Befehl innerhalb der vorhandenen PowerShell-Sitzung ausgeführt wird, wodurch Ausgabe und Fehler im selben Terminal verbleiben.

So geht's:

1. **Befehl direkt ausführen**:
   Wenn sich der Befehl (z.B. `mvn`) im PATH Ihres Systems befindet oder im aktuellen Verzeichnis zugänglich ist, geben Sie den Befehl einfach so ein, wie Sie es in einem Terminal tun würden:

   ```powershell
   mvn clean install
   ```

   Dies führt `mvn` direkt in der PowerShell-Sitzung aus, und die Ausgabe verbleibt im aktuellen Terminal.

2. **Call-Operator (`&`) verwenden**:
   Wenn Sie den Pfad zur ausführbaren Datei angeben müssen oder der Befehl in einer Variable gespeichert ist, verwenden Sie den Call-Operator:

   ```powershell
   & "C:\pfad\zu\maven\bin\mvn.cmd" clean install
   ```

   Für WebSphere-Server-Befehle, wenn Sie etwas wie `wsadmin` oder `startServer` ausführen, können Sie Folgendes tun:

   ```powershell
   & "C:\pfad\zu\WebSphere\AppServer\bin\startServer.bat" server1
   ```

   Der `&`-Operator stellt sicher, dass der Befehl in der aktuellen PowerShell-Sitzung ausgeführt wird.

3. **Befehle mit Leerzeichen oder Variablen behandeln**:
   Wenn der BefehlsPfad Leerzeichen enthält oder in einer Variable gespeichert ist, verwenden Sie `&` mit dem in Anführungszeichen gesetzten Pfad:

   ```powershell
   $mvnPath = "C:\Program Files\Apache Maven\bin\mvn.cmd"
   & $mvnPath clean install
   ```

4. **Umgebungsvariablen setzen (falls erforderlich)**:
   Einige Befehle wie `mvn` oder WebSphere-Skripte erfordern möglicherweise Umgebungsvariablen (z.B. `JAVA_HOME` oder `WAS_HOME`). Setzen Sie diese im Skript, bevor Sie den Befehl ausführen:

   ```powershell
   $env:JAVA_HOME = "C:\pfad\zu\jdk"
   $env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
   mvn --version
   ```

   Für WebSphere:

   ```powershell
   $env:WAS_HOME = "C:\pfad\zu\WebSphere\AppServer"
   & "$env:WAS_HOME\bin\startServer.bat" server1
   ```

5. **Ausgabe erfassen oder Fehler behandeln**:
   Um die Ausgabe des Befehls zu erfassen oder Fehler zu behandeln, verwenden Sie die Standardmechanismen von PowerShell:

   ```powershell
   try {
       $output = & mvn clean install 2>&1
       Write-Output $output
   } catch {
       Write-Error "Fehler beim Ausführen von Maven: $_"
   }
   ```

6. **`Start-Process` vermeiden**:
   Im Gegensatz zu `Start-Process`, das einen neuen Prozess startet (oft in einem separaten Fenster), behalten die oben genannten Methoden die Ausführung in der aktuellen Sitzung bei. Vermeiden Sie die Verwendung von `Start-Process` wie folgt:

   ```powershell
   # Dies öffnet ein neues Eingabeaufforderungsfenster
   Start-Process -FilePath "mvn" -ArgumentList "clean install"
   ```

   Verwenden Sie stattdessen die direkte Ausführung oder `&`.

### Beispielskript
Hier ist ein Beispiel-PowerShell-Skript, um `mvn` und einen WebSphere-Befehl im aktuellen Terminal auszuführen:

```powershell
# Setze Umgebungsvariablen, falls benötigt
$env:JAVA_HOME = "C:\Program Files\Java\jdk-11"
$env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
$env:WAS_HOME = "C:\IBM\WebSphere\AppServer"

# Führe Maven-Befehl aus
Write-Output "Führe Maven aus..."
& mvn clean install

# Führe WebSphere-Server-Befehl aus
Write-Output "Starte WebSphere-Server..."
& "$env:WAS_HOME\bin\startServer.bat" server1
```

### Hinweise
- Stellen Sie sicher, dass die Befehlszeilentools (`mvn`, `startServer.bat`, etc.) in Ihrem PATH sind oder geben Sie den vollständigen Pfad zur ausführbaren Datei an.
- Wenn der Befehl ein bestimmtes Arbeitsverzeichnis erfordert, verwenden Sie `Set-Location` (oder `cd`), bevor Sie ihn ausführen:

   ```powershell
   Set-Location "C:\pfad\zum\projekt"
   & mvn clean install
   ```

- Für Befehle, die auf `.bat`- oder `.cmd`-Dateien angewiesen sind (üblich bei WebSphere), funktioniert der `&`-Operator gut, aber stellen Sie sicher, dass das Skript in PowerShell und nicht in `cmd.exe` ausgeführt wird.
- Wenn Sie auf Probleme mit Umgebungsvariablen oder PATH stoßen, überprüfen Sie diese mit `Get-ChildItem Env:`.

Dieser Ansatz behält alles im aktuellen PowerShell-Terminal bei, vermeidet neue Fenster und gewährleistet einen sauberen Arbeitsablauf. Wenn Sie einen bestimmten Befehl oder ein Setup haben, das Probleme verursacht, teilen Sie weitere Details mit, und ich kann die Lösung weiter anpassen.