---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Inférence LLM efficace avec vLLM
translated: true
type: note
---

### vLLM : Inférence et service efficaces des LLM

vLLM est une bibliothèque open-source conçue pour l'inférence et le service rapides et efficaces en mémoire des grands modèles de langage (LLM). Développée initialement au Sky Computing Lab de l'UC Berkeley, c'est désormais un projet communautaire largement utilisé en production pour déployer des LLM comme Llama ou des variantes de GPT. Son innovation principale est **PagedAttention**, une technique qui traite la mémoire cache clé-valeur (KV) comme des pages de mémoire virtuelle, réduisant le gaspillage et permettant un débit plus élevé en allouant dynamiquement des blocs non contigus.

#### Fonctionnement
- **Traitement par lots continu** : Contrairement aux systèmes traditionnels qui attendent des lots complets, vLLM ajoute et supprime dynamiquement des requêtes en cours d'exécution, minimisant les temps d'inactivité du GPU pendant le décodage.
- **Gestion de la mémoire** : PagedAttention évite la fragmentation dans le cache KV (qui augmente avec la longueur de la séquence), supportant des contextes plus longs sans erreurs de mémoire insuffisante (OOM).
- **Exécution optimisée** : Utilise les graphes CUDA/HIP pour des lancements de noyaux plus rapides, est intégrée à FlashAttention/FlashInfer pour le calcul de l'attention et supporte la quantification (par exemple, AWQ, GPTQ, FP8) pour réduire l'utilisation de la mémoire jusqu'à 4 fois.
- **Fonctionnalités avancées** : Inclut le décodage spéculatif (pour deviner et vérifier les tokens), le préremplissage par blocs (pour les entrées longues), le multi-LoRA (adaptation des modèles à la volée) et le parallélisme distribué (tenseur, pipeline, expert).

vLLM expose un serveur d'API compatible avec OpenAI, s'intègre de manière transparente avec les modèles Hugging Face et fonctionne sur du matériel diversifié (GPU NVIDIA/AMD/Intel, TPU, CPU). C'est idéal pour les scénarios à haut débit, obtenant des accélérations de 2 à 10 fois par rapport aux solutions de base comme Hugging Face Transformers dans les benchmarks de service.

#### Cas d'utilisation principaux
- Service en ligne pour chatbots ou API avec sorties en flux continu.
- Inférence par lots hors ligne pour des tâches comme la synthétisation.
- Passage à l'échelle vers des clusters multi-GPU sans développement personnalisé.

### Ray : Framework unifié pour la mise à l'échelle des applications Python et d'IA

Ray est un framework de calcul distribué open-source qui facilite la mise à l'échelle du code Python — en particulier les charges de travail d'IA/ML — d'une seule machine à des clusters massifs. Créé par Anyscale (ayant des origines à l'UC Berkeley), il abstrait les complexités des systèmes distribués comme l'ordonnancement, la tolérance aux pannes et l'orchestration, permettant aux développeurs de se concentrer sur la logique.

#### Composants principaux
- **Ray Core** : La fondation — des primitives Pythoniques pour les tâches (fonctions parallèles), les acteurs (services avec état) et les objets (partage de données distribué). Il gère automatiquement la mise à l'échelle automatique, les nouvelles tentatives et l'allocation des ressources.
- **Bibliothèques Ray AI** : Des outils spécifiques à un domaine construits sur Core :
  - **Ray Data** : ETL évolutif pour le prétraitement des jeux de données.
  - **Ray Train** : Entraînement distribué avec des intégrations (PyTorch, TensorFlow, Hugging Face).
  - **Ray Tune** : Optimisation des hyperparamètres à grande échelle.
  - **Ray Serve** : Déploiement de modèles pour l'inférence, avec routage, traitement par lots et tests A/B.
  - **RLlib** : Boîte à outils pour l'apprentissage par renforcement.
- **Clusters Ray** : Couche d'infrastructure gérée pour le déploiement sur le cloud (AWS, GCP), Kubernetes ou sur site, avec une mise à l'échelle automatique basée sur la demande.

#### Fonctionnement
Ray s'exécute comme un démon sur les nœuds, formant un cluster avec un nœud principal pour la coordination. Vous décorez les fonctions avec `@ray.remote` pour le parallélisme, et il distribue l'exécution sur les CPU/GPU. Pour le ML, des bibliothèques comme Serve gèrent les points de terminaison HTTP et l'équilibrage de charge, tandis que Core assure une mise à l'échelle tolérante aux pannes (par exemple, redémarrer les tâches échouées).

#### Cas d'utilisation principaux en ML/IA
- Pipelines de bout en bout : Chargement des données → entraînement → réglage → service.
- Balayages d'hyperparamètres sur des centaines de GPU.
- Flottes d'inférence en temps réel, comme dans les systèmes de recommandation.
- Applications distribuées personnalisées, par exemple, des simulations.

La force de Ray est son API unifiée : écrivez une fois, mettez à l'échelle n'importe où, avec moins de code standardisé comparé à Spark ou Dask.

### Relation entre vLLM et Ray
Dans des systèmes comme SLOs-Serve (de notre discussion précédente), vLLM gère le traitement par lots et l'inférence de bas niveau des LLM, tandis que Ray orchestre les déploiements multi-répliques, acheminant les requêtes entre les nœuds pour gérer les pics de charge et la mise à l'échelle.

[Documentation vLLM](https://docs.vllm.ai/en/latest/)  
[Documentation Ray](https://docs.ray.io/en/latest/ray-overview/index.html)