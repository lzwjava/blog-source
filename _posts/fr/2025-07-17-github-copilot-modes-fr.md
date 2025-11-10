---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Modes de GitHub Copilot Comparés
translated: true
type: note
---

### Aperçu
GitHub Copilot propose plusieurs modes d'assistance au codage dans les IDE comme VS Code et Visual Studio, incluant le Mode Édition (qui correspond à votre description du "mode correction" pour sélectionner et réparer des lignes ou fonctions spécifiques) et le Mode Agent (qui gère des modifications plus larges et autonomes sur des fichiers ou projets entiers). Le Mode Édition est précis et contrôlé par l'utilisateur, idéal pour des corrections ciblées, tandis que le Mode Agent agit comme un programmeur pair IA, raisonnant sur des tâches complexes et effectuant des modifications multi-fichiers sans nécessiter une interaction constante.[1][1] Les deux modes améliorent la productivité mais diffèrent par leur portée, leur autonomie et leur flux de travail.

### Différences Clés
Le Mode Édition se concentre sur des extraits de code sélectionnés par l'utilisateur, fournissant des suggestions à examiner et à approuver avant d'appliquer les changements. En revanche, le Mode Agent opère à un niveau supérieur, analysant le contexte complet de la base de code pour planifier, exécuter et itérer sur les modifications de manière autonome, modifiant souvent des fichiers entiers ou des composants connexes pour maintenir la cohérence.[2][1] Voici une comparaison côte à côte :

| Fonctionnalité           | Mode Édition (Mode Correction)                                                                 | Mode Agent                                                                 |
|--------------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Portée**               | Limité aux lignes, fonctions sélectionnées ou à un seul fichier. Vous surlignez le code pour corriger des bugs, le refactoriser ou améliorer des parties spécifiques.[1] | Espace de travail ou projet entier. Il identifie et modifie automatiquement les fichiers connexes, au-delà de votre sélection.[2][3] |
| **Contrôle Utilisateur** | Élevé : Suggère des changements pour votre examen et approbation explicite. Vous définissez exactement ce qu'il faut modifier.[4] | Moyen : Applique les modifications automatiquement mais signale les commandes risquées (ex: exécutions terminal) pour examen. Vous définissez l'objectif via des invites en langage naturel.[1][1] |
| **Autonomie**            | Faible : Fournit des suggestions ciblées ; ne raisonne pas entre les fichiers ni n'exécute d'actions indépendantes.[1] | Élevée : Raisonne étape par étape, exécute des tests/commandes, détecte les erreurs et s'auto-corrige. Maintient le contexte entre les sessions.[2][3] |
| **Temps de Réponse**     | Rapide : Analyse rapide de la sélection uniquement.[2] | Plus Lent : Analyse le contexte complet du projet, ce qui peut prendre plus de temps pour les grandes bases de code.[2] |
| **Idéal Pour**           | Corrections rapides comme déboguer une fonction, optimiser une boucle ou réécrire une méthode sans impact plus large.[1] | Tâches complexes comme le refactoring entre fichiers, la génération de tests pour un module, la migration de code ou la création de fonctionnalités from scratch.[3][5] |
| **Exemples**             | - Sélectionner une fonction boguée : "Corrige cette vérification de null."<br>- Surligner des lignes : "Rends ceci asynchrone." [2] | - Invite : "Refactorise toute la couche service pour utiliser async/await et mets à jour toutes les dépendances."<br>- Ou : "Modernise ce projet Java vers JDK 21 sur tous les fichiers." [5][6] |
| **Risques/Limitations**  | Risque minimal, les changements étant isolés ; mais nécessite une sélection manuelle pour chaque correction.[1] | Une autonomie plus élevée peut entraîner des modifications non désirées ; toujours examiner les diffs. Pas idéal pour les environnements très contrôlés.[7][4] |

### Cas d'Usage et Flux de Travail
- **Mode Édition pour les Corrections Ciblées** : Utilisez ce mode lorsque vous savez exactement ce qui ne va pas, par exemple, en sélectionnant du code sujet aux erreurs dans une fonction pour résoudre un bug ou améliorer les performances. C'est comme un outil de "modification ponctuelle" — sélectionnez le code dans votre IDE, invitez Copilot via le chat (par exemple, "@workspace /fix"), et appliquez l'aperçu du diff. Ce mode excelle dans le développement itératif où vous souhaitez garder un contrôle total et éviter de refondre les zones non affectées. Par exemple, dans un projet .NET, vous pourriez sélectionner une méthode et demander, "Identifie les exceptions de référence null et suggère des corrections" pour cet extrait uniquement.[2][8] Il est disponible dans VS Code et Visual Studio avec les extensions GitHub Copilot.

- **Mode Agent pour les Modifications à l'Échelle du Projet** : Activez ce mode pour des changements holistiques, par exemple lorsque vous devez modifier des fichiers entiers ou coordonner des mises à jour dans une base de code. Démarrez une session dans Copilot Chat (par exemple, "#agentmode" ou via le menu déroulant), donnez une invite de haut niveau comme "Trouve toutes les utilisations de l'API obsolète et migre vers la nouvelle dans ce projet", et observez-le planifier les étapes : analyser les fichiers, proposer des modifications, exécuter des tests et itérer. Il peut créer de nouveaux fichiers, mettre à jour des namespaces, ou même échafauder des sections d'une application. Dans la modernisation Java, par exemple, il scanne un projet legacy, met à jour les dépendances Gradle et valide les changements sur plusieurs fichiers.[5][3] Ce mode est particulièrement puissant pour le refactoring, la chasse aux bugs à grande échelle ou l'automatisation de tâches répétitives comme l'ajout de documentation ou de tests.[6][9]

Le Mode Agent s'appuie sur les fondations du Mode Édition mais les étend — considérez le Mode Édition comme un scalpel pour des coupures précises, et le Mode Agent comme un chirurgien gérant l'opération complète.[1] Des instructions personnalisées (par exemple, via les paramètres VS Code) peuvent guider le Mode Agent pour la cohérence, comme l'application de conventions de nommage sur l'ensemble des modifications.[1]

### Quand Choisir Chaque Mode
- Optez pour le **Mode Édition/Correction** si votre tâche est localisée (ex: corriger une seule fonction) pour rester simple et rapide.
- Passez au **Mode Agent** pour plus d'efficacité sur des portées plus larges, comme les modifications de fichiers entiers ou les refactorisations multi-étapes, mais commencez petit pour bâtir la confiance dans ses résultats.[2][1] Les deux nécessitent un abonnement GitHub Copilot (Pro ou supérieur) et sont intégrés dans VS Code/Visual Studio. Pour de meilleurs résultats, combinez-les : Utilisez le Mode Édition pour les corrections initiales, puis le Mode Agent pour propager les changements à l'échelle du projet.[8] Si vous travaillez sur du code sensible, examinez attentivement toutes les propositions du Mode Agent pour éviter les mauvaises surprises.[7]

Citations :
[1] https://github.blog/ai-and-ml/github-copilot/copilot-ask-edit-and-agent-modes-what-they-do-and-when-to-use-they/
[2] https://devblogs.microsoft.com/dotnet/ask-mode-vs-agent-mode/
[3] https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/
[4] https://github.blog/developer-skills/github/less-todo-more-done-the-difference-between-coding-agent-and-agent-mode-in-github-copilot/
[5] https://github.blog/ai-and-ml/github-copilot/a-step-by-step-guide-to-modernizing-java-projects-with-github-copilot-agent-mode/
[6] https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode
[7] https://www.reddit.com/r/GithubCopilot/comments/1je448f/after_playing_with_agent_mode_i_think_my_favorite/
[8] https://visualstudiomagazine.com/articles/2025/06/18/copilot-compared-advanced-ai-features-in-visual-studio-2022-vs-vs-code.aspx
[9] https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/