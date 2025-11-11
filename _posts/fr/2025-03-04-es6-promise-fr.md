---
audio: false
generated: true
lang: fr
layout: post
title: Promesses de style ES6
translated: true
type: note
---

### Points clés
- Pour utiliser le package `es6-promise` dans npm, commencez par l'installer avec `npm install es6-promise`.
- Vous pouvez ensuite le require dans votre code JavaScript pour utiliser la classe Promise localement ou polyfill la Promise globale pour une compatibilité élargie.
- Les recherches suggèrent que les environnements modernes prennent en charge les promesses natives, ce package est donc principalement destiné aux systèmes plus anciens ou à des besoins spécifiques.

### Installation
Commencez par installer le package en utilisant npm dans le répertoire de votre projet :
- Exécutez la commande : `npm install es6-promise`.

### Utilisation
Vous avez deux options principales pour utiliser le package :

#### Utilisation locale
Si vous souhaitez utiliser la classe Promise dans votre code sans affecter la portée globale :
- Require le package et utilisez-le comme ceci :
  ```javascript
  const Promise = require('es6-promise').Promise;
  // Puis utilisez Promise comme nécessaire, par exemple : new Promise((resolve, reject) => {...});
  ```

#### Polyfill global
Pour vous assurer que la Promise globale est définie sur l'implémentation `es6-promise`, en particulier pour les environnements plus anciens :
- Utilisez la méthode de polyfill :
  ```javascript
  require('es6-promise').polyfill();
  // Désormais, la Promise globale utilisera l'implémentation es6-promise.
  ```
- Alternativement, pour un polyfill automatique, vous pouvez faire :
  ```javascript
  require('es6-promise/auto');
  ```

### Détail inattendu
Notez que `es6-promise` n'a pas été mis à jour depuis plus de six ans, ce qui pourrait soulever des inquiétudes concernant la sécurité et la compatibilité avec les nouvelles fonctionnalités JavaScript, bien qu'il reste fonctionnel pour son usage prévu.

---

### Note d'enquête : Exploration détaillée de l'utilisation du package `es6-promise` dans npm

Cette section fournit une vue d'ensemble complète de l'utilisation du package `es6-promise` dans un projet npm, développant la réponse directe avec un contexte supplémentaire, des détails techniques et des considérations pour les développeurs. Les informations sont structurées pour imiter un article professionnel, en s'assurant que tous les détails pertinents de l'analyse sont inclus, avec des tableaux pour plus de clarté le cas échéant.

#### Introduction à `es6-promise`
Le package `es6-promise` est une bibliothèque légère conçue comme un polyfill pour les Promesses de style ES6, fournissant des outils pour organiser le code asynchrone. Il est particulièrement utile dans les environnements où la prise en charge native des Promesses ES6 est absente ou peu fiable, tels que les anciens navigateurs ou les versions legacy de Node.js. Étant donné que sa dernière mise à jour remonte à 2019, avec la dernière version 4.2.8 publiée il y a six ans à la date du 3 mars 2025, il s'agit d'une solution mature mais potentiellement moins maintenue par rapport aux alternatives modernes.

#### Processus d'installation
Pour intégrer `es6-promise` dans votre projet, l'installation via npm est simple. La commande est :
- `npm install es6-promise`

Cela installe le package dans votre répertoire `node_modules` et met à jour votre `package.json` avec la dépendance. Pour ceux qui utilisent Yarn, une alternative est `yarn add es6-promise`, bien que npm soit l'objectif ici étant donné la requête de l'utilisateur.

| Méthode d'installation | Commande                     |
|---------------------|-----------------------------|
| npm                 | `npm install es6-promise`   |
| Yarn                | `yarn add es6-promise`      |

Le package a été largement adopté, avec 5 528 autres projets dans le registre npm l'utilisant, indiquant sa pertinence dans des cas d'utilisation legacy ou spécifiques.

#### Utilisation en JavaScript
Une fois installé, `es6-promise` peut être utilisé de deux manières principales : localement dans votre code ou comme un polyfill global. Le choix dépend des besoins de votre projet, en particulier si vous devez assurer la compatibilité entre différents environnements.

##### Utilisation locale
Pour une utilisation locale, vous require le package et accédez directement à la classe Promise. La syntaxe est :
- `const Promise = require('es6-promise').Promise;`

Cela vous permet d'utiliser la classe Promise dans votre code sans modifier la portée globale. Par exemple :
```javascript
const Promise = require('es6-promise').Promise;
const myPromise = new Promise((resolve, reject) => {
  resolve('Succès !');
});
myPromise.then(result => console.log(result)); // Affiche : Succès !
```

Cette approche est adaptée si votre projet prend déjà en charge les promesses natives mais que vous souhaitez utiliser `es6-promise` pour des opérations spécifiques ou pour la cohérence.

##### Polyfill global
Pour polyfill l'environnement global, en s'assurant que toute utilisation de Promise dans votre projet utilise l'implémentation `es6-promise`, vous pouvez appeler la méthode de polyfill :
- `require('es6-promise').polyfill();`

Cela définit la `Promise` globale sur l'implémentation `es6-promise`, ce qui est utile pour les environnements plus anciens comme IE<9 ou les versions legacy de Node.js où les promesses natives pourraient être manquantes ou défaillantes. Alternativement, pour un polyfill automatique, vous pouvez utiliser :
- `require('es6-promise/auto');`

La version "auto", avec une taille de fichier de 27,78 Ko (7,3 Ko gzippé), fournit ou remplace automatiquement la `Promise` si elle est manquante ou défaillante, simplifiant la configuration. Par exemple :
```javascript
require('es6-promise/auto');
// Désormais, la Promise globale est polyfillée, et vous pouvez utiliser new Promise(...) n'importe où dans votre code.
```

##### Utilisation dans le navigateur
Bien que la requête de l'utilisateur se concentre sur npm, il est bon de noter que pour les environnements de navigateur, vous pouvez inclure `es6-promise` via CDN, comme :
- `<script src="https://cdn.jsdelivr.net/npm/es6-promise@4/dist/es6-promise.js"></script>`
- Les versions minifiées comme `es6-promise.min.js` sont également disponibles pour la production.

Cependant, étant donné le contexte npm, l'accent reste mis sur l'utilisation avec Node.js.

#### Compatibilité et considérations
Le package est un sous-ensemble de rsvp.js, extrait par @jakearchibald, et est conçu pour imiter le comportement des Promesses ES6. Cependant, il y a des notes de compatibilité à considérer :
- Dans IE<9, `catch` et `finally` sont des mots-clés réservés, provoquant des erreurs de syntaxe. Les solutions de contournement incluent l'utilisation de la notation entre crochets, par exemple `promise['catch'](function(err) { ... });`, bien que la plupart des minifiers corrigent cela automatiquement.
- Étant donné que sa dernière mise à jour remonte à 2019, les développeurs doivent évaluer si `es6-promise` répond aux besoins actuels de sécurité et de compatibilité, en particulier pour les projets ciblant les environnements JavaScript modernes où les promesses natives sont prises en charge.

L'analyse de santé du package npm indique qu'il reçoit plus de 9,5 millions de téléchargements par semaine et est considéré comme un projet clé de l'écosystème, avec 7 290 étoiles GitHub, suggérant une forte communauté historique. Cependant, sans nouvelle version au cours des 12 derniers mois, il peut être considéré comme un projet discontinué, bien que la maintenance soit évaluée comme durable sur la base de l'activité du dépôt.

#### TypeScript et ressources supplémentaires
Pour les utilisateurs de TypeScript, bien que non explicitement mentionné dans la requête, notez que les définitions de type sont disponibles via `@types/es6-promise`, installables avec `npm i @types/es6-promise`. Il s'agit d'un package stub, car `es6-promise` fournit ses propres types, mais il est utile pour assurer la sécurité de type.

Pour en apprendre davantage sur les promesses, la documentation recommande l'article [JavaScript Promises HTML5Rocks](http://www.html5rocks.com/en/tutorials/es6/promises/), qui fournit une utilisation détaillée de l'API et des modèles.

#### Pièges potentiels et insights de la communauté
Certains utilisateurs peuvent rencontrer des problèmes d'installation, tels que des erreurs 404, en particulier sur les systèmes plus anciens ou si les dépendances sont mal configurées. Par exemple, vider `node_modules` et réinstaller peut résoudre de tels problèmes, comme observé dans les discussions de la communauté. De plus, assurez-vous que votre version de Node.js prend en charge les CommonJS requires, étant donné la structure du package.

#### Conclusion
En résumé, `es6-promise` est un outil précieux pour assurer la compatibilité des Promesses ES6 dans les projets npm, en particulier pour les environnements legacy. L'installation est simple avec `npm install es6-promise`, et l'utilisation peut être locale via `require('es6-promise').Promise` ou globale via `require('es6-promise').polyfill()` ou `require('es6-promise/auto')`. Étant donné son âge, évaluez son adéquation aux besoins de votre projet, en particulier dans les contextes JavaScript modernes où les promesses natives sont standard.

#### Citations clés
- [Détails du package npm es6-promise](https://www.npmjs.com/package/es6-promise)
- [Dépôt GitHub es6-promise](https://github.com/stefanpenner/es6-promise)