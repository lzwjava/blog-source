---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Présentation de la commande Git Check-Ignore
translated: true
type: note
---

### Qu'est-ce que `git check-ignore` ?

La commande `git check-ignore` est un outil Git utilisé pour déterminer si un fichier ou un chemin spécifique est ignoré par les mécanismes d'ignorance de Git, tels que les fichiers `.gitignore`, `.git/info/exclude` ou les fichiers d'ignorance globaux (via `core.excludesFile`). Elle est particulièrement utile pour déboguer pourquoi un fichier n'est pas suivi ou ajouté au dépôt.

Si le chemin est ignoré, la commande affiche le chemin (et éventuellement le motif correspondant). S'il n'est pas ignoré, il n'y a aucune sortie (code de sortie 0). Cela la rend adaptée aux scripts pour l'automatisation.

### Utilisation de base

Exécutez-la avec un ou plusieurs chemins à vérifier :

```
git check-ignore <nom_du_chemin>...
```

- **Exemple** : Vérifier si un seul fichier est ignoré :
  ```
  git check-ignore chemin/vers/monfichier.txt
  ```
  - Sortie : S'il est ignoré, affiche `chemin/vers/monfichier.txt`. Sinon, n'affiche rien.

- **Exemple** : Vérifier plusieurs fichiers :
  ```
  git check-ignore fichier1.txt fichier2.txt dossier/fichier3.txt
  ```
  - Affiche uniquement les chemins ignorés, un par ligne.

### Options principales

| Option | Description | Exemple |
|--------|-------------|---------|
| `-v`, `--verbose` | Affiche le motif d'ignorance qui a correspondu (par ex., la ligne du `.gitignore`). | `git check-ignore -v chemin/vers/monfichier.txt`<br>Sortie : `chemin/vers/monfichier.txt: .gitignore:1:*.txt` (chemin + fichier:ligne:motif) |
| `-q`, `--quiet` | Supprime la sortie, mais utilise toujours le code de sortie (0 si non ignoré, 1 si ignoré). Utile dans les scripts. | `git check-ignore -q chemin/vers/monfichier.txt`<br>(Aucune sortie ; vérifier `$?` pour le code de sortie) |
| `--stdin` | Lit les chemins depuis l'entrée standard au lieu de la ligne de commande. | `echo "fichier1.txt\nfichier2.txt" \| git check-ignore --stdin` |
| `--non-matching` | Inverse la sortie : Affiche les chemins qui ne sont *pas* ignorés. | `git check-ignore --non-matching -v fichier1.txt fichier2.txt` |

### Cas d'utilisation courants

1. **Débogage des règles `.gitignore`** :
   - Si `git status` n'affiche pas un fichier attendu, exécutez `git check-ignore -v <fichier>` pour voir exactement quelle règle l'ignore.
   - Exemple de sortie : `src/logs/app.log: .gitignore:5:logs/*` (indique que la ligne 5 dans `.gitignore` correspond).

2. **Dans les scripts** :
   - Vérifier si un fichier doit être ajouté :
     ```
     if git check-ignore -q monfichier.txt; then
         echo "Le fichier est ignoré, ignore..."
     else
         git add monfichier.txt
     fi
     ```

3. **Vérification par lots** :
   - Lister tous les fichiers ignorés dans un répertoire :
     ```
     find . -type f -print0 | xargs -0 git check-ignore
     ```

### Conseils
- Elle respecte la pile d'ignorance de Git : `.gitignore` local, exclusions globales, etc.
- Fonctionne sur les fichiers non suivis ou déjà dans le dépôt (mais vérifie par rapport aux règles d'ignorance).
- Pour plus de détails, consultez la documentation officielle.

[Documentation Git check-ignore](https://git-scm.com/docs/git-check-ignore)  
[Stack Overflow : Commande Git pour afficher les fichiers spécifiques ignorés](https://stackoverflow.com/questions/466764/git-command-to-show-which-specific-files-are-ignored-by-gitignore)  
[Utiliser git check-ignore pour déboguer votre .gitignore](https://alexwlchan.net/til/2020/using-git-check-ignore-to-debug-your-gitignore/)