---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Téléchargement de Fichiers Parquet Spécifiques de FineWeb
translated: true
type: note
---

Vous voulez simplement télécharger et utiliser quelques fichiers parquet d'un dump Common Crawl spécifique (comme CC-MAIN-2013-20) au lieu du monstre complet de 15 000 milliards de tokens de FineWeb — c'est totalement raisonnable ! Voici les méthodes les plus simples pour le faire en 2025.

### Méthode 1 : Téléchargement direct avec huggingface_hub (Recommandée, la plus rapide)
Cela télécharge uniquement les fichiers parquet que vous voulez à pleine vitesse (~ Go/s si vous activez hf-transfer).

```bash
# 1. Installer/mettre à niveau
pip install -U "huggingface_hub[hf_transfer]"

# 2. Activer le téléchargement rapide (très important !)
export HF_HUB_ENABLE_HF_TRANSFER=1   # Linux/macOS
# ou sur Windows PowerShell :
# $env:HF_HUB_ENABLE_HF_TRANSFER = "1"

# 3. Télécharger uniquement les quelques fichiers parquet souhaités
huggingface-cli download HuggingFaceFW/fineweb \
    data/CC-MAIN-2013-20/000_00000.parquet \
    data/CC-MAIN-2013-20/000_00001.parquet \
    data/CC-MAIN-2013-20/000_00002.parquet \
    --repo-type dataset --local-dir fineweb-2013-20
```

Et voilà — vous avez maintenant trois fichiers parquet de ~2,15 Go dans le dossier `fineweb-2013-20/`.

### Méthode 2 : Script Python en une ligne pour télécharger des fichiers spécifiques
```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="HuggingFaceFW/fineweb",
    repo_type="dataset",
    allow_patterns=[
        "data/CC-MAIN-2013-20/000_00000.parquet",
        "data/CC-MAIN-2013-20/000_00001.parquet",
        # ajoutez-en d'autres si vous le souhaitez
    ],
    local_dir="fineweb-2013-20"
)
```

### Comment lire les fichiers Parquet localement
```python
import pandas as pd
# ou utilisez pyarrow pour la vitesse + moins de mémoire
import pyarrow.parquet as pq
import pyarrow.dataset as ds

# Méthode la plus rapide (flux sans tout charger en RAM)
dataset = ds.dataset("fineweb-2013-20/data/CC-MAIN-2013-20/", format="parquet")

for batch in dataset.to_batches(batch_size=1024):
    df = batch.to_pandas()
    for text in df["text"]:
        # faites ce que vous voulez : tokeniser, filtrer, écrire en jsonl, etc.
        print(text[:200])  # exemple
```

Ou simplement avec pandas (acceptable pour quelques fichiers) :
```python
df = pd.read_parquet("fineweb-2013-20/data/CC-MAIN-2013-20/000_00000.parquet")
print(df.columns)  # ['text', 'id', 'dump', 'url', 'date', 'file_path', 'language', 'language_score', 'token_count']
print(df.iloc[0]["text"])
```

### Statistiques rapides pour CC-MAIN-2013-20
- ~207 fichiers parquet × ~2,15 Go ≈ 422 Go au total
- ~44 milliards de tokens (bonne taille pour des expériences petites à moyennes)
- Déjà nettoyés, dédupliqués et filtrés par Hugging Face

C'est tout ce dont vous avez besoin. Choisissez simplement le nombre de fichiers `_0000XX.parquet` que vous voulez (ils sont mélangés), téléchargez uniquement ceux-là, et commencez l'entraînement ou le filtrage immédiatement.