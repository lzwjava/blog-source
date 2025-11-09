---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Erreurs d'Installation npm et Leurs Corrections
translated: true
type: note
---

### Comprendre l'erreur

Il s'agit d'un échec d'installation npm lors d'une mise à jour globale (ou installation) du package `@anthropic-ai/claude-code`. Le problème principal se situe dans la phase "reify", où npm tente de "retirer" (sauvegarder) le répertoire du package existant avant d'installer la nouvelle version. Plus précisément :

- npm tente de renommer `/usr/lib/node_modules/@anthropic-ai/claude-code` vers une sauvegarde temporaire comme `/usr/lib/node_modules/@anthropic-ai/.claude-code-ZjqcDZyQ`.
- Cela échoue avec `ENOTEMPTY: directory not empty` (errno -39), ce qui se produit généralement lorsque :
  - Le répertoire source contient des fichiers/sous-répertoires qui sont verrouillés, en cours d'utilisation ou qui ont des problèmes de permissions.
  - Il existe des liens symboliques cassés, des descripteurs de fichiers ouverts (par exemple, provenant d'un processus `claude` en cours d'exécution) ou des particularités du système de fichiers sous Linux.
  - Rarement, la logique interne de déplacement de fichiers de npm rencontre une condition de concurrence.

Votre configuration :
- Node : v22.18.0
- npm : v11.6.1
- OS : Linux 6.14.0-29-generic (probablement Ubuntu/Debian)
- Exécution en tant que root (selon le chemin du journal `/root/.npm/_logs/`), donc les permissions ne sont pas la cause racine.
- Répertoire de travail : `/home/lzwjava/projects/blog-source` (mais il s'agit d'une installation globale, donc non pertinent).

Le package semble être l'outil Claude Code d'Anthropic (CLI pour l'assistance au codage IA), et la ligne 73 montre un avertissement d'incompatibilité de dépendance pour `@img/sharp-libvips-linux-x64`, mais cela n'est pas lié au plantage.

### Correctifs rapides (Essayer dans l'ordre)

1. **Arrêter tous les processus en cours d'exécution** :
   - Tuez tous les processus CLI `claude` ou processus associés : `pkill claude` (ou `ps aux | grep claude` pour trouver les PIDs, puis `kill <PID>`).
   - Fermez les terminaux/IDEs utilisant le package.

2. **Nettoyer manuellement le répertoire** :
   - Supprimez le package et le binaire existants :
     ```
     sudo rm -rf /usr/lib/node_modules/@anthropic-ai/claude-code
     sudo rm -f /usr/bin/claude
     ```
   - Cela contourne l'étape de sauvegarde de npm. Puis réessayez l'installation :
     ```
     sudo npm install -g @anthropic-ai/claude-code
     ```

3. **Vider le cache npm et réessayer** :
   - Exécutez :
     ```
     sudo npm cache clean --force
     sudo npm install -g @anthropic-ai/claude-code
     ```
   - Si cela persiste, ajoutez `--no-optional` pour ignorer les dépendances optionnelles comme la bibliothèque d'images Sharp.

4. **Alternative : Utiliser npx ou éviter l'installation globale** :
   - Si vous n'en avez pas besoin globalement, installez-le localement dans votre projet : `npm install @anthropic-ai/claude-code` (puis exécutez via `npx claude`).
   - Ou utilisez Yarn : `sudo yarn global add @anthropic-ai/claude-code` (Yarn gère parfois les déplacements différemment).

5. **Si toujours bloqué** :
   - Vérifiez les problèmes de système de fichiers : `ls -la /usr/lib/node_modules/@anthropic-ai/` (recherchez des liens symboliques étranges ou des verrous).
   - Rétrogradez npm temporairement : `sudo npm install -g npm@10` (la v11 a parfois des bugs reify ; revenez en arrière après).
   - Journal complet : Vérifiez `/root/.npm/_logs/2025-10-27T16_10_10_534Z-debug-0.log` pour plus d'indices.

Cela devrait résoudre le problème — les installations globales npm sous Linux peuvent être capricieuses avec les renommages. Si vous partagez la commande exacte que vous avez exécutée ou plus de contexte du journal, je peux affiner cela.