---
audio: false
generated: true
lang: de
layout: post
title: KI-gestützte Code-Editierungswerkzeuge
translated: true
type: note
---

### Visual Studio Code (VS Code) mit GitHub Copilot
VS Code, erweitert durch GitHub Copilot (eine KI-Erweiterung), unterstützt das Auswählen von Code (z. B. einer Funktion) und die Verwendung von KI, um diesen zu reparieren, zu bearbeiten oder umzustrukturieren. Wichtige Funktionen sind:
- **Inline-Chat**: Wählen Sie den Code aus, drücken Sie `Strg+I` (Windows/Linux) oder `Cmd+I` (Mac) und geben Sie eine Aufforderung wie "diesen Fehler beheben" oder "für die Verwendung von async/await umstrukturieren" ein. Copilot schlägt Änderungen direkt im Editor vor.
- **Fehler beheben**: Bei Compiler-Fehlern (rote Wellenlinien) fahren Sie mit der Maus darüber und wählen Sie "Mit Copilot beheben", um KI-generierte Lösungen zu erhalten.
- **Chat-Ansicht**: Öffnen Sie den Copilot-Chat (`Strg+Alt+I`), wählen Sie Code aus und bitten Sie ihn, diesen zu erklären, zu bearbeiten oder Tests zu generieren. Im Agent-Modus kann er auch bearbeitungen über mehrere Dateien hinweg durchführen.
- **Aktionsmenü**: Klicken Sie mit der rechten Maustaste auf den ausgewählten Code für KI-Aktionen wie Erklären, Umbenennen oder Überprüfen.

Copilot ist mit Einschränkungen kostenlos oder gegen Bezahlung für unbegrenzte Nutzung verfügbar.

### Cursor AI Code Editor
Cursor ist ein KI-zentrierter Code-Editor, der von VS Code abgespalten wurde und speziell für KI-unterstützte Bearbeitung entwickelt wurde. Er zeichnet sich besonders beim Auswählen und Modifizieren von Code mit KI aus:
- **Bearbeiten mit Strg+K**: Wählen Sie eine Funktion oder einen Codeblock aus, drücken Sie `Strg+K` (oder `Cmd+K` auf dem Mac) und beschreiben Sie die Änderungen (z. B. "diese Funktion für Leistung optimieren"). Cursor generiert Diffs, die Sie vorschauen und anwenden können.
- **Composer-Modus**: Für komplexe Bearbeitungen über Dateien hinweg verwenden Sie die Composer-Oberfläche, um Änderungen in mehreren Dateien anzufordern, Diffs zu überprüfen und zu iterieren.
- **Agent-Modus**: Drücken Sie `Strg+I`, weisen Sie umfassendere Aufgaben an (z. B. "Fehler in diesem Modul beheben") und der Agent plant, bearbeitet und führt Befehle autonom aus, während Sie auf dem Laufenden bleiben.
- **Vorschläge für nächste Bearbeitung**: Die KI sagt Folgebearbeitungen auf Basis Ihrer Änderungen voraus und schlägt sie vor.

Cursor ist in den Grundzügen kostenlos, mit einem Pro-Tarif für erweiterte Modelle. Er importiert nahtlos VS Code-Erweiterungen.

### IntelliJ IDEA mit JetBrains AI Assistant
IntelliJ IDEA (und andere JetBrains IDEs) verfügt über ein eingebautes AI Assistant-Plugin, das das Auswählen von Code und die Verwendung von KI für Korrekturen oder Bearbeitungen ermöglicht:
- **KI-Aktionen-Menü**: Wählen Sie Code aus, drücken Sie `Alt+Eingabe` oder klicken Sie mit der rechten Maustaste und wählen Sie "AI Actions" > Optionen wie "Refactoring vorschlagen", "Probleme finden" oder "Mit KI beheben". Es analysiert den Kontext und schlägt Änderungen in einem Diff-Viewer vor.
- **Inline-Eingabeaufforderung**: Geben Sie eine Aufforderung direkt im Editor ein (z. B. "diese Funktion umstrukturieren"), drücken Sie `Tab` und die KI generiert/bearbeitet den Code inline.
- **Fehlerkorrekturen**: Für hervorgehobene Fehler wählen Sie "Mit KI beheben", um kontextbezogene Vorschläge zu erhalten.
- **Code-Generierung/-Refactoring**: Rufen Sie es über das Menü auf, um Code zu erklären, Typ-Annotationen hinzuzufügen oder Abschnitte neu zu generieren.

Der AI Assistant erfordert eine JetBrains AI-Lizenz (kostenlose Testversion verfügbar) und wird von Modellen wie Mellum für Vervollständigungen angetrieben.

Alle diese Tools integrieren KI tiefgehend, aber Cursor ist das KI-zentrierteste, VS Code/Copilot ist flexibel und weit verbreitet, und IntelliJs KI ist auf Enterprise-/Java-lastige Workflows zugeschnitten. Wählen Sie basierend auf Ihrem bevorzugten Ökosystem.

Referenzen:  
[GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)  
[Get started with GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/getting-started)  
[Features | Cursor - The AI Code Editor](https://cursor.com/en/features)  
[Cursor AI: A Guide With 10 Practical Examples](https://www.datacamp.com/tutorial/cursor-ai-code-editor)  
[Use AI in editor | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/use-ai-in-editor.html)  
[AI Assistant in JetBrains IDEs | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/ai-assistant-in-jetbrains-ides.html)  
[Use AI prompts to explain and refactor your code | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/use-prompts-to-explain-and-refactor-your-code.html)