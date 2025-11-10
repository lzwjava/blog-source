---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Importance du répertoire de travail pour les agents de programmation
translated: true
type: note
---

Oui — vous avez la bonne intuition.

Lorsque vous exécutez **Claude Code**, **Codex** ou des agents de codage similaires, le répertoire de travail est très important car :

### 1. Contexte des opérations sur fichiers

Si vous exécutez l'agent depuis un répertoire parent, mais que votre code réel se trouve dans un sous-répertoire, vous devrez constamment référencer des chemins comme `sousrep/foo.py`. Cela crée une friction supplémentaire. L'exécuter directement dans le sous-répertoire signifie que les chemins relatifs (comme `./foo.py`) fonctionnent simplement.

### 2. Résolution des dépendances

De nombreux projets utilisent `requirements.txt`, `pyproject.toml`, `package.json` ou `pom.xml` qui supposent que le **répertoire de travail actuel** est la racine du projet. Si vous démarrez depuis le mauvais répertoire :

* Python/JavaScript pourrait ne pas trouver les dépendances correctement.
* Les outils de build comme Maven/Gradle/NPM pourraient échouer.
* Votre environnement virtuel pourrait ne pas s'activer correctement.

### 3. Git & contrôle de version

Les commandes Git se comportent différemment selon l'endroit où vous vous trouvez :

* À la racine du projet → fonctionne comme prévu.
* Dans un sous-module ou répertoire imbriqué → peut afficher un historique incomplet ou le mauvais dépôt.

### 4. Configuration & agents

Claude Code (et Codex, Copilot CLI, etc.) lisent souvent :

* Les fichiers `.env`
* `.gitignore`
* Les configurations de projet (`.clauderc`, `.editorconfig`, etc.)

Si vous n'êtes pas dans la racine/sous-répertoire prévu du projet, l'agent pourrait ne pas récupérer les bons paramètres.

---

✅ **Bonnes pratiques :**

* Si le sous-répertoire est un **projet indépendant** (son propre `package.json`, `pom.xml`, etc.), exécutez l'agent dedans.
* S'il ne fait que partie d'un projet plus vaste (comme `src/` sous une seule racine), exécutez depuis le **répertoire racine** pour que les configurations/dépendances soient cohérentes.

Souhaitez-vous que je suggère une **configuration de workflow** où vous pouvez passer facilement entre des sous-projets sans avoir à faire un `cd` manuellement à chaque fois ?