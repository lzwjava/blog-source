---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Pousser par force Git via suppression de branche
translated: true
type: note
---

```python
#!/usr/bin/env python3
"""
git_force_push.py

Ce script effectue un "push forcé" en supprimant d'abord la branche distante,
puis en poussant la branche locale. Cela fonctionne si le dépôt autorise les
suppressions de branches mais pas les pushes forcés.

Usage: python git_force_push.py <remote> <branche>
Exemple: python git_force_push.py origin main

Note: Cela suppose que vous avez les permissions suffisantes et que la suppression est autorisée.
Soyez prudent, car supprimer une branche peut entraîner la perte de commits.
"""

import subprocess
import sys

def run_command(command):
    """Exécute une commande shell et retourne sa sortie."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande '{command}': {e}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python git_force_push.py <remote> <branche>")
        sys.exit(1)

    remote = sys.argv[1]
    branch = sys.argv[2]

    # Supprimer la branche distante
    delete_cmd = f"git push {remote} :{branch}"
    print(f"Suppression de la branche distante: {delete_cmd}")
    run_command(delete_cmd)

    # Pousser la branche locale
    push_cmd = f"git push {remote} {branch}"
    print(f"Poussée de la branche locale: {push_cmd}")
    run_command(push_cmd)

    print("Push forcé effectué avec succès.")
```

### Fonctionnement
- **Étape de suppression**: Exécute `git push origin :main` pour supprimer la branche distante (tel qu'autorisé dans votre dépôt).
- **Étape de push**: Exécute `git push origin main` pour pousser la branche locale, la recréant ainsi sur le dépôt distant.
- Cela permet effectivement d'effectuer un push forcé en supprimant l'historique distant et en le remplaçant par l'historique local.
- **Notes de sécurité/utilisation**: Testez d'abord dans un dépôt non critique. Cela nécessite une configuration Git appropriée et les permissions adéquates. Si le dépôt a des protections supplémentaires (par exemple via des hooks), cela pourrait échouer. Aucune garantie; les opérations Git peuvent être destructrices.