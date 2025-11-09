---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Hinzufügen ausführbarer Skripte zu Pip-Paketen
translated: true
type: note
---

### Erstellung ausführbarer Skripte in einem Python-Pip-Paket

Um ausführbare Skripte (d.h. Kommandozeilen-Tools) in ein Python-Paket aufzunehmen, das über `pip` installiert werden kann, definiert man **Entry Points** in der Konfigurationsdatei Ihres Pakets. Dies ermöglicht Benutzern, Ihre Skripte direkt nach der Installation auszuführen (z.B. `my-script` vom Terminal).

Wir verwenden ein einfaches Beispiel: ein Paket namens `mytools` mit einem Skript `greet`, das eine Begrüßung ausgibt.

#### Schritt 1: Richten Sie Ihre Paketstruktur ein
Erstellen Sie eine Verzeichnisstruktur wie diese:

```
mytools/
├── pyproject.toml          # Moderne Konfigurationsdatei (empfohlen statt setup.py)
├── README.md
└── src/
    └── mytools/
        ├── __init__.py     # Macht es zu einem Paket
        └── greet.py        # Ihre Skriptlogik
```

In `src/mytools/__init__.py` (kann leer sein oder Versionsinformationen enthalten):
```python
__version__ = "0.1.0"
```

In `src/mytools/greet.py` (die Funktion, die Ihr Skript aufrufen wird):
```python
import sys

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
```

#### Schritt 2: Konfigurieren Sie Entry Points in `pyproject.toml`
Verwenden Sie den Abschnitt `[project.scripts]`, um Console Scripts zu definieren. Dies weist pip an, ausführbare Wrapper zu erstellen.

```toml
[build-system]
requires = ["hatchling"]  # Oder "setuptools", "flit", etc.
build-backend = "hatchling.build"

[project]
name = "mytools"
version = "0.1.0"
description = "A simple tool package"
readme = "README.md"
requires-python = ">=3.8"
dependencies = []  # Fügen Sie hier Ihre Abhängigkeiten hinzu, z.B. "requests"

[project.scripts]
greet = "mytools.greet:main"  # Format: script_name = package.module:function
```

- `greet` ist der Befehl, den Benutzer ausführen werden (z.B. `greet Alice`).
- `mytools.greet:main` verweist auf die `main()`-Funktion in `greet.py`.

Wenn Sie die ältere `setup.py` bevorzugen (funktioniert noch, aber weniger empfohlen):
```python
from setuptools import setup, find_packages

setup(
    name="mytools",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "greet = mytools.greet:main"
        ]
    },
    # ... andere Felder wie description, install_requires
)
```

#### Schritt 3: Bauen und Installieren Sie das Paket
1. Installieren Sie Build-Tools: `pip install build twine` (oder `hatchling`, wenn Sie dieses Backend verwenden).

2. Bauen Sie das Paket:
   ```
   python -m build
   ```
   Dies erstellt `dist/` mit `.tar.gz` und `.whl` Dateien.

3. Installieren Sie lokal zum Testen:
   ```
   pip install -e .  # Editierbarer Modus (Änderungen werden sofort übernommen)
   ```
   Oder für eine saubere Installation: `pip install dist/mytools-0.1.0-py3-none-any.whl`.

4. Testen: Führen Sie `greet Alice` in Ihrem Terminal aus. Es sollte "Hello, Alice!" ausgeben.

#### Schritt 4: Verteilen (Optional)
- Hochladen zu PyPI: `twine upload dist/*` (erfordert PyPI-Account).
- Benutzer können dann `pip install mytools` ausführen und `greet` verwenden.

#### Tipps
- **Mehrere Skripte**: Fügen Sie weitere Zeilen zu `[project.scripts]` hinzu, z.B. `another-script = mytools.other:main`.
- **Argumente**: Verwenden Sie `argparse` in Ihrer `main()`-Funktion für bessere CLI-Behandlung.
- **Abhängigkeiten**: Listen Sie diese in `[project.dependencies]` auf (z.B. `click` für CLI-Frameworks).
- **Virtuelle Umgebung**: Verwenden Sie immer eine (`python -m venv env; source env/bin/activate`), um Konflikte zu vermeiden.
- **Fehler?** Überprüfen Sie `pip install --verbose` für Details. Stellen Sie sicher, dass Ihre Funktion keine Argumente erwartet (oder `sys.argv` selbst verarbeitet).

Für fortgeschrittene Setups (z.B. mit Poetry oder Flit), lesen Sie die offizielle Dokumentation.

#### Referenzen
- [Python Packaging User Guide: Entry Points](https://packaging.python.org/en/latest/guides/writing-entry-points/)
- [PyPI: Building and Publishing](https://packaging.python.org/en/latest/tutorials/packaging-projects/)