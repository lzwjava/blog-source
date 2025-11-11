---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Dot Sourcing von PowerShell-Skripten
translated: true
type: note
---

### Dot Sourcing von PowerShell-Funktionen in .ps1-Dateien

Dot Sourcing (mit dem `.`-Operator) lädt ein PowerShell-Skript (.ps1-Datei) in den Speicher der aktuellen Sitzung, wodurch seine Funktionen und Variablen zur Verwendung verfügbar werden, ohne den Top-Level-Code des Skripts auszuführen. Es ist nützlich zum Importieren von Modulen oder wiederverwendbarem Code.

#### Grundlegende Syntax
Führen Sie diesen Befehl in Ihrer PowerShell-Sitzung aus:
```
. Pfad\Zur\IhremSkript.ps1
```
- Ersetzen Sie `Pfad\Zur\IhremSkript.ps1` durch den tatsächlichen Dateipfad (verwenden Sie absolute Pfade für Zuverlässigkeit).
- Beispiel: `. C:\Skripts\MeineFunktionen.ps1` – Dies lädt die Funktionen aus dieser Datei in Ihre Sitzung.

#### So funktioniert es
- Im Skript definierte Funktionen werden in Ihrer aktuellen Sitzung aufrufbar.
- Variablen werden ebenfalls importiert, aber nur, wenn sie nicht lokal begrenzt sind.
- Vermeiden Sie Dot Sourcing in Produktionsskripts; verwenden Sie Module für eine bessere Organisation.
- Tipp: Wenn der Pfad Leerzeichen enthält, setzen Sie ihn in Anführungszeichen: `. "C:\Meine Skripte\Funktionen.ps1"`

Häufiges Problem: Wenn das Skript Syntaxfehler enthält, schlägt das Dot Sourcing mit einer Fehlermeldung fehl. Testen Sie durch Ausführen von `PowerShell -Command ". .\IhrSkript.ps1"` von einer Eingabeaufforderung aus.

### Verwendung der PowerShell Execution Policy

Ausführungsrichtlinien (Execution Policies) sind Sicherheitseinstellungen, die einschränken, welche Skripte PowerShell ausführen kann, um die Ausführung bösartigen Codes zu verhindern. Sie sind pro Geltungsbereich (z.B. computerweit, benutzerspezifisch).

#### Aktuelle Richtlinie überprüfen
Führen Sie dies in PowerShell aus:
```
Get-ExecutionPolicy
```
- Ausgabebeispiele: `Restricted` (blockiert alle Skripte), `AllSigned` (nur signierte Skripte), `RemoteSigned` (signierte Remote-Skripte, lokale erlaubt) oder `Unrestricted`.

#### Richtlinie setzen oder ändern
Verwenden Sie `Set-ExecutionPolicy` (erfordert Administratorrechte für Änderungen auf Computer-Ebene):
- Beispiel, um lokal geschriebene Skripte zu erlauben: `Set-ExecutionPolicy RemoteSigned`
- Erzwingen ohne Nachfragen: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force`
- Pro Geltungsbereich: `Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser` (betrifft nur Ihr Benutzerkonto).

#### Häufige Richtlinien
- `Restricted`: Standard; keine Skripte werden ausgeführt.
- `AllSigned`: Erfordert digitale Signaturen (sicher, aber unpraktisch).
- `RemoteSigned`: Ausgewogen zwischen Sicherheit – erlaubt lokale Skripte, signiert Remote-Skripte.
- `Unrestricted`: Führt alle Skripte aus (riskant; mit Vorsicht verwenden).
- `Bypass`: Vollständig uneingeschränkt, für Automatisierung.

Tipp: Richtlinien gelten für Konsolen-Sitzungen, aber nicht für ISE oder VS Code, es sei denn, sie sind gesetzt. Testen Sie Änderungen durch Ausführen eines Beispielskripts wie `Write-Host "Hallo"`. Für mehr Informationen, siehe Microsofts Dokumentation: `help about_Execution_Policies`. Wenn Sie in einem Unternehmen arbeiten, könnte Gruppenrichtlinie (Group Policy) lokale Einstellungen überschreiben.