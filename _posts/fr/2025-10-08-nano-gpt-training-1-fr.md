---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Itérations d'entraînement par défaut de nanoGPT
translated: true
type: note
---

Dans la configuration par défaut de nanoGPT (par exemple, lors de l'entraînement sur le jeu de données de caractères de Shakespeare), le modèle s'exécute pour un total de **5000 itérations**.

Ceci est défini par `max_iters = 5000` dans le fichier `config/train_shakespeare_char.py`. Vous pouvez le remplacer via la ligne de commande avec `--max_iters=<valeur>` lors de l'exécution de `train.py`.

[config/train_shakespeare_char.py](https://huggingface.co/nindanaoto/nanoGPT-BitNet158b/blob/main/config/train_shakespeare_char.py)