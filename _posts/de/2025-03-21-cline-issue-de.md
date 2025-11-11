---
audio: false
generated: true
lang: de
layout: post
title: Problem mit der Cline-Erweiterung in Visual Studio Code
translated: true
type: note
---

Es scheint, als hättest du Probleme mit der Cline-Erweiterung in Visual Studio Code (VSCode), bei der sie neu erstellte Dateien nicht erkennt und die `@mention`-Funktionalität nicht funktioniert. Basierend auf dem Kontext von Cline als KI-gestütztem Coding-Assistenten findest du hier Möglichkeiten zur Fehlerbehebung:

---

### 1. Cline erkennt neu erstellte Datei nicht
Cline erkennt eine neu erstellte Datei möglicherweise nicht aufgrund von Verzögerungen bei der Workspace-Indizierung, Berechtigungsproblemen oder einem Fehler im Datei-Überwachungsmechanismus der Erweiterung. So kannst du das Problem beheben:

#### Schritte zur Fehlerbehebung:
- **Workspace aktualisieren**: Nach dem Erstellen einer neuen Datei aktualisiere den VSCode-Workspace manuell, damit Cline sie erkennt.
  - Drücke `Strg+Umschalt+P` (oder `Befehl+Umschalt+P` auf dem Mac), um die Befehlspalette zu öffnen.
  - Tippe `Reload Window` ein und wähle es aus. Dadurch wird VSCode neu geladen und Cline gezwungen, den Workspace neu zu indizieren.
  
- **Überprüfe die Dateierstellungsmethode**: Wenn du Dateien außerhalb von VSCode erstellst (z.B. über das Terminal oder einen anderen Editor), könnte der Datei-Watcher von VSCode sie nicht sofort erkennen.
  - Versuche, die Datei direkt in VSCode zu erstellen (Rechtsklick im Explorer > Neue Datei) und prüfe, ob Cline sie erkennt.
  - Wenn du ein externes Tool verwendest, stelle sicher, dass die Datei im Workspace-Verzeichnis gespeichert ist, das Cline überwacht.

- **Berechtigungen überprüfen**: Cline benötigt Lese-/Schreibberechtigungen, um mit Dateien zu interagieren.
  - Öffne die Einstellungen von Cline in VSCode (über die Erweiterungs-Seitenleiste oder die Befehlspalette: `Cline: Open Settings`).
  - Stelle sicher, dass du die Berechtigung zum Lesen und Ändern von Dateien erteilt hast. Wenn du während einer Aufgabe dazu aufgefordert wirst, genehmige die Aktion.

- **Workspace-Snapshot überprüfen**: Cline erstellt Snapshots deines Workspaces, um Änderungen zu verfolgen. Wenn es nicht aktualisiert wird:
  - Starte eine neue Aufgabe in Cline (klicke auf die "+" Schaltfläche im Cline-Tab) und prüfe, ob die Datei nach einer erneuten Analyse des Workspaces erkannt wird.
  - Alternativ verwende die Schaltflächen `Restore` oder `Compare` in Cline, um eine Workspace-Aktualisierung zu erzwingen.

- **Cline und VSCode aktualisieren**: Stelle sicher, dass du die neuesten Versionen verwendest, da Fehler im Zusammenhang mit der Dateierkennung möglicherweise behoben wurden.
  - VSCode aktualisieren: `Hilfe > Nach Updates suchen`.
  - Cline aktualisieren: Gehe zu Erweiterungen in VSCode, suche nach Cline und klicke auf die Update-Schaltfläche, falls verfügbar.

- **Debugging über Protokolle**: Überprüfe die Protokolle von Cline auf Fehler.
  - Öffne das Ausgabe-Panel in VSCode (`Strg+Umschalt+U` oder `Befehl+Umschalt+U`).
  - Wähle "Cline" aus dem Dropdown-Menü, um die Protokolle anzuzeigen. Suche nach Meldungen über Fehler bei der Dateierkennung und behebe die genannten Probleme (z.B. Pfadfehler).

#### Mögliche Ursache:
Cline verlässt sich auf die Dateisystem-APIs von VSCode, um Änderungen zu erkennen. Wenn die Datei nicht indiziert ist oder der Watcher verzögert arbeitet, sieht Cline sie erst, wenn der Workspace aktualisiert wird.

---

### 2. Cline kann @mention nicht verwenden
Die `@mention`-Syntax in Cline wird typischerweise verwendet, um bestimmte Tools oder Funktionen aufzurufen (z.B. `@url`, um eine Webseite abzurufen, oder `@problems`, um Workspace-Fehler zu behandeln). Wenn es nicht funktioniert, könnte dies an einer Fehlkonfiguration, einem nicht unterstützten Modell oder einem Syntax-Missverständnis liegen.

#### Schritte zur Fehlerbehebung:
- **Syntax überprüfen**: Stelle sicher, dass du die korrekte `@mention`-Syntax verwendest.
  - Beispiele aus der Cline-Dokumentation:
    - `@url`: Ruft eine URL ab und konvertiert sie in Markdown.
    - `@problems`: Bindet Workspace-Fehler/Warnungen ein, damit Cline sie beheben kann.
  - Tippe die `@mention` im Aufgaben-Eingabefeld genau so ein, wie in der Dokumentation beschrieben (Groß-/Kleinschreibung beachten). Zum Beispiel könnte `@Url` oder `@URL` nicht funktionieren, wenn `@url` erwartet wird.

- **Modellunterstützung überprüfen**: Nicht alle von Cline unterstützten KI-Modelle können die `@mention`-Funktionalität verarbeiten. Claude 3.5 Sonnet (von Cline empfohlen) unterstützt agentische Features, andere möglicherweise nicht.
  - Öffne die Einstellungen von Cline und bestätige deinen API-Provider und das Modell.
  - Wenn du OpenRouter oder einen anderen Provider verwendest, wechsle zu Claude 3.5 Sonnet und teste erneut.

- **Mit einer einfachen Aufgabe testen**: Starte eine neue Aufgabe und versuche eine einfache `@mention`:
  - Beispiel: "Behebe die in @problems aufgeführten Probleme."
  - Wenn es nicht reagiert, ist die Funktion möglicherweise deaktiviert oder fehlerhaft konfiguriert.

- **Tool-Erweiterungen aktivieren**: Einige `@mentions` (z.B. benutzerdefinierte Tools wie `@jira` oder `@aws`) erfordern einen Model Context Protocol (MCP) Server.
  - Prüfe, ob die von dir verwendete `@mention` einem benutzerdefinierten Tool entspricht. Wenn ja:
    - Bitte Cline, "ein Tool hinzuzufügen" (z.B. "add a tool that fetches Jira tickets") und folge den Anweisungen zur Einrichtung.
    - Starte VSCode nach dem Hinzufügen des Tools neu, um sicherzustellen, dass es registriert ist.

- **API-Schlüssel überprüfen**: Wenn `@mention` externe Anfragen beinhaltet (z.B. `@url`), könnte deinem API-Schlüssel die erforderlichen Berechtigungen oder Guthaben fehlen.
  - Überprüfe deinen API-Schlüssel in den Einstellungen von Cline (z.B. Anthropic oder OpenRouter Schlüssel).
  - Stelle sicher, dass dein Account über Guthaben oder Zugriff auf die angeforderte Funktion verfügt.

- **Einen Bug melden**: Wenn die oben genannten Schritte fehlschlagen, könnte es sich um einen Fehler handeln.
  - Besuche Cline's GitHub (github.com/cline/cline) und prüfe offene Issues.
  - Wenn kein ähnliches Problem existiert, erstelle einen neuen Issue mit Details: deine Cline-Version, VSCode-Version, verwendetes Modell und die exakt versuchte `@mention`.

#### Mögliche Ursache:
Die `@mention`-Funktion ist möglicherweise für dein Setup nicht vollständig implementiert, oder es gibt eine Diskrepanz zwischen den Fähigkeiten des Modells und dem erwarteten Verhalten.

---

### Allgemeine Tipps
- **VSCode neu starten**: Ein vollständiger Neustart kann vorübergehende Probleme mit Erweiterungen beheben.
- **Cline neu installieren**: Wenn die Probleme bestehen bleiben, deinstalliere und installiere die Erweiterung erneut aus dem VSCode Marketplace.
- **Cline-Community beitreten**: Für Echtzeit-Hilfe trete ihrem Discord bei (verlinkt auf GitHub) und frage im #support oder #contributors Channel.

---

### Beispiel-Workflow zum Testen der Lösungen
1. Erstelle eine neue Datei in VSCode (z.B. `test.txt`).
2. Lade das Fenster neu (`Strg+Umschalt+P > Reload Window`).
3. Öffne Cline, starte eine neue Aufgabe und tippe: "Lies den Inhalt von test.txt und verwende @problems, um alle Probleme aufzulisten."
4. Genehmige alle Berechtigungen und prüfe, ob Cline die Datei erkennt und die `@mention` verarbeitet.

Wenn diese Schritte das Problem nicht lösen, teile mir dein spezifisches Setup mit (Cline-Version, Modell und welche `@mention` du versuchst), und ich werde genauer nachforschen!