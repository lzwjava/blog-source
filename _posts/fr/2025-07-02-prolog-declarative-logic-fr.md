---
audio: false
generated: true
lang: fr
layout: post
title: 'Prolog : Programmation Déclarative Basée sur la Logique'
translated: true
type: note
---

Prolog, abréviation de « Programming in Logic », est un **langage de programmation déclaratif** qui contraste fortement avec les langages impératifs comme Python, Java ou C++. Au lieu d'expliquer à l'ordinateur *comment* résoudre un problème étape par étape, vous décrivez *quel* est le problème, et Prolog utilise son moteur d'inférence intégré pour trouver des solutions.

Il est particulièrement adapté aux problèmes impliquant la **logique, le raisonnement symbolique et la représentation des connaissances**, ce qui en fait une pierre angulaire dans le domaine de l'Intelligence Artificielle (IA), du traitement du langage naturel et des systèmes experts.

### Concepts Clés de Prolog :

1.  **Faits :**
    Les faits sont des vérités fondamentales sur le monde que vous fournissez à Prolog. Ils représentent des affirmations inconditionnelles.

      * **Syntaxe :** `prédicat(argument1, argument2, ...).`
      * **Exemples :**
          * `homme(john).` (John est un homme)
          * `femme(mary).` (Mary est une femme)
          * `parent(john, mary).` (John est un parent de Mary)
          * `capitale_de(france, paris).` (Paris est la capitale de la France)

2.  **Règles :**
    Les règles définissent des relations entre les faits. Elles indiquent qu'un certain fait est vrai si un ou plusieurs autres faits (ou conditions) sont vrais.

      * **Syntaxe :** `tête :- corps.` (Se lit comme « tête est vrai si corps est vrai »)
          * La `tête` est un seul prédicat.
          * Le `corps` est une conjonction d'un ou plusieurs prédicats, séparés par des virgules (`,`), ce qui signifie « ET ».
      * **Exemples :**
          * `heureux(X) :- aime(X, pizza).` (X est heureux si X aime la pizza)
          * `pere(X, Y) :- parent(X, Y), male(X).` (X est le père de Y si X est un parent de Y ET X est un homme)
          * `grand_parent(G, C) :- parent(G, P), parent(P, C).` (G est un grand-parent de C si G est un parent de P ET P est un parent de C)

3.  **Requêtes :**
    Une fois que vous avez défini vos faits et règles (votre « base de connaissances »), vous pouvez poser des questions à Prolog, appelées requêtes, pour récupérer des informations ou vérifier des relations.

      * **Syntaxe :** `?- requête.`
      * Prolog tente de satisfaire la requête en trouvant des variables qui rendent la requête vraie, en se basant sur les faits et règles établis. Si plusieurs solutions existent, vous pouvez souvent demander à Prolog d'en trouver d'autres en tapant un point-virgule (`;`).
      * **Exemples :**
          * `?- homme(john).` (Est-ce que John est un homme ?)
          * `?- parent(john, X).` (De qui John est-il un parent ? - `X` est une variable)
          * `?- grand_parent(elizabeth, william).` (Est-ce qu'Elizabeth est une grand-parent de William ?)

4.  **Variables :**
    Les variables en Prolog sont utilisées pour représenter des valeurs inconnues. Elles commencent toujours par une majuscule ou un underscore (`_`). Contrairement aux variables des langages impératifs, ce ne sont pas des emplacements mémoire pouvant être réaffectés ; ce sont plutôt des espaces réservés que Prolog tente d'unifier avec des valeurs pour satisfaire une requête.

5.  **Unification :**
    C'est le mécanisme central de Prolog. L'unification est un processus de mise en correspondance de modèles qui tente de rendre deux termes identiques en attribuant des valeurs aux variables. Si une correspondance est trouvée, les variables sont « liées » à ces valeurs. Si aucune correspondance n'est possible, l'unification échoue.

6.  **Retour sur trace (Backtracking) :**
    Lorsque Prolog tente de satisfaire une requête, il parcourt les faits et les règles de manière profondeur d'abord. Si un chemin mène à une impasse (un objectif ne peut pas être satisfait), Prolog « revient en arrière » (backtrack) à un point de choix précédent et essaye un autre chemin. Cette recherche systématique lui permet de trouver toutes les solutions possibles à une requête.

### Comment Fonctionne Prolog (Simplifié) :

1.  Vous chargez un programme Prolog (un ensemble de faits et de règles) dans l'interpréteur.
2.  Vous posez une requête.
3.  Prolog tente de prouver la requête en la faisant correspondre à ses faits et aux têtes de ses règles.
4.  Si la tête d'une règle correspond, Prolog tente alors de prouver les conditions dans le corps de la règle (celles-ci deviennent des sous-buts).
5.  Ce processus continue de manière récursive jusqu'à ce que tous les sous-buts soient satisfaits par des faits ou par des règles prouvées avec succès.
6.  Si une solution est trouvée, Prolog présente les liaisons de variables. Si plusieurs solutions existent, il peut revenir en arrière pour les trouver.

### Avantages de Prolog :

  * **Nature Déclarative :** Se concentre sur *quoi* résoudre, pas *comment*. Cela peut conduire à un code plus concis et lisible pour certains problèmes.
  * **Logique et Inférence Intégrées :** Mécanismes puissants pour le raisonnement logique et la recherche.
  * **Excellent pour l'IA Symbolique :** Idéal pour les systèmes experts, le traitement du langage naturel, la représentation des connaissances et la démonstration de théorèmes.
  * **Mise en Correspondance de Modèles et Unification :** Simplifie la manipulation complexe de données.
  * **Retour sur Trace :** Automatise la recherche de solutions, qui devrait être programmée manuellement dans d'autres langages.

### Inconvénients de Prolog :

  * **Courbe d'Apprentissage :** Le paradigme déclaratif peut être difficile pour ceux qui ont l'habitude de la programmation impérative.
  * **Performances :** Peut être moins efficace pour les calculs numériques ou les tâches intensives en E/S par rapport aux langages impératifs.
  * **E/S et Graphismes Limités :** N'est pas conçu pour les interfaces utilisateur complexes ou les applications graphiques.
  * **Débogage :** Tracer le flux d'exécution dans Prolog peut parfois être délicat en raison du retour sur trace.

-----

### Exemples de Code Prolog :

Pour exécuter ces exemples, vous aurez besoin d'un interpréteur Prolog (comme SWI-Prolog, qui est gratuit et largement utilisé). Vous sauvegardez généralement votre code dans un fichier avec l'extension `.pl` (par exemple, `famille.pl`) et vous le chargez dans l'interpréteur.

**Exemple 1 : Relations Familiales**

Définissons quelques relations familiales de base.

**`famille.pl` :**

```prolog
% Faits : Définir les relations de base
homme(john).
homme(jim).
homme(george).
femme(mary).
femme(lisa).
femme(susan).

parent(john, lisa).   % John est un parent de Lisa
parent(john, jim).    % John est un parent de Jim
parent(mary, lisa).   % Mary est un parent de Lisa
parent(mary, jim).    % Mary est un parent de Jim
parent(lisa, george). % Lisa est un parent de George
parent(jim, susan).   % Jim est un parent de Susan

% Règles : Définir les relations dérivées
pere(X, Y) :- parent(X, Y), homme(X).         % X est le père de Y si X est un parent de Y ET X est un homme.
mere(X, Y) :- parent(X, Y), femme(X).         % X est la mère de Y si X est un parent de Y ET X est une femme.
enfant(X, Y) :- parent(Y, X).                 % X est un enfant de Y si Y est un parent de X.
grand_parent(G, C) :- parent(G, P), parent(P, C). % G est un grand-parent de C si G est un parent de P ET P est un parent de C.
frere_ou_soeur(X, Y) :- parent(P, X), parent(P, Y), X \= Y. % X et Y sont frères et sœurs s'ils partagent un parent P, et X n'est pas le même que Y.
```

**Exécution dans un Interpréteur Prolog (ex: SWI-Prolog) :**

```prolog
?- consult('famille.pl').
% famille.pl compiled 0.00 sec, 7 clauses
true.

% Requêtes :

?- homme(john).
true.

?- femme(jim).
false.

?- parent(john, lisa).
true.

?- parent(X, jim). % Qui est un parent de Jim ?
X = john ;           % Tapez ';' pour plus de solutions
X = mary.
false.

?- pere(john, lisa).
true.

?- mere(mary, jim).
true.

?- grand_parent(john, george).
true.

?- grand_parent(X, susan). % Qui est un grand-parent de Susan ?
X = john ;
X = mary.
false.

?- frere_ou_soeur(lisa, jim).
true.

?- frere_ou_soeur(lisa, george).
false. % Parce qu'ils ne partagent pas *tous* les parents
```

**Exemple 2 : Base de Connaissances Simple (Animaux)**

**`animaux.pl` :**

```prolog
% Faits sur les animaux et leurs propriétés
animal(chien).
animal(chat).
animal(oiseau).
animal(poisson).

a_de_la_fourrure(chien).
a_de_la_fourrure(chat).
vole(oiseau).
nage(poisson).

mange(chien, os).
mange(chat, poisson).
mange(oiseau, graines).
mange(poisson, plancton).

% Règles
est_un_mammifere(X) :- animal(X), a_de_la_fourrure(X). % Un mammifère est un animal qui a de la fourrure.
peut_voler(X) :- animal(X), vole(X).                   % Quelque chose peut voler si c'est un animal et qu'il vole.
```

**Exécution dans un Interpréteur Prolog :**

```prolog
?- consult('animaux.pl').
% animaux.pl compiled 0.00 sec, 10 clauses
true.

% Requêtes :

?- animal(chat).
true.

?- a_de_la_fourrure(chien).
true.

?- mange(chat, X). % Que mange un chat ?
X = poisson.

?- est_un_mammifere(chien).
true.

?- est_un_mammifere(oiseau).
false.

?- peut_voler(X). % Quels animaux peuvent voler ?
X = oiseau.
false.
```

Ces exemples illustrent la nature déclarative de Prolog, où vous définissez les relations et les propriétés, et le système déduit les réponses à vos requêtes.