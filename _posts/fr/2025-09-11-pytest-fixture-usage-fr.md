---
audio: false
date: 2025-09-11
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Comprendre l'Utilisation des Fixtures Pytest
translated: true
type: note
---

## Qu'est-ce que `@pytest.fixture` ?

`@pytest.fixture` est un décorateur qui marque une fonction comme une **fixture** - une fonction spéciale qui fournit des données de test, une configuration ou une fonctionnalité de nettoyage à vos tests. Les fixtures sont l'une des fonctionnalités les plus puissantes de pytest et une raison clé pour laquelle de nombreux développeurs préfèrent pytest au module `unittest` intégré à Python.

## Comment fonctionnent les Fixtures

Les fixtures suivent un modèle simple mais puissant :

1.  **Configuration** : Le code avant l'instruction `yield` s'exécute avant le test
2.  **Exécution du test** : Le test s'exécute lorsqu'il atteint l'instruction `yield`
3.  **Nettoyage** : Le code après l'instruction `yield` s'exécute après la fin du test

### Exemple de Fixture Basique

```python
import pytest

@pytest.fixture
def sample_data():
    # Code de configuration
    data = {"name": "John", "age": 30}
    yield data  # Le test s'exécute ici
    # Code de nettoyage (s'exécute après le test)
    print("Nettoyage des données d'exemple")
```

## Pourquoi avons-nous besoin de Fixtures

Les fixtures résolvent plusieurs problèmes courants de test :

1.  **Isolation des tests** : Garantir que chaque test s'exécute avec des données fraîches et prévisibles
2.  **Réutilisation du code** : Éviter la répétition du code de configuration/nettoyage dans plusieurs tests
3.  **Gestion des ressources** : Gérer correctement les ressources comme les connexions à la base de données, les fichiers ou les connexions réseau
4.  **Clarté des tests** : Permettre aux fonctions de test de se concentrer sur ce qu'elles testent, et non sur la configuration
5.  **Injection de dépendance** : Fournir exactement ce dont chaque test a besoin

## Caractéristiques clés des Fixtures

### 1. Injection de Dépendance

Les fixtures peuvent dépendre d'autres fixtures, créant un graphe de dépendances :

```python
@pytest.fixture
def database_connection():
    # Configuration de la connexion à la base de données
    conn = create_connection()
    yield conn
    conn.close()

@pytest.fixture
def user_table(database_connection):
    # Utilise la fixture database_connection
    create_table(database_connection, "users")
    yield
    drop_table(database_connection, "users")
```

### 2. Contrôle de la Portée

Les fixtures peuvent avoir différentes durées de vie :

```python
@pytest.fixture(scope="function")  # Par défaut - s'exécute une fois par test
def per_test_fixture():
    pass

@pytest.fixture(scope="module")  # S'exécute une fois par module
def per_module_fixture():
    pass

@pytest.fixture(scope="session")  # S'exécute une fois par session de test
def per_session_fixture():
    pass
```

### 3. Fixtures à Utilisation Automatique

Les fixtures peuvent s'exécuter automatiquement sans être demandées :

```python
@pytest.fixture(autouse=True)
def always_run_this():
    # Ceci s'exécute avant chaque test dans le module
    yield
    # Ceci s'exécute après chaque test
```

### 4. Fixtures Paramétrées

Les fixtures peuvent générer plusieurs ensembles de données :

```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param  # Exécutera les tests avec 1, 2 et 3
```

## Exemple Pratique avec des Tests d'API

Voici comment les fixtures aident dans votre scénario de test d'en-tête financier :

```python
import pytest
import requests

@pytest.fixture
def financial_header():
    # Configuration - création de l'en-tête
    headers = create_financial_header()  # Votre logique de création
    yield headers  # Le test s'exécute ici avec ces en-têtes

    # Nettoyage - suppression de l'en-tête
    delete_financial_header(headers)  # Votre logique de nettoyage

def test_submit_transaction(financial_header):
    # La fixture fournit automatiquement les en-têtes
    response = requests.post(
        "https://api.example.com/transactions",
        headers=financial_header,
        json={"amount": 100}
    )
    assert response.status_code == 201

def test_validate_header(financial_header):
    # La même fixture utilisée dans un autre test
    response = requests.get(
        "https://api.example.com/validate",
        headers=financial_header
    )
    assert response.json()["valid"] is True
```

## Comparaison avec unittest

| Fonctionnalité         | Fixtures pytest                    | unittest setUp/tearDown          |
|------------------------|------------------------------------|----------------------------------|
| Injection de dépendance | ✅ Oui                             | ❌ Non                            |
| Contrôle de la portée  | ✅ Fonction, classe, module, session | ❌ Niveau méthode/classe uniquement |
| Syntaxe propre         | ✅ Décorateur simple               | ❌ Nécessite l'héritage           |
| Isolation des tests    | ✅ Chaque test obtient des fixtures fraîches | ❌ L'état partagé peut causer des problèmes |
| Paramétrisation        | ✅ Prise en charge intégrée        | ❌ Implémentation manuelle nécessaire |

## Quand Utiliser les Fixtures

Utilisez les fixtures lorsque vous avez besoin de :
- Configurer des données ou des objets de test
- Gérer des ressources externes (connexions DB, fichiers, etc.)
- Effectuer un nettoyage après les tests
- Partager des dépendances de test communes
- Créer différents environnements de test
- Implémenter une logique de configuration/nettoyage complexe

Les fixtures sont particulièrement précieuses dans les tests d'API (comme votre cas d'en-tête financier) car elles aident à gérer le cycle de vie des ressources de test de manière propre et prévisible.