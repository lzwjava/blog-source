---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Dateiinhalt in Vi kopieren
translated: true
type: note
---

## Kopieren (oder Verschieben) des gesamten Inhalts einer Datei in eine neue Datei in Vi

Basierend auf Ihrer Vi-Nutzung gehe ich davon aus, dass Sie den gesamten Inhalt einer Datei auswählen und kopieren/löschen möchten, um ihn dann in eine neue Datei einzufügen. Vi hat keine direkte "Alles auswählen"-Funktion wie GUI-Editoren, aber Sie können dies effizient im **Befehlsmodus** erreichen (drücken Sie `Esc`, um sicherzugehen, dass Sie sich darin befinden). Ich behandele sowohl **Kopieren** (Original bleibt unverändert) als auch **Ausschneiden/Löschen** (Inhalt wird verschoben).

### Schritt-für-Schritt: Gesamten Inhalt in eine neue Datei kopieren
1. Öffnen Sie Ihre Quelldatei:  
   ```
   vi oldfile.txt
   ```

2. Den gesamten Inhalt yanken (kopieren):  
   - Tippen Sie `gg` (gehe zum Anfang der Datei).  
   - Tippen Sie dann `yG` (yankt von der aktuellen Position bis zum Ende der Datei).  
   *Alternative (Vim-spezifisch, funktioniert in Red Hats vim):* Tippen Sie `:1,$y` und drücken Sie `Enter` (yankt Zeilen 1 bis Ende).

3. Öffnen Sie die neue Datei:  
   - Tippen Sie `:e newfile.txt` und drücken Sie `Enter` (erstellt/öffnet die neue Datei).

4. Den Inhalt einfügen:  
   - Tippen Sie `p` (fügt nach dem Cursor ein; da die Datei leer ist, wird oben eingefügt).  
   *Alternative:* Tippen Sie `P`, um vor dem Cursor einzufügen.

5. Die neue Datei speichern und verlassen:  
   - Tippen Sie `:wq` und drücken Sie `Enter`.

Die Originaldatei bleibt unverändert.

### Schritt-für-Schritt: Gesamten Inhalt löschen und in eine neue Datei einfügen (Verschieben)
Dies löscht den Originalinhalt nach dem Kopieren.

1. Öffnen Sie Ihre Quelldatei:  
   ```
   vi oldfile.txt
   ```

2. Zuerst den gesamten Inhalt yanken (kopieren):  
   - `gg` dann `yG` (oder `:1,$y`).

3. Den gesamten Inhalt löschen:  
   - Tippen Sie `gg` (zum Anfang).  
   - Dann `dG` (löscht von der aktuellen Position bis zum Ende).  
   *Alternative:* Tippen Sie `:%d` und drücken Sie `Enter` (löscht alle Zeilen).  
   Bei Bedarf speichern: `:w` (überschreibt die nun leere Datei).

4. Öffnen Sie die neue Datei:  
   - Tippen Sie `:e newfile.txt` und drücken Sie `Enter`.

5. Einfügen:  
   - Tippen Sie `p`.

6. Speichern und verlassen:  
   - `:wq`.

### Schnelle Tipps
- Falls Sie versehentlich löschen, ohne vorher zu yanken, verwenden Sie `u` zum Rückgängig machen.
- Um dies dateiübergreifend zu tun, ohne jedes Mal eine neue zu öffnen: Yanken in der ersten Datei, dann `vi newfile.txt` verwenden, einfügen und speichern.
- Bei großen Dateien sind diese Befehle schnell, da Vi Puffer effizient handhabt.

Üben Sie an Testdateien, um den Dreh rauszukriegen!

[How to Copy Text to Another File in Vim](https://stackoverflow.com/questions/1239801/how-to-copy-to-the-end-of-the-line-in-vim)  
[Vim: Yank (copy) entire file](https://vim.fandom.com/wiki/Yank_%28copy%29_the_entire_file)