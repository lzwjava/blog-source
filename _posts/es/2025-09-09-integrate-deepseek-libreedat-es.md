---
audio: false
date: 2025-09-09
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Guía para integrar DeepSeek con LibreChat
translated: true
type: note
---

Aquí tienes la forma más rápida de **hacer que DeepSeek funcione en LibreChat**. Te mostraré dos opciones: usa la **API oficial de DeepSeek** (recomendado) o ve a través de **OpenRouter**.

---

## Opción A — Usar la API oficial de DeepSeek (recomendado)

1.  **Obtén una clave API de DeepSeek**
    Crea una en tu cuenta de DeepSeek, luego anota la URL base:
    `https://api.deepseek.com` (o la compatible con OpenAI `https://api.deepseek.com/v1`). ([Documentos de la API de DeepSeek][1], [deepseek.apidog.io][2])

2.  **Agrega un endpoint de DeepSeek en `librechat.yaml`**
    Coloca esto bajo `endpoints:` → `custom:`:

```yaml
- name: deepseek
  apiKey: ${DEEPSEEK_API_KEY}
  baseURL: https://api.deepseek.com/v1
  models:
    default: deepseek-chat
    fetch: true
    list:
      - deepseek-chat        # V3 (general)
      - deepseek-coder       # centrado en código
      - deepseek-reasoner    # R1 reasoning
  titleConvo: true
  dropParams: null
```

LibreChat incluye una guía de configuración para **DeepSeek** y confirma los nombres de los modelos (`deepseek-chat`, `deepseek-coder`, `deepseek-reasoner`) y notas sobre R1 transmitiendo su "proceso de pensamiento". ([LibreChat][3])

3.  **Expone la clave API a través de `.env`**
    En tu archivo `.env` de LibreChat:

```
DEEPSEEK_API_KEY=sk-...
```

LibreChat admite proveedores personalizados compatibles con OpenAI a través de `librechat.yaml` + `.env`. ([LibreChat][4])

4.  **Reinicia tu stack**
    Desde tu carpeta de LibreChat:

```bash
docker compose down
docker compose up -d --build
```

(Es necesario para que el contenedor de la API recargue `librechat.yaml` y `.env`). Si tus endpoints personalizados no aparecen, revisa los logs del contenedor `api` en busca de errores de configuración. ([GitHub][5])

---

## Opción B — Usar DeepSeek a través de OpenRouter

Si ya usas OpenRouter, simplemente registra los modelos de DeepSeek en un bloque de endpoint de OpenRouter.

`librechat.yaml`:

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

Dos notas importantes de la documentación de LibreChat:
• No configures el nombre de la variable de entorno `OPENROUTER_API_KEY` (usa un nombre diferente como `OPENROUTER_KEY`) o accidentalmente anularás el endpoint de OpenAI.
• OpenRouter es de primera clase en la lista de endpoints personalizados de LibreChat. ([LibreChat][6])

OpenRouter expone los modelos de DeepSeek con una superficie compatible con OpenAI. ([OpenRouter][7])

---

## Consejos y advertencias

*   **R1 / `deepseek-reasoner`**: Puede transmitir su cadena de pensamiento ("proceso de pensamiento"). Algunos parámetros de OpenAI pueden no aplicar. Si ves una salida extraña, prueba primero con `deepseek-chat`. ([LibreChat][3])
*   **Obtención de modelos**: Configurar `fetch: true` permite que LibreChat obtenga la lista de modelos más reciente cuando sea compatible; de lo contrario, se usa la `list:` que especifiques. ([LibreChat][8])
*   **Dónde viven estas configuraciones**: `librechat.yaml` es el archivo de endpoints personalizados; `.env` contiene las claves y configuraciones de proxy. ([LibreChat][8])

Si quieres, pega tu `librechat.yaml` actual y lo modificaré para agregar DeepSeek de forma limpia (sin tablas, lo prometo).

[1]: https://api-docs.deepseek.com/?utm_source=chatgpt.com "DeepSeek API Docs: Your First API Call"
[2]: https://deepseek.apidog.io/your-first-api-call-835227m0?utm_source=chatgpt.com "DeepSeek API: Your First API Call"
[3]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/deepseek?utm_source=chatgpt.com "Deepseek"
[4]: https://www.librechat.ai/docs/quick_start/custom_endpoints?utm_source=chatgpt.com "Custom Endpoints"
[5]: https://github.com/danny-avila/LibreChat/discussions/2487?utm_source=chatgpt.com "Fix the librechat.yaml file in the main repository. #2487"
[6]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/openrouter?utm_source=chatgpt.com "Openrouter"
[7]: https://openrouter.ai/deepseek/deepseek-v3-base%3Afree/api?utm_source=chatgpt.com "DeepSeek V3 Base – Run with an API"
[8]: https://www.librechat.ai/docs/configuration/librechat_yaml?utm_source=chatgpt.com "librechat.yaml config file"