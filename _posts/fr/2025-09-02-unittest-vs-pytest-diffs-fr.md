---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Unittest contre Pytest Principales Différences
translated: true
type: note
---

Voici une comparaison concise, sans tableau, axée sur ce qui change réellement dans vos tests quotidiens.

# Philosophie & Style

* **unittest** : Style xUnit (ressemble à Java/JUnit). Tests basés sur des classes, hooks de cycle de vie comme `setUp/tearDown`, les noms de méthodes doivent commencer par `test_`.
* **pytest** : Pythonique et minimal. **Fonctions** de test ou classes, fixtures riches, `assert` simple avec réécriture des assertions.

# Découverte des Tests

* **unittest** : `python -m unittest discover` (ou chargement de suites). Cherche `test*.py`, les sous-classes de `TestCase`.
* **pytest** : `pytest` découvre automatiquement `test_*.py` et `*_test.py` ; les fonctions `test_*` et les méthodes des classes `Test*`.

# Assertions

* **unittest** : De nombreuses méthodes spécifiques (`assertEqual`, `assertTrue`, `assertRaises`, …).
* **pytest** : Utilisez `assert` simple et il affiche des différences expressives ("gauche vs droite"), supporte `pytest.raises`.

# Fixtures & Configuration

* **unittest** : `setUp()/tearDown()`, `setUpClass/tearDownClass`, `setUpModule/tearDownModule`.
* **pytest** : **Fixtures** avec portées (fonction/classe/module/session), injection de dépendances, autouse, finaliseurs. Encourage une configuration petite et réutilisable.

# Paramétrisation

* **unittest** : Aucune intégrée ; utilisez des boucles/subTests ou des librairies tierces.
* **pytest** : `@pytest.mark.parametrize` est natif (matrice d'entrées, reporting clair).

# Sauts, Échecs Attendus, Marqueurs

* **unittest** : `@skip`, `@skipIf`, `@expectedFailure`.
* **pytest** : Mêmes idées plus des **marqueurs** puissants (`@pytest.mark.slow`, `xfail`, `filterwarnings`, marqueurs personnalisés) et sélection en ligne de commande (`-m slow`).

# Plugins & Écosystème

* **unittest** : Batteries incluses mais léger ; repose sur des outils/exécuteurs externes pour les fonctionnalités avancées.
* **pytest** : Énorme écosystème de plugins (`pytest-xdist` pour le parallèle, `pytest-randomly`, `pytest-cov`, `pytest-mock`, `pytest-asyncio`, `pytest-django`, etc.).

# Mocks

* **unittest** : `unittest.mock` est standard ; fonctionne partout.
* **pytest** : Utilisez `unittest.mock` ou la fixture `mocker` de `pytest-mock` (patch plus propre et auto-nettoyage).

# Tests Async

* **unittest** : Depuis la 3.8, dispose de `IsolatedAsyncioTestCase` (correct mais verbeux).
* **pytest** : Avec `pytest-asyncio` (ou le plugin trio) vous obtenez `@pytest.mark.asyncio` et le support des fixtures pour les boucles d'événements.

# Performance & Parallélisme

* **unittest** : Aucun parallélisme intégré ; utilisez `unittest-parallel`/astuces CI.
* **pytest** : `pytest-xdist -n auto` est la solution privilégiée.

# IDE/CI/Couverture

* Les deux s'intègrent avec les IDE et la CI. Couverture via `coverage.py` :

  * **unittest** : `coverage run -m unittest` → `coverage report`.
  * **pytest** : `pytest --cov=your_pkg` avec `pytest-cov`.

# Quand choisir lequel

* **Choisissez unittest** si :

  * Vous n'avez besoin que de la bibliothèque standard (pas de dépendances externes).
  * Vous vous intégrez à des bases de code legacy/xUnit ou à des politiques d'entreprise strictes.
* **Choisissez pytest** si :

  * Vous voulez une rédaction plus rapide, des échecs plus clairs et des fixtures/paramétrisation puissantes.
  * Vous profiterez de son écosystème de plugins et de son parallélisme.

# Interopérabilité & Migration

Vous pouvez exécuter les suites **unittest** sous **pytest** (pytest trouve les `unittest.TestCase`). Cela vous permet de migrer progressivement :

1. Commencez à invoquer `pytest` comme exécuteur.
2. Ajoutez des tests pytest à côté des tests existants.
3. Introduisez des fixtures/paramétrisation là où elles aident.
4. Optionnellement, refactorisez les anciens `TestCase` en fonctions plus tard.

# Petits exemples côte à côte

## Le même test

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

## Paramétrisation

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

# Recommandations pratiques

* Nouveaux projets : par défaut, utilisez **pytest** pour la vitesse, la lisibilité et l'écosystème.
* Environnements legacy/stdlib uniquement : restez avec **unittest**, mais envisagez de l'exécuter via **pytest** pour débloquer une meilleure sortie et des plugins sans réécrire les tests.
* Ajoutez `pytest-xdist` tôt pour une CI plus rapide, et `pytest-cov` pour la couverture.
* Utilisez des fixtures plutôt que de grandes configurations de classe ; gardez-les petites et composables.
* Utilisez des marqueurs pour organiser les suites (`slow`, `integration`, `db`) et exécutez des sous-ensembles dans les étapes de la CI.

Si vous le souhaitez, décrivez-moi la structure de votre projet et ses contraintes (stdlib uniquement ? besoin de parallélisme ? async ? Django/Flask/FastAPI ?) et je vous esquisserai une configuration de test minimale et orientée.