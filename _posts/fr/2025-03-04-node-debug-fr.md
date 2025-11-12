---
audio: false
generated: true
lang: fr
layout: post
title: Débogage dans Node.js avec le Package Debug
translated: true
type: note
---

### Points Clés
- Il semble probable que "debug in npm" fasse référence à l'utilisation du package "debug" pour la journalisation dans les projets Node.js gérés par npm.
- Les recherches suggèrent d'installer le package avec `npm install debug`, puis de l'utiliser dans le code avec un espace de nommage comme `require('debug')('myapp:component')`.
- Les preuves penchent en faveur de l'activation de la sortie de débogage en définissant la variable d'environnement `DEBUG`, par exemple `DEBUG=myapp:component npm run start`.

### Installation et Utilisation du Package Debug
Pour utiliser le package "debug" dans votre projet Node.js, installez-le d'abord en utilisant npm :
- Exécutez `npm install debug` dans le répertoire de votre projet.

Ensuite, dans votre code JavaScript, requirez le package et créez une instance debug avec un espace de nommage :
- Exemple : `const debug = require('debug')('myapp:component'); debug('un message');`.

### Activation de la Sortie de Débogage
Pour voir les messages de débogage, définissez la variable d'environnement `DEBUG` lors de l'exécution de votre application :
- Par exemple, exécutez `DEBUG=myapp:component node app.js` ou `DEBUG=myapp:component npm run start` si vous utilisez un script npm.

### Contrôle des Espaces de Nommage
Vous pouvez contrôler quels messages de débogage apparaissent en utilisant des wildcards ou des exclusions :
- Activez plusieurs espaces de nommage avec `DEBUG=myapp:* node app.js`.
- Excluez des espaces de nommage spécifiques avec `DEBUG=*,-myapp:exclude node app.js`.

---

### Note d'Enquête : Exploration Détaillée de l'Utilisation de Debug dans npm

Cette section fournit un aperçu complet de l'utilisation du package "debug" dans les projets Node.js gérés par npm, basé sur la documentation et les ressources disponibles. L'accent est mis sur la mise en œuvre pratique, les fonctionnalités avancées et les considérations pour les développeurs, afin d'assurer une compréhension approfondie pour les débutants comme pour les utilisateurs expérimentés.

#### Introduction à Debug dans le Contexte npm
L'expression "debug in npm" fait très probablement référence à l'utilisation du package "debug", un utilitaire de débogage léger pour les environnements Node.js et navigateur, dans les projets gérés par npm (Node Package Manager). Compte tenu de la notoriété du package "debug" dans les résultats de recherche et de sa pertinence pour le développement Node.js, cette interprétation correspond aux besoins courants des développeurs en matière de journalisation et de débogage dans les projets gérés par npm. Le package, actuellement en version 4.4.0 selon les mises à jour récentes, est largement utilisé, avec plus de 55 746 autres projets du registre npm l'ayant adopté, ce qui indique son statut de standard dans l'écosystème.

#### Installation et Utilisation de Base
Pour commencer, installez le package "debug" en utilisant npm :
- Commande : `npm install debug`
- Cela ajoute le package au `node_modules` de votre projet et met à jour le `package.json`.

Dans votre code JavaScript, requirez le package et initialisez-le avec un espace de nommage pour catégoriser les messages de débogage :
- Exemple : `const debug = require('debug')('myapp:component');`.
- Utilisez l'instance debug pour journaliser les messages : `debug('un message');`.
- L'espace de nommage, tel que 'myapp:component', aide à identifier la source des messages, facilitant le filtrage des journaux dans les grandes applications.

Pour voir ces messages de débogage, définissez la variable d'environnement `DEBUG` lors de l'exécution de votre application :
- Exemple : `DEBUG=myapp:component node app.js`.
- Si votre application démarre via un script npm (par exemple, `npm run start`), utilisez : `DEBUG=myapp:component npm run start`.
- Cette variable d'environnement contrôle quels espaces de nommage sont activés, permettant un débogage sélectif sans modifier le code.

#### Fonctionnalités Avancées et Configuration
Le package "debug" offre plusieurs fonctionnalités avancées pour une meilleure utilisabilité :

##### Contrôle des Espaces de Nommage et Wildcards
- Utilisez des wildcards pour activer plusieurs espaces de nommage : `DEBUG=myapp:* node app.js` affichera les messages de débogage de tous les espaces de nommage commençant par 'myapp:'.
- Excluez des espaces de nommage spécifiques en utilisant un signe moins : `DEBUG=*,-myapp:exclude node app.js` active tous les espaces de nommage sauf ceux commençant par 'myapp:exclude'.
- Ce débogage sélectif est crucial pour se concentrer sur des parties spécifiques d'une application sans être submergé par les journaux.

##### Codage Couleur et Analyse Visuelle
- La sortie de débogage inclut un codage couleur basé sur les noms des espaces de nommage, facilitant l'analyse visuelle.
- Les couleurs sont activées par défaut lorsque stderr est un TTY (terminal) dans Node.js, et peuvent être améliorées en installant le package `supports-color` aux côtés de debug pour une palette de couleurs plus large.
- Dans les navigateurs, les couleurs fonctionnent sur les inspecteurs basés sur WebKit, Firefox (version 31 et ultérieure) et Firebug, améliorant la lisibilité dans les outils de développement.

##### Différence de Temps et Analyse des Performances
- Le package peut afficher la différence de temps entre les appels de débogage, préfixée par "+NNNms", utile pour l'analyse des performances.
- Cette fonctionnalité est automatiquement activée et utilise `Date#toISOString()` lorsque stdout n'est pas un TTY, garantissant une cohérence entre les environnements.

##### Variables d'Environnement et Personnalisation
Plusieurs variables d'environnement affinent la sortie de débogage :
| Nom               | Objectif                                   |
|-------------------|--------------------------------------------|
| DEBUG             | Active/désactive les espaces de nommage   |
| DEBUG_HIDE_DATE   | Masque la date dans la sortie non TTY      |
| DEBUG_COLORS      | Force l'utilisation des couleurs en sortie|
| DEBUG_DEPTH       | Définit la profondeur d'inspection des objets |
| DEBUG_SHOW_HIDDEN | Affiche les propriétés cachées dans les objets |

- Par exemple, définir `DEBUG_DEPTH=5` permet une inspection plus profonde des objets, utile pour les structures de données complexes.

##### Formateurs pour une Sortie Personnalisée
Debug prend en charge les formateurs personnalisés pour différents types de données, améliorant la lisibilité des journaux :
| Formateur | Représentation                            |
|-----------|-------------------------------------------|
| %O        | Affichage formaté d'Object (multi-lignes) |
| %o        | Affichage formaté d'Object (ligne unique) |
| %s        | String                                    |
| %d        | Number (entier/flottant)                  |
| %j        | JSON, gère les références circulaires     |
| %%        | Signe pourcent unique                     |

- Les formateurs personnalisés peuvent être étendus, par exemple `createDebug.formatters.h = (v) => v.toString('hex')` pour une sortie hexadécimale.

#### Intégration avec les Scripts npm
Pour les projets utilisant des scripts npm, l'intégration de debug est transparente :
- Modifiez vos scripts dans `package.json` pour inclure les paramètres debug si nécessaire, bien que définir `DEBUG` à l'exécution suffise généralement.
- Exemple de script : `"start": "node app.js"`, exécuté avec `DEBUG=myapp:component npm run start`.
- Pour les utilisateurs Windows, utilisez CMD avec `set DEBUG=* & node app.js` ou PowerShell avec `$env:DEBUG='*';node app.js`, garantissant une compatibilité multiplateforme.

#### Support Navigateur et Cas Particuliers
Bien que principalement conçu pour Node.js, debug prend également en charge les environnements navigateur :
- Compilez avec des outils comme Browserify ou utilisez des services comme [browserify-as-a-service](https://wzrd.in/standalone/debug@latest) pour une inclusion côté client.
- Persistez l'état activé dans les navigateurs en utilisant `localStorage.debug`, par exemple `localStorage.debug = 'worker:*'`.
- Note : Les navigateurs basés sur Chromium (Brave, Chrome, Electron) peuvent nécessiter l'activation du niveau de journalisation "Verbose" pour une fonctionnalité complète.

#### Bonnes Pratiques et Considérations
- Utilisez des espaces de nommage descriptifs, tels que "connect:bodyParser", pour maintenir la clarté des journaux.
- Ajoutez "*" aux espaces de nommage pour un débogage toujours activé, par exemple `DEBUG=connect:*`.
- Pour la production, assurez-vous que `DEBUG` n'est pas défini pour éviter une journalisation inutile, car les instructions de débogage sont silencieuses sans la variable.
- Tenez compte des performances : debug est léger, ne journalisant que lorsqu'il est activé, ce qui le rend adapté au développement sans impact sur la production.

#### Détail Inattendu : Déboguer npm Lui-même
Bien que l'accent principal soit mis sur le package "debug", il est important de noter que "debug in npm" pourrait être mal interprété comme le débogage de l'outil npm lui-même (par exemple, les problèmes avec `npm install`). Dans de tels cas, utilisez l'option `--verbose` de npm pour une sortie détaillée, mais cela est distinct de l'utilisation du package debug. Cette distinction est importante pour les utilisateurs explorant le débogage lié à npm, bien que le contexte suggère que le package est plus pertinent.

#### Conclusion
L'utilisation du package "debug" dans les projets Node.js gérés par npm offre un moyen robuste et flexible de mettre en œuvre un débogage sélectif. En l'installant via `npm install debug`, en le requérant avec des espaces de nommage et en contrôlant la sortie via `DEBUG`, les développeurs peuvent gérer efficacement les journaux, améliorer la lisibilité avec les couleurs et analyser les performances. Cette approche s'aligne sur les pratiques de développement modernes, offrant un équilibre entre le détail et le contrôle dans les flux de travail de débogage.

**Citations Clés :**
- [debug npm package detailed usage guide](https://www.npmjs.com/package/debug)