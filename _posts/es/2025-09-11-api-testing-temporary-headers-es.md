---
audio: false
date: 2025-09-11
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Pruebas de API con Encabezados Temporales
translated: true
type: note
---

Para probar endpoints de API que requieren headers temporales (como headers financieros) en una suite de pruebas de Python para un proyecto Java, tanto `unittest` como `pytest` son opciones viables, pero `pytest` ofrece algunas ventajas para este escenario.

## Enfoque Recomendado: pytest con Fixtures

`pytest` es generalmente mejor para este caso de uso porque:
- Tiene una gestión de fixtures más potente
- Sintaxis más limpia para setup/teardown
- Mejor soporte para inyección de dependencias
- Organización de pruebas más flexible

Aquí se muestra cómo podrías implementarlo:

### 1. Estructura Básica con pytest

```python
import pytest
import requests

@pytest.fixture
def financial_header():
    # Setup - crear el header
    headers = {
        "X-Financial-Id": "test_123",
        "X-Transaction-Type": "payment",
        "Authorization": "Bearer test_token"
    }
    yield headers  # Aquí es donde se ejecuta la prueba

    # Teardown - eliminar el header (si es necesario)
    # Esto podría implicar llamar a un endpoint de API de limpieza
    cleanup_url = "http://your-api/cleanup"
    requests.post(cleanup_url, headers=headers)

def test_api_with_header(financial_header):
    # Usar el header en tu prueba
    response = requests.get(
        "http://your-api/endpoint",
        headers=financial_header
    )

    # Validar la respuesta
    assert response.status_code == 200
    assert "expected_field" in response.json()
```

### 2. Ejemplo Más Avanzado con Múltiples Fases de Prueba

```python
import pytest
import requests

class FinancialHeaderManager:
    def __init__(self):
        self.header = None
        self.created = False

    def create(self):
        # Llamada a API para crear header
        response = requests.post("http://your-api/headers", json={
            "type": "financial",
            "metadata": {"test": True}
        })
        self.header = response.json()["header"]
        self.created = True
        return self.header

    def delete(self):
        if self.created:
            requests.delete(
                "http://your-api/headers",
                headers={"X-Header-Id": self.header["id"]}
            )
            self.created = False

@pytest.fixture
def header_manager():
    manager = FinancialHeaderManager()
    manager.create()
    yield manager
    manager.delete()

def test_header_lifecycle(header_manager):
    # Probar creación
    assert header_manager.created
    assert "X-Financial-Id" in header_manager.header

    # Probar uso
    response = requests.get(
        "http://your-api/protected",
        headers=header_manager.header
    )
    assert response.status_code == 200

    # Probar validación (si tu API tiene un endpoint de validación)
    validation = requests.post(
        "http://your-api/validate",
        headers=header_manager.header
    )
    assert validation.json()["valid"]
```

### 3. Si Prefieres unittest

Aunque pytest es recomendado, así es como podrías hacerlo con unittest:

```python
import unittest
import requests

class TestFinancialAPI(unittest.TestCase):
    def setUp(self):
        # Crear header
        self.header = {
            "X-Financial-Id": "test_123",
            "X-Transaction-Type": "payment"
        }
        # Si necesitas llamar a una API para crearlo:
        # response = requests.post(...)
        # self.header = response.json()

    def tearDown(self):
        # Eliminar header
        requests.delete(
            "http://your-api/headers",
            headers={"X-Header-Id": self.header["X-Financial-Id"]}
        )

    def test_api_with_header(self):
        response = requests.get(
            "http://your-api/endpoint",
            headers=self.header
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("expected_field", response.json())
```

## Mejores Prácticas

1. **Usa fixtures de pytest** para setup/teardown complejos - son más flexibles que setUp/tearDown de unittest
2. **Aísla las dependencias de prueba** - cada prueba debe ser independiente
3. **Considera usar Session de requests** para mejor rendimiento en las pruebas
4. **Añade lógica de reintento** para pruebas inestables si es necesario
5. **Usa variables de entorno** para diferentes entornos de prueba
6. **Considera usar mocking** si no necesitas probar el backend Java real

## Recomendaciones Adicionales

1. Para escenarios más complejos, considera usar:
   - `pytest-xdist` para ejecución paralela de pruebas
   - Librería `responses` para simular peticiones HTTP cuando sea necesario
   - `pytest-html` para mejores reportes de pruebas

2. Si tu API Java tiene requisitos específicos, podrías necesitar:
   - Manejar tokens CSRF
   - Gestionar sesiones/cookies
   - Lidiar con límites de tasa

¿Te gustaría que profundice en algún aspecto específico de este enfoque de testing?