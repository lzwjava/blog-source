---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration du routeur LLM GitHub Copilot
translated: true
type: note
---

Pour configurer votre routeur LLM afin d'utiliser exclusivement l'API LLM de GitHub Copilot dans un environnement d'entreprise, ajoutez un fournisseur dédié pour celui-ci et ajustez les paramètres du routeur pour acheminer tout le trafic via ce fournisseur.

- **Ajouter un Fournisseur GitHub Copilot** : Incluez une nouvelle entrée dans le tableau "Providers" avec l'URL de base de l'API appropriée, votre jeton d'accès personnel (PAT) GitHub comme clé API, et les modèles pris en charge.
- **Mettre à Jour les Paramètres par Défaut du Routeur** : Modifiez tous les champs du routeur (par exemple, "default", "think") pour qu'ils pointent uniquement vers le nouveau nom du fournisseur, garantissant qu'aucun autre fournisseur n'est appelé.
- **Gérer les Restrictions d'Entreprise** : Utilisez le PAT de votre compte GitHub d'entreprise avec les scopes nécessaires, et utilisez la "PROXY_URL" existante si votre environnement nécessite un routage par proxy pour la conformité.
- **Tester et Vérifier** : Après les mises à jour, validez que tous les appels d'API sont dirigés uniquement vers le point de terminaison Copilot pour se conformer aux politiques autorisant uniquement les interactions avec l'API Copilot.

### Configuration Étape par Étape
1. **Générer un PAT GitHub** : Connectez-vous à votre compte GitHub d'entreprise et créez un jeton d'accès personnel avec des scopes comme `copilot` pour l'accès au chat ou `models:read` pour une inférence de modèle plus large. Cela garantit une authentification sécurisée sans exposer des permissions plus étendues.
2. **Modifier le Tableau des Fournisseurs** : Ajoutez un nouvel objet à la liste "Providers" dans votre JSON de configuration. Définissez "name" sur quelque chose de descriptif comme "github_copilot", "api_base_url" sur "https://api.githubcopilot.com/chat/completions" (pour les agents Copilot) ou "https://models.github.ai/inference/chat/completions" (pour l'inférence générale des GitHub Models), "api_key" sur votre PAT, et listez les modèles compatibles.
3. **Ajuster la Section Routeur** : Remplacez toutes les valeurs dans l'objet "Router" par votre nouveau nom de fournisseur (par exemple, "github_copilot") pour imposer une utilisation exclusive. Cela empêche le recours à d'autres fournisseurs comme OpenRouter.
4. **Considérations pour l'Entreprise** : Dans les environnements restreints, confirmez que vos politiques réseau autorisent les appels sortants vers les domaines de GitHub. Si nécessaire, mettez à jour "PROXY_URL" pour router via un proxy d'entreprise approuvé. Activez la journalisation ("LOG": true) pour auditer les appels et garantir la conformité.

### Exemple de Configuration Mise à Jour
Voici à quoi votre configuration pourrait ressembler après les modifications (remplacez les espaces réservés par votre PAT réel et le point de terminaison préféré) :

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
        "moonshotai/kimi-k2",
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking",
        "anthropic/claude-opus-4",
        "google/gemini-2.5-flash",
        "google/gemini-2.5-pro",
        "deepseek/deepseek-chat-v3.1",
        "deepseek/deepseek-r1",
        "mistralai/mistral-medium-3.1",
        "qwen/qwen3-coder",
        "openai/gpt-oss-120b",
        "openai/gpt-5",
        "z-ai/glm-4.6",
        "x-ai/grok-code-fast-1",
        "x-ai/grok-4-fast",
        "minimax/minimax-m2",
        "moonshotai/kimi-k2-thinking"
      ],
      "transformer": {
        "use": [
          "openrouter"
        ]
      }
    },
    {
      "name": "github_copilot",
      "api_base_url": "https://api.githubcopilot.com/chat/completions",
      "api_key": "ghp_YourPersonalAccessTokenHere",
      "models": [
        "gpt-4o",
        "gpt-4o-mini",
        "claude-3-5-sonnet-20240620"
      ],
      "transformer": {
        "use": [
          "github_copilot"
        ]
      }
    }
  ],
  "Router": {
    "default": "github_copilot",
    "background": "github_copilot",
    "think": "github_copilot",
    "longContext": "github_copilot",
    "longContextThreshold": 30000,
    "webSearch": "github_copilot"
  }
}
```

Cette configuration garantit que le routeur n'interagit qu'avec l'API Copilot, se conformant aux politiques d'entreprise qui restreignent les appels aux points de terminaison approuvés.

---

Dans les environnements d'entreprise, l'intégration d'API LLM comme GitHub Copilot nécessite une configuration minutieuse pour respecter les politiques de sécurité, limitant souvent les appels sortants à des services spécifiques approuvés. La configuration de routeur fournie semble être une configuration personnalisée pour acheminer les requêtes LLM entre différents fournisseurs, similaire à des outils comme OpenRouter ou LiteLLM, où "Providers" définit les points de terminaison d'API et les modèles, et "Router" dicte le routage spécifique à une catégorie ou le repli. Pour l'adapter à l'utilisation exclusive de l'API LLM de GitHub Copilot—en s'assurant qu'aucun autre service externe n'est invoqué—vous devrez intégrer Copilot en tant que fournisseur et l'imposer sur tous les chemins du routeur. Cette approche prend en charge les scénarios où les pare-feux d'entreprise ou les règles de conformité n'autorisent que les API hébergées par GitHub, en tirant parti de l'interface compatible OpenAI de Copilot pour les complétions de chat.

GitHub Copilot fournit un accès LLM principalement via deux canaux : le point de terminaison LLM dédié à Copilot pour créer des agents et des extensions, et l'API GitHub Models plus large pour l'inférence générale. Le point de terminaison spécifique à Copilot à `https://api.githubcopilot.com/chat/completions` est conçu pour le développement d'agents de qualité entreprise, prenant en charge les requêtes POST au format OpenAI de complétion de chat. L'authentification utilise un jeton Bearer dérivé d'un jeton d'accès personnel (PAT) GitHub, généralement passé via un en-tête `Authorization`. Par exemple, une requête type peut inclure des en-têtes comme `Authorization: Bearer <votre-pat>` et `Content-Type: application/json`, avec un corps contenant `messages` (un tableau d'invites utilisateur/système) et des paramètres optionnels comme `stream: true` pour des réponses en temps réel. Les modèles ne sont pas explicitement listés dans la documentation mais correspondent aux fournisseurs sous-jacents de Copilot, tels que les variantes de GPT-4 et les modèles Claude, avec des limites de taux strictes appliquées aux agents tiers pour prévenir les abus.

Alternativement, l'API GitHub Models à `https://models.github.ai/inference/chat/completions` offre un service d'inférence plus polyvalent, permettant l'accès à un catalogue de modèles en utilisant simplement les identifiants GitHub. Ceci est idéal pour le prototypage et l'intégration dans des flux de travail comme GitHub Actions. L'authentification nécessite un PAT avec le scope `models:read`, créé via vos paramètres GitHub (https://github.com/settings/tokens). Dans les configurations d'entreprise, cela peut être étendu aux jetons au niveau de l'organisation ou utilisé dans les pipelines CI/CD en ajoutant `permissions: models: read` aux fichiers YAML de workflow. Les modèles disponibles incluent des standards de l'industrie comme `openai/gpt-4o`, `openai/gpt-4o-mini`, `anthropic/claude-3-5-sonnet-20240620`, la série Llama 3.1 de Meta, et les variantes Mistral, tous invocables via le même format d'API compatible OpenAI. Cette compatibilité facilite son intégration dans votre configuration de routeur sans modifications majeures du code en aval.

Pour les configurations spécifiques à l'entreprise, GitHub Copilot Enterprise améliore le Copilot standard avec des contrôles à l'échelle de l'organisation, tels que des modèles affinés basés sur votre base de code, mais l'accès API suit les mêmes modèles. La gestion du réseau est cruciale : Vous pouvez configurer le routage basé sur l'abonnement pour garantir que le trafic Copilot utilise des chemins approuvés, nécessitant que les utilisateurs mettent à jour leurs extensions d'IDE (par exemple, VS Code) vers des versions minimales prenant en charge cette fonctionnalité. Si votre environnement impose des proxys, mettez à jour la "PROXY_URL" de la configuration pour pointer vers votre serveur proxy d'entreprise, et envisagez des certificats personnalisés pour l'inspection SSL. Des outils comme LiteLLM peuvent agir comme un proxy intermédiaire pour un contrôle supplémentaire—installez-les via `pip install litellm[proxy]`, définissez les modèles dans une configuration YAML, démarrez le serveur sur un port local, et redirigez les requêtes Copilot via celui-ci pour la journalisation, la limitation du débit et la gestion des replis. Cependant, dans votre cas, puisque l'objectif est l'exclusivité, évitez les replis dans le routeur pour vous conformer aux politiques "uniquement autorisé à appeler Copilot".

Pour implémenter cela dans votre configuration, commencez par ajouter un nouvel objet fournisseur. Choisissez le point de terminaison en fonction de votre cas d'utilisation : Utilisez le point de terminaison d'agent Copilot si vous construisez des extensions, ou GitHub Models pour un routage LLM général. Listez les modèles qui chevauchent ceux existants (par exemple, les variantes Claude et GPT) pour maintenir la compatibilité. Ensuite, remplacez tous les champs de "Router" pour qu'ils ne référencent que ce nouveau fournisseur, en éliminant les virgules ou les replis comme ",minimax/minimax-m2". Activez la journalisation pour surveiller la conformité, et testez en simulant des requêtes pour vérifier qu'aucun point de terminaison non autorisé n'est atteint. Si vous intégrez avec VS Code ou d'autres IDE, ajustez les paramètres comme `github.copilot.advanced.debug.overrideProxyUrl` pour router via votre proxy configuré si nécessaire.

Voici un tableau comparatif des deux principales options d'API LLM de GitHub pour vous aider à décider quel point de terminaison utiliser dans votre configuration de fournisseur :

| Aspect                  | API LLM GitHub Copilot (pour les Agents)            | API GitHub Models                                   |
|-------------------------|-----------------------------------------------------|-----------------------------------------------------|
| Point de terminaison    | https://api.githubcopilot.com/chat/completions      | https://models.github.ai/inference/chat/completions |
| Utilisation Principale  | Construction d'extensions et d'agents Copilot       | Prototypage général, inférence et workflows         |
| Authentification        | PAT Bearer (via en-tête Authorization)              | PAT avec le scope models:read                       |
| Modèles Supportés       | Implicites (par ex., GPT-4, variantes Claude)       | Catalogue explicite : gpt-4o, claude-3-5-sonnet, Llama 3.1, etc. |
| Fonctionnalités Entreprise | Limites de taux pour les tiers ; intègre Copilot Enterprise | Utilisable dans GitHub Actions ; support apportez votre propre clé |
| Limites de Taux/Quotas  | Strictes pour les agents non-GitHub                 | Niveau gratuit pour le prototypage ; évolutif pour l'entreprise |
| Compatibilité           | Format de chat OpenAI                               | Compatible OpenAI ; intégration facile dans le routeur |

Ce tableau souligne pourquoi GitHub Models pourrait être préférable pour une utilisation large du routeur, car il offre une sélection de modèles plus explicite et une intégration dans les workflows d'entreprise.

Les défis potentiels incluent l'expiration des jetons (les PAT durent généralement 30 à 90 jours), donc automatisez le renouvellement dans les scripts d'entreprise. Si votre environnement utilise GitHub Enterprise Cloud, activez Copilot au niveau de l'organisation pour un accès transparent. Pour les configurations avancées, explorez l'apport de vos propres clés API (BYOK) dans GitHub Models pour router via les fournisseurs préférés tout en restant dans l'écosystème GitHub. Priorisez toujours la documentation principale de GitHub pour les derniers scopes et points de terminaison, car les fonctionnalités évoluent rapidement. Si les appels API directs échouent en raison de restrictions réseau, envisagez d'utiliser les options de configuration de proxy de GitHub ou l'intégration avec Azure pour les déploiements d'entreprise hybrides.

En résumé, cette configuration transforme votre routeur en un système exclusif à Copilot, s'alignant sur les politiques d'entreprise tout en maintenant la fonctionnalité pour les tâches liées au code ou les tâches LLM générales.

**Citations Clés :**
- [Using GitHub Copilot's LLM for your agent](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-extensions/build-a-copilot-agent/use-copilots-llm)
- [Quickstart for GitHub Models](https://docs.github.com/en/github-models/quickstart)
- [GitHub Copilot | liteLLM](https://docs.litellm.ai/docs/tutorials/github_copilot_integration)
- [Managing GitHub Copilot access to your enterprise's network](https://docs.github.com/enterprise-cloud%40latest/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-access/manage-network-access)
- [Configuring network settings for GitHub Copilot](https://docs.github.com/copilot/configuring-github-copilot/configuring-network-settings-for-github-copilot)
- [Prototyping with AI models](https://docs.github.com/github-models/prototyping-with-ai-models)
- [Using your own API keys in GitHub Models](https://docs.github.com/en/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)