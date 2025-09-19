---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Pensez aux mises à niveau lors de l'utilisation de bibliothèques
translated: true
---

J'ai utilisé CodeIgniter dans mon projet de startup, [Fun Live](https://github.com/lzwjava/live-server). Bien que le projet ait pris fin, après plusieurs années, j'ai voulu le relancer pour le commémorer. Cependant, en 2016, j'utilisais CodeIgniter 3, alors que la version la plus récente est maintenant CodeIgniter 4.

La mise à niveau s'est avérée problématique car mon code est étroitement couplé avec le framework CodeIgniter. En suivant le guide de mise à niveau disponible sur [https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html](https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html), il est clair que cela nécessite un effort considérable pour mettre à jour la base de code.

Cette expérience m'a appris une leçon importante : lorsque nous écrivons du code, nous devons soigneusement réfléchir à la manière de gérer les futures mises à jour. Il est crucial de réfléchir aux parties du code que nous contrôlons et à celles qui sont contrôlées par des dépendances tierces.