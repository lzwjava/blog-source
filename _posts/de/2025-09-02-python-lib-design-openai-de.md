---
audio: false
generated: true
image: false
lang: de
layout: post
title: Entwurfslektionen für Python-Bibliotheken von OpenAI
translated: true
type: note
---

Hier ist ein kurzer Teardown von `openai/openai-python` und die Lehren, die du für den Bau einer großartigen Python-Bibliothek übernehmen kannst.

# Was das Repo zeigt (auf einen Blick)

* **Klares "src-Layout"**: `src/openai` für Code; Top-Level `tests/`, `examples/`, `scripts/`, `.github/`, `pyproject.toml`, `mypy.ini`, `noxfile.py` etc. Diese Trennung hält Importpfade sauber und Test Discovery vorhersehbar. ([GitHub][1])
* **Getippte öffentliche Oberfläche**: Requests verwenden `TypedDict`, Responses sind **Pydantic**-Modelle; großartige Developer Experience und sicherere Refactorings. ([GitHub][1])
* **Sync + Async Parität**: `OpenAI` und `AsyncOpenAI` teilen sich die gleiche API; Standard-Transport ist `httpx`, mit optionalem `aiohttp`. ([GitHub][1])
* **First-Class Streaming**: Server-Sent Events mit einfacher Iteration in sync und async. ([GitHub][1])
* **Auto-Pagination**: Iterierbare List-Endpoints, damit Benutzer keine Page-Loops selbst schreiben müssen. ([GitHub][1])
* **Realtime/WebSocket Client**: Ein Opt-In-Sub-Client mit Beispielen und Error-Handling-Anleitung. ([GitHub][1])
* **Codegen-Pipeline**: Das SDK wird aus einer OpenAPI-Spec generiert (via Stainless), was Konsistenz und Type Coverage erzwingt. ([GitHub][1])

# Design-Erkenntnisse, die du wiederverwenden kannst

* **Bewahre den "einen offensichtlichen Weg"**: Biete einen einzigen `Client` (plus `AsyncClient`) mit gespiegelten Methodennamen an. Benutzer sollten sich nicht fragen "Welche Klasse soll ich verwenden?". Das OpenAI SDK zeigt dies mit `OpenAI` und `AsyncOpenAI`. ([GitHub][1])
* **Portable Transports**: Standardmäßig `httpx`, aber erlaube ein austauschbares HTTP-Backend (z.B. `aiohttp`), damit High-Concurrency-Benutzer nicht eingeschränkt sind. ([GitHub][1])
* **Getippte Requests + Modelle**: Liefere getippte Request-Payloads und reichhaltige Response-Modelle. Das bringt dir Editor-Autocomplete, lintbare Beispiele und sicherere Breaking Changes. ([GitHub][1])
* **Zero-Friction Streaming**: Designe Streaming als einfachen Iterator / Async Iterator. Keine benutzerdefinierten Event Pumps nötig. ([GitHub][1])
* **Iterator-basierte Pagination**: Biete `for item in client.resource.list(limit=...)` an und fetche Seiten lazy. Das hält Benutzercode klein und bleibt effizient. ([GitHub][1])
* **Subsysteme sind Sub-Clients**: Setze spezialisierte Features (z.B. realtime) hinter einen klar benannten Namespace (`client.beta.realtime`), um die Hauptoberfläche sauber zu halten. ([GitHub][1])
* **Generiere, wo es hilft**: Wenn deine API spez-getrieben ist, lass Codegen die langweiligen, stark getippten Schichten erstellen und handcrafte die ergonomischen Teile. ([GitHub][1])

# Ein Skelett, das du kopieren kannst

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
    _errors.py           # Exception hierarchy
    _http.py             # httpx client wrapper, retries, timeouts
    _pagination.py       # generic Pager[T]
    client.py            # Client + AsyncClient, auth, base URL
    resources/
      __init__.py
      widgets.py         # resource groups w/ sync+async methods
    streaming.py         # SSE helpers (sync/async)
  tests/
    test_client.py
    test_widgets.py
  examples/
    quickstart.py
    async_quickstart.py
```

## Public API (`src/yourlib/__init__.py`)

* Re-exportiere nur das, was Benutzer benötigen:

```python
from .client import Client, AsyncClient
from ._errors import YourLibError, APIError, RateLimitError
__all__ = ["Client", "AsyncClient", "YourLibError", "APIError", "RateLimitError"]
```

## Client-Form (sync & async)

* Spiegle die gleichen Methodennamen; unterscheide dich nur in `await`/`async`:

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

## Pagination-Pattern

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

Exponiere es, damit Benutzer `for item in client.widgets.list(limit=50): ...` verwenden können. (Das OpenAI SDK verfolgt den gleichen Ansatz. ([GitHub][1]))

## Streaming-Pattern (SSE)

* Wrappe `httpx`'s Streaming mit einem kleinen Iterator, der Events liefert; spiegle eine Async-Variante. Das ergibt die ergonomische `for event in client.responses.create(..., stream=True)` UX, die im OpenAI SDK zu sehen ist. ([GitHub][1])

# Tooling & Release-Flow, der skaliert

* **`pyproject.toml` (PEP 621)** für Metadaten; sperre Dev-Deps separat.
* **Type Checking**: liefere Types mit, führe `mypy` in CI aus (ihr Repo hat `mypy.ini`). ([GitHub][1])
* **Task Runner**: `nox`-Sessions für Test, Lint, Typecheck, Build (sie verwenden `noxfile.py`). ([GitHub][1])
* **CI**: GitHub Actions in `.github/`, um Tests über Python-Versionen/Plattformen laufen zu lassen. ([GitHub][2])
* **CHANGELOG** und **Versioning**: halte ein menschenlesbares Log; automatisiere Releases (sie verwenden release-please). ([GitHub][1])
* **Security & Contributing Docs**: setze Erwartungen für Reporter und Contributor. ([GitHub][1])

# Docs & Beispiele

* **README-Beispiele** sollten lauffähig und copy-paste-freundlich sein – sync, async, streaming, pagination und alle "special transports" (wie `aiohttp`). Die OpenAI README demonstriert jedes succinctly. ([GitHub][1])
* **API-Referenz**: wenn code-generiert, veröffentliche ein `api.md`/Reference-Site und halte es im Lockstep mit Releases. ([GitHub][1])
* **Examples-Ordner**: beinhalte minimale, fokussierte Scripts, plus ein "vollständiges" Beispiel.

# Errors, Retries und Timeouts (was zu implementieren ist)

* **Error-Hierarchie**: `YourLibError` → `APIError`, `AuthError`, `RateLimitError`, `TimeoutError`. Mappe HTTP-Statuscodes zu Exceptions; beinhole Request-IDs.
* **Retries**: idempotente Operationen sollten auto-retry mit exponentiellem Backoff + Jitter bei 429/5xx durchführen.
* **Timeouts**: setze sinnvolle Defaults und mache sie auf Client- und Per-Call-Ebene konfigurierbar.
* **Logging Hooks**: strukturiertes Debug-Logging ohne Leaking von Secrets.

# Packaging & Kompatibilität

* **Unterstütze 3–4 aktive Python Minors** (z.B. 3.9–3.13) und teste sie in CI.
* **Keine Side Effects beim Import**; verzögere Network/Client-Erstellung bis zur ersten Verwendung.
* **Environment Config**: akzeptiere `API_KEY` Environment Variable, aber lass Benutzer Credentials auch explizit übergeben (OpenAI zeigt `OPENAI_API_KEY` und einen `.env`-Tip). ([GitHub][1])
* **Stabile Public API**: halte Internals privat (`_module.py`), re-exportiere eine saubere Oberfläche in `__init__.py`.

# Fallstricke, die du vermeiden solltest

* Alles in ein einzelnes Modul stopfen; splitte nach Resource und halte Public Imports stabil.
* Transport-Types leaken; deine Resources sollten von einem kleinen "Transport"-Protokoll abhängen, nicht direkt von `httpx`.
* Async sich second-class anfühlen lassen; stelle sicher, dass Tests und Beispiele beide gleichermaßen abdecken (OpenAIs Parität ist ein gutes Modell). ([GitHub][1])
* Für Streaming zwinge Benutzer nicht, Threads oder Callbacks zu jonglieren – Iteratoren sind simpler. ([GitHub][1])

Falls du möchtest, kann ich dieses Strukturgerüst für eine konkrete Domain scaffolden (z.B. einen getippten Client für deine internen REST-Services, mit sync/async, pagination und streaming) und ready-to-run `nox`, CI und Beispiel-Scripts einfügen.

[1]: https://github.com/openai/openai-python "GitHub - openai/openai-python: The official Python library for the OpenAI API"
[2]: https://github.com/openai/openai-python/tree/main/.github "openai-python/.github at main · openai/openai-python · GitHub"