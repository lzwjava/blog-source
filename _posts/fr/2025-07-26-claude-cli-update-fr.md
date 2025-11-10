---
audio: false
generated: true
lang: fr
layout: post
title: Mise à Jour de l'Interface en Ligne de Commande Claude Code
translated: true
type: note
---

Bonjour ! On dirait que vous utilisez l'outil CLI Claude Code d'Anthropic. D'après le résultat que vous avez collé, il semble qu'il ait déjà tenté une mise à jour automatique vers la version 1.0.61, mais si cela ne fonctionne pas ou si vous devez mettre à jour manuellement, voici comment procéder :

Pour mettre à jour le CLI Claude Code :
- Ouvrez votre terminal.
- Exécutez la commande : `claude update`
Cette commande intégrée devrait récupérer et installer la dernière version.

Si la mise à jour échoue (par exemple, à cause de problèmes de permissions ou de réseau), vous pouvez essayer de la réinstaller via npm (en supposant que vous avez Node.js et npm installés) :
- Exécutez : `npm install -g @anthropic-ai/claude-code`

Après la mise à jour, vous devrez peut-être vous reconnecter en exécutant `claude /login` (ou parfois `claude login`, selon la version). Si vous voyez toujours des erreurs, vérifiez votre connexion Internet, assurez-vous que votre clé API est valide ou consultez la documentation officielle de dépannage.

Pour plus de détails sur les commandes, vous pouvez exécuter `claude --help` comme vous l'avez fait, ce qui devrait afficher les options dans la version mise à jour.

[CLI reference - Anthropic API](https://docs.anthropic.com/en/docs/claude-code/cli-reference)  
[How to Set Up and Use the Claude CLI Tool Like a Pro](https://medium.com/@riccardo.bernardi.advisor/unlocking-claude-pros-power-how-to-set-up-and-use-the-claude-cli-tool-like-a-pro-against-github-d29f8f682a03)  
[GitHub - anthropics/claude-code](https://github.com/anthropics/claude-code)  
[Claude Code overview - Anthropic API](https://docs.anthropic.com/en/docs/claude-code/overview)