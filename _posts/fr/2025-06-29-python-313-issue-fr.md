---
audio: false
generated: true
lang: fr
layout: post
title: Erreur CuPy avec Python 3.13
translated: true
type: note
---

### Description du problème

Vous rencontrez une `AttributeError` lors de l'exécution d'un script Python qui importe la bibliothèque CuPy pour des calculs GPU. L'erreur se produit lors de l'instruction `import cupy as cp`, empêchant l'exécution du script. La traceback pointe vers un problème dans le code interne de CuPy, spécifiquement dans `cupy/cuda/device.pyx` à la ligne 105, où un décorateur `memoize` tente de modifier l'attribut `__name__` d'une fonction ou méthode intégrée. Le message d'erreur est :

```
AttributeError: attribute '__name__' of 'builtin_function_or_method' objects is not writable
```

Ce problème semble être lié à votre utilisation de Python 3.13, qui peut introduire des problèmes de compatibilité avec la version de CuPy que vous avez installée.

### Cause de l'erreur

L'erreur se produit parce que :

- **Le décorateur `memoize` de CuPy** : CuPy utilise un décorateur `memoize` pour mettre en cache les résultats des fonctions afin d'optimiser les performances. Ce décorateur s'appuie sur `functools.update_wrapper` de Python pour copier les attributs (comme `__name__`) de la fonction originale vers la fonction wrapper.
- **Fonctions intégrées** : En Python, les fonctions intégrées (implémentées en C) ont un attribut `__name__` en lecture seule. Lorsque `update_wrapper` tente de définir cet attribut, il échoue avec une `AttributeError`.
- **Compatibilité Python 3.13** : La fonction spécifique étant mémorisée dans `device.pyx` de CuPy est probablement une fonction intégrée, et Python 3.13 peut appliquer des règles plus strictes ou gérer les fonctions intégrées différemment des versions précédentes, exposant ainsi ce problème.

Comme l'erreur se produit lors de l'importation de CuPy, il s'agit d'un problème systémique lié à l'initialisation de la bibliothèque plutôt qu'à la logique de votre script.

### Solution recommandée

Le correctif le plus simple et le plus pratique consiste à exécuter votre script avec une version antérieure de Python où CuPy est connu pour être compatible, telle que Python 3.11 ou 3.12. Cela évite le problème de compatibilité avec Python 3.13 sans nécessiter de modifications du code source de CuPy ou des solutions de contournement complexes.

#### Pourquoi cela fonctionne

- **Compatibilité** : Les versions de CuPy jusqu'aux dernières versions (par exemple, v11) sont testées et prises en charge sur des versions de Python comme 3.11 et 3.12, où cette erreur spécifique ne se produit pas.
- **Aucune modification de code** : Votre script, qui benchmark le tri GPU avec CuPy, peut s'exécuter tel quel dans un environnement Python antérieur, garantissant l'intégrité du benchmark.
- **Facilité de mise en œuvre** : Changer de version de Python est simple en utilisant des environnements virtuels ou des outils comme `conda`.

### Correctif étape par étape

Voici comment résoudre le problème :

#### Option 1 : Utilisation de `virtualenv`

1. **Installer Python 3.11 ou 3.12**
   - Assurez-vous que Python 3.11 ou 3.12 est installé sur votre système (par exemple, via votre gestionnaire de paquets ou le site officiel de Python).

2. **Créer un environnement virtuel**
   ```bash
   virtualenv -p python3.11 venv
   ```
   Cela crée un environnement virtuel nommé `venv` utilisant Python 3.11. Remplacez `python3.11` par `python3.12` si vous préférez.

3. **Activer l'environnement virtuel**
   ```bash
   source venv/bin/activate
   ```

4. **Installer CuPy**
   ```bash
   pip install cupy
   ```
   Cela installe la dernière version compatible de CuPy pour Python 3.11.

5. **Exécuter votre script**
   ```bash
   python scripts/benchmark/cudamark.py
   ```
   Votre script devrait maintenant s'exécuter sans l'`AttributeError`.

6. **Désactiver (quand vous avez terminé)**
   ```bash
   deactivate
   ```

#### Option 2 : Utilisation de `conda`

1. **Créer un environnement Conda**
   ```bash
   conda create -n cudabench python=3.11
   ```
   Cela crée un environnement nommé `cudabench` avec Python 3.11. Utilisez `python=3.12` si vous préférez Python 3.12.

2. **Activer l'environnement**
   ```bash
   conda activate cudabench
   ```

3. **Installer CuPy**
   ```bash
   pip install cupy
   ```

4. **Exécuter votre script**
   ```bash
   python scripts/benchmark/cudamark.py
   ```

5. **Désactiver (quand vous avez terminé)**
   ```bash
   conda deactivate
   ```

### Vérification du correctif

Après avoir configuré l'environnement et exécuté le script, vous devriez voir une sortie similaire à :

```
CPU cores: <votre_nombre_coeurs_cpu>
Threads: 1, Time taken: X.XXXX seconds
Threads: 2, Time taken: X.XXXX seconds
...
ThreadCount,TimeTakenSeconds
1,X.XXXXXX
2,X.XXXXXX
...
```

Si le script s'exécute sans l'`AttributeError`, le correctif est réussi.

### Notes supplémentaires

- **Nombre de threads dans votre script** : Votre script itère sur des nombres de threads (`1, 2, 4, 8, 16, 32, 64, 128`), mais la fonction `parallel_sort_gpu` utilise le tri basé sur le GPU de CuPy (`cp.sort`), qui n'utilise pas directement les threads CPU. La boucle du nombre de threads peut ne pas affecter les performances du tri GPU comme prévu. Si cela est intentionnel pour des modifications futures (par exemple, ajouter du threading CPU), c'est acceptable ; sinon, vous pourriez simplifier le benchmark pour vous concentrer uniquement sur les performances GPU.
- **Version de CuPy** : Si vous suspectez une version obsolète de CuPy, assurez-vous d'installer la dernière version en exécutant `pip install cupy --upgrade`. Cependant, le problème principal ici est la compatibilité avec Python 3.13, et non la version de CuPy seule.
- **Solution à long terme** : Si vous devez absolument utiliser Python 3.13, envisagez de vérifier le dépôt GitHub ou le suivi des problèmes de CuPy pour des mises à jour prenant en charge Python 3.13 (en juin 2025, cela pourrait être disponible). Alternativement, vous pourriez forker CuPy et patcher le décorateur `memoize` pour gérer les fonctions intégrées, mais cela est plus complexe et inutile pour un benchmark.

En utilisant Python 3.11 ou 3.12, vous pouvez exécuter votre benchmark GPU de manière fiable sans rencontrer cette erreur.