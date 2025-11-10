---
audio: false
generated: true
image: false
lang: fr
layout: post
title: OpenRouter contre coût direct de l'API
translated: true
type: note
---

Oui, utiliser les API OpenRouter pour accéder aux mêmes modèles est généralement plus coûteux que d'utiliser directement les API officielles des fournisseurs comme DeepSeek, Mistral, Google (pour Gemini) ou xAI (pour Grok). OpenRouter prétend répercuter la tarification du fournisseur sous-jacent sans majoration sur les coûts d'inférence eux-mêmes, mais ils facturent des frais supplémentaires qui augmentent la dépense globale :

- Des frais de 5,5 % (avec un minimum de 0,80 $) lors de l'achat de crédits via les méthodes de paiement standard, plus 5 % supplémentaires pour les paiements en crypto-monnaie.
- Même si vous utilisez vos propres clés API (BYOK) pour les fournisseurs pris en charge, OpenRouter déduit des frais de 5 % (basés sur leur estimation du coût du modèle) de vos crédits OpenRouter.

Ces frais rendent effectivement OpenRouter 5 à 5,5 % plus cher que l'accès direct, en plus des minimums fixes, selon votre utilisation et votre mode de paiement. L'accès direct évite ces suppléments, car vous ne payez que les taux par token du fournisseur.

### Exemples de Comparaison des Coûts
Voici une comparaison approximative basée sur les données de tarification disponibles (en USD par million de tokens ; notez que les taux peuvent varier selon la version du modèle, l'heure, la mise en cache ou la région — vérifiez toujours les sites officiels pour les dernières informations). Les taux de base par token d'OpenRouter correspondent à ceux des fournisseurs (répercutés), mais ajoutent les frais mentionnés ci-dessus.

- **DeepSeek** :
  - Direct : Entrée ~0,14 $–0,55 $ (cache hit/miss), Sortie ~1,10 $–2,19 $ (varie selon le modèle et les périodes de réduction).
  - OpenRouter : Mêmes taux de base + frais de 5–5,5 %.

- **Mistral** :
  - Direct : Entrée ~2,00 $ (pour Large 2), Sortie ~6,00 $ (estimation basée sur des taux moyens ; les modèles plus anciens comme Small étaient ~0,15 $ d'entrée/0,50 $ de sortie).
  - OpenRouter : Mêmes taux de base + frais de 5–5,5 %.

- **Gemini (Google)** :
  - Direct : Varie considérablement selon le modèle (par exemple, Gemini 1.5 Pro : Entrée 1,25 $–2,50 $, Sortie 5,00 $–10,00 $ ; Gemini 1.5 Flash : Entrée 0,075 $–0,15 $, Sortie 0,30 $–0,60 $).
  - OpenRouter : Mêmes taux de base + frais de 5–5,5 % (BYOK peut être pris en charge pour Google).

- **Grok (xAI)** :
  - Pour les détails sur la tarification et l'accès à l'API Grok, visitez https://x.ai/api. Sur la base des informations publiques, les taux sont d'environ Entrée 3,00 $/Sortie 15,00 $ pour Grok-3/Grok-4, ou Entrée 0,30 $/Sortie 0,50 $ pour Grok-3-mini.
  - OpenRouter : Mêmes taux de base + frais de 5–5,5 % (BYOK généralement non mentionné pour xAI).

Si votre utilisation est à volume élevé, les frais en pourcentage s'accumulent rapidement. Pour une utilisation faible ou des tests, la différence pourrait être minime, mais l'accès direct reste moins cher. La valeur d'OpenRouter réside dans son API unifiée et ses fonctionnalités de routage, ce qui peut justifier le coût supplémentaire pour la commodité.

[FAQ OpenRouter](https://openrouter.ai/docs/faq)  
[Tarification de l'API DeepSeek](https://api-docs.deepseek.com/quick_start/pricing)  
[Tarification Mistral AI](https://mistral.ai/pricing)  
[Tarification de l'API Google Gemini](https://ai.google.dev/pricing)  
[API xAI](https://x.ai/api)  
[Analyse de Mistral Large 2](https://artificialanalysis.ai/models/mistral-large-2)  
[Guide des Prix DeepSeek](https://team-gpt.com/blog/deepseek-pricing/)