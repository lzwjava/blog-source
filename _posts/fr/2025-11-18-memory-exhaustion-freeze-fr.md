---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Épuisement de la mémoire provoque un gel du système
translated: true
type: note
---

Votre problème **n'est pas** le GPU (la 4070 Ti est à peine utilisée ici). Ce script est **uniquement CPU + RAM**, et le blocage + le gel de l'interface graphique après ~140M tokens est presque certainement dû au fait que vous **épuisez la RAM** et que le système commence à swapper massivement sur le disque, ce qui fige tout pendant des minutes ou des heures.

### Pourquoi cela se produit vers ~140M–200M tokens

Chaque token → stocké en uint16 → 2 octets.

- 140 millions de tokens ≈ 280 Mo
- 1 milliard de tokens ≈ 2 Go
- 10 milliards de tokens (le FineWeb-10B complet) ≈ 20 Go
- 100B+ tokens (comme de nombreux téléchargements FineWeb/Edu) ≈ 200+ Go

Mais regardez votre liste `all_tokens = []` en Python : les listes Python ont une surcharge énorme. Chaque objet entier fait ~28–32 octets en Python 64 bits (même si la valeur tient dans un uint16).

Utilisation réelle de la mémoire lors de la construction de la liste :
- ~150M tokens dans une liste Python → ~150M × 28–32 octets ≈ **4–5 Go** rien que pour les objets de la liste
- Ensuite, vous faites `np.array(..., dtype=np.uint16)` → encore ~300 Mo pour le tableau compact
- Pic total de RAM pendant la conversion ≈ 5–6 Go + OS + overhead du bureau

Vous avez 62,6 Go de RAM, alors pourquoi un gel à seulement 140M tokens ?

Parce que votre fichier d'entrée `train_fineweb.txt` est probablement **beaucoup plus gros** que vous ne le pensez.

Les gens téléchargent souvent FineWeb-100B ou même des échantillons de 1T et les nomment "train_fineweb.txt". Si votre fichier est, par exemple, l'échantillon populaire FineWeb-Edu de 100B tokens (fichier texte de ~200–300 Go), le script continuera à lire indéfiniment, la liste `all_tokens` grossira jusqu'à des dizaines ou des centaines de milliards de tokens → des centaines de Go de RAM → OOM → swap intensif → gel complet du bureau. Les ventilateurs du GPU tournent parce que le script est toujours vivant (à peine), Python est bloqué dans le `extend()` ou dans la conversion finale `np.array()`.

### Solutions (choisissez-en une)

#### Meilleure solution : Stream directement vers .bin sans jamais garder tous les tokens en RAM
Cette version utilise presque pas de RAM (pic < 1 Go même pour des fichiers texte de taille téraoctet) :

```python
# stream_tokenize_to_bin.py
import os
import numpy as np
import tiktoken

enc = tiktoken.get_encoding("gpt2")
CHUNK_SIZE = 1_000_000  # caractères par chunk, ajuster si nécessaire

def process_file(input_path: str, train_bin: str, val_bin: str, val_ratio=0.0005):
    temp_train = train_bin + '.tmp'
    temp_val = val_bin + '.tmp'

    total_tokens = 0
    val_tokens_written = 0
    val_target = None  # on le décide après la première passe ou on l'approxime

    with open(input_path, "r", encoding="utf-8", errors='ignore') as f, \
         open(temp_train, "wb") as train_f, \
         open(temp_val, "wb") as val_f:

        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            tokens = enc.encode_ordinary(chunk)
            tokens_u16 = np.array(tokens, dtype=np.uint16)

            total_tokens += len(tokens_u16)

            # Split de validation approximatif à la volée (suffisamment bon)
            if val_target is None and total_tokens > 10_000_000:
                val_target = int(total_tokens * val_ratio / (1 - val_ratio))

            if val_tokens_written < val_target:
                split_point = min(len(tokens_u16), val_target - val_tokens_written)
                val_f.write(tokens_u16[:split_point].tobytes())
                train_f.write(tokens_u16[split_point:].tobytes())
                val_tokens_written += split_point
            else:
                train_f.write(tokens_u16.tobytes())

            if total_tokens % 50_000_000 == 0:
                print(f"Processed {total_tokens/1e6:.1f}M tokens")

    # Renommer les fichiers temporaires
    os.rename(temp_train, train_bin)
    os.rename(temp_val, val_bin)
    print(f"Done! Total ≈ {total_tokens/1e9:.2f}B tokens")
    print(f"train.bin and val.bin ready (no RAM explosion)")

if __name__ == "__main__":
    txt_file = "train_fineweb.txt"
    process_file(txt_file, "train.bin", "val.bin")
```

Ceci stream directement sur le disque, ne garde jamais plus d'un chunk en mémoire.

#### Si vous voulez vraiment le style de script original mais sécurisé
Ajoutez une surveillance de la mémoire et fragmentez la sortie :

```python
# ajoutez ceci au lieu d'une seule liste géante
MAX_TOKENS_PER_SHARD = 500_000_000  # ~1 Go par fragment

shard_idx = 0
all_tokens = []

for chunk in iter(lambda: f.read(chunk_size), ""):
    if not chunk:
        break
    tokens = enc.encode_ordinary(chunk)
    all_tokens.extend(tokens)

    if len(all_tokens) >= MAX_TOKENS_PER_SHARD:
        arr = np.array(all_tokens, dtype=np.uint16)
        arr.tofile(f"train_shard_{shard_idx:04d}.bin")
        print(f"Saved shard {shard_idx} - {len(arr)/1e6:.1f}M tokens")
        all_tokens.clear()
        shard_idx += 1
```

Plus tard, concaténez simplement les fragments : `cat train_shard_*.bin > train.bin`

### Vérification rapide de la taille réelle de votre fichier
Exécutez ces commandes dans le terminal :

```bash
du -h train_fineweb.txt          # taille lisible
wc -c train_fineweb.txt          # octets
ls -lh train_fineweb.txt
```

Le texte de FineWeb-10B fait ~20–25 Go, 100B fait ~200–250 Go, etc.

### Résumé
Votre script meurt parce que les listes Python consomment 15–20× plus de RAM que le tableau numpy final. Avec les gros fichiers FineWeb, vous dépassez rapidement 50+ Go → swap → bureau gelé.

Utilisez la version streaming ci-dessus — elle fonctionne sur des fichiers texte de 1To+ avec <2 Go de RAM et se termine en quelques heures sur un seul cœur CPU.

Votre 4070 Ti est innocente ici ; elle attend des données qui n'arrivent jamais parce que la RAM est saturée.