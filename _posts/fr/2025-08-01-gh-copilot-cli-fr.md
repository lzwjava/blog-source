---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Intégration de GitHub Copilot en Ligne de Commande
translated: true
type: note
---

Vous ne pouvez pas invoquer directement GitHub Copilot en tant que plugin depuis la ligne de commande en utilisant une syntaxe comme `code --plugin copilot "hi"` pour obtenir une réponse. Cependant, GitHub Copilot propose une intégration en ligne de commande via GitHub CLI avec l'extension `gh copilot`, qui fournit une interface de type chat pour les suggestions et explications de commandes. Ce n'est pas exactement la même chose qu'un plugin générique invoqué via la commande `code`, mais cela sert un objectif similaire pour les interactions en ligne de commande.

### Détails sur GitHub Copilot en CLI
- **Prérequis** : Vous avez besoin d'un abonnement GitHub Copilot, de GitHub CLI (`gh`) installé et de l'extension `gh-copilot` installée. Les instructions d'installation sont disponibles dans le dépôt ou la documentation de GitHub CLI [Installation de GitHub CLI](https://cli.github.com/) et [Installer GitHub Copilot en CLI](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line).
- **Utilisation** : Une fois configuré, vous pouvez utiliser des commandes comme :
  - `gh copilot suggest -t shell "hi"` pour obtenir une suggestion de commande shell.
  - `gh copilot explain "hi"` pour obtenir une explication d'une commande.
  - Exemple : Exécuter `gh copilot suggest -t shell "say hello"` pourrait suggérer `echo "hello"` ou une commande de synthèse vocale comme `say "hello"` sur macOS, selon le contexte.
- **Limitations** : L'interface CLI est conçue pour les tâches liées à la ligne de commande (par exemple, les commandes shell, Git ou GitHub CLI) et ne prend pas en charge les réponses conversationnelles génériques comme un chatbot. Elle ne prend également en charge que les invites en anglais [Utilisation responsable de GitHub Copilot en CLI](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli).[](https://docs.github.com/en/copilot/responsible-use/copilot-in-the-cli)[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)
- **Mode interactif** : Après avoir exécuté une commande `suggest`, Copilot démarre une session interactive où vous pouvez affiner la suggestion, l'exécuter (copie dans le presse-papiers) ou l'évaluer. Pour une exécution automatique, vous devez configurer l'alias `ghcs` [Utiliser GitHub Copilot en ligne de commande](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line).[](https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/use-copilot-in-the-cli)[](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)

### Pourquoi `code --plugin copilot "hi"` ne fonctionne pas
- **CLI de Visual Studio Code** : La commande `code` (pour VS Code) prend en charge des options comme `--install-extension` pour installer des extensions, mais elle n'a pas de drapeau `--plugin` pour invoquer des extensions directement avec une entrée comme `"hi"`. Les extensions comme GitHub Copilot fonctionnent généralement dans l'éditeur VS Code, fournissant des suggestions en ligne ou des interfaces de chat, et non comme des outils CLI autonomes [GitHub Copilot dans VS Code](https://code.visualstudio.com/docs/copilot/overview).[](https://code.visualstudio.com/docs/copilot/overview)
- **Architecture de Copilot** : Le plugin GitHub Copilot pour VS Code communique avec un serveur de langage et le backend de GitHub pour les complétions de code et le chat. Il n'y a pas de mécanisme d'API publique ou de CLI pour passer des chaînes arbitraires comme `"hi"` directement au plugin depuis la ligne de commande et obtenir une réponse [Comment invoquer Github Copilot programmatiquement ?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- **Alternative pour une entrée générique** : Si vous souhaitez envoyer une invite comme `"hi"` à Copilot et obtenir une réponse, vous devez utiliser Copilot Chat dans VS Code ou un autre IDE pris en charge, ou explorer d'autres outils CLI d'IA qui prennent en charge les invites conversationnelles (par exemple, AI Shell de Microsoft pour Azure CLI) [Utiliser Microsoft Copilot dans Azure avec AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli).[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)

### Solution de contournement pour votre objectif
Si votre objectif est d'invoquer un assistant IA comme Copilot depuis la ligne de commande avec une invite comme `"hi"` et d'obtenir une réponse, vous pouvez :
1. **Utiliser `gh copilot` pour les tâches en ligne de commande** :
   - Installez GitHub CLI et l'extension Copilot.
   - Exécutez `gh copilot suggest -t shell "greet with hi"` pour obtenir une commande comme `echo "hi"`.
   - Ceci est limité aux contextes de ligne de commande, donc `"hi"` seul peut ne pas donner une réponse significative à moins d'être formulé comme une demande de commande.
2. **Utiliser Copilot Chat de VS Code** :
   - Ouvrez VS Code, utilisez l'interface Copilot Chat (accessible via `⌃⌘I` ou l'icône de chat) et tapez `"hi"` pour obtenir une réponse conversationnelle.
   - Cela nécessite une interaction manuelle dans l'éditeur, pas une invocation CLI [Aide-mémoire GitHub Copilot dans VS Code](https://code.visualstudio.com/docs/copilot/copilot-cheat-sheet).[](https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features)
3. **Explorer d'autres outils CLI d'IA** :
   - **AI Shell** : AI Shell de Microsoft permet des invites en langage naturel dans la CLI pour les tâches liées à Azure. Vous pouvez l'installer et essayer des invites comme `"hi"`, bien qu'il soit optimisé pour les commandes Azure CLI et PowerShell [Utiliser Microsoft Copilot dans Azure avec AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli).[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)
   - **Scripts personnalisés** : Vous pourriez écrire un script pour interagir avec l'API d'un modèle d'IA (par exemple, l'API d'OpenAI, si accessible) pour traiter des invites comme `"hi"`. Cependant, l'API de GitHub Copilot n'est pas disponible publiquement pour une telle utilisation [Comment invoquer Github Copilot programmatiquement ?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
4. **Simuler le comportement d'un plugin** :
   - Créez un script shell ou un alias qui redirige l'entrée vers `gh copilot suggest` ou un autre outil CLI d'IA.
   - Exemple :
     ```bash
     alias ai='gh copilot suggest -t shell'
     ai "greet with hi"
     ```
     Cela suggérerait une commande comme `echo "hi"` ou similaire.

### Invocation programmatique
Si vous cherchez à invoquer programmatiquement une fonctionnalité similaire à Copilot (comme l'implique votre exemple), notez que :
- GitHub Copilot n'expose pas d'API publique pour un accès programmatique direct. Certains efforts communautaires ont rétro-conçu le serveur de langage ou utilisé des proxys pour capturer des suggestions, mais ceux-ci sont complexes et risqués (par exemple, risque de bannissement de compte) [Comment invoquer Github Copilot programmatiquement ?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- Vous pourriez explorer des alternatives open-source ou d'autres modèles d'IA avec des intégrations CLI (par exemple, les outils CLI de Hugging Face ou les LLM locaux comme LLaMA avec des wrappers personnalisés).

### Conclusion
Bien que `code --plugin copilot "hi"` ne soit pas pris en charge, vous pouvez obtenir une fonctionnalité similaire en utilisant `gh copilot` pour les tâches en ligne de commande ou Copilot Chat dans VS Code pour les invites conversationnelles. Pour une expérience IA CLI générique, envisagez des outils comme AI Shell ou des scripts personnalisés avec d'autres API d'IA. Vérifiez toujours les suggestions, car les réponses CLI de Copilot peuvent contenir des erreurs ou des biais provenant des données d'entraînement [Utilisation responsable de GitHub Copilot en CLI](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli).[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)

Si vous avez un cas d'utilisation spécifique (par exemple, IA conversationnelle vs génération de commandes), faites-le-moi savoir et je peux adapter la solution davantage !