---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Configuration du routage du code Claude DeepSeek
translated: true
type: note
---

Compris. Votre configuration envoie **le trafic de style Anthropic de Claude Code** vers **le endpoint de style OpenAI d'OpenRouter** pour DeepSeek V3.1. Lorsque Claude Code (l'agent IDE) tente d'utiliser tools/plan/stream, le schéma de message ne correspond pas → erreurs.

Voici une méthode propre pour câbler le système afin que **les modèles Anthropic** utilisent toujours une passerelle de style Anthropic, tandis que **DeepSeek V3.1** (style OpenAI) reste sur `/chat/completions`. Je vais montrer les modifications exactes que vous pouvez coller.

---

### 1) Vérifiez le slug de DeepSeek V3.1

Le slug du modèle de chat sur OpenRouter est :

```
deepseek/deepseek-chat-v3.1
```

(C'est le modèle instruct/chat—distinct du modèle "base".) ([OpenRouter][1])

---

### 2) Ajoutez un proxy au format Anthropic pour Claude Code

Claude Code attend des **Messages Anthropic** (`/messages`, blocs `tool_use`). La solution la plus simple est d'exécuter un petit proxy qui convertit Anthropic→OpenAI (OpenRouter) et vice versa. Il en existe un prêt à l'emploi : **maxnowack/anthropic-proxy**. Démarrez-le comme ceci (la variable d'environnement est votre clé OpenRouter) :

```bash
OPENROUTER_API_KEY=VOTRE_CLÉ npx anthropic-proxy
```

Il écoute localement et traduit les schémas pour vous. ([GitHub][2])

Maintenant, ajoutez un **second fournisseur** qui redirige le trafic de Claude Code vers ce proxy.

#### 🔧 Remplacez votre JSON par ces modifications ciblées

**Ajoutez ce fournisseur (conservez votre fournisseur `openrouter` actuel tel quel) :**

```json
{
  "name": "anthropic-proxy",
  "api_base_url": "http://127.0.0.1:3000/v1/messages",
  "api_key": "", 
  "models": [
    "anthropic/claude-sonnet-4",
    "anthropic/claude-3.5-sonnet",
    "anthropic/claude-3.7-sonnet:thinking",
    "anthropic/claude-opus-4"
  ]
}
```

**Conservez votre fournisseur OpenRouter existant (il est correct d'utiliser `/chat/completions` pour DeepSeek et les autres modèles au schéma OpenAI).** OpenRouter normalise vers un schéma compatible OpenAI et prend en charge des extras comme les tokens de raisonnement, les outils, etc. ([OpenRouter][3])

---

### 3) Routez les modèles vers le bon fournisseur

Dirigez les modèles Anthropic vers **anthropic-proxy** ; dirigez DeepSeek/GPT/Gemini/Qwen vers **openrouter**.

Exemple de bloc Router que vous pouvez insérer :

```json
"Router": {
  "default": "openrouter,openai/gpt-5-mini",

  "background": "openrouter,google/gemini-2.5-flash",
  "think": "openrouter,qwen/qwen3-coder",
  "longContext": "openrouter,moonshotai/kimi-k2",
  "longContextThreshold": 2000,
  "webSearch": "openrouter,mistralai/mistral-medium-3.1",

  "overrides": {
    "anthropic/claude-sonnet-4": "anthropic-proxy,anthropic/claude-sonnet-4",
    "anthropic/claude-3.5-sonnet": "anthropic-proxy,anthropic/claude-3.5-sonnet",
    "anthropic/claude-3.7-sonnet:thinking": "anthropic-proxy,anthropic/claude-3.7-sonnet:thinking",
    "anthropic/claude-opus-4": "anthropic-proxy,anthropic/claude-opus-4",

    "deepseek/deepseek-chat-v3.1": "openrouter,deepseek/deepseek-chat-v3.1"
  }
}
```

> Si votre routeur ne prend pas en charge une carte `overrides`, l'équivalent est : créez des "profils" distincts dans votre application (par exemple, "Claude Code via anthropic-proxy" vs "Chat général via openrouter") et choisissez le profil par action.

---

### 4) Évitez les collisions de flux de raisonnement sur DeepSeek (optionnel mais plus sûr)

DeepSeek V3.1 prend en charge les **tokens de "raisonnement"**. De nombreux wrappers plantent s'ils apparaissent en milieu de flux. Sur OpenRouter, vous pouvez **exclure le raisonnement** avec un drapeau de requête. Si votre routeur vous permet de définir des paramètres par modèle, ajoutez :

```json
"params": {
  "reasoning": { "exclude": true }
}
```

(ou `include_reasoning: false` selon la nomenclature des paramètres de votre routeur). Cela empêche le contenu `