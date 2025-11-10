---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Métriques d'Achèvement du Sonnet de Claude 4 Expliquées
translated: true
type: note
---

Version courte : cela s'est terminé normalement.
`finish_reason: "stop"` signifie que le modèle a atteint une fin naturelle de sa réponse (a rencontré une séquence d'arrêt comme le token de fin d'assistant) et n'a **pas** atteint une limite de longueur, rencontré une erreur, ou été annulé.

Voici ce que le reste de cet enregistrement vous indique, en langage clair :

* **Modèle & route**
  Vous avez appelé **anthropic/claude-4-sonnet-20250522** via **Google Vertex** (`provider_name: "Google"`). C'est pourquoi vous voyez une entrée `provider_responses` avec le statut 200.

* **Timing / vitesse**

  * `latency: 2850` → \~2.85 s jusqu'à l'apparition du **premier token**.
  * `generation_time: 76365` → environ **76.4 s** au total pour terminer la réponse.
  * Avec `tokens_completion: 2376`, cela représente un débit d'environ **31 tokens/sec** sur l'ensemble de la génération (2376 ÷ 76.4 ≈ 31.1).

* **Comptes de tokens (deux jeux)**

  * `tokens_prompt: 8446`, `tokens_completion: 2376` → les comptes de votre agrégateur.
  * `native_tokens_prompt: 9007`, `native_tokens_completion: 2511` → le propre comptabilisation / tokeniseur du **provider**. Ceux-ci diffèrent souvent en raison de tokeniseurs différents, de wrappers système, ou de tokens de contrôle cachés.
  * `native_tokens_reasoning: 0` → cette exécution n'a pas utilisé un compteur de "tokens de raisonnement" (certains providers l'exposent lorsqu'un mode raisonnement spécial est activé).
  * `native_tokens_cached: 0` → aucun hit de cache de prompt.

* **Streaming & annulation**

  * `streamed: true` → les tokens vous ont été streamés.
  * `cancelled: false` → vous ne l'avez pas interrompu.

* **Pourquoi pas "length" ?**
  S'il avait atteint la limite maximale de tokens, vous auriez vu `finish_reason: "length"`. Ce n'est pas le cas, donc le modèle a terminé avant d'atteindre une quelconque limite.

* **Quand est-ce arrivé ?**
  `created_at: "2025-09-02T17:26:45.92824+00:00"` (UTC). Dans votre fuseau horaire (Asia/Taipei, UTC+8), c'est le **2025-09-03 01:26:45**.

* **Champs de coûts/utilisation**

  * `usage: 0.064686` → la métrique de coût/utilisation de votre système (les unités dépendent de votre couche de facturation).
  * Plusieurs champs `null` signifient simplement que votre routeur n'a pas enregistré de détails supplémentaires (latence de modération, résultats de recherche, etc.).

* **Divers**

  * `finish_reason: "stop"` (encore) est la clé : arrêt normal via un token d'arrêt.
  * `origin: ""`, `app_id: null` → aucune étiquette d'application spécifique.
  * `is_byok: false` → pas un appel avec apport de sa propre clé (bring-your-own-key).

Si vous le souhaitez, collez un second exemple où vous avez vu `length` ou `cancelled`, et je les comparerai ligne par ligne (sans tableaux).