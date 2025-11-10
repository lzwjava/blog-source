---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Windows Toast-Benachrichtigungen mit Python
translated: true
type: note
---

### Was ist win10toast?
win10toast ist eine leichtgewichtige Python-Bibliothek, mit der Sie Toast-Benachrichtigungen (Pop-up-Warnungen) unter Windows 10 aus Ihren Python-Skripten senden können. Sie ist nützlich für Benutzerbenachrichtigungen in Desktop-Anwendungen oder Skripten, ähnlich wie native Windows-Toasts.

### Voraussetzungen
- Python 3.x installiert.
- Windows 10 (es nutzt Windows-spezifische APIs).
- Keine zusätzlichen Abhängigkeiten außer Python.

### Installation
Installieren Sie die Bibliothek über pip (den Python-Paketmanager):

```
pip install win10toast
```

Wenn Sie eine virtuelle Umgebung verwenden, aktivieren Sie diese zuerst.

### Grundlegende Verwendung
1. Importieren Sie das Modul:
   ```python
   from win10toast import ToastNotifier
   ```

2. Erstellen Sie eine `ToastNotifier`-Instanz und rufen Sie deren `show_toast`-Methode auf, um eine Benachrichtigung anzuzeigen:
   ```python
   toaster = ToastNotifier()
   toaster.show_toast("Titel", "Nachricht", icon_path=None, duration=5)
   ```
   - **Titel**: Eine Zeichenkette für die Überschrift der Benachrichtigung.
   - **Nachricht**: Eine Zeichenkette für den Haupttext der Benachrichtigung.
   - **icon_path**: Optionaler Pfad zu einer .ico- oder .png-Datei für das Benachrichtigungssymbol (z.B. `"pfad/zum/symbol.ico"`). Weglassen, wenn kein Symbol gewünscht ist.
   - **duration**: Zeit in Sekunden, für die der Toast angezeigt wird (Standard ist 5; Windows kann diesen Wert überschreiben).

Die Benachrichtigung erscheint im Action Center und als Pop-up.

### Erweiterte Verwendung
- **Symbol anpassen**: Verwenden Sie eine Bilddatei (128x128 Pixel werden für beste Qualität empfohlen).
- **Klick-Ereignisse behandeln**: Übergeben Sie eine Callback-Funktion (eingeschränkte Unterstützung; das Verhalten bei Klick ist grundlegend).
- **Mehrere Benachrichtigungen**: Instanziieren Sie `ToastNotifier` einmal und verwenden Sie es wiederholt, um mehrere Toasts zu senden.
- **Fehlerbehandlung**: Umschließen Sie den Code mit try-except, um mögliche Windows-API-Probleme abzufangen, z.B. wenn Benachrichtigungen deaktiviert sind.

Beispiel mit Symbol und Fehlerbehandlung:
```python
from win10toast import ToastNotifier
import os

try:
    toaster = ToastNotifier()
    icon = "C:\\pfad\\zum\\symbol.ico"  # Ersetzen Sie dies mit dem tatsächlichen Pfad
    toaster.show_toast("Warnung!", "Ihr Skript wurde beendet.", icon_path=icon, duration=10)
except Exception as e:
    print(f"Benachrichtigung fehlgeschlagen: {e}")
```

### Einschränkungen und Tipps
- Benachrichtigungen erfordern, dass das Action Center von Windows 10 aktiviert ist (Einstellungen > System > Benachrichtigungen & Aktionen).
- Für komplexere Funktionen (z.B. Aktionen oder Bilder) sollten Alternativen wie plyer oder winrt (Teil des modernen Windows SDK) in Betracht gezogen werden.
- Wenn Benachrichtigungen nicht erscheinen, überprüfen Sie die Windows-Einstellungen für den Fokusmodus (Focus Assist) oder versuchen Sie, das Skript als Administrator auszuführen.

Die vollständige Dokumentation finden Sie im [win10toast GitHub-Repository](https://github.com/Charnelx/win10toast). Wenn Sie auf Probleme stoßen, geben Sie Fehlerdetails für eine maßgeschneiderte Hilfe an.