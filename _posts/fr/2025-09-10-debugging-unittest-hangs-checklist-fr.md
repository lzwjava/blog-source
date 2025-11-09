---
audio: false
date: 2025-09-10
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Liste de vérification pour le débogage des blocages de tests unitaires
translated: true
type: note
---

Les blocages dans `unittest` proviennent généralement de deadlocks (threads/async), d'I/O bloqué, de problèmes de sous-processus/multiprocessing, ou d'un test en attente d'un appel réseau. Voici une checklist précise pour *identifier où ça bloque* et *débloquer la situation*—fonctionne avec Python 3.9–3.11.

### 1) Exécuter unittest en mode verbeux (et correctement)

```bash
# Si xx.py appelle unittest.main()
python xx.py -v

# Ou utiliser la découverte (recommandé)
python -m unittest -v
python -m unittest discover -v -s tests -p "test_*.py"
```

> Note : `python -v` est le **mode import-verbose de l'interpréteur**, pas le mode test-verbose. Utilisez `-m unittest -v` pour les noms de tests et la progression.

### 2) Activer faulthandler + mode dev (dumps de stack sur blocage, avertissements stricts)

```bash
# Ponctuel
python -X faulthandler -X dev -u -m unittest -v
# Ou via variable d'environnement
export PYTHONFAULTHANDLER=1
python -X dev -u -m unittest -v
```

* `-X faulthandler` permet à Python d'afficher les traces de pile des threads sur les signaux fataux/timeouts.
* `-X dev` rend les avertissements/erreurs plus bruyants.
* `-u` désactive la mise en mémoire tampon de stdout/stderr pour *voir* les impressions en temps réel.

### 3) Forcer un traceback quand ça semble bloqué

Option A — depuis un autre terminal (Linux/macOS) :

```bash
kill -SIGUSR1 <pid>  # avec faulthandler activé, affiche les stacks de tous les threads
```

Option B — ajouter au début de votre test (en haut de `xx.py`) :

```python
import faulthandler, signal, sys
faulthandler.enable()
# Dump les stacks sur SIGUSR1 :
faulthandler.register(signal.SIGUSR1, all_threads=True)
# Dump aussi automatiquement si blocage > 120s :
faulthandler.dump_traceback_later(120, repeat=True)
```

### 4) Tracer l'exécution pas à pas (lourd mais décisif)

```bash
python -m trace --trace xx.py
# ou
python -m trace --trace -m unittest discover -v
```

Vous verrez chaque ligne exécutée ; arrêtez-vous quand la sortie "gèle"—c'est l'emplacement du blocage.

### 5) Utiliser le débogueur immédiatement

```bash
python -m pdb xx.py         # si xx.py appelle unittest.main()
# Mettre un point d'arrêt sur une ligne suspecte :
# (Pdb) b mymodule.py:123
# (Pdb) c
```

Pour les exécutions avec discovery, ajoutez `import pdb; pdb.set_trace()` à l'endroit suspecté.

### 6) Causes courantes & correctifs rapides

* **Multiprocessing sur macOS/Windows** : toujours protéger le point d'entrée du test.

  ```python
  if __name__ == "__main__":
      import unittest
      unittest.main()
  ```

  Si vous lancez des processus dans les tests sur macOS :

  ```python
  import multiprocessing as mp
  if __name__ == "__main__":
      mp.set_start_method("fork")  # évite parfois les blocages vs la valeur par défaut "spawn"
  ```

  (Ne faites cela que si vous savez que votre code est compatible avec fork.)

* **Deadlocks de threads** : vérifiez les `join()` sans timeout, les verrous non libérés, ou les threads d'arrière-plan en attente du thread principal. Remplacez :

  ```python
  t.join()
  ```

  par :

  ```python
  t.join(timeout=5); assert not t.is_alive()
  ```

* **Tests Async** : assurez-vous d'utiliser `IsolatedAsyncioTestCase` (3.8+) ou `asyncio.run()`. Les boucles d'événements doubles ou les `await` oubliés bloquent souvent.

* **Appels réseau** : ajoutez des **timeouts courts** partout :

  ```python
  requests.get(url, timeout=5)
  ```

* **Attentes sur stdin** : supprimez `input()` ou protégez-le dans les tests ; CI/stdin peut bloquer indéfiniment.

* **Mocking qui a mal tourné** : une méthode mockée qui ne résout jamais une `Future`/promise ou un serveur simulé non démarré.

### 7) Visibilité supplémentaire

* Voir les allocations si une fuite/boucle est suspectée :

  ```bash
  python -X tracemalloc=25 -m unittest -v
  ```
* Afficher le bruit des imports (rarement nécessaire pour les blocages) :

  ```bash
  python -v -m unittest -v
  ```

### 8) Si ça ne bloque que sur une version de Python

* Essayez les deux :

  ```bash
  pyenv local 3.11.9
  python -X faulthandler -X dev -m unittest -v

  pyenv local 3.9.19
  python -X faulthandler -X dev -m unittest -v
  ```

  Les différences apparaissent généralement autour du comportement de `multiprocessing`, `asyncio` ou des extensions C.

---

Si vous collez le traceback de `faulthandler` (ou les dernières lignes de `trace --trace`), je pointerai vers le coupable exact et suggérerai un correctif ciblé.