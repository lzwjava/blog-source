---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration du proxy Python Requests via .env
translated: true
type: note
---

### Utilisation d'un fichier `.env` pour configurer les proxys HTTP/HTTPS pour Python Requests

La bibliothèque `requests` en Python respecte automatiquement les variables d'environnement standard comme `HTTP_PROXY` et `HTTPS_PROXY` pour la configuration des proxys. Pour les gérer de manière sécurisée (par exemple, sans les coder en dur dans votre script), vous pouvez les stocker dans un fichier `.env` et les charger en utilisant la bibliothèque `python-dotenv`. Cela permet de garder les informations sensibles sur les proxys en dehors de votre code.

#### Étape 1 : Installer les paquets requis
Vous aurez besoin de `requests` (si ce n'est pas déjà installé) et de `python-dotenv` pour charger le fichier `.env`.

```bash
pip install requests python-dotenv
```

#### Étape 2 : Créer un fichier `.env`
À la racine de votre projet, créez un fichier nommé `.env` (sans extension) et ajoutez-y vos paramètres de proxy. Utilisez le format `http://` ou `https://` pour l'URL du proxy, en incluant le nom d'utilisateur et le mot de passe si nécessaire.

Exemple de contenu du fichier `.env` :
```
HTTP_PROXY=http://username:password@proxy-host:port
HTTPS_PROXY=https://username:password@proxy-host:port
NO_PROXY=localhost,127.0.0.1,example.com  # Optionnel : Exclure les domaines du proxy
```

- `HTTP_PROXY` : Pour le trafic HTTP.
- `HTTPS_PROXY` : Pour le trafic HTTPS (souvent le même que `HTTP_PROXY`).
- `NO_PROXY` : Liste d'hôtes/adresses IP séparés par des virgules à exclure du proxy.
- Remarque : Les variables d'environnement ne sont pas sensibles à la casse, mais la convention est d'utiliser les majuscules.

Ajoutez `.env` à votre fichier `.gitignore` pour éviter de commettre des informations sensibles.

#### Étape 3 : Charger le fichier `.env` dans votre script Python
Au début de votre script, chargez les variables d'environnement :

```python
from dotenv import load_dotenv
import requests

# Charger les variables depuis le fichier .env
load_dotenv()  # Recherche .env dans le répertoire courant par défaut

# Maintenant, faites une requête – les proxys sont appliqués automatiquement
response = requests.get('https://httpbin.org/ip')
print(response.json())
```

- `load_dotenv()` lit le fichier `.env` et définit les variables dans `os.environ`.
- `requests` détectera automatiquement `HTTP_PROXY`/`HTTPS_PROXY` – pas besoin de passer un dictionnaire `proxies` sauf pour les remplacer.

#### Étape 4 : Vérifier l'utilisation du proxy (Optionnel)
Pour confirmer que les proxys fonctionnent, testez avec un service comme httpbin.org :

```python
import requests
from dotenv import load_dotenv

load_dotenv()

proxies = requests.utils.get_environ_proxies('https://httpbin.org/ip')  # Inspecter les proxys chargés
print("Proxys chargés :", proxies)

response = requests.get('https://httpbin.org/ip')
print("Votre IP via le proxy :", response.json())
```

Cela devrait afficher l'IP du serveur proxy s'il est configuré correctement.

#### Problèmes courants et conseils
- **Authentification du proxy** : Incluez `username:password@` dans l'URL si nécessaire.
- **Proxys SOCKS** : Utilisez le préfixe `socks5://` (nécessite l'extra `requests[socks]` : `pip install requests[socks]`).
- **Remplacement par requête** : Si vous avez besoin de proxys différents pour un appel spécifique, passez un dictionnaire :
  ```python:disable-run
  proxies = {'http': 'http://custom-proxy:port', 'https': 'https://custom-proxy:port'}
  response = requests.get('url', proxies=proxies)
  ```
- **Environnement** : Fonctionne sur Windows/Linux/macOS. Sur Windows, utilisez `set` dans l'invite de commandes ou les équivalents PowerShell.
- **Sécurité** : Ne commettez jamais `.env` dans le contrôle de version.

Cette configuration est simple, sécurisée et suit les bonnes pratiques pour la configuration basée sur l'environnement.

[Documentation Requests : Proxys](https://requests.readthedocs.io/en/latest/user/advanced/#proxies)  
[Documentation python-dotenv](https://github.com/theskumar/python-dotenv)