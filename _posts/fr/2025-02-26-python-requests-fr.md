---
audio: false
generated: true
lang: fr
layout: post
title: Bibliothèque Python Requests
translated: true
type: note
---

Pour remplacer complètement Postman par la bibliothèque Python `requests`, vous pouvez effectuer toutes les opérations HTTP courantes telles que l'envoi de différents types de requêtes, la gestion des en-têtes, le travail avec des données JSON, le téléchargement de fichiers, l'utilisation de proxies et la vérification des réponses. Ci-dessous, je vais vous guider à travers des exemples pour chacune de ces fonctionnalités étape par étape, afin de vous fournir un guide complet et pratique.

### Étape 1 : Installer la bibliothèque Requests
Avant de commencer, assurez-vous que la bibliothèque `requests` est installée. Exécutez cette commande dans votre terminal :

```bash
pip install requests
```

Maintenant, plongeons dans les exemples.

---

### Envoi de requêtes HTTP
La bibliothèque `requests` prend en charge toutes les méthodes HTTP comme GET, POST, PUT, DELETE, etc. Voici comment envoyer une simple requête GET et POST :

#### Requête GET
```python
import requests

# Envoyer une requête GET
response = requests.get('https://api.example.com/data')

# Afficher le code statut et le corps de la réponse
print("Code statut :", response.status_code)
print("Corps de la réponse :", response.text)
```

#### Requête POST
```python
# Envoyer une requête POST sans données
response = requests.post('https://api.example.com/submit')

print("Code statut :", response.status_code)
print("Corps de la réponse :", response.text)
```

---

### Ajout d'en-têtes
Les en-têtes sont souvent utilisés pour l'authentification, les types de contenu ou les métadonnées personnalisées. Transmettez-les sous forme de dictionnaire au paramètre `headers`.

```python
# Définir des en-têtes personnalisés
headers = {
    'Authorization': 'Bearer my_token',
    'Content-Type': 'application/json',
    'User-Agent': 'MyApp/1.0'
}

# Envoyer une requête GET avec des en-têtes
response = requests.get('https://api.example.com/data', headers=headers)

print("Code statut :", response.status_code)
print("En-têtes de la réponse :", response.headers)
print("Corps de la réponse :", response.text)
```

---

### Envoi de données JSON
Pour envoyer des données JSON dans une requête POST (comme sélectionner JSON dans l'onglet body de Postman), utilisez le paramètre `json`. Cela définit automatiquement le `Content-Type` sur `application/json`.

```python
# Définir les données JSON
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# Envoyer une requête POST avec des données JSON
response = requests.post('https://api.example.com/submit', json=data, headers=headers)

print("Code statut :", response.status_code)
print("Réponse JSON :", response.json())
```

---

### Téléchargement de fichiers
Pour télécharger des fichiers (similaire à l'option form-data de Postman), utilisez le paramètre `files`. Ouvrez les fichiers en mode binaire (`'rb'`) et incluez éventuellement des données de formulaire supplémentaires.

#### Téléchargement simple de fichier
```python
# Préparer le fichier pour le téléchargement
files = {
    'file': open('myfile.txt', 'rb')
}

# Envoyer une requête POST avec le fichier
response = requests.post('https://api.example.com/upload', files=files)

print("Code statut :", response.status_code)
print("Corps de la réponse :", response.text)

# Fermer le fichier manuellement
files['file'].close()
```

#### Téléchargement de fichier avec données de formulaire (Approche recommandée)
L'utilisation d'une instruction `with` garantit que le fichier est fermé automatiquement :
```python
# Données de formulaire supplémentaires
form_data = {
    'description': 'Mon téléchargement de fichier'
}

# Ouvrir et télécharger le fichier
with open('myfile.txt', 'rb') as f:
    files = {
        'file': f
    }
    response = requests.post('https://api.example.com/upload', data=form_data, files=files)

print("Code statut :", response.status_code)
print("Corps de la réponse :", response.text)
```

---

### Utilisation de proxies
Pour router les requêtes via un proxy (similaire aux paramètres de proxy de Postman), utilisez le paramètre `proxies` avec un dictionnaire.

```python
# Définir les paramètres du proxy
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# Envoyer une requête via un proxy
response = requests.get('https://api.example.com/data', proxies=proxies)

print("Code statut :", response.status_code)
print("Corps de la réponse :", response.text)
```

---

### Gestion et vérification des réponses
La bibliothèque `requests` permet un accès facile aux détails de la réponse comme les codes statut, les données JSON, les en-têtes et les cookies. Vous pouvez utiliser les instructions `assert` de Python pour valider les réponses, similaire aux test scripts de Postman.

#### Analyse des réponses JSON
```python
response = requests.get('https://api.example.com/data')

# Vérifier le code statut et analyser le JSON
if response.status_code == 200:
    data = response.json()  # Convertit la réponse en dict/list Python
    print("Données JSON :", data)
else:
    print("Erreur :", response.status_code)
```

#### Vérification des détails de la réponse
```python
response = requests.get('https://api.example.com/data')

# Vérifier le code statut
assert response.status_code == 200, f"Attendu 200, reçu {response.status_code}"

# Analyser le JSON et vérifier le contenu
data = response.json()
assert 'key' in data, "Clé non trouvée dans la réponse"
assert data['key'] == 'expected_value', "La valeur ne correspond pas"

# Vérifier les en-têtes de la réponse
assert 'Content-Type' in response.headers, "En-tête Content-Type manquant"
assert response.headers['Content-Type'] == 'application/json', "Content-Type inattendu"

# Vérifier les cookies
cookies = response.cookies
assert 'session_id' in cookies, "Cookie Session ID manquant"

print("Toutes les vérifications sont passées !")
```

#### Gestion des erreurs
Encapsulez les requêtes dans un bloc `try-except` pour intercepter les erreurs réseau ou HTTP :
```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # Lève une exception pour les erreurs 4xx/5xx
    data = response.json()
    print("Données :", data)
except requests.exceptions.RequestException as e:
    print("Échec de la requête :", e)
```

---

### Exemple complet
Voici un exemple complet combinant les en-têtes, le téléchargement de fichier, les proxies et les vérifications de réponse :

```python
import requests

# Définir les en-têtes
headers = {
    'Authorization': 'Bearer my_token'
}

# Données de formulaire et fichier
form_data = {
    'description': 'Mon téléchargement de fichier'
}

# Paramètres du proxy
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# Envoyer la requête avec téléchargement de fichier
try:
    with open('myfile.txt', 'rb') as f:
        files = {'file': f}
        response = requests.post(
            'https://api.example.com/upload',
            headers=headers,
            data=form_data,
            files=files,
            proxies=proxies
        )
        response.raise_for_status()  # Vérifier les erreurs HTTP

        # Analyser et vérifier la réponse
        data = response.json()
        assert 'upload_id' in data, "Upload ID non trouvé dans la réponse"
        print("Téléchargement réussi, ID :", data['upload_id'])

except requests.exceptions.RequestException as e:
    print("Échec de la requête :", e)
```

---

### Fonctions réutilisables (Remplacer les collections Postman)
Pour imiter les requêtes sauvegardées ou les collections Postman, encapsulez la logique dans des fonctions :

```python
def upload_file(file_path, description, token, proxy=None):
    headers = {'Authorization': f'Bearer {token}'}
    data = {'description': description}
    proxies = {'http': proxy, 'https': proxy} if proxy else None

    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(
                'https://api.example.com/upload',
                headers=headers,
                data=data,
                files=files,
                proxies=proxies
            )
            response.raise_for_status()
            data = response.json()
            assert 'upload_id' in data, "Upload ID non trouvé"
            return data['upload_id']
    except requests.exceptions.RequestException as e:
        print("Échec de la requête :", e)
        return None

# Utilisation
upload_id = upload_file('myfile.txt', 'Mon téléchargement de fichier', 'my_token', 'http://myproxy:8080')
if upload_id:
    print("Téléchargement réussi, ID :", upload_id)
```

---

### Fonctionnalités supplémentaires
- **Sessions** : Utilisez `requests.Session()` pour conserver les cookies ou les en-têtes sur plusieurs requêtes.
- **Timeouts** : Ajoutez `timeout=5` (secondes) aux requêtes pour éviter les blocages.
- **Redirections** : Contrôlez avec `allow_redirects=True/False`.

---

### Résumé
Avec la bibliothèque `requests`, vous pouvez :
- Envoyer des requêtes HTTP (`get`, `post`, etc.)
- Inclure des en-têtes, des données JSON et des téléchargements de fichiers
- Utiliser des proxies
- Analyser et vérifier les réponses (statut, JSON, en-têtes, cookies)
- Organiser le code en fonctions réutilisables

Cela vous offre une alternative programmatique et flexible à Postman, adaptée au scripting et à l'automatisation !