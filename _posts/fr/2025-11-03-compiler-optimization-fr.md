---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Optimisation du compilateur pour programmeurs expérimentés
translated: true
type: note
---

### Optimisation du compilateur

Dans le cours de compilation de Kent Dybvig, il nous a un jour expliqué que de nombreux cours de compilation mettent lourdement l'accent sur « l'optimisation », mais que la plupart de ces optimisations visent en réalité les programmeurs négligents. Par exemple, l'élimination des sous-expressions communes (CSE) — extraire des expressions répétées et coûteuses. Un programmeur bien formé devrait éviter d'écrire des calculs redondants dès le départ en définissant des variables pour réutiliser les résultats. Pourtant, les compilateurs se chargent eux-mêmes de cette tâche, comme si c'était crucial. Ce n'est pas le cas.

Ce qui *est* important, c'est la vitesse du compilateur lui-même. De nombreux compilateurs empilent ce genre d'« optimisations » inutiles dans une tentative de transformer du mauvais code en bon code, ce qui finit par ralentir le compilateur. La construction d'un projet prend une éternité, allongeant le cycle entre les modifications du code et l'obtention des résultats, et réduisant la productivité des développeurs.

C'est pourquoi Chez Scheme ignore la plupart de ces optimisations basiques — il suppose que les programmeurs ont les compétences de base pour éviter eux-mêmes les expressions coûteuses et redondantes. Les optimisations de Chez se concentrent principalement sur le code que le compilateur génère lui-même, comme l'optimisation des fermetures pour réduire autant que possible l'empreinte mémoire des fermetures. Ce sont des domaines que les programmeurs ne peuvent pas contrôler directement, donc le compilateur devrait viser le meilleur résultat possible là-dessus. Mais même celles-ci ont des limites : si la poursuite de l'optimisation rend le compilateur extrêmement lent tout en accélérant à peine le programme final, cela n'en vaut pas la peine. Chez Scheme trouve un équilibre entre la vitesse de compilation et les performances du code généré.

Dans ma pratique technique ultérieure, j'ai pu apprécier cette idée clé à plusieurs reprises.