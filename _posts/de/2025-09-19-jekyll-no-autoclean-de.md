---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Jekyll Build verfügt nicht über eine Auto-Clean-Funktion
translated: true
type: note
---

Jekyll selbst hat kein `--replace`- oder `--refresh`-Flag. Jeder `jekyll build`-Lauf schreibt die generierten Dateien in den von Ihnen angegebenen `--destination`-Ordner (oder überschreibt sie), **entfernt jedoch nicht automatisch alte Dateien**, die in Ihrer Quelle nicht mehr existieren. Das bedeutet, dass veraltete Dateien verbleiben können.

Wenn Sie eine saubere Build-Ausgabe wünschen, müssen Sie das Zielverzeichnis selbst löschen, bevor Sie `jekyll build` ausführen. Zwei gängige Ansätze:

**1. Manuelle Bereinigung in Ihrem Skript**
Löschen Sie vor dem Aufruf von `jekyll build` das Zielverzeichnis:

```python
import shutil

def run_jekyll(destination: str, extra_args: list[str]) -> int:
    # Alte Dateien entfernen
    dest_path = Path(destination)
    if dest_path.exists():
        shutil.rmtree(dest_path)

    command = [
        "jekyll",
        "build",
        "--destination",
        destination,
        *extra_args,
    ]
    completed = subprocess.run(command, check=False)
    return completed.returncode
```

**2. Jekylls eigenes `_site` verwenden**
Wenn Sie Jekyll das standardmäßige `_site`-Verzeichnis unter Ihrem Projektstamm verwenden lassen (anstatt eines benutzerdefinierten `--destination`), ist `jekyll clean` verfügbar, um die Ausgabe vor dem Neuerstellen zu löschen:

```bash
jekyll clean && jekyll build
```

Aber `jekyll clean` kennt nur `_site`, nicht einen benutzerdefinierten Ordner.

---

Zusammenfassend:

* Es gibt kein eingebautes `--replace`.
* Wenn Sie ein benutzerdefiniertes Ziel verwenden (wie in Ihrem Skript), sollten Sie es vor dem Build explizit löschen, wenn Sie eine frische Ausgabe wünschen.

Möchten Sie, dass ich Ihr Skript so anpasse, dass es eine `--clean`-Option (wie `jekyll clean`) hat, die das Zielverzeichnis automatisch vor dem Build löscht?