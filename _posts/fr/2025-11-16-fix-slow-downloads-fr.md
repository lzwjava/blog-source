---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Accélérer les Téléchargements Lents sur Hugging Face
translated: true
type: note
---

C'est un problème courant lors du téléchargement de gros jeux de données HF via un proxy. La combinaison de :

* De nombreux fichiers de plusieurs centaines de Mo
* Python `requests` / `huggingface_hub`
* Un proxy HTTP local (particulièrement Clash, V2Ray, ou tun2socks)

entraîne souvent un débit extrêmement lent ou des réinitialisations de connexion.

Voici les correctifs les plus utiles.

---

## 1. **Meilleure solution : Utiliser `hf_transfer`**

Hugging Face dispose d'un téléchargeur accéléré qui offre des vitesses **10 à 50 fois plus rapides** et une meilleure stabilité.

Installation :

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

Relancez votre commande.

Cela seul résout généralement les lenteurs de téléchargement via les proxys.

---

## 2. Utiliser `aria2c` avec l'interface en ligne de commande Hugging Face (le plus rapide pour les très gros fichiers)

Si vous téléchargez manuellement :

```bash
pip install huggingface_hub[cli]
sudo apt install aria2
```

Puis téléchargez :

```bash
huggingface-cli download --repo-type dataset openwebtext --local-dir ./openwebtext --local-dir-use-symlinks False
```

L'interface en ligne de commande HF utilise automatiquement aria2, qui gère :

* les connexions parallèles
* la reprise
* les proxys instables

beaucoup mieux que `requests`.

---

## 3. Correctif pour la lenteur des proxys locaux : utiliser SOCKS système au lieu de HTTP

Si vous utilisez quelque chose comme :

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

Passez à SOCKS5 si votre proxy le supporte :

```bash
export ALL_PROXY=socks5://127.0.0.1:7891
```

SOCKS est **beaucoup plus stable** pour le streaming de gros fichiers.

---

## 4. Désactiver le proxy pour les gros fichiers

Si votre réseau direct est correct mais que le proxy ralentit :

```bash
unset HTTP_PROXY
unset HTTPS_PROXY
unset ALL_PROXY
```

Puis réessayez. Certains serveurs HF sont rapides même sans proxy selon la région.

---

## 5. Utiliser un miroir HF (parfois lent en Chine continentale / Taïwan)

Vous pouvez forcer l'utilisation du CDN :

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

Puis relancez.
Cela améliore considérablement les vitesses pour certaines régions.

---

## 6. Reprendre les téléchargements interrompus

Les jeux de données HF sont mis en cache ici :

```
~/.cache/huggingface/datasets/
```

Si un fichier a été partiellement téléchargé, HF reprend automatiquement — pas besoin de recommencer depuis zéro.

---

## 7. Si c'est toujours lent : éviter le jeu de données complet, utiliser un petit extrait

OpenWebText fait plus de 40 Go.
Vous pouvez charger seulement une petite partie :

```python
from datasets import load_dataset
ds = load_dataset("openwebtext", split="train[:1%]")
```

---

## Recommandation rapide

Le plus rapide + le plus simple :

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
python data/openwebtext_10k/prepare.py
```

Vous devriez immédiatement voir la vitesse de téléchargement augmenter.

---

Si vous le souhaitez, je peux vous montrer comment modifier votre `prepare.py` pour utiliser un téléchargeur complètement personnalisé avec reprise/backoff et récupération parallèle, afin que votre pipeline télécharge toujours rapidement et ne se bloque jamais.