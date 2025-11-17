---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Compréhension de l'utilisation des FLOPS des modèles
translated: true
type: note
---

Dans NanoGPT, **MFU** signifie **Model FLOPs Utilization**.

Cela vous indique **quelle partie de la capacité de calcul théorique (FLOPs) de votre GPU le modèle utilise réellement pendant l'entraînement**.
Considérez-le comme un indicateur approximatif de « l'efficacité du GPU ».

Voici ce que cela signifie en pratique :

**• MFU de 0 à 20 % :**
Typique pour les petits modèles, les petites tailles de lot, ou lorsque le GPU est sous-utilisé.

**• MFU de 30 à 50 % :**
Très bon pour un modèle modeste sur des GPU grand public.

**• MFU de 50 à 70 % :**
Utilisation très élevée — généralement de grandes tailles de lot, noyaux bien optimisés.

**• MFU de 80 % et plus :**
Proche de la limite ; cela n'arrive que pour les grands modèles avec des noyaux optimisés (FlashAttention, opérations fusionnées, bf16, etc.).

Votre nombre :

```
mfu 10.69%
```

Ceci est normal pour un modèle de 125M de paramètres sur un 4070. Les petits modèles n'utilisent pas pleinement le GPU car :

* Les matmuls sont trop petits pour saturer les SMs
* La taille du lot est petite
* Certains frais généraux (dataloader, Python) dominent
* Le GPU est conçu pour d'énormes multiplications matricielles, pas pour des petites

Si vous voulez augmenter le MFU, vous pouvez essayer :

* D'augmenter la **taille du lot** (nombre maximum de tokens par lot)
* D'augmenter la **taille du modèle**
* D'utiliser **FlashAttention**
* D'utiliser **CUDA graph capture** (déjà utilisé dans les nouvelles configurations)

Mais pour les petits modèles, un MFU d'environ 10 à 20 % est attendu et tout à fait normal.

Si vous le souhaitez, je peux vous aider à lire votre configuration et vous montrer exactement comment votre MFU est lié à votre taille de lot et à votre nombre de paramètres.