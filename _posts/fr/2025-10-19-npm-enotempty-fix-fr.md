---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résoudre l'Erreur d'Installation npm ENOTEMPTY
translated: true
type: note
---

### Comprendre l'erreur

Votre commande `sudo npm i -g @anthropic-ai/claude-code --verbose` échoue avec une erreur `ENOTEMPTY` pendant le processus d'installation. C'est un problème npm courant qui se produit lorsque npm essaie de renommer (ou déplacer) un répertoire existant lors d'une mise à jour ou réinstallation d'un package, mais que le répertoire n'est pas vide. Dans ce cas, l'échec spécifique concerne le renommage de `/usr/lib/node_modules/@anthropic-ai/claude-code` vers un emplacement de sauvegarde temporaire (`/usr/lib/node_modules/@anthropic-ai/.claude-code-ZjqcDZyQ`).

Cela se produit généralement à cause de :
- Une installation précédente partielle ou interrompue ayant laissé des fichiers ou sous-répertoires.
- Des verrous de fichiers par un autre processus (par exemple, si le package était partiellement chargé ou qu'une autre commande npm est en cours d'exécution).
- Plus rarement, des problèmes de permissions avec les installations globales sous `sudo`.

Le package lui-même (`@anthropic-ai/claude-code`) est légitime — c'est l'outil CLI officiel d'Anthropic pour "Claude Code", un assistant de codage agentique qui s'intègre à votre terminal et base de code.

### Correctifs rapides

Essayez ces étapes dans l'ordre. Exécutez-les en tant que root ou avec `sudo` si indiqué, car il s'agit d'une installation globale.

1. **Supprimer manuellement le répertoire existant**  
   Cela nettoie l'installation partielle problématique :  
   ```
   sudo rm -rf /usr/lib/node_modules/@anthropic-ai/claude-code
   ```  
   - Si le répertoire scope parent (`@anthropic-ai`) est maintenant vide, vous pouvez le supprimer aussi :  
     ```
     sudo rm -rf /usr/lib/node_modules/@anthropic-ai
     ```  
   Puis réessayez votre commande originale :  
   ```
   sudo npm i -g @anthropic-ai/claude-code --verbose
   ```

2. **Vider le cache npm**  
   Si l'étape précédente ne fonctionne pas, des entrées de cache corrompues pourraient être en cause :  
   ```
   sudo npm cache clean --force
   sudo npm cache verify
   ```  
   Réessayez l'installation après cela.

3. **Vérifier les processus en cours d'exécution**  
   Assurez-vous qu'aucun autre processus npm/Node n'utilise le répertoire :  
   ```
   ps aux | grep npm
   ```  
   Tuez ceux qui traînent si nécessaire (par exemple `sudo kill <PID>`), puis réessayez.

4. **Alternative : Utiliser npx pour tester**  
   Si vous voulez juste tester l'outil sans une installation globale complète, essayez :  
   ```
   npx @anthropic-ai/claude-code --help
   ```  
   Cela le télécharge et l'exécute temporairement sans modifier vos modules globaux.

### Conseils supplémentaires
- **Meilleure pratique pour les permissions** : Les installations globales avec `sudo` peuvent entraîner des problèmes de propriété plus tard. Envisagez d'utiliser un gestionnaire de version Node comme `nvm` pour éviter complètement `sudo`, ou définissez un préfixe global personnalisé :  
  ```
  mkdir ~/.npm-global
  npm config set prefix '~/.npm-global'
  export PATH=~/.npm-global/bin:$PATH
  ```  
  Puis installez sans `sudo`.
- **Vérifier après l'installation** : Une fois installé, vérifiez avec `claude-code --version` (en supposant que c'est le nom du binaire — confirmez dans la documentation).
- Si les problèmes persistent, partagez le résultat de `npm ls -g @anthropic-ai/claude-code` pour plus de diagnostics.

Cela devrait vous permettre de démarrer rapidement. Si vous rencontrez un autre problème, collez le nouveau log !

[Claude Code sur npm](https://www.npmjs.com/package/@anthropic-ai/claude-code)  
[Documentation Anthropic : Configurer Claude Code](https://docs.claude.com/en/docs/claude-code/setup)