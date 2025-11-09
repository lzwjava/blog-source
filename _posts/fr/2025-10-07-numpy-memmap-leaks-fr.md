---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Correction des Fuites de Mémoire NumPy Memmap
translated: true
type: note
---

### Ce que dit le post Stack Overflow

Le post traite d'un problème courant avec `np.memmap` de NumPy lors du traitement de grands ensembles de données stockés sur le disque. La question initiale décrit l'itération sur une énorme matrice (par exemple, via des indices mélangés) pour lire les lignes par blocs, mais constate que l'utilisation de la RAM et de la mémoire virtuelle augmente régulièrement pendant le processus, ralentissant le système—même si chaque ligne n'est accédée qu'une seule fois. La personne qui pose la question souhaite limiter l'utilisation de la mémoire au bloc actuel et demande des alternatives comme une itération basée sur un générateur ou des E/S de fichier directes (en notant que cette dernière est plus lente).

La réponse liée (ID 61472122, acceptée) identifie la "fuite de mémoire" comme étant due au fait que le memmap de NumPy conserve le tableau entier en mémoire pour la mise en cache, malgré le mode lecture seule et l'accès en une seule passe. Elle propose deux solutions :

1.  **Recréer l'objet memmap par bloc** : Supprimer et réinitialiser `np.memmap` pour chaque lot ou bloc. Cela empêche le tableau complet de s'accumuler en RAM, maintenant une utilisation faible (liée à la taille du bloc). Il y a une surcharge CPU mineure due à la recréation, mais elle est négligeable. Exemple de code :
    ```python:disable-run
    def process_chunks(data_filename, chunk_size=4096):
        for start in range(0, total_size, chunk_size):
            # Recréer le memmap à chaque fois
            data = np.memmap(data_filename, dtype=np.float32, mode='r', shape=full_shape)
            # Traiter uniquement le bloc actuel
            chunk = data[start:start + chunk_size]
            # ... faire le travail ...
            del data  # Supprimer explicitement
    ```

2.  **mmap personnalisé avec conseil mémoire du système d'exploitation** : Accéder à l'objet `mmap` sous-jacent dans le memmap et utiliser `madvise` de Python 3.8+ (par exemple, `MADV_DONTNEED` ou `MADV_DONTDUMP`) pour indiquer au système d'exploitation de libérer les pages inutilisées. C'est plus bas niveau mais évite la surcharge de recréation. Cela inclut des extraits de code de la source de NumPy pour accéder au mmap.

La réponse recommande des outils de profilage comme `memory-profiler` pour vérifier les correctifs.

### Pourquoi NanoGPT utilise cette approche

Dans le code fourni de NanoGPT (une implémentation minimale de GPT pour l'entraînement de modèles de langage), la recréation de `np.memmap` à l'intérieur de la fonction `get_batch` suit exactement la première solution de cette réponse—pour contourner la fuite de mémoire lors de l'échantillonnage répété de lots à partir d'énormes fichiers binaires (par exemple, des données d'entraînement tokenisées).

NanoGPT s'entraîne sur de très grands ensembles de données (comme des milliards de tokens), donc charger le fichier complet en mémoire n'est pas réalisable. Au lieu de cela, il utilise memmap pour un accès disque efficace, mais sans recréation, la mémoire augmenterait sur plusieurs époques car NumPy mettrait en cache de plus en plus de fichiers. En remappant à nouveau à chaque lot (via les lignes `if split == 'train': data = np.memmap(...)`), il garantit une utilisation de la RAM faible et stable—essentielle pour les longues sessions d'entraînement sur du matériel limité comme un seul GPU. Le commentaire crédite explicitement le post SO pour cette astuce "d'évitement de fuite de mémoire". Cela garde le chargeur de données léger tout en permettant un échantillonnage aléatoire (`torch.randint`) pour les paires d'entrées/cibles x/y.

[Stack Overflow : utilisation mémoire numpy memmap - veut itérer une fois](https://stackoverflow.com/questions/45132940/numpy-memmap-memory-usage-want-to-iterate-once/61472122#61472122)