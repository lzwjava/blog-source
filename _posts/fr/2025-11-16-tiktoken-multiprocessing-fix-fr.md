---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Correction de l'Erreur de Pickle avec le Multiprocessing de Tiktoken
translated: true
type: note
---

Votre erreur est très courante lors de l'utilisation de `datasets.map(..., num_proc>1)` avec un tokeniseur personnalisé (comme l'encodeur Tiktoken utilisé dans le script FineWeb de nanoGPT) — le tokeniseur charge le fichier BPE (`cl100k_base.tiktoken` ou similaire) et ce gestionnaire de fichier **ne peut pas être sérialisé (pickled)** lorsqu'il est envoyé aux sous-processus sur Linux (multiprocessing basé sur le fork).

Les processus enfants plantent immédiatement → "One of the subprocesses has abruptly died".

### Correction Rapide (fonctionne 99% du temps)

Modifiez `data/fineweb/prepare.py` et forcez la tokenisation à s'exécuter **uniquement dans le processus principal** :

```python
# Autour de la ligne 80-85, trouvez l'appel .map() et changez num_proc=8 → num_proc=1

tokenized = raw_datasets.map(
    tokenize,
    num_proc=1,               # ← changez cette ligne (ou supprimez simplement l'argument)
    desc="tokenizing the splits",
)
```

Ce sera plus lent (mono-cœur), mais cela fonctionnera de manière fiable. Sur FineWeb-10B, cela prend ~30-60 minutes selon votre CPU/disque.

### Meilleure Correction (conservez le multiprocessing, toujours rapide)

Faites en sorte que le tokeniseur se charge paresseusement à l'intérieur du processus worker au lieu de le faire dans la portée globale.

Remplacez la création actuelle du tokeniseur (autour de la ligne 40-50) par ce modèle :

```python
import tiktoken

# Supprimez le global encoder = tiktoken.get_encoding("cl100k_base")

def get_encoder():
    """Charge le tokeniseur paresseusement dans chaque sous-processus"""
    return tiktoken.get_encoding("cl100k_base")

def tokenize(example):
    enc = get_encoder()                                   # ← chargé par processus
    ids = enc.encode_ordinary(example["text"])
    ids.append(enc.eot_token)  # ou ce que fait le script
    return {"ids": ids, "len": len(ids)}
```

Puis gardez `num_proc=8` (ou n'importe quel nombre). De cette façon, chaque worker charge sa propre copie du fichier .tiktoken après le fork → pas de problèmes de sérialisation.

### Alternative Encore Plus Rapide (recommandée pour des exécutions répétées)

Pré-téléchargez les fragments (shards) FineWeb-Edu 10B/100B depuis Hugging Face et utilisez le script mis à jour de Karpathy qui fonctionne directement sur les fichiers parquet/arrow au lieu du fichier .txt géant :

```bash
# Beaucoup plus rapide et évite complètement ce bug
python data/fineweb/prepare_fineweb.py --version 10B
# ou 100B
```

Le nouveau script (ajouté ~2024) utilise le dataset HF officiel et est sûr pour le multiprocessing.

### Résumé

| Solution                          | Vitesse  | Complexité | Recommandation |
|-----------------------------------|----------|------------|----------------|
| `num_proc=1`                      | Lente    | 1 ligne    | Correction rapide |
| Encoder paresseux dans tokenize() | Rapide   | petite modification | Meilleur pour .txt |
| Utiliser le nouveau script prepare_fineweb.py | La plus rapide | nouvelle commande | Recommandé |

Choisissez une solution et vous surmonterez cette erreur immédiatement. Dites-moi quelle voie vous prenez et je vous donnerai le correctif exact si nécessaire !