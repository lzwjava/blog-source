---
audio: false
date: 2025-09-10
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Verwendung des Python -m Flags für Module
translated: true
type: note
---

Ja, `-m` bedeutet **ein Modul als Skript ausführen**. Lassen Sie uns das anhand Ihrer Beispiele aufschlüsseln:

### `python -m unittest`

Dies weist Python an:

* Das Modul `unittest` zu suchen (es ist Teil der Standardbibliothek).
* Es so auszuführen, als wäre es ein Skript (das bewirkt `-m`).
* Deshalb können Sie Dinge wie folgt tun:

  ```bash
  python -m unittest test_example.py
  python -m unittest discover
  ```

  Dies funktioniert, obwohl Sie keine eigenständige `unittest`-Datei in Ihrem Projekt haben – es ist ein Standardbibliotheksmodul.

### `python -m pip`

Dies folgt demselben Muster:

* Es sucht das `pip`-Modul (mit Python installiert).
* Führt es aus, als wäre es der `pip`-Executable.
* Daher ist `python -m pip install requests` der "offizielle", sichere Weg, pip auszuführen, weil es sicherstellt, dass Sie den pip des selben Python-Interpreters verwenden, der zu Ihrem `python` gehört.
  (Manchmal kann `pip` auf Ihrem System auf eine andere Python-Installation verweisen, daher vermeidet `python -m pip` Verwechslungen.)

### Unterschied zu `python test_xx.py`

Wenn Sie folgendes tun:

```bash
python test_xx.py
```

führen Sie diese spezifische Datei direkt aus und verwenden nicht die Test Discovery oder den Runner von `unittest`.

* Wenn `test_xx.py` ein `unittest.main()` am Ende hat, werden Tests ausgeführt.
* Aber wenn Sie möchten, dass Python automatisch alle Tests in einem Verzeichnis findet, verlassen Sie sich normalerweise auf `python -m unittest discover`.

---

✅ **Zusammenfassung**:

* `-m` = ein Modul als Skript ausführen.
* `python -m unittest` führt den Test Runner der Standardbibliothek aus.
* `python -m pip` stellt sicher, dass pip zum selben Python-Interpreter gehört.
* `python test_xx.py` führt nur eine Datei aus, nicht den allgemeinen Test Runner.

Möchten Sie, dass ich Ihnen auch zeige, wie **pytest** dies anders handhabt, da Sie vielleicht `unittest` vs. `pytest` vergleichen möchten?