---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Auteurs et contributions du Vision Transformer
translated: true
type: note
---

### Présentation des auteurs de « An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale »

L'article fondateur « An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale », présenté en 2020 par Alexey Dosovitskiy et ses collègues de Google, a marqué un tournant décisif dans la vision par ordinateur. Il proposait le Vision Transformer (ViT), un modèle qui applique les architectures de transformateurs – conçues à l'origine pour le traitement du langage naturel – directement à des patches d'images, atteignant des performances de pointe sur des ensembles de données à grande échelle comme ImageNet lorsqu'il était pré-entraîné sur des données massives (par exemple, JFT-300M). Ces travaux ont démontré que des transformeurs purs pouvaient surpasser les réseaux neuronaux convolutifs (CNN) en termes d'efficacité et de précision avec suffisamment de puissance de calcul et de données, influençant les avancées ultérieures en IA multimodale et dans les modèles de vision évolutifs.

L'article fut le fruit d'une collaboration entre 12 chercheurs, principalement de l'équipe zurichoise de Google Brain, alliant des expertises en apprentissage profond, modélisation de séquences et entraînement à grande échelle. Vous trouverez ci-dessous un aperçu des auteurs clés, mettant en lumière leurs parcours et leurs contributions au domaine. (Par souci de concision, je me suis concentré sur les contributeurs principaux ; la liste complète inclut Dirk Weissenborn, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly et Jakob Uszkoreit – tous d'anciens employés de Google ayant une solide expérience dans les transformateurs, l'optimisation et l'intégration vision-langage.)

#### Auteurs clés et parcours

- **Alexey Dosovitskiy** (Auteur principal) : En tant que force motrice derrière ViT, Dosovitskiy a conceptualisé l'idée centrale de traiter les images comme des séquences de patches. Il est titulaire d'un MSc et d'un doctorat en mathématiques de l'Université d'État Lomonosov de Moscou, suivis de travaux postdoctoraux à l'Université de Fribourg sur l'apprentissage de caractéristiques non supervisé. Après avoir rejoint Google Brain en 2019, il a dirigé le développement de ViT avant de partir pour Inceptive (une entreprise d'IA basée à Berlin) en 2021. Ses travaux couvrent la vision par ordinateur, les modèles génératifs et le ML inspiré de la biologie, avec plus de 136 000 citations.

- **Lucas Beyer** : Beyer a joué un rôle crucial dans l'implémentation pratique de ViT, son évaluation sur des benchmarks et les optimisations d'efficacité. D'origine belge, il a étudié le génie mécanique à l'Université RWTH d'Aix-la-Chapelle, obtenant un doctorat en robotique et IA en 2018, axé sur l'IA pour les jeux et l'apprentissage par renforcement. Il a rejoint Google Brain à Zurich après son doctorat, gravissant les échelons pour devenir chercheur principal chez Google DeepMind. En 2025, il est devenu l'une des principales recrues en IA de Meta, poursuivant ses travaux sur les vision transformers et le ML axé sur les données.

- **Alexander Kolesnikov** : Kolesnikov a contribué aux expériences de mise à l'échelle de ViT et aux insights sur l'apprentissage par transfert, en soulignant ses performances sur des ensembles de données de taille moyenne. Il est titulaire d'une maîtrise en mathématiques de l'Université d'État de Moscou et d'un doctorat en apprentissage automatique/vision par ordinateur de l'Institute of Science and Technology Austria (ISTA) en 2018. Entré chez Google Brain en 2018, il a progressé vers des postes de cadre chez DeepMind avant de rejoindre OpenAI puis, en 2025, Meta – où il a été débauché pour son expertise en modèles de vision efficaces.

- **Xiaohua Zhai** : Zhai s'est concentré sur les stratégies de pré-entraînement de ViT et ses extensions multimodales, s'appuyant sur ses travaux en apprentissage de représentations. Il est titulaire d'un doctorat en génie électronique de l'Université de Pékin et a rejoint Google en tant qu'ingénieur logiciel en 2015, passant à la recherche chez Google Brain en 2017 puis chez DeepMind en 2023. Maintenant chercheur chez Meta (via OpenAI Zurich en 2025), ses contributions font le lien entre la vision, le langage et l'apprentissage auto-supervisé, avec plus de 100 000 citations.

- **Neil Houlsby** (Auteur senior) : En tant que responsable d'équipe, Houlsby a supervisé la conception architecturale de ViT et ses implications plus larges pour les lois d'échelle dans la vision. Il a reçu une bourse doctorale européenne Google vers 2010 et a obtenu son doctorat en apprentissage automatique. Chercheur de longue date chez Google depuis ses stages, il a managé des équipes chez Google Brain et DeepMind sur les architectures neuronales et les modèles vision-langage. En 2025, il a rejoint Anthropic pour diriger leur nouveau bureau zurichois, se concentrant sur la mise à l'échelle sécurisée de l'IA.

Cette collaboration de Google Brain (principalement basée à Zurich) a tiré parti de la proximité de l'équipe avec les TPU pour des expériences massives – plus de 25 000 jours-TPU – prouvant la viabilité des transformateurs au-delà du texte. De nombreux auteurs ont depuis rejoint des laboratoires d'IA leaders comme Meta, OpenAI et Anthropic, reflétant l'impact durable de ViT dans le domaine.

#### Références
- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (arXiv)](https://arxiv.org/abs/2010.11929)
- [Alexey Dosovitskiy Google Scholar Profile](https://scholar.google.com/citations?user=FXNJRDoAAAAJ)
- [Lucas Beyer Google Scholar Profile](https://scholar.google.com/citations?user=p2gwhK4AAAAJ)
- [Alexander Kolesnikov Google Scholar Profile](https://scholar.google.com/citations?user=H9I0CVwAAAAJ)
- [Xiaohua Zhai Google Scholar Profile](https://scholar.google.com/citations?user=8gruapYAAAAJ)
- [Neil Houlsby Google Scholar Profile](https://scholar.google.com/citations?user=sm1-TZMAAAAJ)
- [From Ph.D. Detour to Meta's Top AI Hire: Lucas Beyer (Times of India)](https://timesofindia.indiatimes.com/education/news/lucas-beyer-educational-qualification-from-ph-d-detour-and-google-rejection-to-becoming-metas-top-ai-hire/articleshow/122158414.cms)
- [Zuckerberg Poaches Alexander Kolesnikov from OpenAI (Times of India)](https://timesofindia.indiatimes.com/education/news/zuckerberg-poached-alexander-kolesnikov-from-sam-altmans-openai-where-did-this-ai-genius-study/articleshow/122158654.cms)
- [Anthropic Poaches Neil Houlsby from Google DeepMind (Euronews)](https://www.euronews.com/next/2025/02/13/anthropic-poaches-google-deepmind-talent-to-lead-new-european-office)