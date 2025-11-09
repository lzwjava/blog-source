---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: 'vLLM : Moteur de service de LLM efficace'
translated: true
type: note
---

### Invention de vLLM

vLLM (abréviation de « virtual LLM ») est une bibliothèque open-source conçue pour l'inférence et le service des grands modèles de langage (LLM) à haut débit et à efficacité mémoire. Il a été inventé début 2023 par des chercheurs du Sky Computing Lab du RISELab de l'UC Berkeley. Le projet a commencé comme un moteur d'inférence spécialisé optimisé pour les GPU NVIDIA A100 et un ensemble limité de modèles, abordant des défis clés du service des LLM comme la fragmentation de la mémoire et le faible débit.

Principales étapes initiales :
- **Mi-avril 2023** : Première intégration publique avec FastChat, alimentant les démos Vicuna de LMSYS et Chatbot Arena.
- **Juin 2023** : Version officielle et lancement public du dépôt GitHub.
- **12 septembre 2023** : Article de recherche fondateur, « Efficient Memory Management for Large Language Model Serving with PagedAttention », publié sur arXiv, introduisant le mécanisme central PagedAttention qui permet le traitement par lots continu et un gaspillage du cache KV proche de zéro.

Le dépôt GitHub (vllm-project/vllm) a été créé vers mai-juin 2023, coïncidant avec la poussée de développement initiale.

### Montée en popularité

vLLM a commencé à gagner un traction significative en 2024, évoluant d'un outil de recherche de niche vers la solution de facto pour le service des LLM open-source. Sa popularité a explosé grâce à des ajouts rapides de fonctionnalités (par exemple, la quantification, le décodage spéculatif, le support multi-modal), des expansions matérielles (NVIDIA, AMD, Google TPUs, etc.) et des adoptions en production par des entreprises comme Amazon (alimentant Rufus lors du Prime Day 2024) et LinkedIn.

Indicateurs clés de croissance en 2024 :
- **Étoiles GitHub** : A augmenté de 2,3x, passant de 14 000 (début 2024) à 32 600 (fin 2024).
- **Téléchargements mensuels** : A bondi de 4,5x, passant de 6 000 à 27 000.
- **Utilisation des GPU** : A augmenté d'environ 10x au second semestre 2024.
- **Communauté** : Le nombre de contributeurs a augmenté de 3,9x pour atteindre 740, avec des réunions bi-hebdomadaires et des partenariats (par exemple, NVIDIA, IBM, AWS).

Mi-2024, il comptait environ 20 000 étoiles et était fréquemment discuté dans les communautés d'IA pour surpasser les alternatives en termes de débit. L'élan s'est poursuivi en 2025 :
- A rejoint l'écosystème PyTorch en décembre 2024.
- Est entré en incubation au LF AI & Data en octobre 2024.
- A atteint 50 000 étoiles en juin 2025.

Aujourd'hui (octobre 2025), il compte plus de 55 000 étoiles et supporte près de 100 architectures de modèles, ce qui en fait une pierre angulaire pour les déploiements d'IA scalables.

[Article arXiv sur PagedAttention](https://arxiv.org/abs/2309.06180)  
[Dépôt GitHub vLLM](https://github.com/vllm-project/vllm)  
[Billet de blog Rétrospective 2024 de vLLM](https://blog.vllm.ai/2025/01/10/vllm-2024-wrapped-2025-vision.html)  
[Annonce d'intégration PyTorch](https://pytorch.org/blog/vllm-joins-pytorch/)