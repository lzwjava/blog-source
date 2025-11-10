---
audio: false
generated: true
lang: de
layout: post
title: Zugriff auf die Zwischenablage von Python unter Ubuntu
translated: true
type: note
---

Um aus der Zwischenablage (Pasteboard) in Ubuntu mit Python zu lesen, können Sie Bibliotheken wie `pyperclip` verwenden oder mit System-Zwischenablage-Dienstprogrammen wie `xclip` oder `xsel` interagieren. Nachfolgend finden Sie zwei gängige Ansätze:

### Ansatz 1: Verwendung von `pyperclip`
`pyperclip` ist eine plattformübergreifende Python-Bibliothek für den Zugriff auf die Zwischenablage.

1. **pyperclip installieren**:
   ```bash
   pip install pyperclip
   ```

2. **Python-Code zum Lesen aus der Zwischenablage**:
   ```python
   import pyperclip

   # Inhalt der Zwischenablage lesen
   clipboard_content = pyperclip.paste()
   print(clipboard_content)
   ```

3. **Hinweise**:
   - Stellen Sie sicher, dass `xclip` oder `xsel` auf Ubuntu installiert ist, da `pyperclip` darauf angewiesen ist:
     ```bash
     sudo apt update
     sudo apt install xclip xsel
     ```
   - Diese Methode ist einfach und funktioniert plattformübergreifend.

### Ansatz 2: Direkte Verwendung von `xclip`
Wenn Sie lieber direkt mit der System-Zwischenablage interagieren möchten, können Sie `xclip` verwenden.

1. **xclip installieren**:
   ```bash
   sudo apt update
   sudo apt install xclip
   ```

2. **Python-Code zum Lesen aus der Zwischenablage mit `xclip`**:
   ```python
   import subprocess

   # Inhalt der Zwischenablage lesen
   process = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)
   clipboard_content = process.stdout
   print(clipboard_content)
   ```

3. **Hinweise**:
   - Dieser Ansatz ruft das `xclip`-Kommandozeilenwerkzeug direkt auf.
   - Verwenden Sie `-selection clipboard` für die moderne Zwischenablage (Strg+C/Strg+V) oder `-selection primary` für die Mausauswahl-Zwischenablage.
   - Stellen Sie sicher, dass `xclip` installiert ist.

### Empfehlungen
- **Verwenden Sie `pyperclip`** für Einfachheit und Portabilität, es sei denn, Sie haben spezifische Gründe, `xclip` oder `xsel` zu verwenden.
- Beide Methoden erfordern, dass `xclip` oder `xsel` für den Zugriff auf die Zwischenablage unter Ubuntu installiert ist.
- Wenn der Inhalt der Zwischenablage kein Text ist (z. B. ein Bild), funktionieren diese Methoden möglicherweise nicht wie erwartet, und Sie benötigen eine Bibliothek wie `pyclip` oder eine zusätzliche Behandlung für Nicht-Text-Daten.

Getestet auf Ubuntu 22.04 mit Python 3.10. Wenn Sie auf Probleme stoßen, stellen Sie sicher, dass die erforderlichen Tools (`xclip` oder `xsel`) installiert sind und die Zwischenablage Textdaten enthält.