---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Optimisation du cache des LLM par la structure des invites
translated: true
type: note
---

Comme les grands modèles de langage consomment de plus en plus de tokens, la mise en cache devient de plus en plus importante pour réduire les coûts. Manus (une entreprise/outil que vous avez mentionné) a soulevé une optimisation : fixer l'ordre de sérialisation JSON afin que les requêtes répétées puissent être mises en cache plus efficacement.

Je viens de penser à une autre idée : lors de la construction des prompts ou du contexte, il est préférable de placer les variables ou le contenu dynamique **à la fin**. De cette façon, les premières parties restent stables et peuvent toucher le cache plus régulièrement.

Bien sûr, pour les utilisateurs individuels avec une utilisation relativement faible, cette optimisation n'a pas beaucoup d'importance. Mais pour les entreprises proposant des copilots (où les utilisateurs paient un abonnement forfaitaire par mois), le fournisseur backend (comme Manus, Claude, Code ou Cursor) a besoin d'une technologie de cache robuste afin de contrôler les coûts à grande échelle.

---

✅ Donc oui, votre raisonnement est correct :
- **Un ordre stable** → de meilleurs taux de cache.
- **Le contenu dynamique à la fin** → préserve le préfixe réutilisable plus long.
- **Les services à haut volume (style copilot)** bénéficient beaucoup plus de cette optimisation que les utilisateurs individuels à faible utilisation.

---

👉 Souhaitez-vous que j'explique également quelques **stratégies pratiques de mise en cache** que les entreprises utilisent réellement avec les LLM ?