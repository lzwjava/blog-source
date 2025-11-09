---
audio: false
date: 2025-09-09
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Prévenir le forçage de dépôts sur GitHub
translated: true
type: note
---

Sur GitHub, **vous ne pouvez pas empêcher les utilisateurs de forker un dépôt public**. Le forking est une fonctionnalité essentielle de GitHub pour la collaboration ouverte. Si votre dépôt est public, n'importe qui peut en créer un fork.

Voici vos options en fonction de votre objectif :

### 1. Si vous voulez empêcher complètement le forking

* La seule méthode est de rendre votre dépôt **privé**.
* Les dépôts privés ne peuvent pas être forkés vers des comptes extérieurs.
* Au sein d'une organisation, les administrateurs peuvent contrôler si les dépôts privés peuvent être forkés par d'autres membres.

### 2. Si vous voulez réduire l'exposition tout en restant public

* Vous pouvez **restreindre la licence** : ajoutez une licence qui n'autorise pas la redistribution (par exemple, « Tous droits réservés »). Cela n'empêchera pas techniquement les forks mais vous offrira une protection légale.
* Vous pouvez **désactiver GitHub Pages** et d'autres fonctionnalités d'exposition pour réduire la visibilité.

### 3. Si votre dépôt a déjà été forké

* Vous ne pouvez pas « supprimer » la copie d'un autre utilisateur.
* Vous pouvez uniquement demander au propriétaire du fork de le supprimer, ou déposer une **demande de retrait DMCA** auprès de GitHub s'il viole votre licence ou vos droits.

---

👉 En bref :

* Dépôt public → peut toujours être forké.
* Dépôt privé → protection contre le forking, sauf autorisation explicite au sein de votre organisation.

Voulez-vous que je vous explique **comment rendre un dépôt privé et désactiver le forking interne** ?