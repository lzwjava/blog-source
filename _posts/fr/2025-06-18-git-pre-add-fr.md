---
audio: false
generated: true
lang: fr
layout: post
title: Création d'alternatives aux hooks Git pre-add
translated: true
type: note
---

Git ne dispose pas de hook `pre-add` intégré, mais il existe plusieurs façons d'obtenir une fonctionnalité similaire. Voici quelques approches :

### 1. **Alias Git (Approche recommandée)**
Vous pouvez créer un alias Git qui exécute vos vérifications avant d'appeler `git add` :

```bash
git config --global alias.safe-add '!your-pre-add-script.sh && git add'
```

Utilisez ensuite `git safe-add` au lieu de `git add`.

### 2. **Script wrapper**
Créez un script nommé `git-pre-add` dans votre PATH qui :
1. Exécute vos vérifications pre-add
2. Appelle `git add` si les vérifications sont passées

```bash
#!/bin/bash
# Votre logique de validation pre-add ici
if [ some_condition ]; then
  git add "$@"
else
  echo "Échec des vérifications pre-add"
  exit 1
fi
```

### 3. **Utilisation des hooks existants**
Vous pourriez utiliser les hooks existants de manière créative :
- **pre-commit** : Bien qu'il s'exécute après add mais avant commit, vous pourriez vérifier les fichiers staged ici
- **prepare-commit-msg** : Similaire à pre-commit mais plus tôt dans le processus

### 4. **Surveillance du système de fichiers**
Pour des besoins plus avancés, vous pourriez utiliser :
- **inotifywait** (Linux) pour surveiller votre répertoire de travail
- **fswatch** (Mac) pour une fonctionnalité similaire

### Exemple de script de vérification Pre-Add
Voici un exemple simple qui empêche l'ajout de fichiers avec des espaces de fin :

```bash
#!/bin/bash
# .git/hooks/pre-commit (mais fonctionne sur les fichiers staged)

# Vérifier les erreurs d'espacement
if git diff --cached --check; then
  exit 0
else
  echo "Erreurs d'espacement détectées dans les fichiers staged"
  exit 1
fi
```

N'oubliez pas de rendre tous les scripts de hook exécutables (`chmod +x script.sh`).

Souhaitez-vous que je détaille une approche particulière pour votre cas d'utilisation ?