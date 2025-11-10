---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Configuration de Copilot pour les modèles personnalisés
translated: true
type: note
---

Lorsque vous sélectionnez "managed models" dans GitHub Copilot et que vous voyez toujours GPT-4.1 comme modèle par défaut, ou que vous ne pouvez pas utiliser les modèles Grok ou Kimi d'OpenRouter comme prévu, il existe plusieurs raisons potentielles et étapes pour résoudre ce problème. Voici une analyse du problème et comment configurer Copilot pour utiliser les modèles Grok ou Kimi via OpenRouter :

### Pourquoi GPT-4.1 est toujours utilisé
1.  **Paramètre de modèle par défaut** : GitHub Copilot utilise par défaut GPT-4.1 pour Copilot Chat, Edits et Agent Mode, sauf modification explicite. Même lorsque vous sélectionnez "managed models", le modèle par défaut peut persister si vous n'avez pas entièrement configuré l'intégration OpenRouter ou sélectionné un modèle spécifique.
2.  **Utilisation du modèle spécifique au contexte** : La "fix box" (chat en ligne ou complétion de code) dans Copilot pourrait ne pas prendre en charge le changement vers des modèles personnalisés comme Grok ou Kimi dans certains contextes. Par exemple, le panneau Copilot Chat ou les suggestions en ligne peuvent utiliser le modèle par défaut (GPT-4.1) à moins que vous ne basculiez explicitement vers un modèle personnalisé dans la vue immersive ou Agent Mode.
3.  **Limitations de l'intégration OpenRouter** : OpenRouter permet d'accéder à des modèles comme Grok (créé par xAI) et Kimi (de Moonshot AI), mais l'intégration de Copilot avec OpenRouter nécessite une configuration spécifique, et tous les modèles ne sont pas forcément disponibles immédiatement en raison de limitations d'API ou de problèmes de configuration. Par exemple, l'API d'OpenRouter peut ne pas annoncer la prise en charge des outils pour tous les modèles, ce qui peut empêcher Agent Mode ou certaines fonctionnalités de fonctionner avec Grok ou Kimi.
4.  **Restrictions d'abonnement ou de configuration** : Si vous utilisez un abonnement gratuit ou un abonnement Copilot non-Pro/Business, vous pourriez être limité aux modèles par défaut comme GPT-4.1. De plus, certains modèles (par exemple, Grok ou Kimi) peuvent nécessiter des configurations spécifiques ou un accès premium via OpenRouter.

### Comment utiliser les modèles Grok ou Kimi dans Copilot via OpenRouter
Pour utiliser les modèles Grok ou Kimi d'OpenRouter dans Copilot, en particulier pour la "fix box" (chat en ligne ou complétion de code), suivez ces étapes :

1.  **Configurer OpenRouter avec Copilot** :
    *   **Obtenir une clé API OpenRouter** : Inscrivez-vous sur [openrouter.ai](https://openrouter.ai) et obtenez une clé API. Assurez-vous d'avoir des crédits ou un forfait qui prend en charge l'accès aux modèles Grok (xAI) et Kimi (Moonshot AI K2).
    *   **Configurer OpenRouter dans VS Code** :
        *   Ouvrez Visual Studio Code (VS Code) et assurez-vous que la dernière extension GitHub Copilot est installée (v1.100.2 ou ultérieure).
        *   Allez dans le tableau de bord Copilot dans la barre d'état, ou ouvrez la Palette de commandes (`Ctrl+Shift+P` ou `Command+Shift+P` sur Mac) et tapez `GitHub Copilot: Manage Models`.
        *   Ajoutez votre clé API OpenRouter et configurez le endpoint pour inclure les modèles OpenRouter. Vous devrez peut-être suivre la documentation d'OpenRouter pour l'intégration avec l'extension Copilot de VS Code.
    *   **Vérifier la disponibilité des modèles** : Après avoir ajouté le endpoint OpenRouter, vérifiez la section "Manage Models" dans Copilot. Des modèles comme `openrouter/xai/grok` ou `openrouter/moonshotai/kimi-k2` devraient apparaître dans le sélecteur de modèles. Si ce n'est pas le cas, assurez-vous que votre compte OpenRouter a accès à ces modèles et qu'il n'y a pas de restrictions (par exemple, limitations du forfait gratuit).

2.  **Changer de modèles pour la Fix Box** :
    *   **Pour le chat en ligne (Fix Box)** : La "fix box" fait probablement référence à la fonctionnalité de chat en ligne ou de complétion de code de Copilot. Pour changer le modèle pour le chat en ligne :
        *   Ouvrez l'interface Copilot Chat dans VS Code (via l'icône dans la barre de titre ou la barre latérale).
        *   Dans la vue de chat, sélectionnez le menu déroulant `CURRENT-MODEL` (généralement en bas à droite) et choisissez `openrouter/xai/grok` ou `openrouter/moonshotai/kimi-k2` s'ils sont disponibles.
        *   Si le menu déroulant n'affiche pas Grok ou Kimi, cela pourrait être dû au fait que l'API d'OpenRouter n'annonce pas la prise en charge des outils pour ces modèles, ce qui peut limiter leur utilisation dans certaines fonctionnalités de Copilot comme Agent Mode ou les corrections en ligne.
    *   **Pour la complétion de code** : Pour changer le modèle pour les complétions de code (pas seulement le chat) :
        *   Ouvrez la Palette de commandes (`Ctrl+Shift+P` ou `Command+Shift+P`) et tapez `GitHub Copilot: Change Completions Model`.
        *   Sélectionnez le modèle OpenRouter souhaité (par exemple, Grok ou Kimi) dans la liste. Notez que tous les modèles OpenRouter ne prennent pas nécessairement en charge la complétion de code en raison de la limitation actuelle de VS Code qui ne prend en charge que les endpoints Ollama pour les modèles personnalisés, bien qu'OpenRouter puisse fonctionner avec une solution de contournement par proxy.

3.  **Solution de contournement pour les modèles OpenRouter** :
    *   **Solution par proxy** : Étant donné que l'API d'OpenRouter n'annonce pas toujours la prise en charge des outils (requise pour Agent Mode ou les fonctionnalités avancées), vous pouvez utiliser un proxy comme `litellm` pour activer Grok ou Kimi dans Copilot. Modifiez le fichier `config.yaml` pour inclure :
        ```yaml
        model_list:
          - model_name: grok
            litellm_params:
              model: openrouter/xai/grok
          - model_name: kimi-k2
            litellm_params:
              model: openrouter/moonshotai/kimi-k2
        ```
        *   Suivez les instructions de configuration de sources comme [Bas codes](https://bas.codes) ou [DEV Community](https://dev.to) pour des étapes détaillées sur la configuration du proxy.
    *   **Redémarrez VS Code** : Après avoir configuré le proxy, redémarrez VS Code pour vous assurer que les nouveaux modèles sont disponibles dans le sélecteur de modèles.

4.  **Vérifier l'abonnement et les autorisations** :
    *   **Abonnement Copilot** : Assurez-vous d'avoir un abonnement Copilot Pro ou Business, car les utilisateurs du forfait gratuit peuvent ne pas avoir la possibilité d'ajouter des modèles personnalisés.
    *   **Restrictions Business** : Si vous utilisez un abonnement Copilot Business, votre organisation doit activer le changement de modèle. Vérifiez auprès de votre administrateur ou consultez la documentation de GitHub sur la gestion des politiques Copilot.
    *   **Crédits OpenRouter** : Vérifiez que votre compte OpenRouter dispose de suffisamment de crédits pour accéder aux modèles premium comme Grok ou Kimi, car ceux-ci peuvent consommer plus de crédits que d'autres.

5.  **Dépannage de la Fix Box** :
    *   Si la fix box utilise toujours GPT-4.1, c'est peut-être parce que la fonctionnalité de chat en ligne est verrouillée sur le modèle par défaut dans certains contextes (par exemple, la vue non immersive). Essayez de basculer vers la vue immersive de Copilot Chat (`https://github.com/copilot`) pour sélectionner explicitement Grok ou Kimi.
    *   Si Grok ou Kimi n'apparaissent pas dans le sélecteur de modèles, revérifiez l'intégration OpenRouter dans `Manage Models`. Vous devrez peut-être actualiser la liste des modèles ou réajouter la clé API OpenRouter.
    *   Si le problème persiste, testez les modèles dans Agent Mode ou l'interface de chat de Copilot d'abord pour confirmer qu'ils fonctionnent, puis essayez de les appliquer aux corrections en ligne.

6.  **Outils alternatifs** :
    *   Si l'intégration OpenRouter avec Copilot reste problématique, envisagez d'utiliser Grok directement via [grok.com](https://grok.com) ou les applications iOS/Android Grok, qui offrent un accès gratuit avec des quotas d'utilisation. Les modèles Kimi peuvent également être testés via l'interface de chat d'OpenRouter pour s'assurer qu'ils sont accessibles.
    *   Pour une expérience plus fluide, vous pourriez explorer d'autres IDE ou outils comme Cursor, qui a été noté pour bien fonctionner avec le modèle Kimi K2 d'OpenRouter.

### Notes supplémentaires
*   **Performances des modèles** : Grok est optimisé pour le raisonnement et la recherche de vérité, ce qui le rend adapté aux tâches de débogage complexes ou architecturales, tandis que Kimi (K2) peut exceller dans des scénarios de codage spécifiques. Testez les deux pour voir lequel performe le mieux pour votre cas d'utilisation.
*   **Retour de la communauté** : Certains utilisateurs signalent des problèmes avec les modèles OpenRouter n'apparaissant pas dans le sélecteur de modèles de Copilot, en particulier avec les comptes gratuits. Cela pourrait nécessiter un forfait OpenRouter payant ou un abonnement Copilot Pro pour être résolu.
*   **Limitations en cours** : Il existe une discussion ouverte sur l'activation des endpoints API personnalisés directement dans Copilot (voir [microsoft/vscode-copilot-release#7518](https://github.com/microsoft/vscode-copilot-release/issues/7518)). Jusqu'à ce que cela soit implémenté, la solution de contournement par proxy est la méthode la plus fiable pour utiliser Grok ou Kimi.

### Citations
*   [Changing the AI model for Copilot Chat - GitHub Docs](https://docs.github.com/en/copilot/managing-copilot/changing-the-ai-model-for-copilot-chat)
*   [How to Use Third Party Models in GitHub Copilot Agent Mode - Bas codes](https://bas.codes)
*   [Openrouter - openrouter.ai](https://openrouter.ai)
*   [Agent Mode With Third-Party Models in Copilot - DEV Community](https://dev.to)
*   [r/LocalLLaMA on Reddit: Github Copilot now supports Ollama and OpenRouter Models](https://www.reddit.com)
*   [Which AI model should I use with GitHub Copilot? - The GitHub Blog](https://github.blog)
*   [OpenAI GPT-4.1 is now generally available in GitHub Copilot - GitHub Changelog](https://github.blog)
*   [OpenRouter (free) Models Missing from Manage Models - GitHub Issues](https://github.com/microsoft/vscode-copilot-release/issues/10193)

Si vous rencontrez des erreurs spécifiques ou avez besoin d'une aide supplémentaire pour la configuration, veuillez fournir plus de détails (par exemple, messages d'erreur, version de VS Code ou type d'abonnement), et je pourrai adapter la solution davantage !