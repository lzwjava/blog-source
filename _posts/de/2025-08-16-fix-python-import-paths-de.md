---
audio: false
generated: true
image: false
lang: de
layout: post
title: Behebung von Python-Modul-Importpfaden
translated: true
type: note
---

Die kurze Antwort: Du brauchst `sys` hier, um den Python-Modul-Suchpfad (`sys.path`) zu ändern, bevor du `from scripts.create.delete import delete_md` ausführst.

---

### Warum `sys` benötigt wird

* Python sucht nach Modulen/Paketen für den Import in einer Liste von Verzeichnissen, die in `sys.path` gespeichert sind.
* Standardmäßig enthält diese:

  * Das Verzeichnis des aktuellen Skripts.
  * Standard-Bibliotheksverzeichnisse.
  * Installierte site-packages.
* Wenn sich deine `scripts/create/delete.py` Datei nicht an einem dieser Standardorte befindet, schlägt der Import mit `ModuleNotFoundError` fehl.

Daher macht der Code:

```python
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
```

Das bedeutet:

* Nimm den absoluten Pfad der aktuellen Datei (`__file__`).
* Gehe drei Verzeichnisse nach oben.
* Füge dieses Verzeichnis zu `sys.path` hinzu.

Danach kann Python `scripts.create.delete` auflösen, als ob es installiert oder im Projekt-Root wäre.

---

### Ohne `sys`

Wenn dein Projekt so aufgebaut ist:

```
project/
├── scripts/
│   └── create/
│       └── delete.py
└── tools/
    └── myscript.py   <-- du führst dieses hier aus
```

und du `myscript.py` direkt ausführst, weiß Python nicht automatisch, dass `project/` das Root-Verzeichnis ist. Der Import schlägt fehl, es sei denn, du:

* Führst es mit `PYTHONPATH=...` aus (z.B. `PYTHONPATH=.. python myscript.py`), oder
* Packst das Projekt ein und installierst es (`pip install -e .`), oder
* Fügst den Pfad dynamisch im Code mit `sys.path.append(...)` hinzu (wie hier geschehen).

---

👉 Also wird `sys` rein benötigt, um **den Import-Pfad zur Laufzeit zu manipulieren**, damit du Module relativ zu deinem Projekt-Root importieren kannst.

Möchtest du, dass ich dir auch einige **sauberere Alternativen** zeige, um das manuelle Hantieren mit `sys.path` zu vermeiden?