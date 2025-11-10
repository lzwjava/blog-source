---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: PyGetWindow Schnellstartanleitung
translated: true
type: note
---

### Installation
PyGetWindow ist eine Python-Bibliothek zur Manipulation und Abfrage von Fenstern auf mehreren Plattformen (Windows, macOS und Linux). Installieren Sie es über pip:

```bash
pip install pygetwindow
```

### Importieren des Moduls
Importieren Sie das Modul in Ihrem Python-Skript:

```python
import pygetwindow as gw
```

### Abrufen von Fensterobjekten
PyGetWindow repräsentiert Fenster als `Window`-Objekte. Sie können Fenster anhand ihres Titels, Prozesses oder anderer Attribute abrufen.

- **Alle Fensterobjekte abrufen**:  
  Verwenden Sie `gw.getAllWindows()`, um eine Liste aller geöffneten Fenster zurückzugeben.

- **Fenster nach Titel abrufen**:  
  Verwenden Sie `gw.getWindowsWithTitle(title)` oder `gw.getFirstWindowWithTitle(title)` für teilweise oder exakte Übereinstimmungen.

- **Aktives Fenster abrufen**:  
  Verwenden Sie `gw.getActiveWindow()`, um das aktuell fokussierte Fenster zu erhalten.

Beispiel:
```python
windows = gw.getAllWindows()
active = gw.getActiveWindow()
notepad = gw.getWindowsWithTitle('Notepad')  # Liste der Fenster mit 'Notepad' im Titel
```

### Häufige Methoden für Fensterobjekte
Sobald Sie ein `Window`-Objekt haben, können Sie auf Eigenschaften und Methoden zugreifen wie:

- **Eigenschaften**: `title`, `left`, `top`, `width`, `height`, `isMinimized`, `isMaximized`, `isActive`.
- **Methoden**:
  - `activate()`: Bringt das Fenster in den Vordergrund und macht es aktiv.
  - `maximize()` / `minimize()` / `restore()` / `close()`: Steuert den Fensterzustand.
  - `resize() / move()`: Passt Größe und Position an.

Beispiel:
```python
if notepad:
    win = notepad[0]
    print(win.title)  # Ausgabe: z.B. 'Untitled - Notepad'
    win.activate()
    win.maximize()
    win.move(100, 100)  # An Position (100, 100) verschieben
    win.resize(800, 600)  # Auf 800x600 vergrößern/verkleinern
```

### Umgang mit mehreren Plattformen
- Unter Windows und macOS werden native APIs verwendet.
- Unter Linux ist es auf X11 oder Wayland-Unterstützung angewiesen; stellen Sie sicher, dass Ihr System dies installiert hat (z.B. `x11-utils` auf Ubuntu).
- Wenn eine Methode auf Ihrem Betriebssystem nicht unterstützt wird, kann ein `NotImplementedError` ausgelöst werden.

### Beispiele
Hier sind einige praktische Code-Ausschnitte:

1. **Alle Fenstertitel ausgeben**:
   ```python
   for win in gw.getAllWindows():
       print(win.title)
   ```

2. **Ein bestimmtes Fenster schließen**:
   ```python
   firefox_wins = gw.getWindowsWithTitle('Mozilla Firefox')
   if firefox_wins:
       firefox_wins[0].close()
   ```

3. **Mehrere Fenster verschieben und in der Größe ändern**:
   ```python
   windows = gw.getAllWindows()
   for i, win in enumerate(windows[:3]):  # Ersten 3 Fenster
       win.move(50 * i, 50 * i)
       win.resize(400, 400)
   ```

Für erweiterte Verwendungszwecke lesen Sie die [offizielle Dokumentation](https://pygetwindow.readthedocs.io/). Wenn Sie auf plattformspezifische Probleme stoßen, überprüfen Sie Systemberechtigungen oder Abhängigkeiten wie `xdotool` unter Linux.