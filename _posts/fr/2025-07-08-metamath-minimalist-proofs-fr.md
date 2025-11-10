---
audio: false
generated: true
lang: fr
layout: post
title: Norman Megill et les preuves rigoureuses de Metamath
translated: true
type: note
---

Le Dr Norman Dwight Megill (1950-2021) fut une figure très influente dans le domaine des mathématiques formelles et de la vérification automatisée de preuves, principalement connu comme l'auteur principal et la force motrice derrière le projet **Metamath**. Son travail s'est concentré sur la création d'un système unique, à la fois simple et puissant, pour exprimer et vérifier rigoureusement des preuves mathématiques par ordinateur.

**Le Projet Metamath :**

Metamath est un langage informatique et un programme associé conçus pour archiver, vérifier et étudier des preuves mathématiques avec une rigueur absolue. Ce qui distingue Metamath est sa simplicité fondamentale :

* **Langage Minimaliste :** Le langage Metamath est incroyablement léger, avec une quasi-absence de syntaxe intégrée. Il fournit un cadre fondamental pour exprimer essentiellement toutes les mathématiques à travers un petit ensemble de règles de base, principalement basées sur la substitution textuelle. Cette simplicité rend ses preuves très transparentes et permet leur vérification indépendante par divers outils.
* **Indépendant des Axiomes :** Metamath n'est lié à aucun ensemble d'axiomes spécifique. Au lieu de cela, les axiomes sont définis dans une « base de données » (un fichier texte d'axiomes et de théorèmes). Cette flexibilité permet de formaliser et d'explorer différents systèmes axiomatiques. La base de données la plus importante, `set.mm`, construit les mathématiques à partir de zéro, principalement basée sur ZFC (la théorie des ensembles de Zermelo-Fraenkel avec l'axiome du choix) et la logique classique du premier ordre.
* **Étapes de Preuve Exhaustives :** Une caractéristique des preuves Metamath est leur méticulosité. Chaque étape d'une preuve Metamath est explicitement énoncée, chaque étape étant une application d'un axiome ou d'une affirmation précédemment démontrée. Cela contraste avec de nombreux autres systèmes de preuve qui peuvent utiliser des « tactiques » ou de l'« automatisation » qui obscurcissent les étapes sous-jacentes de la preuve. Cette approche exhaustive garantit une précision inégalée et élimine la possibilité d'erreur humaine dans la vérification.
* **Vérification Indépendante :** La simplicité du langage Metamath a permis l'implémentation de nombreux vérificateurs de preuves indépendants dans divers langages de programmation, renforçant encore la fiabilité des preuves.

**Contributions de Norman Megill :**

La vision et le dévouement de Norman Megill ont été déterminants pour le développement et la prolifération de Metamath :

* **Auteur du Langage Metamath :** Il a conçu et développé le langage minimaliste Metamath, qui permet d'exprimer des théorèmes mathématiques complexes et leurs preuves sous une forme vérifiable par un ordinateur.
* **Auteur Principal du Programme Metamath :** Il a créé le programme Metamath original (un outil en ligne de commande basé sur C) qui peut lire, vérifier, modifier et produire des bases de données Metamath.
* **Cultivateur de la Communauté Metamath :** Pendant trois décennies, Megill a favorisé une communauté internationale de mathématiciens, de logiciens et d'informaticiens qui partageaient le rêve de numériser et de vérifier formellement les mathématiques. Ses encouragements et son jugement technique ont été essentiels pour construire cet environnement collaboratif.
* **Formalisation des Mathématiques :** Il a dirigé la création et l'expansion de la base de données Metamath Proof Explorer (MPE) (`set.mm`), qui contient des dizaines de milliers de théorèmes rigoureusement prouvés, couvrant de vastes domaines des mathématiques. Cette base de données est une réalisation significative dans la formalisation du savoir mathématique.
* **Auteur de « Metamath: A Computer Language for Mathematical Proofs » :** En 2019, il a co-écrit ce livre avec David A. Wheeler, fournissant une explication complète du langage et du programme Metamath, avec un accent particulier sur les fondamentaux de la base de données MPE.
* **Recherche en Logique et Physique :** Au-delà de Metamath, Megill a également mené des recherches liées à la logique quantique et aux espaces de Hilbert, utilisant Metamath pour formaliser ses investigations sur des propriétés comme les ensembles de Kochen-Specker, qui sont pertinents pour la contextualité quantique. Il a également contribué à la compréhension des axiomatisations finies par schémas de la logique classique du premier ordre.

Norman Megill a obtenu son diplôme de premier cycle en génie électrique et informatique du MIT en 1972 et son doctorat de l'Université de Zagreb, en Croatie, en 2010. Il est décédé subitement en décembre 2021, laissant un héritage profond dans le domaine des méthodes formelles et de l'effort continu pour atteindre une certitude absolue en mathématiques grâce à la vérification computationnelle. Son travail avec Metamath continue d'influencer les mathématiques formelles et témoigne de la puissance de la simplicité et de la rigueur pour relever des défis intellectuels complexes.