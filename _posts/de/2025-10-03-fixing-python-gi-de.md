---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Reparieren kaputter Python-GI-Bindungen
translated: true
type: note
---

### Aktualisierte Diagnose
Basierend auf den neuen Details hat Ihre Python-3.13.7-Installation (wahrscheinlich manuell oder über PPA/Quellcode) die GObject Introspection (GI)-Bindungen des Systems beschädigt. Die `_gi`-C-Erweiterung des `gi`-Moduls ist für die Standard-Python-Version Ihrer Distribution (wahrscheinlich 3.10 oder 3.11, basierend auf den Verzeichnissen in `/usr/lib/python`) kompiliert, nicht für 3.13. Dies verursacht den zirkulären Importfehler, wenn `gnome-terminal` (ein Python-Skript) versucht, es zu laden. Das Multi-Version-Setup in `/usr/lib/python` bestätigt diese Fehlanpassung – Systempakete wie `python3-gi` sind noch nicht für 3.13 gebaut (es ist für die meisten Distributionen Stand 2025 zu neu).

Die UFW-Logs bleiben irrelevantes Rauschen.

### Empfohlene Lösung: Zurück zur System-Standard-Python-Version
Die sauberste Lösung ist, `/usr/bin/python3` wieder auf den Standard Ihrer Distribution (z.B. 3.10) umzustellen und dann die GI-Bindungen neu zu installieren. Dies vermeidet Hacks wie das Kopieren von .so-Dateien, die zu Inkonsistenzen führen können.

1. **Standard-Python-Version identifizieren und wechseln** (verwenden Sie `update-alternatives`, falls konfiguriert; andernfalls manueller Symlink):
   ```
   # Prüfen, ob Alternatives eingerichtet sind
   sudo update-alternatives --config python3
   ```
   - Falls Optionen aufgelistet werden, wählen Sie die mit der niedrigsten Priorität (normalerweise der Distributionsstandard, wie 3.10).
   - Falls keine Alternatives vorhanden sind (häufig bei Standard-Ubuntu), manuell zurücksetzen:
     ```
     # Angenommen, der Standard ist 3.10 (üblich für Ubuntu 22.04; wechseln Sie zu 3.11, falls das Ihre Basis ist)
     sudo rm /usr/bin/python3
     sudo ln -s /usr/bin/python3.10 /usr/bin/python3
     ```
   - Überprüfen: `python3 --version` sollte jetzt 3.10.x (oder Ihren Standard) anzeigen.

2. **GI- und GNOME Terminal-Pakete neu installieren**:
   ```
   sudo apt update
   sudo apt install --reinstall python3-gi gir1.2-glib-2.0 gnome-terminal
   ```

3. **Test**:
   ```
   python3 -c "from gi.repository import GLib, Gio; print('GI OK')"
   gnome-terminal
   ```
   - Falls der Python-Test erfolgreich ist, das Terminal aber immer noch fehlschlägt, setzen Sie dessen Konfiguration zurück: `dconf reset -f /org/gnome/terminal/`.

### Falls Sie Python 3.13 behalten möchten
- Dies ist schwieriger, da offizielles `python3-gi` für 3.13 noch nicht existiert. Sie müssten PyGObject aus dem Quellcode kompilieren:
  1. Build-Abhängigkeiten installieren: `sudo apt install libgirepository1.0-dev libcairo2-dev pkg-config python3.13-dev`.
  2. PyGObject herunterladen und bauen: Folgen Sie dem [offiziellen Guide](https://pygobject.gnome.org/install.html) mit `--prefix=/usr/local`.
  3. Dies riskiert jedoch, andere System-Tools zu brechen – setzen Sie bei Problemen zurück.
- Oder, hackhaft die `_gi`-Erweiterung kopieren (langfristig nicht empfohlen):
  ```
  cd /usr/lib/python3/dist-packages/gi/
  sudo cp _gi.cpython-3[01]m*.so _gi.cpython-313m-x86_64-linux-gnu.so  # Passen Sie '3[01]' an Ihren Standard an (3.10 oder 3.11)
  ```
  Dann `python3-gi` wie oben neu installieren.

### Vorbeugung
- Überschreiben Sie `/usr/bin/python3` nicht manuell – verwenden Sie Virtualenvs (`python3 -m venv myenv`) für Projekte, die 3.13 benötigen.
- Falls Sie 3.13 über das deadsnakes PPA installiert haben, entfernen Sie es und bleiben Sie bei der Distributions-Python-Version.

Falls dies das Problem nicht behebt, führen Sie `ls -l /usr/bin/python*` und `dpkg -l | grep python3 | grep -E 'gi|default'` aus und teilen Sie die Ausgabe.

[gnome-terminal will not start after trying to install newer version of Python 3](https://askubuntu.com/questions/880188/gnome-terminal-will-not-start-after-trying-to-install-newer-version-of-python-3)  
[ImportError: cannot import name '_gi' from partially initialized module 'gi'](https://stackoverflow.com/questions/59838238/importerror-cannot-import-name-gi-from-partially-initialized-module-gi-mo)  
[Why won't terminal open?](https://www.reddit.com/r/Ubuntu/comments/1f9qh0a/why_wont_terminal_open/)