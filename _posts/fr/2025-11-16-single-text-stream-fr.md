---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Entraînement sur un flux de texte concaténé unique
translated: true
type: note
---

Dans nanoGPT (et essentiellement dans tout entraînement de type GPT, y compris l'entraînement original de GPT-2/GPT-3), **vous devez entraîner le modèle sur un seul et gigantesque flux de texte concaténé**, et non sur des articles/documents individuels fournis un par un comme des séquences séparées.

Voici pourquoi et comment cela est fait en pratique avec FineWeb (et dans le code de nanoGPT d'Andrej) :

### Ce que vous devriez faire (la bonne méthode)
1. Concaténez **tous** les articles individuels en **un seul énorme fichier .txt** (ou plusieurs fichiers fragmentés volumineux), séparés uniquement par un jeton de fin de texte spécial `<|endoftext|>` (ou le séparateur de votre choix).
2. Pendant l'entraînement, nanoGPT va :
   - Charger l'intégralité du texte concaténé dans un énorme tableau de tokens.
   - Le diviser en blocs de longueur fixe (par exemple, block_size = 1024 tokens).
   - Ces blocs traversent très fréquemment les limites des documents — ce n'est pas seulement acceptable, c'est même souhaitable.

C'est exactement ainsi qu'OpenAI a entraîné GPT-2 et GPT-3, et c'est ce que fait Andrej avec Shakespeare, OpenWebText, FineWeb-Edu, etc.

### Ce que fait le script extract_fineweb.py
Le script que vous avez exécuté fait déjà la bonne chose :

```bash
$ python ./scripts/train/extract_fineweb.py
```

Il lit tous les fichiers parquet, extrait uniquement la colonne `text` de chaque ligne (c'est-à-dire chaque page web/article), écrit le texte brut les uns à la suite des autres dans `fineweb_extracted.txt`, et (dans les versions les plus récentes) insère automatiquement le séparateur `<|endoftext|>` entre les documents.

Ainsi, le fichier résultant ressemble à :

```
<texte de l'article 1> <|endoftext|> <texte de l'article 2> <|endoftext|> <texte de l'article 3> <|endoftext|> ...
```

C'est parfait. Vous devriez entraîner le modèle sur ce seul fichier géant (ou sur les fichiers binaires fragmentés que `train.py` créera à partir de celui-ci).

### Ce que vous ne devriez PAS faire
- Ne **pas** fournir chaque article comme un exemple/séquence séparé au modèle et réinitialiser l'attention pour chaque article.
- Ne **pas** tronquer ou compléter (padding) chaque article pour qu'il fasse exactement block_size et n'entraîner le modèle qu'à l'intérieur d'un seul document.
- Ne **pas** utiliser de traitement par lots au niveau du document (Document-level batching) où chaque séquence dans le lot est un document complet.

Cela détruirait la capacité du modèle à apprendre des dépendances à long terme qui s'étendent sur plusieurs documents et nuirait considérablement à ses performances.

### Résumé
Oui → Entraînez sur **un seul et massif fichier de texte concaténé** (exactement ce que produit `extract_fineweb.py`).  
Non → N'entraînez **pas** article par article comme des séquences séparées.

C'est ainsi que les GPT ont toujours été entraînés, et c'est la raison pour laquelle `train.py` de nanoGPT traite simplement les données comme un long flux de tokens.

Alors continuez simplement avec le processus normal de nanoGPT :

```bash
python scripts/train/extract_fineweb.py   # vous avez déjà fait cela
python train.py --dataset=your_extracted_file_or_fineweb10B etc.
```

Vous êtes sur la bonne voie !