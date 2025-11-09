---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Optimiseur MuonClip pour Kimi K2
translated: true
type: note
---

### Aperçu de l'optimiseur Muon

L'optimiseur Muon est un algorithme d'optimisation de pointe mentionné par Zhiling Yang (également connu sous le nom de Yang Zhilin), le fondateur et PDG de Moonshot AI, dans le contexte du développement de leur grand modèle linguistique, Kimi K2[1][2][3]. C'est un optimiseur d'inspiration du second ordre qui utilise des mises à jour de haut rang pour mieux s'adapter à la géométrie de la surface de perte pendant l'entraînement du modèle[2]. Cependant, il présente des problèmes d'instabilité lors de l'entraînement, que Moonshot AI a résolus en créant une version améliorée appelée MuonClip[1][4].

### Caractéristiques principales
- **Efficacité et conception** : Muon vise l'efficacité des tokens, ce qui signifie qu'il traite moins de tokens que les optimiseurs traditionnels comme AdamW tout en obtenant des performances comparables ou supérieures. Il s'inspire des méthodes du second ordre (par exemple, la méthode de Newton) mais s'adapte aux scénarios d'apprentissage profond à grande échelle[2][3].
- **Problèmes de stabilité** : L'optimiseur Muon de base peut provoquer une instabilité lors des longs entraînements, comme des pics de perte, car il est susceptible de diverger dans certaines conditions[2][1].
- **Amélioration MuonClip** : Moonshot AI a introduit MuonClip en intégrant Muon avec une technique "QK-Clip", qui limite les interactions requête-clé dans le mécanisme d'attention pour prévenir l'instabilité. Cela a permis un entraînement stable et sans pics de Kimi K2 sur 15,5 billions de tokens[1][4][5].

### Application dans Kimi K2
MuonClip a été crucial dans le pré-entraînement de Kimi K2, un modèle à architecture Mixture-of-Experts d'un billion de paramètres totaux (32 milliards de paramètres activés). L'optimiseur a permis à Moonshot AI d'atteindre des résultats de pointe dans des benchmarks comme Tau2-Bench (66,1), ACEBench (76,5) et SWE-Bench Verified (65,8) sans pensée étendue[4][6]. Yang a souligné cela comme une percée pour le développement de l'IA open-source, en soulignant son rôle pour rendre l'entraînement à grande échelle plus efficace et stable[7][8].

Pour les détails techniques, reportez-vous à l'article sur Kimi K2 sur arXiv[1][4]. Zhiling Yang en a parlé dans des interviews et des annonces autour de la sortie du modèle en juillet 2025[2][7].

Citations :
[1] https://arxiv.org/pdf/2507.20534?
[2] https://artificialintelligencemadesimple.substack.com/p/kimi-k2-is-the-most-important-model?utm_source=post-email-title&publication_id=1315074&post_id=169438943&utm_campaign=email-post-title&isFreemail=true&r=36rt3&triedRedirect=true&utm_medium=email
[3] https://composio.dev/blog/notes-on-kimi-k2
[4] https://arxiv.org/abs/2507.20534
[5] https://www.hpcwire.com/2025/07/16/chinas-moonshot-ai-releases-trillion-parameter-model-kimi-k2/
[6] https://intuitionlabs.ai/pdfs/analysis-of-the-kimi-k2-open-weight-language-model.pdf
[7] https://www.chinatalk.media/p/kimi-k2-the-open-source-way
[8] https://github.com/MoonshotAI/Kimi-K2