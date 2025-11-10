---
audio: false
generated: true
lang: de
layout: post
title: Schnelle Code-Auswahl & KI-Bearbeitung
translated: true
type: note
---

Nachfolgend finden Sie eine Übersicht, wie Sie in **Visual Studio Code (VS Code)**, **Cursor** und **IntelliJ IDEA** schnell eine Funktion oder Methode mit Shortcuts auswählen und anschließend deren KI-Funktionen nutzen können, um den ausgewählten Code zu korrigieren oder zu bearbeiten.

### Visual Studio Code (VS Code)
VS Code hat keinen direkten Shortcut, um eine gesamte Funktion/Methode auszuwählen, wenn sich Ihr Cursor darin befindet, aber Sie können die folgenden Ansätze verwenden:
- **Auswahl erweitern**: Drücken Sie `Strg+Umschalt+.` (Windows/Linux) oder `Cmd+Umschalt+.` (Mac), um den Auswahlbereich zu erweitern. Wiederholtes Drücken wählt den umschließenden Block aus (z.B. Funktionsrumpf, dann gesamte Funktion). Dies funktioniert gut für JavaScript, Python usw.
- **Intelligente Auswahl**: Verwenden Sie `Strg+Umschalt+Rechte Pfeiltaste` (Windows/Linux) oder `Cmd+Umschalt+Rechte Pfeiltaste` (Mac), um die Auswahl basierend auf der Syntax zu erweitern (möglicherweise sind mehrere Drücke erforderlich, um die gesamte Funktion zu erfassen).
- **Erweiterung: Select By**: Installieren Sie die "Select By"-Erweiterung und konfigurieren Sie eine Tastenzuordnung (z.B. `Strg+K, Strg+S`), um die umschließende Funktion/Methode basierend auf sprachspezifischen Mustern auszuwählen.

**KI-Bearbeitung mit GitHub Copilot**:
- Nachdem Sie die Funktion ausgewählt haben, drücken Sie `Strg+I` (Windows/Linux) oder `Cmd+I` (Mac), um den Inline-Chat von Copilot zu öffnen. Geben Sie eine Aufforderung wie "fix bugs in this function" oder "refactor to use arrow functions" ein.
- Alternativ klicken Sie mit der rechten Maustaste auf die Auswahl und wählen "Copilot > Fix" oder "Copilot > Refactor" für KI-Vorschläge.
- In der Copilot Chat-Ansicht (`Strg+Alt+I`) fügen Sie den ausgewählten Code ein und bitten um Bearbeitungen (z.B. "optimize this function").

### Cursor AI Code Editor
Cursor, basierend auf VS Code, verbessert die Auswahl und KI-Integration:
- **Umschließenden Block auswählen**: Drücken Sie `Strg+Umschalt+.` (Windows/Linux) oder `Cmd+Umschalt+.` (Mac), um die Auswahl auf die umschließende Funktion/Methode zu erweitern, ähnlich wie in VS Code. Das Sprachmodell-Bewusstsein von Cursor macht dies oft präziser für Sprachen wie Python oder TypeScript.
- **Benutzerdefinierte Tastenzuordnungen**: Sie können eine benutzerdefinierte Tastenzuordnung in `settings.json` festlegen (z.B. `editor.action.selectToBracket`), um den Funktionsbereich direkt auszuwählen.

**KI-Bearbeitung in Cursor**:
- Nachdem Sie die Funktion ausgewählt haben, drücken Sie `Strg+K` (Windows/Linux) oder `Cmd+K` (Mac) und beschreiben dann die Änderungen (z.B. "add error handling to this function"). Cursor zeigt eine Diff-Vorschau der KI-generierten Bearbeitungen an.
- Verwenden Sie `Strg+I` für den Agent Mode, um die Funktion autonom über Dateien hinweg zu korrigieren oder zu optimieren, mit iterativem Feedback.
- Der Composer Mode (zugänglich über die UI) ermöglicht Mehrdateien-Bearbeitungen, wenn die Funktion andere Teile der Codebasis beeinflusst.

### IntelliJ IDEA
IntelliJ IDEA bietet robuste Shortcuts zum Auswählen von Funktionen/Methoden:
- **Codeblock auswählen**: Wenn sich Ihr Cursor in einer Methode befindet, drücken Sie `Strg+W` (Windows/Linux) oder `Cmd+W` (Mac), um den umschließenden Block schrittweise auszuwählen. Wiederholtes Drücken erweitert die Auswahl auf die gesamte Methode (einschließlich Signatur). Dies funktioniert für Java, Kotlin, Python usw.
- **Auswahl verkleinern**: Verwenden Sie `Strg+Umschalt+W` (Windows/Linux) oder `Cmd+Umschalt+W` (Mac), um die Auswahl zu verkleinern, wenn Sie zu weit gegangen sind.
- **Strukturbewusste Auswahl**: Drücken Sie `Strg+Alt+Umschalt+Hoch` (Windows/Linux) oder `Cmd+Option+Umschalt+Hoch` (Mac), um die umschließende Methode direkt über den Strukturbaum auszuwählen.

**KI-Bearbeitung mit JetBrains AI Assistant**:
- Nachdem Sie die Methode ausgewählt haben, drücken Sie `Alt+Eingabe` oder klicken Sie mit der rechten Maustaste und wählen "AI Actions" > "Fix with AI" oder "Suggest Refactoring". Der AI Assistant liefert kontextbewusste Vorschläge in einem Diff-Viewer.
- Verwenden Sie die Inline-Eingabeaufforderung (geben Sie `/` gefolgt von Ihrer Anfrage ein, z.B. `/refactor to use streams`, und drücken Sie dann `Tab`), um die ausgewählte Methode direkt zu bearbeiten.
- Öffnen Sie das AI Assistant Toolfenster, um komplexe Änderungen zu beschreiben (z.B. "add logging to this method") und den generierten Code zu übernehmen.

### Zusammenfassung
- **VS Code**: Verwenden Sie `Strg+Umschalt+.`, um die Auswahl zu erweitern, dann `Strg+I` für Copilot-KI-Bearbeitungen.
- **Cursor**: Gleicher Auswahl-Shortcut (`Strg+Umschalt+.`) mit `Strg+K` für präzise KI-gesteuerte Bearbeitungen.
- **IntelliJ IDEA**: Verwenden Sie `Strg+W` für die schnelle Methodenauswahl, dann `Alt+Eingabe` für AI Assistant-Korrekturen.

IntelliJ IDEA hat den präzisesten integrierten Shortcut zum Auswählen von Methoden (`Strg+W`), während die KI-Integration von Cursor für die Bearbeitung von ausgewähltem Code am nahtlosesten ist. VS Code ist flexibel, erfordert aber möglicherweise Erweiterungen für eine schnellere Funktionsauswahl.

Referenzen:  
[Code Navigation in Visual Studio Code](https://code.visualstudio.com/docs/editor/editingevolved)  
[Cursor AI: A Guide With 10 Practical Examples](https://www.datacamp.com/tutorial/cursor-ai-code-editor)  
[Code Editing in IntelliJ IDEA](https://www.jetbrains.com/help/idea/working-with-source-code.html)  
[Use AI in editor | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/use-ai-in-editor.html)