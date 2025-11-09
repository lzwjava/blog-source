---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Modèle IA Open-Source MiniMax M2
translated: true
type: note
---

### Qu’est-ce que MiniMax M2 ?

MiniMax M2 est un nouveau grand modèle de langage (LLM) open-source publié par MiniMax AI, une entreprise chinoise d'IA spécialisée dans les modèles de fond pour le texte, l'audio, l'image et la vidéo. Lancé il y a seulement quelques heures (au 27 octobre 2025), c'est un modèle de type Mixture of Experts (MoE) optimisé pour le codage et les workflows agentiques — pensez à des agents IA autonomes qui planifient, exécutent des outils et gèrent des tâches complexes comme le développement full-stack, l'analyse de données ou la recherche en plusieurs étapes. Ce n'est pas un généraliste comme GPT ou Claude, mais il excelle dans les applications de programmation et d'agents de bout en bout, s'intégrant parfaitement à des outils comme Claude Code, Cursor ou des interpréteurs navigateur/shell.

Spécifications clés :
- **Paramètres** : 230 milliards au total, mais seulement 10 milliards actifs (pour l'efficacité).
- **Longueur de contexte** : Jusqu'à 128K tokens.
- **Déploiement** : Disponible sur Hugging Face sous licence MIT ; prend en charge des frameworks comme SGLang et vLLM pour l'auto-hébergement.
- **Accès** : Essai API gratuit jusqu'au 7 novembre 2025 via MiniMax Agent (agent.minimax.io). L'API payante est à 0,30 $ par million de tokens en entrée et 1,20 $ par million de tokens en sortie — environ 8 % du coût de Claude 3.5 Sonnet.

Il est alimenté par une approche de "pensée entrelacée" (utilisant des balises `