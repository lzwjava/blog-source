---
audio: false
generated: true
lang: de
layout: post
title: VSCode Zeilenumbruch
translated: true
type: note
---

Um in VSCode Zeilen umbrechen zu lassen, sodass Sie leicht erkennen können, wenn Zeilen zu lang sind, können Sie die Word-Wrap-Einstellungen so konfigurieren, dass Zeilen an einer bestimmten Spalte umgebrochen werden. So geht's:

### Schritte zum Aktivieren des Zeilenumbruchs an einer bestimmten Spalte

1. **Öffnen Sie die Einstellungen in VSCode**:
   - Drücken Sie `Strg + ,` (oder `Cmd + ,` auf macOS), um den Einstellungsbereich zu öffnen.
   - Alternativ gehen Sie zu `Datei` > `Einstellungen` > `Einstellungen`.

2. **Suchen Sie nach den Word-Wrap-Einstellungen**:
   - Tippen Sie im Einstellungsbereich "word wrap" in die Suchleiste.
   - Suchen Sie die Einstellung mit der Bezeichnung **Editor: Word Wrap**.

3. **Setzen Sie Word Wrap auf "wordWrapColumn"**:
   - Ändern Sie die Einstellung **Editor: Word Wrap** auf `"wordWrapColumn"`.
   - Diese Option ermöglicht es, Zeilen an einer bestimmten Spalte umzubrechen.

4. **Geben Sie die Spaltenbegrenzung an**:
   - Suchen Sie nach der Einstellung **Editor: Word Wrap Column** (sie erscheint, wenn "wordWrapColumn" ausgewählt ist).
   - Setzen Sie diese auf Ihre bevorzugte Spaltenbegrenzung, z.B. `80`.
   - Das bedeutet, dass jede Zeile, die länger als 80 Zeichen ist, umgebrochen wird.

5. **(Optional) Fügen Sie ein vertikales Lineal zur visuellen Orientierung hinzu**:
   - Suchen Sie in der Einstellungs-Suchleiste nach "rulers".
   - Finden Sie die Einstellung **Editor: Rulers**.
   - Fügen Sie Ihre bevorzugte Spalte zur Liste hinzu, z.B. `[80]`.
   - Dies zeigt eine vertikale Linie bei Spalte 80 an und bietet so einen visuellen Hinweis auf die maximale Zeilenlänge.

6. **(Optional) Passen Sie den Umbrucheinzug für bessere Lesbarkeit an**:
   - Suchen Sie in der Einstellungs-Suchleiste nach "wrapping indent".
   - Finden Sie die Einstellung **Editor: Wrapping Indent**.
   - Setzen Sie sie auf `"indent"` (oder eine andere Option wie `"deepIndent"`), um umbrochene Zeilen einzuziehen.
   - Dies hilft dabei, umbrochene Zeilen von neuen Zeilen zu unterscheiden, und macht klar, dass es sich um Fortsetzungen handelt.

### So funktioniert es

- Nachdem Sie diese Einstellungen konfiguriert haben, wird jede Zeile, die die angegebene Spalte (z.B. 80 Zeichen) überschreitet, umbrochen und auf mehreren visuellen Zeilen angezeigt.
- Die umbrochenen Zeilen werden eingerückt (falls Sie den Umbrucheinzug angepasst haben), sodass leicht zu erkennen ist, dass sie zur selben logischen Zeile gehören.
- Das vertikale Lineal (falls aktiviert) zeigt eine Linie bei der angegebenen Spalte an und verstärkt so die visuelle Begrenzung.
- Indem Sie bemerken, dass eine Zeile umbrochen ist, können Sie schnell erkennen, dass sie zu lang ist, da sie Ihre Spaltenbegrenzung überschreitet.

### Beispiel

Angenommen, Sie haben eine Codezeile, die 100 Zeichen lang ist:
- Wenn **Editor: Word Wrap** auf `"wordWrapColumn"` und **Editor: Word Wrap Column** auf `80` gesetzt ist, wird die Zeile beim 80. Zeichen umgebrochen.
- Der umbrochene Teil wird eingerückt, und das Lineal (falls aktiviert) zeigt an, wo sich die 80. Spalte befindet.
- Dieser Aufbau macht horizontales Scrollen überflüssig und macht deutlich, dass die Zeile 80 Zeichen überschreitet.

### Zusätzliche Hinweise

- Der Umbruch ist rein visuell; der eigentliche Code bleibt eine logische Zeile, daher hat dies keine Auswirkungen darauf, wie Ihr Code ausgeführt oder formatiert wird.
- Wenn Sie strenge Beschränkungen der Zeilenlänge durchsetzen möchten, sollten Sie die Verwendung von Linters oder Formatierern zusätzlich zu diesen visuellen Einstellungen in Betracht ziehen.
- Für schnelle Überprüfungen können Sie auch auf die Statusleiste in VSCode verweisen, die die aktuelle Zeilen- und Spaltennummer anzeigt, aber der Umbruch und das Lineal sollten für die visuelle Identifikation ausreichen.

Indem Sie diese Schritte befolgen, können Sie leicht erkennen, wann Zeilen in VSCode zu lang sind, ohne horizontal scrollen zu müssen, da sie an Ihrer festgelegten Spaltenbegrenzung umgebrochen werden.