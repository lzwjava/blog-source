---
audio: true
lang: de
layout: post
title: Aktivieren Sie das Wortumbruch nur für bestimmte Dateiendungen
translated: true
---

Ich nehme an, dass Sie fragen, wie man Visual Studio Code (VS Code) so konfiguriert, dass Zeilenumbruch nur für bestimmte Dateiendungen aktiviert wird. Hier ist, wie Sie dies erreichen können:

1. **VS Code-Einstellungen öffnen**:
   - Drücken Sie `Strg + ,` (oder `Cmd + ,` auf macOS), um die Einstellungen zu öffnen, oder gehen Sie zu `Datei > Einstellungen > Einstellungen`.

2. **Verwenden Sie die JSON-Einstellungsdatei**:
   - Klicken Sie in der Einstellungs-Oberfläche auf das `{}`-Symbol in der oberen rechten Ecke, um die `settings.json`-Datei zu öffnen. Dies ermöglicht eine feinere Kontrolle.

3. **Zeilenumbruch pro Dateityp konfigurieren**:
   - Fügen Sie eine Konfiguration mit der Syntax `"[filetype]": {}` hinzu, um Einstellungen für bestimmte Dateiendungen zu spezifizieren. Zum Beispiel, um Zeilenumbruch nur für `.md` (Markdown) und `.txt` (Text) Dateien zu aktivieren, können Sie etwas wie dies hinzufügen:

   ```json
   {
       "editor.wordWrap": "off", // Standard: kein Umbruch für alle Dateien
       "[markdown]": {
           "editor.wordWrap": "on" // Umbruch nur für .md-Dateien
       },
       "[plaintext]": {
           "editor.wordWrap": "on" // Umbruch nur für .txt-Dateien
       }
   }
   ```

4. **Erklärung**:
   - `"editor.wordWrap": "off"` setzt den globalen Standard auf keinen Umbruch.
   - `"[markdown]"` und `"[plaintext]"` sind Sprachidentifikatoren für Markdown- und Plain-Text-Dateien. Sie können sie durch andere Sprachidentifikatoren wie `[javascript]`, `[python]` usw. ersetzen, basierend auf den Dateiendungen, die Sie ansprechen möchten.
   - `"editor.wordWrap": "on"` aktiviert den Umbruch für diese spezifischen Dateitypen.

5. **Sprachidentifikatoren finden**:
   - Wenn Sie sich nicht sicher sind, welcher Sprachidentifikator für eine Dateiendung gilt, öffnen Sie eine Datei dieses Typs in VS Code, klicken Sie auf den Sprachmodus in der unteren rechten Ecke (z. B. "Plain Text" oder "Python") und beachten Sie den Identifikator, der im Befehlspalette angezeigt wird, wenn Sie eine Sprache auswählen.

6. **Speichern und Testen**:
   - Speichern Sie die `settings.json`-Datei, und VS Code wird die Einstellungen sofort anwenden. Öffnen Sie Dateien mit verschiedenen Erweiterungen, um das Verhalten zu bestätigen.

Dieser Ansatz stellt sicher, dass der Zeilenumbruch nur für die Dateitypen aktiviert wird, die Sie angeben, und alle anderen unbeeinflusst lässt. Lassen Sie mich wissen, wenn Sie Hilfe mit bestimmten Erweiterungen benötigen!