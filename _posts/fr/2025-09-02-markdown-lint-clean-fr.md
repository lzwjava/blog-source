---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Lintage Markdown pour des Fichiers Propres et Cohérents
translated: true
type: note
---

Voici une présentation claire et conviviale du projet **markdownlint** par David Anson :

---

## Qu'est-ce que **markdownlint** ?

**markdownlint** est un outil d'analyse statique pour les fichiers Markdown/CommonMark, construit sur Node.js. Son objectif principal est de faire respecter des règles de cohérence et de style dans le contenu Markdown, aidant ainsi les rédacteurs à maintenir un format propre et uniforme et à éviter les constructions qui pourraient se rompre ou s'afficher de manière incohérente selon les analyseurs utilisés ([GitHub][1]).

Inspiré par l'outil Ruby markdownlint (markdownlint/mdl), cet outil s'appuie sur une riche bibliothèque de règles de linting. Il utilise l'analyseur micromark pour la prise en charge de CommonMark et l'étend avec les fonctionnalités de GitHub Flavored Markdown (GFM) comme les tableaux, les liens automatiques, les directives, les notes de bas de page et les formules mathématiques ([GitHub][1]).

## Fonctionnalités principales et intégrations

* **Couverture des règles** : Propose un ensemble complet de règles intégrées, allant des styles de titres et de l'indentation des listes aux espaces de fin de ligne et à la longueur des lignes (par exemple, MD001, MD009, MD013…) ([GitHub][1]).
* **Compatibilité avec l'écosystème** :

  * **Outils en ligne de commande** :

    * `markdownlint-cli` – une interface CLI traditionnelle.
    * `markdownlint-cli2` – une CLI plus rapide, basée sur la configuration, avec des options de formatage flexibles, la prise en charge des globs, des formats de sortie, la correction automatique et l'intégration dans les workflows CI ([GitHub][2], [GitHub][3]).
  * **Extension VS Code** :

    * `vscode‑markdownlint` apporte le linting en temps réel dans votre éditeur. Les violations sont signalées en ligne (soulignées), avec des infobulles au survol et des suggestions de correction rapide ([GitHub][4]).
  * **Action GitHub** :

    * `markdownlint‑cli2‑action` vous permet d'intégrer markdownlint dans votre pipeline CI, activant les vérifications automatiques (et les corrections automatiques optionnelles) pendant les workflows GitHub ([GitHub][5]).

---

## Pourquoi l'utiliser ?

* **Cohérence** : Garantit que les fichiers Markdown adhèrent à un guide de style défini, réduisant la dérive du formatage dans un projet.
* **Aide à l'édition** : Les retours en ligne dans VS Code et autres intégrations rendent l'écriture plus propre et plus rapide.
* **Automatisation** : Utilisez-le dans les pipelines CI avec des outils de lint ou GitHub Actions pour faire respecter les standards avant les fusions.
* **Personnalisable** : Vous pouvez personnaliser les ensembles de règles ou même désactiver des règles via des fichiers de configuration ou des commentaires en ligne (par exemple, désactiver MD013 pour les longues lignes) ([GitHub][5], [Software Recommendations Stack Exchange][6]).

---

Souhaitez-vous un guide de démarrage rapide pour le configurer avec npm, utiliser l'extension VS Code ou l'intégrer dans des workflows CI ?

[1]: https://github.com/DavidAnson/markdownlint?utm_source=chatgpt.com "DavidAnson/markdownlint: A Node.js style checker and lint ..."
[2]: https://github.com/markdownlint/markdownlint?utm_source=chatgpt.com "Markdown lint tool"
[3]: https://github.com/DavidAnson/markdownlint-cli2?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2"
[4]: https://github.com/DavidAnson/vscode-markdownlint?utm_source=chatgpt.com "DavidAnson/vscode-markdownlint: Markdown linting and ..."
[5]: https://github.com/DavidAnson/markdownlint-cli2-action?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2-action"
[6]: https://softwarerecs.stackexchange.com/questions/7138/markdown-lint-tool?utm_source=chatgpt.com "validation - Markdown lint tool"