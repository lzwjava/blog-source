---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Entraînement de jeux de données personnalisés avec nanoGPT
translated: true
type: note
---

### Préparation et entraînement d’un jeu de données texte personnalisé avec nanoGPT

nanoGPT est conçu pour faciliter l’entraînement sur des données texte, y compris des jeux de données personnalisés. Le processus consiste à préparer votre texte sous forme de fichiers binaires de tokens, à configurer les paramètres d’entraînement et à exécuter le script d’entraînement. Je vais décrire les étapes en m’appuyant sur les exemples du dépôt (par exemple, Shakespeare ou OpenWebText). Vous aurez besoin de Python 3.8+ et d’un GPU pour un entraînement efficace (le CPU fonctionne, mais est plus lent).

#### 1. Installer les dépendances
Tout d’abord, configurez l’environnement :
```
pip install torch numpy transformers datasets tiktoken wandb tqdm
```
- `torch` : pour PyTorch (installez avec CUDA si vous utilisez un GPU : par exemple, `pip install torch --index-url https://download.pytorch.org/whl/cu118`).
- Les autres gèrent la tokenisation, le chargement des données et la journalisation.

#### 2. Préparer votre jeu de données personnalisé
nanoGPT attend vos données sous forme de fichiers binaires (`train.bin` et `val.bin`) contenant des entiers tokenisés. Vous devrez écrire un script de préparation simple pour traiter votre texte brut.

- **Placer votre fichier texte** : placez votre texte brut (par exemple, `input.txt`) dans un nouveau dossier sous `data/`, comme `data/my_dataset/`.
  
- **Créer un script de préparation** : copiez et adaptez un exemple du dépôt (par exemple, `data/shakespeare_char/prepare.py` pour le niveau caractère ou `data/openwebtext/prepare.py` pour le niveau token BPE de GPT-2).
  
  **Exemple pour une tokenisation au niveau caractère** (simple pour les petits jeux de données ; traite chaque caractère comme un token) :
  ```python
  # Enregistrez sous data/my_dataset/prepare.py
  import os
  import requests
  import numpy as np
  from torch.utils.data import Dataset, random_split

  # Chargez votre texte (remplacez par le chemin de votre fichier)
  with open('data/my_dataset/input.txt', 'r', encoding='utf-8') as f:
      text = f.read()

  # Encodez en caractères
  chars = sorted(list(set(text)))
  vocab_size = len(chars)
  stoi = {ch: i for i, ch in enumerate(chars)}
  itos = {i: ch for i, ch in enumerate(chars)}
  def encode(s): return [stoi[c] for c in s]
  def decode(l): return ''.join([itos[i] for i in l])

  # Tokenisez l’intégralité du texte
  data = torch.tensor(encode(text), dtype=torch.long)

  # Divisez en train/val (90/10)
  n = int(0.9 * len(data))
  train_data = data[:n]
  val_data = data[n:]

  # Enregistrez en fichiers .bin
  train_data = train_data.numpy()
  val_data = val_data.numpy()
  train_data.tofile('data/my_dataset/train.bin')
  val_data.tofile('data/my_dataset/val.bin')

  # Affichez les statistiques
  print(f"Longueur du jeu de données en caractères : {len(data)}")
  print(f"Taille du vocabulaire : {vocab_size}")
  ```
  Exécutez-le :
  ```
  python data/my_dataset/prepare.py
  ```
  Cela crée `train.bin` et `val.bin`.

- **Pour la tokenisation BPE de GPT-2** (mieux pour les jeux de données plus volumineux ; utilise des sous-mots) :
  Adaptez `data/openwebtext/prepare.py`. Vous devrez installer `tiktoken` (déjà dans les dépendances) et traiter votre texte de manière similaire, mais utilisez `tiktoken.get_encoding("gpt2").encode()` au lieu de l’encodage caractère. Divisez votre texte en morceaux train/val (par exemple, 90/10), puis enregistrez-les sous forme de tableaux NumPy dans `.bin`.

- **Conseils** :
  - Gardez votre jeu de données propre (par exemple, supprimez les caractères spéciaux si nécessaire).
  - Pour les fichiers très volumineux, traitez-les par blocs pour éviter les problèmes de mémoire.
  - Taille du vocabulaire : ~65 pour les caractères (Shakespeare) ; ~50k pour BPE.

#### 3. Configurer l’entraînement
Créez un fichier de configuration en copiant un exemple (par exemple, `config/train_shakespeare_char.py`) vers `config/train_my_dataset.py` et modifiez-le.

Paramètres clés à ajuster :
```python
# Extrait de configuration exemple
out_dir = 'out-my_dataset'  # Dossier de sortie pour les points de contrôle
dataset = 'my_dataset'      # Correspond au nom de votre dossier de données
batch_size = 64             # Ajustez en fonction de la mémoire GPU (par exemple, 12 pour un petit GPU)
block_size = 256            # Longueur de contexte (tokens par exemple)
n_layer = 6                 # Couches du Transformer
n_head = 6                  # Têtes d’attention
n_embd = 384                # Dimension d’embedding
max_iters = 5000            # Étapes d’entraînement
lr = 6e-4                   # Taux d’apprentissage
dropout = 0.2               # Taux de dropout
init_from = 'scratch'       # 'scratch' pour un nouveau modèle ; 'gpt2' pour charger un modèle pré-entraîné
```
- Pour le fine-tuning (démarrer à partir de GPT-2 pré-entraîné) : définissez `init_from = 'gpt2'` (ou 'gpt2-medium').
- Pour Apple Silicon : ajoutez `device = 'mps'`.
- Les points de contrôle sont enregistrés toutes les 500 itérations par défaut.

#### 4. Lancer l’entraînement
Entraînez à partir de zéro ou effectuez un fine-tuning :
```
python train.py config/train_my_dataset.py
```
- Pour multi-GPU (par exemple, 8 GPU) : `torchrun --standalone --nproc_per_node=8 train.py config/train_my_dataset.py`.
- Surveillez avec WandB (journalise les pertes, les échantillons ; activez dans la configuration avec `wandb_log = True`).
- Temps d’entraînement : quelques minutes pour les petits modèles sur GPU ; plusieurs heures/jours pour les plus grands.

#### 5. Générer des échantillons (tester le modèle)
Après l’entraînement, échantillonnez du texte :
```
python sample.py --out_dir=out-my_dataset --start="Votre amorce ici"
```
Cela charge le dernier point de contrôle et génère.

#### Problèmes courants
- **Erreurs de mémoire** : réduisez `batch_size` ou `block_size`.
- **Pas de GPU** : ajoutez `--device=cpu --compile=False` aux commandes.
- **Jeux de données volumineux** : utilisez l’entraînement distribué pour la mise à l’échelle.

Pour plus de détails, consultez le README du dépôt et les exemples de données/config.

[nanoGPT GitHub](https://github.com/karpathy/nanoGPT)