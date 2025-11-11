---
audio: false
generated: true
lang: fr
layout: post
title: Transistors en tant qu'interrupteurs
translated: true
type: note
---

### Les transistors en tant qu'interrupteurs : un tutoriel

Ce tutoriel explique comment un transistor, plus précisément un transistor bipolaire (BJT), peut fonctionner comme un interrupteur commandé par un courant électrique.

**1. L'amplification du courant pour la commutation**

* Comme nous l'avons vu précédemment, un transistor peut amplifier un faible courant de base pour contrôler un courant collecteur-émetteur plus important.
* Cette amplification est fondamentale pour son utilisation en tant qu'interrupteur. Un faible courant de commande peut gérer un courant beaucoup plus important nécessaire pour alimenter des composants comme une LED.

**2. L'état "Marche" : la saturation**

* Lorsque le transistor laisse passer le courant maximum possible entre le collecteur et l'émetteur, il est dans un état appelé **saturation**.
* Cela se produit lorsque le courant souhaité pour le circuit est inférieur au courant maximum que le transistor peut fournir en fonction de son amplification.
* En saturation, le transistor se comporte comme un **interrupteur fermé** ou un court-circuit, laissant passer le courant librement.

**3. L'état "Arrêt" : le blocage**

* Lorsqu'il n'y a pas de courant de base, le transistor restreint considérablement ou arrête complètement le flux de courant entre le collecteur et l'émetteur. Cet état est appelé **blocage** (cut-off).
* À l'état de blocage, le transistor agit comme un **interrupteur ouvert**, bloquant complètement le flux de courant.

**4. Son fonctionnement en tant qu'interrupteur**

* En passant de l'état de **saturation** (marche) à l'état de **blocage** (arrêt), un transistor fonctionne efficacement comme un **interrupteur commandé par le courant**.
* Un faible courant de commande sur la base détermine si l'interrupteur est "ouvert" (blocage) ou "fermé" (saturation), contrôlant ainsi un chemin de courant plus important.

**5. Applications en circuit**

* Comprendre ces états de commutation est crucial pour la construction de circuits électroniques où les transistors sont utilisés pour contrôler le flux d'énergie vers d'autres composants.

En résumé, en utilisant un faible courant de base pour amener le transistor soit en saturation, soit en blocage, nous pouvons l'utiliser pour activer ou désactiver un flux de courant plus important, permettant son utilisation comme un élément de base fondamental dans l'électronique numérique et les applications de commutation.