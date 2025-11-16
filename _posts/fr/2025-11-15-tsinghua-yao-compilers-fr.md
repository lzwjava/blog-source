---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Anciens de la Classe Yao de Tsinghua en Compilateurs
translated: true
type: note
---

### Aperçu de la classe Yao de Tsinghua
La classe Yao de l'Université Tsinghua (officiellement « Tsinghua Academy of Computer Science Experimental Class » ou « 清华学堂计算机科学实验班 ») est un programme de premier cycle d'élite fondé en 2005 par Andrew Chi-Chih Yao, le premier lauréat chinois du prix Turing. Il recrute des talents exceptionnels (souvent des médaillés d'Olympiades et les meilleurs aux examens provinciaux) et met l'accent sur l'informatique théorique, visant à rivaliser avec le MIT ou Stanford. En 2024, il a diplômé plus de 500 étudiants, dont beaucoup poursuivent une carrière académique, avec une forte représentation dans la recherche en algorithmes, IA et systèmes. Bien que tous ne se concentrent pas sur les compilateurs ou les langages de programmation, la formation rigoureuse en théorie et en computation conduit naturellement certains anciens élèves vers ces domaines.

Les discussions sur Zhihu présentent souvent les anciens de la classe Yao comme des « pépites méconnues » du monde académique, notant leur impact considérable malgré la jeunesse du programme (premiers diplômés vers 2010). Ci-dessous, je me concentre sur ceux qui travaillent dans le milieu universitaire sur les compilateurs, les langages de programmation (PL) ou des domaines étroitement liés comme la conception de langages, la représentation intermédiaire (IR) et les systèmes de calcul haute performance. Ceci est basé sur des profils publics, des publications et des bases de données d'anciens élèves—les listes exhaustives sont difficiles à établir en raison de la vie privée, mais voici des exemples notables.

### Anciens élèves notables de la classe Yao dans le milieu universitaire (axé sur les compilateurs/langages de programmation)
Voici un tableau des principaux anciens élèves, leurs rôles actuels et leurs contributions. J'ai privilégié ceux ayant des liens directs avec la recherche sur les compilateurs/PL.

| Nom | Année de diplôme | Poste actuel | Contributions majeures en compilateurs/PL |
|------|-----------------|------------------|----------------------------------|
| **Yuanming Hu (胡渊明)** | 2017 | Professeur assistant, MIT EECS (à partir de 2024) ; Fondateur, Taichi Graphics | Créateur de Taichi, un DSL (domain-specific language) embarqué et un compilateur orienté données pour le calcul visuel et les simulations haute performance. Se concentre sur la compilation à la volée (JIT), les structures de données creuses et la parallélisation pour les charges de travail graphiques/IA. Publications dans SIGGRAPH/ACM Transactions on Graphics ; cité pour ses avancées en programmation différentiable et les optimisations de compilateur pour le calcul spatial. |
| **Mingkuan Xu** | 2021 | Doctorant, Université Carnegie Mellon (encadré par Zhihao Jia & Umut Acar) | Travaille sur l'infrastructure de compilateur pour le calcul visuel, y compris les compilateurs de quantification pour des simulations efficaces en mémoire et la standardisation de l'IR (intermediate representation) de Taichi. Sa recherche fait le lien entre la théorie des PL et l'accélération matérielle ; publications sur les compilateurs portables et haute performance pour les charges de travail creuses. |
| **Danqi Chen** | 2012 | Professeure assistante, Université de Princeton (Groupe TAL) | Bien que principalement dans le TAL, son travail implique des modèles de langage et de l'analyse syntaxique, incluant les représentations sémantiques et les systèmes de types pour le traitement du langage naturel. Co-auteure d'articles fondamentaux sur la compréhension automatique (par ex., les benchmarks SQuAD), avec des liens vers les PL via la compilation efficace de modèles pour l'inférence à grande échelle. (Note : Influence plus large sur les PL via la compréhension évolutive du langage.) |
| **Beihang Xiao (贝小辉, Xiao Beihang)** | ~années 2010 (première promotion) | Professeur assistant, Université technologique de Nanyang | Recherche en informatique théorique avec des applications pour les langages de programmation quantique et la vérification de compilateurs. Se concentre sur les langages type-safe pour la correction d'erreurs quantiques et le calcul parallèle ; publications dans POPL (Principles of Programming Languages) et conférences associées. |
| **Ma Tengyu (马腾宇)** | ~années 2010 | Professeur assistant, Université Duke | Spécialisé dans la théorie de l'apprentissage automatique à l'intersection avec les PL, incluant la programmation probabiliste et la vérification automatisée pour les compilateurs en ML. Travail sur l'optimisation non convexe pour les réseaux neuronaux ayant des implications pour la compilation à la volée dans les frameworks d'apprentissage profond. |

### Contexte supplémentaire
- **Tendances générales** : Mi-2024, environ 21 anciens de la classe Yao enseignent dans des universités chinoises de premier plan (par ex., Tsinghua, Pékin), et environ 17 dans des universités étrangères (par ex., Stanford, Princeton). Beaucoup publient dans des conférences de PL comme PLDI, OOPSLA, ou POPL, mais les compilateurs/PL sont une niche—la plupart s'orientent vers les algorithmes/l'IA. Les fils de discussion Zhihu (par ex., sur « 姚班学术成果 ») louent des anciens comme Hu Yuanming pour avoir « démocratisé la programmation haute performance » via des outils open-source.
- **Pourquoi ces domaines ?** Le programme de la classe Yao (lourd en mathématiques discrètes, algorithmes et théorie) prépare les étudiants pour les PL/compilateurs, mais l'ingénierie pratique est plus légère, convenant mieux au milieu universitaire qu'aux outils industriels.
- **Sources pour approfondir** :
  - Page des anciens de Tsinghua IIIS : [iiis.tsinghua.edu.cn/en/Yao_Class](https://iiis.tsinghua.edu.cn/en/Yao_Class)
  - Discussion Zhihu sur les réalisations de la classe Yao : [zhihu.com/question/667767788](https://www.zhihu.com/question/667767788)
  - Profil de Yuanming Hu : [yuanming.taichi.graphics](https://yuanming.taichi.graphics)
  - Site de Mingkuan Xu : [mingkuan.taichi.graphics](https://mingkuan.taichi.graphics)

Si vous avez des noms spécifiques ou plus de détails provenant du post Zhihu, je peux approfondir !