---
audio: false
generated: true
lang: fr
layout: post
title: Comment appeler GitHub Copilot depuis une extension VSCode
translated: true
type: note
---

GitHub Copilot est un assistant de codage puissant alimenté par l'IA et intégré à Visual Studio Code (VSCode) et IntelliJ IDEA via leurs plugins respectifs. Bien qu'il n'existe pas d'API REST publique pour appeler directement Copilot, les développeurs peuvent interagir avec ses capacités de manière programmatique au sein d'une extension VSCode en utilisant l'API de chat VSCode, l'API de modèle de langage ou les interactions par commandes. Cet article de blog détaille la création d'une extension VSCode qui déclenche la fonctionnalité de chat de Copilot avec une invite personnalisée, simulant effectivement un "appel d'API" à Copilot, et explique comment exploiter Copilot lui-même pour rationaliser le développement.

## Comprendre l'intégration de Copilot dans VSCode

GitHub Copilot n'expose pas d'API traditionnelle (par exemple, des points de terminaison REST) pour un accès programmatique direct. Au lieu de cela, ses fonctionnalités sont disponibles via :
- **L'API de chat VSCode** : Permet aux extensions de créer des participants de chat personnalisés qui interagissent avec le système de chat de Copilot pour des requêtes en langage naturel.
- **L'API de modèle de langage VSCode** : Permet aux extensions d'accéder aux grands modèles de langage (LLM) de Copilot pour des tâches comme la génération ou l'analyse de code.
- **Les commandes VSCode** : Permet de déclencher les fonctionnalités intégrées de Copilot, telles que l'ouverture de la fenêtre de chat avec une invite prédéfinie.

Ce guide se concentre sur l'utilisation de la commande `workbench.action.chat.open` pour déclencher l'interface de chat de Copilot, car c'est le moyen le plus simple d'intégrer les capacités de Copilot dans une extension.

## Guide étape par étape : Créer une extension VSCode pour déclencher le chat Copilot

Voici un guide étape par étape pour créer une extension VSCode qui ouvre la fenêtre de chat de Copilot avec une invite personnalisée, "appelant" effectivement Copilot pour traiter une requête définie par l'utilisateur.

### 1. Configurer l'extension VSCode

1. **Structurer le projet** :
   - Installez le générateur d'extension VSCode Yeoman : `npm install -g yo generator-code`.
   - Exécutez `yo code` et sélectionnez "New Extension (TypeScript)" pour créer une extension basée sur TypeScript.
   - Nommez l'extension, par exemple `copilot-api-caller`.

2. **Configurer `package.json`** :
   - Définissez une commande pour déclencher le chat Copilot.
   - Exemple de `package.json` :

```json
{
  "name": "copilot-api-caller",
  "displayName": "Copilot API Caller",
  "description": "Déclenche GitHub Copilot Chat avec une invite personnalisée",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.85.0"
  },
  "categories": ["Other"],
  "activationEvents": [
    "onCommand:copilot-api-caller.triggerCopilotChat"
  ],
  "main": "./out/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "copilot-api-caller.triggerCopilotChat",
        "title": "Déclencher le chat Copilot"
      }
    ]
  },
  "scripts": {
    "vscode:prepublish": "npm run compile",
    "compile": "tsc -p ./",
    "watch": "tsc -watch -p ./"
  },
  "devDependencies": {
    "@types/vscode": "^1.85.0",
    "@types/node": "^20.2.5",
    "typescript": "^5.1.3"
  }
}
```

   - **Utilisation de Copilot** : Lors de l'édition de `package.json`, Copilot peut suggérer des champs comme `contributes.commands` ou `activationEvents` au fur et à mesure que vous tapez. Acceptez-les avec `Tab` pour accélérer la configuration.

### 2. Écrire le code de l'extension

Créez la logique de l'extension pour enregistrer une commande qui ouvre le chat de Copilot avec une invite fournie par l'utilisateur.

- **Fichier** : `src/extension.ts`
- **Code** :

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // Enregistrer la commande pour déclencher le chat Copilot
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // Obtenir la saisie de l'utilisateur pour l'invite
    const prompt = await vscode.window.showInputBox({
      prompt: 'Entrez votre requête pour GitHub Copilot',
      placeHolder: 'par ex., Écrire une fonction JavaScript pour trier un tableau'
    });

    if (prompt) {
      try {
        // Exécuter la commande pour ouvrir le chat Copilot avec l'invite
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('Invite envoyée au chat Copilot !');
      } catch (error) {
        vscode.window.showErrorMessage(`Échec du déclenchement du chat Copilot : ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **Fonctionnement** :
  - Enregistre une commande `copilot-api-caller.triggerCopilotChat`.
  - Demande à l'utilisateur une requête (par exemple, "Écrire une fonction Python pour inverser une chaîne").
  - Utilise `vscode.commands.executeCommand('workbench.action.chat.open', prompt)` pour ouvrir la fenêtre de chat de Copilot avec l'invite.
- **Utilisation de Copilot** : Dans VSCode, tapez `import * as vscode` et Copilot suggérera l'importation complète. Ajoutez un commentaire comme `// Enregistrer une commande pour ouvrir le chat Copilot`, et Copilot peut proposer la structure `vscode.commands.registerCommand`. Pour l'exécution de la commande, tapez `// Ouvrir le chat Copilot avec une invite`, et Copilot pourrait suggérer l'appel `executeCommand`.

### 3. Améliorer avec du contexte (Optionnel)

Pour rendre l'extension plus puissante, incluez le contexte de l'éditeur, tel que le code sélectionné, pour fournir à Copilot des informations supplémentaires.

- **Code modifié** (`src/extension.ts`) :

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // Obtenir le texte sélectionné de l'éditeur actif
    const editor = vscode.window.activeTextEditor;
    let context = '';
    if (editor) {
      const selection = editor.selection;
      context = editor.document.getText(selection);
    }

    // Demander la saisie de l'utilisateur
    const prompt = await vscode.window.showInputBox({
      prompt: 'Entrez votre requête pour GitHub Copilot',
      placeHolder: 'par ex., Expliquer ce code',
      value: context ? `Concernant ce code : \n\`\`\`\n${context}\n\`\`\`\n` : ''
    });

    if (prompt) {
      try {
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('Invite envoyée au chat Copilot !');
      } catch (error) {
        vscode.window.showErrorMessage(`Échec du déclenchement du chat Copilot : ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **Fonctionnement** :
  - Récupère le texte sélectionné de l'éditeur actif et l'inclut comme contexte dans l'invite.
  - Pré-remplit la boîte de saisie avec le code sélectionné, formaté comme un bloc de code Markdown.
  - Envoie l'invite combinée à l'interface de chat de Copilot.
- **Utilisation de Copilot** : Commentez `// Obtenir le texte sélectionné de l'éditeur`, et Copilot peut suggérer `vscode.window.activeTextEditor`. Pour le formatage, tapez `// Formater le code en markdown`, et Copilot pourrait proposer la syntaxe des triples backticks.

### 4. Tester l'extension

1. Appuyez sur `F5` dans VSCode pour lancer l'hôte de développement d'extension.
2. Ouvrez la palette de commandes (`Ctrl+Shift+P` ou `Cmd+Shift+P`) et exécutez `Déclencher le chat Copilot`.
3. Entrez une invite (par exemple, "Générer un client d'API REST en TypeScript") ou sélectionnez du code et exécutez la commande.
4. Vérifiez que la fenêtre de chat de Copilot s'ouvre avec votre invite et fournit une réponse.
5. **Utilisation de Copilot** : Si des erreurs se produisent, ajoutez un commentaire comme `// Gérer les erreurs pour l'exécution de la commande`, et Copilot peut suggérer des blocs try-catch ou des messages d'erreur.

### 5. Avancé : Utilisation de l'API de chat VSCode

Pour plus de contrôle, utilisez l'API de chat VSCode pour créer un participant de chat personnalisé qui s'intègre aux modèles de langage de Copilot, permettant un traitement du langage naturel au sein de votre extension.

- **Exemple de code** (`src/extension.ts`) :

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // Enregistrer un participant de chat
  const participant = vscode.chat.createChatParticipant('copilot-api-caller.myParticipant', async (request, context, stream, token) => {
    stream.markdown('Traitement de votre requête...\n');
    // Utiliser l'API de modèle de langage pour générer une réponse
    const model = await vscode.lm.selectChatModels({ family: 'gpt-4' })[0];
    if (model) {
      const response = await model.sendRequest([{ text: request.prompt }], {}, token);
      for await (const chunk of response.stream) {
        stream.markdown(chunk);
      }
    } else {
      stream.markdown('Aucun modèle approprié disponible.');
    }
  });

  participant.iconPath = new vscode.ThemeIcon('sparkle');
  context.subscriptions.push(participant);
}

export function deactivate() {}
```

- **Fonctionnement** :
  - Crée un participant de chat (`@copilot-api-caller.myParticipant`) invocable dans la vue de chat Copilot.
  - Utilise l'API de modèle de langage pour accéder au modèle `gpt-4` de Copilot (ou un autre modèle disponible) pour traiter l'invite.
  - Diffuse la réponse en continu vers la vue de chat.
- **Utilisation de Copilot** : Commentez `// Créer un participant de chat pour Copilot`, et Copilot peut suggérer la structure `vscode.chat.createChatParticipant`. Pour l'API de modèle de langage, commentez `// Accéder au LLM de Copilot`, et Copilot pourrait proposer `vscode.lm.selectChatModels`.

### 6. Empaqueter et déployer

1. Installez `vsce` : `npm install -g @vscode/vsce`.
2. Exécutez `vsce package` pour créer un fichier `.vsix`.
3. Installez l'extension dans VSCode via la vue Extensions ou partagez le fichier `.vsix` avec d'autres.
4. **Utilisation de Copilot** : Ajoutez un commentaire comme `// Ajouter un script pour empaqueter l'extension` dans `package.json`, et Copilot peut suggérer le script `vscode:prepublish`.

## Exploiter Copilot pendant le développement

GitHub Copilot peut accélérer considérablement le développement d'extensions :
- **Suggestions de code** : Lorsque vous tapez dans `src/extension.ts`, Copilot suggère des imports, des enregistrements de commandes et la gestion des erreurs. Par exemple, taper `vscode.commands.` provoque des suggestions comme `registerCommand`.
- **Ingénierie des invites** : Utilisez des commentaires clairs comme `// Déclencher le chat Copilot avec une invite utilisateur` pour guider les suggestions de Copilot. Affinez les commentaires si les suggestions sont inexactes.
- **Débogage** : Si l'extension échoue, ajoutez des commentaires comme `// Journaliser les détails de l'erreur`, et Copilot peut suggérer `console.log` ou `vscode.window.showErrorMessage`.

## Limitations

- **Aucun accès direct à l'API** : Copilot n'expose pas d'API REST publique. Les API de chat et de modèle de langage de VSCode sont les interfaces programmatiques principales.
- **Authentification** : Les utilisateurs doivent avoir un abonnement Copilot actif (gratuit ou payant) et être connectés à VSCode avec un compte GitHub.
- **Portée de l'API de chat** : L'API de chat est limitée à l'interface de chat ; l'accès direct au moteur de complétion de code de Copilot n'est pas disponible de manière programmatique.
- **Environnement** : Assurez-vous que l'extension respecte les politiques organisationnelles concernant les extensions VSCode personnalisées.

## Conclusion

En utilisant le système de commandes de VSCode ou l'API de chat, les développeurs peuvent effectivement "appeler" GitHub Copilot depuis une extension personnalisée, permettant une interaction programmatique avec ses capacités d'IA. L'exemple ci-dessus montre comment déclencher le chat de Copilot avec une invite personnalisée, améliorée avec le contexte de l'éditeur, et fournit une base pour des intégrations plus avancées utilisant l'API de modèle de langage. Avec l'assistance de Copilot pendant le développement, la création de telles extensions devient plus rapide et plus intuitive.

Pour aller plus loin, envisagez d'expérimenter avec l'API de chat pour des participants personnalisés ou d'intégrer un contexte d'éditeur supplémentaire pour des invites plus riches. Bon codage !