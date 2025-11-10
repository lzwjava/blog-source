---
audio: false
generated: true
lang: fr
layout: post
title: Suppression de modèles personnalisés dans GitHub Copilot
translated: true
type: note
---

Pour supprimer un modèle dans l'extension GitHub Copilot pour Visual Studio Code (VS Code), notez que les modèles intégrés (comme le modèle GitHub Copilot par défaut) ne peuvent pas être supprimés, car ils font partie de l'extension. Cependant, si vous faites référence à un modèle personnalisé que vous avez ajouté via un fournisseur tiers (par exemple, Anthropic, OpenAI, Google Gemini, ou d'autres) en utilisant votre propre clé API, vous pouvez effectivement le supprimer en effaçant la clé API associée et les détails du fournisseur. Cette fonctionnalité est en préversion et pourrait ne pas encore être disponible pour les utilisateurs Copilot Business ou Enterprise.

Voici les étapes basées sur la documentation officielle :

1. Ouvrez la vue Chat dans VS Code (si elle n'est pas déjà ouverte, utilisez la Palette de commandes avec `Ctrl+Maj+P` ou `Cmd+Maj+P` sur macOS, puis recherchez "Copilot: Open Chat").
2. Dans la vue Chat, cliquez sur la liste déroulante de sélection du modèle (à côté du champ de saisie) et sélectionnez **Manage Models**. Alternativement, ouvrez la Palette de commandes et exécutez la commande **GitHub Copilot: Manage Models**.
3. Dans l'interface Manage Models, survolez le fournisseur du modèle que vous souhaitez supprimer et cliquez sur l'icône en forme d'engrenage pour modifier ses détails.
4. Supprimez la clé API (et toute URL de point de terminaison le cas échéant) des champs, puis enregistrez les modifications. Cela devrait retirer la disponibilité du modèle dans la liste de sélection.

Si vous rencontrez des problèmes (par exemple, le champ de la clé API ne se met pas à jour ou ne se vide pas correctement, ce qui a été signalé comme un bug dans certains cas), essayez d'abord cette solution de contournement :
- Sélectionnez un modèle différent dans la liste de sélection de la vue Chat pour désélectionner celui que vous essayez de supprimer.
- Retournez dans Manage Models, modifiez le fournisseur, puis supprimez la clé API.

Prérequis et notes :
- Ceci s'applique uniquement aux fonctionnalités de chat ; cela n'affecte pas les complétions de code ou les autres outils.
- Assurez-vous que votre abonnement Copolit permet l'accès à plusieurs modèles (par exemple, Individual, Pro, ou les fonctionnalités de préversion activées pour les organisations).
- Si le modèle persiste ou si vous rencontrez des erreurs, redémarrez VS Code ou vérifiez les mises à jour de l'extension.

Si cela ne correspond pas à ce que vous entendez par "supprimer un modèle" (par exemple, si vous essayez de désactiver l'extension entière ou de masquer les fonctionnalités Copilot), précisez votre demande pour obtenir des étapes plus adaptées.