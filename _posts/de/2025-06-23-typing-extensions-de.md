---
audio: false
generated: true
lang: de
layout: post
title: Behebung des Problems mit dem typing-extensions-Paket
translated: true
type: note
---

### So beheben Sie den Fehler "Cannot uninstall typing-extensions None"

Wenn Sie diesen Fehler während der Paketinstallation mit pip erhalten, liegt das an einem Problem beim Deinstallieren des `typing-extensions`-Pakets. Die Fehlermeldung lautet:

```
error: uninstall-no-record-file
× Cannot uninstall typing-extensions None
╰─> The package's contents are unknown: no RECORD file was found for typing-extensions.
```

Dieser Fehler tritt auf, weil pip versucht, eine vorhandene Installation von `typing-extensions` zu deinstallieren (wahrscheinlich, um sie durch eine Version zu ersetzen, die von den Paketen, die Sie installieren, benötigt wird), aber nicht fortfahren kann, weil die RECORD-Datei fehlt. Die RECORD-Datei ist eine Metadatendatei, die pip verwendet, um die von einem Paket installierten Dateien zu verfolgen. Ohne sie weiß pip nicht, wie `typing-extensions` ordnungsgemäß zu deinstallieren ist. Das Installationsprotokoll gibt auch einen hilfreichen Hinweis:

```
hint: You might be able to recover from this via: pip install --force-reinstall --no-deps typing-extensions==4.14.0
```

Nachfolgend finden Sie eine Schritt-für-Schritt-Lösung, um dieses Problem zu beheben und Ihre Paketinstallation erfolgreich abzuschließen.

---

### Schritt 1: Das Problem verstehen
Das Protokoll zeigt, dass pip die folgenden Pakete installiert:
- `pyperclip`
- `typing-extensions`
- `packaging`
- `jmespath`

Während dieses Prozesses versucht pip, die vorhandene `typing-extensions`-Installation zu deinstallieren, weil eines der Pakete, die Sie installieren (oder eine vorhandene Abhängigkeit), wahrscheinlich eine bestimmte Version von `typing-extensions` benötigt. Die Deinstallation schlägt jedoch fehl, weil die RECORD-Datei für die aktuelle `typing-extensions`-Installation fehlt oder beschädigt ist. Dies kann passieren, wenn das Paket unsachgemäß installiert wurde, die RECORD-Datei gelöscht wurde oder die Installation in der Vergangenheit unterbrochen wurde.

Die Angabe "typing-extensions None" in der Fehlermeldung deutet darauf hin, dass pip die Version der vorhandenen Installation nicht bestimmen kann, was weiter auf ein Problem mit den Metadaten hindeutet.

---

### Schritt 2: Die `typing-extensions`-Installation reparieren
Um dies zu beheben, müssen Sie die beschädigte `typing-extensions`-Installation reparieren. Der vorgeschlagene Befehl aus dem Hinweis ist der beste Ansatz:

```bash
pip install --force-reinstall --no-deps typing-extensions==4.14.0
```

#### Was dieser Befehl bewirkt:
- **`pip install`**: Installiert das angegebene Paket.
- **`--force-reinstall`**: Zwingt pip dazu, `typing-extensions` neu zu installieren, auch wenn es bereits vorhanden ist, und überschreibt die vorhandene Installation.
- **`--no-deps`**: Verhindert, dass pip Abhängigkeiten von `typing-extensions` installiert. Da `typing-extensions` ein eigenständiges reines Python-Paket ohne Abhängigkeiten ist, gewährleistet dieses Flag eine saubere Neuinstallation, ohne andere Pakete zu beeinflussen.
- **`typing-extensions==4.14.0`**: Spezifiziert die Version 4.14.0, was wahrscheinlich die Version ist, die pip zu installieren versuchte, als der Fehler auftrat.

Die Ausführung dieses Befehls wird:
- `typing-extensions` Version 4.14.0 neu installieren.
- Eine ordnungsgemäße RECORD-Datei im Paketverzeichnis (typischerweise in `site-packages`) erstellen.
- Die beschädigte oder unvollständige Installation beheben.

#### Führen Sie den Befehl aus:
Öffnen Sie Ihr Terminal und führen Sie aus:

```bash
pip install --force-reinstall --no-deps typing-extensions==4.14.0
```

Nachdem dieser Befehl erfolgreich abgeschlossen wurde, sollte das `typing-extensions`-Paket korrekt mit allen notwendigen Metadaten installiert sein.

---

### Schritt 3: Die ursprüngliche Installation wiederholen
Sobald `typing-extensions` repariert ist, können Sie mit der Installation der Pakete fortfahren, die Sie ursprünglich installieren wollten. Dem Protokoll zufolge haben Sie wahrscheinlich einen Befehl wie diesen ausgeführt:

```bash
pip install pyperclip
```

Dieser Befehl hat wahrscheinlich die Installation von `pyperclip`, `typing-extensions`, `packaging` und `jmespath` ausgelöst, weil `pyperclip` oder ein anderes Paket Abhängigkeiten davon hat. Jetzt, da `typing-extensions` ordnungsgemäß installiert ist, sollte das Deinstallationsproblem nicht mehr auftreten.

#### Führen Sie den ursprünglichen Befehl aus:
Wiederholen Sie die Installation, indem Sie ausführen:

```bash
pip install pyperclip
```

Dies sollte nun ohne Fehler abgeschlossen werden und alle gesammelten Pakete erfolgreich installieren.

---

### Warum das funktioniert
- Die fehlende RECORD-Datei verhinderte, dass pip die alte `typing-extensions`-Installation deinstallieren konnte, was zum Fehlschlagen des Prozesses führte.
- Das erzwungene Neuinstallieren von `typing-extensions` mit der angegebenen Version stellt sicher, dass pip das Paket korrekt verwalten kann.
- Das Flag `--no-deps` hält die Reparatur auf `typing-extensions` beschränkt und vermeidet unnötige Änderungen an anderen Paketen.

---

### Zusätzliche Hinweise
- **Sicherheit**: Da `typing-extensions` ein reines Python-Paket und keine System-Level-Abhängigkeit ist, ist das erzwungene Neuinstallieren sicher und wird Ihre Python-Umgebung nicht stören.
- **Versionsbestätigung**: Der Hinweis spezifiziert die Version 4.14.0, die wahrscheinlich von einem der Pakete, die Sie installieren, benötigt wird. Wenn Sie eine andere Version benötigen, können Sie die Anforderungen von `pyperclip`, `packaging` oder `jmespath` prüfen (z.B. über deren Dokumentation oder `pip show <paket>` nach der Installation).
- **Manuelle Bereinigung (Nicht empfohlen)**: Sie könnten den `typing-extensions`-Ordner manuell aus `site-packages` löschen, aber das ist riskanter und unnötig, da `pip --force-reinstall` dies sauber erledigt.

---

### Finale Schritte
1. Reparieren Sie `typing-extensions`:
   ```bash
   pip install --force-reinstall --no-deps typing-extensions==4.14.0
   ```
2. Installieren Sie Ihre Pakete:
   ```bash
   pip install pyperclip
   ```

Nachdem Sie diese Schritte befolgt haben, sollte der Fehler behoben sein und Ihre Paketinstallation erfolgreich abgeschlossen werden. Wenn Sie weitere Probleme haben, teilen Sie bitte das aktualisierte Protokoll für zusätzliche Unterstützung mit!