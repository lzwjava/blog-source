---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Aufbau der Setup.py-Datei
translated: true
type: note
---

### Übersicht
Dies ist eine `setup.py`-Datei, ein Standard-Python-Skript, das mit `setuptools` verwendet wird, um ein Python-Paket zu definieren und zu bauen. Konkret handelt es sich hier um die **Requests**-Bibliothek – einen beliebten HTTP-Client für Python. Sie verwaltet Metadaten wie den Paketnamen, die Version, Abhängigkeiten und Klassifizierer (für die PyPI-Verteilung). Wenn Sie `pip install requests` ausführen, wird dieses Skript (oder seine gebauten Artefakte) im Hintergrund ausgeführt, um das Paket zu installieren.

Das Skript ist als einzelner `setup()`-Funktionsaufruf strukturiert, enthält aber einige Guards, Helfer und dynamische Lesevorgänge aus anderen Dateien. Ich werde es abschnittsweise aufschlüsseln.

### 1. Imports und Python-Versionsprüfung
```python
#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 9)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    # Fehlermeldung und Beenden
    sys.exit(1)
```
- **Shebang (`#!/usr/bin/env python`)**: Macht die Datei auf Unix-ähnlichen Systemen ausführbar und führt sie mit dem systemeigenen Python-Interpreter aus.
- **Imports**: Bindet `os` und `sys` für Systeminteraktionen ein, `codecs.open` zum sicheren Lesen von UTF-8-Dateien (für den Umgang mit Nicht-ASCII-Zeichen) und `setup` von `setuptools` für den Paketbau.
- **Versionsprüfung**: Stellt sicher, dass der Benutzer Python 3.9 oder höher ausführt. Falls nicht, wird eine hilfreiche Fehlermeldung ausgegeben, die ein Upgrade oder das Anheften an eine ältere Requests-Version (<2.32.0) vorschlägt, und dann mit Code 1 (Fehler) beendet. Dies erzwingt die Kompatibilität, da Requests die Unterstützung für ältere Python-Versionen eingestellt hat.

### 2. Publish-Shortcut
```python
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()
```
- Ein Komfortfeature für Maintainer: Wenn Sie `python setup.py publish` ausführen, geschieht Folgendes:
  - Es baut Source Distribution (`sdist`) und Wheel (`bdist_wheel`) Archive im Ordner `dist/`.
  - Es lädt diese mit `twine` (einem sicheren Uploader) zu PyPI hoch.
- Dies ist eine schnelle Methode, um eine neue Version zu veröffentlichen, ohne manuelle Befehle. Das Skript wird nach der Ausführung beendet.

### 3. Abhängigkeiten
```python
requires = [
    "charset_normalizer>=2,<4",
    "idna>=2.5,<4",
    "urllib3>=1.21.1,<3",
    "certifi>=2017.4.17",
]
test_requirements = [
    "pytest-httpbin==2.1.0",
    "pytest-cov",
    "pytest-mock",
    "pytest-xdist",
    "PySocks>=1.5.6, !=1.5.7",
    "pytest>=3",
]
```
- **`requires`**: Kernabhängigkeiten, die bei `pip install requests` installiert werden. Diese kümmern sich um Kodierung (`charset_normalizer`), internationalisierte Domainnamen (`idna`), HTTP-Transport (`urllib3`) und SSL-Zertifikate (`certifi`).
- **`test_requirements`**: Werden nur installiert, wenn Sie Tests ausführen (z.B. via `pip install -e '.[tests]'`). Enthält Test-Tools wie `pytest`-Varianten für HTTP-Mocking, Coverage und paralleles Testen. `PySocks` dient der SOCKS-Proxy-Unterstützung in Tests.

### 4. Dynamisches Laden von Metadaten
```python
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "src", "requests", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()
```
- **`about`-Dict**: Liest Metadaten aus `src/requests/__version__.py` (z.B. `__title__`, `__version__`, `__description__`, etc.) mittels `exec()`. Dies zentralisiert die Versionsinformationen – aktualisieren Sie sie einmal, und `setup.py` holt sie sich.
- **`readme`**: Lädt die gesamte `README.md`-Datei als String für die lange Beschreibung des Pakets auf PyPI.

### 5. Der Haupt-`setup()`-Aufruf
Dies ist das Herzstück der Datei. Es konfiguriert das Paket für den Bau/die Installation:
```python
setup(
    name=about["__title__"],  # z.B. "requests"
    version=about["__version__"],  # z.B. "2.32.3"
    description=about["__description__"],  # Kurze Zusammenfassung
    long_description=readme,  # Vollständige README
    long_description_content_type="text/markdown",  # Wird auf PyPI als Markdown gerendert
    author=about["__author__"],  # z.B. "Kenneth Reitz"
    author_email=about["__author_email__"],
    url=about["__url__"],  # z.B. GitHub-Repo
    packages=["requests"],  # Installiert das 'requests'-Paket
    package_data={"": ["LICENSE", "NOTICE"]},  # Schließt Nicht-Python-Dateien ein
    package_dir={"": "src"},  # Quellcode befindet sich in 'src/'
    include_package_data=True,  # Bindet alle Daten-Dateien ein
    python_requires=">=3.9",  # Spiegelt die Versionsprüfung wider
    install_requires=requires,  # Von weiter oben
    license=about["__license__"],  # z.B. "Apache 2.0"
    zip_safe=False,  # Ermöglicht das Bearbeiten installierter Dateien (üblich für Bibliotheken)
    classifiers=[  # PyPI-Kategorien für Auffindbarkeit
        "Development Status :: 5 - Production/Stable",
        # ... (vollständige Liste enthält Python-Versionen, Betriebssysteme, Themen)
    ],
    tests_require=test_requirements,  # Für `pip install -e '.[tests]'`
    extras_require={  # Optionale Abhängigkeiten
        "security": [],  # Leer – vielleicht für zukünftige Verwendung
        "socks": ["PySocks>=1.5.6, !=1.5.7"],  # SOCKS-Proxy-Unterstützung
        "use_chardet_on_py3": ["chardet>=3.0.2,<6"],  # Legacy Zeichensatz-Fallback
    },
    project_urls={  # Links auf der PyPI-Seite
        "Documentation": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests",
    },
)
```
- **Wichtige Argumente**:
  - **Name/Version/Beschreibung**: Werden aus `__version__.py` gezogen, um die Wartung zu erleichtern.
  - **Packages/Package Dir**: Weist setuptools an, dass sich das Paket unter `src/requests/` befindet und als `import requests` installiert werden soll.
  - **Classifiers**: Eine Liste von Strings, die das Paket kategorisieren (z.B. stabil, Python 3.9+, Apache-Lizenz, Web/HTTP-Thema). Dies hilft Benutzern, es auf PyPI zu finden.
  - **Extras Require**: Ermöglicht es Benutzern, optionale Funktionen zu installieren, wie z.B. `pip install requests[socks]` für Proxy-Unterstützung.
  - **Project URLs**: Fügt der PyPI-Seite klickbare Links zur Dokumentation und zur Quelle hinzu.

### Wie es in der Praxis funktioniert
- **Installation**: `pip install .` (aus dem Repo) oder `pip install requests` (von PyPI) führt dies aus, um Dateien zu kopieren, Abhängigkeiten zu installieren und das Paket einzurichten.
- **Bauen**: `python setup.py sdist` erstellt verteilbare Archive.
- **Warum diese Struktur?**: Es ist ein "src-Layout" (Code in `src/`), was eine moderne Best Practice ist, um versehentliche Imports während der Entwicklung zu vermeiden. Die Datei ist in sich geschlossen, delegiert aber Details an andere Dateien wie `__version__.py`.

Diese setup.py stammt aus dem offiziellen Requests-Repo und hat sich über die Versionen hinweg kaum verändert – sie ist erprobt und zuverlässig.

### Referenzen
- [Requests Dokumentation](https://requests.readthedocs.io/en/latest/)
- [Requests GitHub Repository](https://github.com/psf/requests)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)