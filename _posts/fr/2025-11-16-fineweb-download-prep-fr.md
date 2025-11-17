---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Téléchargement et Préparation des Données FineWeb
translated: true
type: note
---

### Téléchargement du fichier Parquet

L'URL que vous avez fournie pointe vers un fichier Parquet spécifique de l'ensemble de données FineWeb (un sous-ensemble nettoyé des données CommonCrawl). Ce fichier (`000_00000.parquet` du dump `CC-MAIN-2013-20`) contient environ 1 million de lignes de texte web en anglais, chaque ligne incluant une colonne `text` déjà prétraitée pour l'entraînement de modèles de langage (HTML supprimé, dédupliqué, filtré par qualité via des outils comme Trafilatura).

Pour le télécharger :
- Utilisez la CLI Hugging Face : `huggingface-cli download HuggingFaceFW/fineweb data/CC-MAIN-2013-20/000_00000.parquet --local-dir ./fineweb_data`
- Ou via Python avec `huggingface_hub` :
  ```python
  from huggingface_hub import hf_hub_download

  file_path = hf_hub_download(
      repo_id="HuggingFaceFW/fineweb",
      filename="data/CC-MAIN-2013-20/000_00000.parquet",
      local_dir="./fineweb_data"
  )
  print(f"Downloaded to: {file_path}")
  ```
Ceci sauvegarde le fichier d'environ 500MB localement (par ex., `./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet`).

Pour le dump complet (des centaines de fichiers), utilisez `snapshot_download` comme indiqué dans la documentation du jeu de données, mais commencez par ce fichier unique pour les tests.

### Extraction du texte

La colonne `text` de FineWeb est du texte brut prêt pour l'entraînement—inutile de parser du HTML ou du HTML brut. Utilisez `pandas` ou `pyarrow` pour le charger efficacement. Voici comment :

1. **Installer les Dépendances** (si nécessaire) : `pip install pandas pyarrow datasets` (en supposant que vous les avez pour la configuration NanoGPT).

2. **Charger le Fichier Parquet et Extraire le Texte** :
   ```python
   import pandas as pd
   import os

   # Chemin vers votre fichier téléchargé
   parquet_path = "./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet"

   # Charger le fichier Parquet (efficace pour les gros fichiers)
   df = pd.read_parquet(parquet_path, columns=['text'])  # Ne charger que la colonne text pour économiser la mémoire

   # Extraire tout le texte dans une liste (ou itérer si la mémoire est limitée)
   texts = df['text'].tolist()  # Liste d'environ 1 million de chaînes de caractères

   # Optionnel : Nettoyage basique (FineWeb est déjà propre, mais normaliser les espaces)
   import re
   def clean_text(text):
       if pd.isna(text):  # Ignorer les valeurs nulles (rares dans FineWeb)
           return ''
       text = re.sub(r'\s+', ' ', text.strip())  # Réduire les espaces blancs
       return text if len(text) > 10 else ''  # Filtrer les textes très courts

   cleaned_texts = [clean_text(t) for t in texts if t]  # Appliquer le filtre

   print(f"Extracted {len(cleaned_texts)} text samples")
   print("Sample:", cleaned_texts[0][:200] + "...")  # Aperçu du premier texte
   ```

   - **Conseil Mémoire** : Ce fichier a environ 1 million de lignes, chaque texte fait environ 1 à 5k caractères. Sur une machine avec 16GB de RAM, il se charge bien. Pour des dumps plus gros, utilisez `pyarrow` pour une lecture par morceaux :
     ```python
     import pyarrow.parquet as pq

     table = pq.read_table(parquet_path, columns=['text'])
     texts = table['text'].to_pylist()
     ```

   - **Alternative en Flux** (pas besoin de téléchargement complet) : Utilisez la bibliothèque `datasets` pour itérer sans tout charger :
     ```python
     from datasets import load_dataset

     # Charger un dump spécifique en mode streaming
     dataset = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)

     texts = []
     for i, sample in enumerate(dataset):
         if i >= 100000:  # Limite pour les tests
             break
         texts.append(sample['text'])

     # Nettoyer comme ci-dessus
     ```

### Préparation pour l'entraînement NanoGPT

NanoGPT attend un seul fichier texte (par ex., `input.txt`) avec des documents concaténés séparés par un jeton spécial (comme `"<|endoftext|>"`). Voici comment formater le texte extrait :

```python
# Après avoir extrait cleaned_texts comme ci-dessus
with open('input.txt', 'w', encoding='utf-8') as f:
    for text in cleaned_texts:
        f.write(text + "\n<|endoftext|>\n")  # Séparateur par défaut de NanoGPT

print("Saved to input.txt – ready for NanoGPT!")
```

- **Pourquoi ce Format ?** Le script `data.py` de NanoGPT lira `input.txt`, l'encodera avec votre tokeniseur (par ex., GPT-2) et créera des jeux d'entraînement/validation. Chaque document se termine par `"<|endoftext|>"` pour éviter le mélange de contexte entre documents.
- **Personnalisation** :
  - Filtrer par longueur : Ajoutez `if 100 < len(text.split()) < 10000:` avant l'écriture pour ne conserver que les documents de taille moyenne.
  - Sous-ensemble pour les Tests : Utilisez `cleaned_texts[:10000]` pour une exécution rapide avec 10k échantillons.
  - Commande d'Entraînement : Une fois `input.txt` prêt, exécutez `python train.py` dans NanoGPT (ajustez `--dataset=input.txt` si nécessaire).

Ce fichier unique donne environ 5 à 10 milliards de jetons—parfait pour le fine-tuning. Pour plus, téléchargez des fichiers Parquet supplémentaires et concaténez-les. Si vous rencontrez des problèmes de mémoire ou avez besoin d'aide avec la configuration NanoGPT, partagez les détails !

**Référence** : [FineWeb Dataset Card](https://huggingface.co/datasets/HuggingFaceFW/fineweb)