---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: NanoChat Compact Full Stack LLM
translated: true
type: note
---

### Qu'est-ce que NanoChat ?

NanoChat est une implémentation compacte et complète d'un système de grand modèle linguistique (LLM) similaire à ChatGPT, construite dans une base de code unique et minimale, facile à bidouiller et nécessitant peu de dépendances. Créé par Andrej Karpathy (célèbre pour ses travaux en IA, comme nanoGPT), il est conçu pour exécuter l'intégralité du pipeline LLM — de la tokenisation et du pré-entraînement au fine-tuning, à l'évaluation, à l'inférence, et même une interface web simple pour discuter avec votre modèle — sur du matériel abordable comme un seul nœud avec 8xH100 GPU.

Il est présenté comme le "meilleur ChatGPT que 100 dollars peuvent acheter", servant de référence pour le développement de LLM économiques (moins de 1 000 dollars au total). Cela en fait un projet de synthèse pour le futur cours LLM101n de Karpathy chez Eureka Labs, privilégiant la simplicité par rapport aux configurations complexes.

### Fonctionnalités principales
- **Pipeline Complet** : Gère tout en ~2 000 lignes de code (avec un tout petit fichier `uv.lock` pour les dépendances). Entraîne un modèle performant avec 4e19 FLOPs en environ 4 heures sur une configuration 8xH100 coûtant ~24$/heure.
- **Interface Similaire à ChatGPT** : Après l'entraînement, lancez un serveur web pour interagir avec votre modèle comme avec le vrai ChatGPT.
- **Rapport d'Évaluation** : Génère automatiquement un `report.md` avec des scores de référence sur des tâches comme ARC-Challenge, GSM8K, HumanEval, MMLU, et plus encore. Par exemple, une exécution type à 100 dollars montre des améliorations progressives à travers les étapes (BASE, MID, SFT, RL) :

| Métrique       | BASE   | MID    | SFT    | RL     |
|----------------|--------|--------|--------|--------|
| CORE           | 0.2219 | -      | -      | -      |
| ARC-Challenge  | -      | 0.2875 | 0.2807 | -      |
| ARC-Easy       | -      | 0.3561 | 0.3876 | -      |
| GSM8K          | -      | 0.0250 | 0.0455 | 0.0758 |
| HumanEval      | -      | 0.0671 | 0.0854 | -      |
| MMLU           | -      | 0.3111 | 0.3151 | -      |
| ChatCORE       | -      | 0.0730 | 0.0884 | -      |

(Temps total : ~3h51m pour l'exécution complète.)
- **Flexibilité Matérielle** : Fonctionne sur Ampere 8xA100 (plus lent), sur des GPU uniques (avec accumulation de gradient automatique), ou sur des configurations à VRAM réduite en ajustant la taille des lots. Utilise PyTorch standard ; adaptable à d'autres appareils avec des ajustements.
- **Sources de Données** : Récupère des données de Hugging Face datasets comme FineWeb et SmolTalk.
- **Extras** : Inclut des tests (par exemple, pour le tokenizer basé sur Rust), et il est facile d'empaqueter l'intégralité du dépôt (~330 Ko) pour l'interroger avec d'autres LLM.

Il s'inspire des projets précédents de Karpathy, nanoGPT et modded-nanoGPT, mais est adapté pour une expérience de chat complète.

### Comment Commencer
Le moyen le plus rapide est le script `speedrun.sh`, qui gère le modèle de niveau 100 dollars de bout en bout sur une machine 8xH100 (par exemple, via Lambda Labs) :

1. Démarrez une instance 8xH100 et clonez le dépôt.
2. Exécutez :
   ```
   bash speedrun.sh
   ```
   (Ou dans une session screen pour la journalisation : `screen -L -Logfile speedrun.log -S speedrun bash speedrun.sh`. Détachez avec Ctrl+A+D et suivez le journal avec `tail`.)

3. Une fois terminé (~4 heures), activez l'environnement (`source .venv/bin/activate`) et servez l'interface utilisateur :
   ```
   python -m scripts.chat_web
   ```
   Ouvrez l'URL locale (par exemple, http://your-ip:8000) pour discuter avec votre modèle. Consultez `report.md` pour les résultats.

Pour des modèles plus grands (par exemple, le niveau 300 dollars en ~12 heures, surpassant GPT-2 sur certains scores), modifiez `speedrun.sh` pour télécharger plus de fragments de données et ajustez la profondeur/la taille des lots. Exécutez les tests avec `python -m pytest tests/test_rustbpe.py -v -s`.

Il est sous licence MIT et ouvert aux contributions pour pousser plus loin les micro-modèles. Pour une explication détaillée, consultez les Discussions du dépôt.

[Dépôt GitHub nanoChat](https://github.com/karpathy/nanochat)