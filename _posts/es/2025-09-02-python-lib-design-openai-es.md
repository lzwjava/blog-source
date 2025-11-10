---
audio: false
generated: true
image: false
lang: es
layout: post
title: Lecciones de diseño de bibliotecas de Python de OpenAI
translated: true
type: note
---

Aquí tienes un desglise rápido de `openai/openai-python` y las lecciones que puedes aplicar para construir una gran librería de Python.

# Lo que muestra el repositorio (de un vistazo)

* **Estructura clara de "src layout"**: `src/openai` para el código; en el nivel superior `tests/`, `examples/`, `scripts/`, `.github/`, `pyproject.toml`, `mypy.ini`, `noxfile.py`, etc. Esa separación mantiene las rutas de importación limpias y la detección de tests predecible. ([GitHub][1])
* **Superficie pública tipada**: las solicitudes usan `TypedDict`, las respuestas son modelos **Pydantic**; gran DX y refactorizaciones más seguras. ([GitHub][1])
* **Paridad Sincrónica + Asincrónica**: `OpenAI` y `AsyncOpenAI` comparten la misma API; el transporte por defecto es `httpx`, con `aiohttp` opcional. ([GitHub][1])
* **Streaming de primera clase**: Eventos enviados por el servidor (Server-Sent Events) con iteración simple tanto en sincrónico como asincrónico. ([GitHub][1])
* **Auto-paginación**: endpoints de lista iterables para que los usuarios no tengan que crear bucles de página manualmente. ([GitHub][1])
* **Cliente en tiempo real/WebSocket**: un sub-cliente opcional con ejemplos y guía de manejo de errores. ([GitHub][1])
* **Pipeline de generación de código**: el SDK se genera a partir de una especificación OpenAPI (vía Stainless), lo que impone consistencia y cobertura de tipos. ([GitHub][1])

# Conclusiones de diseño que puedes reutilizar

* **Mantén la "forma obvia"**: expone un único `Client` (más `AsyncClient`) con nombres de métodos espejo. Los usuarios no deberían preguntarse "¿qué clase debo usar?". El SDK de OpenAI muestra esto con `OpenAI` y `AsyncOpenAI`. ([GitHub][1])
* **Transportes portátiles**: por defecto `httpx`, pero permite un backend HTTP intercambiable (ej., `aiohttp`), para que los usuarios de alta concurrencia no estén limitados. ([GitHub][1])
* **Solicitudes + modelos tipados**: incluye cargas útiles de solicitud tipadas y modelos de respuesta enriquecidos. Eso te da autocompletado en el editor, ejemplos que se pueden verificar con linters, y cambios rupturistas más seguros. ([GitHub][1])
* **Streaming sin fricción**: diseña el streaming como un iterador simple / iterador asincrónico. No se necesitan bombas de eventos personalizadas. ([GitHub][1])
* **Paginación basada en iteradores**: expone `for item in client.resource.list(limit=...)` y obtiene las páginas de forma perezosa. Mantiene el código del usuario pequeño y sigue siendo eficiente. ([GitHub][1])
* **Los subsistemas son sub-clientes**: coloca características especializadas (ej., tiempo real) detrás de un espacio de nombres claramente nombrado (`client.beta.realtime`) para mantener la superficie principal limpia. ([GitHub][1])
* **Genera donde ayude**: si tu API está impulsada por especificaciones, deja que la generación de código cree las capas aburridas y fuertemente tipadas y elabora manualmente las partes ergonómicas. ([GitHub][1])

# Un esqueleto que puedes copiar

```bash
yourlib/
  pyproject.toml
  noxfile.py
  mypy.ini
  README.md
  CHANGELOG.md
  SECURITY.md
  src/yourlib/
    __init__.py
    _version.py
    _types.py            # TypedDicts, enums
    _errors.py           # Jerarquía de excepciones
    _http.py             # Wrapper del cliente httpx, reintentos, timeouts
    _pagination.py       # Pager[T] genérico
    client.py            # Client + AsyncClient, auth, URL base
    resources/
      __init__.py
      widgets.py         # grupos de recursos con métodos sync+async
    streaming.py         # helpers SSE (sync/async)
  tests/
    test_client.py
    test_widgets.py
  examples/
    quickstart.py
    async_quickstart.py
```

## API Pública (`src/yourlib/__init__.py`)

* Re-exporta solo lo que los usuarios necesitan:

```python
from .client import Client, AsyncClient
from ._errors import YourLibError, APIError, RateLimitError
__all__ = ["Client", "AsyncClient", "YourLibError", "APIError", "RateLimitError"]
```

## Forma del Cliente (sync & async)

* Refleja los mismos nombres de métodos; difieren solo en `await`/`async`:

```python
# src/yourlib/client.py
import httpx
from .resources.widgets import Widgets
from ._http import HttpTransport

class Client:
    def __init__(self, api_key=None, base_url="https://api.example.com", http_client=None):
        self._transport = HttpTransport(api_key, base_url, http_client or httpx.Client(timeout=30))
        self.widgets = Widgets(self._transport)

class AsyncClient:
    def __init__(self, api_key=None, base_url="https://api.example.com", http_client=None):
        self._transport = HttpTransport(api_key, base_url, http_client or httpx.AsyncClient(timeout=30))
        self.widgets = Widgets(self._transport)
```

## Patrón de Paginación

```python
# src/yourlib/_pagination.py
from typing import AsyncIterator, Iterator, Generic, TypeVar, Callable, Optional
T = TypeVar("T")
class Pager(Generic[T]):
    def __init__(self, fetch: Callable[..., dict], limit: int = 100):
        self._fetch = fetch
        self._limit = limit
        self._cursor = None
    def __iter__(self) -> Iterator[T]:
        while True:
            page = self._fetch(limit=self._limit, cursor=self._cursor)
            for item in page["data"]:
                yield item
            self._cursor = page.get("next_cursor")
            if not self._cursor:
                break
```

Expónlo para que los usuarios puedan hacer `for item in client.widgets.list(limit=50): ...`. (El SDK de OpenAI toma el mismo enfoque. ([GitHub][1]))

## Patrón de Streaming (SSE)

* Envuelve el streaming de `httpx` con un pequeño iterador que produce eventos; refleja una variante asincrónica. Eso produce la UX ergonómica `for event in client.responses.create(..., stream=True)` vista en el SDK de OpenAI. ([GitHub][1])

# Herramientas y flujo de lanzamiento que escala

* **`pyproject.toml` (PEP 621)** para metadatos; bloquea las dependencias de desarrollo por separado.
* **Verificación de tipos**: incluye tipos, ejecuta `mypy` en CI (su repositorio tiene `mypy.ini`). ([GitHub][1])
* **Ejecutor de tareas**: sesiones `nox` para test, lint, verificación de tipos, build (ellos usan `noxfile.py`). ([GitHub][1])
* **CI**: GitHub Actions en `.github/` para ejecutar tests en distintas versiones de Python y plataformas. ([GitHub][2])
* **CHANGELOG** y **versionado**: mantén un registro legible por humanos; automatiza los lanzamientos (ellos usan release-please). ([GitHub][1])
* **Docs de Seguridad y Contribución**: establece expectativas para quienes reportan y contribuyen. ([GitHub][1])

# Documentación y ejemplos

* **Ejemplos en el README** deben ser ejecutables y fáciles de copiar y pegar—sincrónicos, asincrónicos, streaming, paginación, y cualquier "transporte especial" (como `aiohttp`). El README de OpenAI demuestra cada uno de manera sucinta. ([GitHub][1])
* **Referencia de la API**: si está generada por código, publica un `api.md`/sitio de referencia y mantenlo alineado con los lanzamientos. ([GitHub][1])
* **Carpeta de ejemplos**: incluye scripts mínimos y enfocados, más una muestra "completa".

# Errores, reintentos y timeouts (qué implementar)

* **Jerarquía de errores**: `YourLibError` → `APIError`, `AuthError`, `RateLimitError`, `TimeoutError`. Asigna códigos de estado HTTP a excepciones; incluye IDs de solicitud.
* **Reintentos**: las operaciones idempotentes deberían reintentarse automáticamente con retroceso exponencial + jitter en 429/5xx.
* **Timeouts**: establece valores predeterminados sensatos y hazlos configurables a nivel de cliente y por llamada.
* **Ganchos de logging**: registro estructurado de depuración sin filtrar secretos.

# Empaquetado y compatibilidad

* **Soporta 3-4 versiones activas menores de Python** (ej., 3.9–3.13), y pruébalas en CI.
* **Sin efectos secundarios al importar**; difiere la creación de red/cliente hasta el primer uso.
* **Configuración de entorno**: acepta la variable de entorno `API_KEY` pero permite que los usuarios pasen credenciales explícitamente también (OpenAI muestra `OPENAI_API_KEY` y un tip de `.env`). ([GitHub][1])
* **API pública estable**: mantén los internos privados (`_module.py`), re-exporta una superficie ordenada en `__init__.py`.

# Errores comunes a evitar

* Meter todo en un único módulo; divide por recurso y mantén las importaciones públicas estables.
* Filtrar tipos de transporte; tus recursos deberían depender de un pequeño protocolo de "transporte", no de `httpx` directamente.
* Hacer que lo asincrónico parezca de segunda clase; asegúrate de que las pruebas y los ejemplos cubran ambos por igual (la paridad de OpenAI es un buen modelo). ([GitHub][1])
* Para el streaming, no obligues a los usuarios a manejar hilos o callbacks—los iteradores son más simples. ([GitHub][1])

Si quieres, puedo preparar esta estructura para un dominio concreto (ej., un cliente tipado para tus servicios REST internos, con sincronía/asincronía, paginación y streaming) e incluir scripts `nox`, CI y ejemplos listos para ejecutar.

[1]: https://github.com/openai/openai-python "GitHub - openai/openai-python: The official Python library for the OpenAI API"
[2]: https://github.com/openai/openai-python/tree/main/.github "openai-python/.github at main · openai/openai-python · GitHub"