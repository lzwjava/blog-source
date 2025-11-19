---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Correction du tueur OOM dans le script FineWeb
translated: true
type: note
---

Le message "Killed" sans aucune traceback Python signifie que le tueur OOM (Out-of-Memory) de Linux a terminé le processus. Cela se produit dans le script `data/fineweb/prepare.py` car il essaie de charger l'intégralité de votre fichier texte concaténé d'environ 15 Go (`train_fineweb.txt`) dans la RAM en une seule fois avec quelque chose comme `open(...).read()` avant le tokenisation.

Même si FineWeb-Edu est conçu pour le streaming (le téléchargeur officiel utilise Hugging Face `datasets` et traite les fragments un par un en morceaux d'environ 100M de tokens sans jamais tout charger en mémoire), le dossier nanoGPT fineweb a un chemin de fichier local personnalisé qui n'est pas efficace en mémoire pour les gros fichiers.

### Correctifs rapides (choisissez-en un)

1. **Meilleure et recommandée : Utiliser le téléchargeur officiel en streaming de FineWeb-Edu au lieu de vos fichiers locaux**  
   N'utilisez pas du tout le `data/fineweb/prepare.py` de nanoGPT.  
   Utilisez le script plus récent de Karpathy fait exactement pour FineWeb-Edu 10B tokens (ou plus) :

   ```bash
   # Depuis la racine de nanoGPT (ou n'importe où)
   wget https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py
   python fineweb.py
   ```

   Cela télécharge et tokenise l'échantillon FineWeb-Edu sample-10BT (10 milliards de tokens, ~15-20 GB brut) en mode streaming en utilisant `datasets.load_dataset(..., streaming=True)` et le multiprocessing. Il ne charge jamais l'intégralité du jeu de données dans la RAM et produit exactement les mêmes fragments `.bin` que nanoGPT attend dans un dossier comme `edu_fineweb10B/`.  
   Il fonctionne bien sur des machines avec 32-64 GB de RAM (ou même moins si vous réduisez `num_proc_load_dataset` et `num_proc` dans le script).

   Pour les versions complètes 100B ou 1T, changez simplement `remote_name = "sample-10BT"` en `"100BT"` ou ce dont vous avez besoin.

2. **Si vous voulez vraiment conserver votre fichier local de 10 parquet → txt**  
   Modifiez `data/fineweb/prepare.py` pour traiter le texte par morceaux au lieu de tout charger :

   Ouvrez le script et remplacez le gros bloc `with open(local_file, 'r', encoding='utf-8') as f: data = f.read()` par quelque chose comme ceci :

   ```python
   from tqdm import tqdm
   import tiktoken
   enc = tiktoken.get_encoding("gpt2")

   chunk_size = 1_000_000  # caractères par morceau, ajustez si nécessaire
   tokens = []
   with open(local_file, "r", encoding="utf-8") as f:
       while True:
           chunk = f.read(chunk_size)
           if not chunk:
               break
           tokens.extend(enc.encode_ordinary(chunk))  # ou enc.encode(chunk)
           print(f"Tokenized so far: {len(tokens)/1e6:.1f}M tokens")
   tokens = np.array(tokens, dtype=np.uint16)
   ```

   Cela maintient la mémoire RAM maximale en dessous de ~10-15 GB même pour votre fichier de 15 GB.

3. **Solutions matérielles (temporaires, pas idéales)**  
   - Ajoutez beaucoup de swap (par exemple, un fichier d'échange de 64-128 GB). Ce sera extrêmement lent une fois qu'il commencera à swapper, mais cela peut finir.  
     ```bash
     sudo fallocate -l 64G /swapfile
     sudo chmod 600 /swapfile
     sudo mkswap /swapfile
     sudo swapon /swapfile
     ```
   - Exécutez sur une machine/instance avec ≥64 GB de RAM (par exemple, AWS r6i.4xlarge ou plus gros).

### Résumé
Exécutez simplement le `fineweb.py` officiel de build-nanogpt — c'est la solution la plus propre et celle que tout le monde utilise pour FineWeb maintenant. Votre fichier txt concaténé de 15 GB est le problème, pas FineWeb lui-même.

[Téléchargeur officiel de FineWeb-Edu](https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py)  
[Page du jeu de données FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)