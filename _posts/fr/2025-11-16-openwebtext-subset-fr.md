---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Téléchargement d'une partie d'OpenWebText
translated: true
type: note
---

Ah, compris — vous souhaitez rester avec **Hugging Face CLI** mais ne récupérer qu'une petite partie. Le problème est le suivant : le CLI est conçu pour télécharger des **fichiers entiers**, pas des morceaux. OpenWebText est divisé en 21 fichiers sous-ensemble `.tar` ; si vous utilisez le CLI, il téléchargera des archives entières, donc vous ne pouvez pas obtenir exactement "1%" sans télécharger de gros morceaux.

Voici une approche pratique :

---

### 1. Télécharger seulement un sous-ensemble de fichiers

Au lieu des 21 fichiers complets, choisissez seulement quelques archives :

```bash
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset00.tar \
  --local-dir ./openwebtext
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset01.tar \
  --local-dir ./openwebtext
```

* Chaque archive fait ~625MB, donc si vous en téléchargez 1 ou 2, cela représente environ 1–2% du dataset.
* Vous pouvez ajuster les sous-ensembles que vous choisissez ; HF n'impose pas d'ordre séquentiel.

---

### 2. Extraire seulement ce dont vous avez besoin

Après le téléchargement :

```bash
cd ./openwebtext
tar -xvf urlsf_subset00.tar
tar -xvf urlsf_subset01.tar
```

Ensuite, vous pouvez traiter seulement quelques documents de ces sous-ensembles.

---

### 3. Optionnel : Combiner avec HF Transfer

Pour accélérer les téléchargements via le CLI :

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

Puis réessayez les commandes CLI — les téléchargements seront beaucoup plus rapides.

---

Si vous voulez, je peux créer un **petit snippet de commande qui sélectionne automatiquement ~1% d'OpenWebText en utilisant uniquement le CLI**, afin que vous n'ayez pas à choisir manuellement les archives. Voulez-vous que je fasse cela ?