---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Quantification 4 bits pour des LLM efficaces
translated: true
type: note
---

### Qu'est-ce que la quantification 4-bit (dans le contexte de QLoRA ou GPTQ) ?

La quantification 4-bit est une technique permettant de réduire considérablement l'empreinte mémoire des grands modèles de langage (LLM) en stockant chaque poids en utilisant seulement 4 bits au lieu de la précision habituelle de 16 bits (FP16/BF16) ou 32 bits (FP32).

Modèles normaux (pleine précision) :
- FP32 : 4 octets par paramètre → modèle 7B ≈ 28 Go
- FP16/BF16 : 2 octets par paramètre → modèle 7B ≈ 14 Go

Quantification 4-bit :
- ~0.5 octet par paramètre → modèle 7B ≈ 3,5–4 Go (soit environ 1/4 à 1/8 de la taille originale selon la méthode exacte)

Il existe deux approches majeures en 4-bit couramment utilisées aujourd'hui :

| Méthode | Nom complet | Article principal / année | Cas d'utilisation typique | Caractéristiques principales |
|----------|----------------------------|-------------------|-----------------------------------|---------------------------------------------------------------------------------------|
| GPTQ | GPTQ | 2023 | Quantification post-entraînement (inférence uniquement) | One-shot, très précise, ne nécessite pas de réentraînement. Arrondit les poids en 4-bit après l'entraînement. |
| QLoRA | Quantized Low-Rank Adaptation | 2023 (Juin) | Fine-tuning efficace / instruction tuning | Combine un stockage 4-bit + des adaptateurs LoRA + des optimiseurs paginés. Permet de fine-tuner des modèles 65B+ sur une seule GPU de 24–48 Go. |

#### QLoRA en détail (celle que les gens désignent généralement par "4-bit QLoRA")
QLoRA fait quatre choses astucieuses en même temps :

1. Quantification 4-bit NormalFloat (NF4)
   - Un type de données 4-bit spécial optimisé pour les poids à distribution normale (la plupart des poids des LLM sont ≈ Gaussiens après l'entraînement).
   - Meilleur que le simple INT4 ; théoriquement optimal pour les données normalement distribuées.

2. Double quantification
   - Même les constantes de quantification (facteurs d'échelle) sont quantifiées de FP16 → 8-bit, économisant ainsi quelques Mo supplémentaires.

3. Optimiseurs paginés
   - Les états de l'optimiseur (moments AdamW) sont stockés dans la RAM du CPU et paginés vers le GPU via la mémoire unifiée NVIDIA. Empêche les OOM pendant l'entraînement.

4. Adaptateurs LoRA
   - N'entraîne que de petites matrices de faible rang (r=64 ou moins) tandis que le modèle de base en 4-bit reste gelé.

Résultat : Vous pouvez effectuer un fine-tuning complet d'un modèle Llama/Mistral 65B sur une seule RTX A6000 48 Go, ou même d'un modèle 70B sur une seule A100 80 Go avec QLoRA, alors qu'un fine-tuning normal complet nécessiterait 8×A100 ou plus.

#### GPTQ (celle axée sur l'inférence)
- Effectuée après la fin de l'entraînement.
- Utilise des informations du second ordre (Hessienne) pour minimiser l'erreur d'arrondi lors de la compression des poids en 4-bit.
- Extrêmement précise — généralement une dégradation de perplexité <0.1 par rapport au FP16.
- Populaire avec des outils comme AutoGPTQ, ExLlama, vLLM, et llama.cpp (GGUF a aussi des modes de type GPTQ).

### Gradient Checkpointing (aussi appelé "activation checkpointing")

Une technique d'économie de mémoire complètement distincte utilisée pendant l'entraînement.

Fonctionnement :
- Normalement, la rétropropagation doit stocker toutes les activations intermédiaires de la passe forward → la mémoire croît linéairement avec la profondeur du modèle/la taille du lot/la longueur de la séquence.
- Le Gradient Checkpointing échange de la puissance de calcul contre de la mémoire :
  - Pendant la passe forward, il ne sauvegarde que quelques activations "checkpoint".
  - Pendant la passe backward, il recalcule les activations manquantes à la volée.

Économie de mémoire typique : 50–80% de la mémoire d'activation, au prix d'un entraînement ~20–30% plus lent.

Il est presque toujours utilisé conjointement avec QLoRA ou tout fine-tuning de grand modèle car, même avec des poids en 4-bit, les activations peuvent saturer la mémoire GPU.

### Résumé TL;DR

"Quantification 4-bit (style QLoRA ou GPTQ) + Gradient Checkpointing" est la recette moderne pour :

- Exécuter ou fine-tuner d'énormes modèles (33B, 70B, 405B) sur des GPU grand public ou d'entreprise unique.
- 4-bit style QLoRA → fine-tuning avec une très faible mémoire GPU.
- 4-bit style GPTQ → inférence rapide avec une très faible mémoire GPU.
- Gradient Checkpointing → rend la passe backward réelle possible sur de longues séquences sans OOM.

Ensemble, c'est la raison pour laquelle on voit aujourd'hui des gens fine-tuner Llama-3-70B sur une seule 3090/4090.