---
audio: false
generated: true
lang: fr
layout: post
title: Paramètres JVM personnalisés dans le plugin Liberty Tools
translated: true
type: note
---

Vous pouvez passer des paramètres JVM personnalisés — comme `-Dversion=5.1` — en les ajoutant à votre configuration de lancement du mode dev Liberty dans VS Code. Typiquement, vous faites cela en modifiant (ou en créant) le fichier `.vscode/launch.json` dans votre projet et en incluant le paramètre sous une propriété comme `"vmArgs"` (ou `"args"` si votre configuration attend des arguments de goal Maven).

Par exemple, si vous utilisez l'extension Liberty Tools avec le mode dev, votre configuration pourrait ressembler à ceci :

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "liberty",
      "request": "launch",
      "name": "Liberty Dev Mode",
      "goal": "dev",
      "vmArgs": "-Dversion=5.1"
    }
  ]
}
```

### Étapes :
1. **Ouvrir ou Créer la Configuration de Lancement :**
   - Dans VS Code, ouvrez votre projet.
   - Naviguez jusqu'au dossier `.vscode` et ouvrez (ou créez) le fichier `launch.json`.

2. **Ajouter Votre Configuration de Mode Dev :**
   - Ajoutez une entrée de configuration comme montré ci-dessus. La clé `"vmArgs"` vous permet de spécifier les options JVM qui seront passées au serveur lorsque le mode dev démarre.

3. **Sauvegarder et Lancer :**
   - Sauvegardez le fichier.
   - Utilisez la vue Exécuter et Déboguer pour démarrer la configuration "Liberty Dev Mode".

Si vous utilisez Maven directement, vous pouvez également démarrer le mode dev depuis la ligne de commande avec :

```bash
mvn liberty:dev -Dversion=5.1
```

Cela passe la propriété personnalisée à la JVM lors du démarrage du serveur.

En configurant de cette manière, l'extension Liberty Tools inclura votre paramètre personnalisé (`-Dversion=5.1`) chaque fois que vous démarrez le mode dev.