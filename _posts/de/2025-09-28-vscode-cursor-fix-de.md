---
audio: false
generated: true
image: false
lang: de
layout: post
model: anthropic/claude-sonnet-4
title: Beheben von VSCode-Kreuzcursor-Problemen
translated: true
type: note
---

Der Mauszeiger, der sich in VSCode in ein Kreuz/Plus-Symbol (十字架) verwandelt, zeigt normalerweise an, dass VSCode sich in einem speziellen Modus befindet oder es ein Konfigurationsproblem gibt. Hier sind die häufigsten Ursachen und Lösungen:

## Häufige Ursachen:

1. **Spaltenauswahlmodus**: Sie haben möglicherweise versehentlich den Spalten-/Blockauswahlmodus aktiviert
   - Versuchen Sie, `Alt + Shift + I` oder `Strg + Shift + Alt + Pfeiltasten` zu drücken, um diesen Modus zu verlassen

2. **Erweiterungskonflikt**: Einige Erweiterungen können das Zeigerverhalten ändern
   - Versuchen Sie, Erweiterungen vorübergehend zu deaktivieren: `Strg + Umschalt + P` → "Developer: Reload Window"
   - Oder starten Sie VSCode im abgesicherten Modus: `code --disable-extensions`

3. **Zoom-/Auswahlwerkzeuge**: Sie haben möglicherweise ein Zoom- oder Auswahlwerkzeug aktiviert
   - Drücken Sie mehrmals die `Escape`-Taste
   - Versuchen Sie es mit `Strg + Z`, um recent actions rückgängig zu machen

4. **Terminal-Fokusproblem**: Wenn das Terminal den Fokus hat, kann dies das Zeigerverhalten ändern
   - Klicken Sie in den Editor-Bereich, um den Fokus neu zu setzen
   - Versuchen Sie `Strg + 1`, um den Fokus auf den Editor zu legen

## Schnelle Lösungen:

1. **VSCode neu starten**: Einfach, aber oft effektiv
   - `Strg + Umschalt + P` → "Developer: Reload Window"

2. **Mauseinstellungen überprüfen**:
   - Gehen Sie zu Datei → Einstellungen → Settings
   - Suchen Sie nach "cursor" und überprüfen Sie die zeigerbezogenen Einstellungen

3. **Workspace zurücksetzen**:
   - Schließen Sie VSCode
   - Löschen Sie den `.vscode`-Ordner in Ihrem Projekt (falls vorhanden)
   - Öffnen Sie das Projekt erneut

4. **Systemweites Problem überprüfen**:
   - Testen Sie, ob das Zeigerproblem auch in anderen Anwendungen auftritt
   - Wenn ja, könnte es ein GNOME-/Systemeinstellungsproblem sein

Versuchen Sie zuerst, ein paar Mal `Escape` zu drücken, und starten Sie dann VSCode neu. Dies behebt normalerweise das Problem mit dem Kreuz-Zeiger.