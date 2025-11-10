---
audio: false
generated: true
lang: de
layout: post
title: Aktiviere Soft Wrap in Zed
translated: true
type: note
---

Zed verwendet, wie viele moderne Texteditoren, das Konzept des "Soft Wraps" für den Zeilenumbruch. Das bedeutet, dass Zeilen im Editor umgebrochen angezeigt werden, aber keine tatsächlichen Zeilenumbruchzeichen in Ihre Datei eingefügt werden.

So aktivieren Sie den Zeilenumbruch in Zed:

1.  **Öffnen Sie die Einstellungen von Zed:**

      * Drücken Sie `Befehl + Umschalt + P` (macOS) oder `Strg + Umschalt + P` (Windows/Linux), um die Befehlspalette zu öffnen.
      * Tippen Sie "local" und wählen Sie "zed: Open Local Settings". Dadurch wird Ihre `settings.json`-Datei geöffnet.

2.  **Fügen Sie die `soft_wrap`-Einstellung hinzu:**

      * Fügen Sie in Ihrer `settings.json`-Datei die `"soft_wrap"`-Einstellung hinzu oder ändern Sie sie. Sie haben mehrere Optionen:

          * **`"editor_width"`:** Dies ist die gebräuchlichste und allgemein empfohlene Option. Sie bricht Zeilen so um, dass sie in die aktuelle Breite Ihres Editor-Fensters passen.
            ```json
            {
              "soft_wrap": "editor_width"
            }
            ```
          * **`"preferred_line_length"`:** Diese Option bricht Zeilen basierend auf einer festgelegten `preferred_line_length` um (z. B. 80 Zeichen). Sie müssen auch `preferred_line_length` definieren.
            ```json
            {
              "soft_wrap": "preferred_line_length",
              "preferred_line_length": 80
            }
            ```
          * **`"bounded"`:** Diese Option bietet ein erweitertes Umbruchverhalten, obwohl `editor_width` oder `preferred_line_length` für die meisten Benutzer normalerweise ausreichen.
          * **`"none"`:** Dies deaktiviert den Zeilenumbruch.

3.  **Speichern Sie die Datei:**

      * Drücken Sie `Befehl + S` (macOS) oder `Strg + S` (Windows/Linux), um die `settings.json`-Datei zu speichern.

Zed sollte Zeilen nun entsprechend Ihrer gewählten Einstellung umbrechen.

**Wichtige Hinweise:**

  * **Projektebene Einstellungen:** Sie können den Zeilenumbruch auch auf Projektebene aktivieren, indem Sie einen `.zed`-Ordner in Ihrem Projektverzeichnis erstellen und darin eine `settings.json`-Datei mit der gewünschten `soft_wrap`-Konfiguration ablegen. Dies überschreibt Ihre globalen Einstellungen für dieses spezifische Projekt.
  * **Sprachspezifische Einstellungen:** Sie können `soft_wrap` sogar für bestimmte Sprachen konfigurieren. Um beispielsweise den Soft Wrap für Markdown-Dateien festzulegen:
    ```json
    {
      "languages": {
        "Markdown": {
          "soft_wrap": "editor_width"
        }
      }
    }
    ```
  * **"Rewrap"-Befehl:** Wenn Sie nach einem Befehl suchen, um Text "hart" umzubrechen (tatsächliche Zeilenumbrüche einfügen) und nicht nur visuell, hat Zed auch einen "Rewrap"-Befehl (oft belegt mit `Alt-Q` oder `Alt-W`). Dies ist nützlich zum Formatieren von Kommentaren oder langen Textzeilen.