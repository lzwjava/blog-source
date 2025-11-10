---
audio: false
generated: true
image: false
lang: fr
layout: post
title: L'Évolution des Transformateurs à la Lumière d'une Leçon Amère
translated: true
type: note
---

Dans sa conférence lors de l'événement Stanford CS25, Hyung Won Chung propose une analyse historique et prédictive détaillée des architectures **Transformer**, affirmant que comprendre les forces motrices de leur évolution est essentiel pour anticiper l'avenir de l'IA. Le cœur de son argumentation s'articule autour de « The Bitter Lesson » (La Leçon Amère) du développement de l'IA, qu'il illustre à travers l'évolution des modèles Transformer.

***

### La Force Motrice du Progrès en IA

Chung postule que le facteur le plus significatif propulsant la recherche en IA est **la diminution exponentielle du coût du calcul**, qui a permis une augmentation correspondante de l'échelle des modèles et des données. Il soutient que pour comprendre le rythme rapide des changements dans ce domaine, il faut se concentrer sur cette force motrice dominante plutôt que de se perdre dans les détails des innovations architecturales individuelles.

Il introduit le concept de **« The Bitter Lesson »**, qui suggère que le progrès à long terme de l'IA favorise les méthodes plus simples et plus générales, avec moins d'hypothèses intégrées (biais inductifs). Bien que les modèles très structurés et spécifiques à un domaine puissent offrir des gains à court terme, ils finissent par devenir des goulots d'étranglement à mesure que l'échelle du calcul et des données augmente. Il encourage les chercheurs à constamment remettre en question et simplifier les structures sous-jacentes de leurs modèles.

***

### L'Évolution des Architectures Transformer

Chung utilise trois architectures Transformer majeures pour illustrer ses propos :

1.  **Encodeur-Décodeur (Transformer Original) :** Cette architecture, initialement utilisée pour des tâches comme la traduction automatique, possède une structure plus inhérente. Elle utilise des paramètres distincts pour l'encodeur et le décodeur ainsi que des motifs d'attention croisée spécifiques. Bien qu'efficace pour les tâches à entrées/sorties distinctes, cette structure devient moins pertinente à l'ère des grands modèles à usage général.

2.  **Encodeur-Uniquement (ex. : BERT) :** Une architecture plus simple qui renonce à la génération, se concentrant sur des tâches comme la classification. Bien que puissante pour des benchmarks spécifiques, sa focalisation étroite la rend moins généralisable pour un large éventail d'applications modernes.

3.  **Décodeur-Uniquement (ex. : GPT-3) :** C'est l'architecture la plus générale et la moins structurée des trois. Elle utilise une seule pile de couches et des paramètres partagés, la rendant très adaptée aux grands modèles de langage modernes qui traitent des tâches diverses, apprennent des connaissances générales et effectuent de la génération longue.

***

### Principaux Enseignements et Prédictions

Selon Chung, la tendance est claire : l'IA évolue vers **des architectures plus simples, plus générales, avec moins de structure imposée**. Cela permet aux modèles la liberté d'apprendre des modèles et des relations complexes à partir de vastes quantités de données sans être contraints par des hypothèses fixes.

Il suggère que le prochain goulot d'étranglement en IA pourrait ne pas être l'architecture elle-même, mais **l'objectif d'apprentissage**. Il considère des méthodes comme le Reinforcement Learning from Human Feedback (RLHF) comme une étape vers des fonctions objectif moins structurées et apprises, mieux adaptées aux tâches de génération ouvertes et complexes. Il encourage l'audience à réfléchir de manière critique à ces principes pour contribuer à façonner l'avenir de l'IA.

Vous pouvez regarder l'intégralité de la conférence à l'adresse [https://www.youtube.com/watch?v=3gb-ZkVRemQ&pp=0gcJCfwAo7VqN5tD](https://www.youtube.com/watch?v=3gb-ZkVRemQ&pp=0gcJCfwAo7VqN5tD).