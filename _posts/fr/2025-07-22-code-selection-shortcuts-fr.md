---
audio: false
generated: true
lang: fr
layout: post
title: Sélection Rapide de Code et Édition par IA
translated: true
type: note
---

Voici un aperçu de la façon de sélectionner rapidement une fonction ou une méthode à l'aide de raccourcis dans **Visual Studio Code (VS Code)**, **Cursor** et **IntelliJ IDEA**, suivi de l'utilisation de leurs fonctionnalités d'IA pour corriger ou modifier le code sélectionné.

### Visual Studio Code (VS Code)
VS Code n'a pas de raccourci direct pour sélectionner une fonction/méthode entière lorsque votre curseur est à l'intérieur, mais vous pouvez utiliser les approches suivantes :
- **Étendre la Sélection** : Appuyez sur `Ctrl+Shift+.` (Windows/Linux) ou `Cmd+Shift+.` (Mac) pour étendre la portée de la sélection. Des appuis répétés sélectionnent le bloc englobant (par exemple, le corps de la fonction, puis la fonction entière). Cela fonctionne bien pour JavaScript, Python, etc.
- **Sélection Intelligente** : Utilisez `Ctrl+Shift+Flèche Droite` (Windows/Linux) ou `Cmd+Shift+Flèche Droite` (Mac) pour étendre la sélection basée sur la syntaxe (peut nécessiter plusieurs appuis pour capturer la fonction entière).
- **Extension : Select By** : Installez l'extension "Select By" et configurez un raccourci clavier (par exemple, `Ctrl+K, Ctrl+S`) pour sélectionner la fonction/méthode englobante basée sur des motifs spécifiques au langage.

**Édition par IA avec GitHub Copilot** :
- Après avoir sélectionné la fonction, appuyez sur `Ctrl+I` (Windows/Linux) ou `Cmd+I` (Mac) pour ouvrir le chat inline de Copilot. Tapez une instruction comme "corriger les bugs dans cette fonction" ou "refactoriser pour utiliser les fonctions fléchées".
- Alternativement, faites un clic droit sur la sélection, choisissez "Copilot > Fix" ou "Copilot > Refactor" pour obtenir des suggestions d'IA.
- Dans la vue Copilot Chat (`Ctrl+Alt+I`), collez le code sélectionné et demandez des modifications (par exemple, "optimiser cette fonction").

### Cursor AI Code Editor
Cursor, basé sur VS Code, améliore la sélection et l'intégration de l'IA :
- **Sélectionner le Bloc Englobant** : Appuyez sur `Ctrl+Shift+.` (Windows/Linux) ou `Cmd+Shift+.` (Mac) pour étendre la sélection à la fonction/méthode englobante, similaire à VS Code. La conscience du modèle de langage de Cursor rend souvent cela plus précis pour des langages comme Python ou TypeScript.
- **Raccourcis Personnalisés** : Vous pouvez définir un raccourci personnalisé dans `settings.json` (par exemple, `editor.action.selectToBracket`) pour sélectionner directement la portée de la fonction.

**Édition par IA dans Cursor** :
- Après avoir sélectionné la fonction, appuyez sur `Ctrl+K` (Windows/Linux) ou `Cmd+K` (Mac), puis décrivez les changements (par exemple, "ajouter la gestion d'erreur à cette fonction"). Cursor affiche un aperçu diff des modifications générées par l'IA.
- Utilisez `Ctrl+I` pour le Mode Agent afin de corriger ou d'optimiser la fonction de manière autonome à travers les fichiers, avec un retour itératif.
- Le Mode Composer (accessible via l'interface utilisateur) permet des modifications multi-fichiers si la fonction impacte d'autres parties de la base de code.

### IntelliJ IDEA
IntelliJ IDEA offre des raccourcis robustes pour sélectionner les fonctions/méthodes :
- **Sélectionner le Bloc de Code** : Avec votre curseur à l'intérieur d'une méthode, appuyez sur `Ctrl+W` (Windows/Linux) ou `Cmd+W` (Mac) pour sélectionner de manière incrémentielle le bloc englobant. Des appuis répétés étendent la sélection à la méthode entière (signature incluse). Cela fonctionne pour Java, Kotlin, Python, etc.
- **Réduire la Sélection** : Utilisez `Ctrl+Shift+W` (Windows/Linux) ou `Cmd+Shift+W` (Mac) pour réduire la sélection si vous dépassez.
- **Sélection Sensible à la Structure** : Appuyez sur `Ctrl+Alt+Shift+Haut` (Windows/Linux) ou `Cmd+Option+Shift+Haut` (Mac) pour sélectionner directement la méthode englobante via l'arborescence de structure.

**Édition par IA avec JetBrains AI Assistant** :
- Après avoir sélectionné la méthode, appuyez sur `Alt+Entrée` ou faites un clic droit et choisissez "AI Actions" > "Fix with AI" ou "Suggest Refactoring". AI Assistant fournit des suggestions sensibles au contexte dans une visionneuse diff.
- Utilisez l'invite inline (tapez `/` suivi de votre demande, par exemple, `/refactor to use streams`, puis appuyez sur `Tab`) pour modifier directement la méthode sélectionnée.
- Ouvrez la fenêtre d'outils AI Assistant pour décrire des changements complexes (par exemple, "ajouter la journalisation à cette méthode") et appliquer le code généré.

### Résumé
- **VS Code** : Utilisez `Ctrl+Shift+.` pour étendre la sélection, puis `Ctrl+I` pour les modifications par IA Copilot.
- **Cursor** : Même raccourci de sélection (`Ctrl+Shift+.`) avec `Ctrl+K` pour des modifications précises pilotées par l'IA.
- **IntelliJ IDEA** : Utilisez `Ctrl+W` pour une sélection rapide de méthode, puis `Alt+Entrée` pour les corrections par AI Assistant.

IntelliJ a le raccourci intégré le plus précis pour sélectionner les méthodes (`Ctrl+W`), tandis que l'intégration de l'IA de Cursor est la plus transparente pour modifier le code sélectionné. VS Code est flexible mais peut nécessiter des extensions pour une sélection de fonction plus rapide.

Références :  
[Code Navigation in Visual Studio Code](https://code.visualstudio.com/docs/editor/editingevolved)  
[Cursor AI: A Guide With 10 Practical Examples](https://www.datacamp.com/tutorial/cursor-ai-code-editor)  
[Code Editing in IntelliJ IDEA](https://www.jetbrains.com/help/idea/working-with-source-code.html)  
[Use AI in editor | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/use-ai-in-editor.html)