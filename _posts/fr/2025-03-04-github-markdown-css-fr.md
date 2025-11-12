---
audio: false
generated: true
lang: fr
layout: post
title: Stylage Markdown de GitHub
translated: true
type: note
---

### Points Clés
- Il semble probable que pour utiliser le package npm "github-markdown-css", vous devez d'abord l'installer avec `npm install github-markdown-css`.
- Les recherches suggèrent que vous devez ensuite importer le fichier CSS dans votre projet et envelopper votre contenu Markdown dans une div avec la classe "markdown-body".
- Les preuves indiquent qu'il est conseillé de définir une largeur et un padding optionnels pour correspondre au style de GitHub, et de s'assurer d'avoir un DOctype pour éviter les problèmes de style.

### Installation
Commencez par installer le package en utilisant npm dans votre répertoire de projet :
- Exécutez `npm install github-markdown-css` pour l'ajouter à vos dépendances.

### Utilisation
Après l'installation, intégrez le CSS dans votre projet :
- Importez le fichier CSS, par exemple, en JavaScript/React avec `import 'github-markdown-css';`.
- Enveloppez votre contenu Markdown rendu dans une `<div class="markdown-body">...</div>` pour appliquer les styles.
- Optionnellement, ajoutez du CSS pour la largeur et le padding afin d'imiter l'apparence de GitHub :
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
- Assurez-vous que votre HTML inclut un DOctype (par exemple, `<!DOCTYPE html>`) pour empêcher les problèmes de mode de compatibilité (quirks mode), qui pourraient affecter le style.

### Détail Inattendu
Vous pourriez ne pas vous attendre à ce que le package prenne également en charge la génération de CSS personnalisé via un package associé, [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css), si vous avez besoin de styles sur mesure.

---

### Note d'Enquête : Guide Complet sur l'Utilisation du Package npm github-markdown-css

Ce guide détaillé explore l'utilisation du package npm "github-markdown-css", conçu pour reproduire le style de rendu Markdown de GitHub dans les projets web. Il fournit une approche étape par étape pour l'installation et l'intégration, ainsi que des considérations supplémentaires pour une utilisation optimale, en particulier dans divers contextes de développement comme React ou le HTML simple. Les informations sont tirées de la documentation officielle du package, des dépôts GitHub et de ressources web connexes, assurant une compréhension approfondie pour les développeurs de tous niveaux.

#### Contexte et Objectif
Le package "github-markdown-css", maintenu par [sindresorhus](https://github.com/sindresorhus), offre un ensemble minimal de CSS pour imiter le style de rendu Markdown de GitHub. Ceci est particulièrement utile pour les développeurs qui souhantent que leur contenu Markdown, tel que la documentation ou les articles de blog, apparaisse cohérent avec la présentation familière et épurée de GitHub. Le package est largement utilisé, avec plus de 1 168 autres projets dans le registre npm l'utilisant, ce qui indique sa popularité et sa fiabilité selon les mises à jour récentes.

#### Processus d'Installation
Pour commencer, vous devez installer le package via npm, le gestionnaire de packages Node.js. La commande est simple :
- Exécutez `npm install github-markdown-css` dans votre répertoire de projet. Ceci ajoute le package à votre dossier `node_modules` et met à jour votre `package.json` avec la dépendance.

La dernière version du package, selon des vérifications récentes, est la 5.8.1, publiée pour la dernière fois il y a environ trois mois, ce qui suggère une maintenance et des mises à jour actives. Ceci assure la compatibilité avec les pratiques modernes de développement web et les frameworks.

#### Intégration et Utilisation
Une fois installé, l'étape suivante consiste à intégrer le CSS dans votre projet. Le package fournit un fichier nommé `github-markdown.css`, que vous pouvez importer en fonction de la configuration de votre projet :

- **Pour les Frameworks JavaScript/Modernes (ex. React, Vue) :**
  - Utilisez une instruction d'import dans vos fichiers JavaScript ou TypeScript, telle que `import 'github-markdown-css';`. Ceci fonctionne bien avec des bundlers comme Webpack ou Vite, qui gèrent les imports CSS de manière transparente.
  - Pour React, vous pourriez voir des exemples où les développeurs l'importent dans un fichier de composant, assurant que les styles sont disponibles globalement ou de manière scopée selon les besoins.

- **Pour le HTML Simple :**
  - Liez le fichier CSS directement dans la section head de votre HTML :
    ```html
    <link rel="stylesheet" href="node_modules/github-markdown-css/github-markdown.css">
    ```
  - Notez que le chemin peut varier selon la structure de votre projet ; assurez-vous que le chemin relatif pointe correctement vers le répertoire `node_modules`.

Après l'importation, appliquez les styles en enveloppant votre contenu Markdown rendu dans une `<div>` avec la classe "markdown-body". Par exemple :
```html
<div class="markdown-body">
  <h1>Licornes</h1>
  <p>Toutes les choses</p>
</div>
```
Cette classe est cruciale car le CSS cible les éléments à l'intérieur de `.markdown-body` pour appliquer un style similaire à GitHub, incluant la typographie, les blocs de code, les tableaux, et plus encore.

#### Considérations de Style
Pour reproduire complètement l'apparence Markdown de GitHub, envisagez de définir la largeur et le padding pour la classe `.markdown-body`. La documentation suggère :
- Une largeur maximale de 980px, avec un padding de 45px sur les écrans plus larges, et un padding de 15px sur les appareils mobiles (écrans ≤ 767px).
- Vous pouvez y parvenir avec le CSS suivant :
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
Ceci assure la réactivité et s'aligne avec le design de GitHub, améliorant la lisibilité et l'expérience utilisateur.

#### Notes Techniques et Bonnes Pratiques
- **Exigence de DOctype :** La documentation met en lumière des problèmes de style potentiels, tels qu'un rendu incorrect des tableaux en mode sombre, si le navigateur entre en mode de compatibilité (quirks mode). Pour empêcher cela, incluez toujours un DOctype en haut de votre HTML, tel que `<!DOCTYPE html>`. Ceci assure un rendu conforme aux standards et évite les comportements inattendus.
- **Analyse Syntaxique Markdown :** Bien que le package fournisse le CSS, il n'analyse pas le Markdown en HTML. Vous aurez besoin d'un analyseur Markdown comme [marked.js](https://marked.js.org/) ou [react-markdown](https://github.com/remarkjs/react-markdown) pour les projets React afin de convertir le texte Markdown en HTML, qui peut ensuite être stylisé avec ce CSS.
- **Génération de CSS Personnalisé :** Pour les utilisateurs avancés, le package associé [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) permet de générer du CSS personnalisé, potentiellement utile pour un thème spécifique ou des modifications. C'est un détail inattendu pour ceux qui pourraient supposer que le package est uniquement pour une utilisation directe.

#### Utilisation dans des Contextes Spécifiques
- **Projets React :** Dans React, combiner `github-markdown-css` avec `react-markdown` est courant. Après avoir installé les deux, importez le CSS et utilisez le composant :
  ```javascript
  import React from 'react';
  import ReactMarkdown from 'react-markdown';
  import 'github-markdown-css';

  const MarkdownComponent = () => (
    <div className="markdown-body">
      <ReactMarkdown># Bonjour, le Monde !</ReactMarkdown>
    </div>
  );
  ```
  Assurez-vous de également définir le CSS de largeur et de padding comme montré précédemment pour un style GitHub complet.

- **HTML Simple avec CDN :** Pour un prototypage rapide, vous pouvez utiliser une version CDN, disponible sur [cdnjs](https://cdnjs.com/libraries/github-markdown-css), en la liant directement :
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css">
  ```
  Appliquez ensuite la classe `.markdown-body` comme auparavant.

#### Problèmes Potentiels et Solutions
- **Conflits de Style :** Si votre projet utilise d'autres frameworks CSS (ex. Tailwind, Bootstrap), assurez-vous qu'il n'y a pas de conflits de spécificité. La classe `.markdown-body` devrait remplacer la plupart des styles, mais testez minutieusement.
- **Prise en Charge du Mode Sombre :** Le package inclut la prise en charge du mode sombre, mais assurez-vous que votre analyseur Markdown et la configuration de votre projet gèrent correctement le changement de thème, en particulier pour les blocs de code et les tableaux.
- **Compatibilité du Navigateur :** Étant donné l'utilisation répandue du package, la compatibilité est généralement bonne, mais testez toujours sur les principaux navigateurs (Chrome, Firefox, Safari) pour assurer un rendu cohérent.

#### Analyse Comparative
Comparé à d'autres options de CSS Markdown, comme [Markdown CSS](https://markdowncss.github.io/), "github-markdown-css" se distingue par sa réplication directe du style de GitHub, le rendant idéal pour une documentation reflétant l'apparence de GitHub. Cependant, il manque d'options de thème intégrées sans personnalisation supplémentaire, contrairement à certaines alternatives qui offrent plusieurs thèmes prêts à l'emploi.

#### Tableau : Fonctionnalités Clés et Considérations

| Fonctionnalité                  | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| Commande d'Installation          | `npm install github-markdown-css`                                           |
| Méthode d'Import CSS             | `import 'github-markdown-css';` ou `<link>` en HTML                         |
| Classe Requise                   | `.markdown-body` pour l'application du style                                |
| Largeur et Padding               | Max 980px, padding 45px (bureau) ; padding 15px (mobile ≤ 767px)            |
| Exigence de DOctype              | Essentiel pour éviter le mode de compatibilité et assurer un rendu correct  |
| Génération de CSS Personnalisé   | Possible via [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) |
| Compatibilité                    | Fonctionne avec les analyseurs Markdown comme marked.js, react-markdown ; large support des navigateurs |

#### Conclusion
Utiliser "github-markdown-css" est simple pour les développeurs cherchant à reproduire le style Markdown de GitHub. En suivant les étapes d'installation et d'intégration, et en considérant les notes techniques et de style supplémentaires, vous pouvez obtenir un aspect cohérent et professionnel pour votre contenu Markdown. Pour une personnalisation avancée, explorez le package de génération, et testez toujours pour les problèmes de compatibilité et de rendu, en particulier dans les projets complexes.

#### Citations Clés
- [Page du package npm github-markdown-css](https://www.npmjs.com/package/github-markdown-css)
- [Le dépôt GitHub : The minimal amount of CSS to replicate GitHub Markdown style](https://github.com/sindresorhus/github-markdown-css)
- [Page de démonstration GitHub Markdown CSS](https://sindresorhus.com/github-markdown-css/)
- [Package npm pour générer le CSS pour github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css)
- [CDN github-markdown-css par cdnjs](https://cdnjs.com/libraries/github-markdown-css)