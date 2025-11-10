---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide de l'Interface Python C avec CFFI
translated: true
type: note
---

### Qu'est-ce que CFFI ?
CFFI (C Foreign Function Interface) est une bibliothèque Python permettant d'appeler des fonctions C depuis du code Python. Elle est compatible avec CPython et PyPy, offrant une alternative plus sûre et plus portable que des bibliothèques comme ctypes. Elle prend en charge deux modes principaux : ABI (pour appeler des bibliothèques partagées existantes) et API (pour compiler du code C en ligne).

### Installation
Installez CFFI avec pip :
```bash
pip install cffi
```
CFFI nécessite un compilateur C (par exemple, GCC sous Linux, Visual Studio sous Windows) pour construire les modules.

### Exemple d'utilisation de base
Voici un guide étape par étape pour un cas d'usage simple : appeler une fonction C qui additionne deux entiers en utilisant le mode API (recommandé pour le nouveau code).

1. **Importer et configurer FFI** :
   ```python
   from cffi import FFI
   ffibuilder = FFI()
   ```

2. **Définir les déclarations C** :
   Spécifiez les signatures des fonctions C dans une chaîne de caractères :
   ```python
   ffibuilder.cdef("""
       int add(int a, int b);
   """)
   ```

3. **Fournir le code source C** :
   Incluez l'implémentation C :
   ```python
   ffibuilder.set_source("_example",
       """
       int add(int a, int b) {
           return a + b;
       }
       """)
   ```

4. **Compiler le module** :
   Exécutez ce script une fois pour construire l'extension C :
   ```python
   if __name__ == "__main__":
       ffibuilder.compile(verbose=True)
   ```
   Cela génère un module compilé (par exemple, `_example.cpython-39-x86_64-linux-gnu.so`).

5. **Utiliser le module compilé** :
   Dans votre code Python, importez et appelez la fonction :
   ```python
   from _example import lib
   result = lib.add(5, 3)
   print(result)  # Sortie : 8
   ```

### Concepts clés
- **Objet FFI** : L'interface principale, créée avec `FFI()`. Utilisez `cdef()` pour les déclarations et `set_source()` pour le code.
- **Déclarations** : Informent Python sur les types C, les structs, les fonctions, etc. Les chaînes doivent correspondre exactement à la syntaxe C.
- **Conversion de type** : CFFI gère les types de base (int, float, pointeurs) automatiquement. Utilisez les tableaux, les structs ou les callbacks pour les cas complexes.
- **Gestion des erreurs** : Des exceptions comme `CDefError` se produisent pour des définitions C invalides. Les erreurs d'exécution C (par exemple, via `errno`) peuvent être vérifiées avec `ffi.errno`.
- **Gestion de la mémoire** : Utilisez `ffi.new()` pour les structs/tableaux C, et assurez une désallocation correcte pour éviter les fuites de mémoire.

### Modes : ABI vs API
- **Mode ABI** (pour les bibliothèques existantes) : Charge une bibliothèque partagée (par exemple, `ffi.dlopen("mylib.so")`) et appelle les fonctions directement. Exemple :
  ```python
  from cffi import FFI
  ffi = FFI()
  ffi.cdef("int add(int a, int b);")
  lib = ffi.dlopen("/path/to/libmylib.so")
  result = lib.add(5, 3)
  ```
  Ce mode est plus rapide pour les bibliothèques précompilées mais moins portable — vous avez besoin du binaire exact.

- **Mode API** (recommandé) : Compile le code C en ligne, comme dans l'exemple ci-dessus. Il est plus sûr, optimise mieux et fonctionne sur plusieurs plateformes.

### Fonctionnalités avancées
- **Structs et Unions** : Définissez des types complexes, par exemple `cdef("struct Point { int x, y; }")`.
- **Tableaux et Pointeurs** : Utilisez `ffi.new("int[10]")` pour les tableaux ou `ffi.cast("int*", ptr)` pour les casts.
- **Callbacks** : Passez des fonctions Python à C en utilisant `ffi.callback()`.
- **Intégration avec les paquets** : De nombreuses bibliothèques (par exemple, cryptography, NumPy) utilisent CFFI pour la performance.
- **Conseils de performance** : La compilation prend du temps ; utilisez des builds inplace ou des paquets cffi pour la distribution. Évitez les transitions lourdes Python-C dans les boucles.

Pour la documentation complète, consultez la [documentation officielle de CFFI](https://cffi.readthedocs.io/). Ceci couvre l'essentiel — expérimentez avec les exemples pour les adapter à vos besoins. Si vous avez un cas d'usage spécifique, fournissez plus de détails pour des conseils personnalisés.