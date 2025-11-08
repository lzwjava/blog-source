---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Modes de discussion personnalisés pour GitHub Copilot
translated: true
type: note
---

### Qu'est-ce que chatmode.md ?

Dans l'extension GitHub Copilot pour Visual Studio Code (VS Code), les fichiers `chatmode.md` sont utilisés pour définir **des modes de chat personnalisés**. Ils vous permettent de configurer Copilot Chat pour qu'il adopte des personas ou des comportements spécifiques pour des tâches comme la planification, les revues de sécurité ou l'implémentation de code. Chaque mode peut spécifier des instructions, les outils disponibles (par exemple, la recherche, fetch, ou l'accès au repo GitHub), et même le modèle d'IA à utiliser. Cette fonctionnalité est en preview à partir de VS Code 1.101 et aide à adapter les réponses pour une cohérence dans votre flux de travail.

Les modes personnalisés sont stockés sous forme de fichiers Markdown avec l'extension `.chatmode.md`, soit dans votre espace de travail (pour le partage en équipe) soit dans votre profil utilisateur (pour une réutilisation personnelle).

### Pourquoi utiliser des modes de chat personnalisés ?
- **Réponses Adaptées** : Appliquez des directives, comme générer des plans sans modifier le code.
- **Contrôle des Outils** : Limitez les outils en lecture seule pour la planification ou activez l'édition pour l'implémentation.
- **Efficacité** : Réutilisez des configurations pour des rôles courants (par exemple, architecte, relecteur).

### Comment créer un fichier chatmode.md

1. Ouvrez la **vue Chat** dans VS Code :
   - Cliquez sur l'icône Copilot Chat dans la barre de titre, ou utilisez `Ctrl+Alt+I` (Windows/Linux) / `Cmd+Option+I` (macOS).

2. Dans la vue Chat, cliquez sur **Configurer le chat > Modes**, puis sélectionnez **Créer un nouveau fichier de mode de chat personnalisé**. Alternativement, ouvrez la Palette de commandes (`Ctrl+Maj+P` / `Cmd+Maj+P`) et exécutez **Chat: New Mode File**.

3. Choisissez un emplacement :
   - **Espace de travail** : Enregistre par défaut dans `.github/chatmodes/` (partageable avec votre équipe). Personnalisez les dossiers via le paramètre `chat.modeFilesLocations`.
   - **Profil utilisateur** : Enregistre dans votre dossier de profil pour la synchronisation entre les appareils.

4. Nommez le fichier (par exemple, `planning.chatmode.md`) et modifiez-le dans VS Code.

Pour gérer les modes existants, utilisez **Configurer le chat > Modes** ou la commande **Chat: Configure Chat Modes**.

### Structure du fichier et syntaxe

Un fichier `.chatmode.md` utilise Markdown avec un en-tête YAML facultatif pour les métadonnées. Voici la structure de base :

- **En-tête YAML** (encadré par des lignes `---`, facultatif) :
  - `description` : Texte court affiché dans l'indicateur de la zone de saisie du chat et dans l'infobulle du menu déroulant.
  - `tools` : Tableau des noms d'outils (par exemple, `['fetch', 'search']`). Utilisez des outils intégrés comme `githubRepo` ou des outils d'extension ; configurez-les via **Configure Tools**.
  - `model` : Modèle d'IA (par exemple, `"Claude Sonnet 4"`). Utilise par défaut le modèle que vous avez sélectionné.

- **Corps** : Instructions Markdown pour l'IA, incluant des invites, des directives ou des liens vers des fichiers externes.

Priorité des outils : Fichier d'invite > Mode référencé > Outils du mode par défaut.

### Exemple de fichier chatmode.md

Ceci crée un mode "Planification" pour générer des plans d'implémentation sans modifier le code :

```
---
description: Générer un plan d'implémentation pour de nouvelles fonctionnalités ou pour restructurer du code existant.
tools: ['fetch', 'githubRepo', 'search', 'usages']
model: Claude Sonnet 4
---
# Instructions du mode Planification

Vous êtes en mode planification. Votre tâche est de générer un plan d'implémentation pour une nouvelle fonctionnalité ou pour restructurer du code existant. Ne faites aucune modification de code — générez uniquement un plan.

Le plan consiste en un document Markdown avec les sections suivantes :

* **Aperçu** : Brève description de la fonctionnalité ou de la restructuration.
* **Exigences** : Liste des exigences.
* **Étapes d'implémentation** : Étapes détaillées pour la mise en œuvre.
* **Tests** : Liste des tests pour vérifier.
```

Enregistrez le fichier, et il apparaîtra dans le menu déroulant des modes de chat.

### Comment utiliser un mode de chat personnalisé

1. Ouvrez la **vue Chat** (comme indiqué ci-dessus).

2. Dans le menu déroulant en haut de la vue Chat (à côté du sélecteur de mode), choisissez votre mode personnalisé (par exemple, "Planification").

3. La `description` du mode apparaît comme indicateur dans la zone de saisie. Tapez votre invite (par exemple, "Planifier une fonctionnalité d'authentification utilisateur").

4. Copilot répond en suivant les instructions et les outils du mode. Changez de mode à tout moment via le menu déroulant — les modes intégrés (Ask, Edit, Agent) restent disponibles.

Pour plus d'exemples, consultez les contributions de la communauté dans le dépôt [Awesome Copilot](https://github.com/github/awesome-copilot/tree/main).

### Références
- [Modes de chat personnalisés dans VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes)
- [Commencer avec le chat dans VS Code](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)