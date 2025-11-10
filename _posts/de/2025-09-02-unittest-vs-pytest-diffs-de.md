---
audio: false
generated: true
image: false
lang: de
layout: post
title: Unittest vs Pytest Hauptunterschiede
translated: true
type: note
---

Hier ist ein präziser Vergleich ohne Tabellen, der sich darauf konzentriert, was sich in Ihrem täglichen Testalltag tatsächlich ändert.

# Philosophie & Stil

*   **unittest**: xUnit-Stil (Java/JUnit-Vibe). Klassenbasierte Tests, Lifecycle-Hooks wie `setUp/tearDown`, Methodennamen müssen mit `test_` beginnen.
*   **pytest**: Pythonisch und minimal. Test-**Funktionen** oder Klassen, umfangreiche Fixtures, einfaches `assert` mit Assertion Rewriting.

# Test Discovery

*   **unittest**: `python -m unittest discover` (oder Suites laden). Sucht nach `test*.py`, `TestCase`-Subklassen.
*   **pytest**: `pytest` entdeckt automatisch `test_*.py` und `*_test.py`; Funktionen `test_*` und Methoden in `Test*`-Klassen.

# Assertions

*   **unittest**: Viele spezifische Methoden (`assertEqual`, `assertTrue`, `assertRaises`, …).
*   **pytest**: Verwenden Sie einfaches `assert` und es gibt aussagekräftige Diffs aus ("left vs right"), unterstützt `pytest.raises`.

# Fixtures & Setup

*   **unittest**: `setUp()/tearDown()`, `setUpClass/tearDownClass`, `setUpModule/tearDownModule`.
*   **pytest**: **Fixtures** mit Scopes (Function/Class/Module/Session), Dependency Injection, Autouse, Finalizers. Ermutigt zu kleinem, wiederverwendbarem Setup.

# Parametrisierung

*   **unittest**: Keine eingebaute; verwenden Sie Loops/subTests oder Bibliotheken von Drittanbietern.
*   **pytest**: `@pytest.mark.parametrize` ist First-Class (Matrix von Eingaben, saubere Berichterstattung).

# Skips, Erwartete Fehler, Marker

*   **unittest**: `@skip`, `@skipIf`, `@expectedFailure`.
*   **pytest**: Gleiche Ideen plus leistungsstarke **Marker** (`@pytest.mark.slow`, `xfail`, `filterwarnings`, benutzerdefinierte Marks) und Kommandozeilenauswahl (`-m slow`).

# Plugins & Ecosystem

*   **unittest**: Batteries-included, aber schlank; verlässt sich für erweiterte Funktionen auf externe Runner/Tools.
*   **pytest**: Riesiges Plugin-Ökosystem (`pytest-xdist` für parallel, `pytest-randomly`, `pytest-cov`, `pytest-mock`, `pytest-asyncio`, `pytest-django`, etc.).

# Mocks

*   **unittest**: `unittest.mock` ist Standard; funktioniert überall.
*   **pytest**: Verwenden Sie `unittest.mock` oder die `mocker`-Fixture von `pytest-mock` (saubereres Patching & Auto-Teardown).

# Async Testing

*   **unittest**: Seit 3.8, hat `IsolatedAsyncioTestCase` (okay, aber ausführlich).
*   **pytest**: Mit `pytest-asyncio` (oder Trios Plugin) erhalten Sie `@pytest.mark.asyncio` und Fixture-Support für Event Loops.

# Performance & Parallel

*   **unittest**: Kein eingebautes Parallel; verwenden Sie `unittest-parallel`/CI-Tricks.
*   **pytest**: `pytest-xdist -n auto` ist der Standard.

# IDE/CI/Coverage

*   Beide integrieren sich mit IDEs und CI. Coverage über `coverage.py`:

    *   **unittest**: `coverage run -m unittest` → `coverage report`.
    *   **pytest**: `pytest --cov=your_pkg` mit `pytest-cov`.

# Wann man was wählt

*   **Wählen Sie unittest**, wenn:

    *   Sie nur die Standardbibliothek benötigen (keine externen Abhängigkeiten).
    *   Sie sich in Legacy/xUnit-Codebasen oder strengen Org-Richtlinien einfügen.
*   **Wählen Sie pytest**, wenn:

    *   Sie schnelleres Erstellen, klarere Fehlermeldungen und leistungsstarke Fixtures/Parametrisierung wünschen.
    *   Sie von seinem Plugin-Ökosystem und Parallelisierung profitieren.

# Interop & Migration

Sie können **unittest**-Suites unter **pytest** ausführen (pytest findet `unittest.TestCase`s). Dies ermöglicht eine schrittweise Migration:

1.  Beginnen Sie damit, `pytest` als Runner aufzurufen.
2.  Fügen Sie pytest-Tests neben den bestehenden hinzu.
3.  Führen Sie Fixtures/Parametrisierung dort ein, wo sie helfen.
4.  Refaktorisieren Sie optional alte `TestCase`s später zu Funktionen.

# Kleine Beispiele im Vergleich

## Der gleiche Test

**unittest**

```python
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]

    def test_sum(self):
        self.assertEqual(sum(self.data), 6)

    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

if __name__ == "__main__":
    unittest.main()
```

**pytest**

```python
import pytest

@pytest.fixture
def data():
    return [1, 2, 3]

def test_sum(data):
    assert sum(data) == 6

def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

## Parametrisierung

**unittest (subTest)**

```python
import unittest

class TestParity(unittest.TestCase):
    def test_even(self):
        for n in [0, 2, 4]:
            with self.subTest(n=n):
                self.assertEqual(n % 2, 0)
```

**pytest**

```python
import pytest

@pytest.mark.parametrize("n", [0, 2, 4])
def test_even(n):
    assert n % 2 == 0
```

## Mocking

**unittest.mock**

```python
from unittest.mock import patch

@patch("pkg.api.fetch_user", return_value={"id": 1})
def test_uses_api(mock_fetch):
    from pkg.service import get_user
    assert get_user(1)["id"] == 1
    mock_fetch.assert_called_once_with(1)
```

**pytest-mock**

```python
def test_uses_api(mocker):
    mock_fetch = mocker.patch("pkg.api.fetch_user", return_value={"id": 1})
    from pkg.service import get_user
    assert get_user(1)["id"] == 1
    mock_fetch.assert_called_once_with(1)
```

# Praktische Empfehlungen

*   Neue Projekte: Standardmäßig **pytest** für Geschwindigkeit, Lesbarkeit und Ökosystem.
*   Legacy/Stdlib-only Umgebungen: Bleiben Sie bei **unittest**, ziehen Sie aber in Betracht, es über **pytest** auszuführen, um bessere Ausgabe und Plugins ohne Umschreiben der Tests zu erhalten.
*   Fügen Sie früh `pytest-xdist` für schnellere CI und `pytest-cov` für Coverage hinzu.
*   Verwenden Sie Fixtures anstelle von großen Klassen-Setups; halten Sie sie klein und komponierbar.
*   Verwenden Sie Marker, um Suites zu organisieren (`slow`, `integration`, `db`) und führen Sie Teilmengen in CI-Stages aus.