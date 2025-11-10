---
audio: false
generated: true
lang: fr
layout: post
title: 'PySonar2 : Indexeur Sémantique Python'
translated: true
type: note
---

PySonar2 est un indexeur sémantique pour Python, développé par yinwang0, qui utilise l'inférence de types interprocédurale pour analyser de grandes bases de code Python. Il est conçu pour le traitement par lots, le rendant adapté à la création d'index pour les navigateurs de code et les moteurs de recherche plutôt que pour les Environnements de Développement Intégrés (IDE) en temps réel. Son objectif principal est la précision via l'inférence de types, qui vise à décrire comment le code est réellement utilisé.

**Fonctionnalités et caractéristiques principales :**

* **Indexation Sémantique :** La fonction principale de PySonar2 est de construire un index sémantique du code Python, permettant des capacités avancées de navigation et de recherche dans le code.
* **Inférence de Types Interprocédurale :** Il utilise une inférence de types interprocédurale sophistiquée pour comprendre le flux et l'utilisation des types à travers l'ensemble d'une base de code, contribuant ainsi à sa précision.
* **Traitement par Lots :** Optimisé pour traiter de grands projets de manière groupée, par opposition aux outils d'analyse en temps réel.
* **Bibliothèque pour Outils de Développement :** PySonar2 est conçu comme une bibliothèque fondamentale pour d'autres outils de développement, et non comme une application autonome pour l'utilisateur final.
* **Licence Apache-2.0 :** Le projet est open-source sous la licence Apache-2.0, permettant une utilisation, modification et distribution gratuites.

**Adoption et Utilisation :**

PySonar2 a connu une adoption significative dans l'industrie, servant notamment de moteur d'indexation pour :

* La recherche de code interne de Google (Google's internal Code Search)
* sourcegraph.com
* insight.io

**Détails Techniques :**

* **Langages :** Le dépôt est principalement écrit en Java (94,4 %), le Python (5,1 %) étant utilisé pour la cible d'analyse.
* **Système de Build :** Il utilise Maven pour la construction. Pour construire le projet, exécutez `mvn package -DskipTests`.
* **Démo :** Une démo est disponible pour construire un simple navigateur de code pour la bibliothèque standard de Python 2.7 en utilisant une commande Java.
* **Configuration Système Requise :** Nécessite Python 2.7.x ou 3.x, Java 8+ et Maven. Une configuration correcte des variables d'environnement `PATH` et `PYTHONPATH` est cruciale.
* **Tests :** Les tests unitaires peuvent être exécutés avec `mvn test`. La création de nouveaux tests implique de créer du code Python dans des répertoires se terminant par ".test" au sein du répertoire `tests`.

**Statut du Dépôt :**

Le dépôt a attiré une attention considérable, comme en témoignent :

* **1,4 k stars**
* **506 forks**

Des commits récents indiquent une maintenance continue, incluant des mises à jour du README et de la version, ainsi que des corrections pour les "code smells".

**Contributions :**

Les contributions sont les bienvenues, bien que des changements significatifs soient encouragés à être discutés avec le mainteneur en raison de la théorie complexe sous-jacente au projet.

Pour plus de détails, vous pouvez visiter le [Dépôt GitHub PySonar2](https://github.com/yinwang0/pysonar2).