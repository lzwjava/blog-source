---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Questions d'Entretien pour Ingénieur IA Senior 2024-2025
translated: true
type: note
---

Voici les questions d'entretien les plus courantes et typiques que vous rencontrerez pour un poste d'**Ingénieur Senior en IA/Agent/LLM** en 2024–2025, particulièrement dans les entreprises leaders (niveau FAANG, laboratoires d'IA comme Anthropic/OpenAI/xAI, scale-ups comme Adept, Imbue, etc.).

Elles sont regroupées par catégorie et par difficulté (la plupart sont de niveau senior, supposant une compréhension approfondie et une expérience en production).

### Conception Système & Architecture
1. Concevez un système scalable de serving d'inférence pour LLM capable de gérer 10k+ QPS avec une latence p99 <200ms.
2. Comment concevriez-vous un agent IA en temps réel capable de naviguer sur le web, d'utiliser des outils et de maintenir une mémoire à long terme ?
3. Conception d'un pipeline de génération augmentée par retrieval (RAG) à partir de zéro (choix de la base de données vectorielle, chunking, reranking, recherche hybride, évaluation).
4. Comment réduisez-vous le coût d'inférence d'un modèle 70B par un facteur 5–10x tout en maintenant une dégradation de la qualité <2% ?
5. Concevez un framework d'évaluation pour les tâches d'agents ouvertes (ex : shopping web, recherche).
6. Comment construiriez-vous un système multi-agents où les agents collaborent (débat, hiérarchie, etc.) ?

### Fondamentaux des LLM & Utilisation Avancée
- Expliquez le fonctionnement de l'attention from scratch (incluant les Rotary Positional Embeddings, le Grouped-Query Attention, le Sliding Window Attention).
- Pourquoi Llama 3/4 utilise-t-il RoPE au lieu d'ALiBi ? Avantages/inconvénients.
- Dérivez les lois de scaling (Kaplan, Hoffmann "Chinchilla", DeepMind "Emergent Abilities").
- Qu'est-ce qui cause le "lost in the middle" dans les modèles à contexte long ? Comment y remédier ?
- Comparez les architectures Mixture-of-Experts (MoE) (Mixtral, DeepSeek, Grok-1, Qwen-2.5-MoE). Pourquoi la sparsité d'activation est-elle difficile en pratique ?
- Comment fonctionne réellement la quantification (GPTQ, AWQ, SmoothQuant, bitsandbytes) ? Compromis entre 4-bit, 3-bit, 2-bit.
- Quelle est la différence entre RLHF, DPO, KTO, PPO, GRPO, et quand utiliseriez-vous chacune ?

### Agents & Utilisation d'Outils
- Comment implémentez-vous un tool calling / function calling fiable avec le mode JSON vs ReAct vs les outils OpenAI ?
- Expliquez ReAct, Reflexion, ReWOO, Toolformer, DEPS, Chain-of-Verification.
- Comment empêchez-vous les boucles infinies dans l'exécution d'un agent ?
- Comment évaluez-vous la performance d'un agent sur des benchmarks comme GAIA, WebArena, AgentBench ?
- Comment ajouteriez-vous une mémoire à long terme à un agent (vector store vs key-value store vs mémoire épisodique) ?

### Entraînement, Fine-tuning & Alignement
- Parcourez la stack complète de fine-tuning : LoRA, QLoRA, DoRA, LoftQ, LLaMA-Adapter, IA³.
- Comment fonctionne QLoRA sous le capot (NF4, double quantification, optimiseurs paginés) ?
- Vous avez 10k exemples d'instructions de haute qualité et souhaitez fine-tuner un modèle 70B sur 8×H100. Donnez la recette exacte.
- Expliquez constitutional AI, RLAIF, self-critique, supervision du processus vs du résultat.
- Comment détectez-vous et atténuez-vous le reward hacking dans le RLHF ?

### Codage & Implémentation (Live coding ou take-home)
- Implémentez un agent ReAct simple from scratch (Python).
- Implémentez un sliding-window attention efficace avec un cache de style flash-attention.
- Construisez un système RAG basique avec LangChain / LlamaIndex (ils jugeront l'architecture).
- Optimisez une passe forward de transformer pour un contexte de 128k (efficacité mémoire).
- Écrivez une fonction autograd PyTorch personnalisée pour un nouveau noyau de quantification.

### Fondamentaux du ML (ils le demandent encore aux seniors)
- Pourquoi AdamW fonctionne-t-il mieux qu'Adam ? Dérivez la formulation du weight-decay.
- Expliquez le label smoothing, le teacher forcing, les objectifs d'entraînement au niveau de la séquence vs au niveau du token.
- Quelle est la différence entre BLEU, ROUGE, BERTScore, LLM-as-a-judge, G-Eval ?
- Dérivez la fonction de perte du transformer et expliquez pourquoi nous ignorons les tokens de padding.

### Production & MLOps
- Comment surveillez-vous les sorties des LLM en production (dérive, toxicité, fuite de PII, injection de prompt) ?
- Vous constatez que 5% de vos utilisateurs font du jailbreaking du modèle. Comment détectez-vous et défendez-vous ?
- Comparez vLLM, TGI, TensorRT-LLM, lmdeploy, Outlines, Guidance pour la vitesse d'inférence.
- Comment effectuez-vous du fine-tuning continu / de l'apprentissage en ligne en toute sécurité ?

### Comportemental / Expérience
- Parlez-moi du problème de production le plus difficile que vous ayez résolu avec les LLMs.
- Comment avez-vous livré un produit agent que les utilisateurs ont vraiment aimé ?
- Décrivez une fois où vous avez réduit le coût d'inférence de >50%.
- Quel est le pire désastre d'hallucination que vous ayez vu et comment l'avez-vous résolu ?

### Sujets Chauds Actuels (2025)
- Comment fonctionnent les méthodes de scaling au moment du test (DeepSeek R1, le raisonnement de style o1, les process reward models) ?
- Comparez chain-of-thought, tree-of-thought, graph-of-thought, process reward vs outcome reward.
- Quels sont les meilleurs modèles de raisonnement open-source actuels (Llama-3.1-405B, Qwen-2.5-72B-Instruct, DeepSeek-V3, Gemma-2-27B) ?
- Opinions sur les boucles de génération de données synthétiques (Self-Refine, STaR, Quiet-STaR, synthèse de données basée sur MCTS).

Les entreprises qui posent actuellement les questions les plus difficiles : OpenAI, Anthropic, xAI, Adept, Scale AI, Helion, Imbue, Character.AI, Cohere, Mistral.

Préparez-vous à faire du system design au tableau blanc et à coder sur un ordinateur portable (sans internet). La plupart des processus seniors comportent 5 à 7 tours avec beaucoup de system design et de coding en profondeur.

Bonne chance !