---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Les modèles d'IA de SenseTime sont à la traîne par rapport à leurs rivaux
translated: true
type: note
---

### Comprendre les modèles DayDayNew et Riri Xin de SenseTime

SenseTime, l'un des « dragons de l'IA » chinois, est un leader dans le domaine de la vision par ordinateur et de la reconnaissance faciale depuis 2014. À l'ère de l'IA générative, l'entreprise s'est tournée vers les grands modèles de langage (LLM) sous la bannière SenseNova. « DayDayNew » (souvent stylisé « 日日新 » en chinois) fait référence à leur plateforme d'IA interactive et à leur série de modèles, la dernière version, DayDayNew 6.5, ayant été dévoilée lors de la Conférence mondiale sur l'intelligence artificielle (WAIC) fin octobre 2025. Il est conçu pour des tâches multimodales comme le traitement de texte, d'images et de vidéos, avec un accent marqué sur les applications entreprises, les intégrations d'API et les liens matériels (par exemple, les lunettes IA Xiaomi). « Riri Xin » (modèle intégré 日日新) est un LLM multimodal léger apparenté, lancé plus tôt en 2025, qui se concentre sur le raisonnement profond, la génération cross-modale et l'efficacité pour les appareils grand public.

Ces modèles visent à rivaliser dans le paysage hyper-compétitif de l'IA en Chine, mais ils ont effectivement pris du retard dans les benchmarks de performance brute par rapport aux acteurs de pointe comme DeepSeek (DeepSeek-V3), Kimi (la série Kimi de Moonshot AI) et MiniMax (série ABAB). Pour contexte, mi-2025, les benchmarks SuperCLUE (une évaluation clé des LLM chinois pour le raisonnement, les mathématiques et les capacités générales) plaçaient DeepSeek-V3 en tête des scores globaux (~85/100), Kimi K2 à ~82, et MiniMax ABAB à ~80, tandis que les variantes SenseNova (incluant les intégrations Riri Xin) se situaient autour de 70-75, perdant souvent face à MiniMax dans les tâches de raisonnement et de codage. Des écarts similaires apparaissent dans les évaluations globales comme MMLU ou HumanEval, où SenseTime privilégie le multimodal par rapport au raisonnement textuel pur.

### Pourquoi ce retard par rapport à DeepSeek, Kimi et MiniMax ?

Plusieurs facteurs l'expliquent, ancrés dans l'héritage de SenseTime, la dynamique du marché et les pressions externes :

1.  **Pivot tardif de la vision par ordinateur vers les LLM** : SenseTime a bâti son empire sur l'IA de perception (ex. : technologie de surveillance), n'entrant pleinement dans les LLM génératifs qu'avec SenseNova en 2023. Ce retard a ralenti leur mise à l'échelle par rapport aux startups natives LLM. DeepSeek (fondé en 2023) et Moonshot AI (Kimi, 2023) ont commencé avec une concentration laser sur des modèles efficaces et open-weight, itérant rapidement sur des architectures comme l'attention sparse pour un entraînement rentable. MiniMax, bien que plus jeune (2021), a optimisé dès le premier jour pour les applications grand public comme la génération vidéo (Hailuo).

2.  **Sanctions de la liste des entités américaines** : Inscrite sur la liste noire des États-Unis en 2019 pour de présumées questions de droits de l'homme, SenseTime voit son accès aux puces avancées (ex. : GPU NVIDIA) et à la technologie américaine restreint. Cela entrave l'entraînement à l'échelle des rivaux — DeepSeek utilise de manière innovante les puces Huawei Ascend domestiques, tandis que Kimi et MiniMax exploitent des configurations hybrides sans les mêmes restrictions à l'exportation. Résultat : des mises à jour de modèles plus lentes et des coûts plus élevés, élargissant l'écart de performance.

3.  **Startups agiles contre géant établi** : SenseTime est une société cotée (HKEX) avec un chiffre d'affaires d'environ 1 milliard de dollars+, servant des clients entreprises (ex. : banques, gouvernements). Cela entraîne une certaine bureaucratie et une focalisation sur des solutions multimodales conformes plutôt que sur les benchmarks de pointe. En contraste :
    - DeepSeek met l'accent sur des modèles « rapides, bon marché, ouverts », dominant les classements open-source avec de faibles coûts d'inférence.
    - Kimi excelle dans le raisonnement à long contexte (jusqu'à 200K tokens), rivalisant avec l'o1 d'OpenAI.
    - MiniMax brille dans le multimodal (texte-à-vidéo) et l'efficacité, battant souvent SenseTime en confrontation directe.

    Ironiquement, les fondateurs de MiniMax (Yan Junjie et Zhou Yucong) sont d'anciens ingénieurs de SenseTime qui y dirigeaient les chaînes d'outils de deep learning. Ils sont partis pour créer une startup plus agile, emportant cette expertise pour devancer leur ancien employeur — illustrant comment la mobilité des talents alimente la course aux armements de l'IA en Chine.

4.  **Dynamique des benchmarks et du battage médiatique** : Les évaluations chinoises comme SuperCLUE récompensent le raisonnement/les maths, domaines où les startups se surinvestissent. La force de SenseTime est l'intégration (ex. : le cloud SenseCore pour le fine-tuning), mais ils sous-performent dans les tests « frontières ». Moins de battage médiatique signifie moins d'utilisateurs/de données pour l'itération, créant une boucle de rétroaction. En octobre 2025, SenseTime détient environ 14 % de part de marché AIGC (top 3), mais c'est en termes de revenus, pas de capacité.

### Actualités récentes et ce que SenseTime a fait

L'actualité de SenseTime a été plus discrète que la frénésie des startups (ex. : la sortie virale de R1 de DeepSeek), mais l'entreprise est active dans la croissance de l'IA générative et entreprise :

-   **Avril 2025** : Lancement de SenseNova V6 Omni, le modèle multimodal « le plus avancé » de Chine selon leurs dires, avec des améliorations de l'infrastructure SenseCore 2.0 pour une meilleure compréhension des modèles.
-   **Juin 2025** : A rejoint ByteDance/Alibaba dans les mises à jour de modèles au milieu de la course à l'IA, en mettant l'accent sur des API rentables.
-   **Août 2025** : La plateforme DayDayNew intégrée aux lunettes IA Xiaomi ; les revenus ont bondi de 21 % en glissement annuel grâce à la demande d'IA générative (services d'entraînement/d'inférence).
-   **Septembre 2025** : Scission d'unités non essentielles pour recentrer l'effort sur l'IA générative, visant la rentabilité.
-   **Octobre 2025** : Présentation de DayDayNew 6.5 et de la plateforme Mynie à la WAIC, renforçant l'interaction multimodale (ex. : +30 % de compréhension vidéo).

Ils redoublent d'efforts sur le B2B (ex. : services cloud, intégrations matérielles) plutôt que sur les chatbots grand public, ce qui explique l'impression de « pas de nouvelles » — moins de démos virales, plus de victoires discrètes en entreprise. Néanmoins, avec les discussions d'assouplissement des sanctions et les progrès des puces domestiques, ils pourraient combler leur retard d'ici 2026.

En bref, l'héritage de SenseTime pèse dans une course de vitesse dominée par les startups, mais leur pari multimodal les positionne pour des victoires pratiques plutôt que pour la seule course aux benchmarks.

[ChinAI #324 : Benchmarks SuperCLUE — Bilan de mi-2025](https://chinai.substack.com/p/chinai-324-superclue-large-model)  
[Les modèles de base SenseNova de SenseTime parmi les trois premiers](https://www.sensetime.com/en/news-detail/51169429?categoryId=1072)  
[Aperçu des tigres de l'IA chinois](https://www.topbots.com/chinese-ai-tigers-overview/)  
[La chinoise SenseTime se restructure pour se concentrer sur la croissance de l'IA générative](https://www.reuters.com/technology/artificial-intelligence/chinas-sensetime-reshapes-focus-generative-ai-growth-2024-12-04/)  
[SenseTime dévoile le modèle IA DayDayNew 6.5](https://forntend-test-5sqwmq-3a22a9-107-172-80-230.traefik.me/sensetime-unveils-daydaynew-6-5-ai-model-and-mynie-platform-1753705726167)