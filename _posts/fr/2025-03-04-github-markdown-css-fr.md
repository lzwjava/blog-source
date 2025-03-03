---
audio: false
generated: true
lang: fr
layout: post
title: GitHub et le style Markdown
translated: true
---

### Points Clés
- Il semble probable que pour utiliser le package npm "github-markdown-css", vous devez d'abord l'installer avec `npm install github-markdown-css`.
- La recherche suggère ensuite d'importer le fichier CSS dans votre projet et d'envelopper votre contenu Markdown dans une div avec la classe "markdown-body".
- Les preuves penchent en faveur de la définition d'une largeur et d'un remplissage optionnels pour correspondre au style GitHub, et de s'assurer d'un DOctype pour éviter les problèmes de mise en forme.

### Installation
Commencez par installer le package en utilisant npm dans votre répertoire de projet :
- Exécutez `npm install github-markdown-css` pour l'ajouter à vos dépendances.

### Utilisation
Après l'installation, intégrez le CSS dans votre projet :
- Importez le fichier CSS, par exemple, en JavaScript/React avec `import 'github-markdown-css';`.
- Enveloppez votre contenu Markdown rendu dans un `<div class="markdown-body">...</div>` pour appliquer les styles.
- Optionnellement, ajoutez du CSS pour la largeur et le remplissage pour imiter l'apparence de GitHub :
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
- Assurez-vous que votre HTML inclut un DOctype (par exemple, `<!DOCTYPE html>`) pour éviter les problèmes de mode bizarre, qui pourraient affecter la mise en forme.

### Détail Inattendu
Vous pourriez ne pas vous attendre à ce que le package supporte également la génération de CSS personnalisé via un package associé, [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css), si vous avez besoin de styles personnalisés.

---

### Note de l'Enquête : Guide Complet de l'Utilisation du Package npm github-markdown-css

Ce guide détaillé explore l'utilisation du package npm "github-markdown-css", conçu pour reproduire le style Markdown de GitHub dans les projets web. Il fournit une approche étape par étape pour l'installation et l'intégration, ainsi que des considérations supplémentaires pour une utilisation optimale, notamment dans divers contextes de développement comme React ou HTML pur. Les informations sont dérivées de la documentation officielle du package, des dépôts GitHub et des ressources web associées, garantissant une compréhension approfondie pour les développeurs de tous niveaux.

#### Contexte et Objectif
Le package "github-markdown-css", maintenu par [sindresorhus](https://github.com/sindresorhus), offre un ensemble minimal de CSS pour émuler le style de rendu Markdown de GitHub. Cela est particulièrement utile pour les développeurs qui souhaitent que leur contenu Markdown, tel que la documentation ou les billets de blog, apparaisse de manière cohérente avec la présentation propre et familière de GitHub. Le package est largement utilisé, avec plus de 1 168 autres projets dans le registre npm l'utilisant, ce qui indique sa popularité et sa fiabilité selon les mises à jour récentes.

#### Processus d'Installation
Pour commencer, vous devez installer le package via npm, le gestionnaire de packages Node.js. La commande est simple :
- Exécutez `npm install github-markdown-css` dans votre répertoire de projet. Cela ajoute le package à votre dossier `node_modules` et met à jour votre `package.json` avec la dépendance.

La dernière version du package, selon les vérifications récentes, est 5.8.1, publiée il y a environ trois mois, ce qui suggère une maintenance et des mises à jour actives. Cela garantit la compatibilité avec les pratiques modernes de développement web et les frameworks.

#### Intégration et Utilisation
Une fois installé, l'étape suivante consiste à intégrer le CSS dans votre projet. Le package fournit un fichier nommé `github-markdown.css`, que vous pouvez importer en fonction de la configuration de votre projet :

- **Pour JavaScript/Frameworks Modernes (par exemple, React, Vue) :**
  - Utilisez une instruction d'importation dans vos fichiers JavaScript ou TypeScript, comme `import 'github-markdown-css';`. Cela fonctionne bien avec des bundlers comme Webpack ou Vite, qui gèrent les imports CSS de manière transparente.
  - Pour React, vous pourriez voir des exemples où les développeurs l'importent dans un fichier de composant, garantissant que les styles sont disponibles globalement ou selon les besoins.

- **Pour HTML Pur :**
  - Liez le fichier CSS directement dans la section head de votre HTML :
    ```html
    <link rel="stylesheet" href="node_modules/github-markdown-css/github-markdown.css">
    ```
  - Notez que le chemin peut varier en fonction de la structure de votre projet ; assurez-vous que le chemin relatif pointe correctement vers le dossier `node_modules`.

Après l'importation, appliquez les styles en enveloppant votre contenu Markdown rendu dans un `<div>` avec la classe "markdown-body". Par exemple :
```html
<div class="markdown-body">
  <h1>Licornes</h1>
  <p>Toutes les choses</p>
</div>
```
Cette classe est cruciale car le CSS cible les éléments au sein de `.markdown-body` pour appliquer un style similaire à GitHub, y compris la typographie, les blocs de code, les tableaux, et plus encore.

#### Considérations de Mise en Forme
Pour reproduire pleinement l'apparence Markdown de GitHub, envisagez de définir la largeur et le remplissage pour la classe `.markdown-body`. La documentation suggère :
- Une largeur maximale de 980px, avec 45px de remplissage sur les grands écrans, et 15px de remplissage sur les appareils mobiles (écrans ≤ 767px).
- Vous pouvez obtenir cela avec le CSS suivant :
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
Cela garantit la réactivité et s'aligne sur la conception de GitHub, améliorant la lisibilité et l'expérience utilisateur.

#### Notes Techniques et Bonnes Pratiques
- **Exigence de DOctype :** La documentation met en évidence des problèmes de mise en forme potentiels, tels que les tableaux en mode sombre qui se rendent incorrectement, si le navigateur entre en mode bizarre. Pour éviter cela, incluez toujours un DOctype en haut de votre HTML, tel que `<!DOCTYPE html>`. Cela garantit un rendu conforme aux normes et évite un comportement inattendu.
- **Analyse Markdown :** Bien que le package fournisse du CSS, il ne parse pas le Markdown en HTML. Vous aurez besoin d'un analyseur Markdown comme [marked.js](https://marked.js.org/) ou [react-markdown](https://github.com/remarkjs/react-markdown) pour les projets React pour convertir le texte Markdown en HTML, qui peut ensuite être stylisé avec ce CSS.
- **Génération de CSS Personnalisé :** Pour les utilisateurs avancés, le package associé [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) permet de générer du CSS personnalisé, potentiellement utile pour un thème spécifique ou des modifications. C'est un détail inattendu pour ceux qui pourraient supposer que le package est uniquement pour une utilisation directe.

#### Utilisation dans des Contextes Spécifiques
- **Projets React :** Dans React, la combinaison de `github-markdown-css` avec `react-markdown` est courante. Après avoir installé les deux, importez le CSS et utilisez le composant :
  ```javascript
  import React from 'react';
  import ReactMarkdown from 'react-markdown';
  import 'github-markdown-css';

  const MarkdownComponent = () => (
    <div className="markdown-body">
      <ReactMarkdown># Bonjour, Monde !</ReactMarkdown>
    </div>
  );
  ```
  Assurez-vous également de définir le CSS de largeur et de remplissage comme montré précédemment pour un style GitHub complet.

- **HTML Pur avec CDN :** Pour un prototypage rapide, vous pouvez utiliser une version CDN, disponible sur [cdnjs](https://cdnjs.com/libraries/github-markdown-css), en liant directement :
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css">
  ```
  Ensuite, appliquez la classe `.markdown-body` comme précédemment.

#### Problèmes Potentiels et Solutions
- **Conflits de Mise en Forme :** Si votre projet utilise d'autres frameworks CSS (par exemple, Tailwind, Bootstrap), assurez-vous qu'il n'y a pas de conflits de spécificité. La classe `.markdown-body` devrait remplacer la plupart des styles, mais testez soigneusement.
- **Support du Mode Sombre :** Le package inclut le support du mode sombre, mais assurez-vous que votre analyseur Markdown et la configuration de votre projet gèrent correctement la commutation de thème, en particulier pour les blocs de code et les tableaux.
- **Compatibilité des Navigateurs :** Étant donné l'utilisation généralisée du package, la compatibilité est généralement bonne, mais testez toujours sur les principaux navigateurs (Chrome, Firefox, Safari) pour garantir un rendu cohérent.

#### Analyse Comparative
Par rapport à d'autres options de CSS Markdown, comme [Markdown CSS](https://markdowncss.github.io/), "github-markdown-css" se distingue par sa réplication directe du style GitHub, le rendant idéal pour la documentation reflétant l'apparence de GitHub. Cependant, il manque d'options de thème intégrées sans personnalisation supplémentaire, contrairement à certaines alternatives qui offrent plusieurs thèmes hors de la boîte.

#### Tableau : Fonctionnalités Clés et Considérations

| Fonctionnalité                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Commande d'Installation     | `npm install github-markdown-css`                                           |
| Méthode d'Importation CSS        | `import 'github-markdown-css';` ou `<link>` dans HTML                         |
| Classe Requise           | `.markdown-body` pour l'application des styles                                    |
| Largeur et Remplissage        | Max 980px, 45px de remplissage (desktop) ; 15px de remplissage (mobile ≤ 767px)            |
| Exigence de DOctype      | Essentielle pour éviter le mode bizarre et garantir un rendu correct                  |
| Génération de CSS Personnalisé    | Possible via [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) |
| Compatibilité            | Fonctionne avec les analyseurs Markdown comme marked.js, react-markdown ; large support des navigateurs |

#### Conclusion
L'utilisation de "github-markdown-css" est simple pour les développeurs cherchant à reproduire le style Markdown de GitHub. En suivant les étapes d'installation et d'intégration, et en tenant compte des notes supplémentaires de mise en forme et techniques, vous pouvez obtenir une apparence cohérente et professionnelle pour votre contenu Markdown. Pour une personnalisation avancée, explorez le package de génération, et testez toujours pour les problèmes de compatibilité et de rendu, surtout dans les projets complexes.

#### Citations Clés
- [Page du package npm github-markdown-css](https://www.npmjs.com/package/github-markdown-css)
- [Le minimum de CSS pour reproduire le style Markdown de GitHub dépôt GitHub](https://github.com/sindresorhus/github-markdown-css)
- [Page de démonstration GitHub Markdown CSS](https://sindresorhus.com/github-markdown-css/)
- [Générer le CSS pour le package npm github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css)
- [github-markdown-css CDN par cdnjs](https://cdnjs.com/libraries/github-markdown-css)