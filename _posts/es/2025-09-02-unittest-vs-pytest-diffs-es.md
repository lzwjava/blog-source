---
audio: false
generated: true
image: false
lang: es
layout: post
title: Unittest contra Pytest Diferencias Clave
translated: true
type: note
---

Aquí tienes una comparación concisa, sin tablas, centrada en lo que realmente cambia en tu día a día de testing.

# Filosofía y Estilo

* **unittest**: Estilo xUnit (similar a Java/JUnit). Tests basados en clases, hooks de ciclo de vida como `setUp/tearDown`, los nombres de métodos deben comenzar con `test_`.
* **pytest**: Pythonico y minimalista. **Funciones** de test o clases, fixtures ricos, `assert` simple con reescritura de aserciones.

# Descubrimiento de Tests

* **unittest**: `python -m unittest discover` (o cargar suites). Busca `test*.py`, subclases de `TestCase`.
* **pytest**: `pytest` descubre automáticamente `test_*.py` y `*_test.py`; funciones `test_*` y métodos en clases `Test*`.

# Aserciones

* **unittest**: Muchos métodos específicos (`assertEqual`, `assertTrue`, `assertRaises`, …).
* **pytest**: Usa `assert` simple y muestra diferencias expresivas ("izquierda vs derecha"), soporta `pytest.raises`.

# Fixtures y Configuración

* **unittest**: `setUp()/tearDown()`, `setUpClass/tearDownClass`, `setUpModule/tearDownModule`.
* **pytest**: **Fixtures** con alcances (function/class/module/session), inyección de dependencias, autouse, finalizadores. Fomenta configuraciones pequeñas y reutilizables.

# Parametrización

* **unittest**: No incorporada; usa bucles/subTests o librerías de terceros.
* **pytest**: `@pytest.mark.parametrize` es de primera clase (matriz de entradas, reportes limpios).

# Omisiones, Fallos Esperados, Marcadores

* **unittest**: `@skip`, `@skipIf`, `@expectedFailure`.
* **pytest**: Las mismas ideas más **marcadores** potentes (`@pytest.mark.slow`, `xfail`, `filterwarnings`, marcas personalizadas) y selección por línea de comandos (`-m slow`).

# Plugins y Ecosistema

* **unittest**: Incluye lo básico pero es limitado; depende de runners/herramientas externas para características avanzadas.
* **pytest**: Gran ecosistema de plugins (`pytest-xdist` para paralelismo, `pytest-randomly`, `pytest-cov`, `pytest-mock`, `pytest-asyncio`, `pytest-django`, etc.).

# Mocks

* **unittest**: `unittest.mock` es estándar; funciona en todas partes.
* **pytest**: Usa `unittest.mock` o el fixture `mocker` de `pytest-mock` (parcheo más limpio y auto-limpieza).

# Testing Asíncrono

* **unittest**: Desde la versión 3.8, tiene `IsolatedAsyncioTestCase` (aceptable pero verboso).
* **pytest**: Con `pytest-asyncio` (o el plugin de trio) obtienes `@pytest.mark.asyncio` y soporte de fixtures para event loops.

# Rendimiento y Paralelismo

* **unittest**: Sin paralelismo incorporado; usa `unittest-parallel`/trucos de CI.
* **pytest**: `pytest-xdist -n auto` es la solución habitual.

# IDE/CI/Cobertura

* Ambos se integran con IDEs y CI. Cobertura vía `coverage.py`:

  * **unittest**: `coverage run -m unittest` → `coverage report`.
  * **pytest**: `pytest --cov=your_pkg` con `pytest-cov`.

# Cuándo elegir cada uno

* **Elige unittest** si:

  * Necesitas solo la librería estándar (sin dependencias externas).
  * Te integras en bases de código legacy/xUnit o políticas estrictas de la organización.
* **Elige pytest** si:

  * Quieres una escritura más rápida, fallos más claros y fixtures/parametrización potentes.
  * Te beneficiarás de su ecosistema de plugins y paralelización.

# Interoperabilidad y Migración

Puedes ejecutar suites de **unittest** bajo **pytest** (pytest encuentra `unittest.TestCase`s). Esto permite migrar gradualmente:

1. Comienza invocando `pytest` como el runner.
2. Añade tests de pytest junto a los existentes.
3. Introduce fixtures/parametrize donde ayuden.
4. Opcionalmente, refactoriza los antiguos `TestCase` a funciones más tarde.

# Pequeños ejemplos comparativos

## El mismo test

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

## Parametrización

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

# Recomendaciones prácticas

* Proyectos nuevos: por defecto usa **pytest** por velocidad, legibilidad y ecosistema.
* Entornos legacy/solo stdlib: mantente con **unittest**, pero considera ejecutarlo vía **pytest** para obtener mejor salida y plugins sin reescribir tests.
* Añade `pytest-xdist` pronto para un CI más rápido, y `pytest-cov` para cobertura.
* Usa fixtures en lugar de configuraciones grandes de clases; mantenlas pequeñas y componibles.
* Usa marcadores para organizar suites (`slow`, `integration`, `db`) y ejecutar subconjuntos en etapas de CI.

Si quieres, cuéntame la estructura de tu proyecto y sus restricciones (¿solo stdlib? ¿necesitas paralelismo? ¿async? ¿Django/Flask/FastAPI?) y esbozaré una configuración de tests mínima y opinada para ti.