---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: PEP 517 Python-Packaging-Leitfaden
translated: true
type: note
---

PEP 517, akzeptiert im Jahr 2016, definiert eine standardisierte Schnittstelle für den Bau von Python-Paketen, die das Build-Backend (die Logik zur Erstellung von Distributionen) vom Frontend (Werkzeuge wie pip, die den Prozess orchestrieren) entkoppelt. Dies ermöglicht es Entwicklern, moderne Build-Tools zu verwenden, ohne an veraltete Systeme wie `setup.py` von setuptools gebunden zu sein. In Kombination mit PEP 518 (welches Build-Abhängigkeiten spezifiziert) ermöglicht es zuverlässige, isolierte Builds aus Source Trees oder Source Distributions (sdists). Seit 2025 ist PEP 517 die Grundlage für modernes Python Packaging, unterstützt von pip (seit Version 10 für PEP 518 und 19 für vollständiges PEP 517) und Werkzeugen wie Poetry, Flit und PDM.

Dieser Leitfaden behandelt die Motivation, Schlüsselkonzepte, Spezifikation, Workflows, Implementierung und Best Practices.

## Motivation und Hintergrund

Python Packaging entwickelte sich von `distutils` (eingeführt in Python 1.6, 2000) zu `setuptools` (2004), welches Abhängigkeitsverwaltung hinzufügte, aber Probleme einführte:
- **Imperativ und Fragil**: Builds verließen sich auf die Ausführung von `python setup.py`, ein beliebiges Skript, das aufgrund von Umgebungsannahmen fehlschlagen konnte (z.B. fehlendes Cython für Erweiterungen).
- **Keine Build-Abhängigkeiten**: Für den Build benötigte Werkzeuge (z.B. Compiler, Cython) wurden nicht deklariert, was zu manuellen Installationen und Versionskonflikten führte.
- **Enge Kopplung**: Pip war fest auf den Aufruf von `setup.py` programmiert, was alternative Build-Systeme wie Flit oder Bento blockierte.
- **Verschmutzung der Host-Umgebung**: Builds verwendeten die globale Python-Umgebung des Benutzers, was Nebenwirkungen riskierte.

Diese Probleme hemmten Innovation und verursachten Fehler während Source-Installationen (z.B. aus Git). PEP 517 löst dies durch die Standardisierung einer minimalen Schnittstelle: Frontends rufen Backend-Hooks in isolierten Umgebungen auf. Wheels (vorgebaute Binärdateien, eingeführt 2014) vereinfachen die Distribution – Backends müssen nur konforme Wheels/sdists produzieren. PEP 518 ergänzt dies durch die Deklaration von Build-Anforderungen in `pyproject.toml`, was Isolation ermöglicht.

Das Ergebnis: Ein deklaratives, erweiterbares Ökosystem, in dem `setup.py` optional ist und Werkzeuge wie pip jedes konforme Projekt ohne Legacy-Fallbacks bauen können.

## Schlüsselkonzepte

### Source Trees und Distributions
- **Source Tree**: Ein Verzeichnis (z.B. VCS-Checkout), das Paketcode und `pyproject.toml` enthält. Werkzeuge wie `pip install .` bauen daraus.
- **Source Distribution (Sdist)**: Ein gzip-komprimiertes Tarball (`.tar.gz`) wie `package-1.0.tar.gz`, das sich in ein `{name}-{version}` Verzeichnis mit `pyproject.toml` und Metadaten (PKG-INFO) entpackt. Wird für Releases und Downstream-Packaging (z.B. Debian) verwendet.
- **Wheel**: Eine `.whl` Binärdistribution – vorgebaut, plattformspezifisch und ohne Kompilierung installierbar. PEP 517 schreibt Wheels für Reproduzierbarkeit vor.

Legacy sdists (vor PEP 517) entpacken sich in ausführbare Trees, müssen aber jetzt `pyproject.toml` für Konformität enthalten.

### pyproject.toml
Diese TOML-Datei zentralisiert die Konfiguration. Der Abschnitt `[build-system]` (von PEP 518/517) spezifiziert:
- `requires`: Liste der PEP 508 Abhängigkeiten für den Build (z.B. `["setuptools>=40.8.0", "wheel"]`).
- `build-backend`: Entry Point zum Backend (z.B. `"setuptools.build_meta"` oder `"poetry.masonry.api"`).
- `backend-path` (optional): In-Tree-Pfade, die `sys.path` für selbst-gehostete Backends hinzugefügt werden (z.B. `["src/backend"]`).

Beispiel für minimale Konfiguration:
```
[build-system]
requires = ["setuptools>=40.8.0", "wheel"]
build-backend = "setuptools.build_meta"
```

Anforderungen bilden einen DAG (keine Zyklen; Frontends erkennen dies und schlagen fehl). Andere Abschnitte wie `[project]` (PEP 621) oder `[tool.poetry]` halten Metadaten/Abhängigkeiten.

### Build Backends und Frontends
- **Backend**: Implementiert die Build-Logik via Hooks (aufrufbare Funktionen). Läuft in einem Subprozess für Isolation.
- **Frontend**: Orchestriert (z.B. pip). Richtet Isolation ein, installiert Anforderungen, ruft Hooks auf.
- **Entkopplung**: Frontends rufen standardisierte Hooks auf, nicht `setup.py`. Dies unterstützt verschiedene Backends ohne Pip-Änderungen.

Hooks verwenden `config_settings` (Dict für Flags, z.B. `{"--debug": true}`) und können nach stdout/stderr (UTF-8) ausgeben.

## Die Spezifikation

### [build-system] Details
- `requires`: PEP 508 Strings (z.B. `">=1.0; sys_platform == 'win32'"`).
- `build-backend`: `module:object` (z.B. importiert `flit_core.buildapi` das Modul `flit_core` und weist `backend = flit_core.buildapi` zu).
- Keine sys.path-Verschmutzung – Backends importieren via Isolation.

### Hooks
Backends stellen diese als Attribute bereit:

**Verpflichtend:**
- `build_wheel(wheel_directory, config_settings=None, metadata_directory=None) -> str`: Baut Wheel in `wheel_directory`, gibt Basisnamen zurück (z.B. `"myproj-1.0-py3-none-any.whl"`). Verwendet vorherige Metadaten, falls bereitgestellt. Handelt schreibgeschützte Quellen via Temporärdateien.
- `build_sdist(sdist_directory, config_settings=None) -> str`: Baut Sdist in `sdist_directory` (pax-Format, UTF-8). Löst `UnsupportedOperation` aus, wenn unmöglich (z.B. kein VCS).

**Optional (Standardwerte sind `[]` oder Fallbacks):**
- `get_requires_for_build_wheel(config_settings=None) -> list[str]`: Zusätzliche Wheel-Abhängigkeiten (z.B. `["cython"]`).
- `prepare_metadata_for_build_wheel(metadata_directory, config_settings=None) -> str`: Schreibt `{pkg}-{ver}.dist-info` Metadaten (gemäß Wheel-Spezifikation, kein RECORD). Gibt Basisnamen zurück; Frontends extrahieren sie aus dem Wheel, falls fehlend.
- `get_requires_for_build_sdist(config_settings=None) -> list[str]`: Zusätzliche Sdist-Abhängigkeiten.

Hooks lösen Exceptions bei Fehlern aus. Frontends rufen sie in isolierten Umgebungen auf (z.B. venv mit nur stdlib + Anforderungen).

### Build-Umgebung
- Isolierte venv: Bootstrap für `get_requires_*`, vollständig für Builds.
- CLI-Werkzeuge (z.B. `flit`) im PATH.
- Kein stdin; Subprozesse pro Hook.

## Wie der Build-Prozess funktioniert

### Schritt-für-Schritt Workflow
Für `pip install .` (Source Tree) oder Sdist-Installation:

1. **Entdeckung**: Frontend liest `pyproject.toml`.
2. **Isolationsaufbau**: Erstellt venv; installiert `requires`.
3. **Anfrage der Anforderungen**: Ruft `get_requires_for_build_wheel` auf (installiert Extras).
4. **Metadatenvorbereitung**: Ruft `prepare_metadata_for_build_wheel` auf (oder baut Wheel und extrahiert).
5. **Wheel-Bau**: Ruft `build_wheel` in isolierter Umgebung auf; installiert resultierendes Wheel.
6. **Fallbacks**: Wenn Sdist nicht unterstützt, baue Wheel; wenn keine Hooks, Legacy `setup.py`.

Für Sdists: Entpacken, als Source Tree behandeln. Entwickler-Workflow (z.B. `pip wheel .`):
1. Isoliere Umgebung.
2. Rufe Backend-Hooks für Wheel/Sdist auf.

### Build-Isolation (PEP 518)
Erstellt temporäre venv für Builds, vermeidet Host-Verschmutzung. Pips `--no-build-isolation` deaktiviert es (mit Vorsicht verwenden). Werkzeuge wie tox standardisieren auf Isolation.

Alt vs. Neu:
- **Alt**: `python setup.py install` in Host-Umgebung – riskiert Konflikte.
- **Neu**: Isolierte Hooks – reproduzierbar, sicher.

## Implementierung eines Build Backends

Um eines zu erstellen:
1. Definiere ein Modul mit Hooks (z.B. `mybackend.py`).
2. Verweise `build-backend` darauf.

Minimalbeispiel (reines Python-Paket):
```python
# mybackend.py
from zipfile import ZipFile
import os
from pathlib import Path

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    # Kopiere Quelle in Wheel-Verz., zip als .whl
    dist = Path(wheel_directory) / "myproj-1.0-py3-none-any.whl"
    with ZipFile(dist, 'w') as z:
        for src in Path('.').rglob('*'):
            z.write(src, src.relative_to('.'))
    return str(dist.relative_to(wheel_directory))

# Optionale Hooks
def get_requires_for_build_wheel(config_settings=None):
    return []

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    # Schreibe METADATA, etc.
    return "myproj-1.0.dist-info"
```

In `pyproject.toml`:
```
[build-system]
requires = []
build-backend = "mybackend:build_wheel"  # Zeigt eigentlich auf Modulobjekt
```

Verwende Bibliotheken wie `pyproject-hooks` für Boilerplate. Für Erweiterungen, integriere C-Compiler via `config_settings`.

## Verwendung von PEP 517 mit Werkzeugen

- **pip**: Erkennt `pyproject.toml` automatisch; verwende `--use-pep517` (Standard seit 19.1). Für editierbar: `pip install -e .` ruft Hooks auf.
- **Poetry**: Deklaratives Werkzeug. Generiert:
  ```
  [build-system]
  requires = ["poetry-core>=1.0.0"]
  build-backend = "poetry.core.masonry.api"
  ```
  Installiert via `poetry build`; pip-kompatibel.
- **Flit**: Einfach für reines Python. Verwendet:
  ```
  [build-system]
  requires = ["flit_core >=3.2,<4"]
  build-backend = "flit_core.buildapi"
  ```
  `flit publish` baut/uploadet.
- **Setuptools**: Legacy-Brücke:
  ```
  [build-system]
  requires = ["setuptools>=40.8.0", "wheel"]
  build-backend = "setuptools.build_meta"
  ```
  Unterstützt `setup.cfg` für deklarative Metadaten.

Migration von Legacy: Füge `[build-system]` hinzu; entferne `setup.py` Aufrufe.

## Fehlerbehandlung und Best Practices

- **Fehler**: Hooks lösen aus (z.B. `ValueError` für ungültige Konfiguration). Zyklen: Frontend schlägt mit Nachricht fehl. Nicht unterstützte Sdist: Fallback auf Wheel.
- **Best Practices**:
  - Bevorzuge deklarativ (`setup.cfg` oder `[project]`).
  - Deklariere exakte Build-Abhängigkeiten (z.B. `cython==0.29`).
  - Teste Isolation: `pip wheel . --no-build-isolation` zum Debuggen.
  - Für In-Tree-Backends: Verwende `backend-path`; vermeide Zyklen.
  - Sicherheit: Hooks in Subprozessen; kein beliebiger Code.
  - Kompatibilität: Füge `setup.py` für alte Werkzeuge hinzu.

Stand 2025 dominiert setuptools (laut Umfragen), aber die Adoption von Poetry/Flit wächst aufgrund der Einfachheit.

## Referenzen
- [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517/)
- [PEP 517 and 518 in Plain English](https://chadsmith-software.medium.com/pep-517-and-518-in-plain-english-47208ca8b7a6)
- [Python packaging - Past, Present, Future](https://bernat.tech/posts/pep-517-518/)
- [What is PEP 517/518 compatibility?](https://pydevtools.com/handbook/explanation/what-is-pep-517/)
- [Modern pip build process (–use-pep517)](https://fromkk.com/posts/modern-pip-build-process-use-pep517/)
- [What is a build backend?](https://pydevtools.com/handbook/explanation/what-is-a-build-backend/)