---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Extension de l'interface de ligne de commande GitHub Copilot
translated: true
type: note
---

La commande `gh extension install github/gh-copilot` installe l'extension GitHub Copilot pour GitHub CLI, activant des fonctionnalités Copilot telles que les suggestions et explications en ligne de commande. Pour les utilisateurs d'entreprise, l'applicabilité de cette commande dépend de conditions spécifiques :

- **Configuration d'entreprise** : Les utilisateurs d'entreprise peuvent utiliser l'extension CLI Copilot si leur organisation ou entreprise dispose d'un abonnement GitHub Copilot Business ou Copilot Enterprise et que la fonctionnalité CLI est activée par les administrateurs. Si le propriétaire de l'organisation ou l'administrateur d'entreprise a désactivé Copilot dans la CLI, l'extension ne peut pas être utilisée, même si elle est installée.[](https://docs.github.com/fr/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
- **Authentification** : Les utilisateurs d'entreprise doivent s'authentifier à GitHub CLI avec un compte GitHub auquel un siège Copilot est attribué. Pour les comptes d'utilisateur managés sur GitHub Enterprise Cloud (GHE.com), une configuration supplémentaire peut être requise, telle que la mise à jour des paramètres avant la connexion.[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)
- **Prérequis d'installation** : GitHub CLI doit être installé avant d'exécuter la commande. Le processus d'installation lui-même est identique pour les utilisateurs d'entreprise et individuels, mais les politiques d'entreprise peuvent restreindre l'utilisation.[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)

**Étapes pour les utilisateurs d'entreprise** :
1. Assurez-vous que GitHub CLI est installé (voir le [dépôt GitHub CLI](https://github.com/cli/cli) pour les instructions).
2. Vérifiez auprès de votre administrateur d'entreprise que Copilot CLI est activé pour votre organisation.
3. Exécutez `gh extension install github/gh-copilot` dans votre terminal.
4. Authentifiez-vous en utilisant `gh auth login` avec votre compte GitHub attribué par l'entreprise.
5. Si vous utilisez un compte d'utilisateur managé sur GHE.com, suivez les étapes de configuration supplémentaires décrites dans [Utilisation de GitHub Copilot avec un compte sur GHE.com](https://docs.github.com/en/enterprise-cloud@latest/copilot/configuring-github-copilot-in-your-environment/using-github-copilot-with-an-account-on-ghecom).[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)

Si votre entreprise restreint l'accès à la CLI ou n'a pas activé Copilot, l'extension peut s'installer mais ne fonctionnera pas. Consultez votre administrateur pour les détails de la politique.

[Installation de GitHub Copilot dans la CLI](https://docs.github.com/en/enterprise-cloud@latest/copilot/installing-github-copilot-in-the-cli)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
[Configuration de GitHub Copilot pour votre entreprise](https://docs.github.com/en/enterprise-cloud@latest/copilot/setting-up-github-copilot-for-your-enterprise)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/set-up-for-enterprise)