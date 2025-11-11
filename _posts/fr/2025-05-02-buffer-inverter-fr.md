---
audio: false
generated: true
lang: fr
layout: post
title: Circuits de tampon et d'inverseur
translated: true
type: note
---

Voici un tutoriel sur les circuits buffer et inverseur basé sur la vidéo YouTube fournie :

### Comprendre les circuits à transistors

* La vidéo explore deux circuits à transistors avec des entrées et des sorties, en se concentrant sur la tension.
* Les transistors agissent comme des interrupteurs à courant ; une tension d'entrée positive (par exemple, +5V) crée un courant, activant le transistor. Une tension nulle signifie aucun courant, et le transistor est désactivé.
* Les entrées et les sorties sont discutées en termes de uns et de zéros, où 0 représente 0V et 1 représente +5V.

### Circuit 1 : Émetteur suiveur / Buffer

* **L'entrée est 0 (0V) :** Le transistor est désactivé, et la sortie est connectée à la masse via une résistance, ce qui donne une sortie de 0.
* **L'entrée est 1 (+5V) :** Le courant circule, et la sortie est directement connectée à +5V, ce qui donne une sortie de 1.
* Ce circuit est appelé un **émetteur suiveur** car l'émetteur suit la base (l'entrée).
* Un autre nom pour celui-ci est un **buffer**, qui délivre en sortie le même niveau de tension que l'entrée.
* Le buffer est symbolisé par un triangle dans les schémas de logique numérique.

### Circuit 2 : Inverseur

* **L'entrée est 0 :** Aucun courant ne circule, le transistor est désactivé, et la sortie est reliée à +5V via une résistance de pull-up, ce qui donne une sortie de 1.
* **L'entrée est 1 :** Le courant circule, connectant la sortie à la masse, ce qui donne une sortie de 0.
* Ce circuit est connu sous le nom d'**inverseur**.
* Le symbole logique de l'inverseur est similaire à un buffer mais avec une bulle sur la sortie, indiquant l'inversion.
* Un circuit inverseur délivre en sortie l'opposé de l'entrée.

En résumé, la vidéo explique comment les circuits à transistors peuvent fonctionner comme un buffer, qui maintient le signal d'entrée, ou comme un inverseur, qui inverse le signal d'entrée.
http://googleusercontent.com/youtube_content/0