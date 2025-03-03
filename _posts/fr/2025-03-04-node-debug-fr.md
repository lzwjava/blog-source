---
audio: false
generated: true
lang: fr
layout: post
title: Débogage en Node.js avec le package Debug
translated: true
---

### Points Clés
- Il semble probable que "debug in npm" fait référence à l'utilisation du package "debug" pour la journalisation dans les projets Node.js gérés par npm.
- La recherche suggère d'installer le package avec `npm install debug`, puis de l'utiliser dans le code avec un espace de noms comme `require('debug')('myapp:component')`.
- Les preuves penchent en faveur de l'activation de la sortie de débogage en définissant la variable d'environnement `DEBUG`, comme `DEBUG=myapp:component npm run start`.

### Installation et Utilisation du Package Debug
Pour utiliser le package "debug" dans votre projet Node.js, installez-le d'abord avec npm :
- Exécutez `npm install debug` dans votre répertoire de projet.

Ensuite, dans votre code JavaScript, requérez le package et créez une instance de débogage avec un espace de noms :
- Exemple : `const debug = require('debug')('myapp:component'); debug('some message');`.

### Activation de la Sortie de Débogage
Pour voir les messages de débogage, définissez la variable d'environnement `DEBUG` lors de l'exécution de votre application :
- Par exemple, exécutez `DEBUG=myapp:component node app.js` ou `DEBUG=myapp:component npm run start` si vous utilisez un script npm.

### Contrôle des Espaces de Noms
Vous pouvez contrôler quels messages de débogage apparaissent en utilisant des jokers ou des exclusions :
- Activez plusieurs espaces de noms avec `DEBUG=myapp:* node app.js`.
- Excluez des espaces de noms spécifiques avec `DEBUG=*,-myapp:exclude node app.js`.

---

### Note de l'Enquête : Exploration Détaillée de l'Utilisation de Debug dans npm

Cette section fournit une vue d'ensemble complète de l'utilisation du package "debug" dans les projets Node.js gérés par npm, basée sur la documentation et les ressources disponibles. L'accent est mis sur la mise en œuvre pratique, les fonctionnalités avancées et les considérations pour les développeurs, garantissant une compréhension approfondie pour les débutants et les utilisateurs expérimentés.

#### Introduction à Debug dans le Contexte npm
La phrase "debug in npm" fait probablement référence à l'utilisation du package "debug", une utilité de débogage légère pour les environnements Node.js et navigateur, dans les projets gérés par npm (Node Package Manager). Étant donné la prévalence du package "debug" dans les résultats de recherche et sa pertinence pour le développement Node.js, cette interprétation s'aligne sur les besoins courants des développeurs en matière de journalisation et de débogage dans les projets gérés par npm. Le package, actuellement à la version 4.4.0 selon les mises à jour récentes, est largement utilisé, avec plus de 55 746 autres projets dans le registre npm l'adoptant, indiquant son statut standard dans l'écosystème.

#### Installation et Utilisation de Base
Pour commencer, installez le package "debug" en utilisant npm :
- Commande : `npm install debug`
- Cela ajoute le package à votre `node_modules` du projet et met à jour `package.json`.

Dans votre code JavaScript, requérez le package et initialisez-le avec un espace de noms pour catégoriser les messages de débogage :
- Exemple : `const debug = require('debug')('myapp:component');`.
- Utilisez l'instance de débogage pour journaliser des messages : `debug('some message');`.
- L'espace de noms, tel que 'myapp:component', aide à identifier la source des messages, facilitant le filtrage des journaux dans les grandes applications.

Pour voir ces messages de débogage, définissez la variable d'environnement `DEBUG` lors de l'exécution de votre application :
- Exemple : `DEBUG=myapp:component node app.js`.
- Si votre application démarre via un script npm (par exemple, `npm run start`), utilisez : `DEBUG=myapp:component npm run start`.
- Cette variable d'environnement contrôle quels espaces de noms sont activés, garantissant un débogage sélectif sans modifier le code.

#### Fonctionnalités Avancées et Configuration
Le package "debug" offre plusieurs fonctionnalités avancées pour une utilisabilité accrue :

##### Contrôle des Espaces de Noms et Jokers
- Utilisez des jokers pour activer plusieurs espaces de noms : `DEBUG=myapp:* node app.js` affichera les messages de débogage de tous les espaces de noms commençant par 'myapp:'.
- Excluez des espaces de noms spécifiques en utilisant un signe moins : `DEBUG=*,-myapp:exclude node app.js` active tous les espaces de noms sauf ceux commençant par 'myapp:exclude'.
- Ce débogage sélectif est crucial pour se concentrer sur des parties spécifiques d'une application sans être submergé par les journaux.

##### Codage en Couleur et Analyse Visuelle
- La sortie de débogage inclut un codage en couleur basé sur les noms des espaces de noms, aidant à l'analyse visuelle.
- Les couleurs sont activées par défaut lorsque stderr est un TTY (terminal) dans Node.js, et peuvent être améliorées en installant le package `supports-color` en plus de debug pour une palette de couleurs plus large.
- Dans les navigateurs, les couleurs fonctionnent sur les inspecteurs basés sur WebKit, Firefox (version 31 et ultérieure), et Firebug, améliorant la lisibilité dans les outils de développement.

##### Différence de Temps et Perspectives sur les Performances
- Le package peut afficher la différence de temps entre les appels de débogage, précédée de "+NNNms", utile pour l'analyse des performances.
- Cette fonctionnalité est activée automatiquement et utilise `Date#toISOString()` lorsque stdout n'est pas un TTY, garantissant la cohérence à travers les environnements.

##### Variables d'Environnement et Personnalisation
Plusieurs variables d'environnement ajustent finement la sortie de débogage :
| Nom             | But                              |
|------------------|--------------------------------------|
| DEBUG            | Active/désactive les espaces de noms          |
| DEBUG_HIDE_DATE  | Masque la date dans la sortie non-TTY         |
| DEBUG_COLORS     | Force l'utilisation des couleurs dans la sortie         |
| DEBUG_DEPTH      | Définit la profondeur d'inspection des objets         |
| DEBUG_SHOW_HIDDEN| Affiche les propriétés cachées dans les objets   |

- Par exemple, définir `DEBUG_DEPTH=5` permet une inspection plus approfondie des objets, utile pour les structures de données complexes.

##### Formatteurs pour une Sortie Personnalisée
Debug prend en charge les formatteurs personnalisés pour différents types de données, améliorant la lisibilité des journaux :
| Formatteur | Représentation                      |
|-----------|-------------------------------------|
| %O        | Affiche joliment un Objet (plusieurs lignes)|
| %o        | Affiche joliment un Objet (une seule ligne)   |
| %s        | Chaîne                              |
| %d        | Nombre (entier/flottant)              |
| %j        | JSON, gère les références circulaires   |
| %%        | Un seul signe pourcent                 |

- Les formatteurs personnalisés peuvent être étendus, par exemple, `createDebug.formatters.h = (v) => v.toString('hex')` pour une sortie hexadécimale.

#### Intégration avec les Scripts npm
Pour les projets utilisant des scripts npm, l'intégration de debug est fluide :
- Modifiez vos scripts `package.json` pour inclure les paramètres de debug si nécessaire, bien que définir `DEBUG` au moment de l'exécution suffise généralement.
- Exemple de script : `"start": "node app.js"`, exécutez avec `DEBUG=myapp:component npm run start`.
- Pour les utilisateurs de Windows, utilisez CMD avec `set DEBUG=* & node app.js` ou PowerShell avec `$env:DEBUG='*';node app.js`, garantissant la compatibilité multiplateforme.

#### Support des Navigateurs et Cas Particuliers
Bien que principalement pour Node.js, debug prend également en charge les environnements de navigateur :
- Construisez avec des outils comme Browserify ou utilisez des services comme [browserify-as-a-service](https://wzrd.in/standalone/debug@latest) pour l'inclusion côté client.
- Persistez l'état activé dans les navigateurs en utilisant `localStorage.debug`, par exemple, `localStorage.debug = 'worker:*'`.
- Note : Les navigateurs basés sur Chromium (Brave, Chrome, Electron) peuvent nécessiter l'activation du niveau de journal "Détaille" pour une fonctionnalité complète.

#### Meilleures Pratiques et Considérations
- Utilisez des espaces de noms descriptifs, tels que "connect:bodyParser", pour maintenir la clarté dans les journaux.
- Ajoutez "*" aux espaces de noms pour un débogage toujours activé, par exemple, `DEBUG=connect:*`.
- Pour la production, assurez-vous que `DEBUG` n'est pas défini pour éviter une journalisation inutile, car les instructions de débogage sont silencieuses sans la variable.
- Considérez les performances : debug est léger, ne journalisant que lorsqu'il est activé, le rendant adapté au développement sans impacter la production.

#### Détail Inattendu : Débogage de npm Lui-Même
Bien que le focus principal soit le package "debug", il est intéressant de noter que "debug in npm" pourrait être mal interprété comme le débogage de l'outil npm (par exemple, les problèmes de `npm install`). Pour de tels cas, utilisez le drapeau `--verbose` de npm pour une sortie détaillée, mais cela est distinct de l'utilisation du package debug. Cette distinction est importante pour les utilisateurs explorant le débogage lié à npm, bien que le contexte suggère que le package est plus pertinent.

#### Conclusion
L'utilisation du package "debug" dans les projets Node.js gérés par npm fournit une méthode robuste et flexible pour mettre en œuvre un débogage sélectif. En l'installant via `npm install debug`, en le requérant avec des espaces de noms et en contrôlant la sortie via `DEBUG`, les développeurs peuvent gérer efficacement les journaux, améliorer la lisibilité avec des couleurs et analyser les performances. Cette approche s'aligne sur les pratiques de développement modernes, offrant un équilibre entre détail et contrôle dans les flux de travail de débogage.

**Citations Clés :**
- [guide d'utilisation détaillé du package debug npm](https://www.npmjs.com/package/debug)