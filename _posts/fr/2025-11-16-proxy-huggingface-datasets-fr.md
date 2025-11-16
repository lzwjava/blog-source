---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Utilisation d'un proxy avec les jeux de données Hugging Face
translated: true
type: note
---

Oui — `datasets` suit vos **paramètres proxy système / d'environnement**, mais il **n'a pas** sa propre configuration de proxy.
Vous pouvez donc absolument faire en sorte que Hugging Face télécharge des jeux de données via un proxy lorsque vous êtes en Chine.

Voici comment.

---

# Comment faire en sorte que `load_dataset` utilise un proxy (compatible Chine)

## 1. Définir les variables d'environnement pour le proxy HTTP/HTTPS

`datasets` utilise la bibliothèque `requests` de Python en interne.
`requests` utilise automatiquement les variables d'environnement de proxy standard :

### Linux / macOS

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

Si votre proxy utilise SOCKS5 :

```bash
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"
```

### Windows (PowerShell)

```powershell
setx HTTP_PROXY "http://127.0.0.1:7890"
setx HTTPS_PROXY "http://127.0.0.1:7890"
```

Puis rouvrez le terminal.

---

## 2. Si vous exécutez Python dans du code (comme Jupyter), définissez-les dans Python

```python
import os

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
```

Cela fonctionne de manière fiable.

---

## 3. Confirmer que le proxy fonctionne

Vous pouvez tester avec :

```python
import requests
print(requests.get("https://api.ipify.org?format=json").text)
```

Si l'IP est le nœud de sortie de votre proxy, alors les téléchargements de jeux de données Hugging Face passeront également par ce proxy.

---

## 4. Le `huggingface_hub` de Hugging Face respecte également ces variables

`datasets` utilise en interne `huggingface_hub`, et il suit **aussi** :

* `HTTP_PROXY`
* `HTTPS_PROXY`
* `http_proxy`
* `https_proxy`

Ainsi, une fois les variables d'environnement définies, les téléchargements de modèles et de jeux de données utiliseront automatiquement votre proxy.

---

# Notes sur l'utilisation en Chine

* Les téléchargements bruts de Hugging Face nécessitent souvent un proxy car ils sont hébergés sur des serveurs aux États-Unis/Europe.
* Si vous observez des délais d'expiration avec les fichiers de jeux de données `.zst`, c'est normal sans proxy.
* Un proxy global (Clash, V2Ray, Qv2ray, etc.) rend tout plus fluide.

---

# Si vous voulez, je peux vous montrer :

* Comment s'assurer que NanoGPT télécharge les jeux de données via votre proxy
* Comment mettre le jeu de données en cache localement pour éviter les téléchargements futurs
* Comment mettre en miroir les jeux de données Hugging Face localement en Chine (par exemple, la solution de contournement du miroir Tsinghua)

Dites-moi simplement ce dont vous avez besoin.