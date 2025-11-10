---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Ordre de la Fusion de Squash Git Expliqué
translated: true
type: note
---

Lorsque vous exécutez `git rebase -i` (rebase interactif) pour squasher des commits, Git suit un ordre et une logique très spécifiques :

---

### 1. Ordre par défaut

Lorsque vous démarrez un rebase interactif (par exemple, `git rebase -i HEAD~5`), Git ouvre votre éditeur avec les **commits listés du plus ancien au plus récent** (haut = plus ancien, bas = plus récent).
L'ordre est important : c'est la séquence que Git va tenter de rejouer sur la nouvelle base.

---

### 2. Pick vs. Squash

* **pick** → conserve le commit tel quel.
* **squash (ou s)** → combine ce commit avec le **commit précédent marqué comme `pick`**.
* **fixup (ou f)** → identique à squash, mais ignore le message de commit (ne conserve que le message du premier commit).

Ainsi, si vous écrivez :

```
pick  a1b2c3  Fonctionnalité initiale
squash d4e5f6  Correction mineure
squash g7h8i9  Nettoyage mineur
pick  j1k2l3  Autre fonctionnalité
```

Git fusionnera `d4e5f6` et `g7h8i9` dans `a1b2c3`, produisant un seul commit.

---

### 3. Réorganisation des commits

Vous pouvez **réorganiser les commits directement dans l'éditeur de rebase** en déplaçant les lignes vers le haut ou vers le bas.
Par exemple :

```
pick  a1b2c3  Fonctionnalité initiale
pick  j1k2l3  Autre fonctionnalité
squash d4e5f6  Correction mineure
squash g7h8i9  Nettoyage mineur
```

Ici, Git appliquera d'abord `a1b2c3`, puis `j1k2l3`.
Les commits `squash` (`d4e5f6` et `g7h8i9`) seront maintenant squashés dans **`j1k2l3`**, car squash fusionne toujours dans le `pick` précédent le plus récent.

---

### 4. Édition des messages

Après le squash, Git marque une pause et vous permet de **modifier le message de commit** pour le commit squashé. Vous pouvez :

* Conserver tous les messages.
* Les combiner manuellement.
* Ne conserver que le premier.

---

### 5. Pièges courants

* Si vous placez `squash` comme tout premier commit (aucun `pick` avant), Git générera une erreur — il a besoin d'un commit de base dans lequel squasher.
* Si les commits entrent en conflit après une réorganisation, vous devrez résoudre les conflits manuellement pendant le rebase.
* La réorganisation peut changer l'historique de manière significative ; ne le faites que sur des branches que vous n'avez pas encore poussées/partagées, à moins d'être sûr de vouloir réécrire l'historique.

---

✅ En bref :

* Les commits sont listés **du plus ancien au plus récent**.
* `pick` conserve, `squash` fusionne dans le **`pick` antérieur le plus proche**.
* Vous pouvez réorganiser les commits manuellement dans l'éditeur ; squash attache toujours les commits suivants au commit pické précédent.

---

Souhaitez-vous que j'illustre cela avec un **exemple d'historique de commits avant/après** (montrant `git log --oneline` avant et après le squash) ? Cela rend généralement l'ordre plus clair.