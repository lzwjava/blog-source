---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4.1-fast
title: Principaux chercheurs en IA incarnée
translated: true
type: note
---

### Chercheurs et influenceurs majeurs en IA incarnée (Focus sur Diffusion Policy, RT-2/RT-X, ACT, OpenVLA, Octo et modèles VLA associés)

Le domaine de l'IA incarnée — en particulier les modèles vision-langage-action (VLA), les politiques basées sur la diffusion et l'apprentissage par imitation pour la robotique — a récemment explosé. Voici les "stars pédagogiques" actuelles (chercheurs techniques qui partagent activement des idées, du code, des articles et des explications). Ce sont les équivalents les plus proches d'Andrej Karpathy dans cette niche : des experts approfondis qui rendent la robotique complexe accessible via des conférences, des blogs, des tweets ou des versions open-source.

#### Sur X (Twitter) – Comptes à suivre absolument
Ces personnes publient des mises à jour fréquentes sur les nouveaux articles, les versions de code, les démos de robots et les analyses techniques :

- **@JimFan** (Jim Fan (Chercheur principal chez NVIDIA) – Extrêmement actif et perspicace. Publie sur les modèles de fondation pour la robotique, les lois d'échelle VLA, RT-X/Open X-Embodiment, les politiques de diffusion et les robots humanoïdes. L'un des meilleurs pour le commentaire en temps réel sur le domaine.
- **@SergeyLevine10** Sergey Levine (UC Berkeley) – Professeur dont le labo (BAIR/RAIL) a été un pionnier d'Octo, a co-dirigé OpenVLA et RT-X/Open X-Embodiment. Partage les annonces d'articles, les vidéos de robots et des fils de discussion approfondis sur les politiques d'imitation/de diffusion.
- **@chelseabfinn** Chelsea Finn (Stanford) – Professeure à Stanford, co-responsable d'OpenVLA et de nombreux articles sur les modèles VLA/fondation. Excellente pour les explications de haut niveau et les nouvelles versions.
- **@pieterabbeel** Pieter Abbeel (UC Berkeley) – Pionnier du RL profond et de l'apprentissage par imitation ; son laboratoire a produit des travaux précurseurs menant au chunking de type ACT et aux politiques modernes.
- **@_akhaliq** Akshay (Akhaliq) – N'est pas un chercheur central mais gère les fils de discussion quotidiens "Papers with Code" ; met en lumière chaque nouvel article sur l'IA incarnée (variantes de Diffusion Policy, modèles VLA, etc.) avec des liens et des résumés rapides.
- **@covariantai** Covariant AI (compte de l'entreprise, fondé par Pieter Abbeel et d'autres) – Partage les déploiements réels de modèles de type RT-X dans les entrepôts.
- **@shuransong** Shuran Song (Stanford/Columbia) – Responsable de Diffusion Policy ; publie sur les politiques visuomotrices et la nouvelle diffusion en robotique.
- **@TonyZhaozh** Tony Zhao (Doctorant à UC Berkeley) – Premier auteur d'ACT (Action Chunking Transformer) et de nombreux travaux qui ont suivi ; très actif avec les versions de code et les explications.
- **@karolhausman** Karol Hausman (Google DeepMind) – Contributeur principal à RT-1/RT-2/RT-X ; publie sur les avancées de Google Robotics.
- **@lerobot_hugging** LeRobot (Équipe robotique de Hugging Face) – Publie les versions open-source, les tutoriels et les comparaisons d'OpenVLA, Octo, Diffusion Policy, etc.

Autres comptes à suivre recommandés : @feifei_li (Fei-Fei Li, marraine de "l'intelligence visuelle", impliquée dans les travaux sur l'IA incarnée), @drjimfan à nouveau pour la diversité des sujets.

#### Chaînes YouTube et Blogueurs Techniques
Le bon contenu technique YouTube sur l'IA incarnée émerge encore (la plupart sont des séminaires ou de courtes démonstrations), mais voici les meilleures sources pour des analyses approfondies :

- **Montréal Robotics and Embodied AI Lab (MILA)** – Chaîne officielle avec des séminaires de chercheurs de premier plan (Sergey Levine, Chelsea Finn, Pieter Abbeel y parlent fréquemment).
- **UC Berkeley BAIR Robotics** – Série de séminaires avec des conférences sur Octo, Diffusion Policy, ACT, OpenVLA, etc. De nombreuses vidéos s'intitulent "Octo: An Open-Source Generalist Robot Policy" ou similaire.
- **Stanford Vision and Learning Lab (SVL)** & **Stanford AI Lab** – Chelsea Finn et d'autres donnent des conférences détaillées sur OpenVLA et la mise à l'échelle des VLA.
- **Google DeepMind Robotics** – Vidéos longues occasionnelles sur RT-2, RT-X et AutoRT (leur système de collecte de données).
- **Hugging Face (section/chaîne LeRobot)** – Tutoriels pratiques sur l'exécution d'OpenVLA, Octo, Diffusion Policy en simulation/sur de vrais robots. Très pratique avec le code.
- **Yannic Kilcher** – Pas spécifique à la robotique, mais il fait des revues approfondies d'articles (y compris RT-2, OpenVLA, Diffusion Policy) avec des explications de code.
- **Outlier (par Daniel Bashir)** – Interviews de type podcast avec des chercheurs en IA incarnée (par exemple, Sergey Levine, Chelsea Finn, Jim Fan).

Pour plus de contenu de type séminaire, recherchez sur YouTube "RSS 2024 robotics" ou "CoRL 2024" — presque tous les articles majeurs (OpenVLA, Octo, variantes de Diffusion Policy) ont une vidéo de présentation de 10 à 15 minutes.

#### Laboratoires / Projets clés à surveiller (Ils publient du matériel pédagogique)
- **UC Berkeley BAIR/RAIL** (Sergey Levine) → Octo, parties d'OpenVLA, de nombreux articles sur la diffusion/l'imitation.
- **Stanford Improbable AI Lab** (Chelsea Finn, Jeannette Bohg) → Laboratoire principal d'OpenVLA.
- **Google DeepMind Robotics** → RT-2, RT-X, AutoRT.
- **Columbia Shuransong Lab** → Diffusion Policy original.
- **Physical Intelligence (modèles π0)** → Nouvelles politiques de diffusion + VLM ; très actif sur X.
- **Hugging Face LeRobot** → Démocratise tout ce qui précède avec du code open-source et des notebooks.

Si vous voulez apprendre par la pratique, commencez par le dépôt Hugging Face LeRobot — il contient des modèles pré-entraînés OpenVLA, Octo et Diffusion Policy que vous pouvez exécuter en quelques minutes.

Ce sont les "stars" actuelles qui font avancer le domaine avec du code open-source, des blogs détaillés et des explications publiques — dans un esprit très similaire aux conférences de Karpathy mais axé sur les robots au lieu des LLM. Le domaine évolue incroyablement vite (plusieurs articles révolutionnaires chaque mois), donc suivre les comptes X ci-dessus est le meilleur moyen de rester à jour.