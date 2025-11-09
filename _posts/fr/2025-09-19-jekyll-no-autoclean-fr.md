---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Jekyll Build ne dispose pas de la fonctionnalité de nettoyage automatique
translated: true
type: note
---

Jekyll lui-même n’a pas d’option `--replace` ou `--refresh`. Chaque exécution de `jekyll build` va écrire (ou écraser) les fichiers générés dans le dossier `--destination` que vous spécifiez, mais **il ne supprime pas automatiquement les anciens fichiers** qui n’existent plus dans votre source. Cela signifie que des fichiers obsolètes peuvent rester.

Si vous voulez une sortie de build propre, vous devez vider vous-même le répertoire de destination avant d’exécuter `jekyll build`. Deux approches courantes :

**1. Nettoyage manuel dans votre script**
Avant d’appeler `jekyll build`, effacez le répertoire de destination :

```python
import shutil

def run_jekyll(destination: str, extra_args: list[str]) -> int:
    # Supprimer les anciens fichiers
    dest_path = Path(destination)
    if dest_path.exists():
        shutil.rmtree(dest_path)

    command = [
        "jekyll",
        "build",
        "--destination",
        destination,
        *extra_args,
    ]
    completed = subprocess.run(command, check=False)
    return completed.returncode
```

**2. Utiliser le `_site` par défaut de Jekyll**
Si vous laissez Jekyll utiliser le `_site` par défaut à la racine de votre projet (au lieu d’un `--destination` personnalisé), `jekyll clean` est disponible pour purger la sortie avant de reconstruire :

```bash
jekyll clean && jekyll build
```

Mais `jekyll clean` ne connaît que `_site`, pas un dossier personnalisé.

---

Donc :

* Il n’y a pas d’option `--replace` intégrée.
* Si vous utilisez une destination personnalisée (comme dans votre script), vous devriez explicitement la supprimer avant de builder si vous voulez une sortie fraîche.

Voulez-vous que j’ajuste votre script pour qu’il ait une option `--clean` (comme `jekyll clean`) qui vide automatiquement la destination avant de builder ?