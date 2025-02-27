---
audio: true
lang: de
layout: post
title: Aktivieren Sie das Wortumbruch nur für bestimmte Dateierweiterungen
translated: true
---

Ich nehme an, dass Sie fragen, wie man Visual Studio Code (VS Code) so konfiguriert, dass das Wortumbruch nur für bestimmte Dateiendungen aktiviert wird. Hier ist, wie Sie das erreichen können:

1. **VS Code-Einstellungen öffnen**:
   - Drücken Sie `Strg + ,` (oder `Cmd + ,` auf macOS), um die Einstellungen zu öffnen, oder gehen Sie zu `Datei > Einstellungen > Einstellungen`.

2. **JSON-Einstellungsdatei verwenden**:
   - Klicken Sie in der Einstellungs-Oberfläche auf das `{}`-Symbol in der oberen rechten Ecke, um die `settings.json`-Datei zu öffnen. Dies ermöglicht eine feinere Kontrolle.

3. **Wortumbruch pro Dateityp konfigurieren**:
   - Fügen Sie eine Konfiguration mit der Syntax `"[filetype]": {}` hinzu, um Einstellungen für bestimmte Dateiendungen zu spezifizieren. Zum Beispiel, um den Wortumbruch nur für `.md` (Markdown) und `.txt` (Text) Dateien zu aktivieren, können Sie etwas wie dies hinzufügen:

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
   - `"[markdown]"` und `"[plaintext]"` sind Sprachidentifikatoren für Markdown- und Plain-Text-Dateien. Sie können diese durch andere Sprachidentifikatoren wie `[javascript]`, `[python]` usw. ersetzen, basierend auf den Dateiendungen, die Sie ansprechen möchten.
   - `"editor.wordWrap": "on"` aktiviert den Umbruch für diese spezifischen Dateitypen.

5. **Sprachidentifikatoren finden**:
   - Wenn Sie sich nicht sicher sind, welchen Sprachidentifikator eine Dateiendung hat, öffnen Sie eine Datei dieses Typs in VS Code, klicken Sie auf den Sprachmodus in der unteren rechten Ecke (z. B. "Plain Text" oder "Python") und beachten Sie den Identifikator, der im Befehlspalette angezeigt wird, wenn Sie eine Sprache auswählen.

6. **Speichern und Testen**:
   - Speichern Sie die `settings.json`-Datei, und VS Code wird die Einstellungen sofort anwenden. Öffnen Sie Dateien mit verschiedenen Erweiterungen, um das Verhalten zu bestätigen.

Dieser Ansatz stellt sicher, dass der Wortumbruch nur für die Dateitypen aktiviert wird, die Sie angeben, und alle anderen unbeeinflusst lässt. Lassen Sie mich wissen, wenn Sie Hilfe mit bestimmten Erweiterungen benötigen!

---

Wenn Sie mit `.log`-Dateien in Visual Studio Code arbeiten und den Wortumbruch speziell für diese aktivieren möchten, müssen Sie sicherstellen, dass VS Code diese Dateien als einen eigenen Sprachmodus erkennt. Standardmäßig werden `.log`-Dateien möglicherweise nicht als ein eindeutiger Sprachidentifikator wie `[log]` erkannt – sie werden oft als Plain Text (`[plaintext]`) behandelt. Sie können jedoch dieses Verhalten konfigurieren. Hier ist, wie Sie dies tun können:

### Option 1: Verwenden Sie `[plaintext]`, wenn `.log`-Dateien als Plain Text erkannt werden
Wenn Ihre `.log`-Dateien als Plain Text erkannt werden (überprüfen Sie den Sprachmodus in der unteren rechten Ecke von VS Code, wenn eine `.log`-Datei geöffnet ist), können Sie einfach `[plaintext]` verwenden:

```json
{
    "editor.wordWrap": "off", // Standard: kein Umbruch
    "[plaintext]": {
        "editor.wordWrap": "on" // Aktivieren für .txt- und .log-Dateien (wenn als Plain Text erkannt)
    }
}
```

- **Hinweis**: Dies wird auf alle Plain-Text-Dateien (z. B. `.txt`, `.log`) angewendet, nicht nur auf `.log`-Dateien. Wenn das zu allgemein ist, gehen Sie zu Option 2.

### Option 2: `.log`-Dateien mit einem benutzerdefinierten Sprachmodus verknüpfen
Wenn Sie `[log]` als spezifischen Identifikator verwenden möchten, müssen Sie VS Code anweisen, `.log`-Dateien mit einem "Log"-Sprachmodus zu verknüpfen. Hier ist, wie:

1. **Installieren Sie eine Log-Datei-Erweiterung (optional)**:
   - Installieren Sie eine Erweiterung wie "Log File Highlighter" aus dem VS Code Marketplace. Diese Erweiterung weist `.log`-Dateien oft einen spezifischen Sprachmodus (z. B. `log`) zu.
   - Nach der Installation überprüfen Sie den Sprachmodus für eine `.log`-Datei (untere rechte Ecke). Wenn es "Log" oder ähnliches sagt, können Sie `[log]` direkt verwenden.

2. **Manuelles Verknüpfen von `.log`-Dateien**:
   - Wenn Sie keine Erweiterung möchten, können Sie `.log` manuell mit einem Sprachmodus über `files.associations` in `settings.json` verknüpfen:
   ```json
   {
       "files.associations": {
           "*.log": "log" // Verknüpft .log mit dem "log"-Sprachmodus
       },
       "editor.wordWrap": "off", // Standard: kein Umbruch
       "[log]": {
           "editor.wordWrap": "on" // Aktivieren nur für .log-Dateien
       }
   }
   ```
   - **Hinweis**: Der `log`-Sprachmodus muss existieren (z. B. von einer Erweiterung oder VS Code bereitgestellt). Wenn nicht, fällt VS Code möglicherweise auf Plain Text zurück, und `[log]` funktioniert nicht wie erwartet ohne weitere Anpassungen.

3. **Sprachmodus überprüfen**:
   - Öffnen Sie eine `.log`-Datei, klicken Sie auf den Sprachmodus in der unteren rechten Ecke und sehen Sie, was er eingestellt ist. Wenn es `log` nach Ihren Änderungen ist, funktioniert `[log]`. Wenn es immer noch `plaintext` ist, verwenden Sie `[plaintext]` oder passen Sie die Verknüpfung an.

### Option 3: Feinabstimmung mit Dateimustern (am genauesten)
Für die ultimative Kontrolle können Sie die Einstellung `"files.associations"` verwenden, um `.log`-Dateien spezifisch zu zielen, und dann auf einen Rückfall-Sprachmodus wie `plaintext` nur für `.log` zu setzen:

```json
{
    "files.associations": {
        "*.log": "plaintext" // Erzwingt, dass .log-Dateien als Plain Text behandelt werden
    },
    "editor.wordWrap": "off", // Standard: kein Umbruch
    "[plaintext]": {
        "editor.wordWrap": "on" // Aktivieren für .log (und .txt, falls gewünscht)
    }
}
```

- **Um `.txt` auszuschließen**: Wenn Sie `.log`, aber nicht `.txt` umbrechen möchten, benötigen Sie eine benutzerdefinierte Erweiterung oder eine fortschrittlichere Einrichtung (z. B. eine VS Code-Erweiterung, um einen eindeutigen `log`-Modus zu definieren), da VS Code `.log` nicht von `.txt` ohne zusätzliche Konfiguration unterscheidet.

### `[log]` direkt testen
Wenn Sie nicht sicher sind, ob `[log]` direkt funktioniert (aufgrund einer Erweiterung oder dem eingebauten Verhalten von VS Code), versuchen Sie dies:

```json
{
    "editor.wordWrap": "off",
    "[log]": {
        "editor.wordWrap": "on"
    }
}
```

Öffnen Sie eine `.log`-Datei und sehen Sie, ob der Umbruch angewendet wird. Wenn nicht, ist der Sprachmodus nicht `log`, und Sie müssen eine der oben genannten Optionen verwenden.

### Empfehlung
- **Einfachste Methode**: Verwenden Sie `[plaintext]`, wenn Sie damit einverstanden sind, dass sowohl `.txt` als auch `.log` umbrechen.
- **Spezifisch**: Installieren Sie eine "Log File Highlighter"-Erweiterung, bestätigen Sie, dass der Modus `log` ist, und verwenden Sie `[log]`.
- Lassen Sie mich wissen, welchen Sprachmodus Ihre `.log`-Dateien anzeigen, und ich kann die Lösung weiter verfeinern!

---

Ich habe die folgende Konfiguration getestet, und sie funktioniert großartig.

```json
   {
       "editor.wordWrap": "off", // Standard: kein Umbruch
       "[log]": {
           "editor.wordWrap": "on" // Aktivieren nur für .log-Dateien
       }
   }
```