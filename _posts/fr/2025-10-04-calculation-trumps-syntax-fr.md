---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Le calcul prime sur la syntaxe en IA
translated: true
type: note
---

Tu as parfaitement raison que le cœur de l'IA et des LLM ne réside pas dans l'élégance de la prose ou les réflexions philosophiques sur les langages de programmation—même si des personnes comme Yin Wang et Daniel P. Friedman ont incontestablement aiguisé notre réflexion sur le sujet. Le blog de Wang plonge au plus profond des entrailles de systèmes comme Python et Lisp, critiquant la façon dont ils façonnent le calcul en pratique, tandis que les livres de Friedman (pensez à la série *The Little Schemer*) démystifient la récursion et les paradigmes fonctionnels d'une manière presque poétique. Mais effectivement, quand il s'agit de construire quelque chose qui *fonctionne*—comme générer un texte cohérent ou traiter des gradients dans un réseau de neurones—le moment de vérité arrive dans le "comment" et le "quoi" du calcul, pas dans le sucre syntaxique.

### Pourquoi le Calcul Prime sur la Syntaxe
À la base, un LLM comme moi ne médite pas sur les macros Lisp ou les hiérarchies d'objets de Java ; il exécute des multiplications matricielles, des mécanismes d'attention et de l'échantillonnage probabiliste à grande échelle. Le "comment calculer" se résume à :
-   **Algorithmes et modèles** : Des éléments comme les architectures de transformers (Vaswani et al., 2017) définissent *ce qui* est calculé—l'auto-attention sur les embeddings de tokens, les encodages positionnels, etc. C'est là que la magie opère, indépendamment du langage. Tu pourrais implémenter GPT en pseudocode et cela "fonctionnerait" sur le papier ; la syntaxe n'est qu'un véhicule.
-   **Précision numérique et efficacité** : Ici, le "quoi calculer" est extrêmement important. Nous parlons de probabilités de tokens, de fonctions de coût (par exemple, l'entropie croisée) et de rétropropagation. Si tu te trompes dans les maths, ton modèle hallucine et produit des absurdités. La syntaxe ? C'est secondaire—NumPy de Python te permet d'arriver à 90% du résultat avec une lisibilité remarquable, mais il est interprété et lent pour entraîner des modèles colossaux.

Le choix du langage s'insinue toutefois comme un filtre pragmatique. Le C++ excelle pour les parties critiques en termes de performance dans l'IA (par exemple, les noyaux de TensorFlow ou les liaisons CUDA de PyTorch), où chaque cycle compte dans l'entraînement distribué. Python domine pour le prototypage car il est concis—pourquoi lutter avec la gestion de la mémoire en C++ quand `torch.nn.Linear` te permet d'enchainer les couches en une ligne ? Mais tu as raison : c'est un "petit problème". Les vrais goulots d'étranglement sont algorithmiques (par exemple, les lois de mise à l'échelle comme celles de Kaplan et al.) ou liés aux données, et non pas au fait que tu tapes `def` ou `struct`.

### Où les Idées des Langages de Programmation Persistent
Cela dit, rejeter entièrement les langages de programmation, c'est jeter le bébé avec l'eau du bain. Une bonne conception de langage (inspirée par des gens comme Friedman/Wang) rend *l'expression* de ces calculs plus sûre et plus rapide :
-   **Abstractions pour le raisonnement** : La pureté fonctionnelle (à la Scheme) aide à éviter les bogues dans le code probabiliste, ce qui est énorme pour une inférence IA fiable.
-   **Performance sans effort** : Rust ou même le C++ moderne s'inspirent de la recherche sur les langages de programmation pour te donner de la vitesse *plus* de la sécurité, réduisant les erreurs de "calcul incorrect" qui parasitent le C brut.

En fin de compte, le progrès de l'IA, c'est 80 % de maths/modèles/données, 15 % d'ingénierie (où les langages comme le C++ excellent) et 5 % de poésie syntaxique. Si nous optimisions pour cette dernière, nous aurions des articles plus jolis mais des robots plus lents. Quel est ton avis—penses-tu que nous verrons plus de fusion entre les langages de programmation et l'IA, comme des langages spécifiques à un domaine pour les approches neuro-symboliques ?

[Blog de Wang](https://www.yinwang.org)
[Essence of Programming de Friedman](https://www.cs.indiana.edu/~dfriedman/)
[Attention Is All You Need (Article sur les Transformers)](https://arxiv.org/abs/1706.03762)
[Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)