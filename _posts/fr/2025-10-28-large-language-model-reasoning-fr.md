---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Techniques de raisonnement des grands modèles de langage
translated: true
type: note
---

### Aperçu
Denny Zhou (probablement "Danny Zhou" voulu) a donné une conférence intitulée "Le Raisonnement des Grands Modèles de Langage" dans le cadre du cours CS25 de Stanford : Transformers United (Version 5). Il y fournit un aperçu complet du raisonnement dans les grands modèles de langage (LLMs), en mettant l'accent sur les techniques pratiques, les fondements théoriques et les défis actuels. Voici un résumé structuré de ses points clés, tiré directement de ses diapositives et des notes accompagnatrices.

### Définition du raisonnement dans les LLMs
- Le raisonnement dans les LLMs consiste fondamentalement à **générer des tokens intermédiaires** (ou étapes) entre l'invite d'entrée et la sortie finale, plutôt qu'à passer directement à la réponse. Ce processus permet au modèle de décomposer des problèmes complexes.
- Il n'a pas besoin de mimer exactement le raisonnement humain — l'objectif est la résolution efficace de problèmes. Par exemple, résoudre "Quelles sont les deux dernières lettres de 'intelligence artificielle' ?" en concaténant les fins de mots étape par étape donne "le", montrant comment les intermédiaires aident au calcul.
- Fondement théorique : Pour les problèmes résolubles par des circuits booléens de taille *T*, les transformers de taille constante peuvent les traiter en produisant *O(T)* tokens intermédiaires, évitant ainsi un passage à l'échelle massif du modèle.

### Motivations
- Les LLMs pré-entraînés sont intrinsèquement capables de raisonnement sans prompting ou fine-tuning spécial ; le mythe selon lequel ils ne le peuvent pas est réfété — les problèmes proviennent de méthodes de décodage qui ne parviennent pas à faire émerger des sorties raisonnées.
- Cette approche s'aligne sur "The Bitter Lesson" : Tirer parti du calcul (via la génération de tokens) plutôt que des raccourcis de type humain, permettant l'émergence de comportements semblables à ceux des humains grâce à la prédiction du token suivant.
- Se concentrer sur l'optimisation des métriques de l'objectif final comme l'exactitude, en utilisant des données générées par le modèle au lieu d'annotations humaines coûteuses.

### Idées principales
- **Décodage Chaîne de Pensée (CoT)** : Générer plusieurs réponses candidates et sélectionner celle avec la plus haute confiance sur la réponse finale. Les chemins raisonnés ont souvent une confiance plus élevée que les suppositions directes (par exemple, compter des pommes dans un scénario).
- **Passage à l'échelle via la Longueur, pas la Profondeur** : Entraîner les modèles à générer des séquences plus longues (*O(T)* tokens) pour les problèmes sérieels, les rendant arbitrairement puissants sans gonfler la taille du modèle.
- **Agrégation sur les Réponses Uniques** : Générer et combiner plusieurs réponses (par exemple, via un vote majoritaire) surpasse les sorties uniques ; la récupération de problèmes similaires + le raisonnement bat le raisonnement seul.
- Exemple : Le "mode réflexion" de Gemini 2.0 résout des énigmes comme former 2025 avec les nombres 1-10 en prioritisant les opérations (par exemple, 45 × 45 = 2025).

### Techniques clés
- **Prompting** : Utiliser des exemples few-shot ou des phrases comme "Réfléchissons étape par étape" pour susciter des intermédiaires (par exemple, pour les problèmes de mots mathématiques). Le zero-shot fonctionne mais est moins fiable.
- **Supervised Fine-Tuning (SFT)** : Entraîner sur des solutions étape par étape annotées par des humains pour augmenter la probabilité des chemins raisonnés.
- **Auto-amélioration** : Générer vos propres données d'entraînement en filtrant les solutions raisonnées correctes à partir des sorties du modèle.
- **RL Fine-Tuning (ReFT)** : Récompenser itérativement les réponses complètes correctes (raisonnement + réponse) et pénaliser les incorrectes, en utilisant un vérificateur. Cela généralise le mieux pour les tâches vérifiables ; crédit aux membres de l'équipe comme Jonathan Lai.
- **Auto-cohérence** : Échantillonner plusieurs chemins, puis agréger (par exemple, la réponse la plus fréquente). La variante universelle pour les tâches ouvertes permet au modèle de s'auto-sélectionner.
- **Récupération + Raisonnement** : Intégrer des exemples similaires pour amorcer (par exemple, rappeler des formules de distance pour des requêtes de surface).
- **Autres Améliorateurs** : "Take a Step Back" pour l'abstraction ; la marginalisation pour corriger les biais de décodage probabiliste.

### Limitations
- **Prompting** : Simple mais fragile — a besoin d'exemples spécifiques à la tâche ; les prompts génériques sont moins performants.
- **SFT** : Ne généralise pas bien aux problèmes hors distribution (par exemple, échoue sur un nouveau comptage de lettres "strawberry" malgré l'entraînement).
- **RL** : Repose sur des vérificateurs fiables, qui ne sont pas disponibles pour toutes les tâches (par exemple, l'écriture créative).
- **Défis Généraux** : Les LLMs sont des prédicteurs probabilistes, donc le décodage glouton favorise les réponses fluides mais incorrectes. L'agrégation aide mais ne résout pas les domaines non vérifiables.
- Désalignement du décodage : Même les modèles forts peuvent ne pas classer les sorties raisonnées le plus haut sans intervention.

### Directions futures
- Aller au-delà des benchmarks vers des applications réelles, en particulier les tâches non vérifiables (par exemple, l'optimisation de la traduction sans métriques parfaites).
- Passer à l'échelle de l'agrégation et de la récupération pour des gains plus importants.
- Améliorer le décodage (par exemple, via la marginalisation) pour mieux aligner les sorties probabilistes avec l'exactitude.
- Construire des systèmes qui "se souviennent" des chemins de raisonnement réussis entre les sessions.

Cette conférence met en avant le RL fine-tuning comme la méthode la plus puissante actuellement, avec un changement vers une vision du raisonnement comme un problème de génération scalable.

### Références
- [Diapositives sur le Raisonnement des LLMs (PDF)](https://dennyzhou.github.io/LLM-Reasoning-Stanford-CS-25.pdf)
- [Post X de Denny Zhou sur les Points Clés](https://x.com/denny_zhou/status/1948499173986201915)
- [Vidéo de la conférence sur YouTube](https://www.youtube.com/watch?v=ebnX5Ur1hBk)
- [Page du cours CS25](https://web.stanford.edu/class/cs25/)