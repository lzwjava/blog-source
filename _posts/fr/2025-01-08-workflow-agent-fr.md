---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Le workflow est en BFS (Breadth-First Search), l'agent est en DFS (Depth-First
  Search).
translated: true
type: post
---

Selon Anthropic [^1] :

- **Workflows** sont des systèmes dans lesquels les LLM et les outils sont orchestrés via des chemins de code prédéfinis.
- **Agents**, en revanche, sont des systèmes où les LLM contrôlent dynamiquement leurs propres processus et l'utilisation des outils, conservant ainsi une flexibilité dans la manière dont les tâches sont accomplies.

Ce que je comprends de cela est :

- Utiliser des **workflows** pour améliorer une application ou une plateforme est similaire à **BFS (Breadth-First Search)**, où les tâches sont accomplies de manière systématique, niveau par niveau.
- Utiliser des **agents** ressemble davantage à **DFS (Depth-First Search)**, où les tâches sont abordées de manière plus exploratoire, étape par étape.

Parfois, **BFS** et **DFS** peuvent être combinés. DFS peut être imbriqué dans un autre DFS, et il en va de même pour BFS.

Par exemple, **o1 (chaîne de pensée)** est similaire à BFS (Breadth-First Search). Initialement, les tâches principales sont divisées en étapes distinctes, et chaque étape est ensuite développée en explications plus détaillées. Ensuite, sur la base de toutes ces réflexions, le résultat final est fourni.

Pour des tâches très complexes, comme demander à une IA de créer une application YouTube ou de concevoir un système d'exploitation, elle pourrait utiliser BFS (Breadth-First Search), DFS (Depth-First Search), ou une combinaison des deux. Tout dépend de la manière dont nous utilisons BFS et DFS — parfois, l'IA doit creuser en profondeur (DFS), et parfois elle doit élargir son approche (BFS).

Une autre considération est que, à chaque étape, l'IA devrait évaluer ce qu'elle doit faire ensuite pour atteindre ses objectifs.

**Les cibles** sont un aspect intéressant. Il peut y avoir de nombreuses cibles, comme la création d'une application YouTube, où l'IA doit s'assurer que tout le code fonctionne bien, que toutes les fonctionnalités sont implémentées et que tous les tests sont réussis. La manière d'atteindre ces cibles est fascinante. L'IA devrait-elle s'attaquer à une cible à la fois, ou devrait-elle progresser sur toutes les cibles simultanément et ensuite itérer sur chacune ?

---

[^1]: Construire des agents efficaces, [Anthropic](https://www.anthropic.com/research/building-effective-agents)