---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide des certificats SSL Python Certifi
translated: true
type: note
---

Le paquet **`certifi`** sur PyPI est une petite bibliothèque qui fournit **les certificats racines de confiance de Mozilla** dans un bundle. Il est couramment utilisé par des bibliothèques Python comme `requests`, `urllib3`, ou tout client HTTPS qui a besoin de valider les certificats SSL/TLS.

Voici comment l'utiliser :

---

### 1. Installer `certifi`

```bash
pip install certifi
```

---

### 2. Obtenir le chemin du bundle d'AC

En Python :

```python
import certifi

print(certifi.where())
```

Cela affichera le chemin complet vers le bundle de certificats d'AC (un fichier `.pem`). Par exemple :

```
/usr/local/lib/python3.11/site-packages/certifi/cacert.pem
```

---

### 3. Utilisation avec `requests` ou `urllib3`

```python
import requests
import certifi

response = requests.get("https://example.com", verify=certifi.where())
print(response.status_code)
```

Par défaut, `requests` utilise déjà `certifi` en interne, mais passer explicitement `verify=certifi.where()` garantit l'utilisation du bundle mis à jour.

---

### 4. Utilisation dans d'autres bibliothèques HTTPS

Si vous travaillez directement avec `urllib3` :

```python
import urllib3
import certifi

http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)

response = http.request("GET", "https://example.com")
print(response.status)
```

---

### 5. Utilisation système (optionnel)

Parfois, vous pouvez souhaiter pointer une application vers le bundle d'AC de certifi :

```bash
export SSL_CERT_FILE=$(python -m certifi)
```

---

👉 En bref :

* Installez avec `pip install certifi`
* Utilisez `certifi.where()` pour obtenir le chemin du bundle de certificats
* Passez-le aux bibliothèques qui ont besoin d'une validation de certificat

---

Voulez-vous que je vous montre aussi **comment faire en sorte que votre environnement Python entier utilise les certificats de certifi par défaut**, afin que vous n'ayez pas besoin de configurer chaque bibliothèque individuellement ?