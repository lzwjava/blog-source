---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Métriques de Couverture JaCoCo Expliquées
translated: true
type: note
---

Oui — **JaCoCo fournit plusieurs niveaux de métriques de couverture**, incluant celles que vous avez mentionnées :

* **Couverture des Fichiers/Classes**  
  Elle suit la couverture au niveau de la classe, montrant la proportion de chaque classe qui a été exercée pendant les tests.

* **Couverture des Packages**  
  Elle agrège la couverture de toutes les classes d'un package, vous permettant de voir l'exhaustivité des tests pour des modules de plus haut niveau.

* **Couverture des Méthodes/Fonctions**  
  Elle mesure si des méthodes individuelles (fonctions) ont été invoquées et si leurs instructions/branches ont été couvertes.

* **Couverture des Instructions et des Branches**  
  Au niveau le plus granulaire, elle montre quelles instructions bytecode et branches conditionnelles ont été exécutées.

Lorsque vous générez un rapport HTML JaCoCo, vous verrez typiquement une vue arborescente :

* Nœud supérieur = couverture globale du projet.
* Suivant = couverture par package.
* Puis = couverture par classe.
* À l'intérieur de chaque classe = couverture par méthode, avec un surlignage ligne par ligne.

👉 Donc pour répondre à votre question : oui, JaCoCo prend en charge **la couverture des fichiers (classes), des packages et des fonctions (méthodes)** nativement.

Souhaitez-vous que je détaille **comment JaCoCo calcule chaque métrique** (par exemple, la différence entre la couverture des instructions, des branches, des lignes et des méthodes) pour que vous ayez une image plus claire de ce qui est réellement mesuré ?