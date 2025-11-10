---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Personnaliser les exclusions de recherche dans VS Code
translated: true
type: note
---

Dans VS Code, la recherche globale de fichiers respecte les **exclusions de recherche** que vous configurez. Vous pouvez lui indiquer d'ignorer certains fichiers ou dossiers afin qu'ils n'apparaissent pas dans les résultats de recherche.

Voici les principales méthodes :

---

### 1. Utiliser `search.exclude` dans **settings.json**

Ouvrez vos paramètres (`⌘,` / `Ctrl+,` → en haut à droite "Ouvrir les paramètres (JSON)") et ajoutez :

```json
"search.exclude": {
  "**/node_modules": true,
  "**/dist": true,
  "**/*.log": true
}
```

* Les clés sont des [modèles glob](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options).
* `true` signifie "exclure de la recherche".
* Exemples :

  * `**/node_modules` → tous les dossiers node\_modules
  * `**/*.log` → tous les fichiers `.log` n'importe où
  * `**/build/**` → tout ce qui se trouve dans les dossiers build

---

### 2. Utiliser `.gitignore`

Si votre projet a un fichier `.gitignore`, vous pouvez demander à VS Code de le respecter pendant la recherche :

```json
"search.useIgnoreFiles": true
```

De cette façon, tout ce qui est ignoré par Git n'apparaîtra pas dans les résultats de recherche.

---

### 3. Utiliser `.ignore`

Vous pouvez également créer un fichier `.ignore` à la racine de votre projet (même format que `.gitignore`) spécifiquement pour les outils de l'éditeur. VS Code le respectera si `search.useIgnoreFiles` est activé.

---

### 4. Exclusion rapide dans l'interface de recherche

Lorsque vous effectuez une recherche, survolez un fichier/dossier dans les résultats et cliquez sur **"Exclure"**. Cela ajoute temporairement ce chemin à `search.exclude` dans les paramètres.

---

👉 La configuration la plus courante est donc :

* Ajouter les exclusions générales pour l'ensemble du projet dans `.gitignore`.
* Ajouter les exclusions spécifiques à l'éditeur (comme `dist`, `.vscode`) dans `search.exclude`.

---

Souhaitez-vous que je vous montre comment **exclure uniquement pendant la recherche** tout en conservant ces fichiers dans l'Explorateur, ou également les masquer dans le panneau latéral de l'Explorateur ?