---
audio: false
generated: true
image: false
lang: fr
layout: post
model: google/gemini-3-pro-preview
title: Catégories d'outils d'assistance au code
translated: true
type: note
---

Les **appels d'outils** ou **actions** typiques dans un assistant de code puissant comme Claude Code sont centrés sur sa capacité à interagir avec un environnement de codage réel et à effectuer les tâches d'un développeur humain.

Ces appels d'outils se répartissent en quelques catégories principales :

### 1. Interaction avec le système de fichiers et la base de code

Ces outils sont essentiels pour que l'assistant comprenne le projet, lise le code existant et effectue des modifications.

| Outil/Action | Cas d'utilisation typique |
| :--- | :--- |
| **`read_file`** (ou référence de fichier comme `@filename`) | Récupérer le contenu d'un fichier spécifique pour comprendre sa logique, ses dépendances ou son contexte. |
| **`list_directory`** | Obtenir la structure des fichiers ou une liste des fichiers dans un répertoire pour identifier les modules pertinents ou trouver un fichier spécifique. |
| **`edit_file` / `write_file`** | L'action principale pour implémenter une solution, refactoriser, ajouter une fonctionnalité ou corriger un bug dans le code. |
| **`create_file`** | Écrire de nouveaux fichiers, comme un nouveau fichier de test, un fichier de configuration ou un nouveau composant. |
| **`search_files`** | Trouver tous les fichiers de la base de code qui contiennent une chaîne de caractères spécifique (par exemple, un nom de fonction, un nom de classe ou un message d'erreur). |

### 2. Exécution et débogage

Pour vérifier son travail, corriger les erreurs et obtenir un retour en temps réel, l'assistant doit exécuter des commandes.

| Outil/Action | Cas d'utilisation typique |
| :--- | :--- |
| **`bash` / `run_command`** | Exécuter des commandes shell comme lancer une build (`npm build`), exécuter des tests (`pytest`, `npm test`), linter le code (`eslint`) ou exécuter un script. |
| **`code_interpreter`** | Exécuter un petit extrait de code dans un environnement sandbox pour calculer rapidement quelque chose, tester une fonction de bibliothèque ou analyser un petit jeu de données. |

### 3. Contrôle de version (Git)

Un assistant de codage agentiel peut gérer le flux de développement en interagissant avec Git.

| Outil/Action | Cas d'utilisation typique |
| :--- | :--- |
| **`git status`** | Vérifier l'état actuel du répertoire de travail. |
| **`git diff`** | Voir les modifications qui ont été apportées pour réviser son propre travail. |
| **`git commit`** | Sauvegarder les modifications dans le dépôt, souvent avec un message de commit généré automatiquement. |
| **`git checkout`** | Changer de branche ou annuler les modifications non validées. |
| **`create_pull_request`** | Automatiser l'étape finale d'une fonctionnalité ou d'une correction. |

### 4. Informations externes

Pour des informations à jour, de la documentation ou pour se connecter à des services externes, des outils spécialisés sont utilisés.

| Outil/Action | Cas d'utilisation typique |
| :--- | :--- |
| **`web_search`** | Rechercher la dernière syntaxe, lire la documentation officielle d'une API ou trouver des guides de dépannage pour une erreur spécifique. |
| **Custom APIs / MCP Servers** | Se connecter à des services externes en utilisant le Model Context Protocol (MCP), comme récupérer des données depuis un Google Drive, interagir avec une base de données (PostgreSQL) ou envoyer un message à un outil de communication (Slack). |

En substance, ces "appels d'outils" permettent au Grand Modèle de Langage (LLM) de se transformer d'un générateur de texte en un **agent** complet qui peut observer son environnement (lire des fichiers, exécuter des commandes), penser (planifier le travail) et agir (modifier des fichiers, valider du code).

Souhaitez-vous voir un exemple étape par étape de la façon dont un assistant de code pourrait utiliser ces outils pour corriger un bug simple ?