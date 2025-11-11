---
audio: false
generated: true
lang: de
layout: post
title: Schreiben von Windows-Stapelverarbeitungsdateien
translated: true
type: note
---

Eine Windows-Batch-Datei (.bat oder .cmd) ist eine Skriptdatei, die eine Reihe von Befehlen enthält, die von der Windows-Eingabeaufforderung (cmd.exe) ausgeführt werden. Batch-Dateien automatisieren repetitive Aufgaben, verwalten Systemoperationen oder führen Programme aus. Im Folgenden finden Sie eine umfassende Einführung in das Schreiben von Windows-Batch-Dateien, die deren Zweck, Syntax, gängige Befehle und Best Practices abdeckt.

### Was ist eine Batch-Datei?
Eine Batch-Datei ist eine reine Textdatei mit der Erweiterung `.bat` oder `.cmd`, die Befehle enthält, die von der Windows-Eingabeaufforderung interpretiert werden. Bei der Ausführung werden die Befehle sequentiell ausgeführt, was die Automatisierung von Aufgaben wie Dateiverwaltung, Systemkonfiguration oder Softwareinstallation ermöglicht.

### Warum Batch-Dateien verwenden?
- **Automatisierung**: Führen Sie mehrere Befehle mit einem einzigen Skript aus.
- **Einfachheit**: Es sind keine fortgeschrittenen Programmierkenntnisse erforderlich.
- **Systemverwaltung**: Führen Sie Aufgaben wie Backups, Benutzerverwaltung oder Environment-Setup durch.
- **Kompatibilität**: Funktioniert auf allen Windows-Versionen mit Eingabeaufforderung.

### Erstellen einer Batch-Datei
1. **Skript schreiben**: Verwenden Sie einen Texteditor (z.B. Notepad, VS Code), um Befehle zu schreiben.
2. **Mit korrekter Erweiterung speichern**: Speichern Sie die Datei mit der Erweiterung `.bat` oder `.cmd` (z.B. `skript.bat`).
3. **Ausführen**: Doppelklicken Sie auf die Datei oder führen Sie sie über die Eingabeaufforderung aus.

### Grundlegende Syntax und Struktur
- **Befehle**: Batch-Dateien verwenden Befehle der Eingabeaufforderung (z.B. `dir`, `copy`, `del`) und batch-spezifische Befehle (z.B. `echo`, `set`, `goto`).
- **Kommentare**: Verwenden Sie `REM` oder `::`, um Kommentare zur Klarheit hinzuzufügen.
- **Groß-/Kleinschreibung wird ignoriert**: Befehle und Variablen sind nicht case-sensitive.
- **Zeilenweise Ausführung**: Befehle werden zeilenweise ausgeführt, sofern sie nicht durch Flussbefehle wie `if`, `for` oder `goto` gesteuert werden.

### Häufige Befehle und Funktionen
#### 1. **Grundlegende Befehle**
- `ECHO`: Steuert die Befehlsausgabe oder zeigt Text an.
  - Beispiel: `ECHO Hallo Welt!` zeigt "Hallo Welt!" an.
  - `ECHO OFF`: Unterdrückt die Anzeige von Befehlen während der Ausführung.
- `CLS`: Löscht den Bildschirm der Eingabeaufforderung.
- `PAUSE`: Pausiert die Ausführung und wartet auf Benutzereingabe.
- `EXIT`: Beendet das Skript oder die Eingabeaufforderungssitzung.

#### 2. **Variablen**
- **Variablen setzen**: Verwenden Sie `SET`, um Variablen zu erstellen oder zu ändern.
  - Beispiel: `SET MEINE_VAR=Hallo` erstellt eine Variable `MEINE_VAR`.
- **Variablen verwenden**: Referenzieren Sie sie mit `%VARIABLENNAME%`.
  - Beispiel: `ECHO %MEINE_VAR%` zeigt "Hallo" an.
- **Umgebungsvariablen**: Eingebaute Variablen wie `%PATH%`, `%USERNAME%` oder `%DATE%`.

#### 3. **Eingabe und Ausgabe**
- **Benutzereingabe**: Verwenden Sie `SET /P`, um eine Eingabe anzufordern.
  - Beispiel: `SET /P NAME=Geben Sie Ihren Namen ein: ` speichert die Benutzereingabe in `NAME`.
- **Ausgabe umleiten**: Verwenden Sie `>`, um die Ausgabe in eine Datei zu schreiben, oder `>>`, um anzuhängen.
  - Beispiel: `DIR > dateiliste.txt` speichert das Verzeichnislisting in `dateiliste.txt`.

#### 4. **Bedingte Anweisungen**
- Verwenden Sie `IF`, um Befehle basierend auf Bedingungen auszuführen.
  - Syntax: `IF Bedingung Befehl [ELSE Befehl]`
  - Beispiel: `IF "%NAME%"=="Admin" ECHO Willkommen, Admin! ELSE ECHO Zugriff verweigert.`

#### 5. **Schleifen**
- **FOR-Schleife**: Iteriert über Dateien, Verzeichnisse oder Werte.
  - Beispiel: `FOR %i IN (*.txt) DO ECHO %i` listet alle `.txt`-Dateien auf.
  - Hinweis: In Batch-Dateien verwenden Sie `%%i` anstelle von `%i` für Variablen.
- **WHILE-ähnliche Schleifen**: Simulieren mit `GOTO` und `IF`.

#### 6. **Unterprogramme und Labels**
- **Labels**: Verwenden Sie `:label`, um einen Codeabschnitt zu markieren.
- **GOTO**: Springt zu einem markierten Abschnitt.
  - Beispiel: `GOTO :EOF` springt zum Ende der Datei.
- **CALL**: Ruft eine andere Batch-Datei oder ein Unterprogramm auf.
  - Beispiel: `CALL :meinUnterprogramm` führt ein markiertes Unterprogramm aus.

#### 7. **Fehlerbehandlung**
- Überprüfen Sie den Befehlserfolg mit `%ERRORLEVEL%`.
  - Beispiel: `IF %ERRORLEVEL% NEQ 0 ECHO Befehl fehlgeschlagen.`

### Best Practices
- **`ECHO OFF` verwenden**: Reduziert Unordnung, indem die Befehlsausgabe ausgeblendet wird.
- **Kommentare hinzufügen**: Verwenden Sie `REM` oder `::`, um Code zu dokumentieren.
- **Inkrementell testen**: Führen Sie kleine Abschnitte aus, um zu debuggen.
- **Fehler behandeln**: Überprüfen Sie `%ERRORLEVEL%` auf Fehler.
- **Anführungszeichen für Pfade verwenden**: Schließen Sie Dateipfade in Anführungszeichen ein, um Leerzeichen zu handhaben (z.B. `"C:\Programme\"`).
- **Reservierte Namen vermeiden**: Verwenden Sie keine Namen wie `CON`, `NUL` oder `PRN` für Dateien oder Variablen.
- **`@` für Stille verwenden**: Stellen Sie Befehlen `@` voran, um die Ausgabe einzelner Befehle zu unterdrücken (z.B. `@ECHO OFF`).

### Beispiel-Batch-Datei
Im Folgenden finden Sie eine Beispiel-Batch-Datei, die gängige Funktionen demonstriert: Auffordern zur Benutzereingabe, Erstellen eines Verzeichnisses und Protokollieren der Ausgabe.

```
@echo off
REM Beispiel-Batch-Datei zum Erstellen eines Verzeichnisses und Protokollieren von Aktionen
ECHO Starte Skript...

:: Nach Verzeichnisnamen fragen
SET /P VERZEICHNIS=Geben Sie den Verzeichnisnamen ein:

:: Überprüfen, ob die Eingabe leer ist
IF "%VERZEICHNIS%"=="" (
    ECHO Fehler: Kein Verzeichnisname angegeben.
    PAUSE
    EXIT /B 1
)

:: Verzeichnis erstellen und Ergebnis protokollieren
MKDIR "%VERZEICHNIS%"
IF %ERRORLEVEL%==0 (
    ECHO Verzeichnis "%VERZEICHNIS%" erfolgreich erstellt.
    ECHO %DATE% %TIME%: Verzeichnis "%VERZEICHNIS%" erstellt >> log.txt
) ELSE (
    ECHO Fehler beim Erstellen des Verzeichnisses "%VERZEICHNIS%".
    ECHO %DATE% %TIME%: Fehler beim Erstellen des Verzeichnisses "%VERZEICHNIS%" >> log.txt
)

::PAUSE
ECHO Fertig.
EXIT /B
```

### Ausführen der Batch-Datei
- Speichern Sie den obigen Code als `beispiel.bat`.
- Doppelklicken Sie darauf oder führen Sie sie über die Eingabeaufforderung aus (`cmd.exe /c beispiel.bat`).

### Erweiterte Tipps
- **Verzögerte Erweiterung**: Verwenden Sie `SETLOCAL EnableDelayedExpansion` für Variablen, die in Schleifen aktualisiert werden (z.B. `!VAR!` anstelle von `%VAR%`).
- **Error Levels**: Testen Sie Befehle mit `IF ERRORLEVEL n` für spezifische Exit-Codes.
- **Externe Tools**: Integrieren Sie Tools wie `PowerShell` oder `curl` für erweiterte Funktionalität.
- **Sicherheit**: Vermeiden Sie das Ausführen von Batch-Dateien aus nicht vertrauenswürdigen Quellen, um bösartigen Code zu verhindern.

### Einschränkungen
- **Komplexität**: Batch-Dateien sind für komplexe Aufgaben weniger leistungsfähig als PowerShell oder Python.
- **Fehlerbehandlung**: Im Vergleich zu modernen Skriptsprachen eingeschränkt.
- **Plattformübergreifend**: Batch-Dateien sind Windows-spezifisch.

### Ressourcen
- **Offizielle Dokumentation**: Die Command-Prompt-Referenz von Microsoft (`help`-Befehl in cmd.exe).
- **Tutorials**: Websites wie SS64.com bieten detaillierte Befehlsreferenzen.
- **Community**: Suchen Sie nach Batch-Datei-Beispielen auf X oder in Foren wie Stack Overflow.

Diese Einführung bietet eine Grundlage für das Schreiben von Batch-Dateien. Üben Sie mit einfachen Skripten und erkunden Sie Befehle über `help` in der Eingabeaufforderung, um Ihre Fähigkeiten zu erweitern.