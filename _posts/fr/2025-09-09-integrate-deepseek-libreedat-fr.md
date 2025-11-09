---
audio: false
date: 2025-09-09
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Guide d'intégration de DeepSeek avec LibreChat
translated: true
type: note
---

Voici le moyen le plus rapide de faire fonctionner **DeepSeek dans LibreChat**. Je vais présenter deux options — utilisez l'**API officielle de DeepSeek** (recommandé), ou passez par **OpenRouter**.

---

## Option A — Utiliser l'API officielle de DeepSeek (recommandé)

1.  **Obtenez une clé API DeepSeek**
    Créez-en une dans votre compte DeepSeek, puis notez l'URL de base :
    `https://api.deepseek.com` (ou la version compatible OpenAI `https://api.deepseek.com/v1`). ([Documentation de l'API DeepSeek][1], [deepseek.apidog.io][2])

2.  **Ajoutez un endpoint DeepSeek dans `librechat.yaml`**
    Placez ceci sous `endpoints:` → `custom:` :

```yaml
- name: deepseek
  apiKey: ${DEEPSEEK_API_KEY}
  baseURL: https://api.deepseek.com/v1
  models:
    default: deepseek-chat
    fetch: true
    list:
      - deepseek-chat        # V3 (général)
      - deepseek-coder       # axé sur le code
      - deepseek-reasoner    # R1 raisonnement
  titleConvo: true
  dropParams: null
```

LibreChat fournit un guide de configuration **DeepSeek** et confirme les noms des modèles (`deepseek-chat`, `deepseek-coder`, `deepseek-reasoner`) ainsi que des notes concernant le streaming du "processus de pensée" de R1. ([LibreChat][3])

3.  **Exposez la clé API via `.env`**
    Dans votre fichier `.env` de LibreChat :

```
DEEPSEEK_API_KEY=sk-...
```

LibreChat prend en charge les fournisseurs compatibles OpenAI personnalisés via `librechat.yaml` + `.env`. ([LibreChat][4])

4.  **Redémarrez votre stack**
    Depuis votre dossier LibreChat :

```bash
docker compose down
docker compose up -d --build
```

(Nécessaire pour que le conteneur API recharge `librechat.yaml` et `.env`.) Si vos endpoints personnalisés n'apparaissent pas, vérifiez les logs du conteneur `api` pour détecter les erreurs de configuration. ([GitHub][5])

---

## Option B — Utiliser DeepSeek via OpenRouter

Si vous utilisez déjà OpenRouter, il suffit d'enregistrer les modèles DeepSeek dans un bloc d'endpoint OpenRouter.

`librechat.yaml` :

```yaml
- name: openrouter
  apiKey: ${OPENROUTER_KEY}
  baseURL: https://openrouter.ai/api/v1
  models:
    default: deepseek/deepseek-chat
    list:
      - deepseek/deepseek-chat
      - deepseek/deepseek-coder
      - deepseek/deepseek-reasoner
```

Deux notes importantes de la documentation LibreChat :
• Ne définissez pas le nom de variable d'environnement `OPENROUTER_API_KEY` (utilisez un nom différent comme `OPENROUTER_KEY`) sinon vous écraserez accidentellement l'endpoint OpenAI.
• OpenRouter est un endpoint personnalisé de premier ordre dans la liste de LibreChat. ([LibreChat][6])

OpenRouter expose les modèles DeepSeek avec une interface compatible OpenAI. ([OpenRouter][7])

---

## Conseils et pièges courants

*   **R1 / `deepseek-reasoner`** : Il peut streamer son raisonnement en chaîne ("processus de pensée"). Certains paramètres OpenAI peuvent ne pas s'appliquer. Si vous observez un résultat étrange, testez d'abord avec `deepseek-chat`. ([LibreChat][3])
*   **Récupération des modèles** : Définir `fetch: true` permet à LibreChat de récupérer la liste des modèles la plus récente lorsque c'est pris en charge ; sinon, la `list:` que vous spécifiez est utilisée. ([LibreChat][8])
*   **Où se trouvent ces paramètres** : `librechat.yaml` est le fichier des endpoints personnalisés ; `.env` contient les clés et les paramètres de proxy. ([LibreChat][8])

Si vous le souhaitez, collez votre `librechat.yaml` actuel et je l'adapterai pour ajouter DeepSeek proprement (pas de tableaux, promis).

[1]: https://api-docs.deepseek.com/?utm_source=chatgpt.com "DeepSeek API Docs: Your First API Call"
[2]: https://deepseek.apidog.io/your-first-api-call-835227m0?utm_source=chatgpt.com "DeepSeek API: Your First API Call"
[3]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/deepseek?utm_source=chatgpt.com "Deepseek"
[4]: https://www.librechat.ai/docs/quick_start/custom_endpoints?utm_source=chatgpt.com "Custom Endpoints"
[5]: https://github.com/danny-avila/LibreChat/discussions/2487?utm_source=chatgpt.com "Fix the librechat.yaml file in the main repository. #2487"
[6]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/openrouter?utm_source=chatgpt.com "Openrouter"
[7]: https://openrouter.ai/deepseek/deepseek-v3-base%3Afree/api?utm_source=chatgpt.com "DeepSeek V3 Base – Run with an API"
[8]: https://www.librechat.ai/docs/configuration/librechat_yaml?utm_source=chatgpt.com "librechat.yaml config file"