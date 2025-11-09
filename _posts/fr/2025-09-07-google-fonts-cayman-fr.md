---
audio: false
date: 2025-09-07
generated: true
image: false
lang: fr
layout: post
title: Importation de Google Fonts dans le thème Cayman
translated: true
type: note
---

Oui — c’est très probablement la raison.

Lorsque vous écrivez :

```scss
@import "jekyll-theme-cayman";
```

vous n'importez pas simplement un fichier SCSS local — vous importez la **feuille de style complète du thème**, qui contient elle-même (ou référence) l'importation des Google Fonts. Cayman utilise **Open Sans** comme police par défaut, et la récupère depuis `https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap`.

Le flux est donc le suivant :

1. Votre SCSS contient `@import "jekyll-theme-cayman";`.
2. Jekyll développe cela dans les fichiers `_sass` du thème.
3. Dans le SCSS de Cayman, il y a une ligne comme :

   ```scss
   @import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap");
   ```
4. C'est la requête réseau que vous voyez dans les DevTools.

---

### Comment supprimer ou remplacer

* **Remplacer l'importation de police** : Copiez le SCSS principal du thème dans votre projet (par exemple `assets/css/style.scss`), supprimez la ligne Google Fonts, et indiquez à Jekyll de ne pas l'importer.

* **Simplement remplacer la famille de polices** : Gardez le reste de Cayman mais imposez une stack de polices système dans votre propre CSS :

  ```css
  html, body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu,
                 "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  }
  ```

  Même si la requête Google Fonts a lieu, le navigateur ne l'utilisera pas.

* **Auto-héberger Open Sans** : Si vous aimez Open Sans mais ne voulez pas d'appel externe, téléchargez les fichiers de police et définissez-les avec `@font-face` dans votre propre CSS, puis supprimez le `@import url(...)` de Cayman.

---

👉 Si vous voulez, je peux vous montrer exactement quel fichier SCSS de Cayman contient la ligne Google Fonts et comment la remplacer proprement dans votre configuration Jekyll. Voulez-vous que je vous guide étape par étape ?