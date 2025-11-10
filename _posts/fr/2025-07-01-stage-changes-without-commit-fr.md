---
audio: false
generated: true
lang: fr
layout: post
title: Modifications de l'étape dans le hook de pré-validation
translated: true
type: note
---

Pour intégrer les modifications du script `update_notes_link.py` dans le commit actuel (au lieu de créer un commit séparé) lors d'un hook pre-commit, vous devez modifier le hook pour indexer les fichiers mis à jour sans les committer séparément. Ainsi, les modifications du script Python seront incluses dans le commit de l'utilisateur. Ci-dessous, je fournis un script de hook pre-commit révisé qui réalise cela.

### Modifications Clés
- **Aucun Commit Séparé** : Au lieu d'exécuter `git commit` dans le hook, le script indexera seulement les fichiers mis à jour (`git add`) afin qu'ils soient inclus dans le commit de l'utilisateur.
- **Préserver le Message de Commit de l'Utilisateur** : Le hook ne créera pas de nouveau commit, garantissant que le message de commit original de l'utilisateur est utilisé.
- **Gestion des Erreurs** : Si le script Python échoue, le hook se terminera avec un statut non nul pour empêcher le commit.

### Script de Hook Pre-Commit

Voici le script de hook pre-commit mis à jour qui indexe les changements sans créer de commit séparé :

```x-shellscript
#!/bin/bash

# Exécuter le script update_notes_link.py et capturer sa sortie
OUTPUT=$(python scripts/generate/update_notes_link.py 2>&1)
EXIT_CODE=$?

# Vérifier si le script Python s'est exécuté avec succès
if [ $EXIT_CODE -ne 0 ]; then
    echo "Erreur : update_notes_link.py a échoué avec le code de sortie $EXIT_CODE"
    echo "$OUTPUT"
    exit 1
fi

# Vérifier si le fichier spécifique a été mis à jour
if echo "$OUTPUT" | grep -q "Updated original/2025-01-11-notes-en.md"; then
    echo "Liens des notes mis à jour, indexation des changements pour le commit actuel."

    # Indexer les fichiers concernés
    git add original/2025-01-11-notes-en.md
    git add _posts/en/*.md

    # Vérifier que les fichiers ont été indexés
    if ! git diff --cached --quiet; then
        echo "Changements indexés avec succès."
    else
        echo "Aucun changement à indexer."
    fi
else
    echo "Aucune mise à jour pour original/2025-01-11-notes-en.md, aucun fichier supplémentaire indexé."
fi

# Quitter avec succès pour permettre au commit de procéder
exit 0
```

### Explication du Script

- **Shebang (`#!/bin/bash`)** : Garantit que le script s'exécute dans un shell Bash.
- **Exécuter le Script Python** : Exécute `python scripts/generate/update_notes_link.py` et capture sa sortie et son code de sortie.
- **Gestion des Erreurs** : Vérifie le code de sortie (`$EXIT_CODE`) du script Python. S'il est non nul, le hook échoue, affiche l'erreur et arrête le commit.
- **Vérifier la Sortie** : Utilise `grep` pour vérifier si la sortie indique que `original/2025-01-11-notes-en.md` a été mis à jour.
- **Indexer les Fichiers** : Exécute `git add` sur les fichiers spécifiés (`original/2025-01-11-notes-en.md` et `_posts/en/*.md`) pour les inclure dans le commit de l'utilisateur.
- **Aucun Commit** : Ignore `git commit`, permettant à la commande `git commit` de l'utilisateur d'inclure les changements indexés avec son message de commit original.
- **Retour d'Information** : Affiche des messages pour informer l'utilisateur si des changements ont été indexés.
- **Code de Sortie** : Se termine avec `0` pour permettre au commit de procéder, sauf si le script Python échoue.

### Configuration du Hook

1. **Créer le Hook** :
   - Placez le script dans `.git/hooks/pre-commit` de votre dépôt.

2. **Le Rendre Exécutable** :
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

3. **Tester le Hook** :
   - Modifiez un fichier ou assurez-vous que le script Python mettra à jour `original/2025-01-11-notes-en.md`.
   - Exécutez `git commit -m "Votre message de commit"`.
   - Vérifiez que les fichiers mis à jour sont inclus dans le commit en vérifiant `git diff --cached` avant de committer ou `git show` après avoir commité.

### Utilisation du Framework `pre-commit` (Optionnel)

Si vous préférez utiliser le framework `pre-commit`, vous pouvez définir la même logique dans un fichier `.pre-commit-config.yaml`. Cette approche est plus portable et vous permet de spécifier quels fichiers déclenchent le hook.

1. **Installer pre-commit** :
   ```bash
   pip install pre-commit
   ```

2. **Créer `.pre-commit-config.yaml`** :

```yaml
repos:
- repo: local
  hooks:
  - id: update-notes-links
    name: Update Notes Links
    entry: bash -c '
      OUTPUT=$(python scripts/generate/update_notes_link.py 2>&1);
      EXIT_CODE=$?;
      if [ $EXIT_CODE -ne 0 ]; then
        echo "Error: update_notes_link.py failed with exit code $EXIT_CODE";
        echo "$OUTPUT";
        exit 1;
      fi;
      if echo "$OUTPUT" | grep -q "Updated original/2025-01-11-notes-en.md"; then
        echo "Notes links updated, staging changes for the current commit.";
        git add original/2025-01-11-notes-en.md;
        git add _posts/en/*.md;
        if ! git diff --cached --quiet; then
          echo "Changes staged successfully.";
        else
          echo "No changes to stage.";
        fi;
      else
        echo "No updates to original/2025-01-11-notes-en.md, no additional files staged.";
      fi'
    language: script
    files: ^(original/2025-01-11-notes-en\.md|_posts/en/.*\.md)$
    stages: [commit]
```

3. **Installer le Hook** :
   ```bash
   pre-commit install
   ```

4. **Tester le Hook** :
   - Committez des changements sur les fichiers correspondant à l'expression rationnelle `files` (par exemple, `original/2025-01-11-notes-en.md` ou `_posts/en/*.md`).
   - Vérifiez que le hook s'exécute, indexe les changements si applicable, et les inclut dans votre commit.

### Différences Clés par Rapport aux Actions GitHub Originales

- **Aucun Commit Séparé** : Contrairement au workflow GitHub Actions, qui créait un nouveau commit, ce hook indexe les changements pour le commit actuel de l'utilisateur.
- **Aucun Push** : Le hook ne pousse pas les changements, car les hooks pre-commit s'exécutent localement avant que le commit ne soit finalisé. L'utilisateur doit exécuter `git push` manuellement.
- **Gestion des Erreurs** : Le hook vérifie le code de sortie du script Python pour s'assurer qu'il n'échoue pas silencieusement.
- **Aucune Configuration Git User** : Le script omet `git config user.name` et `user.email` puisque la configuration Git de l'utilisateur sera utilisée pour le commit.

### Notes

- **Script Python** : Assurez-vous que `scripts/generate/update_notes_link.py` existe et est exécutable localement. S'il dépend de variables d'environnement ou de dépendances, assurez-vous qu'elles sont disponibles.
- **Chemins de Fichiers** : Vérifiez que les chemins `original/2025-01-11-notes-en.md` et `_posts/en/*.md` correspondent à la structure de votre dépôt.
- **Échec du Hook** : Si le script Python échoue, le hook empêchera le commit, garantissant qu'aucune mise à jour partielle n'est indexée.
- **Test** : Testez avec `git commit` pour confirmer que les changements sont indexés et inclus dans le commit sans créer de commit supplémentaire. Utilisez `git show` pour inspecter le contenu du commit.

### Vérification

Pour vérifier :
1. Modifiez un fichier ou assurez-vous que le script Python met à jour `original/2025-01-11-notes-en.md`.
2. Exécutez `git commit -m "Commit test"`.
3. Vérifiez `git show` pour confirmer que les fichiers mis à jour sont inclus dans le commit avec votre message original.
4. Assurez-vous qu'aucun commit supplémentaire n'est créé (par exemple, pas de commit `chore(notes): Update notes links`).

Si vous avez besoin d'ajustements supplémentaires, comme gérer des cas d'erreur spécifiques ou ajouter plus de fichiers à indexer, faites-le-moi savoir !