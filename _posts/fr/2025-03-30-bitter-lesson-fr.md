---
audio: false
generated: true
lang: fr
layout: post
title: La Leçon Amère de Rich Sutton
translated: true
type: note
---

La « leçon amère » de Rich Sutton est une observation stimulante sur l'histoire de la recherche en intelligence artificielle. En substance, elle affirme que **les chercheurs en IA qui tentent d'intégrer des connaissances de type humain et des fonctionnalités conçues à la main dans leurs systèmes finissent par atteindre un mur et sont dépassés par des approches qui reposent davantage sur des algorithmes d'apprentissage à usage général, à condition de disposer de suffisamment de calcul.**

La partie « amère » vient du fait que les chercheurs ont souvent de fortes intuitions sur le fonctionnement de l'intelligence et sur les types de connaissances ou d'architectures qui devraient être bénéfiques. Cependant, l'histoire a maintes fois montré que ces intuitions mènent souvent à des impasses par rapport au fait de laisser les algorithmes apprendre directement à partir des données via des méthodes comme la recherche et l'apprentissage.

Voici une analyse des aspects clés de la leçon amère :

* **La connaissance humaine est souvent une béquille à court terme :** Bien qu'intégrer des connaissances humaines puisse conduire à des progrès initiaux ou à de meilleures performances sur de petits ensembles de données, cela limite souvent la capacité du système à évoluer et à s'adapter à des problèmes plus complexes ou à de plus grandes quantités de données. Les fonctionnalités conçues à la main deviennent fragiles et ne parviennent pas à généraliser.
* **Les méthodes générales triomphent avec l'échelle :** Sutton soutient que les percées les plus significatives en IA sont venues de méthodes générales comme la recherche (par exemple, dans les jeux) et l'apprentissage (par exemple, dans le machine learning et le deep learning). Ces méthodes, lorsqu'elles disposent de suffisamment de données et de puissance de calcul, peuvent découvrir leurs propres représentations et stratégies, surpassant souvent les solutions conçues par l'homme.
* **L'importance du calcul :** Un thème central est la disponibilité et l'importance croissantes du calcul. À mesure que la puissance de calcul augmente, l'avantage passe vers les méthodes qui peuvent exploiter efficacement cette puissance pour apprendre à partir de vastes quantités de données.
* **Exemples souvent cités par Sutton :**
    * **Jeux (Échecs, Go) :** Les premières tentatives de création de programmes jouant aux échecs reposaient fortement sur des règles codées manuellement et des fonctions d'évaluation basées sur les connaissances expertes humaines. Celles-ci ont finalement été surpassées par des systèmes comme Deep Blue (qui utilisait une recherche massive) et AlphaGo (qui utilisait l'apprentissage par renforcement profond), qui ont appris leurs stratégies par le calcul et les données.
    * **Reconnaissance vocale :** Les premiers systèmes de reconnaissance vocale incorporaient beaucoup de connaissances linguistiques et de fonctionnalités conçues à la main. Les systèmes modernes basés sur le deep learning, entraînés sur des quantités massives de données audio, ont obtenu de bien meilleures performances sans encoder explicitement ces connaissances.
    * **Vision par ordinateur :** Semblable à la reconnaissance vocale, la vision par ordinateur reposait initialement sur des fonctionnalités conçues manuellement comme des détecteurs de contours et des descripteurs de texture. Les modèles de deep learning, entraînés de bout en bout sur de grands ensembles de données d'images, ont révolutionné le domaine.

**Implications pour la recherche en IA :**

La leçon amère de Sutton suggère que la recherche en IA devrait davantage se concentrer sur le développement d'algorithmes d'apprentissage généralistes et évolutifs, et leur fournir autant de données et de calcul que possible, plutôt que d'essayer de coder en dur une intelligence de type humain ou de s'appuyer lourdement sur des fonctionnalités conçues à la main. C'est un appel à faire confiance au pouvoir de l'apprentissage et à l'augmentation inexorable des ressources de calcul.

Bien que la leçon amère ne rejette pas complètement la valeur de l'intuition humaine dans la conception des algorithmes d'apprentissage eux-mêmes, elle souligne que la connaissance du *domaine problématique* est souvent mieux apprise directement à partir des données plutôt que d'être explicitement programmée.

En résumé, la leçon amère est un rappel que si l'intuition humaine peut être un point de départ, le succès à long terme de l'IA réside souvent dans la capacité des méthodes d'apprentissage générales à découvrir des solutions par le calcul et les données, même si ces solutions ne sont pas immédiatement intuitives pour les humains.