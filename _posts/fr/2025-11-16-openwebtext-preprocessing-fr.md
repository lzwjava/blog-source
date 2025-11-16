---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Script de prétraitement du jeu de données OpenWebText
translated: true
type: note
---

### Aperçu
Ce script Python traite un gros fichier texte contenant le jeu de données OpenWebText (un corpus de texte extrait du web, similaire à ce qui est utilisé pour entraîner des modèles comme GPT-2). L'objectif est de :
- Diviser le texte brut en "documents" gérables (des morceaux de texte).
- Créer un objet `Dataset` Hugging Face pour une manipulation facile.
- Tokeniser le texte en utilisant le tokenizer GPT-2 Byte Pair Encoding (BPE) de TikToken (en ignorant les tokens spéciaux et en ajoutant un marqueur de fin de texte).
- Diviser le jeu de données en ensembles d'entraînement (99,95 %) et de validation (0,05 %).
- Sauvegarder les données tokenisées sous forme de fichiers binaires compacts (`train.bin` et `val.bin`) en utilisant les tableaux memory-mapped de NumPy. Ces fichiers stockent des séquences d'ID de tokens (sous forme d'entiers 16 bits) pour un chargement efficace pendant l'entraînement du modèle de machine learning.

Le script est conçu pour être efficace sur les systèmes multi-cœurs, en utilisant le multiprocessing pour la tokenisation. Il s'inspire d'un module de chargement de données du dépôt Flash Attention (lien dans le code), qui gère un prétraitement similaire pour l'entraînement de modèles de langage. Note : OpenWebText est très volumineux (~40 Go décompressé), mais ce script suppose un fichier local `openwebtext.txt` pré-téléchargé. Les fichiers de sortie sont beaucoup plus petits : `train.bin` ~17 Go (9B tokens) et `val.bin` ~8,5 Mo (4M tokens).

Le script affiche les paramètres de proxy au début (probablement pour déboguer les problèmes de réseau lors de téléchargements implicites, bien qu'aucun ne soit explicite ici). Il utilise 8 processus de travail pour la tokenisation par défaut.

### Détail étape par étape

#### 1. Imports et configuration initiale
```python
import os
import tarfile
from tqdm import tqdm
import numpy as np
import tiktoken
from huggingface_hub import hf_hub_download
from datasets import load_dataset # huggingface datasets
import datasets

print("HTTP_PROXY:", os.getenv("HTTP_PROXY"))
print("HTTPS_PROXY:", os.getenv("HTTPS_PROXY"))

# number of workers in .map() call
# good number to use is ~order number of cpu cores // 2
num_proc = 8

# number of workers in load_dataset() call
# best number might be different from num_proc above as it also depends on NW speed.
# it is better than 1 usually though
num_proc_load_dataset = num_proc

enc = tiktoken.get_encoding("gpt2")

datasets.logging.set_verbosity_info()
```
- **Objectif** : Importe les bibliothèques pour la gestion des fichiers (`os`, `tarfile`), les barres de progression (`tqdm`), les opérations numériques (`numpy`), la tokenisation (`tiktoken`) et les utilitaires Hugging Face (`huggingface_hub`, `datasets`).
- **Affichage des proxies** : Journalise les variables d'environnement pour les proxies HTTP/HTTPS, utile si le script rencontre des restrictions réseau (par exemple, pour télécharger les modèles de tokenisation, bien que TikToken gère cela en interne).
- **Travailleurs** : Définit `num_proc=8` pour le traitement parallèle lors de la tokenisation (environ la moitié des cœurs du CPU pour un équilibre). `num_proc_load_dataset` lui correspond mais n'est pas utilisé ici (vestige du code d'inspiration, qui charge depuis Hugging Face).
- **Encodeur** : Charge le tokenizer BPE de GPT-2 (`enc`). Celui-ci convertit le texte en ID de tokens entiers (plage 0–50 256).
- **Journalisation** : Définit le niveau de journalisation de Hugging Face datasets à "info" pour une sortie verbeuse pendant le traitement.

La garde `if __name__ == '__main__':` assure que la logique principale ne s'exécute que lorsque le script est exécuté directement (et non importé).

#### 2. Lecture et division du fichier texte
```python
if __name__ == '__main__':
    # Read the local openwebtext.txt file
    txt_file = os.path.join(os.path.dirname(__file__), 'openwebtext.txt')
    print(f"Reading from local file: {txt_file}")

    # Read the text content
    texts = []
    with open(txt_file, 'r', encoding='utf-8', errors='ignore') as f:
        # Read the entire file
        full_text = f.read().strip()

        # Try to split into documents by double newlines first
        documents = full_text.split('\n\n')

        # If we only got one document, split by single newlines
        if len(documents) <= 1:
            documents = full_text.split('\n')

        # If we still only have one document, split by period followed by space
        if len(documents) <= 1:
            # Split on period followed by space, then join back sentences
            sentences = full_text.split('. ')
            # Group sentences into chunks of ~100 sentences per document
            chunk_size = 100
            for i in range(0, len(sentences), chunk_size):
                chunk = '. '.join(sentences[i:i+chunk_size])
                if chunk.strip():
                    texts.append(chunk.strip() + '.')
        else:
            # Process documents from double/single newline splits
            for doc in documents:
                doc = doc.strip()
                if doc:  # Only add non-empty documents
                    texts.append(doc)

        print(f"Created {len(texts)} documents from the text file")
```
- **Lecture du fichier** : Ouvre `openwebtext.txt` (supposé être dans le même répertoire que le script) en mode UTF-8, en ignorant les erreurs d'encodage. Lit tout le contenu dans `full_text` et supprime les espaces blancs.
- **Logique de division** : Tente de diviser le texte en "documents" (morceaux logiques comme des paragraphes ou des articles) :
  - **Primaire** : Diviser par des doubles sauts de ligne (`\n\n`), courant pour séparer les documents dans les corpus.
  - **Solution de repli 1** : Si cela ne donne qu'un seul morceau (par exemple, pas de doubles sauts de ligne), diviser par des sauts de ligne simples (`\n`) pour un texte basé sur des lignes.
  - **Solution de repli 2** : Si on a toujours qu'un seul morceau (par exemple, un seul bloc de texte), diviser en phrases par `. ` (point + espace), puis regrouper toutes les 100 phrases dans un "document". Cela évite des entrées uniques trop longues. Ajoute un point à la fin de chaque morceau pour la complétude.
- **Sortie** : Stocke les documents non vides, nettoyés, dans la liste `texts`. Affiche le nombre total créé (par exemple, 10k exemples pour un sous-ensemble).
- **Pourquoi cette méthode ?** OpenWebText est une concaténation de pages web, donc la division crée des exemples d'entraînement qui ne sont pas de simples déversements bruts. Cela imite la façon dont les jeux de données comme BookCorpus sont traités.

#### 3. Création et division du jeu de données
```python
    # Create dataset from texts
    dataset = datasets.Dataset.from_dict({'text': texts})

    # create train/val split from the 10k examples
    split_dataset = dataset.train_test_split(test_size=0.0005, seed=2357, shuffle=True)
    split_dataset['val'] = split_dataset.pop('test') # rename the test split to val
```
- **Création du jeu de données** : Enveloppe la liste `texts` dans un `Dataset` Hugging Face avec une seule colonne `'text'`. Cela permet des opérations parallèles efficaces comme le mapping.
- **Division** : Utilise `train_test_split` pour diviser en ensembles d'entraînement (99,95 %) et de test (0,05 %). La petite taille de validation est intentionnelle pour les très gros jeux de données—suffisante pour l'évaluation sans gaspiller de calcul.
  - `test_size=0.0005` : 0,05 % pour la validation (par exemple, ~50 exemples sur 100k).
  - `seed=2357` : Graine aléatoire fixe pour la reproductibilité.
  - `shuffle=True` : Mélange avant la division.
- **Renommage** : Supprime `'test'` et le renomme en `'val'`. Maintenant, `split_dataset` est un dictionnaire avec les clés `'train'` et `'val'`, chacune étant un objet `Dataset`.

#### 4. Fonction de tokenisation
```python
    # we now want to tokenize the dataset. first define the encoding function (gpt2 bpe)
    def process(example):
        ids = enc.encode_ordinary(example['text']) # encode_ordinary ignores any special tokens
        ids.append(enc.eot_token) # add the end of text token, e.g. 50256 for gpt2 bpe
        # note: I think eot should be prepended not appended... hmm. it's called "eot" though...
        out = {'ids': ids, 'len': len(ids)}
        return out
```
- **Objectif** : Convertit le texte en ID de tokens pour l'entrée du modèle.
- **`encode_ordinary`** : Tokenise la chaîne de texte en une liste d'entiers (vocabulaire GPT-2). Ignore tous les tokens non standard dans le texte.
- **Ajouter EOT** : Ajoute le token de fin de texte (ID 50256 pour GPT-2) à la fin. Cela signale la limite de la séquence pendant l'entraînement. (Le commentaire note un débat potentiel entre l'ajout au début ou à la fin, mais l'ajout à la fin est courant dans les configurations de LM causales comme GPT.)
- **Sortie** : Retourne un dictionnaire avec `'ids'` (liste des ID de tokens) et `'len'` (longueur de la séquence, pour sommation ultérieure).

#### 5. Application de la tokenisation
```python
    # tokenize the dataset
    tokenized = split_dataset.map(
        process,
        remove_columns=['text'],
        desc="tokenizing the splits",
        num_proc=num_proc,
    )
```
- **Mapping** : Applique `process` à chaque exemple des jeux de données d'entraînement/validation en utilisant des travailleurs parallèles (`num_proc=8`).
- **`remove_columns=['text']`** : Supprime le texte original pour économiser la mémoire (nous n'avons besoin que des tokens maintenant).
- **Progression** : Affiche une barre de progression via `desc`. Cette étape peut prendre du temps pour les gros jeux de données en raison de l'encodage.

#### 6. Sauvegarde des données tokenisées dans des fichiers binaires
```python
    # concatenate all the ids in each dataset into one large file we can use for training
    for split, dset in tokenized.items():
        arr_len = np.sum(dset['len'], dtype=np.uint64)
        filename = os.path.join(os.path.dirname(__file__), f'{split}.bin')
        dtype = np.uint16 # (can do since enc.max_token_value == 50256 is < 2**16)
        arr = np.memmap(filename, dtype=dtype, mode='w+', shape=(arr_len,))

        # Use adaptive batch size based on dataset size
        total_batches = min(1024, len(dset))
        if total_batches < 1024:
            print(f"Using {total_batches} batches for {split} dataset (size: {len(dset)})")

        idx = 0
        for batch_idx in tqdm(range(total_batches), desc=f'writing {filename}'):
            # Only process if this batch index is valid for the dataset size
            if batch_idx < len(dset):
                # Batch together samples for faster write
                batch = dset.shard(num_shards=total_batches, index=batch_idx, contiguous=True).with_format('numpy')
                arr_batch = np.concatenate(batch['ids'])
                # Write into mmap
                arr[idx : idx + len(arr_batch)] = arr_batch
                idx += len(arr_batch)
        arr.flush()
```
- **Boucle sur les splits** : Pour `'train'` et `'val'`, calcule le nombre total de tokens (`arr_len`) en additionnant les champs `'len'`.
- **Tableau memory-mapped** : Crée un fichier memmap NumPy (`train.bin` ou `val.bin`) comme un tableau inscriptible d'entiers uint16 (correspond à la valeur maximale de token de GPT-2, 50 256 ; économise ~50 % d'espace par rapport à int32). La forme est 1D : `(total_tokens,)`.
- **Traitement par lots pour l'efficacité** : Divise le jeu de données en jusqu'à 1024 fragments (`total_batches`) pour éviter de tout charger en RAM à la fois. Pour les petits jeux de données (<1024 exemples), utilise le nombre exact.
  - **`shard`** : Divise le jeu de données en lots contigus (pas de mélange ici).
  - **`with_format('numpy')`** : Convertit le lot en tableaux NumPy pour une concaténation rapide.
- **Écriture** : Concatène les ID de tokens de chaque lot et les copie séquentiellement dans le tableau memmap en commençant à `idx`. Suit la progression avec `tqdm`.
- **`flush()`** : Assure que toutes les données sont écrites sur le disque.
- **Pourquoi binaire/memmap ?** Ces fichiers sont énormes mais peuvent être streamés. Pendant l'entraînement, vous pouvez les charger avec `np.memmap('train.bin', dtype=np.uint16, mode='r')` sans tout charger en mémoire.

#### 7. Commentaires sur la sortie et l'utilisation
```python
    # train.bin is ~17GB, val.bin ~8.5MB
    # train has ~9B tokens (9,035,582,198)
    # val has ~4M tokens (4,434,897)

    # to read the bin files later, e.g. with numpy:
    # m = np.memmap('train.bin', dtype=np.uint16, mode='r')
```
- Ce sont des exemples de tailles pour le OpenWebText complet (votre fichier local peut différer).
- **Astuce de lecture** : Utilisez memmap pour un accès en lecture seule. Dans les boucles d'entraînement, vous pouvez échantillonner des indices de départ aléatoires et lire des séquences de longueur fixe (par exemple, 1024 tokens) à partir du tableau plat.

### Problèmes potentiels et notes
- **Utilisation de la mémoire** : Lire le fichier `openwebtext.txt` complet en RAM pourrait échouer pour les très gros fichiers (40 Go+). Envisagez une lecture en streaming si nécessaire.
- **Placement de EOT** : Le commentaire remet en question l'ajout au début ou à la fin de EOT ; en pratique, l'ajout à la fin fonctionne pour les modèles autorégressifs (il marque la fin après le contenu).
- **Personnalisation** : Suppose un fichier local ; le code d'inspiration télécharge depuis Hugging Face, mais cette version lit localement (plus rapide, pas besoin d'authentification).
- **Dépendances** : Requiert `tiktoken`, `datasets`, `numpy`, `tqdm`. Installez-les via pip s'ils manquent.
- **Évolutivité** : Pour le vrai OpenWebText, exécutez sur une machine avec 64 Go+ de RAM et un stockage rapide (SSD). La division en 10k exemples suggère qu'il pourrait s'agir d'un sous-ensemble.

Ce script transforme le texte brut en un format prêt pour l'entraînement, optimisé pour les modèles de langage comme GPT. Si vous avez des questions sur sa modification (par exemple, tokenizer différent ou taille de morceau), faites-le moi savoir !