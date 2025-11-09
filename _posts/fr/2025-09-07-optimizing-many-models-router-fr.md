---
audio: false
date: 2025-09-07
generated: true
image: false
lang: fr
layout: post
title: Optimisation de votre routeur de code multi-modèles
translated: true
type: note
---

Réponse courte : oui — votre « routeur à modèles multiples » peut absolument être moins performant qu’une pile étroitement intégrée comme Codex (l'assistant de codage d'OpenAI) qui est optimisée de bout en bout sur une seule famille de modèles avec un contexte profond de l'IDE. Voici pourquoi et comment y remédier rapidement.

### Pourquoi Codex peut sembler meilleur

* **Un seul cerveau par tâche.** Rester sur un seul modèle préserve son plan latent et son style de codage. Passer d'un modèle à un autre en cours de tâche réinitialise ce plan et introduit souvent des conventions conflictuelles.
* **Intégration verticale.** Codex (OpenAI) contrôle modèle → appels d'outils → index du dépôt → tests → modifications inline. Cette boucle fermée lui donne des signaux plus riches (graphe de symboles, cartes de chaleur des fichiers, tests en échec) avec une latence de code de glue réduite.
* **Alignement prompt + politique.** Leurs prompts, formateurs de code et heuristiques "créer un diff minimal et compilable" sont co-conçus pour la famille GPT-5. Un routeur général peut facilement mal spécifier la température, les séquences d'arrêt ou le format de correctif pour certains modèles.
* **Latence/débit.** Chaque saut supplémentaire (proxy, middleware OpenRouter, négociation de modèle) ajoute du gigue. Les workflows de codage sont sensibles au feedback ; 300 à 800 ms de latence supplémentaire par tour nuisent notablement au « flux ».
* **Qualité du contexte.** Les intégrations IDE qui calculent une carte du dépôt (topologie des fichiers, symboles, changements récents) surpassent le simple « dumping d'un long contexte ». Les longs contextes sans structure gaspillent des tokens et diluent l'attention.

### Ce qui dans votre configuration vous nuit probablement

* **Prolifération des modèles.** Vous mélangez des généralistes, des codeurs et des modèles de raisonnement. Les variantes « thinking » (p. ex., `claude-3.7-sonnet:thinking`, `deepseek-r1`) sont excellentes pour les preuves mais plus lentes et plus bavardes pour les modifications de code.
* **Inadéquation de la route par défaut.** `default: "openrouter,x-ai/grok-code-fast-1"` semble indiquer que vous voulez Grok Code Fast, mais il n'est pas listé dans votre tableau `models`. Cela peut provoquer un basculement silencieux et une incohérence.
* **Intentions non délimitées.** Un seul « default » pour tout signifie que les petites modifications, les refactorisations lourdes et les lectures de contexte longues se disputent toutes le même chemin.
* **Dérive de température/format.** Si vous n'appliquez pas un format de correctif strict et une faible température par modèle, les sorties varient considérablement selon les fournisseurs.

### Rendez votre routeur semblable à Codex

1.  **Choisissez un principal et tenez-vous-en par tâche.** Choisissez un bon codeur comme défaut (p. ex., `openai/gpt-5` ou `x-ai/grok-code-fast-1` ou `qwen/qwen3-coder`) et ne changez que pour des raisons claires (contexte très long ou calculs lourds).
2.  **Répartissez par intention (et non par marque).**

    *   *Petite modification / correction rapide :* modèle rapide (GPT-5-mini ou Gemini-Flash).
    *   *Refactorisation / changement multi-fichiers :* GPT-5 (ou Claude Sonnet 3.7 non-thinking).
    *   *Lecture de contexte ultra-long :* Kimi-K2.
    *   *Raisonnement difficile avant codage :* DeepSeek-R1 pour esquisser → passez la main à un modèle codeur pour produire le correctif.
3.  **Appliquez un contrat de correctif strict.** Demandez toujours un diff unifié ou un JSON explicite "ApplyPatch" avec chemins de fichiers + tronçons. Rejetez tout autre chose et redemandez automatiquement.
4.  **Réduisez l'aléatoire pour le code.** `temperature: 0–0.2`, pas de pénalités de fréquence/présence, et plafonnez `top_p` ~0.9.
5.  **Donnez une carte du dépôt, pas seulement des tokens.** Fournissez un index de symboles compact : points d'entrée, classes/fonctions clés, cibles de test, diffs récents. Cela surpasse le dumping de 200k tokens de fichiers bruts.
6.  **Gardez la boucle outil serrée.** Un modèle propose un correctif → vous exécutez build/tests/linters → renvoyez les échecs au *même* modèle pour itérer. Évitez de changer de modèle en milieu de boucle.
7.  **Réduisez la liste des modèles.** Gardez-en 3 à 5 maximum. Chaque modèle supplémentaire augmente la variance et les erreurs de routage.
8.  **Retirez les modèles « thinking » des chemins critiques.** Utilisez-les uniquement pour produire un bref plan de conception, puis basculez vers un codeur pour les modifications réelles.

### Une configuration plus légère (idée prête à l'emploi ; adaptez les noms à votre framework)

```json
{
  "PROXY_URL": "http://127.0.0.1:7890",
  "LOG": true,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "",
      "models": [
        "openai/gpt-5",
        "openai/gpt-5-mini",
        "x-ai/grok-code-fast-1",
        "moonshotai/kimi-k2",
        "anthropic/claude-3.7-sonnet",
        "qwen/qwen3-coder"
      ],
      "transformer": {"use": ["openrouter"]}
    }
  ],
  "Router": {
    "default": "openrouter,openai/gpt-5",
    "quickEdit": "openrouter,openai/gpt-5-mini",
    "refactor": "openrouter,openai/gpt-5",
    "reasonPlan": "openrouter,anthropic/claude-3.7-sonnet",
    "longContext": "openrouter,moonshotai/kimi-k2",
    "longContextThreshold": 220000,
    "webSearch": "openrouter,qwen/qwen3-coder"
  }
}
```

### Échafaudages de prompt qui stabilisent les sorties (pas de tableaux)

*   **Système :** « Vous êtes un ingénieur logiciel senior. Produisez des correctifs minimaux et compilables. Gardez un style cohérent avec le dépôt. Si vous n'êtes pas sûr, posez une seule question de clarification, sinon procédez. »
*   **Règles :** « Sortez UNIQUEMENT un diff unifié (format git). N'incluez jamais de commentaire. Si un fichier n'existe pas, créez-le et incluez-le dans le diff. Préservez les en-têtes de licence. »
*   **Bloc de contexte :** carte du dépôt (fichiers, symboles clés), erreurs actuelles, cibles de test.
*   **Boucle outil :** après le diff, exécutez automatiquement `build + tests + lints` ; renvoyez uniquement les échecs au même modèle.

### Hygiène pratique

*   Réduisez votre liste de modèles et corrigez la valeur par défaut vers un modèle qui existe réellement dans `models`.
*   Définissez des températures par route ; gardez le code à 0–0.2.
*   Mettez en cache la carte du dépôt entre les tours ; ne renvoyez pas de contextes géants sauf si les fichiers ont changé.
*   Évitez les changements de modèle en cours de tâche.
*   Préférez le « diff » au « remplacer ce fichier entier » pour réduire les imports hallucinés.

Si vous voulez, collez les prompts et les paramètres de température de votre routeur, et je les resserrerai pour chaque route afin que Claude Code et votre pile se comportent de manière plus cohérente avec la fiabilité de type Codex.