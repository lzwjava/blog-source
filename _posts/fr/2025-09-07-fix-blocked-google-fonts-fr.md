---
audio: false
date: 2025-09-07
generated: true
image: false
lang: fr
layout: post
title: Correction de la Requête de Polices Google Bloquées
translated: true
type: note
---

Cette requête provient de votre page qui tente de charger une feuille de style de webfont depuis Google Fonts :

*   **Ce que c'est :** `https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap` est le CSS qui définit les polices **Open Sans**. Votre thème ou votre CSS personnalisé l'inclut pour que le site puît s'afficher avec Open Sans.
*   **Pourquoi vous voyez "Status: — / 0 B / no headers" :** Les DevTools affichent cela lorsque la requête est **bloquée ou annulée** (par ex., par un bloqueur de publicités/de vie privée, une Content-Security-Policy stricte, un réseau instable, ou un blocage au niveau du pays). La page *tente* toujours de la requêter, d'où la ligne dans l'onglet réseau.

### Provenance probable dans un blog Jekyll

L'une de ces options est généralement vraie :

1.  **Le thème l'inclut dans le `<head>`**
    Cherchez une ligne comme
    `<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap" rel="stylesheet">`
    dans `_layouts/default.html` ou `_includes/head.html` (ou l'équivalent du thème si vous utilisez `remote_theme`).

2.  **Le SCSS l'importe**
    Vérifiez dans `/assets/css/*.scss` ou `/_sass/**` la présence de
    `@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap");`

3.  **Un thème distant** (par ex., jekyll-theme-cayman) intègre en dur Google Fonts dans son include `head`. Surcharger le `head` ou la mise en page du thème dans votre dépôt vous permettra de le supprimer.

### Comment le trouver rapidement

Depuis la racine de votre dépôt de site, essayez l'une de ces commandes :

```
rg -n "fonts.googleapis.com"
rg -n "Open Sans"
rg -n "display=swap"
```

### Options pour corriger ou le modifier

**A) Supprimer Google Fonts et utiliser une pile de polices système (plus rapide et respectueux de la vie privée)**

1.  Supprimez la balise `<link>` (ou l'`@import` SCSS) qui appelle Google Fonts.
2.  Dans votre feuille de style principale, définissez une pile système :

    ```css
    html, body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu,
                   "Helvetica Neue", Arial, "Noto Sans", sans-serif,
                   "Apple Color Emoji", "Segoe UI Emoji";
    }
    ```

    (Dans Jekyll, placez ceci dans `assets/css/style.scss` avec des lignes de front-matter `---` en haut.)

**B) Conserver Open Sans mais l'héberger soi-même**

1.  Téléchargez les fichiers WOFF2 pour Open Sans (400 & 700) et placez-les dans `assets/fonts/`.
2.  Ajoutez à votre CSS :

    ```css
    @font-face {
      font-family: "Open Sans";
      font-style: normal;
      font-weight: 400;
      font-display: swap;
      src: url("/assets/fonts/OpenSans-400.woff2") format("woff2");
    }
    @font-face {
      font-family: "Open Sans";
      font-style: normal;
      font-weight: 700;
      font-display: swap;
      src: url("/assets/fonts/OpenSans-700.woff2") format("woff2");
    }
    body { font-family: "Open Sans", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; }
    ```
3.  Supprimez la balise `<link>`/`@import` Google Fonts.

**C) Laisser tel quel mais empêcher l'échec de la requête**

*   Désactivez l'extension de blocage pour votre site, ou assouplissez votre CSP pour autoriser `https://fonts.googleapis.com` et `https://fonts.gstatic.com`.
*   Si vous êtes dans une région où ces domaines sont bloqués, préférez les options A ou B.

### Conseils spécifiques à Jekyll pour la surcharge

*   **Thème distant :** copiez le `/_includes/head.html` ou `/_layouts/default.html` du thème dans votre dépôt avec le même chemin, supprimez la ligne Google Fonts, et Jekyll utilisera votre version.
*   **Include `head` minifié :** parfois le thème injecte les polices via une variable. Si c'est le cas, définissez cette variable comme vide ou surchargez l'include pour exclure les polices.

Si vous partagez le nom de votre thème (ou les valeurs `theme` / `remote_theme` de votre `_config.yml`), je peux indiquer le fichier exact à surcharger et le diff minimal.