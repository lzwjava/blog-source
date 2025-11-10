---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Utiliser requests.Session pour des sessions HTTP persistantes
translated: true
type: note
---

### Fonctionnement de requests.Session

Dans la bibliothèque `requests` de Python, `requests.Session` est une classe qui permet de maintenir une session persistante à travers plusieurs requêtes HTTP. Elle offre plusieurs avantages par rapport à l'utilisation d'appels individuels comme `requests.get()` :

- **Persistance des cookies** : Par défaut, elle stocke et envoie automatiquement les cookies reçus du serveur dans les requêtes suivantes. Cela permet des interactions basées sur des sessions, comme se connecter une fois et rester authentifié.
- **Regroupement de connexions** : Elle réutilise les connexions TCP sous-jacentes pour le même hôte, améliorant ainsi les performances en évitant la surcharge liée à l'établissement de nouvelles connexions.
- **Configurations partagées** : Vous pouvez définir des en-têtes par défaut, une authentification, des proxies ou d'autres paramètres qui s'appliquent à toutes les requêtes de la session.
- **Sous le capot** : Elle utilise la bibliothèque `urllib3` pour la gestion HTTP. Lorsque vous créez une `Session`, elle initialise des attributs comme `cookies` (une instance de `RequestsCookieJar`), `headers`, et plus encore. Par exemple, les cookies d'une réponse sont automatiquement inclus dans la requête suivante vers le même domaine.

Voici un exemple basique de création et d'utilisation d'une session :

```python
import requests

# Créer une session
session = requests.Session()

# Définir un en-tête par défaut pour toutes les requêtes de cette session
session.headers.update({'User-Agent': 'MyApp/1.0'})

# Effectuer plusieurs requêtes, en partageant la session
response1 = session.get('https://example.com/login')
response2 = session.post('https://example.com/data', data={'key': 'value'})

# Accéder aux cookies stockés dans la session
print(session.cookies)
```

Cela garantit que les cookies (comme les ID de session) sont gérés de manière transparente sans intervention manuelle.

### Utiliser Python pour appeler les API de projets Java/Spring

Pour interagir avec les API construites en utilisant Java/Spring (généralement des points de terminaison RESTful via Spring MVC ou Spring Boot), vous utilisez `requests.Session` comme avec n'importe quelle API HTTP. Les projets Spring exposent souvent des API via HTTP/HTTPS, et `requests` peut gérer l'authentification, les jetons CSRF ou la limitation de débit si elles sont implémentées.

- **Authentification** : Spring peut utiliser Spring Security avec des formulaires, JWT ou OAuth. Pour une authentification basée sur une session (par exemple, via des formulaires de connexion), `requests.Session` automatise la gestion des cookies après une requête de connexion.
- **Effectuer des appels** : Utilisez les méthodes HTTP standard comme `GET`, `POST`, etc. Si l'API Spring nécessite des charges utiles JSON, passez `json=vos_données`.

Exemple de connexion à une API Spring authentifiée et d'appel à un autre point de terminaison :

```python
import requests

session = requests.Session()

# Se connecter (en supposant un POST vers /login avec nom d'utilisateur/mot de passe)
login_payload = {'username': 'user', 'password': 'pass'}
response = session.post('https://spring-api.example.com/login', data=login_payload)

if response.ok:
    # Maintenant, appeler un autre point de terminaison de l'API, les cookies de session persistent
    data_response = session.get('https://spring-api.example.com/api/data')
    print(data_response.json())
else:
    print("Échec de la connexion")
```

Les API Spring sont par défaut sans état mais peuvent gérer les sessions via un stockage côté serveur (par exemple, dans Tomcat ou des serveurs embarqués). Assurez-vous que votre client Python gère tout CORS, CSRF ou tout en-tête personnalisé requis par Spring.

### Relation avec JSESSIONID côté Java/Spring

- **Qu'est-ce que JSESSIONID ?** : Dans les applications web Java (y compris Spring, qui s'exécute souvent sur des conteneurs Servlet comme Tomcat), JSESSIONID est un cookie HTTP standard utilisé par le conteneur pour suivre les sessions utilisateur. Il est défini lorsqu'une session est créée (par exemple, après une connexion) et renvoyé dans les réponses. Côté client, les navigateurs (ou les clients HTTP comme `requests`) l'incluent dans les requêtes suivantes pour maintenir l'état, comme l'authentification de l'utilisateur ou les données d'un panier.
- **Comment cela se rapporte à requests.Session** : `requests.Session` traite JSESSIONID comme n'importe quel autre cookie — il le stocke automatiquement à partir de l'en-tête "Set-Cookie" du serveur et l'inclut dans l'en-tête "Cookie" des requêtes futures. Cela permet une interaction transparente avec les API Spring avec état sans avoir à analyser/extraire manuellement les cookies.
- **Gestion côté serveur** : Côté Java/Spring, le ServletContext gère les sessions. Lorsque votre client Python envoie une requête avec JSESSIONID, HttpSession de Spring récupère les données associées côté serveur. Si la session a expiré ou est invalide, Spring peut exiger une ré-authentification. Pour des sessions sécurisées, assurez-vous que votre configuration utilise HTTPS, car JSESSIONID peut être vulnérable au vol via HTTP.
- **Problèmes potentiels** : Si Spring applique des jetons CSRF ou d'autres protections, vous devrez peut-être les extraire et les inclure (par exemple, à partir de champs de formulaire cachés). Pour les API Spring sans état basées sur JWT, `requests.Session` aide toujours en conservant les jetons d'authentification dans les en-têtes, mais JSESSIONID devient moins pertinent.

Si vous rencontrez des erreurs spécifiques (par exemple, 401 Non autorisé) lors de l'appel d'une API Spring, vérifiez les logs réseau pour les problèmes de cookies ou activez le débogage de `requests` avec `import logging; logging.basicConfig(level=logging.DEBUG)`. Pour en savoir plus sur Spring Security, consultez leur documentation officielle.