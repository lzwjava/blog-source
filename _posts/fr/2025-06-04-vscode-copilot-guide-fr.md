---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser GitHub Copilot dans Visual Studio Code
translated: true
type: note
---

GitHub Copilot est un assistant de codage alimenté par l'IA développé par GitHub et OpenAI, conçu pour améliorer la productivité des développeurs dans Visual Studio Code (VS Code). Il fournit des complétions de code contextuelles, un chat en langage naturel et des capacités de édition avancées. Ce guide vous accompagne dans la configuration de Copilot, l'exploration de ses fonctionnalités et l'optimisation de votre flux de travail avec des astuces et des bonnes pratiques.

## 1. Introduction à GitHub Copilot
GitHub Copilot agit comme un programmeur pair IA, offrant des suggestions de code en temps réel, répondant aux questions de codage et automatisant les tâches répétitives. Il est alimenté par de grands modèles de langage entraînés sur de vastes ensembles de données de code public, lui permettant de prendre en charge de nombreux langages de programmation et frameworks, notamment Python, JavaScript, TypeScript, Ruby, Go, C# et C++.

Les fonctionnalités clés incluent :
- **Complétions de code** : Suggère des extraits de code au fur et à mesure que vous tapez, des lignes uniques aux fonctions entières.
- **Copilot Chat** : Permet des requêtes en langage naturel pour expliquer le code, générer des extraits ou déboguer des problèmes.
- **Mode Agent** : Automatise les tâches de codage à plusieurs étapes, telles que le refactoring ou la création d'applications.
- **Instructions personnalisées** : Adapte les suggestions pour correspondre à votre style de codage ou aux exigences de votre projet.

## 2. Configuration de GitHub Copilot dans VS Code

### Prérequis
- **VS Code** : Téléchargez et installez Visual Studio Code depuis le [site officiel](https://code.visualstudio.com/). Assurez-vous d'avoir une version compatible (toute version récente supporte Copilot).
- **Compte GitHub** : Vous avez besoin d'un compte GitHub avec accès à Copilot. Les options incluent :
  - **Copilot Gratuit** : Complétions et interactions de chat limitées par mois.
  - **Copilot Pro/Pro+** : Plans payants avec des limites plus élevées et des fonctionnalités avancées.
  - **Accès Organisation** : Si fourni par votre organisation, vérifiez auprès de votre administrateur pour les détails d'accès.
- **Connexion Internet** : Copilot nécessite une connexion active pour fournir des suggestions.

### Étapes d'installation
1. **Ouvrez VS Code** :
   Lancez Visual Studio Code sur votre machine.

2. **Installez l'extension GitHub Copilot** :
   - Allez dans la vue **Extensions** (Ctrl+Shift+X ou Cmd+Shift+X sur macOS).
   - Recherchez "GitHub Copilot" dans le Marketplace des Extensions.
   - Cliquez sur **Installer** pour l'extension officielle GitHub Copilot. Ceci installe également automatiquement l'extension Copilot Chat.

3. **Connectez-vous à GitHub** :
   - Après l'installation, une invite peut apparaître dans la Barre d'état de VS Code (coin inférieur droit) pour configurer Copilot.
   - Cliquez sur l'icône Copilot et sélectionnez **Sign in** pour vous authentifier avec votre compte GitHub.
   - Si aucune invite n'apparaît, ouvrez la Palette de commandes (Ctrl+Shift+P ou Cmd+Shift+P) et exécutez la commande `GitHub Copilot: Sign in`.
   - Suivez le flux d'authentification via le navigateur, en copiant le code fourni par VS Code vers GitHub.

4. **Vérifiez l'activation** :
   - Une fois connecté, l'icône Copilot dans la Barre d'état devrait devenir verte, indiquant un état actif.
   - Si vous n'avez pas d'abonnement Copilot, vous serez inscrit au plan Copilot Gratuit avec une utilisation mensuelle limitée.

5. **Optionnel : Désactivez la Télémétrie** :
   - Par défaut, Copilot collecte des données de télémétrie. Pour désactiver, allez dans **Paramètres** (Ctrl+, ou Cmd+,), recherchez `telemetry.telemetryLevel`, et définissez-la sur `off`. Alternativement, ajustez les paramètres spécifiques à Copilot sous `GitHub Copilot Settings`.

> **Note** : Si votre organisation a désactivé Copilot Chat ou restreint les fonctionnalités, contactez votre administrateur. Pour le dépannage, référez-vous au [Guide de dépannage GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting).[](https://code.visualstudio.com/docs/copilot/setup)

## 3. Fonctionnalités principales de GitHub Copilot dans VS Code

### 3.1 Complétions de code
Copilot suggère du code au fur et à mesure que vous tapez, des lignes uniques aux fonctions ou classes entières, basé sur le contexte de votre code et la structure de votre fichier.
- **Comment ça marche** :
  - Commencez à taper dans un langage supporté (par exemple, JavaScript, Python, C#).
  - Copilot affiche les suggestions en texte "fantôme" grisé.
  - Appuyez sur **Tab** pour accepter une suggestion ou continuez à taper pour l'ignorer.
  - Utilisez **Alt+]** (suivant) ou **Alt+[** (précédent) pour parcourir les suggestions multiples.
- **Exemple** :
  ```javascript
  // Calculate factorial of a number
  function factorial(n) {
  ```
  Copilot pourrait suggérer :
  ```javascript
  if (n === 0) return 1;
  return n * factorial(n - 1);
  }
  ```
  Appuyez sur **Tab** pour accepter la suggestion.

- **Astuces** :
  - Utilisez des noms de fonctions descriptifs ou des commentaires pour guider Copilot (par exemple, `// Trier un tableau en ordre croissant`).
  - Pour plusieurs suggestions, survolez la suggestion pour ouvrir le Panneau de Complétions (Ctrl+Entrée) pour voir toutes les options.

### 3.2 Copilot Chat
Copilot Chat vous permet d'interagir avec Copilot en utilisant le langage naturel pour poser des questions, générer du code ou déboguer des problèmes.
- **Accéder au Chat** :
  - Ouvrez la **Vue Chat** depuis la Barre d'activité ou utilisez **Ctrl+Alt+I** (Windows/Linux) ou **Cmd+Ctrl+I** (macOS).
  - Alternativement, utilisez le **Chat Inline** (Ctrl+I ou Cmd+I) directement dans l'éditeur pour des requêtes contextuelles.
- **Cas d'utilisation** :
  - **Expliquer le code** : Sélectionnez un bloc de code, ouvrez le Chat Inline et tapez `explain this code`.
  - **Générer du code** : Tapez `write a Python function to reverse a string` dans la Vue Chat.
  - **Débogage** : Collez un message d'erreur dans le Chat et demandez une correction.
- **Exemple** :
  Dans la Vue Chat, tapez :
  ```
  What is recursion?
  ```
  Copilot répond avec une explication détaillée, incluant souvent des exemples de code en Markdown.

- **Commandes Slash** :
  Utilisez des commandes comme `/explain`, `/doc`, `/fix`, `/tests`, ou `/optimize` pour spécifier des tâches. Par exemple :
  ```
  /explain this function
  ```
  avec une fonction sélectionnée générera une explication détaillée.

### 3.3 Mode Agent (Aperçu)
Le Mode Agent permet à Copilot de gérer de manière autonome des tâches de codage à plusieurs étapes, telles que la création d'applications, le refactoring de code ou l'écriture de tests.
- **Comment l'utiliser** :
  - Ouvrez la **Vue Copilot Edits** dans VS Code Insiders ou Stable (si disponible).
  - Sélectionnez **Agent** dans le menu déroulant des modes.
  - Entrez une invite, par exemple, `Create a React form component with name and email fields`.
  - Copilot analyse votre base de code, suggère des modifications et peut exécuter des commandes terminal ou des tests.
- **Capacités** :
  - Génère du code sur plusieurs fichiers.
  - Surveille les erreurs et itère pour corriger les problèmes.
  - Intègre de nouvelles bibliothèques ou migre le code vers des frameworks modernes.

> **Note** : Le Mode Agent est expérimental et fonctionne mieux dans les petits dépôts. Partagez vos retours via le dépôt GitHub de VS Code.[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)

### 3.4 Instructions personnalisées
Personnalisez Copilot pour qu'il s'aligne sur votre style de codage ou les exigences de votre projet.
- **Configuration** :
  - Créez un fichier `.github/copilot-instructions.md` dans votre espace de travail.
  - Ajoutez des instructions en Markdown, par exemple, `Use snake_case for Python variable names`.
  - Activez les instructions personnalisées dans **Paramètres** > **GitHub** > **Copilot** > **Enable custom instructions** (VS Code 17.12 ou ultérieur).
- **Exemple** :
  ```markdown
  # Instructions personnalisées Copilot
  - Utilisez le camelCase pour les variables JavaScript.
  - Préférez async/await à .then() pour les promesses.
  ```
  Copilot adaptera ses suggestions à ces préférences.

### 3.5 Contexte de l'espace de travail avec @workspace
Utilisez la commande `@workspace` pour interroger l'ensemble de votre base de code.
- **Exemple** :
  Dans la Vue Chat, tapez :
  ```
  @workspace Where is the database connection string configured?
  ```
  Copilot recherche dans votre espace de travail et référence les fichiers pertinents.

### 3.6 Suggestions de modification suivante (Aperçu)
Copilot prédit et suggère la modification logique suivante basée sur vos changements récents.
- **Comment ça marche** :
  - Lorsque vous modifiez du code, Copilot met en évidence les modifications suivantes potentielles.
  - Acceptez les suggestions avec **Tab** ou modifiez-les via le Chat Inline.
- **Cas d'utilisation** : Idéal pour le refactoring itératif ou pour compléter des modifications de code liées.

## 4. Astuces pour optimiser l'utilisation de Copilot

### 4.1 Rédiger des invites efficaces
- Soyez spécifique : Au lieu de `write a function`, essayez `write a Python function to sort a list of dictionaries by the 'age' key`.
- Fournissez du contexte : Incluez des détails sur le framework ou la bibliothèque (par exemple, `use React hooks`).
- Utilisez des commentaires : Écrivez `// Generate a REST API endpoint in Express` pour guider les complétions.

### 4.2 Tirer parti du contexte
- **Référencer des Fichiers/Symboles** : Utilisez `#filename`, `#folder` ou `#symbol` dans les invites de Chat pour limiter le contexte.
  ```
  /explain #src/utils.js
  ```
- **Glisser-Déposer** : Glissez des fichiers ou des onglets de l'éditeur dans l'invite de Chat pour ajouter du contexte.
- **Attacher des Images** : Dans VS Code 17.14 Preview 1 ou ultérieur, attachez des captures d'écran pour illustrer des problèmes (par exemple, des bugs d'interface utilisateur).

### 4.3 Utiliser les commandes Slash
- `/doc` : Générer une documentation pour une fonction.
- `/fix` : Suggérer des corrections pour les erreurs.
- `/tests` : Créer des tests unitaires pour le code sélectionné.
- Exemple :
  ```
  /tests Generate Jest tests for this function
  ```

### 4.4 Sauvegarder et réutiliser les invites
- Créez un fichier `.prompt.md` dans `.github/prompts/` pour stocker des invites réutilisables.
- Exemple :
  ```markdown
  # Invite de composant React
  Générer un composant fonctionnel React avec un style Tailwind CSS. Demander le nom du composant et les props s'ils ne sont pas fournis.
  ```
- Attachez l'invite dans le Chat pour la réutiliser à travers les projets.

### 4.5 Choisir le bon modèle
- Copilot supporte plusieurs modèles de langage (par exemple, GPT-4o, Claude Sonnet).
- Sélectionnez les modèles dans le menu déroulant de la Vue Chat pour un codage plus rapide ou un raisonnement plus profond.
- Pour les tâches complexes, Claude Sonnet peut performer mieux en Mode Agent.[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)

### 4.6 Indexer votre espace de travail
- Activez l'indexation de l'espace de travail pour des recherches de code plus rapides et plus précises.
- Utilisez un index distant pour les dépôts GitHub ou un index local pour les grandes bases de code.

## 5. Bonnes pratiques
- **Vérifier les suggestions** : Vérifiez toujours les suggestions de Copilot pour leur exactitude et leur alignement avec les standards de votre projet.
- **Combiner avec IntelliCode** : Dans Visual Studio, Copilot complète IntelliCode pour des complétions améliorées.[](https://devblogs.microsoft.com/visualstudio/github-copilot-in-visual-studio-2022/)
- **Vérifier la sécurité** : Copilot peut suggérer du code avec des vulnérabilités. Vérifiez les suggestions, surtout dans les projets sensibles, et conformez-vous aux politiques de votre organisation.[](https://medium.com/%40codebob75/how-to-use-copilot-in-visual-studio-a-step-by-step-guide-b2a5db3b54ba)
- **Utiliser des noms significatifs** : Des noms de variables et de fonctions descriptifs améliorent la qualité des suggestions.
- **Itérer avec le Chat** : Affinez les invites si les suggestions initiales ne sont pas bonnes.
- **Surveiller les limites d'utilisation** : Avec Copilot Gratuit, suivez vos complétions et interactions de chat mensuelles via les paramètres du compte GitHub ou le badge Copilot dans VS Code.[](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-free-plan?view=vs-2022)

## 6. Dépannage des problèmes courants
- **Copilot inactif** : Assurez-vous d'être connecté avec un compte GitHub ayant accès à Copilot. Actualisez les identifiants via le menu déroulant de la Barre d'état de Copilot.
- **Aucune suggestion** : Vérifiez votre connexion internet ou passez à un langage supporté. Ajustez les paramètres sous **Outils** > **Options** > **GitHub Copilot**.
- **Fonctionnalités limitées** : Si vous atteignez la limite d'utilisation de Copilot Gratuit, vous reviendrez aux suggestions IntelliCode. Passez à un plan payant ou vérifiez votre statut.[](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-free-plan?view=vs-2022)
- **Problèmes de réseau** : Consultez le [Guide de dépannage GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting).

## 7. Cas d'utilisation avancés
- **Requêtes de base de données** : Demandez à Copilot de générer des requêtes SQL (par exemple, `Write a SQL query to join two tables`).
- **Développement d'API** : Demandez du code pour des endpoints d'API (par exemple, `Create a Flask route to handle POST requests`).
- **Tests unitaires** : Utilisez `/tests` pour générer des tests pour des frameworks comme Jest ou Pytest.
- **Refactoring** : Utilisez le Mode Agent pour refactoriser du code sur plusieurs fichiers (par exemple, `Migrate this jQuery code to React`).

## 8. Considérations de confidentialité et de sécurité
- **Utilisation des données** : Copilot transmet des extraits de code aux serveurs de GitHub en temps réel pour générer des suggestions mais ne les conserve pas (Copilot for Business supprime les extraits immédiatement).[](https://medium.com/%40codebob75/how-to-use-copilot-in-visual-studio-a-step-by-step-guide-b2a5db3b54ba)
- **Correspondance de code public** : Copilot peut suggérer du code correspondant à des dépôts GitHub publics. Activez la référence de code pour voir les détails de licence.[](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-extension?view=vs-2022)
- **Politiques organisationnelles** : Vérifiez si votre organisation autorise l'utilisation de Copilot, car certaines désactivent le Chat ou restreignent les suggestions.[](https://docs.github.com/en/copilot/quickstart)
- **Télémétrie** : Désactivez la télémétrie dans les paramètres de VS Code si vous le souhaitez.[](https://code.visualstudio.com/docs/copilot/setup)

## 9. Ressources pour approfondir
- [Documentation GitHub Copilot](https://docs.github.com/en/copilot)
- [Démarrage rapide VS Code Copilot](https://code.visualstudio.com/docs/copilot/copilot-quickstart)
- [Tutoriel Copilot Chat](https://code.visualstudio.com/docs/copilot/copilot-chat)
- [Série VS Code Copilot sur YouTube](https://www.youtube.com/playlist?list=PLj6YeMhvp2S6X0vF4TrRkpZ7GIqM3oPWp)
- [FAQ GitHub Copilot](https://docs.github.com/en/copilot/faq)

## 10. Conclusion
GitHub Copilot dans VS Code est un outil puissant qui rationalise le codage en fournissant des suggestions intelligentes, en répondant aux questions et en automatisant les tâches complexes. En le configurant correctement, en exploitant ses fonctionnalités et en suivant les bonnes pratiques, vous pouvez considérablement booster votre productivité et vous concentrer sur les tâches de codage créatif. Expérimentez avec les capacités de Copilot, personnalisez-le pour votre flux de travail et restez attentif à la sécurité et aux limites d'utilisation pour tirer le meilleur parti de ce programmeur pair IA.