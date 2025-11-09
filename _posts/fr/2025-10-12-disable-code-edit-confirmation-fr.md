---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Désactiver la fenêtre de confirmation de modification de code Claude
translated: true
type: note
---

Pour désactiver la popup de confirmation d'édition dans Claude Code (afin qu'elle applique directement les modifications aux fichiers comme `sync_githook.py` sans demander), vous devez configurer les permissions dans votre fichier `settings.json`. C'est le "Claude Code JSON" dont vous parlez - c'est le fichier de configuration principal de Claude Code pour les configurations au niveau utilisateur.

### Étapes pour le configurer

1. **Localiser ou créer le fichier** :
   - Le fichier se trouve à `~/.claude/settings.json` (sur macOS/Linux) ou `%USERPROFILE%\.claude\settings.json` (sur Windows). Le dossier `.claude` est caché, utilisez donc votre terminal/explorateur de fichiers pour y accéder.
   - Si le fichier ou le dossier n'existe pas, créez-les. Vous pouvez le faire en exécutant la commande `/config` de Claude Code dans son REPL interactif (cela vous guidera pour ouvrir l'interface des paramètres).

2. **Modifier le JSON** :
   - Ouvrez `settings.json` dans n'importe quel éditeur de texte (par exemple, VS Code).
   - Ajoutez ou mettez à jour la section `permissions` pour approuver automatiquement les modifications. Voici une configuration simple pour désactiver les invites pour toutes les actions d'édition :

     ```json:disable-run
     {
       "permissions": {
         "defaultMode": "acceptEdits",
         "allow": [
           "Edit(*)",
           "Write(*)",
           "MultiEdit(*)"
         ],
         "ask": []
       }
     }
     ```

     - **Ce que cela fait** :
       - `"defaultMode": "acceptEdits"` : Définit le mode global par défaut pour accepter les modifications sans invite.
       - `"allow"` : Pré-approuve des outils spécifiques comme `Edit` (pour les modifications de fichier unique), `Write` (pour écrire du contenu) et `MultiEdit` (pour les modifications par lot) pour tous les fichiers (caractère générique `*`).
       - `"ask": []` : Garantit qu'aucune action ne déclenche une invite sauf si elle est explicitement refusée ailleurs.
     - Enregistrez le fichier. Les modifications s'appliquent immédiatement dans votre prochaine session Claude Code.

3. **Le tester** :
   - Redémarrez Claude Code ou rechargez la session.
   - Demandez-lui de modifier un fichier (par exemple, "Modifie sync_githook.py pour ajouter un commentaire"). Il devrait appliquer le changement sans la popup.
   - Si vous voulez des paramètres spécifiques au projet (par exemple, seulement pour ce dépôt), créez `.claude/settings.json` dans le dossier racine de votre projet à la place.

4. **Ajustements optionnels** :
   - Pour un contrôle plus granulaire (par exemple, n'autoriser les modifications que dans certains répertoires) : Changez `"Edit(*)"` en `"Edit(./src/**)"`.
   - Si les invites persistent, exécutez `/allowed-tools` dans le REPL pour vérifier les règles actuelles, ou utilisez `/config` pour ajuster via l'interface utilisateur.
   - Pour la sécurité, évitez les règles `allow` trop larges - commencez simplement et élargissez.

Cela devrait accélérer votre flux de travail sans interruptions. Si vous êtes dans un environnement d'entreprise, vérifiez auprès de votre administrateur, car les politiques gérées pourraient remplacer les paramètres utilisateur.

[Documentation des paramètres Claude Code](https://docs.claude.com/en/docs/claude-code/settings)  
[Guide pour désactiver les invites de permission Claude Code](https://www.arsturn.com/blog/how-to-disable-claude-code-permission-prompts)