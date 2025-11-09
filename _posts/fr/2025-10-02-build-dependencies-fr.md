---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Dépendances de développement et outils de construction
translated: true
type: note
---

### DevDependencies
Ces paquets sont utilisés durant le développement, et ne sont pas inclus dans la build finale.

- **babel-core** (6.13.0) : Compilateur principal Babel pour transpiler le JavaScript moderne (ES6+) en ES5 pour une compatibilité navigateur étendue.
- **babel-loader** (6.2.5) : Loader Webpack qui intègre Babel pour la transformation JavaScript dans les processus de build.
- **babel-plugin-transform-runtime** (6.12.0) : Plugin Babel qui réutilise les helpers d'exécution pour réduire la taille du bundle dans le code transpilé.
- **babel-preset-es2015** (6.13.2) : Présélection Babel pour compiler les fonctionnalités ES2015 (ES6) en ES5.
- **babel-runtime** (6.11.6) : Bibliothèque d'exécution fournissant des polyfills et des helpers pour le code transpilé par Babel.
- **cross-env** (^1.0.8) : Définit les variables d'environnement de manière multiplateforme (par ex., NODE_ENV) sans les différences de shell.
- **css-loader** (^0.23.1) : Charge et traite les fichiers CSS, en résolvant les imports et les dépendances.
- **detect-indent** (4.0.0) : Détecte le style d'indentation (espaces/tabulations) des fichiers pour un formatage cohérent.
- **exports-loader** (^0.6.3) : Rend les exports de modules disponibles dans différents contextes (par ex., pour les modules non-AMD).
- **extract-text-webpack-plugin** (^1.0.1) : Extrait le CSS des bundles JavaScript dans des fichiers séparés pour de meilleures performances.
- **file-loader** (0.9.0) : Gère le chargement de fichiers (par ex., images) en les émettant vers le répertoire de sortie et en renvoyant leurs URLs.
- **html-webpack-plugin** (^2.22.0) : Génère des fichiers HTML et injecte les assets bundle, simplifiant la configuration des applications single-page.
- **rimraf** (^2.5.4) : Suppression récursive de fichiers multiplateforme (comme `rm -rf` sur Unix).
- **style-loader** (^0.13.1) : Injecte le CSS dans le DOM via des balises style pour un chargement dynamique.
- **stylus** (^0.54.5) : Préprocesseur CSS avec une syntaxe expressive, compilé en CSS.
- **stylus-loader** (^2.1.1) : Loader Webpack pour traiter les fichiers Stylus en CSS.
- **url-loader** (0.5.7) : Encode les petits fichiers (par ex., images) en base64 en ligne ou émet les plus gros ; se rabat sur file-loader.
- **vue-hot-reload-api** (^1.2.0) : Active le remplacement de module à chaud (hot module replacement) pour les composants Vue.js durant le développement.
- **vue-html-loader** (^1.0.0) : Loader Webpack pour analyser les modèles HTML dans les composants Vue single-file.
- **vue-loader** (8.5.3) : Charge et traite les composants Vue single-file (fichiers .vue) en JavaScript et CSS.
- **vue-style-loader** (^1.0.0) : Gère le CSS des composants Vue, en s'intégrant avec style-loader.
- **webpack** (1.13.2) : Module bundler pour construire et optimiser les assets web comme le JS, le CSS et les images.
- **webpack-dev-server** (1.14.0) : Serveur de développement avec rechargement à la volée (live reloading) et remplacement de module à chaud.

### Dependencies
Il s'agit des paquets d'exécution inclus dans la build finale de l'application.

- **debug** (^2.2.0) : Utilitaire de débogage avec journalisation par espace de noms et sortie conditionnelle (uniquement activé via la variable d'environnement DEBUG).
- **es6-promise** (^3.0.2) : Polyfill pour l'API Promise ES6 dans les anciens navigateurs/environnements.
- **font-awesome** (^4.6.3) : Bibliothèque d'icônes populaire fournissant des icônes vectorielles évolutives via des classes CSS.
- **github-markdown-css** (^2.4.0) : CSS pour styliser le Markdown de style GitHub.
- **highlight.js** (^9.6.0) : Surligneur de syntaxe pour les blocs de code dans de multiples langages.
- **hls.js** (^0.7.6) : Bibliothèque JavaScript pour lire les vidéos HTTP Live Streaming (HLS) avec la vidéo HTML5.
- **inherit** (^2.2.6) : Utilitaire pour l'héritage classique et prototypal dans les objets JavaScript.
- **jquery** (^3.1.0) : Bibliothèque JavaScript rapide et riche en fonctionnalités pour la manipulation du DOM, AJAX et les événements.
- **json-loader** (^0.5.4) : Charge les fichiers JSON en tant que modules JavaScript.
- **leancloud-realtime** (^3.2.3) : SDK pour le service de messagerie en temps réel et de synchronisation de données de LeanCloud.
- **marked** (^0.3.6) : Analyseur Markdown qui convertit le Markdown en HTML.
- **moment** (^2.14.1) : Bibliothèque de manipulation de date/heure pour analyser, valider et formater les dates.
- **moment-timezone** (^0.5.7) : Extension pour Moment.js pour gérer les fuseaux horaires et l'heure d'été.
- **qiniu-js-sdk** (0.0.2) : SDK JavaScript pour interagir avec le stockage cloud Qiniu (téléversement/téléchargement de fichiers).
- **raw-loader** (^0.5.1) : Loader Webpack qui charge les fichiers sous forme de chaînes brutes (par ex., modèles de texte).
- **rupture** (^0.6.1) : Extension de media query pour Stylus, fournissant des points de rupture pour le design responsive.
- **sprintf-js** (^1.0.3) : Implémentation JavaScript de sprintf pour le formatage de chaînes avec des espaces réservés.
- **vue** (^1.0.26) : Framework MVVM progressif pour construire des interfaces utilisateur (v1.x, version plus ancienne).
- **vue-resource** (^0.6.1) : Client HTTP pour Vue.js pour simplifier les requêtes AJAX/API.
- **vue-router** (^0.7.13) : Routeur officiel pour Vue.js, permettant la navigation d'applications single-page.
- **vue-spinner** (^1.0.2) : Bibliothèque de composants spinner/loading pour Vue.js.
- **vue-weui** (^0.3.2) : Wrappers Vue.js pour les composants WeUI (bibliothèque d'interface utilisateur pour les interfaces de style WeChat).
- **weixin-js-sdk** (^1.2.0) : SDK JavaScript WeChat pour intégrer les fonctionnalités web WeChat (par ex., partage, scan).
- **weui** (^0.4.3) : Framework CSS WeUI pour construire des interfaces mobiles inspirées du design de WeChat.
- **word-color** (^1.2.0) : Bibliothèque pour colorer les mots en fonction de facteurs comme le hachage ou la langue, probablement pour des effets de type heatmap.