---
audio: false
generated: true
lang: de
layout: post
title: Aktiviere Zeilenumbruch nur für bestimmte Dateierweiterungen
translated: true
type: note
---

Ich nehme an, Sie fragen, wie Sie Visual Studio Code (VS Code) konfigurieren können, um den Zeilenumbruch nur für bestimmte Dateierweiterungen zu aktivieren. So können Sie das erreichen:

1.  **Öffnen Sie die VS Code-Einstellungen**:
    *   Drücken Sie `Strg + ,` (oder `Cmd + ,` auf macOS), um die Einstellungen zu öffnen, oder gehen Sie zu `Datei > Einstellungen > Einstellungen`.

2.  **Verwenden Sie die JSON-Einstellungsdatei**:
    *   Klicken Sie in der Einstellungs-UI auf das `{}`-Symbol in der oberen rechten Ecke, um die `settings.json`-Datei zu öffnen. Dies ermöglicht eine feinere Kontrolle.

3.  **Konfigurieren Sie den Zeilenumbruch pro Dateityp**:
    *   Fügen Sie eine Konfiguration mit der Syntax `"[dateityp]": {}` hinzu, um Einstellungen für bestimmte Dateierweiterungen festzulegen. Um beispielsweise den Zeilenumbruch nur für `.md` (Markdown) und `.txt` (Text)-Dateien zu aktivieren, können Sie so etwas hinzufügen:

    ```json
    {
        "editor.wordWrap": "off", // Standard: Kein Umbruch für alle Dateien
        "[markdown]": {
            "editor.wordWrap": "on" // Umbruch nur für .md-Dateien
        },
        "[plaintext]": {
            "editor.wordWrap": "on" // Umbruch nur für .txt-Dateien
        }
    }
    ```

4.  **Erklärung**:
    *   `"editor.wordWrap": "off"` setzt den globalen Standard auf "kein Umbruch".
    *   `"[markdown]"` und `"[plaintext]"` sind Sprachkennungen für Markdown- und Plain-Text-Dateien. Sie können sie durch andere Sprachkennungen wie `[javascript]`, `[python]` usw. ersetzen, je nachdem, welche Dateierweiterungen Sie ansprechen möchten.
    *   `"editor.wordWrap": "on"` aktiviert den Umbruch für diese spezifischen Dateitypen.

5.  **Sprachkennungen finden**:
    *   Wenn Sie sich nicht sicher sind, welche Sprachkennung eine Dateierweiterung hat, öffnen Sie eine Datei dieses Typs in VS Code, klicken Sie auf den Sprachmodus in der unteren rechten Ecke (z. B. "Plain Text" oder "Python") und notieren Sie die Kennung, die in der Befehlspalette bei der Auswahl einer Sprache angezeigt wird.

6.  **Speichern und Testen**:
    *   Speichern Sie die `settings.json`-Datei, und VS Code wendet die Einstellungen sofort an. Öffnen Sie Dateien mit verschiedenen Erweiterungen, um das Verhalten zu bestätigen.

Dieser Ansatz stellt sicher, dass der Zeilenumbruch nur für die von Ihnen angegebenen Dateitypen aktiviert ist, während alle anderen unberührt bleiben. Lassen Sie mich wissen, wenn Sie Hilfe mit bestimmten Erweiterungen benötigen!

---

Wenn Sie mit `.log`-Dateien in Visual Studio Code arbeiten und den Zeilenumbruch speziell für diese aktivieren möchten, müssen Sie sicherstellen, dass VS Code diese Dateien als einen bestimmten Sprachmodus erkennt. Standardmäßig haben `.log`-Dateien möglicherweise keine eindeutige Sprachkennung wie `[log]` – sie werden oft als Plain Text (`[plaintext]`) behandelt. Sie können dieses Verhalten jedoch konfigurieren. So gehen Sie vor:

### Option 1: Verwenden Sie `[plaintext]`, wenn `.log`-Dateien als Plain Text erkannt werden
Wenn Ihre `.log`-Dateien als Plain Text erkannt werden (überprüfen Sie den Sprachmodus in der unteren rechten Ecke von VS Code, wenn eine `.log`-Datei geöffnet ist), können Sie einfach `[plaintext]` verwenden:

```json
{
    "editor.wordWrap": "off", // Standard: Kein Umbruch
    "[plaintext]": {
        "editor.wordWrap": "on" // Aktiviert für .txt- und .log-Dateien (falls als Plaintext erkannt)
    }
}
```

*   **Hinweis**: Dies gilt für alle Plain-Text-Dateien (z. B. `.txt`, `.log`), nicht nur für `.log`-Dateien. Wenn das zu weitreichend ist, fahren Sie mit Option 2 fort.

### Option 2: `.log`-Dateien einem benutzerdefinierten Sprachmodus zuordnen
Wenn Sie möchten, dass `[log]` als spezifische Kennung funktioniert, müssen Sie VS Code anweisen, `.log`-Dateien einem "Log"-Sprachmodus zuzuordnen. So geht's:

1.  **Installieren Sie eine Log-File-Erweiterung (Optional)**:
    *   Installieren Sie eine Erweiterung wie "Log File Highlighter" aus dem VS Code Marketplace. Diese Erweiterung weist `.log`-Dateien oft einen spezifischen Sprachmodus (z. B. `log`) zu.
    *   Überprüfen Sie nach der Installation den Sprachmodus für eine `.log`-Datei (unten rechts). Wenn "Log" oder ähnliches angezeigt wird, können Sie `[log]` direkt verwenden.

2.  **Ordnen Sie `.log`-Dateien manuell zu**:
    *   Wenn Sie keine Erweiterung verwenden möchten, können Sie `.log`-Dateien manuell über `files.associations` in `settings.json` einem Sprachmodus zuordnen:
    ```json
    {
        "files.associations": {
            "*.log": "log" // Ordnet .log dem "log"-Sprachmodus zu
        },
        "editor.wordWrap": "off", // Standard: Kein Umbruch
        "[log]": {
            "editor.wordWrap": "on" // Nur für .log-Dateien aktivieren
        }
    }
    ```
    *   **Einschränkung**: Der `log`-Sprachmodus muss existieren (z. B. bereitgestellt durch eine Erweiterung oder VS Code). Wenn nicht, könnte VS Code auf Plain Text zurückfallen, und `[log]` funktioniert ohne weitere Anpassungen nicht wie erwartet.

3.  **Überprüfen Sie den Sprachmodus**:
    *   Öffnen Sie eine `.log`-Datei, klicken Sie auf den Sprachmodus in der unteren rechten Ecke und sehen Sie nach, auf was er eingestellt ist. Wenn er nach Ihren Änderungen auf `log` steht, funktioniert `[log]`. Wenn er noch `plaintext` ist, verwenden Sie `[plaintext]` oder passen Sie die Zuordnung an.

### Option 3: Feineinstellung mit Dateimustern (Am präzisesten)**
Für maximale Kontrolle können Sie die Einstellung `"files.associations"` verwenden, um speziell `.log`-Dateien anzusprechen und sich dann auf einen Fallback-Sprachmodus wie `plaintext` nur für `.log` zu verlassen:

```json
{
    "files.associations": {
        "*.log": "plaintext" // Erzwingt, dass .log-Dateien als Plaintext behandelt werden
    },
    "editor.wordWrap": "off", // Standard: Kein Umbruch
    "[plaintext]": {
        "editor.wordWrap": "on" // Aktivieren für .log (und .txt, falls gewünscht)
    }
}
```

*   **Um `.txt` auszuschließen**: Wenn Sie möchten, dass `.log`-, aber nicht `.txt`-Dateien umbrochen werden, benötigen Sie eine benutzerdefinierte Erweiterung oder ein erweitertes Setup (z. B. eine VS-Code-Erweiterung, die einen eindeutigen `log`-Modus definiert), da VS Code `.log` nicht nativ von `.txt` unterscheidet ohne zusätzliche Konfiguration.

### `[log]` direkt testen
Wenn Sie unsicher sind, ob `[log]` sofort funktioniert (aufgrund einer Erweiterung oder dem integrierten Verhalten von VS Code), versuchen Sie dies:

```json
{
    "editor.wordWrap": "off",
    "[log]": {
        "editor.wordWrap": "on"
    }
}
```

Öffnen Sie eine `.log`-Datei und prüfen Sie, ob der Umbruch angewendet wird. Wenn nicht, ist der Sprachmodus nicht `log`, und Sie müssen eine der obigen Optionen verwenden.

### Empfehlung
*   **Einfachste Lösung**: Verwenden Sie `[plaintext]`, wenn es für Sie in Ordnung ist, dass sowohl `.txt` als auch `.log` umbrochen werden.
*   **Spezifische Lösung**: Installieren Sie eine "Log File Highlighter"-Erweiterung, bestätigen Sie, dass der Modus `log` ist, und verwenden Sie `[log]`.
*   Lassen Sie mich wissen, welchen Sprachmodus Ihre `.log`-Dateien anzeigen, und ich kann die Lösung weiter verfeinern!

---

Ich habe die folgende Konfiguration getestet, und sie funktioniert einwandfrei.

```json
   {
       "editor.wordWrap": "off", // Standard: Kein Umbruch
       "[log]": {
           "editor.wordWrap": "on" // Nur für .log-Dateien aktivieren
       }
   }
```