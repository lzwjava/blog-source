---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4.1-fast
title: Aperçu de l'intelligence incarnée
translated: true
type: note
---

### L’intelligence incarnée : un aperçu

L'intelligence incarnée, également appelée IA incarnée, désigne les systèmes d'intelligence artificielle qui sont physiquement situés dans le monde grâce à un corps (par exemple, un robot) et qui apprennent, raisonnent et agissent via une interaction directe avec leur environnement. Contrairement à l'IA traditionnelle, qui traite des données abstraites de manière isolée (par exemple, les modèles de langage comme GPT), l'IA incarnée souligne que la véritable intelligence émerge des boucles sensori-motrices : percevoir le monde, agir sur lui et s'adapter en fonction des retours. Ce paradigme s'inspire des sciences cognitives, où la cognition est considérée comme étant ancrée dans l'incarnation physique plutôt que dans le calcul pur.

Les principes clés incluent :
- **Perception multimodale** : Intégration de la vision, du toucher, de la proprioception, et parfois du langage ou du son.
- **Apprentissage par l'interaction** : Les agents s'améliorent par essais et erreurs dans le monde réel ou dans des simulations de haute fidélité (transfert sim-to-real).
- **Généralisation et adaptation** : Gestion d'environnements non structurés et dynamiques avec des tâches à long horizon, la multimodalité (par exemple, combiner la vision et le langage) et la robustesse aux perturbations.

En 2025, l'IA incarnée a explosé grâce aux modèles de fondation (grands modèles vision-langage pré-entraînés), aux techniques de diffusion et aux jeux de données massifs comme Open X-Embodiment. Elle alimente les progrès dans les robots humanoïdes, la manipulation, la navigation et l'interaction humain-robot. Des défis subsistent en matière de performance en temps réel, de sécurité, d'écarts sim-to-real et de passage à l'échelle pour les tâches en monde ouvert. Les efforts leaders incluent la série RT de Google, OpenVLA et les politiques basées sur la diffusion, visant à créer des robots généralistes.

### Technologies clés : Diffusion Policy, RT-2 et ACT

Ces trois approches représentent l'état de l'art pour l'apprentissage de politiques robotiques (mappings des observations vers les actions) via l'apprentissage par imitation – entraînement sur des démonstrations humaines ou expertes sans récompenses explicites.

#### ACT (Action Chunking with Transformer)
- **Origine** : Introduit en 2023 par Tony Zhao et al. (Covariant.ai, anciennement de UC Berkeley) dans le cadre du système ALOHA pour la manipulation bimanuelle à faible coût.
- **Idée centrale** : Une politique basée sur un transformateur qui prédit des **blocs** d'actions futures (par exemple, 100 étapes à la fois) au lieu d'une action par pas de temps. Cela réduit les erreurs temporelles (accumulation d'erreurs sur de longs horizons) et permet un contrôle fluide et haute fréquence (par exemple, 50 Hz).
- **Architecture** : Utilise un backbone de type Variational Autoencoder (VAE) ou transformateur. Entrée : Images RVB multi-vues + proprioception (états des articulations). Sortie : Positions/vitesses articulaires groupées.
- **Points forts** :
  - Extrêmement efficace en échantillons (apprend des tâches complexes à partir d'environ 50 démonstrations).
  - Capable de fonctionner en temps réel sur du matériel grand public.
  - Excelle dans les tâches précises et dextères (par exemple, enfiler une aiguille, plier du linge) avec des robots low-cost.
- **Limitations** : Principalement basé sur l'imitation ; support intrinsèque moindre pour les instructions langagières ou la généralisation à l'échelle du web sans extensions.
- **Impact dans le monde réel** : Alimente des systèmes comme ALOHA (manipulateurs mobiles) et a été largement adopté pour les tâches bimanuelles.

#### Diffusion Policy
- **Origine** : Article de 2023 par Cheng Chi et al. (Columbia University, Toyota Research Institute, MIT). Étendu dans des travaux comme 3D Diffusion Policy et ScaleDP (jusqu'à 1 milliard de paramètres en 2025).
- **Idée centrale** : Traite les actions du robot comme des échantillons génératifs provenant d'un modèle de diffusion (inspiré par les générateurs d'images comme Stable Diffusion). Commence avec des actions bruitées, les débruite itérativement conditionnées par les observations pour produire des séquences d'actions de haute qualité et multimodales.
- **Architecture** : Modèle de diffusion conditionnel à débruitage (souvent avec des transformateurs). Apprend la "fonction de score" (gradient de la distribution des actions). L'inférence utilise un contrôle à horizon glissant : Planifier une séquence, exécuter la première action, replanifier.
- **Points forts** :
  - Gère naturellement les comportements **multimodaux** (par exemple, plusieurs manières valides de saisir un objet – la diffusion en échantillonne une de manière cohérente sans les moyenner).
  - Robuste aux actions de haute dimension et aux démonstrations bruitées.
  - State-of-the-art sur les benchmarks (amélioration de plus de 46 % par rapport aux méthodes antérieures en 2023 ; toujours compétitif en 2025).
  - Les extensions comme 3D Diffusion Policy utilisent les nuages de points pour une meilleure compréhension 3D.
- **Limitations** : Inférence plus lente (10–100 étapes de débruitage), bien que des optimisations (par exemple, moins d'étapes, distillation) la rendent viable en temps réel.
- **Impact dans le monde réel** : Large utilisation pour la manipulation visuomotrice ; intégré dans des systèmes comme PoCo (composition de politiques) et des modèles scalés.

#### RT-2 (Robotics Transformer 2)
- **Origine** : 2023 par Google DeepMind (s'appuyant sur RT-1). Fait partie de la famille Vision-Language-Action (VLA).
- **Idée centrale** : Co-affiner un grand modèle vision-langage pré-entraîné (par exemple, PaLM-E ou PaLI-X, jusqu'à 55 milliards de paramètres) sur des trajectoires robotiques. Les actions sont tokenisées comme des chaînes de texte, permettant au modèle de sortir des actions directement tout en tirant parti des connaissances à l'échelle du web (images + texte).
- **Architecture** : Transformateur qui prend images + instructions langagières → actions tokenisées. Compétences émergentes issues du pré-entraînement web (par exemple, raisonnement sur les symboles, chain-of-thought).
- **Points forts** :
  - **Généralisation sémantique** : Comprend des commandes nouvelles (par exemple, "ramasse l'animal éteint" → attrape un jouet dinosaure) sans entraînement spécifique au robot.
  - Transfère les connaissances du web à la robotique (par exemple, reconnaît les déchets à partir d'images internet).
  - Jusqu'à 3 fois meilleur sur les compétences émergentes par rapport aux modèles robotiques antérieurs.
- **Limitations** : Modèles volumineux → calcul plus important ; moins précis pour le contrôle dextre de bas niveau par rapport à ACT/Diffusion (meilleur pour le raisonnement de haut niveau).
- **Impact dans le monde réel** : Alimente la collecte de données de la flotte de robots de Google (AutoRT) ; a évolué vers RT-X et s'est intégré aux systèmes ultérieurs.

### Tableau comparatif

| Aspect                  | ACT                                      | Diffusion Policy                          | RT-2                                      |
|-------------------------|------------------------------------------|-------------------------------------------|-------------------------------------------|
| **Méthode principale** | Transformateur + regroupement d'actions (déterministe/régressif) | Diffusion par débruitage (génératif)      | VLA (actions tokenisées dans LLM/VLM)    |
| **Entrée**              | Images multi-vues + proprioception      | Images/nuages de points + proprioception | Images + instructions langagières         |
| **Sortie**             | Actions articulaires groupées           | Séquences d'actions débruitées           | Chaînes d'actions tokenisées              |
| **Point fort clé**     | Efficacité des échantillons, précision, temps réel | Multimodalité, robustesse, expressivité  | Raisonnement sémantique, généralisation depuis les données web |
| **Vitesse d'inférence**| Rapide (passe unique)                   | Plus lente (débruitage itératif)         | Moyenne (transformateur autorégressif)   |
| **Efficacité des données** | Très élevée (~50 démos/tâche)          | Élevée                                   | Moyenne (bénéficie du pré-entraînement web) |
| **Idéal pour**         | Manipulation dextre et précise          | Tâches complexes et multimodales         | Tâches guidées par le langage, nouvelles/émergentes |
| **Amélioration typique du taux de succès (vs. lignes de base)** | Fort sur les benchmarks robotiques réels | +46% (benchmarks 2023)                   | 2–3× sur les compétences émergentes      |
| **Statut 2025**        | Ligne de base pour le matériel low-cost | Monté en puissance jusqu'à des milliards de paramètres | Fondation pour les successeurs OpenVLA/RT-X |

### Leur place dans l'intelligence incarnée

- **ACT et Diffusion Policy** : Politiques visuomotrices pures – excellent dans les compétences sensori-motrices de bas niveau, le "corps" de l'IA incarnée. Elles permettent aux robots d'agir avec fluidité dans le monde physique à partir de pixels bruts.
- **RT-2 (et modèles VLA)** : Pont vers la cognition supérieure – ajoutent le langage pour une interaction et un raisonnement de type humain, poussant vers des agents incarnés généralistes.
- **Les hybrides sont l'avenir** : Les tendances 2025 les combinent (par exemple, OpenVLA = type RT-2 + têtes de diffusion ; OCTO = petits modèles efficaces avec éléments de diffusion). Objectif ultime : Des robots qui perçoivent de manière multimodale, raisonnent avec des LLM/modèles du monde et agissent avec précision via la diffusion/le regroupement.

Ces méthodes ont démocratisé la robotique dextre : Des tâches qui nécessitaient autrefois des années d'ingénierie réussissent maintenant avec des dizaines de démonstrations humaines. Alors que les jeux de données croissent (par exemple, Open X-Embodiment) et que le matériel s'améliore (humanoïdes comme Figure 01, Tesla Optimus), l'IA incarnée s'approche rapidement de robots polyvalents et utiles dans le monde réel.

[Page du projet Diffusion Policy](https://diffusion-policy.cs.columbia.edu/)  
[Annonce RT-2](https://deepmind.google/discover/blog/rt-2-new-model-translates-vision-and-language-into-action/)  
[Article ALOHA / ACT](https://tonyzhaozh.github.io/aloha/)  
[Jeu de données Open X-Embodiment](https://robotics-transformer-x.github.io/)