---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Jagd auf das böse Byte
translated: true
type: note
---

### Warum das das fehlerhafte Byte nicht gefunden hat
Die `hexdump`-Ausgabe, die Sie erhalten haben, stimmte mit **dem Datei-Offset** (`000008d0`) überein, nicht mit einem `\x8D`-Byte im tatsächlichen Inhalt. Grep durchsucht die gesamte Zeile nach Text, und "8d" erscheint in der Hex-Adresse (z.B. `08d0`), daher hat es diese irrelevante Zeile ausgegeben. Die Datenbytes dort (`6f 67 20 ...`) sind nur normale ASCII-Zeichen für `"og = og_images[i"`, keine Probleme.

### Bessere Methoden, um das `\x8D`-Byte zu finden
Versuchen Sie diese Befehle in Ihrem Projektverzeichnis (neben `_layouts/default.html`). Sie durchsuchen die Bytes der Datei direkt.

1. **Verbessertes Hexdump (Nach Byte in den Daten grepen)**:
   Dies sucht nach ` 8d ` (Leerzeichen drumherum, um Hex-Bytes und nicht Offsets zu treffen):
   ```
   hexdump -C _layouts/default.html | grep ' 8d '
   ```
   - Wenn es etwas findet, sehen Sie den Offset (linke Spalte) und die umgebenden Bytes. Notieren Sie den Offset und springen Sie dann zu dieser Position in Ihrem Editor (z.B. VS Code: Strg+G > Byte-Offset / 16 für ungefähre Zeile).
   - Beispielausgabe bei einem Treffer: `00001234  ...  8d  20  61  62  ... |... ab...|`

2. **`xxd` verwenden (Oft besser als Hexdump)**:
   macOS hat `xxd` integriert:
   ```
   xxd _layouts/default.html | grep 8d
   ```
   - Ähnlich: Findet "8d" in Hex-Bytes. Wenn keine Ausgabe, ist das Byte nicht vorhanden (selten, aber möglich, wenn es in einer anderen Datei ist).

3. **Binäres Grep (Direkte Bytesuche)**:
   ```
   grep -a -o -P '\x8d' _layouts/default.html | hexdump -C
   ```
   - Dies extrahiert exakte Treffer für das Byte und gibt sie in Hex aus. Wenn leer, kein `\x8D`.

4. **Ruby One-Liner (Präzise Position)**:
   Wie ich zuvor vorgeschlagen habe – führen Sie dies aus, um den Byte-Index zu erhalten:
   ```
   ruby -e "File.open('_layouts/default.html', 'rb') { |f| f.read.each_byte.with_index { |b, i| puts \"Found at byte #{i}: #{b.chr(Encoding::ASCII_8BIT).inspect}\" if b == 0x8D } }"
   ```
   - Gibt aus z.B.: `Found at byte 1234: "\x8D"`. Dann bearbeiten: Datei öffnen, zu Zeichen ~1234 gehen (oder Zeile = 1234/80 ungefähr) und das unsichtbare Zeichen löschen (es könnte wie nichts aussehen; Bereich darum herum auswählen/löschen).

### Wenn keine Treffer?
- Das `\x8D` könnte in einer **anderen Datei** sein (z.B. ein Post in `_posts/`, der via `{{ content }}` im Layout gerendert wird). Scannen Sie die gesamte Site:
  ```
  find . -name "*.md" -o -name "*.html" | xargs grep -l $'\x8D'
  ```
  (Oder verwenden Sie das Ruby-Skript für jede verdächtige Datei.)
- Oder es ist ein BOM/unsichtbar am Dateianfang: In Editor öffnen, erste Zeile löschen, falls leer, neu als UTF-8 speichern.

Sobald Sie es entfernt haben, führen Sie `bundle exec jekyll serve --incremental` erneut aus. Wenn es immer noch hakt, posten Sie die Ausgabe von einem dieser Befehle (oder dem Ruby-Befehl), und wir kriegen es hin.

[Hexdump-Tipps für die Bytesuche](https://unix.stackexchange.com/questions/38331/finding-bad-characters-in-hex-dump)