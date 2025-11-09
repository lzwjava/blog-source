---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Ändern des VS Code-Cursors zur Linie
translated: true
type: note
---

### Behebung des Block- (Rechteck-) Cursors in VS Code

Verstanden – es klingt, als ob Ihr Cursor auf einen Block-/Rechteckstil umgeschaltet hat (üblich im Überschreibmodus oder Standardeinstellungen), aber Sie möchten den dünnen vertikalen **Linien**-Stil für einfacheres Editieren. Das ist eine schnelle Einstellungsänderung. Folgen Sie diesen Schritten genau:

#### Über die Einstellungs-Oberfläche (Am einfachsten):
1. Öffnen Sie VS Code.
2. Drücken Sie `Strg + ,` (Windows/Linux) oder `Cmd + ,` (macOS), um die Einstellungen zu öffnen.
3. Geben Sie in das Suchfeld oben ein: **cursor style**.
4. Suchen Sie nach **Editor: Cursor Style** (unter Text Editor > Cursor).
5. Klicken Sie auf das Dropdown-Menü und wählen Sie **Line** (dort könnte momentan "Block" stehen).
6. Die Änderung erfolgt sofort – testen Sie die Eingabe in einer Datei, um den dünnen Linien-Cursor zu sehen.

Wenn er sich immer noch nicht aktualisiert, schließen und öffnen Sie VS Code neu oder starten Sie es komplett neu.

#### Über settings.json (Für Präzision):
1. Öffnen Sie die Befehlspalette: `Strg + Umschalt + P` (oder `Cmd + Umschalt + P` auf macOS).
2. Geben Sie ein und wählen Sie: **Preferences: Open User Settings (JSON)**.
3. Fügen Sie diese Zeile innerhalb der `{}` hinzu oder aktualisieren Sie sie (erstellen Sie sie, falls leer):
   ```json:disable-run
   "editor.cursorStyle": "line"
   ```
4. Speichern Sie die Datei (`Strg + S` oder `Cmd + S`).

#### Zusätzliche Tipps:
- **Überschreibmodus?** Wenn Sie sich versehentlich im "Überschreibmodus" befinden (wo Zeichen blockweise überschrieben werden), drücken Sie die **Einfg**-Taste auf Ihrer Tastatur, um zurück in den Einfügemodus zu wechseln.
- **Blink-Problem?** Wenn die Linie ruckelig aussieht, suchen Sie in den Einstellungen nach **cursor blinking** und setzen Sie es auf **Blink** oder **Smooth**.
- **Stören Erweiterungen?** Deaktivieren Sie Erweiterungen wie Vim vorübergehend (Erweiterungen-Ansicht > Rechtsklick > Deaktivieren), um es zu testen.

Das sollte Ihnen sofort den sauberen Linien-Cursor besorgen. Wenn er danach immer noch rechteckig ist, teilen Sie Ihr Betriebssystem oder einen Screenshot für gezieltere Hilfe mit!

[VS Code Cursor-Dokumentation](https://code.visualstudio.com/docs/editor/codebasics#_cursor-style)