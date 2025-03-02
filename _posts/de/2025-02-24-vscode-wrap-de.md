---
audio: false
generated: false
lang: de
layout: post
title: VSCode Zeilen umbrechen
translated: true
---

Um VSCode so zu konfigurieren, dass Zeilen umgebrochen werden und Sie leicht erkennen können, wenn Zeilen zu lang sind, können Sie die Einstellungen für den Zeilenumbruch so konfigurieren, dass Zeilen an einer bestimmten Spalte umgebrochen werden. Hier ist, wie Sie dies tun können:

### Schritte zum Aktivieren des Zeilenumbruchs an einer bestimmten Spalte

1. **Einstellungen in VSCode öffnen**:
   - Drücken Sie `Strg + ,` (oder `Cmd + ,` auf macOS), um das Einstellungsfenster zu öffnen.
   - Alternativ gehen Sie zu `Datei` > `Einstellungen` > `Einstellungen`.

2. **Nach Zeilenumbruch-Einstellungen suchen**:
   - Geben Sie im Einstellungsfenster "Zeilenumbruch" in die Suchleiste ein.
   - Finden Sie die Einstellung mit der Bezeichnung **Editor: Zeilenumbruch**.

3. **Zeilenumbruch auf "wordWrapColumn" setzen**:
   - Ändern Sie die Einstellung **Editor: Zeilenumbruch** in `"wordWrapColumn"`.
   - Diese Option ermöglicht es, Zeilen an einer bestimmten Spalte umzubrechen.

4. **Spaltengrenze festlegen**:
   - Suchen Sie nach der Einstellung **Editor: Zeilenumbruch-Spalte** (erscheint, wenn "wordWrapColumn" ausgewählt ist).
   - Setzen Sie diese auf Ihre bevorzugte Spaltengrenze, z.B. `80`.
   - Das bedeutet, dass jede Zeile, die länger als 80 Zeichen ist, umgebrochen wird.

5. **(Optional) Vertikale Linie für visuelle Unterstützung hinzufügen**:
   - Geben Sie "Linien" in die Suchleiste der Einstellungen ein.
   - Finden Sie die Einstellung **Editor: Linien**.
   - Fügen Sie Ihre bevorzugte Spalte zur Liste hinzu, z.B. `[80]`.
   - Dies zeigt eine vertikale Linie an der Spalte 80 an und bietet eine visuelle Anleitung für die Zeilenlängengrenze.

6. **(Optional) Einrückung des Umbruchs für Klarheit anpassen**:
   - Geben Sie "Einrückung des Umbruchs" in die Suchleiste der Einstellungen ein.
   - Finden Sie die Einstellung **Editor: Einrückung des Umbruchs**.
   - Setzen Sie diese auf `"indent"` (oder eine andere Option wie `"deepIndent"`) um umgebrochene Zeilen einzurücken.
   - Dies hilft, umgebrochene Zeilen von neuen Zeilen zu unterscheiden und macht es klarer, dass sie Fortsetzungen sind.

### Funktionsweise

- Nach der Konfiguration dieser Einstellungen wird jede Zeile, die die festgelegte Spalte (z.B. 80 Zeichen) überschreitet, umgebrochen und auf mehreren visuellen Zeilen angezeigt.
- Die umgebrochenen Zeilen werden eingerückt (wenn Sie die Einrückung des Umbruchs angepasst haben), sodass leicht erkennbar ist, dass sie Teil derselben logischen Zeile sind.
- Die vertikale Linie (wenn aktiviert) zeigt eine Linie an der festgelegten Spalte an und verstärkt die visuelle Grenze.
- Durch das Erkennen, dass eine Zeile umgebrochen ist, können Sie schnell feststellen, dass sie zu lang ist, da sie Ihre Spaltengrenze überschreitet.

### Beispiel

Angenommen, Sie haben eine Codezeile, die 100 Zeichen lang ist:
- Mit **Editor: Zeilenumbruch** auf `"wordWrapColumn"` und **Editor: Zeilenumbruch-Spalte** auf `80` wird die Zeile am 80. Zeichen umgebrochen.
- Der umgebrochene Teil wird eingerückt und die Linie (wenn aktiviert) zeigt an, wo die 80. Spalte ist.
- Diese Einstellung eliminiert die Notwendigkeit des horizontalen Scrollens und macht es klar, dass die Zeile 80 Zeichen überschreitet.

### Zusätzliche Hinweise

- Der Umbruch ist rein visuell; der eigentliche Code bleibt eine logische Zeile, sodass er sich nicht auf die Ausführung oder Formatierung Ihres Codes auswirkt.
- Wenn Sie strikte Zeilenlängenbeschränkungen durchsetzen möchten, sollten Sie Linters oder Formatierer zusammen mit diesen visuellen Einstellungen verwenden.
- Für schnelle Überprüfungen können Sie auch auf die Statusleiste in VSCode zurückgreifen, die die aktuelle Zeile und Spaltennummer anzeigt, aber der Umbruch und die Linie sollten für die visuelle Identifikation ausreichen.

Durch die Beachtung dieser Schritte können Sie in VSCode leicht erkennen, wenn Zeilen zu lang sind, ohne horizontal scrollen zu müssen, da sie an Ihrer festgelegten Spaltengrenze umgebrochen werden.