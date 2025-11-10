---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Sessions HTTP persistantes avec Python Requests
translated: true
type: note
---

Une `Session` dans la bibliothèque `requests` de Python permet de conserver certains paramètres, tels que les cookies, les en-têtes et l'authentification, à travers plusieurs requêtes HTTP. Elle fournit une interface pratique pour effectuer des requêtes répétées vers le même serveur ou des endpoints connexes tout en maintenant l'état, en améliorant l'efficacité et en simplifiant le code. Ci-dessous, j'expliquerai le fonctionnement de `requests.Session`, ses principales caractéristiques et fournirai des exemples pour illustrer son utilisation.

## Qu'est-ce qu'une `requests.Session` ?

La bibliothèque `requests` est largement utilisée pour effectuer des requêtes HTTP en Python. Bien que vous puissiez utiliser des fonctions autonomes comme `requests.get()` ou `requests.post()`, un objet `Session` vous permet de créer une session persistante qui conserve les configurations (par exemple, les cookies, les en-têtes ou les informations d'authentification) à travers plusieurs requêtes. Ceci est particulièrement utile pour interagir avec des sites web ou des API qui nécessitent des interactions avec état, comme le maintien d'une session de connexion ou la réutilisation des connexions TCP.

Un objet `Session` :
- Conserve les cookies entre les requêtes.
- Réutilise les connexions TCP sous-jacentes (via le regroupement de connexions) pour de meilleures performances lors de requêtes multiples vers le même hôte.
- Vous permet de définir des paramètres par défaut (par exemple, les en-têtes, les timeouts) qui s'appliquent à toutes les requêtes effectuées avec la session.
- Prend en charge l'authentification et les configurations personnalisées.

## Comment fonctionne une `Session` ?

Lorsque vous créez un objet `Session`, il agit comme un conteneur pour vos requêtes HTTP. Voici un aperçu de son fonctionnement :

1. **Cookies persistants** : Lorsque vous effectuez une requête avec une `Session`, tous les cookies définis par le serveur (par exemple, les cookies de session après une connexion) sont stockés dans la session et automatiquement envoyés dans les requêtes suivantes. Ceci est essentiel pour maintenir l'état, comme rester connecté.

2. **Regroupement de connexions** : Pour les requêtes vers le même hôte, la `Session` réutilise la même connexion TCP, réduisant la latence et la surcharge par rapport à la création de nouvelles connexions pour chaque requête.

3. **Paramètres par défaut** : Vous pouvez définir des attributs comme les en-têtes, l'authentification ou les timeouts sur l'objet `Session`, et ils s'appliqueront à toutes les requêtes effectuées avec cette session, sauf s'ils sont remplacés.

4. **Personnalisable** : Vous pouvez configurer des proxies, la vérification SSL, ou même monter des adaptateurs personnalisés (par exemple, pour les nouvelles tentatives ou un transport personnalisé) pour contrôler la façon dont les requêtes sont traitées.

## Utilisation de base

Voici un exemple simple d'utilisation de `requests.Session` :

```python
import requests

# Créer une session
session = requests.Session()

# Définir les en-têtes par défaut pour toutes les requêtes de cette session
session.headers.update({'User-Agent': 'MyApp/1.0'})

# Effectuer une requête GET
response1 = session.get('https://api.example.com/data')
print(response1.json())

# Effectuer une autre requête ; les cookies et les en-têtes sont réutilisés
response2 = session.post('https://api.example.com/submit', data={'key': 'value'})
print(response2.json())

# Fermer la session pour libérer les ressources
session.close()
```

Dans cet exemple :
- Une `Session` est créée et un en-tête `User-Agent` personnalisé est défini pour toutes les requêtes.
- La session gère les cookies automatiquement, donc si `response1` définit un cookie, il est envoyé avec `response2`.
- La session réutilise la connexion vers `api.example.com`, améliorant les performances.

## Caractéristiques principales et exemples

### 1. **Conservation des cookies**
Les sessions sont particulièrement utiles pour les sites web qui utilisent des cookies pour maintenir l'état, comme les sessions de connexion.

```python
import requests

# Créer une session
session = requests.Session()

# Se connecter à un site web
login_data = {'username': 'user', 'password': 'pass'}
response = session.post('https://example.com/login', data=login_data)

# Accéder à une page protégée ; la session envoie automatiquement le cookie de connexion
protected_page = session.get('https://example.com/protected')
print(protected_page.text)

# Fermer la session
session.close()
```

Ici, la session stocke le cookie d'authentification de la requête de connexion et l'envoie avec la requête suivante vers la page protégée.

### 2. **Définition de paramètres par défaut**
Vous pouvez définir des en-têtes, une authentification ou d'autres paramètres par défaut pour toutes les requêtes de la session.

```python
import requests

session = requests.Session()

# Définir les en-têtes par défaut
session.headers.update({
    'Authorization': 'Bearer my_token',
    'Accept': 'application/json'
})

# Définir le timeout par défaut
session.request = functools.partial(session.request, timeout=5)

# Effectuer des requêtes ; les en-têtes et le timeout sont automatiquement appliqués
response1 = session.get('https://api.example.com/endpoint1')
response2 = session.get('https://api.example.com/endpoint2')

session.close()
```

### 3. **Regroupement de connexions**
Lorsque vous effectuez plusieurs requêtes vers le même hôte, `Session` réutilise les connexions, ce qui est plus efficace que les requêtes autonomes.

```python
import requests
import time

# Sans session
start = time.time()
for _ in range(5):
    requests.get('https://api.example.com/data')
print(f"Sans session: {time.time() - start} seconds")

# Avec session
session = requests.Session()
start = time.time()
for _ in range(5):
    session.get('https://api.example.com/data')
print(f"Avec session: {time.time() - start} seconds")
session.close()
```

Les requêtes basées sur une session sont généralement plus rapides car elles réutilisent la connexion TCP.

### 4. **Authentification**
Les sessions simplifient la gestion de l'authentification, comme l'authentification HTTP Basic ou l'authentification personnalisée par jeton.

```python
import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()
session.auth = HTTPBasicAuth('user', 'pass')

# Toutes les requêtes incluront l'authentification Basic
response = session.get('https://api.example.com/protected')
print(response.json())

session.close()
```

### 5. **Adaptateurs personnalisés**
Vous pouvez monter des adaptateurs personnalisés pour contrôler des aspects comme les nouvelles tentatives ou le comportement du regroupement de connexions.

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

# Configurer les nouvelles tentatives
retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

# Effectuer une requête avec une logique de nouvelle tentative
response = session.get('https://api.example.com/unstable_endpoint')
print(response.json())

session.close()
```

Cet exemple configure des nouvelles tentatives automatiques pour des codes d'erreur HTTP spécifiques.

## Quand utiliser une `Session`

Utilisez `requests.Session` lorsque :
- Vous devez maintenir l'état (par exemple, les cookies) à travers plusieurs requêtes, comme pour l'authentification.
- Vous effectuez plusieurs requêtes vers le même hôte et souhaitez bénéficier du regroupement de connexions.
- Vous voulez appliquer des configurations cohérentes (en-têtes, timeouts, etc.) à travers les requêtes.
- Vous interagissez avec des API ou des sites web qui nécessitent des interactions basées sur des sessions.

Si vous effectuez une seule requête ou n'avez pas besoin de conserver l'état, les fonctions autonomes `requests.get()` ou `requests.post()` sont suffisantes.

## Fermeture d'une session

Fermez toujours une session lorsque vous avez terminé pour libérer les ressources (par exemple, les connexions) :

```python
session.close()
```

Alternativement, utilisez une session comme gestionnaire de contexte pour garantir sa fermeture automatique :

```python
with requests.Session() as session:
    session.headers.update({'User-Agent': 'MyApp/1.0'})
    response = session.get('https://api.example.com/data')
    print(response.json())
# La session est automatiquement fermée à la sortie du bloc
```

## Notes avancées
- **Sécurité des threads** : Les objets `Session` ne sont pas thread-safe. Si vous utilisez le multithreading, créez une `Session` distincte pour chaque thread.
- **Proxies** : Vous pouvez définir des proxies sur une session avec `session.proxies = {'http': 'http://proxy.com', 'https': 'https://proxy.com'}`.
- **Vérification SSL** : Par défaut, `Session` vérifie les certificats SSL. Pour désactiver (non recommandé en production), utilisez `session.verify = False`.

## Références
[Documentation de Requests](https://requests.readthedocs.io/en/latest/)  
[Objets Session de Requests](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects)