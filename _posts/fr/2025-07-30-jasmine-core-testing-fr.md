---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Présentation du Framework de Tests Jasmine Core
translated: true
type: note
---

### Jasmine-Core
Jasmine-core est la bibliothèque principale de Jasmine, un framework de test JavaScript populaire. Il fournit des outils pour écrire des tests de développement piloté par le comportement (BDD), incluant des fonctionnalités comme des suites de test (blocs `describe`), des tests individuels (blocs `it`) et des matchers pour les assertions (par exemple, `expect().toBe()`). Il est autonome et peut s'exécuter dans des navigateurs ou des environnements Node.js.

- **Objectif** : Permet aux développeurs d'écrire et d'exécuter des tests unitaires pour des applications JavaScript dans un format lisible, semblable à des spécifications.
- **Installation** : Généralement via npm (`npm install jasmine-core`).
- **Exemple d'utilisation** : Vous pouvez configurer les tests manuellement ou les intégrer avec des outils comme Karma. C'est un projet open-source maintenu sur GitHub (https://github.com/jasmine/jasmine), la dernière version (à la date de ma dernière mise à jour) étant autour de la 5.x.
- **Preuve de pertinence** : C'est une dépendance fondamentale pour de nombreuses configurations de test JavaScript, utilisée par des projets comme les applications Angular et React pour les pratiques TDD/BDD.

### Karma-Jasmine-HTML-Reporter
Le karma-jasmine-html-reporter est un package NPM qui fournit un plugin de rapporteur basé sur HTML pour Karma, le lanceur de tests JavaScript. Il s'intègre aux tests Jasmine en affichant les résultats dans une interface web conviviale, montrant les tests réussis/échoués, les traces de pile et les informations de timing, le tout rendu dans une page HTML qui se met à jour en temps réel pendant l'exécution des tests.

- **Objectif** : Améliore la rétroaction des tests en offrant une interface utilisateur HTML basée sur un navigateur au lieu d'une sortie console, facilitant le débogage pour les développeurs. Il s'appuie sur jasmine-core pour la logique de test et sur karma pour exécuter les tests sur plusieurs navigateurs.
- **Installation** : Via npm (`npm install karma-jasmine-html-reporter --save-dev`).
- **Configuration** : Ajouté au fichier de configuration de Karma (par exemple, `karma.conf.js`) en tant que plugin et rapporteur. Nécessite que karma et karma-jasmine soient configurés.
- **Preuve de pertinence** : C'est un choix populaire pour les utilisateurs de Karma, avec une documentation sur le site officiel de Karma (https://karma-runner.github.io) et des mises à jour fréquentes. Il ne modifie pas l'exécution des tests mais améliore la visualisation, comme on peut le voir dans de nombreux workflows de développement.

Les deux outils sont souvent utilisés ensemble : jasmine-core gère la logique de test, tandis que karma-jasmine-html-reporter visualise les résultats dans une suite de tests exécutée par Karma. Si vous configurez des tests JS, commencez par la documentation de Karma pour l'intégration.