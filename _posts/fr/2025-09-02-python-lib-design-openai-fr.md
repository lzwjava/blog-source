---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Leçons de conception de bibliothèque Python d'OpenAI
translated: true
type: note
---

Voici un rapide démontage de `openai/openai-python` et les leçons que vous pouvez en tirer pour construire une excellente bibliothèque Python.

# Ce que le dépôt montre (en un coup d'œil)

* **Une structure "src" claire** : `src/openai` pour le code ; à la racine `tests/`, `examples/`, `scripts/`, `.github/`, `pyproject.toml`, `mypy.ini`, `noxfile.py`, etc. Cette séparation maintient des chemins d'importation propres et une découverte des tests prévisible. ([GitHub][1])
* **Une surface publique typée** : les requêtes utilisent `TypedDict`, les réponses sont des modèles **Pydantic** ; excellente expérience développeur et refactorisations plus sûres. ([GitHub][1])
* **Parité Sync + Async** : `OpenAI` et `AsyncOpenAI` partagent la même API ; le transport par défaut est `httpx`, avec `aiohttp` en option. ([GitHub][1])
* **Streaming de première classe** : Server-Sent Events avec une itération simple en sync et async. ([GitHub][1])
* **Auto-pagination** : des endpoints de listes itérables pour que les utilisateurs n'aient pas à écrire leurs propres boucles de pagination. ([GitHub][1])
* **Client Realtime/WebSocket** : un sous-client optionnel avec des exemples et des conseils de gestion d'erreurs. ([GitHub][1])
* **Pipeline de génération de code** : le SDK est généré à partir d'une spécification OpenAPI (via Stainless), ce qui impose la cohérence et la couverture des types. ([GitHub][1])

# Points à retenir que vous pouvez réutiliser

* **Rester sur le "seul moyen évident"** : exposer un seul `Client` (plus `AsyncClient`) avec des noms de méthodes miroirs. Les utilisateurs ne devraient pas se demander "quelle classe dois-je utiliser ?". Le SDK OpenAI montre cela avec `OpenAI` et `AsyncOpenAI`. ([GitHub][1])
* **Transports portables** : utiliser `httpx` par défaut, mais permettre un backend HTTP interchangeable (par ex. `aiohttp`), afin que les utilisateurs à haute concurrence ne soient pas limités. ([GitHub][1])
* **Requêtes et modèles typés** : fournir des payloads de requête typés et des modèles de réponse riches. Cela vous donne l'autocomplétion de l'éditeur, des exemples vérifiables par le linter, et des changements cassants plus sûrs. ([GitHub][1])
* **Streaming sans friction** : concevoir le streaming comme un simple itérateur / itérateur asynchrone. Aucune pompe à événements personnalisée nécessaire. ([GitHub][1])
* **Pagination basée sur les itérateurs** : exposer `for item in client.resource.list(limit=...)` et récupérer les pages paresseusement. Cela garde le code utilisateur minuscule tout en restant efficace. ([GitHub][1])
* **Les sous-systèmes sont des sous-clients** : placer les fonctionnalités spécialisées (par ex., realtime) derrière un espace de noms clairement nommé (`client.beta.realtime`) pour garder la surface principale propre. ([GitHub][1])
* **Générer là où cela aide** : si votre API est pilotée par une spec, laissez la génération de code créer les couches ennuyeuses et fortement typées et fabriquez manuellement les parties ergonomiques. ([GitHub][1])

# Une structure que vous pouvez copier

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
    _errors.py           # Hiérarchie d'exceptions
    _http.py             # Wrapper du client httpx, nouvelles tentatives, timeouts
    _pagination.py       # Pager[T] générique
    client.py            # Client + AsyncClient, auth, URL de base
    resources/
      __init__.py
      widgets.py         # Groupes de ressources avec méthodes sync+async
    streaming.py         # Helpers SSE (sync/async)
  tests/
    test_client.py
    test_widgets.py
  examples/
    quickstart.py
    async_quickstart.py
```

## API Publique (`src/yourlib/__init__.py`)

* Ré-exporter uniquement ce dont les utilisateurs ont besoin :

```python
from .client import Client, AsyncClient
from ._errors import YourLibError, APIError, RateLimitError
__all__ = ["Client", "AsyncClient", "YourLibError", "APIError", "RateLimitError"]
```

## Forme du Client (sync & async)

* Refléter les mêmes noms de méthodes ; différer uniquement par `await`/`async` :

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

## Modèle de Pagination

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

L'exposer pour que les utilisateurs puissent faire `for item in client.widgets.list(limit=50): ...`. (Le SDK OpenAI adopte la même approche. ([GitHub][1]))

## Modèle de Streaming (SSE)

* Envelopper le streaming de `httpx` avec un petit itérateur qui produit des événements ; refléter une variante asynchrone. Cela donne l'UX ergonomique `for event in client.responses.create(..., stream=True)` vue dans le SDK OpenAI. ([GitHub][1])

# Outillage et flux de release qui évoluent

* **`pyproject.toml` (PEP 621)** pour les métadonnées ; verrouiller les dépendances de dev séparément.
* **Vérification des types** : fournir les types, exécuter `mypy` en CI (leur repo a `mypy.ini`). ([GitHub][1])
* **Gestionnaire de tâches** : sessions `nox` pour test, lint, vérification de types, build (ils utilisent `noxfile.py`). ([GitHub][1])
* **CI** : GitHub Actions dans `.github/` pour exécuter les tests sur différentes versions de Python et plateformes. ([GitHub][2])
* **CHANGELOG** et **versioning** : tenir un journal lisible par un humain ; automatiser les releases (ils utilisent release-please). ([GitHub][1])
* **Docs Sécurité & Contribution** : définir les attentes pour les reporters et les contributeurs. ([GitHub][1])

# Docs & exemples

* **Les exemples du README** doivent être exécutables et faciles à copier-coller — sync, async, streaming, pagination, et tout "transport spécial" (comme `aiohttp`). Le README d'OpenAI démontre chacun succinctement. ([GitHub][1])
* **Référence d'API** : si générée par code, publier un site `api.md`/reference et le maintenir synchronisé avec les releases. ([GitHub][1])
* **Dossier d'exemples** : inclure des scripts minimaux et ciblés, plus un exemple "complet".

# Erreurs, nouvelles tentatives et timeouts (ce qu'il faut implémenter)

* **Hiérarchie d'erreurs** : `YourLibError` → `APIError`, `AuthError`, `RateLimitError`, `TimeoutError`. Faire correspondre les codes de statut HTTP aux exceptions ; inclure les IDs de requête.
* **Nouvelles tentatives** : les opérations idempotentes devraient réessayer automatiquement avec un backoff exponentiel + jitter sur les erreurs 429/5xx.
* **Timeouts** : définir des valeurs par défaut sensibles et les rendre configurables au niveau du client et par appel.
* **Crochets de journalisation** : journalisation de débogage structurée sans fuite de secrets.

# Packaging & compatibilité

* **Supporter 3–4 versions mineures actives de Python** (par ex., 3.9–3.13), et les tester en CI.
* **Aucun effet de bord à l'importation** ; reporter la création du réseau/du client jusqu'au premier usage.
* **Configuration par environnement** : accepter la variable d'environnement `API_KEY` mais permettre aussi aux utilisateurs de passer les credentials explicitement (OpenAI montre `OPENAI_API_KEY` et une astuce `.env`). ([GitHub][1])
* **API publique stable** : garder les internes privés (`_module.py`), ré-exporter une surface soignée dans `__init__.py`.

# Pièges à éviter

* Tout entasser dans un seul module ; séparer par ressource et garder les imports publics stables.
* Fuiter les types de transport ; vos ressources doivent dépendre d'un petit protocole "transport", pas de `httpx` directement.
* Rendre l'async secondaire ; s'assurer que les tests et les exemples couvrent les deux également (la parité d'OpenAI est un bon modèle). ([GitHub][1])
* Pour le streaming, ne pas forcer les utilisateurs à jongler avec les threads ou les callbacks — les itérateurs sont plus simples. ([GitHub][1])

Si vous le souhaitez, je peux échafauder cette structure pour un domaine concret (par ex., un client typé pour vos services REST internes, avec sync/async, pagination et streaming) et y insérer des scripts `nox`, CI et exemples prêts à l'emploi.

[1]: https://github.com/openai/openai-python "GitHub - openai/openai-python: The official Python library for the OpenAI API"
[2]: https://github.com/openai/openai-python/tree/main/.github "openai-python/.github at main · openai/openai-python · GitHub"