---
audio: false
generated: true
lang: fr
layout: post
title: Outil de modification de code propulsé par l'IA
translated: true
type: note
---

### Visual Studio Code (VS Code) avec GitHub Copilot
VS Code, enrichi par GitHub Copilot (une extension d'IA), permet de sélectionner du code (comme une fonction) et d'utiliser l'IA pour le corriger, le modifier ou le restructurer. Les principales fonctionnalités incluent :
- **Chat Inline** : Sélectionnez le code, appuyez sur `Ctrl+I` (Windows/Linux) ou `Cmd+I` (Mac), et entrez une instruction comme "corriger ce bug" ou "restructurer pour utiliser async/await". Copilot suggère des modifications directement dans l'éditeur.
- **Corriger les Erreurs** : Pour les erreurs de compilation (soulignés rouges), survolez et sélectionnez "Corriger avec Copilot" pour obtenir des corrections générées par l'IA.
- **Vue Chat** : Ouvrez le Chat Copilot (`Ctrl+Alt+I`), sélectionnez du code, et demandez à expliquer, modifier ou générer des tests. Il peut gérer les modifications multi-fichiers en mode agent.
- **Menu Actions** : Faites un clic droit sur le code sélectionné pour accéder aux actions IA comme expliquer, renommer ou réviser.

Copilot est gratuit avec des limites ou payant pour un usage illimité.

### Éditeur de Code IA Cursor
Cursor est un éditeur de code axé sur l'IA, dérivé de VS Code, conçu spécifiquement pour l'édition assistée par l'IA. Il excelle dans la sélection et la modification de code avec l'IA :
- **Modifier avec Ctrl+K** : Sélectionnez une fonction ou un bloc de code, appuyez sur `Ctrl+K` (ou `Cmd+K` sur Mac), et décrivez les changements (par exemple, "optimiser cette fonction pour les performances"). Cursor génère des différences que vous pouvez prévisualiser et appliquer.
- **Mode Composer** : Pour des modifications complexes sur plusieurs fichiers, utilisez l'interface Composer pour demander des changements multi-fichiers, examiner les différences et itérer.
- **Mode Agent** : Appuyez sur `Ctrl+I`, donnez des instructions pour des tâches plus larges (par exemple, "corriger les bugs dans ce module"), et il planifie, modifie et exécute des commandes de manière autonome tout en vous tenant informé.
- **Suggestions de Modification Suivante** : L'IA prédit et suggère des modifications de suivi en fonction de vos changements.

Cursor est gratuit pour les fonctions de base, avec un plan Pro pour les modèles avancés. Il importe les extensions VS Code de manière transparente.

### IntelliJ IDEA avec l'Assistant IA JetBrains
IntelliJ IDEA (et autres IDE JetBrains) dispose d'un plugin intégré d'Assistant IA qui permet de sélectionner du code et d'utiliser l'IA pour des corrections ou des modifications :
- **Menu Actions IA** : Sélectionnez du code, appuyez sur `Alt+Entrée` ou faites un clic droit, choisissez "Actions IA" > options comme "Suggérer une restructuration", "Trouver des problèmes" ou "Corriger avec l'IA". Il analyse le contexte et suggère des modifications dans une visionneuse de différences.
- **Invite Inline** : Tapez une instruction directement dans l'éditeur (par exemple, "restructurer cette fonction"), appuyez sur `Tab`, et l'IA génère/modifie le code en ligne.
- **Corrections d'Erreurs** : Pour les erreurs en surbrillance, sélectionnez "Corriger avec l'IA" pour obtenir des suggestions contextuelles.
- **Génération/Restructuration de Code** : Invoquez via le menu pour expliquer le code, ajouter des annotations de type ou régénérer des sections.

L'Assistant IA nécessite une licence JetBrains AI (essai gratuit disponible) et est alimenté par des modèles comme Mellum pour les complétions.

Tous ces outils intègrent profondément l'IA, mais Cursor est le plus centré sur l'IA, VS Code/Copilot est flexible et largement utilisé, et l'IA d'IntelliJ est adaptée aux workflows d'entreprise ou centrés sur Java. Choisissez en fonction de votre écosystème préféré.

Références :  
[GitHub Copilot dans VS Code](https://code.visualstudio.com/docs/copilot/overview)  
[Démarrer avec GitHub Copilot dans VS Code](https://code.visualstudio.com/docs/copilot/getting-started)  
[Fonctionnalités | Cursor - L'Éditeur de Code IA](https://cursor.com/en/features)  
[Cursor AI : Un Guide Avec 10 Exemples Pratiques](https://www.datacamp.com/tutorial/cursor-ai-code-editor)  
[Utiliser l'IA dans l'éditeur | Documentation IntelliJ IDEA](https://www.jetbrains.com/help/idea/use-ai-in-editor.html)  
[Assistant IA dans les IDE JetBrains | Documentation IntelliJ IDEA](https://www.jetbrains.com/help/idea/ai-assistant-in-jetbrains-ides.html)  
[Utiliser les invites IA pour expliquer et restructurer votre code | Documentation IntelliJ IDEA](https://www.jetbrains.com/help/idea/use-prompts-to-explain-and-refactor-your-code.html)