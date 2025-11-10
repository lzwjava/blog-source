---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide Essentiel du Commit Racine Rebase
translated: true
type: note
---

`git rebase --root` est une forme spéciale de rebase qui vous permet de réécrire **tout premier commit** de votre dépôt. Normalement, `git rebase` a besoin d'un commit parent pour effectuer le rebase, mais l'option `--root` traite le commit racine (le premier commit sans parent) comme s'il était également rebasé.

Voici comment cela fonctionne en pratique :

### 1. Rebase standard vs. rebase racine

* **`git rebase` normal** : Vous réappliquez des commits sur une autre branche ou un autre commit, modifiant ainsi l'historique après une base choisie.
* **`git rebase --root`** : Au lieu de commencer après la racine, il réécrit la racine elle-même. Vous pouvez la diviser, la squasher avec des commits ultérieurs, ou même la remplacer complètement.

### 2. Cas d'utilisation typiques

* **Modifier le message du premier commit**
  Si vous souhaitez réécrire le message du tout premier commit de votre projet, vous pouvez exécuter :

  ```bash
  git rebase --root -i
  ```

  et changer `pick` en `reword` pour le premier commit.

* **Squasher la racine avec des commits ultérieurs**
  Par exemple, si votre premier commit n'était qu'une structure (comme un `README`), vous pouvez le squasher dans le commit suivant pour nettoyer l'historique.

* **Diviser le commit racine**
  Si votre premier commit contenait trop de choses (par exemple, un dump complet du code du projet), vous pouvez le diviser en plusieurs commits logiques lors d'un rebase interactif.

### 3. Ce qui se passe en interne

* Git crée un commit parent "factice" temporaire pour le commit racine afin de pouvoir appliquer les opérations de rebase à partir de zéro.
* Chaque commit est rejoué (rebasé) comme si le dépôt avait commencé différemment.
* Vous réécrivez essentiellement les fondations de l'historique de votre dépôt.

### 4. Exemple de workflow

```bash
git rebase --root -i
```

Vous obtiendrez un éditeur comme ceci :

```
pick a1b2c3d Commit initial
pick d4e5f6g Ajouter la fonctionnalité A
pick h7i8j9k Ajouter la fonctionnalité B
```

À partir de là, vous pouvez :

* Changer `pick` en `reword` pour le commit racine → modifier son message.
* Changer `pick` en `squash` → fusionner la racine avec le commit suivant.
* Réorganiser ou diviser selon les besoins.

### ⚠️ Note importante

`git rebase --root` **réécrit l'historique**, il ne doit donc être utilisé que sur des branches qui n'ont pas été poussées/partagées, ou vous devez effectuer un force-push ensuite. Sur les branches partagées, cela peut causer de la confusion et des conflits pour les collaborateurs.

---

Souhaitez-vous que je vous montre également un **exemple concret d'historique avant-après** (avec les hachages de commit) pour que vous puissiez voir exactement comment `git rebase --root` modifie le log ?