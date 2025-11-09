---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Rebase Git interactif depuis la racine
translated: true
type: note
---

### Démystifier `git rebase -i --root`

`git rebase -i --root` est une commande Git qui effectue un rebasage interactif en commençant par le tout premier commit (la racine) dans l'historique de votre dépôt. Décomposons-la étape par étape.

#### Éléments clés de la commande
- **`git rebase`** : Cette commande réécrit l'historique de vos commits en les déplaçant vers une nouvelle base. Elle est utile pour nettoyer des historiques désordonnés, fusionner des commits ou modifier des messages.
- **`-i` (ou `--interactive`)** : Exécute le rebasage en mode interactif, en ouvrant un éditeur de texte où vous pouvez spécifier des actions pour chaque commit (par exemple, pick, squash, edit ou drop).
- **`--root`** : Ce drapeau indique à Git de commencer le rebasage à partir du commit racine — le commit initial dans le dépôt. Sans cela, `git rebase -i` commence généralement au premier commit après une base spécifiée ou à partir d'un certain point de l'historique.

#### Que signifie « Racine » ici ?
- Dans Git, la « racine » fait référence au commit ancêtre le plus ancien, celui qui n'a pas de parent (par exemple, le premier commit créé avec `git commit --allow-empty --allow-empty-message` ou similaire). Il peut s'agir du tout premier commit du dépôt.
- L'utilisation de `--root` signifie réappliquer l'intégralité de l'historique depuis le début, vous permettant de modifier chaque commit, y compris le commit racine. C'est comme effectuer un rebasage complet sur tous les commits jamais effectués dans le dépôt.

#### Quand et pourquoi l'utiliser ?
- **Cas d'usage** : Idéal pour les dépôts où vous souhaitez nettoyer ou réécrire l'intégralité de l'historique des commits (par exemple, lors du fork d'un projet et de la nécessité de supprimer un historique initial désordonné). Vous pourriez fusionner des commits initiaux, changer des messages de commit ou réorganiser des éléments.
- **Exemple de workflow** :
  1. Exécutez `git rebase -i --root`.
  2. Un éditeur s'ouvre avec une liste de tous les commits, en commençant par la racine.
  3. Modifiez le fichier pour spécifier les actions (par exemple, transformer plusieurs commits initiaux en un seul).
  4. Enregistrez et quittez ; Git réapplique l'historique.

Cette commande est puissante mais destructive — elle réécrit l'historique, évitez donc de l'utiliser sur des branches partagées (utilisez-la uniquement sur des branches locales ou après coordination avec les collaborateurs). Si des conflits surviennent, vous devrez les résoudre manuellement.

Pour plus de détails, consultez la documentation officielle de Git : `git help rebase`. Si vous avez un cas d'usage spécifique, fournissez plus de contexte !