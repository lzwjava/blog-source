---
audio: false
date: 2025-09-10
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Résoudre la mise en mémoire tampon de sortie Python dans les tests unitaires
translated: true
type: note
---

Oui — ce délai est presque toujours dû au **buffering de sortie**, et Git-Bash/mintty sur Windows peut le rendre plus visible. Vous n'avez pas besoin d'une queue sauf si vous faites du logging multi-processus ; commencez par rendre stdout/stderr non bufferisé et évitez le buffering propre à unittest.

### Faites ceci quand vous exécutez

```bash
# PowerShell / CMD :
py -3.11 -u -m unittest -v

# Git-Bash :
PYTHONUNBUFFERED=1 py -3.11 -u -m unittest -v
# ou
PYTHONUNBUFFERED=1 python -u -m unittest -v
```

* `-u` = stdio non bufferisé
* `PYTHONUNBUFFERED=1` = idem, affecte aussi les processus enfants

Si vous utilisez directement `xx.py` :

```bash
python -u xx.py -v
```

### Rendez-le immédiat dans votre code (solution prête à l'emploi)

Placez ceci tout au début de votre bootstrap de test (ou du bloc `if __name__ == "__main__":`) :

```python
import os, sys
os.environ.setdefault("PYTHONUNBUFFERED", "1")

# Python 3.7+
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True, write_through=True)
    sys.stderr.reconfigure(line_buffering=True, write_through=True)

print("booting tests...", flush=True)
```

Et à chaque fois que vous faites un `print(...)`, ajoutez `flush=True` pour les points critiques.

### Si vous utilisez le module `logging`

```python
import logging, sys
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
    force=True,  # 3.8+
)
# StreamHandler flush chaque enregistrement ; ceci garantit qu'il pointe vers stdout
```

### Attention au buffering de unittest

Si vous (ou un framework) l'avez activé, la sortie est retenue jusqu'à la fin du test :

* **À éviter** : `unittest.main(buffer=True)` ou `python -m unittest -b`
* Utilisez la valeur par défaut (pas de `-b`) pour que les logs s'affichent au moment où ils se produisent.

### Conseils spécifiques à Git-Bash

* Mintty fait parfois croire aux programmes que stdout n'est pas un TTY → plus de buffering. Vos deux meilleures solutions sont la combinaison **`-u`/`PYTHONUNBUFFERED`** ci-dessus ou exécutez simplement depuis **Windows Terminal/PowerShell/CMD** pour comparer.
* Si vous lancez des sous-processus, ils seront aussi bufferisés sauf s'ils héritent de l'environnement. Avec `PYTHONUNBUFFERED=1` exporté, les processus enfants Python se comportent correctement.

### Quand une queue *est* utile

Seulement si vous faites du logging **multiprocessing** : utilisez `logging.handlers.QueueHandler/QueueListener` pour envoyer les logs des workers au processus principal ; sinon, les buffers des enfants ou l'entrelacement peuvent poser problème.

Si vous collez un petit extrait de la façon dont vous exécutez les tests (commande + tout argument `unittest.main(...)`) et comment vous loggez/imprimez, je personnaliserai le changement minimal pour rendre toute la sortie instantanée.