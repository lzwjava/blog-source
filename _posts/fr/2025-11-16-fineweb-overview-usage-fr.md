---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Aperçu et Utilisation du Jeu de Données FineWeb
translated: true
type: note
---

### Présentation du jeu de données FineWeb
Le jeu de données FineWeb est un corpus de texte web anglais à grande échelle et de haute qualité, développé par Hugging Face, dérivé d'instantanés CommonCrawl (2013–2024). Il contient plus de 15 000 milliards de tokens après filtrage et déduplication, ce qui le rend adapté pour le pré-entraînement de grands modèles de langage (LLM). Il est publié sous la licence Open Data Commons Attribution (ODC-By) et hébergé sur Hugging Face Datasets.

Il existe des variantes comme FineWeb-Edu (filtré pour le contenu éducatif) et FineWeb2 (extension multilingue). Pour l'entraînement de LLM, le cœur `HuggingFaceFW/fineweb` est le point de départ.

### Prérequis
- **Environnement Python** : Python 3.8+ avec la bibliothèque `datasets` de Hugging Face.
- **Stockage** : Le jeu de données complet est très volumineux (~16 To compressé). Utilisez le mode streaming pour un traitement à la volée pendant l'entraînement.
- **Optionnel pour la vitesse** : Installez `huggingface_hub` avec le support HF Transfer :  
  ```
  pip install huggingface_hub[hf_transfer]
  ```
  Puis définissez la variable d'environnement :  
  ```
  export HF_HUB_ENABLE_HF_TRANSFER=1
  ```
- **Compte Hugging Face** : Optionnel mais recommandé pour un accès contrôlé ou des téléchargements plus rapides (créez un compte gratuit et connectez-vous via `huggingface-cli login`).

### Comment charger le jeu de données
Utilisez la bibliothèque `datasets` pour y accéder directement. Voici un guide étape par étape avec des exemples de code.

#### 1. Installer les dépendances
```bash
pip install datasets
```

#### 2. Charger le jeu de données complet (Mode Streaming pour l'Entraînement)
Le mode streaming évite de télécharger l'intégralité du jeu de données à l'avance—idéal pour un entraînement avec un stockage limité. Il fournit les données par lots.

```python
from datasets import load_dataset

# Charger l'intégralité du jeu de données FineWeb en mode streaming
dataset = load_dataset("HuggingFaceFW/fineweb", split="train", streaming=True)

# Exemple : Itérer sur les premiers exemples
for example in dataset.take(5):
    print(example)  # Chaque exemple a des champs comme 'text', 'url', 'date', etc.
```

- **Splits** : Principalement `train` (toutes les données). Les extraits CommonCrawl individuels sont disponibles en tant que configurations, comme `CC-MAIN-2015-11` (chargez via `load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2015-11", split="train")`).
- **Format des données** : Fichiers Parquet avec des colonnes incluant `text` (contenu nettoyé), `url`, `date`, `quality_score`, etc. Le texte est prêt pour la tokenisation.

#### 3. Charger un sous-ensemble ou une configuration spécifique
Pour des tests ou un entraînement à plus petite échelle :
```python
# Charger un extrait CommonCrawl spécifique (par exemple, les données de 2023)
dataset = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2023-50", split="train")

# Ou charger le sous-ensemble éducatif (FineWeb-Edu, ~0,5 T tokens)
edu_dataset = load_dataset("HuggingFaceFW/fineweb-edu", split="train", streaming=True)
```

#### 4. Intégrer avec les pipelines d'entraînement
Pour l'entraînement de LLM (par exemple, avec Transformers ou des boucles personnalisées), utilisez l'itérateur streaming directement dans votre chargeur de données :
```python
from transformers import DataCollatorForLanguageModeling, Trainer, TrainingArguments

# En supposant que vous ayez un tokenizer et un modèle
tokenizer = ...  # par exemple, AutoTokenizer.from_pretrained("gpt2")

def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, max_length=512)

# Tokeniser à la volée (dans une fonction map avec batched=True pour l'efficacité)
tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=dataset.column_names)

# Procéder au Trainer ou à la boucle personnalisée
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
# ... (configurer le Trainer avec tokenized_dataset)
```

- **Conseil d'efficacité** : Traitez par lots avec `batched=True` dans `.map()`. Pour l'entraînement distribué, utilisez Hugging Face Accelerate.

#### 5. Télécharger le jeu de données complet (Mode Non-Streaming)
Si vous avez besoin d'un stockage local (non recommandé pour la taille complète) :
```python
dataset = load_dataset("HuggingFaceFW/fineweb", split="train")  # Télécharge vers ~/.cache/huggingface/datasets
```
Utilisez `dataset.save_to_disk("/chemin/vers/sauvegarde")` ensuite.

### Conseils supplémentaires pour l'entraînement
- **Déduplication** : FineWeb est déjà dédupliqué, mais vérifiez les métadonnées comme `minhash_cluster_size` pour un suréchantillonnage si nécessaire.
- **Filtrage de qualité** : Utilisez le `quality_score` intégré (seuil >0,5) pour sous-échantillonner les échantillons de haute qualité.
- **Variantes** :
  - **FineWeb-Edu** : Pour un entraînement axé sur le contenu éducatif. Chargez comme ci-dessus.
  - **FineWeb2** : Pour des données multilingues (1000+ langues). Chargez via `load_dataset("HuggingFaceFW/fineweb-2", name="eng_Latn", split="train", streaming=True)`.
- **Évaluation** : Hugging Face fournit des modèles d'ablation et des benchmarks ; entraînez de petits modèles (par exemple, 1,8B paramètres) sur des sous-ensembles pour comparer.
- **Ressources** : Tous les détails dans l'[article de recherche](https://arxiv.org/abs/2402.06645). Le code pour le filtrage personnalisé est sur [GitHub](https://github.com/huggingface/fineweb).

Pour les problèmes, consultez la [documentation Hugging Face Datasets](https://huggingface.co/docs/datasets/loading). Si vous utilisez un framework spécifique (par exemple, PyTorch Lightning), adaptez l'itérateur en conséquence.