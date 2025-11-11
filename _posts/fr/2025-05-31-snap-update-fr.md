---
audio: false
generated: true
lang: fr
layout: post
title: Mise à jour de VSCode via Snap sur Ubuntu
translated: true
type: note
---

Pour mettre à jour Visual Studio Code (VSCode) installé via Snap sur Ubuntu, suivez ces étapes :

1. **Ouvrir un terminal** : Vous pouvez le faire en appuyant sur `Ctrl + Alt + T`.

2. **Vérifier les mises à jour** : Snap vérifie automatiquement les mises à jour en arrière-plan, mais vous pouvez déclencher manuellement une vérification en exécutant :
   ```bash
   sudo snap refresh
   ```

3. **Mettre à jour VSCode** : Si une version plus récente de VSCode est disponible, la commande `snap refresh` la téléchargera et l'installera. Vous verrez une sortie indiquant la progression, comme :
   ```
   code 1.85.2 from Visual Studio Code (code✓) refreshed
   ```
   Si aucune mise à jour n'est disponible, le message sera :
   ```
   Tous les snaps sont à jour.
   ```

4. **Vérifier la mise à jour** : Pour confirmer la version installée de VSCode, exécutez :
   ```bash
   code --version
   ```
   Cela affichera la version actuelle de VSCode.

### Notes :
- **Mises à jour automatiques** : Les paquets Snap, y compris VSCode, sont généralement mis à jour automatiquement en arrière-plan. Vous n'avez généralement pas besoin d'intervenir manuellement, sauf si vous souhaitez forcer une mise à jour.
- **Privilèges root** : La commande `sudo` est requise pour les opérations Snap à l'échelle du système.
- **Vérifier l'état de Snap** : Si vous souhaitez voir quels paquets Snap sont installés et leurs versions, utilisez :
   ```bash
   snap list
   ```
- **Dépannage** : Si la mise à jour échoue, assurez-vous que votre connexion Internet est stable et que le démon Snap est en cours d'exécution (`sudo systemctl status snapd`). Vous pouvez également essayer d'actualiser les métadonnées Snap avec :
   ```bash
   sudo snap refresh --list
   ```

Ce processus garantit que VSCode reste à jour avec la dernière version disponible dans le Snap store.