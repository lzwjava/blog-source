---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Mise à Niveau du Code Claude vers la Dernière Version
translated: true
type: note
---

Pour mettre à niveau Claude Code de la version v2.0.0 à la dernière version, utilisez l'une des méthodes suivantes selon votre type d'installation (toutes les versions prennent en charge les mises à jour automatiques par défaut, qui s'appliquent au prochain démarrage de l'outil ; vous pouvez les désactiver en définissant `DISABLE_AUTOUPDATER=1`) :

### Via la Commande Intégrée de Claude Code
Exécutez la commande de mise à jour manuelle dans votre terminal :
```
claude update
```
Cela applique automatiquement la dernière version. [1][2]

### Via npm (Si Installé Globalement)
Si vous avez initialement installé via npm, mettez à jour avec :
```
npm update -g @anthropic-ai/claude-code
```
Ou forcez l'installation de la dernière version :
```
npm install -g @anthropic-ai/claude-code@latest
```
[3][4]

### Via Binaire Natif (Programme d'Installation Beta)
Pour les installations natives, réexécutez le script d'installation pour la dernière version :
```
# macOS/Linux/WSL
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Windows PowerShell
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest
```
[1]

**Vérification :** Après la mise à niveau, vérifiez votre version avec `claude --version` pour confirmer qu'elle est à jour (par exemple, avec la version stable actuelle). Si vous rencontrez des problèmes, assurez-vous que npm est à jour (`npm install -g npm@latest`). Les paramètres et configurations sont préservés entre les mises à jour. [1][3][4]

Citations :
[1] https://docs.claude.com/en/docs/claude-code/setup
[2] https://www.reddit.com/r/ClaudeAI/comments/1lvbijz/claude_code_updates_from_version_1045_to_1044/
[3] https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/
[4] https://www.claudelog.com/faq/