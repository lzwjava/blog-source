---
audio: false
generated: true
lang: fr
layout: post
title: Créer une extension VSCode
translated: true
type: note
---

Créer une extension Visual Studio Code (VSCode) peut être une façon gratifiante d'améliorer votre flux de travail de développement ou de contribuer à la communauté. Voici un guide complet pour vous aider à commencer à écrire un plugin VSCode :

### 1. Prérequis
- **Node.js et npm** : Assurez-vous d'avoir Node.js et npm installés. Vous pouvez les télécharger sur [nodejs.org](https://nodejs.org/).
- **Yeoman et VSCode Extension Generator** : Installez Yeoman et le générateur d'extension VSCode globalement en utilisant npm.

```bash
npm install -g yo generator-code
```

### 2. Configuration de votre environnement de développement
- **Installer Visual Studio Code** : Assurez-vous d'avoir VSCode installé. Vous pouvez le télécharger sur [code.visualstudio.com](https://code.visualstudio.com/).

### 3. Générer une nouvelle extension
Utilisez le générateur Yeoman pour créer la structure d'une nouvelle extension. Ouvrez un terminal et exécutez :

```bash
yo code
```

Suivez les invites pour configurer votre extension. Il vous sera demandé :
- Le type d'extension (par exemple, Nouvelle Extension, Nouveau Thème de Couleur, etc.)
- Le nom de votre extension
- Un identifiant (par exemple, `my-extension`)
- Une description
- Initialiser un dépôt git
- Choisir la langue (TypeScript ou JavaScript)
- Installer les dépendances nécessaires

### 4. Comprendre la structure du projet
Votre nouvelle extension aura la structure suivante :
- `.vscode/` : Contient les configurations de lancement pour le débogage.
- `src/` : Contient le code source de votre extension.
- `package.json` : Le fichier manifeste de votre extension.
- `tsconfig.json` : Fichier de configuration TypeScript (si vous utilisez TypeScript).

### 5. Écrire votre extension
- **Activation** : Définissez quand votre extension doit être activée dans `package.json` dans le champ `activationEvents`.
- **Points de contribution** : Définissez ce que votre extension apporte à VSCode, comme des commandes, des vues ou des langages, dans la section `contributes` de `package.json`.

### 6. Implémentation des commandes
Créez des commandes que les utilisateurs peuvent invoquer. Définissez-les dans `package.json` et implémentez-les dans votre fichier d'extension principal (par exemple, `src/extension.ts` ou `src/extension.js`).

Exemple d'une commande dans `package.json` :

```json
"contributes": {
    "commands": [
        {
            "command": "extension.sayHello",
            "title": "Say Hello"
        }
    ]
}
```

Implémentez la commande dans `src/extension.ts` :

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('extension.sayHello', () => {
        vscode.window.showInformationMessage('Hello, World!');
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
```

### 7. Débogage de votre extension
- Appuyez sur `F5` pour ouvrir une nouvelle fenêtre VSCode avec votre extension chargée.
- Définissez des points d'arrêt et utilisez la console de débogage pour tester votre extension.

### 8. Empaquetage et publication
- **Empaqueter l'extension** : Utilisez l'outil `vsce` pour empaqueter votre extension.

```bash
npm install -g vsce
vsce package
```

- **Publier sur le Marketplace** : Suivez les instructions sur le [VSCode Marketplace](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) pour publier votre extension.

### 9. Documentation et bonnes pratiques
- **Documentation** : Fournissez une documentation claire pour votre extension dans un fichier `README.md`.
- **Tests** : Écrivez des tests pour vous assurer que votre extension fonctionne comme prévu.
- **Gestion de version** : Suivez le versionnage sémantique pour les versions de votre extension.

### 10. Ressources supplémentaires
- **Documentation de l'API VSCode** : [vscode-api](https://code.visualstudio.com/api)
- **Exemples d'extensions** : [vscode-extension-samples](https://github.com/microsoft/vscode-extension-samples)

En suivant ces étapes, vous serez bien parti pour créer une extension VSCode fonctionnelle et utile. Bon codage !