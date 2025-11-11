---
audio: false
generated: true
lang: fr
layout: post
title: Source d'installation des packages npm
translated: true
type: note
---

Pour changer la source d'installation du package `@ngx-formly/bootstrap` d'un fichier local `.tgz` vers le registre npm, suivez ces étapes :

### 1. Désinstaller le package installé localement
Étant donné que vous avez précédemment installé `@ngx-formly/bootstrap` à partir d'un fichier local `.tgz`, il se trouve actuellement dans le répertoire `node_modules` de votre projet. Pour le supprimer, exécutez la commande suivante dans votre terminal :

```bash
npm uninstall @ngx-formly/bootstrap
```

Cette commande supprime le package de `node_modules`. Si le package a été ajouté manuellement à votre fichier `package.json` sous `dependencies` ou `devDependencies`, cela le supprimera également de là. S'il n'était pas listé dans `package.json` (ce qui est courant lors de l'installation à partir d'un fichier `.tgz` sans sauvegarde), il sera quand même supprimé de votre projet.

### 2. Installer le package depuis le registre npm
Maintenant, installez le package depuis le registre npm en exécutant :

```bash
npm install @ngx-formly/bootstrap
```

Cette commande récupère la dernière version de `@ngx-formly/bootstrap` depuis le registre npm (généralement `https://registry.npmjs.org/` sauf si vous avez configuré un registre différent) et l'installe dans votre répertoire `node_modules`. Elle ajoutera également le package à votre fichier `package.json` sous `dependencies` par défaut (dans les versions récentes de npm), garantissant qu'il est suivi comme faisant partie de votre projet.

### Optionnel : Vérifier le registre (si nécessaire)
Si vous avez précédemment modifié votre registre npm et souhaitez vous assurer qu'il est défini sur le registre npm par défaut, vous pouvez le vérifier avec :

```bash
npm config get registry
```

Si le résultat est `https://registry.npmjs.org/`, vous utilisez le registre par défaut, et la commande `npm install` fonctionnera comme prévu. S'il est défini sur un registre différent et que vous souhaitez revenir au défaut, exécutez :

```bash
npm config set registry https://registry.npmjs.org/
```

Cependant, puisque vous avez mentionné avoir déjà configuré votre registre, cette étape peut ne pas être nécessaire.

### Notes
- **Contrôle de version** : Si vous avez besoin de la même version que celle dans votre fichier `.tgz`, vérifiez le numéro de version dans `node_modules/@ngx-formly/bootstrap/package.json` avant de désinstaller. Ensuite, installez cette version spécifique avec :
  ```bash
  npm install @ngx-formly/bootstrap@<version>
  ```
  Si vous ne spécifiez pas de version, la dernière version du registre sera installée.
- **Type de dépendance** : Si vous souhaitez que le package soit une dépendance de développement plutôt qu'une dépendance régulière, utilisez :
  ```bash
  npm install @ngx-formly/bootstrap --save-dev
  ```

En suivant ces étapes, vous réussirez à basculer `@ngx-formly/bootstrap` d'une installation via un fichier local `.tgz` à une installation depuis le registre npm.