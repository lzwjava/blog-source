---
audio: false
date: 2025-09-11
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Comprender el Uso de Accesorios de Pytest
translated: true
type: note
---

## ¿Qué es `@pytest.fixture`?

`@pytest.fixture` es un decorador que marca una función como un **fixture** - una función especial que proporciona datos de prueba, configuración o funcionalidad de desmontaje a tus pruebas. Los fixtures son una de las características más potentes de pytest y una razón clave por la que muchos desarrolladores prefieren pytest sobre el módulo `unittest` integrado de Python.

## Cómo Funcionan los Fixtures

Los fixtures siguen un patrón simple pero potente:

1.  **Configuración**: El código antes de la declaración `yield` se ejecuta antes de la prueba
2.  **Ejecución de la Prueba**: La prueba se ejecuta cuando llega a la declaración `yield`
3.  **Desmontaje**: El código después de la declaración `yield` se ejecuta después de que la prueba finaliza

### Ejemplo Básico de un Fixture

```python
import pytest

@pytest.fixture
def sample_data():
    # Código de configuración
    data = {"name": "John", "age": 30}
    yield data  # La prueba se ejecuta aquí
    # Código de desmontaje (se ejecuta después de la prueba)
    print("Cleaning up sample data")
```

## Por Qué Necesitamos Fixtures

Los fixtures resuelven varios problemas comunes en las pruebas:

1.  **Aislamiento de Pruebas**: Asegura que cada prueba se ejecute con datos frescos y predecibles
2.  **Reutilización de Código**: Evita repetir código de configuración/desmontaje en múltiples pruebas
3.  **Gestión de Recursos**: Maneja correctamente recursos como conexiones de base de datos, archivos o conexiones de red
4.  **Claridad en las Pruebas**: Mantiene las funciones de prueba centradas en lo que están probando, no en la configuración
5.  **Inyección de Dependencias**: Proporciona exactamente lo que cada prueba necesita

## Características Clave de los Fixtures

### 1. Inyección de Dependencias

Los fixtures pueden depender de otros fixtures, creando un gráfico de dependencias:

```python
@pytest.fixture
def database_connection():
    # Configurar conexión a la base de datos
    conn = create_connection()
    yield conn
    conn.close()

@pytest.fixture
def user_table(database_connection):
    # Utiliza el fixture database_connection
    create_table(database_connection, "users")
    yield
    drop_table(database_connection, "users")
```

### 2. Control de Alcance

Los fixtures pueden tener diferentes tiempos de vida:

```python
@pytest.fixture(scope="function")  # Por defecto - se ejecuta una vez por prueba
def per_test_fixture():
    pass

@pytest.fixture(scope="module")  # Se ejecuta una vez por módulo
def per_module_fixture():
    pass

@pytest.fixture(scope="session")  # Se ejecuta una vez por sesión de prueba
def per_session_fixture():
    pass
```

### 3. Fixtures de Uso Automático

Los fixtures pueden ejecutarse automáticamente sin ser solicitados:

```python
@pytest.fixture(autouse=True)
def always_run_this():
    # Esto se ejecuta antes de cada prueba en el módulo
    yield
    # Esto se ejecuta después de cada prueba
```

### 4. Fixtures Parametrizados

Los fixtures pueden generar múltiples conjuntos de datos:

```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param  # Ejecutará las pruebas con 1, 2 y 3
```

## Ejemplo Práctico con Pruebas de API

Así es como los fixtures ayudan en tu escenario de prueba de encabezados financieros:

```python
import pytest
import requests

@pytest.fixture
def financial_header():
    # Configuración - crear el encabezado
    headers = create_financial_header()  # Tu lógica de creación
    yield headers  # La prueba se ejecuta aquí con estos encabezados

    # Desmontaje - eliminar el encabezado
    delete_financial_header(headers)  # Tu lógica de limpieza

def test_submit_transaction(financial_header):
    # El fixture proporciona los encabezados automáticamente
    response = requests.post(
        "https://api.example.com/transactions",
        headers=financial_header,
        json={"amount": 100}
    )
    assert response.status_code == 201

def test_validate_header(financial_header):
    # El mismo fixture se usa en otra prueba
    response = requests.get(
        "https://api.example.com/validate",
        headers=financial_header
    )
    assert response.json()["valid"] is True
```

## Comparación con unittest

| Característica          | pytest Fixtures                     | unittest setUp/tearDown          |
|-------------------------|-------------------------------------|----------------------------------|
| Inyección de dependencias | ✅ Sí                               | ❌ No                            |
| Control de alcance      | ✅ Función, clase, módulo, sesión  | ❌ Solo a nivel método/clase     |
| Sintaxis limpia         | ✅ Decorador simple                 | ❌ Requiere herencia             |
| Aislamiento de pruebas  | ✅ Cada prueba obtiene fixtures nuevos | ❌ El estado compartido puede causar problemas |
| Parametrización         | ✅ Soporte integrado                | ❌ Se necesita implementación manual |

## Cuándo Usar Fixtures

Usa fixtures cuando necesites:
- Configurar datos u objetos de prueba
- Gestionar recursos externos (conexiones DB, archivos, etc.)
- Realizar limpieza después de las pruebas
- Compartir dependencias comunes de prueba
- Crear diferentes entornos de prueba
- Implementar lógica compleja de configuración/desmontaje

Los fixtures son particularmente valiosos en las pruebas de API (como tu caso de encabezados financieros) porque ayudan a gestionar el ciclo de vida de los recursos de prueba de manera limpia y predecible.