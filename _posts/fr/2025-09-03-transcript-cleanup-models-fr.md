---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide des meilleurs modèles pour le nettoyage de transcriptions
translated: true
type: note
---

Excellent cas d'usage. Pour le **nettoyage de transcriptions longues avec un formatage strict et « sans commentaires superflus »**, voici ce qui fonctionne le mieux actuellement sur OpenRouter, par scénario.

**Cheval de bataille rapide + économique (EN/zh, fichiers longs) : DeepSeek-V3.1**
Fort dans le suivi des instructions, gère un contexte de 128k, et vous pouvez désactiver le « raisonnement » pour la vitesse ou l'activer lorsque le texte est désordonné. Bonnes performances bilingues pour la suppression des mots de remplissage et des étiquettes d'intervenants cohérentes. ([Docs API DeepSeek][1], [OpenRouter][2])

**Interviews fortement en chinois et expressions familières : Kimi K2 Instruct**
Le K2 (MoE) de Moonshot est particulièrement fluide avec l'argot et le style chinois ; excellent pour les transcriptions en chinois prioritaire tout en conservant les noms techniques intacts. ([OpenRouter][3])

**La meilleure conformité aux instructions d'édition : Claude Sonnet (3.7/4)**
La gamme Sonnet d'Anthropic est excellente pour « produire uniquement le texte raffiné, sans métadonnées », et a tendance à être conservatrice concernant les changements de sens—idéal pour vos contraintes de liste d'étapes. Utilisez Sonnet 4 si disponible ; la version 3.7 performe également bien. ([OpenRouter][4])

**Sessions ultra-longues ou passes uniques sur un projet entier : GPT-5**
Lorsque vous souhaitez pousser de très grands contextes et garder les hallucinations faibles, GPT-5 est le choix le plus sûr parmi les modèles frontières sur OpenRouter (listé avec un très grand contexte ; raisonnement et édition solides). À utiliser pour les transcriptions marathon ou les passes de « polissage » final. ([OpenRouter][5])

**Également solide, mais surveillez les coûts : Gemini 2.5 Pro**
Très compétent en raisonnement et en édition de long contexte. Il est solide pour le raffinement, mais attention au prix/quotas selon votre voie d'approvisionnement. ([OpenRouter][6])

---

### Une recette de routage pratique (sans tableaux)

* **≤128k tokens, mixte EN/zh, la vitesse compte :** DeepSeek-V3.1 (sans raisonnement). Passez au mode raisonnement uniquement lorsque les paragraphes sont chaotiques. ([Docs API DeepSeek][1])
* **Transcriptions principalement en chinois :** Kimi K2 Instruct. ([OpenRouter][3])
* **Comportement strict « d'éditeur » (sans commentaires), ton juridique/finance :** Claude Sonnet. ([OpenRouter][4])
* **Fichiers gigantesques ou polissage final en une seule passe :** GPT-5. ([OpenRouter][5])

---

### Ajustements de code rapides pour le rendre robuste

* **Rendre le modèle sélectionnable** : ajouter un flag CLI `--model` ; par défaut `deepseek-v3.1`.
* **Routage automatique par taille/langue** : détecter le nombre de tokens et le ratio de chinois ; choisir K2 pour le zh-dominant, GPT-5 pour les entrées énormes, Claude pour le mode « édition stricte ».
* **Bascule du raisonnement (DeepSeek)** : ajouter un paramètre pour définir `reasoning.enabled` dans votre appel OpenRouter pour les passages difficiles. ([Docs API DeepSeek][1])
* **Corriger les petits bugs** : ce `print(".1f")` parasite ; et élargir l'expression régulière des étiquettes d'intervenants pour autoriser `A：` (deux-points pleine chasse) et les variantes sans espace.
* **Garde-fous** : si le delta de longueur est >10%, réessayer automatiquement avec un rappel « ne pas supprimer de contenu » ; si aucun `A:`/`B:` n'est trouvé, réessayer automatiquement avec une incitation « étiqueter les intervenants ».

Si vous voulez, je peux réécrire votre script pour ajouter le flag `--model` et la logique de routage intelligent immédiatement.

[1]: https://api-docs.deepseek.com/quick_start/pricing?utm_source=chatgpt.com "Models & Pricing"
[2]: https://openrouter.ai/deepseek/deepseek-chat-v3.1?utm_source=chatgpt.com "DeepSeek V3.1 - API, Providers, Stats"
[3]: https://openrouter.ai/moonshotai/kimi-k2?utm_source=chatgpt.com "Kimi K2 - API, Providers, Stats"
[4]: https://openrouter.ai/anthropic/claude-3.7-sonnet?utm_source=chatgpt.com "Claude 3.7 Sonnet - API, Providers, Stats"
[5]: https://openrouter.ai/openai/gpt-5?utm_source=chatgpt.com "GPT-5 - API, Providers, Stats"
[6]: https://openrouter.ai/google/gemini-2.5-pro?utm_source=chatgpt.com "Gemini 2.5 Pro - API, Providers, Stats"